# Format selection and writing

Loaded at Step 2 + 3 of the social-post skill.

## Tone enforcement (hard rules)

- Matching the user's captured voice baseline is not optional. Every caption must pass a voice check before output.
- **Clear over clever.** Use simple language. "Only 197 made the cut" not "27% survival rate." If a phrase sounds smart but a normal person would pause to decode it, rewrite it.
- **Active voice always.** "I built the strategy skill from" not "The strategy skill was built from."
- **No resume language.** Never write "a decade of hands-on experience", "extensive background", "proven track record." Say "my own experience" or skip the qualifier.
- **Auto-select polish level based on post type:**
  - **Professional polish** for: showcase posts (presenting something you built), giveaway/download posts, authority/credibility posts, process breakdowns with numbers. Every statement confident and direct. No hedging. No "I think" before facts. No "basically." The voice is still yours (short sentences, active, simple), but the version of you presenting, not chatting.
  - **Conversational polish** for: opinion/hot take posts, behind the scenes, observations, lessons, casual engagement. At least one signature connector ("I think", "basically", "super") and one opinion marker ("I think the key thing is..."). The voice of you talking to a friend.
- **Both levels share:** Grammatically correct, short sentences, active voice, simple language, no formal transitions, no fluff. The structure and directness stay the same. Only the confidence level and verbal tics change.

## Voice guardrail

The user is a builder and optimizer. Never frame posts as emotional, fearful, or vulnerable. Even personal topics (conflict, risk, uncertainty) should read as "I engineered a solution to this problem." Practical, systems-thinking, not sentimental. If the topic has emotional weight, the angle is still: here's what I built, here's how it works, here's why it's useful.

## Show, don't claim

Never state expertise, skill, or knowledge directly. No "I knew what to do", "my experience made the difference", "the skill didn't change", or "I did." Instead, show specific actions taken and results achieved. Let competence be inferred by the reader, never claimed by the author. If a post needs a punchline, make it about the outcome or the method, not about you being good. Facts and examples speak louder than self-reference.

## Numbers formatting (hard rule)

Always write numbers as digits, not words. "4 days" not "four days." "2-3 weeks" not "two to three weeks." "60 websites" not "sixty websites." This matches the user's natural writing style and reads faster on social. Exception: "one" when used as a pronoun ("one of the best") rather than a quantity.

---

## Step 2: Select format

| Format | Best for | Signals |
|---|---|---|
| **Text post** | Opinions, lessons, hot takes, observations | Short idea, single insight, no process or steps |
| **Carousel** | Step-by-step processes, frameworks, lists, comparisons | 3+ steps, visual breakdown, "how I did X" |
| **Image post** | Data points, quotes, announcements, single stats | One number, one visual idea, announcement |
| **Stat highlight** | Single metric or number is the main point | "We hit X", "Saved Y hours", results with one hero number |
| **Quote card** | Standalone statement, opinion, punchy takeaway | Single line, no process, no steps. No photo needed. |
| **Document post** | Mini case studies, deep breakdowns, long processes | 8+ steps, needs more depth than a carousel |

Auto-select based on content. State the selection and why in the output metadata. User can override.

**Screenshot override:** If screenshots exist in `inbox/screenshot/`, default to **carousel** format. Screenshots + contextual text slides make natural carousel content. Text-only posts waste the visual asset. **Exception:** if the user explicitly requests a different format, user intent wins.

**Value bomb signal:** If the brief contains "deep one", "value bomb", "full breakdown", or similar depth signals, default to **carousel** (target 7 slides, go up to 10+ if the content needs room), pack with actionable steps, keep the caption short and drive to first comment for the link. Mark output metadata as `DEPTH: VALUE_BOMB`.

**Video deprioritization (2026):** LinkedIn deprioritized video content in favor of carousels and PDFs. Video reach plummeted in 2025. Avoid video format unless the content is <60 seconds and highly specific. It is no longer a growth format on LinkedIn.

**Format rotation (2026 rule):** Do not suggest the same format for consecutive posts. Rotating between carousel, text, text+photo, and poll boosts follower growth 40%+. Check the user's last post format (in scheduled-published/) and suggest a different one.

**Niche specificity (2026 algorithm):** LinkedIn's AI now matches niche topics to niche audiences. The more specific to growth marketing, AI, and automation, the better it performs. Generic marketing advice gets buried. Always lean into the user's specific expertise rather than broad takes.

**First 90 minutes (2026 algorithm):** LinkedIn now decides distribution in the first 60-90 minutes after posting. Early engagement determines whether the post reaches a wider audience. This makes posting time and audience timezone alignment more important than before.

---

## Step 3: Write the post

### Formatting rule (hard rule, all platforms)

**One sentence per line. Blank line between lines. No paragraphs. Ever.**

Example of correct formatting:
```
I built an automation that saves me 3 hours a week.

It took me 45 minutes to set up.

Here's how it works.

Step 1: I recorded my manual process for one day.

Step 2: I mapped every repeatable action.

Step 3: I built it in n8n and connected to my CRM.

Now it runs on autopilot.

What's one process you keep doing manually that should be automated?
```

If the content is too long for a caption, the format changes (carousel, document, video). The caption stays short and drives engagement with the asset.

### Audience language rule

Write in words the user's audience actually uses. If a word has a specific meaning in dev or product culture that differs from common usage, use the plain alternative. Test: would someone in that audience use this exact word to describe the same thing? If no, rephrase. Words with one unambiguous meaning inside the field are fine, including tool and product names the audience uses daily. Words that mean one thing to developers and something else to everyone else (shipped, pipeline, deployed, checkpointed) are not. Two hard substitutions regardless of audience: "leverage" is always "use", and "utilize" is always "use". When in doubt, describe what the thing does instead of labelling it. This applies to captions and image text alike.

### Topic signal optimization (2026 algorithm)

LinkedIn's AI classifies your content by topic and serves it to interested audiences. Help it match correctly:

- Use full terms on first mention, abbreviation after. "Domain Rating (DR)" not just "DR." "Search Engine Optimization (SEO)" only if the audience might not know it; for growth marketers, "SEO" alone is fine.
- Name specific tools and platforms. "Claude Code" not "an AI tool." "n8n" not "an automation platform." "LinkedIn" not "this platform." Specific names are stronger topic signals.
- Include the parent category at least once. If the post is about a specific tactic, mention the broader category too. "This backlink strategy" + "SEO" in the same post. The tactic is niche, the category ensures the right audience sees it.
- Do not repeat terms unnaturally. One mention of the full term is enough. This is topic signaling, not keyword stuffing. If it reads like it's optimized, rewrite it.
- Carousel slide text counts. LinkedIn extracts text from PDF carousels. Use specific terms in slide content, not just the caption.

### Carousel caption rule (hard rule)

When format is carousel, the caption is a companion, not a transcript. Maximum 15 lines. The carousel tells the story, the caption sells the swipe. Hook, one line per key point, the hero number, swipe CTA. Do not retell the carousel content in the caption. If the caption repeats what the slides say, it is too long.

### Caption structure

1. **Hook** (line 1): Select deliberately from a fixed taxonomy of verbal hook types rather than writing by feel. Must earn the scroll-stop. No "I'm excited to share." No preamble.
   - **Specificity rule (hard rule):** When the brief contains a specific location, situation, or identity, the hook MUST include it. Generic hooks fail the call-out test. Apply the cocktail-party effect: a reader's attention snaps to something that names them or their exact situation, so name the place, the situation, or the person. If the hook could apply to anyone anywhere, it's too weak. Specificity is the scroll-stopper.
   - **Hook cascade rule:** When the hook changes after initial production, cascade the update to: all platform captions, cover slide(s), single-image, and carousel PDF. The hook sets the tone for everything downstream. A hook change is a full regeneration, not a line swap.
2. **White space**: Blank line after the hook. Always.
3. **Body**: Deliver on the hook's promise.
   - One sentence per line.
   - Blank line between every line.
   - 3-7 bullets or numbered steps for process posts.
   - Build tension or curiosity through the middle.
4. **Save hint** (in body, not CTA): When the engagement strategy targets saves, add one natural save line in the caption body near where reference value is described. Not at the end. Examples: "Save this for when you build yours." / "Worth bookmarking if you're planning outreach." / "You'll want this later." Skip for opinion/hot take posts.
5. **CTA** (last line): Default is follow CTA. The CTA type adjusts based on engagement strategy:
   - **Follow CTA** (default): "Follow for more on growth marketing, AI, and automation." Use for most posts. Builds audience.
   - **Giveaway CTA**: "Comment [keyword] and I will send you [asset]." Use when post has a downloadable resource.
   - **Question CTA** (only when it adds value): For controversial takes or genuine debate starters. Must feel natural, not forced.
   - **Statement CTA**: Strong closing line when the post needs no ask. The content earns engagement by being good.
   - **Share prompt** (rare, secondary): "Send this to someone who [specific situation]." Only when teaching a specific skill and it fits naturally.
   - Avoid: ending every post with a question. It looks robotic. Let the content breathe.
   - The save hint lives in the body, not the CTA position. The final line is always follow, giveaway, question, or statement.
6. **No accidental links (hard rule):** Never include TLD suffixes (.com, .io, .ai, .co, .org, etc.) in tool or brand names in captions. LinkedIn treats any word containing a TLD as a URL and penalizes reach. Write "Make" not "Make.com", "Apollo" not "Apollo.io", "Instantly" not "Instantly.ai". Only exception: the user's own URLs when explicitly requested. This applies to all platform captions.

### Giveaway engagement tactics (LinkedIn)

When the post gives something away (free download, ungated resource, tool, template), use these tactics to maximise engagement before sharing the link:

1. **Comment CTA:** "Comment [keyword] and I will send you the link directly." One word, low friction. Every comment is an algorithm signal. Pick a keyword that matches the topic (e.g., "SEO", "TEMPLATE", "SKILL").
2. **Connection prompt:** "Make sure we are connected so I can message you." Required for DMs on LinkedIn. Natural, not pushy.
3. **Save prompt:** "Save this post so you can come back to it later." Saves are a strong LinkedIn signal. Use "Save" (LinkedIn's terminology), not "bookmark."
4. **No link in first comment on publish.** Do NOT post the link immediately. The comment CTA only works if people have to comment to get it. Post the link as a public comment 2-4 hours later, after the initial engagement wave.
5. **DM each commenter** with the link + a short personal message. This builds connections, not just engagement.

**File output for giveaway posts:**
- `first-comment.txt`: The delayed public comment (posted 2-4 hours later). Pure copy-paste, no instructions or labels.
- `dm-reply.txt`: The DM message sent to each commenter. Pure copy-paste, no instructions or labels.
- Both files must be ready to paste directly. No headers, no explanations, no "Section 1" labels. Just the text.

**When NOT to use:** Regular posts without a giveaway. Standard posts use the normal CTA patterns (statement, question, follow, direct). Only use giveaway tactics when there is a concrete, downloadable resource being offered.

### Teaching structure (for how-to and lesson posts)

Auto-select when the content teaches something actionable: a method, a process, a lesson with a replicable takeaway. This replaces the default body structure.

1. **Problem** — What specific problem does this solve? One sentence. Make the reader feel it.
2. **Method** — How to solve it. Steps, tools, approach. This is the meat. Be specific enough that someone can follow along.
3. **Result** — What happened. Numbers, outcomes, before/after. Proof it works.
4. **Your turn** — What they can do right now. Not a question. An action. "Try this on your next project." / "Run this audit today."

This structure builds authority because it teaches, not tells. The reader learns something they can use.

### Length strategy

| Length | Lines | Use for |
|---|---|---|
| Short | 1-5 | Opinion, hot take, observation |
| Medium | 6-15 | Lesson, mini-breakdown (default) |
| Long | 16+ | Only for step-by-step or case study. Consider carousel instead. |

Default to medium. If the content needs more than 15 lines, move the depth into a carousel, document, or video. Caption stays short and scannable.

---

## Step 3b: Caption and outline confirmation checkpoint

**After writing the main LinkedIn caption, show it alongside the visual outline. Then ask confirmation questions.**

What to show (adapts by format):
- **Carousel:** caption + metadata block + slide-by-slide outline (title + key point per slide)
- **Text + photo:** caption + metadata block + photo source + planned overlay/stat/quote assets
- **Text + screenshot:** caption + metadata block + screenshot usage plan + standalone variant plan
- **Carousel + screenshots:** caption + metadata block + mixed slide outline (text slides + screenshot slides) + Cover A/B plan

The user must see the full picture before confirming. Never ask confirmation questions without showing the outline first.

Use AskUserQuestion to verify:
- "Here is the caption and outline. Does this match what you meant?"
- "I am including these facts/claims: [list any facts not in the original brief]. All correct? Remove any?"
- "Tone: [conversational/professional]. Audience: growth marketers, AI, automation. Sound right?"

**Minimum 2 questions at this checkpoint.** Even if everything looks perfect.

Only after confirmation: generate all platform captions (Twitter, Instagram, Facebook, YouTube) and LinkedIn angle variations.
