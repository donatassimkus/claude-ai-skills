# Growth Marketing Skills for Claude Code

Copy-paste skills that turn your AI agent into a growth marketer: SEO, CRM, marketing automation, inbox triage, and the build-and-QA work that ships the pages. Each skill is a single prompt you paste into **Claude Code, Cursor, or any AI agent**. The agent reads it, sets the skill up on your own machine and accounts, and applies it from then on. Nothing to sign up for, no keys, no accounts.

These are the working methods behind ten years of growth marketing, written down as files an agent can install rather than advice you have to remember.

**Live catalog with full previews:** [donatassimkus.com/ai-skills](https://donatassimkus.com/ai-skills)

![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)
![Skills](https://img.shields.io/badge/skills-12-blue.svg)
![GitHub stars](https://img.shields.io/github/stars/donatassimkus/claude-ai-skills?style=social)

## How to use a skill

1. Open a skill folder under [`skills/`](skills/).
2. Copy its `INSTALL-PROMPT.md`.
3. Paste it into your AI agent (Claude Code, Cursor, Gemini CLI, or similar) and say go.

The agent reads the prompt, asks a question or two, and sets the skill up for you. There are two kinds:

- **Knowledge** skills install a method your agent applies from then on. It just *knows* SEO, or n8n, or GoHighLevel, and uses that knowledge whenever your work touches the topic.
- **Agent** skills have your agent build and run an actual tool on your machine (for example, an inbox organizer that labels your mail and drafts replies).

Want a single skill without cloning the whole repo? `npx degit donatassimkus/claude-ai-skills/skills/n8n` pulls just that folder.

## The skills

### SEO & Search

| Skill | Type | What it does |
|---|---|---|
| [seo](skills/seo/) | Knowledge | The complete SEO method: keyword research, content, technical SEO, and links, installed as real files and run on your own pages. |
| [seo-hacks](skills/seo-hacks/) | Knowledge | 152 white-hat tactical SEO wins, each with execution steps and its original source. |
| [local-seo](skills/local-seo/) | Knowledge | Google Business Profile, the map pack, citations, reviews, location pages, and multi-location strategy. |
| [youtube-seo](skills/youtube-seo/) | Knowledge | The two algorithms, keyword research, titles, thumbnails, watch-time structure, and channel architecture. |

### Build & Automation

| Skill | Type | What it does |
|---|---|---|
| [n8n](skills/n8n/) | Knowledge | Reliable n8n workflow design: error handling, AI-agent workflows, recipes, and a debugging playbook. |
| [automation](skills/automation/) | Knowledge | Cross-tool automation: which tool for which job, whether to automate at all, and how to design it. |
| [ghl](skills/ghl/) | Knowledge | GoHighLevel: account architecture, the white-label SaaS model, core modules, snapshots, and recipes. |
| [chrome-extension](skills/chrome-extension/) | Knowledge | Ship a Chrome extension through Web Store review: Manifest V3 popup-only, icons, every store field, and the rejection reasons. |
| [vibe-coding](skills/vibe-coding/) | Knowledge | Idea to working product fast with AI: tool selection, prompts that produce working code, MVP scoping, and AI debugging. |
| [technical-audit](skills/technical-audit/) | Knowledge | Pre-launch website sweep: responsive overflow, broken links, meta, sitemap, launch assets, and migration URL parity. Ships two scripts. |
| [replit-quality](skills/replit-quality/) | Knowledge | Replit QA: a pre-delivery checklist plus 16 categories of recurring bug with the root cause and fix for each. |

### Email ops

| Skill | Type | What it does |
|---|---|---|
| [inbox-organizer](skills/inbox-organizer/) | Agent | Labels your inbox into seven categories, archives the noise, and drafts the replies. Never sends, never deletes. |

## Adding more

This is a growing library. Each skill is one self-contained folder under `skills/`, so new ones drop in cleanly. See [CONTRIBUTING.md](CONTRIBUTING.md) for the layout and how to add one.

## License

[MIT](LICENSE). Fork it, adapt it, ship it. Attribution appreciated, not required.

---

Built by [Donatas Simkus](https://donatassimkus.com). More skills, with live previews you can read before you copy, at [donatassimkus.com/ai-skills](https://donatassimkus.com/ai-skills).
