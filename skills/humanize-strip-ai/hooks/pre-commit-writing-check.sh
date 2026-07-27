#!/usr/bin/env bash
# Pre-commit gate for pass 1. Blocks a commit that adds a banned word or a banned
# sentence pattern to any prose file.
#
# Why this exists: running a scanner by hand means running it when you remember to,
# which is not when you need it. A gate that fires on every commit is the difference
# between a rule you have and a rule that holds. Pass 2 (structure) stays advisory
# here on purpose: it needs judgement and a corpus, so it is reported, never blocking.
#
# INSTALL (git): write a WRAPPER, do not copy this file into .git/hooks/.
# Copying it there breaks it: this script finds the scanners at ../scripts relative to
# itself, and from inside .git/hooks that resolves to .git/scripts, which does not exist.
# So point at the kit where it actually lives:
#
#   printf '#!/bin/sh\nexec "/abs/path/to/humanize-strip-ai/hooks/pre-commit-writing-check.sh"\n' \
#     > .git/hooks/pre-commit && chmod +x .git/hooks/pre-commit
#
# If you already have a pre-commit hook, add that one exec line to it instead.
# Alternatively set KIT_DIR to the kit root and this script will find the scanners
# wherever it is invoked from:  KIT_DIR=/abs/path/to/humanize-strip-ai
#
# INSTALL (any other runner): call it from a CI step or a pre-publish task. With no git
# index it scans the paths given as arguments:
#   ./pre-commit-writing-check.sh draft.md posts/*.md
#
# Requires: python3, and the two scanners in the kit's scripts/ folder.
# Exit 0 = clean or advisory-only. Exit 1 = a blocking hit.

set -uo pipefail

HERE="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
# KIT_DIR wins when set, so the hook works from any invocation point; otherwise assume
# the kit layout (hooks/ and scripts/ as siblings), which holds when it runs in place.
SCRIPTS="${KIT_DIR:-$HERE/..}/scripts"
PATTERN_SCAN="$SCRIPTS/banned-pattern-scan.py"
STRUCTURAL_SCAN="$SCRIPTS/structural-scan.py"

# Extensions worth scanning. Code and binaries are skipped: the rules are about prose,
# and a banned word inside a variable name is not a writing problem.
SCAN_EXT_RE='\.(md|markdown|txt|html|mdx)$'

# NEVER scan these. Two classes, both deliberate:
#   1. The word list itself, and the scanner that holds the pattern list. Those files
#      ARE the lists, so scanning them always fires.
#   2. Verbatim third-party text. Quotations are immutable: rewriting a transcript or
#      a testimonial to fit a style guide falsifies what someone actually said.
# Add your own quoted-source folders to this pattern.
# Each folder alternative is anchored with (^|/) so it matches whether the path is
# relative (transcripts/x.md) or absolute (/repo/transcripts/x.md). Anchoring on a bare
# slash silently lets every relative path through, which is how this rule first shipped
# broken: the exemption looked present and never fired.
SKIP_RE='(banned-words\.txt|banned-pattern-scan\.py|-transcript\.|(^|/)(transcripts|quotes|testimonials)/)'

if [[ ! -f "$PATTERN_SCAN" ]]; then
  echo "pre-commit-writing-check: cannot find the scanner at $PATTERN_SCAN" >&2
  echo "  Most likely this file was COPIED into .git/hooks/ instead of being called" >&2
  echo "  from there. Replace .git/hooks/pre-commit with a one-line wrapper:" >&2
  echo "    #!/bin/sh" >&2
  echo "    exec \"/abs/path/to/humanize-strip-ai/hooks/pre-commit-writing-check.sh\"" >&2
  echo "  Or set KIT_DIR=/abs/path/to/humanize-strip-ai before calling it." >&2
  exit 1
fi
if ! command -v python3 >/dev/null 2>&1; then
  echo "pre-commit-writing-check: python3 not found, skipping the writing gate." >&2
  exit 0
fi

# Prefer the staged set; fall back to arguments so the same script works outside git.
FILES=()
if [[ $# -gt 0 ]]; then
  FILES=("$@")
elif git rev-parse --git-dir >/dev/null 2>&1; then
  while IFS= read -r f; do [[ -n "$f" ]] && FILES+=("$f"); done \
    < <(git diff --cached --name-only --diff-filter=ACM)
fi

FAILED=0
CHECKED=0
for f in "${FILES[@]:-}"; do
  [[ -f "$f" ]] || continue
  [[ "$f" =~ $SCAN_EXT_RE ]] || continue
  [[ "$f" =~ $SKIP_RE ]] && continue
  CHECKED=$((CHECKED + 1))

  if ! OUT=$(python3 "$PATTERN_SCAN" "$f" --json-only 2>/dev/null); then
    echo ""
    echo "BLOCKED: $f"
    python3 - "$OUT" <<'PY'
import json, sys
try:
    d = json.loads(sys.argv[1])
except Exception:
    sys.exit(0)
for h in d.get("hits", []):
    kind = h.get("type", "hit")
    print('  [%s] %s: "%s"' % (kind, h["pattern"], h["match"]))
print("  Fix by REPHRASING the sentence, never by swapping a synonym:")
print("  the pattern flags a cliche of structure, and a synonym leaves it in place.")
PY
    FAILED=1
  fi

  # Advisory only. Structure needs judgement, so it reports and never blocks.
  if [[ -f "$STRUCTURAL_SCAN" ]]; then
    python3 "$STRUCTURAL_SCAN" "$f" 2>/dev/null | grep -E '\[OVER THRESHOLD\]' | sed "s|^|  note ($f): |"
  fi
done

if [[ "$FAILED" == "1" ]]; then
  echo ""
  echo "Commit blocked by the pass-1 writing gate. Fix the hits above, or commit with"
  echo "--no-verify if the text is a verbatim quote (then add its path to SKIP_RE)."
  exit 1
fi

[[ "$CHECKED" -gt 0 ]] && echo "writing gate: $CHECKED file(s) clean on pass 1."
exit 0
