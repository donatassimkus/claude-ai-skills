# Self-check, output, and file save

Loaded at the end of the social-post skill workflow.

## Self-check

Run before returning output:

1. No sentence longer than 25 words.
2. No banned words (checked against the user's banned-words list).
3. No em dashes.
4. No formal transitions (Furthermore, Moreover, Additionally).
5. No "I'm excited to share" or "I'm thrilled" openers.
6. Hook is line 1. No preamble before it.
7. White space after the hook.
8. Post ends with intention: strong closing statement, question (only if it genuinely adds value), or direct CTA. No forced questions.
9. Voice matches the user's captured voice baseline at the conversational polish level.
10. Polish level matches post type. Professional: no "I think", "basically", "super" before facts. Conversational: at least one signature connector. Both: grammatically correct, short sentences, active voice.
11. Reads like someone talking, not a press release.
12. No aspirational filler. Every sentence describes something concrete.
13. Hashtags only if platform warrants them (Instagram yes, LinkedIn/Facebook/YouTube community no by default).
14. One sentence per line. No paragraphs anywhere in the caption.
15. Voice is builder/optimizer, not emotional/fearful. Even personal topics framed as "I built a solution."
16. Caption is raw markdown, not inside a code block. Must be copy-paste ready with line breaks.
17. Post includes at least one concrete element (stat, framework, specific example, named tool) beyond pure opinion.
18. Checked position log for contradictions with previous posts. Any conflicts flagged to user.
19. No self-congratulatory claims about expertise or skill. No "I knew", "I did", "my experience." Competence shown through actions and results, never stated directly.
20. Could any practitioner in this space have written this post? If yes, flag to user: "This reads generic. Want to add a personal angle or ship as-is?" User decides. Not a blocker.
21. Tense matches reality. If the situation is ongoing, use present tense ("News is everywhere" not "News was everywhere"). Past tense only when the situation has concluded.
22. LinkedIn angle variations generated (minimum 2 beyond original). Each has a different hook, matching first-comment file, and passes all self-checks independently.
23. Audience language check. Would a growth marketer on LinkedIn use this exact word to describe the same thing? If the word belongs to dev/product culture and the audience isn't devs, rephrase it. Technical terms that have one clear meaning in context are fine.
24. Every standalone image title includes the full topic. No generic titles like "What changed" or "How it works." Always include the subject.
25. Engagement strategy executed: if saves are primary/secondary, check that save hint exists in caption body (not CTA) and on at least one reference-heavy image. If comments are primary, check first comment seeds conversation. If shares are primary, check bonus assets make sense standalone.
26. Save hint is in the caption body, not the final CTA line. Final CTA stays as follow (default), giveaway, question, or statement.

---

## Output format

### Single post (default)

Metadata in a code block:
```
FORMAT: [Text / Carousel (slide count) / Image / Document]
PILLAR: [which content pillar]
HOOK TYPE: [which hook type used]
POLISH: [Professional / Conversational]
POST DAY: [day(s) of the week only. Heavy: 1 peak day. Medium: 1 primary + 1 alternative. Light: 2-3 options.]
CHANNELS:
  LinkedIn: [Yes/No] — [mid-morning, audience local time]
  X/Twitter: [Yes/No] — [midday, audience local time] — [format note if different from LinkedIn, e.g. "single image version"]
  Instagram: [Yes/No] — [evening, audience local time] — [format note if different]
  YouTube: [Yes/No] — [mid-morning, audience local time] — [community post only]
  Facebook: [Yes/No] — [mid-morning, audience local time] — [link in body OK]
ENGAGEMENT: [Primary: saves/comments/shares/profile visits] [Secondary: one or two others] [Tactics: 2-3 specific tactics for this post]
PHOTO: [None / Solo / Family / With-kid / Fitness / inbox]
CREDITS: [tagged people or sources, or "none"]
RISK: [Low / Medium / High]
```

**Caption:** Output as raw markdown (NOT inside a code block). One sentence per line. Blank line between every sentence. This ensures the user can copy-paste directly with line breaks preserved.

After the caption, add if applicable:

**VISUAL DIRECTION:** (only if carousel or image format)
- Slides: [count]
- [Slide-by-slide outline or image concept]
- Style: [notes]

**FIRST COMMENT:** [if link or additional context needed]

**Output rule:** The caption must never be inside a code block, fenced block, or quote block. Raw markdown only. This is required for copy-paste formatting to work on LinkedIn and other platforms.

### Batch mode

When asked for multiple posts on a topic:

```
POST 1 OF [N]
[same structure as single post]

---

POST 2 OF [N]
[same structure as single post]
```

Vary hook types across the batch. Label each with format and pillar.

### Repurpose mode

When given existing content (blog post, video transcript, case study) to turn into social posts:

Produce 3-5 variants, each with a different hook angle:
- Main takeaway
- Contrarian angle
- Step-by-step extract
- Single stat or number highlight
- Question/debate starter

Label each variant. Apply the user's repurposing framework from their brand strategy, if they have one written down.

---

## File output

After producing a post, save it under the user's social-posts working directory (established once on first use and persisted):

Structure:
```
social-posts/
  YYYY-MM-DD-topic-slug/        (date = today's date when created, NOT predicted posting date)
    caption-linkedin.txt             (original, always generated)
    caption-linkedin-value-first.txt  (angle variation, if applicable)
    caption-linkedin-credit-angle.txt (angle variation, if applicable)
    caption-linkedin-opinion.txt      (angle variation, if applicable)
    caption-linkedin-numbers.txt      (angle variation, if applicable)
    caption-linkedin-personal.txt     (angle variation, if applicable)
    caption-twitter.txt
    caption-instagram.txt
    caption-facebook.txt
    caption-youtube.txt
    raw-input.txt                     (user's brief, source material, feedback)
    production-log.txt                (full decision trail, angles, checkpoints, reasoning)
    document-title.txt                (LinkedIn carousel document title, max 58 chars)
    first-comment.txt                 (matches original caption)
    first-comment-value-first.txt     (matches value-first caption)
    first-comment-credit-angle.txt    (matches credit-angle caption)
    first-comment-numbers.txt         (matches numbers caption)
    first-comment-personal.txt        (matches personal caption)
    dm-reply.txt                      (DM message for commenters, giveaway posts only)
    posting-schedule.txt              (suggested repost timing for variations)
    assets/                     (carousel slides, images, PDF)
  scheduled-published/          (user moves folders here when scheduled or posted)
  archive/                      (user moves folders here when discarding)
```

### Post lifecycle

Posts move through folders by the user (not by Claude):

1. **Created** → `social-posts/YYYY-MM-DD-slug/` (root level). This is where Claude saves new posts.
2. **Scheduled or published** → user moves the folder to `scheduled-published/`.
3. **Discarded** → user moves the folder to `archive/`.

When looking for past posts (repurposing, contradiction checks, or reference):
- Check `scheduled-published/` for posts that were actually used.
- Check `archive/` for posts that were discarded.
- Root level folders are drafts not yet actioned.

### File save rules

- One folder per post, named by date and short topic slug.
- One caption file per platform requested.
- Caption files are plain text (.txt) with blank lines between every sentence. No code blocks.
- Assets folder created only if visual direction is provided.
- Always save automatically after producing the post. No need to ask.
- After saving, provide a clickable markdown link to each caption file so the user can open it directly from the terminal.
- Save the user's raw input (brief, source material, prompts, whatever they provided) to `raw-input.txt` in the post folder. Include any feedback given during production. This builds a learning archive over time.
- Save `production-log.txt` with every post. This is the full decision trail showing how the post was produced. Starts with a quick summary (angle, format, photo, hook, tone, engagement prediction, risk level), then breaks down every step: brief parsing, editorial review findings, format selection, caption writing decisions, checkpoint questions and answers, image generation details, and a chronological decisions log with reasoning. Written incrementally during production. Include ALL questions asked and ALL user answers. Include reasoning for every decision, even obvious ones. If something changed after a checkpoint, log what changed and why. Quick mode posts still get a production log.
- After saving all files, append a new row to `references/position-log.md` with: date, topic slug, core position (1-2 sentences), and nuance/caveats. This tracks published positions for contradiction checking on future posts.
- Save `document-title.txt` with every carousel post. This is the title LinkedIn shows when uploading a PDF carousel. It helps discovery. **Maximum 58 characters.** Keep it descriptive, include key topic words, match the actual content. Not clickbait. Example: "197 SEO Hacks for Claude Code (Free Download)" (47 chars). Not needed for non-carousel posts.
- Save `first-comment.txt` with every post. Must be pure copy-paste text. No instructions, labels, or headers. Content depends on post type:
  - **Regular posts**: extra context, a follow-up thought, or "Follow [the brand handle] for more on growth marketing, AI, and automation."
  - **Value bomb posts**: website link + what they'll get. "Full breakdown + templates at [the brand website]" or similar.
  - **Never put links in the main caption** (LinkedIn kills reach). First comment is always the link vehicle.
- Save `dm-reply.txt` for giveaway posts. This is the DM sent to people who comment the keyword. Pure copy-paste. Contains the promised link + brief context about what they're getting. No instructions or labels.
