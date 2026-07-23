# Technical Audit for Claude Code

**Knowledge skill.** A repeatable pre-launch technical sweep that answers one question: is this site safe to ship? Responsive overflow, broken links and images, meta hygiene, noindex leaks, sitemap and structured data, launch assets, migration URL parity, and forms and accessibility hygiene, ending in a verdict table that is explicit about what was not measured.

## Install

Copy [`INSTALL-PROMPT.md`](INSTALL-PROMPT.md) and paste it into your AI agent (Claude Code, Cursor, or similar). It installs [`SKILL.md`](SKILL.md) and the two scripts unchanged, asks one question about what you usually audit (a new launch, a rebuild or migration, or a live site you sweep periodically), then runs a real audit on one of your own sites. No accounts, no keys.

## What's here

- `INSTALL-PROMPT.md`: the runbook you paste.
- `SKILL.md`: the method your AI installs.
- `scripts/audit-build.mjs`: scans a built output folder for broken internal links, broken local images, missing and duplicate titles and descriptions, over-length meta, and noindex leaks.
- `scripts/sitemap-parity.mjs`: fetches the old site's sitemap and reports every old URL as present, redirected, or MISSING, so nothing 404s after a migration. Reads three redirect-file shapes (JSON object, JSON array, or `_redirects` text) and tells you how many rules it parsed.

Both scripts use Node built-ins only. Nothing to install, no package manager needed. Node 18 or newer.

## Credit

The interaction, forms, and accessibility section of the method is adapted from Vercel's publicly published Web Interface Guidelines. That credit belongs to Vercel and is kept in the shipped file.

Live preview: [donatassimkus.com/ai-skills/technical-audit](https://donatassimkus.com/ai-skills/technical-audit)
