# Growth Marketing Skills for Claude Code

Copy-paste skills that turn your AI agent into a growth marketer: SEO, CRM, marketing automation, inbox triage, and the build-and-QA work that ships the pages. Each skill is a single prompt you paste into **Claude Code, Cursor, or any AI agent**. The agent reads it, sets the skill up on your own machine and accounts, and applies it from then on. Nothing to sign up for, no keys, no accounts.

These are the working methods behind ten years of growth marketing, written down as files an agent can install rather than advice you have to remember.

**Live catalog with full previews:** [donatassimkus.com/ai-skills](https://donatassimkus.com/ai-skills)

![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)
![Skills](https://img.shields.io/badge/skills-66-blue.svg)
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

### Build & Automation

| Skill | Type | What it does |
|---|---|---|
| [inbox-organizer](skills/inbox-organizer/) | Agent | Labels your inbox, archives the noise, and drafts the replies. Never sends, never deletes. |
| [n8n](skills/n8n/) | Knowledge | Build reliable n8n workflows: design principles, error handling, AI agents, and debugging. |
| [automation](skills/automation/) | Knowledge | Cross-tool architecture: which tool for which job, and how to wire a stack that runs itself. |
| [ghl](skills/ghl/) | Knowledge | Stand up a CRM, funnels, and automations in GoHighLevel without the trial and error. |
| [chrome-extension](skills/chrome-extension/) | Knowledge | Scaffold a Manifest V3 extension and ship it to the Web Store without the rejections. |
| [vibe-coding](skills/vibe-coding/) | Knowledge | Go from idea to a working product fast with AI, whatever the stack. |
| [technical-audit](skills/technical-audit/) | Knowledge | Point your AI at a site before launch and get every break that would ship, ranked. |
| [replit-quality](skills/replit-quality/) | Knowledge | A pre-ship UX and QA checklist, plus 16 categories of Replit bug with the fix for each. |

### Growth & Acquisition

| Skill | Type | What it does |
|---|---|---|
| [leads](skills/leads/) | Knowledge | The Core Four methods to fill a pipeline, with the outreach that books calls. |
| [cold-outreach](skills/cold-outreach/) | Knowledge | Cold email, DMs, and pitches that get replies, plus the sequencing behind them. |
| [growth](skills/growth/) | Knowledge | Funnel, channel-priority, and MRR frameworks for growth that compounds. |
| [gtm](skills/gtm/) | Knowledge | Launch a product or enter a market: ICP, positioning, and channel choice. |
| [nurture](skills/nurture/) | Knowledge | Pre-sale follow-up and post-sale retention that lifts show rates and cuts churn. |
| [paid-media](skills/paid-media/) | Knowledge | Google, Meta, and LinkedIn ad execution without burning the budget. |
| [abm](skills/abm/) | Knowledge | Target and land named enterprise accounts with multi-threaded outreach. |
| [email](skills/email/) | Knowledge | Sequences, deliverability, and the infrastructure behind inbox placement. |

### SEO & Search

| Skill | Type | What it does |
|---|---|---|
| [seo-hacks](skills/seo-hacks/) | Knowledge | 152 white-hat tactical SEO wins you can run today, sorted by effort and impact. |
| [seo](skills/seo/) | Knowledge | Site-wide SEO: audits, architecture, and the roadmap behind the rankings. |
| [local-seo](skills/local-seo/) | Knowledge | Rank in the map pack: Google Business Profile, citations, and reviews. |
| [youtube-seo](skills/youtube-seo/) | Knowledge | Rank videos and grow a channel: titles, thumbnails, and watch-time. |
| [analytics](skills/analytics/) | Knowledge | GA4, Search Console, and UTMs wired so you can trust your numbers. |

### Content & Writing

| Skill | Type | What it does |
|---|---|---|
| [hooks](skills/hooks/) | Knowledge | Openers that stop the scroll, with a framework to test them. |
| [writing-audit](skills/writing-audit/) | Knowledge | Paste your copy and your AI strips out the ChatGPT tells and clichés. |
| [tone-of-voice](skills/tone-of-voice/) | Knowledge | Turn your own writing into a reusable voice your AI matches every time. |
| [content](skills/content/) | Knowledge | Blog, email, landing, and ad copy that sounds like you, not a template. |
| [social-post](skills/social-post/) | Knowledge | Turn one idea into ready-to-post content, LinkedIn first. |
| [personal-brand](skills/personal-brand/) | Knowledge | Position yourself and build a content system that compounds attention. |
| [pr](skills/pr/) | Knowledge | Get featured in press, podcasts, and awards without a PR agency. |
| [blog-post](skills/blog-post/) | Knowledge | Turn a keyword into a full, structured, ready-to-publish SEO post. |
| [blog-batch](skills/blog-batch/) | Agent | Generate a batch of SEO posts as drafts, scheduled one per day. |
| [blog-audit](skills/blog-audit/) | Knowledge | Check published posts held up: SEO decay and keyword cannibalization. |
| [content-plan](skills/content-plan/) | Knowledge | Turn a keyword or a skill into a validated pillar-and-cluster content map. |

### Sales & Revenue

| Skill | Type | What it does |
|---|---|---|
| [offer](skills/offer/) | Knowledge | Design an offer people feel stupid saying no to, and price it right. |
| [closing](skills/closing/) | Knowledge | Handle objections and run discovery calls that actually close. |
| [customer-success](skills/customer-success/) | Knowledge | Onboarding and account health that turns customers into renewals. |
| [sales-management](skills/sales-management/) | Knowledge | Build and comp a sales team, and run a pipeline that forecasts. |

### Brand, Product & UX

| Skill | Type | What it does |
|---|---|---|
| [branding](skills/branding/) | Knowledge | Positioning and brand strategy that earns a price premium. |
| [product-marketing](skills/product-marketing/) | Knowledge | Positioning, messaging, and battlecards to sell what you built. |
| [product](skills/product/) | Knowledge | Decide what to build: PMF signals, roadmaps, and PRDs. |
| [cro](skills/cro/) | Knowledge | Audit a funnel and lift conversion where it actually moves. |
| [ui-ux-audit](skills/ui-ux-audit/) | Knowledge | Point your AI at a flow and get the usability breaks, before users find them. |
| [ux](skills/ux/) | Knowledge | UX principles: heuristics, flows, cognitive load, and the states most sites skip. |
| [web-design](skills/web-design/) | Knowledge | Direction, composition, and components for a page that doesn't look generic. |
| [research](skills/research/) | Knowledge | Size a market, map competitors, and pin down an ICP. |

### AI Systems & Ops

| Skill | Type | What it does |
|---|---|---|
| [save-session](skills/save-session/) | Knowledge | Promote a chat's learnings into permanent memory, so your AI compounds what it knows. |
| [memory-maintenance](skills/memory-maintenance/) | Agent | Keep your AI's memory clean: merge duplicates, fix stale facts, prune the index. |
| [ingest](skills/ingest/) | Agent | Drop any source (PDF, video, podcast, article) and your AI reads, distils, and files it. |
| [brief](skills/brief/) | Knowledge | A morning brief across email, Slack, calendar, and CRM: what needs you today. |
| [handoff](skills/handoff/) | Knowledge | Hand a long chat off to a fresh one without losing the thread. |
| [skill-authoring](skills/skill-authoring/) | Knowledge | Split every skill's universal method from its per-context config, so a library scales without turning to mush. |
| [portable-prompt](skills/portable-prompt/) | Knowledge | Turn any capability into a paste-ready prompt others can rebuild on their own setup. |
| [content-idea](skills/content-idea/) | Knowledge | Capture a content idea mid-work before it slips, with no drafting. |
| [agent-team](skills/agent-team/) | Knowledge | Spawn a coordinated team of AI agents for a multi-domain build. |
| [optimize-vs-skill](skills/optimize-vs-skill/) | Knowledge | A human-gated optimizer that grades work against your own quality rubrics. |
| [optimize-vs-score](skills/optimize-vs-score/) | Agent | An unattended loop that grinds one metric overnight, keeping only what scores better. |
| [claude-code-audit](skills/claude-code-audit/) | Knowledge | Audit and fix your AI coding setup: health check for the whole rig. |
| [manual](skills/manual/) | Knowledge | Generate a living map of your whole AI system, straight from the files. |

### BizOps & Finance

| Skill | Type | What it does |
|---|---|---|
| [finance](skills/finance/) | Knowledge | Models for runway, margins, and the numbers that decide the business. |
| [fundraising](skills/fundraising/) | Knowledge | Decks, term sheets, and cap tables for a raise. |
| [scaling](skills/scaling/) | Knowledge | Org design, hiring, and SOPs that survive fast growth. |
| [partnerships](skills/partnerships/) | Knowledge | Channel and co-marketing programs that add a growth lever. |
| [community](skills/community/) | Knowledge | Build and retain a community that compounds over time. |
| [entrepreneur](skills/entrepreneur/) | Knowledge | Pick the right business model and vehicle before you build the thing. |
| [business-acquisition](skills/business-acquisition/) | Knowledge | Evaluate buying a business: the due diligence and the deal math. |

### Tactics & Hacks

| Skill | Type | What it does |
|---|---|---|
| [marketing-hacks](skills/marketing-hacks/) | Knowledge | White-hat marketing tactics for quick, compounding wins. |
| [business-hacks](skills/business-hacks/) | Knowledge | White-hat ops, pricing, and SaaS tactics worth stealing. |


## Adding more

This is a growing library. Each skill is one self-contained folder under `skills/`, so new ones drop in cleanly. See [CONTRIBUTING.md](CONTRIBUTING.md) for the layout and how to add one.

## License

[MIT](LICENSE). Fork it, adapt it, ship it. Attribution appreciated, not required.

---

Built by [Donatas Simkus](https://donatassimkus.com). More skills, with live previews you can read before you copy, at [donatassimkus.com/ai-skills](https://donatassimkus.com/ai-skills).
