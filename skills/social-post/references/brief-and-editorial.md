# Brief parsing and editorial review

Loaded at Step 1 and Step 1c of the social-post skill.

## Step 1: Load dependencies

Before writing anything:

1. Load the user's captured voice baseline. Apply those voice patterns throughout. Use the "Conversational" polish level for LinkedIn and social. Use "Professional" for more formal platforms if requested.
2. Load the user's content pillars and positioning, if they have them written down. Identify which pillar this post aligns to. Apply the quality rules either way: practitioner not thought leader, real numbers, no motivational filler.
3. Select a hook type deliberately rather than writing the first line by feel. Work from a fixed taxonomy of verbal hook types and name which one is being used.
4. Apply the user's banned words and patterns as hard constraints on every caption.

## Step 1b: Parse brief and set direction

### Auto-detect signals

Before doing anything else, parse the brief for these signals:

| Signal | Detected from | Action |
|---|---|---|
| **Photo category** | "solo", "my photo", "with my kid", "with my wife", "family photo", "fitness photo" | Set photo category. No need to ask. |
| **Quick mode** | Brief starts with "quick:", "tip:", "just write:" | Skip all of Step 1b. Go straight to Step 2. No research, no questions. |
| **Format** | "breakdown", "carousel", "step by step" → carousel. "tip", "hot take", "observation" → text post. | Pre-select format. Confirm only if ambiguous. |
| **Depth** | "value bomb", "deep one", "full breakdown" | Carousel (target 7 slides, more if needed), short caption. |

If a signal is detected, act on it silently. Do not explain the detection or ask for confirmation.

### Brief quality gate

Score the brief 1-5:

| Score | Description | Action |
|---|---|---|
| 1 | Bare topic, no angle | Ask 3-5 questions: angles, personal data, direction. |
| 2 | Topic + angle, no personal element | Ask 2-3 questions: personal angle, numbers, confirm direction. |
| 3-4 | Clear enough to write | Ask 1-2 confirmation questions: confirm angle, photo, any additions. |
| 5 | Original insight, own data, named method | Ask 1 confirmation question minimum. Even perfect briefs get a check. |

**Minimum questions rule (hard rule):** Every post gets at least 3 questions total across all checkpoints (Step 1b + Step 1c + caption confirmation + image confirmation). Even with perfect information, ask at least 1 question per checkpoint. Quick yes/no confirms are fine. Skipping is not.

### Quick mode (hard rule)

When the brief starts with "quick:", "tip:", or "just write:", the run is FULLY non-interactive end to end: skip Step 1b (scoring/research/questions) AND Step 1c editorial review, AND auto-accept the recommended option at EVERY later checkpoint without asking, the caption + outline confirmation (Step 3b) and the image-direction confirmation (Step 4a) included. Never emit `## CHECKPOINT QUESTIONS`, never call AskUserQuestion. The brief is the brief: write, pick the recommended caption and image direction, log each auto-choice, and return. This is what the blog batch relies on to run `--from-blog` without hanging. The "minimum questions" hard rule above does NOT apply in quick mode.

### When to research

- **Score 1 briefs only**: research before presenting angle options.
- **Score 2+**: do NOT research. The user has a direction. Respect it.
- **Exception**: if the user explicitly asks for research ("what are people saying about this?", "find me data on this").

### How to research (when triggered)

Use web search to find:
1. **Current conversation:** What people are saying on LinkedIn, Twitter/X, Reddit.
2. **Data and stats:** Numbers, studies, benchmarks.
3. **Contrarian takes:** Counter-arguments, hot debates.

### How to ask questions (AskUserQuestion, not text)

**All clarification questions must use AskUserQuestion with concrete options.** Never present questions as text paragraphs.

**Presentation rule:** Show editorial review context (core angle, alternative angles, risk assessment, gut check, suggestions, hooks) inline as regular text. Then ask checkpoint questions one at a time via AskUserQuestion. Present the context first, then ask Question 1. After the user answers, ask Question 2. Continue sequentially until all questions for that checkpoint are answered. Never batch all questions into a single message.

**Subagent fallback:** If running as a forked subagent without access to AskUserQuestion, clearly separate the editorial review (context) from the questions section. Mark questions with `## CHECKPOINT QUESTIONS` so the main agent can ask them sequentially via AskUserQuestion.

Rules:
- **Ask questions one at a time, sequentially.** Present context inline, then ask the first question via AskUserQuestion. Wait for the answer. Then ask the next question. Never dump all questions at once.
- **Max 1 round of questions per checkpoint.** After the user answers all questions, proceed. No second round at the same checkpoint.
- **Max 4 questions per round.**
- **Every question must have 2-4 concrete options.** No open-ended "what do you think?"
- **Always mark the recommended option** with "(Recommended)" at the end of the label. Put it first in the list.
- **Use multi-select (checkboxes) when choices are not mutually exclusive.** Examples: "Which angles to include?", "Which suggestions to adopt?", "Which hooks to test?" The user should be able to pick multiple.
- **Use single-select when choices are mutually exclusive.** Examples: "Which hook to lead with?", "Where to place the caveat?", "Conversational or professional polish?"
- **The user can always type free-form feedback** via the built-in "Other" option on every question. No need to add a separate "give feedback" option.
- **Include a "just write it" or "proceed as-is" option** on at least one question so the user can skip.
- **Never ask about things already detected from signals.** If the brief says "solo", do not ask about photos.

Example question patterns:
- "Which angles to include?" (multi-select) → [How-to, Contrarian take, Personal story, Numbers]
- "Which hook to lead with?" (single-select) → [Data shock (Recommended), Outdated strategy call-out, Single surprise fact]
- "Which suggestions to adopt?" (multi-select) → [Add a personal story, Include data caveat, Flip the framing, Skip all]
- "Where to place the caveat?" (single-select) → [In the carousel (Recommended), In the caption, In the first comment, Skip]

### Check position log

Read `references/position-log.md` silently. Only surface a conflict if one exists, and use AskUserQuestion to let the user decide how to handle it. If no conflict, say nothing.

### Framework opportunity

If the post describes a repeatable process the user created, suggest naming it via AskUserQuestion (one option = suggested name, another = "skip"). Target: roughly one named framework per month. Skip for shared/found tactics.

---

## Step 1c: Editorial review

**Skipped in quick mode.** For all other posts, run this before writing.

Do a light web search on the topic (current conversation, risks, data points), then present a structured editorial review.

### Editorial review format

**Core angle**
2-3 sentences. The single strongest take for this post. Ground it in personal experience or a concrete observation when possible.

**Alternative angles**
3-4 bullets. Each: bold label + 1 sentence explaining the direction. Include at least one contrarian or unexpected angle. Push beyond the obvious.

**Risk assessment**
- **High risk**: Could trigger backlash, misinterpretation, or reputational damage. Who would push back and why.
- **Medium risk**: Might polarize a portion of the audience. Explain the nuance.
- **Low risk**: Minor concerns, easy to mitigate with a disclaimer or reframe.
- If the topic is genuinely low risk across the board, say so and move on.

**Gut check**
- Is this idea on the right track? Honest yes, no, or conditional with reasoning.
- Is the thinking correct? Flag logical gaps, weak assumptions, or missing context.
- What else should be considered? Blind spots, adjacent topics, context the user may not have thought about.
- Is the angle strong enough to stand alone? Or does it need a stronger hook or combination?

**Suggestions before production**
3-5 specific, actionable bullets. Examples: add a personal story, include data, flip the framing, add a disclaimer, show a screenshot, lead with a question. Each immediately usable.

**Hook directions**
3-5 potential opening lines. Varied styles: bold claim, personal confession, provocative question, surprising stat. Ready to copy and test.

**"So what?" test**
After reading this post, what does the reader do differently? If the answer is nothing, flag it via AskUserQuestion: "This post has no clear takeaway. Want to add an action step, or ship as an observation post?"
If the post has a clear action or takeaway, pass silently.

**Differentiation check**
Has this topic been covered heavily on LinkedIn or Twitter? Check during research. If yes, flag it via AskUserQuestion: "This topic has been posted about a lot. Your version needs a personal angle or unique spin. Can you add one, or should we reframe?"
If the post is already differentiated (personal data, unique method, contrarian take), pass silently.

### Engagement strategy (required)

Predict the primary and secondary engagement types. Then define specific tactics for this post.

Primary engagement types and their triggers:
- **Saves**: Post contains reference material (tool lists, stat collections, process steps, prompt templates, comparison tables, checklists). People save what they can't memorize but will need later. Density drives saves, not depth.
- **Comments**: Two tiers. **Volume comments**: giveaway keyword drops, quick reactions. Good for algorithm signal. **Quality comments**: specific questions from practitioners ("how did you set up the Perplexity integration?"). These start relationships and lead to DMs. Optimize for quality comments by making content that prompts specific questions, not just keyword drops. When there's no giveaway, quality comments should be the target.
- **Shares**: Post teaches a specific skill or contains a visual someone would forward to look smart or helpful. "Send this to someone who..." framing. Stat highlights and quote cards are inherently shareable. Shares put your name in front of new audiences.
- **Profile visits**: Post shows real work (screenshots of automations, dashboards, results) that creates curiosity about who built it. Show don't tell is the profile visit engine. **Profile visits should be primary or secondary on most posts.** This is the highest-value engagement because it converts attention into relationships. Every post should make someone want to know more about who made this.

**Weighting guidance (internal, never expose):**
- Profile visits are undervalued by most creators. Weight them higher than shares.
- The save + profile visit combo is the ideal outcome: they bookmark your content AND check who you are.
- Volume comments (giveaway keywords) have diminishing returns. Use them for posts with downloadable assets, not as a default.
- 60%+ of posts should include screenshots of real work. This is the single biggest lever for driving profile curiosity.

For each post, output:
```
PRIMARY: [saves/comments/shares/profile visits]
SECONDARY: [one or two others]
TACTICS:
- [specific tactic 1 for this post]
- [specific tactic 2 for this post]
- [specific tactic 3 if applicable]
```

Not every post can maximize all types. Pick 1-2 and go hard. The tactics should be concrete and specific to this post's content, not generic advice.

**Save optimization (when saves are primary or secondary):**
- Structure at least one visual as a "reference card": tool list with use cases, stat table, process checklist, or prompt template. Dense and scannable.
- Add a save hint in the caption body (not the CTA position). Place it near where the reference value is described. Examples: "Save this for when you build yours." / "Worth bookmarking if you're planning outreach." / "You'll want this later."
- On the most reference-heavy slide or single image: add "Save for later" in muted text near the bottom. Subtle, not a banner.
- Single images with reference value (tool tables, stat comparisons, process overviews) get save treatment too. Saves are not carousel-only.
- **Tool/software list in caption:** When the post references a stack, workflow, or multi-tool setup, list the tool names directly in the caption body (e.g., "The stack: Clay, Instantly, Vapi, Apollo, GoHighLevel."). Strip TLD suffixes from tool names (see "No accidental links" rule). If a tool name is not self-explanatory or does not appear in the slides, add a short descriptor (e.g., "Firecrawl (web scraping for LLMs)"). Keep descriptions to 3-5 words max. This makes the caption a standalone reference people save even without swiping through the carousel.

**Comment optimization (when comments are primary or secondary):**
- **Quality comments** (default target): Structure content to prompt specific follow-up questions. Leave one detail partially explained so practitioners ask about it. "I used Perplexity for the research layer" makes people ask "how?" without you needing to ask a question.
- **Volume comments** (giveaway posts only): "Comment [keyword]" CTA drives volume. Reserve for posts with a downloadable asset. Not every post needs a keyword CTA.
- Credit someone by name/tag. They often reply, which seeds the thread and puts you in front of their audience.
- First comment strategy: always post a first comment that adds context, a behind-the-scenes detail, or a follow-up question. Never just drop a link. The first comment sets the tone for the thread.
- For opinion posts: end with a genuine question or a statement people will want to react to.

**Share optimization (when shares are primary or secondary):**
- Bonus assets (stat highlights, quote cards, standalone tables) must make the sharer look smart. They need to make sense with zero context.
- Teaching posts ("here's how to do X") get shared more than opinions.
- "Send this to someone who [specific situation]" framing when it fits naturally. Never forced.

**Profile visit optimization (apply to most posts, not just when explicitly primary):**
- Screenshots of real work (automations, dashboards, code, results) create curiosity. Default to including at least one screenshot of real work on 60%+ of posts. This is the single biggest lever.
- Show don't tell: demonstrate capability through actions, never claim it. The work speaks.
- Incomplete reveals: show the output or result, reference the full method on the site. People click the profile to learn more. "Full breakdown on my site" is one pattern. Better: leave one interesting detail partially explained so people ask about it or click to find out.
- Every post should pass the "curiosity test": after reading this, does someone want to know more about who made this? If not, consider adding a screenshot, a specific tool mention, or a behind-the-scenes detail that creates that pull.

**Algorithmic reach multipliers (apply to all posts):**
- Post mid-morning in the audience's timezone, when they are active. The first 60-90 minutes determine distribution.
- Save + comment combo is the strongest algorithm signal on LinkedIn.
- Carousel dwell time counts: more slides = more time on post = more reach.
- Early engagement matters most. First comment seeds the thread immediately.

### Caveat placement

When research reveals caveats, downsides, or risks about the tactic or topic (e.g., "Google can remove extensions used for link building"), ask the user where to include them via AskUserQuestion:
- "In the main caption (adds credibility and shows balanced thinking)"
- "In a carousel slide (if format is carousel, dedicate a slide to caveats)"
- "In the first comment only (keeps the caption clean, adds context below)"
- "Do not include (skip the caveat entirely)"

Never silently decide where caveats go. Always ask. Including caveats in the main caption can make the post stronger by showing the author thinks critically, not just promoting a tactic.

### Skill demonstration check (internal, never expose)

Which marketable skill does this post demonstrate? Name it (e.g., "SEO strategy", "automation building", "AI tool selection", "growth experimentation", "data analysis"). If the post is interesting but does not demonstrate a skill someone would hire or pay for, flag it: "This post is engaging but does not showcase a marketable skill. Want to add a practical angle, or ship as-is?" Check position log and recent posts to track skill coverage over time. If one skill is underrepresented over the past month, suggest it for the next post.

### "Would I hire this person?" test (internal, never expose)

After writing the caption, ask internally: if a hiring manager or potential client reads only this post, does it demonstrate a skill they would pay for? If no, flag in editorial review. Not a blocker. The user decides. Some posts are for engagement and brand warmth (personal, family), not skill demonstration. That is fine. But the balance should lean toward posts that show capability.

### Connection-building signal check (internal, never expose)

Does this post create a natural reason for someone to connect or DM? Not a CTA, but an embedded trigger. The best triggers feel accidental, like a detail that makes a specific type of person think "I need to talk to this person."

Trigger types (pick the strongest fit, don't force all):
- **Tool or method mention**: naming a specific tool or approach invites "how did you set that up?" questions.
- **Incomplete reveal**: showing the result but not the full method. People DM to ask for the rest.
- **Crediting someone**: tagging a person or source often brings their audience to your profile.
- **Specific number or result**: "cut reporting from 2 hours to 15 minutes" makes people want the process.
- **Behind-the-scenes screenshot**: showing the actual dashboard, automation, or code invites specific technical questions.

If the post has none of these, suggest adding one. A single tool mention or screenshot can be the difference between "interesting post" and "I should connect with this person."

This check is about creating inbound interest naturally. Never make the trigger feel like a pitch. The content demonstrates, the reader self-selects.

### Content pillar balance check

Check the last 4-8 posts in scheduled-published/ and position-log.md. Which pillars have been covered? If one pillar (growth marketing, AI and tools, automation, behind the scenes, operator mindset) has not appeared in the last 4 posts, suggest it for this post or the next one. The goal: roughly equal rotation across pillars over each month. Do not force a pillar change if the current brief is strong. Just surface the gap.

### After the review

- **Clean review (low risk, angle is strong):** Present the review and proceed to Step 2 without waiting. The user can interrupt if they want changes.
- **Decision needed (high risk found, or a significantly stronger angle exists):** Use AskUserQuestion with concrete options before proceeding.
- **Never block on a clean review.** The editorial review is informational, not a gate. Show it and keep moving.
