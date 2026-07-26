#!/usr/bin/env python3
"""
structural-scan.py - discourse-level AI-writing tells (Pass 2).

Companion to banned-pattern-scan.py, which covers word and sentence level (Pass 1).
This one works ABOVE the sentence: how emotion is rendered, whether the lesson is
stated for the reader, whether references are checkable, how tidily the piece closes.

Why this exists: StoryScope (Russell et al. 2026, arXiv:2604.03136) detected AI text
at 93.2% macro F1 from narrative structure alone with every style feature withheld.
Running AI text through a professional surface rewriter moved detection 1.6 points.
Word-level scanning covers the cheap half of the problem.

DEFAULT IS ADVISORY. Exit 0 always, print a report. Use --strict to exit 1 when a
category reaches the threshold (for a pre-publish gate on outward-facing content only).
Applied to internal docs and plans it will fire on text nobody needs to sound human.

Categories are thresholded, not zero-tolerance: one embodied-emotion line in a 2,000
word post is a choice, four is a tell.

Suppress a deliberate line by putting `structural-ignore` in it.

Usage:
    structural-scan.py FILE [FILE ...]
    structural-scan.py --json FILE
    structural-scan.py --strict FILE     # exit 1 if any category hits threshold
    cat draft.md | structural-scan.py -
"""

import argparse
import json
import re
import statistics
import sys

# Hits per category, per document, before --strict fails.
THRESHOLD = 2

PRONOUN = r"(?:my|his|her|their|its|the)"

CATEGORIES = {
    "embodied_emotion": {
        "why": "AI performs emotion through the body 81% of the time vs 38% for humans. Name the feeling plainly instead; reserve one embodied moment for where it is earned.",
        "patterns": [
            rf"\b{PRONOUN}\s+(?:chest|throat|jaw|stomach|gut|shoulders?|hands?|fingers?)\s+"
            rf"(?:tighten|clench|knot|drop|sink|sag|constrict|seize|flip|turn|twist|churn|tremble|shake)\w*",
            rf"\b{PRONOUN}\s+(?:heart|pulse)\s+(?:raced?|hammer|pound|skip|quicken|stutter)\w*",
            r"\b(?:a|the)\s+(?:knot|lump|weight|chill|warmth)\s+(?:in|on)\s+(?:my|his|her|their)\s+"
            r"(?:stomach|throat|chest|gut|shoulders?)",
            r"\bbreath\s+(?:I|he|she|they)\s+(?:did\s?n.t|had\s?n.t)\s+(?:know|known|realize|realized)\b",
            r"\b(?:let|blew|released)\s+out\s+(?:a|the)\s+(?:breath|sigh)\b",
            r"\b(?:swallowed|choked back|blinked back)\s+(?:hard|the|a)\b",
            r"\b(?:something|the air)\s+(?:shifted|changed|settled)\s+in\s+(?:the room|me|my chest)\b",
        ],
    },
    "stated_lesson": {
        "why": "The narrator states the theme 77% of the time in AI text vs 52% human. State the point once where it lands hardest, then cut every restatement and leave at least one example uninterpreted.",
        "patterns": [
            r"\bthe\s+(?:real\s+)?(?:bottom\s+line|takeaway|lesson\s+here)\b",
            r"\bwhat\s+this\s+(?:really\s+)?means\s+for\s+you\b",
            r"\bthe\s+point\s+(?:here\s+)?is\s+(?:this|that)\b",
            r"\b(?:and\s+)?that.s\s+(?:exactly\s+)?(?:the|my)\s+(?:point|lesson|whole point)\b",
            r"\bwhich\s+brings\s+(?:me|us)\s+(?:back\s+)?to\b",
            r"\bthe\s+(?:bigger|broader|deeper)\s+(?:lesson|truth|principle)\b",
            r"\bif\s+(?:there.s|there\s+is)\s+one\s+thing\s+(?:to\s+take|you\s+take|I.d\s+want)\b",
            r"\bwhat\s+I\s+(?:learned|took\s+away)\s+(?:from\s+this\s+)?is\b",
        ],
    },
    "vague_allusion": {
        "why": "Humans use named, checkable references 47% of the time vs 24% for AI. Swap every vague allusion for a name, price, version, date or place.",
        "patterns": [
            r"\bstudies\s+(?:show|suggest|have\s+shown|indicate|found)\b",
            r"\b(?:a|one)\s+(?:recent|popular|well-known|leading|major)\s+"
            r"(?:study|book|article|report|survey|tool|platform|company)\b",
            r"\b(?:experts|researchers|analysts)\s+(?:say|agree|suggest|believe)\b",
            r"\b(?:many|most|some)\s+(?:experts|marketers|founders|companies|businesses)\s+(?:say|believe|agree|think)\b",
            r"\bresearch\s+(?:shows|suggests|has\s+shown)\b",
            r"\bit.s\s+(?:widely|well)\s+(?:known|documented|understood)\b",
            r"\b(?:industry|market)\s+data\s+(?:shows|suggests)\b",
        ],
    },
    # Matched ONLY in the final two paragraphs. A tidy bow is the single most
    # reliable Claude fingerprint (the epilogue habit).
    "tidy_closer": {
        "why": "AI resolves cleanly far more often than humans, and Claude specifically adds a wrap-up coda after the natural ending. Cut the coda; sometimes stop on the spike.",
        "closing_only": True,
        "patterns": [
            r"\bat\s+the\s+end\s+of\s+the\s+day\b",
            r"\bone\s+thing\s+is\s+(?:clear|certain)\b",
            r"\bthe\s+(?:future|journey|road\s+ahead)\s+(?:is|looks|remains)\b",
            r"\bwhatever\s+(?:you|path\s+you)\s+(?:choose|decide|take)\b",
            r"\bstart\s+(?:small|today|now)(?:,|\.|\s+and)\b",
            r"\bthe\s+rest\s+(?:will\s+)?follows?\b",
            r"\b(?:so|now)\s+go\s+(?:and\s+)?(?:build|do|try|make)\b",
            r"\bit.s\s+(?:that\s+)?simple\b",
            r"\bhappy\s+(?:building|writing|shipping|hunting)\b",
        ],
    },
}

# Strip fenced code, inline code, HTML, YAML frontmatter, and markdown link targets
# so the scanner never fires on machinery instead of prose.
FENCE_RE = re.compile(r"```.*?```", re.S)
INLINE_CODE_RE = re.compile(r"`[^`]*`")
HTML_RE = re.compile(r"<script.*?</script>|<style.*?</style>|<[^>]+>", re.S | re.I)
FRONTMATTER_RE = re.compile(r"\A---\n.*?\n---\n", re.S)
LINK_TARGET_RE = re.compile(r"\]\([^)]*\)")


def clean(text):
    """Remove machinery, preserving character offsets is not needed; we report line numbers
    off the ORIGINAL text, so keep a parallel line-preserving version."""
    out = FRONTMATTER_RE.sub(lambda m: "\n" * m.group(0).count("\n"), text)
    out = FENCE_RE.sub(lambda m: "\n" * m.group(0).count("\n"), out)
    out = HTML_RE.sub(lambda m: "\n" * m.group(0).count("\n"), out)
    out = INLINE_CODE_RE.sub(" ", out)
    out = LINK_TARGET_RE.sub("]", out)
    return out


def paragraphs(text):
    """Prose paragraphs only: drop headings, list items, blockquotes, tables."""
    blocks = [b.strip() for b in re.split(r"\n\s*\n", text) if b.strip()]
    out = []
    for b in blocks:
        first = b.lstrip()[:2]
        if first.startswith("#") or first.startswith("|"):
            continue
        if re.match(r"^\s*(?:[-*+]|\d+\.|>)\s", b):
            continue
        out.append(b)
    return out


def closing_span(text):
    """Character offset where the final two prose paragraphs begin."""
    paras = paragraphs(text)
    if len(paras) < 3:
        return 0
    anchor = paras[-2]
    idx = text.rfind(anchor)
    return idx if idx != -1 else 0


def line_of(text, offset):
    return text.count("\n", 0, offset) + 1


def sentence_at(text, offset, width=160):
    start = max(text.rfind(".", 0, offset), text.rfind("\n", 0, offset)) + 1
    end = text.find(".", offset)
    end = len(text) if end == -1 else end + 1
    return " ".join(text[start:end].split())[:width]


def scan(text):
    cleaned = clean(text)
    lines = text.split("\n")
    ignored = {i + 1 for i, ln in enumerate(lines) if "structural-ignore" in ln}
    close_start = closing_span(cleaned)

    hits = []
    counts = {}
    for name, spec in CATEGORIES.items():
        counts[name] = 0
        for pat in spec["patterns"]:
            for m in re.finditer(pat, cleaned, re.I):
                if spec.get("closing_only") and m.start() < close_start:
                    continue
                ln = line_of(cleaned, m.start())
                if ln in ignored:
                    continue
                hits.append(
                    {
                        "category": name,
                        "match": m.group(0).strip(),
                        "line": ln,
                        "sentence": sentence_at(cleaned, m.start()),
                    }
                )
                counts[name] += 1

    return hits, counts, metrics(cleaned)


def metrics(cleaned):
    """Two cheap non-regex signals. Informational only, never fail --strict on these."""
    paras = paragraphs(cleaned)
    words = re.findall(r"\b[\w'-]+\b", cleaned)
    wc = len(words)
    out = {"word_count": wc, "paragraph_count": len(paras)}

    if len(paras) >= 5:
        lengths = [len(re.findall(r"\b[\w'-]+\b", p)) for p in paras]
        mean = statistics.mean(lengths)
        if mean > 0:
            cv = statistics.pstdev(lengths) / mean
            out["paragraph_length_cv"] = round(cv, 3)
            out["uniform_paragraphs"] = cv < 0.35

    numbers = re.findall(r"(?<![\w-])\d[\d,.]*(?![\w-])", cleaned)
    out["numbers"] = len(numbers)
    if wc >= 300:
        out["numbers_per_100w"] = round(len(numbers) * 100 / wc, 2)
        out["no_specifics"] = len(numbers) == 0

    return out


def report(path, hits, counts, mets, threshold):
    over = {k: v for k, v in counts.items() if v >= threshold}
    total = len(hits)

    print(f"\n=== {path} ===")
    print(f"{mets['word_count']} words, {mets['paragraph_count']} prose paragraphs")

    if not total:
        print("No structural tells found.")
    else:
        for name in CATEGORIES:
            cat_hits = [h for h in hits if h["category"] == name]
            if not cat_hits:
                continue
            flag = "  [OVER THRESHOLD]" if counts[name] >= threshold else ""
            print(f"\n{name} ({counts[name]}){flag}")
            print(f"  why: {CATEGORIES[name]['why']}")
            for h in cat_hits[:6]:
                print(f"  L{h['line']}: \"{h['match']}\"")
                print(f"      {h['sentence']}")
            if len(cat_hits) > 6:
                print(f"  ... {len(cat_hits) - 6} more")

    notes = []
    if mets.get("uniform_paragraphs"):
        notes.append(
            f"paragraph lengths are uniform (CV {mets['paragraph_length_cv']} < 0.35); real writing varies hard"
        )
    if mets.get("no_specifics"):
        notes.append(f"{mets['word_count']} words and zero numbers; add a name, price, date or version")
    if notes:
        print("\nmetrics:")
        for n in notes:
            print(f"  - {n}")

    return over


def main():
    ap = argparse.ArgumentParser(description="Discourse-level AI-writing tells (Pass 2).")
    ap.add_argument("files", nargs="+", help="files to scan, or - for stdin")
    ap.add_argument("--json", action="store_true", help="machine-readable output")
    ap.add_argument("--json-only", action="store_true", help="json, no report (for hooks)")
    ap.add_argument("--strict", action="store_true", help="exit 1 if a category hits the threshold")
    ap.add_argument("--threshold", type=int, default=THRESHOLD, help=f"hits per category (default {THRESHOLD})")
    args = ap.parse_args()

    failed = False
    results = []

    for path in args.files:
        try:
            text = sys.stdin.read() if path == "-" else open(path, encoding="utf-8", errors="replace").read()
        except OSError as e:
            print(f"cannot read {path}: {e}", file=sys.stderr)
            continue

        hits, counts, mets = scan(text)
        over = {k: v for k, v in counts.items() if v >= args.threshold}

        if not (args.json or args.json_only):
            report(path, hits, counts, mets, args.threshold)
        results.append(
            {"file": path, "hits": hits, "counts": counts, "metrics": mets, "over_threshold": over, "total": len(hits)}
        )
        if over:
            failed = True

    if args.json or args.json_only:
        print(json.dumps(results if len(results) > 1 else results[0], indent=2))

    sys.exit(1 if (failed and args.strict) else 0)


if __name__ == "__main__":
    main()
