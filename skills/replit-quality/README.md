# Replit Quality for Claude Code

**Knowledge skill.** The QA checklist and the bug encyclopedia for Replit sites, in one file: what to verify before you hand a site over, and 16 categories of recurring bug with the root cause, the exact fix, and the prevention for each.

## Install

Copy [`INSTALL-PROMPT.md`](INSTALL-PROMPT.md) and paste it into your AI agent (Claude Code, Cursor, or similar). It installs [`SKILL.md`](SKILL.md) unchanged, asks one question about what you build (client sites, your own products, or prototypes), then runs the checklist on a real site of yours or matches a live bug to its entry. No accounts, no keys.

## What's here

- `INSTALL-PROMPT.md`: the runbook you paste.
- `SKILL.md`: the full reference, roughly 1,100 lines in two halves. Pre-ship UX rules, a pre-delivery checklist, and a known-issues log. Then 16 categories of recurring bug: hydration, meta tags and SEO, server stability, build and deploy, CSS, layout and mobile, routing, performance, email, PDF, images, copy, Open Graph, analytics, database and API, and component patterns.

## Scope

The debugging half is written for React + Vite + Express projects. Most entries are stack bugs that were simply catalogued on Replit, so they apply to that stack wherever it runs; the genuinely platform-specific ones say so. Your AI states this before installing anything, so you can decline if you build on a materially different stack.

Live preview: [donatassimkus.com/ai-skills/replit-quality](https://donatassimkus.com/ai-skills/replit-quality)
