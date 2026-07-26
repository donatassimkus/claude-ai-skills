#!/usr/bin/env python3
"""Check first-person density in a draft.

The failure mode this catches is NOT the number of "I"s. It is sentence-initial
stacking: "I built this. I tested it. I found the bug." reads as a diary within
three lines, while the same count of "I"s sitting mid-sentence reads as a person
talking. So the thresholds below are about POSITION and RUN LENGTH.

Rule and rationale: SKILL.md, section 7, "Person: I, you, or neither".

Usage:
  person-density.py <file> [--strict] [--json]

Advisory by default (always exits 0). --strict exits 1 when a threshold fails,
for use as a publish gate.
"""

from __future__ import annotations

import argparse
import json
import re
import sys

# Thresholds. Derived from a hand-tuned sample that reads correct (17 sentences,
# 18% sentence-initial "I", longest run 1, ratio 2:1).
MAX_INITIAL_PCT = 20.0   # sentence-initial "I" as a share of all sentences
MAX_CONSECUTIVE = 2      # consecutive sentences opening with "I"
MIN_YOU_TO_I = 1.5       # "you" words per "I" word across the piece
FULL_PIECE_WORDS = 600   # below this the ratio is reported, not enforced (see analyse)

FIRST = r"\b(i|i'm|i've|i'll|i'd|my|me|mine)\b"
SECOND = r"\b(you|you're|you've|you'll|you'd|your|yours)\b"
OPENS_FIRST = r"^(i|i'm|i've|i'll|i'd|my)\b"

# The guard runs BOTH ways. Too much "I" reads as a diary; none at all is the
# voiceless default that pipeline-generated content falls into, and it is the
# harder failure to notice: a piece with no author in it passes every anti-AI
# scanner and still reads machine-made.
GENERIC_OPENERS = [
    r"^most (people|of us|companies|teams|marketers)",
    r"^every(one|body) (knows|has|struggles)",
    r"^we('ve| have) all\b",
    r"^in today'?s\b",
    r"^many (people|companies|teams)",
    r"^it'?s no secret\b",
    r"^there (is|are) (a lot|many|no shortage)",
]


def prose(text: str) -> str:
    """Drop code fences, headings, tables and list markers; keep prose."""
    text = re.sub(r"```.*?```", " ", text, flags=re.S)
    text = re.sub(r"`[^`]*`", " ", text)
    kept = []
    for line in text.split("\n"):
        s = line.strip()
        if not s or s.startswith("#") or s.startswith("|") or s.startswith(">"):
            continue
        s = re.sub(r"^([-*+]|\d+\.)\s+", "", s)   # list markers, keep the text
        kept.append(s)
    return " ".join(kept)


def analyse(text: str) -> dict:
    body = prose(text)
    sentences = [s.strip() for s in re.split(r"(?<=[.!?])\s+", body) if s.strip()]
    initial, run, longest = 0, 0, 0
    for s in sentences:
        if re.match(OPENS_FIRST, s, re.I):
            initial += 1
            run += 1
            longest = max(longest, run)
        else:
            run = 0

    first = len(re.findall(FIRST, body, re.I))
    second = len(re.findall(SECOND, body, re.I))
    n = len(sentences)
    pct = round(initial / n * 100, 1) if n else 0.0
    ratio = round(second / first, 2) if first else float("inf")

    opener = sentences[0] if sentences else ""
    generic = next((p for p in GENERIC_OPENERS
                    if re.match(p, opener.strip(), re.I)), None)
    opening_has_author = bool(re.search(FIRST, opener, re.I))

    failures, notes = [], []
    # Too much "I".
    if pct > MAX_INITIAL_PCT:
        failures.append(
            f"{pct}% of sentences open with 'I' (limit {MAX_INITIAL_PCT}%)")
    if longest > MAX_CONSECUTIVE:
        failures.append(
            f"{longest} consecutive sentences open with 'I' (limit {MAX_CONSECUTIVE})")
    # The ratio is a WHOLE-PIECE metric. An I-led block (the opening, the method,
    # what went wrong) is correct to be I-heavy on its own, so failing the ratio on
    # a short excerpt would push first person out of exactly the blocks that need it.
    # Below the full-piece threshold it reports but does not fail.
    words = len(re.findall(r"\b[\w']+\b", body))
    if first and ratio < MIN_YOU_TO_I:
        msg = (f"'you' to 'I' ratio is {ratio}:1 (want at least {MIN_YOU_TO_I}:1 "
               f"in instructional writing)")
        if words >= FULL_PIECE_WORDS:
            failures.append(msg)
        else:
            notes.append(
                msg + f" [not failed: {words} words is an excerpt, and this is a "
                      f"whole-piece measure. Check it on the full draft]")
    # Too little. The other half of the guard.
    if first == 0 and n >= 4:
        failures.append(
            "no author present: zero first-person words. This is the voiceless "
            "default, and it passes every anti-AI scanner while reading machine-made")
    if generic:
        failures.append(
            f"opens with a generic claim about people in general: {opener[:60]!r}. "
            "Open with something only the author can say")
    elif not opening_has_author and n >= 4:
        failures.append(
            f"opening carries no author: {opener[:60]!r}. The hook is the one block "
            "that should be I-led")

    return {
        "sentences": n,
        "first_person_words": first,
        "second_person_words": second,
        "you_to_i_ratio": None if ratio == float("inf") else ratio,
        "sentence_initial_i": initial,
        "sentence_initial_pct": pct,
        "longest_i_run": longest,
        "opening_has_author": opening_has_author,
        "generic_opener": generic,
        "failures": failures,
        "notes": notes,
        "passed": not failures,
    }


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("file")
    ap.add_argument("--strict", action="store_true",
                    help="exit 1 when a threshold fails")
    ap.add_argument("--json", action="store_true")
    args = ap.parse_args()

    try:
        text = open(args.file, encoding="utf-8", errors="replace").read()
    except OSError as exc:
        print(f"cannot read {args.file}: {exc}", file=sys.stderr)
        sys.exit(2)

    r = analyse(text)

    if args.json:
        print(json.dumps(r, indent=2))
    else:
        print(f"\n=== {args.file} ===")
        print(f"{r['sentences']} sentences | "
              f"I-words {r['first_person_words']} | you-words {r['second_person_words']}"
              + (f" | ratio {r['you_to_i_ratio']}:1" if r['you_to_i_ratio'] is not None else ""))
        print(f"sentence-initial 'I': {r['sentence_initial_i']} "
              f"({r['sentence_initial_pct']}%), longest run {r['longest_i_run']}")
        for nt in r.get("notes", []):
            print(f"  note: {nt}")
        if r["failures"]:
            print("\n!! I-density problems:")
            for f in r["failures"]:
                print(f"  - {f}")
            print("\nFix by moving first person INSIDE sentences rather than cutting it.")
        else:
            print("Person balance OK.")

    sys.exit(1 if (args.strict and not r["passed"]) else 0)


if __name__ == "__main__":
    main()
