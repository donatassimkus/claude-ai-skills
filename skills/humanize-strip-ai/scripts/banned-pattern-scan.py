#!/usr/bin/env python3
"""
Banned word and sentence-pattern scanner. Pass 1 of the anti-AI method.

Reads text from stdin or a file argument and scans it on two axes:
  1. Single banned WORDS, loaded from banned-words.txt beside this script.
  2. Multi-word LLM-tell PATTERNS, from the PATTERNS list below.

Both are needed. The word list catches vocabulary tells ("tapestry",
"groundbreaking"); the pattern list catches structural cliches a word list
cannot see ("it's not X, it's Y"). A scan that runs only one axis reports
clean on text that is obviously machine-written on the other.

Outputs JSON:
  { "hits": [{type, pattern, match, sentence, char_offset}, ...],
    "total": N, "words_checked": N, "patterns_checked": N }

Wire it wherever a draft is about to ship: a pre-publish gate, a pre-commit
hook, a CI step, or by hand on one file.

banned-words.txt and the PATTERNS list are the two sources of truth. If you
mirror either into a style guide for readability, update the mirror from
here, never the reverse.

Usage:
  echo "text" | python3 banned-pattern-scan.py
  python3 banned-pattern-scan.py path/to/file.html
  python3 banned-pattern-scan.py --json-only path/to/file.html  # bare JSON, no stderr summary

Exit codes:
  0 = no hits
  1 = at least one hit (use as a CI / pre-publish hard-fail)
  2 = input error
"""
from __future__ import annotations
import json
import re
import sys
from pathlib import Path

# Resolved against THIS script's own directory, not the working directory, so
# the scan works from anywhere the reader happens to run it.
WORDS_FILE = Path(__file__).resolve().parent / "banned-words.txt"

# Each pattern is (label, regex). Regex is compiled with IGNORECASE.
PATTERNS: list[tuple[str, str]] = [
    ("it's worth noting",        r"it'?s worth noting that|it is worth noting"),
    ("in conclusion",            r"\b(in conclusion|to conclude)\b"),
    ("let's explore",            r"let'?s explore|we'?ll explore|we will explore"),
    ("in this article we'll",    r"in this (article|guide|post|piece) (we'?ll|we will)"),
    ("by the end of this",       r"by the end of this (article|guide|post|piece)"),
    ("as we've seen",            r"as we'?ve seen|as mentioned earlier|as discussed (earlier|above)"),
    ("filler transition",        r"\b(without further ado|that said,|having said that)\b"),
    ("look no further than",     r"look no further than"),
    ("the world of X",           r"\bthe world of [a-z]+\b|\bin the world of\b"),
    ("deep dive",                r"\b(deep[- ]dive|let'?s dive|dive deep) (into|in)\b"),
    ("in today's fast-paced",    r"in today'?s (fast-paced|digital|connected) (world|age|landscape)"),

    # Negative parallelism, all six shapes. Worth knowing why there are six:
    # a single regex requiring a literal " is "/" isn't " plus the word "just"
    # catches "SEO is just keywords" and misses every contraction form, including
    # the canonical "It's not X, it's Y". Measured at 0 of 6 shapes caught.
    ("not just X but Y",         r"\b\w+ (is|isn'?t) (more than )?just \w+(,? it'?s also)?"),
    # Handles both the contracted ("it's not") and uncontracted ("it is not") forms.
    ("neg-parallel: not X, it's Y",
     r"\b(it|this|that|there)(?:'?s|\s+is)\s+not\s+(just\s+|only\s+|merely\s+)?[^.,;!?]{2,45}[,;]\s*(it|this|that)(?:'?s|\s+is)\b"),
    ("neg-parallel: not only X but Y",
     r"\bnot only\b[^.!?]{2,80}\bbut (also|it|they|you)\b"),
    ("neg-parallel: not because X. Because Y",
     r"\bnot because\b[^.!?]{2,70}[.!?]\s*because\b"),
    ("neg-parallel: aren't X. They're Y",
     r"\b(these|those|they|it|that|this)\s+(aren'?t|isn'?t|are not|is not)\s+[^.!?]{2,55}[.!?]\s*(they|it|that|these|those)'?(re|s)\b"),
    ("neg-parallel: was never about X",
     r"\b(it|this|that|they)\s+(was|were|is|are)\s+never\s+(about|just|only)\b"),

    # Assistant register: the chatbot voice leaking into first-person writing.
    # Distinct from the vocabulary list, which covers single words rather than the
    # tone of a helpful assistant. These sit near zero in most people's real writing.
    ("assistant: hope this helps",     r"\bhope (this|that) helps\b"),
    ("assistant: careful consideration", r"\bafter careful (consideration|analysis|thought|review)\b"),
    ("assistant: quick update",        r"\b(I|we) (just )?wanted to (provide|give|share|drop|reach out with)\b"),
    ("assistant: here's the thing",    r"\bhere'?s the thing\b"),
    ("assistant: anything else",       r"\blet me know if you (need|have) (anything|any other|further)\b"),
    ("assistant: hope you're well",    r"\bhope (this|my) (email|message|note) finds you well\b"),
    ("assistant: great question",      r"\b(that'?s a |what a )?great question\b"),
    ("assistant: dive in / unpack",    r"\blet'?s (unpack|break (this|it) down)\b"),
]


def load_banned_words() -> list[str]:
    """Read banned-words.txt beside this script. One term per line, # comments ignored.

    Returns [] and warns on stderr if the file is absent, so a missing word list
    degrades the scan to patterns-only rather than crashing. Silence would be
    worse: a clean report from a scan that checked nothing reads as a pass.
    """
    if not WORDS_FILE.is_file():
        print(f"WARNING: {WORDS_FILE.name} not found beside this script. "
              "Scanning PATTERNS only, no words checked.", file=sys.stderr)
        return []
    words = []
    for line in WORDS_FILE.read_text(encoding="utf-8", errors="replace").splitlines():
        line = line.strip()
        if line and not line.startswith("#"):
            words.append(line)
    return words


def strip_html(text: str) -> str:
    """Remove HTML tags + script/style blocks before scanning."""
    text = re.sub(r"<script\b[^>]*>.*?</script>", " ", text, flags=re.DOTALL | re.IGNORECASE)
    text = re.sub(r"<style\b[^>]*>.*?</style>", " ", text, flags=re.DOTALL | re.IGNORECASE)
    text = re.sub(r"<[^>]+>", " ", text)
    text = re.sub(r"\s+", " ", text)
    return text.strip()


def find_sentence(text: str, offset: int) -> str:
    """Return the sentence containing the char offset (truncated to 200 chars)."""
    start = max(0, text.rfind(".", 0, offset) + 1, text.rfind("!", 0, offset) + 1, text.rfind("?", 0, offset) + 1)
    end_candidates = [text.find(".", offset), text.find("!", offset), text.find("?", offset)]
    end_candidates = [e for e in end_candidates if e > 0]
    end = min(end_candidates) + 1 if end_candidates else min(len(text), offset + 200)
    sentence = text[start:end].strip()
    if len(sentence) > 200:
        sentence = sentence[:197] + "..."
    return sentence


def scan(text: str) -> dict:
    """Scan text against the word list AND the pattern list. Returns hit dict."""
    cleaned = strip_html(text)
    hits = []

    words = load_banned_words()
    for word in words:
        # Word boundaries on both ends, so "foster" does not match "fostered"
        # and multi-word entries ("at the forefront") match as a phrase.
        for m in re.finditer(rf"\b{re.escape(word)}\b", cleaned, flags=re.IGNORECASE):
            hits.append({
                "type": "word",
                "pattern": word,
                "match": m.group(0),
                "char_offset": m.start(),
                "sentence": find_sentence(cleaned, m.start()),
            })

    for label, pat in PATTERNS:
        for m in re.finditer(pat, cleaned, flags=re.IGNORECASE):
            hits.append({
                "type": "pattern",
                "pattern": label,
                "match": m.group(0),
                "char_offset": m.start(),
                "sentence": find_sentence(cleaned, m.start()),
            })

    hits.sort(key=lambda h: h["char_offset"])
    return {
        "hits": hits,
        "total": len(hits),
        "words_checked": len(words),
        "patterns_checked": len(PATTERNS),
    }


def main(argv: list[str]) -> int:
    json_only = "--json-only" in argv
    args = [a for a in argv if a != "--json-only"]

    if len(args) > 1:
        path = Path(args[1])
        if not path.is_file():
            print(f"ERROR: file not found: {path}", file=sys.stderr)
            return 2
        text = path.read_text(encoding="utf-8", errors="replace")
    else:
        text = sys.stdin.read()

    if not text.strip():
        print('ERROR: empty input', file=sys.stderr)
        return 2

    result = scan(text)
    print(json.dumps(result, indent=2, ensure_ascii=False))

    if not json_only and result["total"] > 0:
        w = sum(1 for h in result["hits"] if h["type"] == "word")
        p = result["total"] - w
        print(f"\n!! {result['total']} hit(s): {w} banned word(s), {p} banned pattern(s). "
              f"Checked {result['words_checked']} words and {result['patterns_checked']} patterns.",
              file=sys.stderr)
        print("   Fix by REPHRASING the sentence, never by swapping a synonym.", file=sys.stderr)

    return 1 if result["total"] > 0 else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
