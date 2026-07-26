# Humanize: Strip AI for Claude Code

**Knowledge skill.** Two passes that take the machine out of a draft: the words first, then the shape.

## Install

Copy [`INSTALL-PROMPT.md`](INSTALL-PROMPT.md) and paste it into your AI agent (Claude Code, Cursor, or similar). It installs the skill files unchanged, asks one question to calibrate, then runs the method on your own material. No accounts, no keys.

## What's here

- `INSTALL-PROMPT.md`: the runbook you paste.
- `SKILL.md`: the router your AI installs. It loads the reference each task needs.
- `scripts/banned-pattern-scan.py`: shipped with the kit.
- `scripts/banned-words.txt`: shipped with the kit.
- `scripts/shape-convergence.py`: shipped with the kit.
- `scripts/structural-scan.py`: shipped with the kit.

Live preview: [donatassimkus.com/ai-skills/humanize-strip-ai](https://donatassimkus.com/ai-skills/humanize-strip-ai)
