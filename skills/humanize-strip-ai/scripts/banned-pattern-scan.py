#!/usr/bin/env python3
"""
Banned sentence-pattern scanner.

Reads text from stdin or a file argument, scans against the multi-word
LLM-tell patterns in the PATTERNS list below, and outputs
JSON: { "hits": [{pattern, match, sentence, char_offset}, ...], "total": N }.

Pass 1 of the anti-AI method. Wire it wherever a draft is about to ship:
a pre-publish gate, a pre-commit hook, a CI step, or by hand on one file.

The PATTERNS list below is the source of truth. If you mirror it into a
style guide for readability, update the mirror from here, never the reverse.

Usage:
  echo "text" | python3 banned-pattern-scan.py
  python3 banned-pattern-scan.py path/to/file.html
  python3 banned-pattern-scan.py --json-only path/to/file.html  # bare JSON, no stderr summary

Exit codes:
  0 = no hits
  1 = at least one hit (CI / Phase 6 hard-fail)
  2 = input error
"""
from __future__ import annotations
import json
import re
import sys
from pathlib import Path

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
    """Scan text against PATTERNS. Returns hit dict."""
    cleaned = strip_html(text)
    hits = []
    for label, pat in PATTERNS:
        for m in re.finditer(pat, cleaned, flags=re.IGNORECASE):
            hits.append({
                "pattern": label,
                "match": m.group(0),
                "char_offset": m.start(),
                "sentence": find_sentence(cleaned, m.start()),
            })
    return {"hits": hits, "total": len(hits), "patterns_checked": len(PATTERNS)}


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
        print(f"\n!! {result['total']} banned-pattern hit(s) across {len(set(h['pattern'] for h in result['hits']))} pattern(s)", file=sys.stderr)

    return 1 if result["total"] > 0 else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
