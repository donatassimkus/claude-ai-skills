---
name: social-post
description: "Produce ready-to-post social media content: caption, format, visuals, tags. Primary: LinkedIn. Also Twitter/X, Instagram, Facebook, YouTube. Use for social posts, tweets, captions. Content strategy and long-form writing are adjacent disciplines handled separately."
user-invocable: true
argument-hint: [topic or brief] [optional: platform, format, or pillar] [optional: a published blog post URL to repurpose]
context: fork
---

## Social Post Skill

> **Scope:** This skill produces individual social posts ready to publish. Content strategy, pillars and frequency planning; blog posts, emails, landing pages and ad copy; and hook craft as a discipline in itself are all adjacent, handled separately.

Your job: take a topic and return something the user can copy-paste and post. No editing needed. No preamble.

**Target audience (set this per user, do not assume one).** Everything downstream depends on who the posts are for: vocabulary, what gets explained versus assumed, which formats land, and what counts as a credible proof point. Before the first post, establish and persist the user's audience: who they are, what they already know, and what they would find obvious. Then hold two rules. Write at the level of that audience, so do not explain concepts they use daily. And do not write for beginners unless the brief explicitly says so, because writing down to an expert audience reads as filler to them and wins nothing from the beginners who were never going to be the readers.

**Project context is loaded from the active CLAUDE.md.** Apply professional context, audience, and platform from that file.

---

## Hard rules (apply everywhere)

These are the rules the model must remember at all times. Detail behind each rule lives in the referenced file.

1. **Credit rule.** Always credit sources, people, or tools that inspired the post. Tag them on LinkedIn when possible. Never strip attribution. Detail in `references/brief-and-editorial.md`.
2. **Voice guardrail (set the register per user).** Establish once what emotional register the user actually writes in, and hold it consistently rather than drifting post to post. Where the register is matter-of-fact and practitioner-first, which is the common case for a builder or operator audience, never frame posts as emotional, fearful, or vulnerable: even a personal topic reads as "here is the problem and what I did about it". Detail in `references/format-and-writing.md`.
3. **Show, don't claim.** Never state expertise, skill, or knowledge directly. No "I knew", "my experience", "I did." Show actions and results. Let competence be inferred.
4. **Internal goal awareness, never expose.** Content serves whatever commercial goals the user has named (getting hired, winning clients, growing an audience, positioning a product). Keep those goals in mind when choosing angles, and never reference them in captions, slides, or CTAs. No "hire me", no "DM for consulting". The goal shapes what gets written; it never appears in the writing.
5. **Pushback rule.** When the user hesitates without a concrete reason, challenge them. Comfort is not the goal. Results are.
6. **Numbers as digits.** "4 days" not "four days." "60 websites" not "sixty websites."
7. **Disclosure guardrail.** Never reference employer, clients, or side projects unless the user explicitly provides that context. Generic framing ("a site I manage") is fine. Named projects only when the user volunteers them.
8. **Tone enforcement.** Matching the user's captured voice baseline is not optional. Clear over clever. Active voice always. No resume language. Auto-select polish level: Professional for showcase posts, Conversational for opinion + behind-the-scenes. Detail in `references/format-and-writing.md`.
9. **One sentence per line. Blank line between every sentence. No paragraphs. Ever.** Hard format rule for all platforms. Detail in `references/format-and-writing.md`.
10. **No accidental links.** Never include TLD suffixes (.com, .io, .ai, .co) in tool or brand names in captions. LinkedIn penalizes any word containing a TLD. Write "Make" not "Make.com".
11. **Sequential production.** When given multiple posts to produce, work on them one at a time. Fully complete one before starting the next.

12. **Voice drift bans (specific phrasings).** These are the drift patterns AI writing falls into when it is trying to sound thoughtful. Do not put them in any caption, slide, quote card, or asset. When caught, rewrite in the user's actual voice, not with synonyms for the same construction.
    - **Anthropomorphic verbs for tools.** "X lives inside Y", "Y handles X", "X sits in Z", "X catches Y". Tools don't live, sit, or handle. Use plain mechanical verbs.
    - **Abstract spatial metaphors.** "the workflow around the thing", "the layer above", "where the script stops". Be concrete instead: name the actual boundary and what falls on each side of it.
    - **Literary state shifts.** "the friction hit a threshold", "the moment X clicked for me", "what it opened up". Describe events plainly, not feelings about events.
    - **Internal jargon teaser lists.** A standalone run of unexplained feature nouns as a teaser ("Multi-step bundling. Multi-output. Triggered actions."). Either expand each into a concrete example or kill the list.
    - **Self-positioning as opinionated curator.** "The interesting work in X is Y", "What's interesting is Z". Describe mechanics, not opinions about mechanics.
    - **"Sat down with" + AI tool name.** Replace with the plain version: "5 minutes with X and I had Y", or "asked X to write Y".

    **Voice baseline (set this per user, do not assume one).** A named ban list only works against a positive reference. Before writing the first post for a user, capture their baseline: ask for two or three of their own posts that sounded most like them, or the closest thing they have if they have not posted yet. Read those and write down, in three or four lines, what is actually true of their sentences: typical length, whether they use metaphor at all, first person or not, how they open, how they close, what they never do. Persist that alongside the skill and treat it as the reference every later post is matched against.

    Add to the ban list above as drift shows up in review. Anything the user rejects twice for the same reason becomes a new bullet, written as the pattern rather than the single phrase, so it generalises.

13. **Inspect rendered output before declaring done.** Before reporting any multi-file caption batch, carousel render, or image bundle as complete:
    - Read each caption file produced, including all angle variations. Surface any voice-drift hits (per rule 12), redundancy, or grammar issues.
    - Visually open the cover render and any standalone images via Read tool. Confirm copy and layout.
    - Surface flagged issues to the user BEFORE saying "done." Never declare done based on the generator script's "completed successfully" line alone.

14. **Polish, don't restructure, when user flags a phrase.** When the user says "I don't understand X" pointing at a specific phrase, default action is EXPLAIN that phrase in chat — not REWRITE the surrounding copy. Rewrite only when user explicitly asks for a rewrite. Treat "this is unclear" as a request to clarify mechanics, not as a request to redraft.

15. **Don't force one comparison axis across every card in a carousel.** When the angle of the post is "X beats Y", it's tempting to put a "Why X" line on every card. Audit before you do: is the comparison REAL for that specific use case, or stapled on? If a given use case has nothing to do with Y, because nobody would have reached for Y there in the first place, the comparison reads as forced. Keep the positioning in the cover + caption where it lands once. Cards themselves sell each use case on its own terms.

16. **Cover-caption vocabulary alignment.** The cover hook, subhook, and caption body must reuse the same key terms. If the cover says "Use AI to write small scripts," the caption should also say "AI" and "scripts" — don't switch to "Claude" or "LLM" or "machine-generated" mid-post. Pick the terminology once, repeat it.

17. **Cover hook is for cold scrollers.** Slide 1 must be understandable in 0.5 seconds by someone who has never read the body. NO code, formula notation, or syntax as primary hook text: it reads as code rather than as a message, and a cold scroller does not stop to parse it. NO internal jargon. NO abstract spatial metaphors ("the layer above", "the workflow around the thing"). Plain action verbs plus the most common terms in the audience's vocabulary. If the angle genuinely requires the syntax, save it for slide 2 or later, where the reader is already engaged.

---

## Draft mode: capture-now, batch-later

The user has a `save this idea` workflow for capturing post ideas in-flight, without doing full production. Use this when the user wants to queue an idea for a later batch session instead of producing immediately.

**Triggers (any of these phrases):** `save this idea` · `save as draft` · `save this for later` · `draft this for later` · `save as a post idea` · `save a post idea`.

**On trigger, do this and ONLY this:**
1. Extract from the current conversation context:
   - Topic (what was just discussed or what the user said the idea is about)
   - Hook (the interesting / novel / contrarian part — the thing that makes it postworthy)
   - Specific numbers, examples, facts mentioned in the conversation
   - Suggested angle (story / opinion / numbers / personal / value-first / how-to)
   - Photo cue if the conversation suggests one
2. Generate a kebab-case slug from the topic (3-5 words).
3. Write the draft to the drafts folder inside the user's social-posts working directory, as `drafts/idea-YYYY-MM-DD-{slug}.md`. Establish that working directory once, on first use, and persist it; everything this skill writes lives under it. Use this template:

```markdown
# Idea: {short title}

**Date saved:** YYYY-MM-DD
**Source:** {one-line context — what conversation/work this came from}

## Core insight
{1-2 sentences on the idea}

## Hook candidate
{the best opener line, in the user's voice}

## Key points to include
- {bullet}
- {bullet}

## Suggested angle
{story / opinion / numbers / personal / value-first / how-to}

## Notes
- {any voice / framing / structural guardrails specific to this idea}
```

4. Confirm in chat with ONE line: `Saved to drafts/idea-{date}-{slug}.md. {N} drafts in queue.`

**DO NOT** ask clarifying questions, produce polished captions, generate images, or run any other part of the social-post workflow. Capture mode is intentionally lightweight.

**Batch production triggers:** `list drafts` · `show drafts` · `ready for the batch` · `run the drafts batch`.

**On batch trigger:**
1. Scan the drafts folder for all `idea-*.md` files (ignore the `archived/` subfolder).
2. List each in chat: date, slug, 1-line topic summary, full path.
3. Ask the user (via `AskUserQuestion`, multi-select) which drafts to produce.
4. For each selected draft, run the full social-post workflow using the draft's content as the brief. Produce sequentially per Rule 11.
5. After each draft is produced successfully, move the source draft from `drafts/` to `drafts/archived/{date}/` so it's not re-listed next time.

---

## When invoked

`$ARGUMENTS` defines the topic, brief, or idea.

Parse for optional signals:
- **Platform override** (default: LinkedIn)
- **Format override** (default: auto-select)
- **Pillar alignment** (default: infer from topic)
- **Length preference** (default: medium)
- **Batch mode** ("give me 5 posts on X")
- **Repurpose mode** (existing content to turn into social posts)
- **From a published blog post** (repurpose an existing article into social): first capture the post's SPINE, by reading the live post or exporting it from the CMS: title, primary keyword, the H2 headings, the summary or TL;DR, and the canonical URL. If the post cannot be resolved, or the spine comes back empty, STOP and report rather than writing from nothing; a repurpose built on an empty brief invents claims the article never made. Then run Repurpose mode with that spine as the brief: produce 3-5 variants per channel, FORCE the image visual on rather than skipping it (a link post without a visual underperforms badly), and put the canonical URL in `first-comment.txt` rather than the caption body, per the no-accidental-links rule. Only ever repurpose a live, published post: a scheduled or future-dated draft's URL returns a 404 to everyone who clicks it. If this runs unattended as part of a larger batch, suppress this skill's interactive checkpoints so the run cannot block: skip the brief-quality and editorial checkpoints, auto-accept the recommended caption and the recommended image direction, and log every auto-choice so an operator can review what was decided. In an attended run, the user drives those checkpoints normally.

If `$ARGUMENTS` is a bare topic with no other signals: produce captions for ALL platforms by default (LinkedIn, Twitter/X, Instagram, Facebook, YouTube community), auto-select format, infer pillar. Save each as a separate caption file.

If no arguments: ask one question — what is the topic or idea?

---

## The 6-step workflow

Each step has a dedicated reference file. Load the file when you reach that step.

### Step 1: Load dependencies and parse brief
Load `references/brief-and-editorial.md`. Covers:
- Dependency loads: the user's captured voice baseline, their content pillars and positioning, hook craft, and their banned-words list.
- Auto-detect signals (photo category, quick mode, format, depth).
- Brief quality gate (1-5 score).
- Quick mode rule.
- When and how to research.
- AskUserQuestion patterns (one-at-a-time, max 4 per round, multi-select rules).
- Position log check (`references/position-log.md`).
- Framework opportunity flag.

### Step 1c: Editorial review
Same file: `references/brief-and-editorial.md`. Covers:
- Editorial review format (core angle, alternative angles, risk, gut check, suggestions, hook directions).
- "So what?" / Differentiation / Skill demonstration / Connection-building / Content pillar checks.
- Engagement strategy (saves, comments, shares, profile visits, with tactics).
- Caveat placement decision.
- After-the-review handling (clean = proceed, decision needed = AskUserQuestion).

### Step 2 + 3: Select format and write the post
Load `references/format-and-writing.md`. Covers:
- Format selection table (text, carousel, image, stat, quote, document).
- 2026 algorithm rules (screenshot override, value bomb, video deprio, format rotation, niche specificity, first 90 minutes).
- Formatting hard rule (one-sentence-per-line example).
- Audience language rule.
- Topic signal optimization.
- Carousel caption rule.
- Caption structure (hook, white space, body, save hint, CTA, no accidental links).
- Giveaway engagement tactics.
- Teaching structure (problem, method, result, your turn).
- Length strategy.
- Caption + outline confirmation checkpoint.

### Step 4: Visual direction and image generation
Load `references/images.md`. Covers:
- Visual direction (slide count, outline, concept, overlay, style notes).
- Image direction confirmation checkpoint (photo-topic match check).
- Image inbox (an `inbox/` folder inside the social-posts working directory).
- Photo library (an `assets/photo-library/` folder, organised into categories).
- Required assets (headshot, badge, fonts).
- Generate all styles pipeline (branded, photo, overlay, screenshot, stat, quote).
- Bonus asset enforcement (stat highlights and quote cards always when content qualifies).
- Standalone quality rules.
- Repurposable single images.
- Output structure (asset folder layout).

Visual specs (colors, fonts, dimensions, slide types) live in `references/design-config.md`.

### Step 5 + 6: Hashtags, angle variations, platform adapters
Load `references/platforms.md`. Covers:
- Hashtags and tags table (per platform).
- LinkedIn angle variations (5 angles: original, value-first, credit, opinion, numbers, personal).
- Naming convention for variation files.
- Posting schedule (10-14 days, 21-28 days, 35-42 days for repost variations).
- Platform adapters (LinkedIn, Twitter/X, Instagram, Facebook, YouTube community, YouTube description).
- Channel selection (load `references/channel-strategy.md`).

### Self-check + output + file save
Load `references/quality-and-output.md`. Covers:
- 26-item self-check (run before returning output).
- Output format (metadata block + caption + visual direction + first comment).
- Single, batch, and repurpose modes.
- File output structure (every file produced per post).
- Post lifecycle (created → scheduled-published → archive).
- File save rules (raw-input.txt, production-log.txt, document-title.txt, first-comment.txt, dm-reply.txt, posting-schedule.txt).

---

## Reference files

| File | Loads at step | Purpose |
|---|---|---|
| `references/brief-and-editorial.md` | Step 1 + 1c | Brief parsing, editorial review, all engagement and quality checks |
| `references/format-and-writing.md` | Step 2 + 3 | Format selection, writing rules, caption structure |
| `references/images.md` | Step 4 | Visual direction and image generation pipeline |
| `references/platforms.md` | Step 5 + 6 | Angle variations, hashtags, platform adapters |
| `references/quality-and-output.md` | Final | Self-check, output format, file save rules |
| `references/design-config.md` | Step 4 (visual specs) | Brand colors, fonts, sizes, slide types |
| `references/channel-strategy.md` | Step 6 (channel select) | Per-platform channel rules and timing |
| `references/position-log.md` | Step 1 (contradiction check) | Published positions log |
| `references/weekly-content-schedule.md` | When user asks for a weekly plan | Content schedule template |

---

## Adjacent disciplines (where this skill stops)

- Personal brand strategy — content pillars, positioning, frequency, the repurposing framework. That work plans what this skill produces, so if the user has it written down, load it before writing.
- Voice patterns — the user's captured voice baseline (see Hard rule 12). Loaded before writing every post.
- Hook craft — the hook type taxonomy and testing frameworks. Referenced for hook selection.
- Writing rules — the user's banned words and patterns. Applied as hard constraints on every caption.
- General content creation — blog posts, emails, landing pages, ad copy. For social posts, use this skill instead.
