#!/usr/bin/env python3
"""
shape-convergence.py - does this draft repeat the skeleton of recent pieces?

Audit 6 of the structural pass, and the only check in the chain that looks
outside the current document. Every piece can pass every word-level and
sentence-level rule on its own while the body of work still reads as machine-made,
because all of them share one shape.

Grounded in the StoryScope convergence finding: all five models tested occupied one
tight region of structural space (AI-to-AI centroid distance 4.3) while humans were
dispersed (human-to-AI 6.6). Human mean rarity percentile 0.71 against AI 0.49.
Rarity is the signal, so repetition of your own template is the thing to catch.

This is a deterministic backstop, not a verdict. It measures the shape features that
can be counted. A model reading the outlines side by side catches what counting
cannot, so run audit 6 by hand as well when the stakes are high.

Usage:
    shape-convergence.py DRAFT --against RECENT1 RECENT2 RECENT3
    shape-convergence.py DRAFT --against-dir ~/path/to/published/
    shape-convergence.py DRAFT --against-dir DIR --json
"""

import argparse
import glob
import json
import os
import re
import statistics
import sys

# Similarity at or above this is flagged as a repeated shape.
SIMILARITY_FLAG = 0.85

FENCE_RE = re.compile(r"```.*?```", re.S)
FRONTMATTER_RE = re.compile(r"\A---\n.*?\n---\n", re.S)
HTML_RE = re.compile(r"<[^>]+>")

CLOSER_RE = re.compile(
    r"\b(at the end of the day|one thing is (clear|certain)|start (small|today|now)"
    r"|the rest (will )?follows?|it.s (that )?simple|whatever you (choose|decide))\b",
    re.I,
)


def clean(text):
    out = FRONTMATTER_RE.sub("", text)
    out = FENCE_RE.sub("", out)
    out = HTML_RE.sub(" ", out)
    return out


def blocks(text):
    out = []
    for b in re.split(r"\n\s*\n", text):
        b = b.strip()
        if b:
            out.append(b)
    return out


def is_heading(b):
    return b.lstrip().startswith("#")


def is_list(b):
    return bool(re.match(r"^\s*(?:[-*+]|\d+\.)\s", b))


def prose(text):
    return [b for b in blocks(text) if not is_heading(b) and not is_list(b) and not b.startswith("|")]


def words(s):
    return re.findall(r"\b[\w'-]+\b", s)


def opening_move(paras):
    """How the piece starts. AI converges hard on a small set of openers."""
    if not paras:
        return "none"
    first = paras[0].strip()
    sent = re.split(r"(?<=[.!?])\s", first)[0]
    if sent.rstrip().endswith("?"):
        return "question"
    if re.match(r"^\s*[\"“']", sent):
        return "quote"
    if re.match(r"^\s*\d|\b\d+%|\$\d", sent):
        return "number"
    if re.match(r"^\s*(I|My|We)\b", sent):
        return "first-person"
    if re.match(r"^\s*(If|When|Imagine|Picture|Think|Consider|Stop|Try)\b", sent, re.I):
        return "imperative-or-conditional"
    if re.match(r"^\s*(Most|Everyone|Nobody|Every|All)\b", sent, re.I):
        return "sweeping-claim"
    return "declarative"


def closing_move(paras):
    if not paras:
        return "none"
    last = paras[-1]
    if CLOSER_RE.search(last):
        return "tidy-closer"
    if last.rstrip().endswith("?"):
        return "question"
    if re.search(r"\b\d", last):
        return "number"
    if re.match(r"^\s*(So|Now|Go|Start|Try)\b", last, re.I):
        return "call-to-action"
    return "declarative"


def signature(path, text):
    c = clean(text)
    all_blocks = blocks(c)
    paras = prose(c)
    wc = len(words(c))

    para_lens = [len(words(p)) for p in paras] or [0]
    sents = [s for s in re.split(r"(?<=[.!?])\s+", " ".join(paras)) if s.strip()]
    sent_lens = [len(words(s)) for s in sents] or [0]

    def cv(xs):
        m = statistics.mean(xs)
        return round(statistics.pstdev(xs) / m, 3) if m else 0.0

    return {
        "file": path,
        "word_count": wc,
        "paragraphs": len(paras),
        "headings": sum(1 for b in all_blocks if is_heading(b)),
        "lists": sum(1 for b in all_blocks if is_list(b)),
        "avg_para_words": round(statistics.mean(para_lens), 1),
        "para_cv": cv(para_lens),
        "avg_sentence_words": round(statistics.mean(sent_lens), 1),
        "sentence_cv": cv(sent_lens),
        "numbers_per_100w": round(len(re.findall(r"(?<![\w-])\d[\d,.]*(?![\w-])", c)) * 100 / wc, 2) if wc else 0,
        "opening_move": opening_move(paras),
        "closing_move": closing_move(paras),
        "heading_ratio": round(sum(1 for b in all_blocks if is_heading(b)) / len(all_blocks), 3) if all_blocks else 0,
        "list_ratio": round(sum(1 for b in all_blocks if is_list(b)) / len(all_blocks), 3) if all_blocks else 0,
    }


# Numeric features compared as a normalised vector.
NUMERIC = [
    ("paragraphs", 30),
    ("avg_para_words", 60),
    ("para_cv", 1.0),
    ("avg_sentence_words", 30),
    ("sentence_cv", 1.0),
    ("numbers_per_100w", 5),
    ("heading_ratio", 1.0),
    ("list_ratio", 1.0),
]


def similarity(a, b):
    """1.0 = identical shape. Numeric closeness plus categorical opening/closing match."""
    diffs = []
    for key, scale in NUMERIC:
        d = abs(a[key] - b[key]) / scale
        diffs.append(min(d, 1.0))
    numeric_sim = 1 - (sum(diffs) / len(diffs))

    cat = 0
    cat += 1 if a["opening_move"] == b["opening_move"] else 0
    cat += 1 if a["closing_move"] == b["closing_move"] else 0
    cat_sim = cat / 2

    # Openings and closings are the most visible repetition to a reader, so weight them.
    return round(0.6 * numeric_sim + 0.4 * cat_sim, 3)


def load(path):
    with open(path, encoding="utf-8", errors="replace") as fh:
        return fh.read()


def main():
    ap = argparse.ArgumentParser(description="Does this draft repeat the shape of recent pieces?")
    ap.add_argument("draft")
    ap.add_argument("--against", nargs="*", default=[], help="recent pieces in the same channel")
    ap.add_argument("--against-dir", help="directory of recent pieces (md/txt)")
    ap.add_argument("--flag-at", type=float, default=SIMILARITY_FLAG, help=f"similarity to flag (default {SIMILARITY_FLAG})")
    ap.add_argument("--json", action="store_true")
    args = ap.parse_args()

    refs = list(args.against)
    if args.against_dir:
        for ext in ("*.md", "*.txt", "*.mdx"):
            refs.extend(glob.glob(os.path.join(os.path.expanduser(args.against_dir), ext)))
    refs = [r for r in dict.fromkeys(refs) if os.path.abspath(r) != os.path.abspath(args.draft)]

    if not refs:
        print("No reference pieces given. Use --against or --against-dir.", file=sys.stderr)
        sys.exit(2)

    draft_sig = signature(args.draft, load(args.draft))
    results = []
    for r in refs:
        try:
            sig = signature(r, load(r))
        except OSError:
            continue
        results.append({"file": r, "similarity": similarity(draft_sig, sig), "signature": sig})

    results.sort(key=lambda x: -x["similarity"])
    flagged = [r for r in results if r["similarity"] >= args.flag_at]

    if args.json:
        print(json.dumps({"draft": draft_sig, "comparisons": results, "flagged": flagged}, indent=2))
        sys.exit(1 if flagged else 0)

    print(f"\n=== shape convergence: {os.path.basename(args.draft)} ===")
    print(
        f"opening: {draft_sig['opening_move']}   closing: {draft_sig['closing_move']}   "
        f"{draft_sig['paragraphs']} paras, avg {draft_sig['avg_para_words']}w (CV {draft_sig['para_cv']})"
    )
    print(f"\ncompared against {len(results)} recent piece(s):")
    for r in results[:8]:
        mark = "  <-- REPEATED SHAPE" if r["similarity"] >= args.flag_at else ""
        s = r["signature"]
        print(f"  {r['similarity']:.2f}  {os.path.basename(r['file'])[:48]:48s} ({s['opening_move']}/{s['closing_move']}){mark}")

    if flagged:
        print(f"\n{len(flagged)} piece(s) at or above {args.flag_at} similarity.")
        same_open = [r for r in flagged if r["signature"]["opening_move"] == draft_sig["opening_move"]]
        same_close = [r for r in flagged if r["signature"]["closing_move"] == draft_sig["closing_move"]]
        if same_open:
            print(f"  - same opening move ({draft_sig['opening_move']}) as {len(same_open)} of them. Change how it starts.")
        if same_close:
            print(f"  - same closing move ({draft_sig['closing_move']}) as {len(same_close)} of them. Change how it ends.")
        print("  Break the pattern before publishing. Rotate one structural choice: cold open,")
        print("  delayed reveal, oblique tangent, open thread, or end hot instead of on a coda.")
    else:
        print(f"\nNo repeated shape above {args.flag_at}. Skeleton is distinct from recent pieces.")

    sys.exit(1 if flagged else 0)


if __name__ == "__main__":
    main()
