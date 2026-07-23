---
name: content
description: "Write and edit blog posts, landing pages, email sequences, ad copy, social posts, and outreach. Use when asked to write, edit, rewrite, repurpose, or create any content. Dedicated hook and headline craft, and style auditing of existing copy, are adjacent disciplines handled separately."
user-invocable: true
argument-hint: [content type] [topic or brief]
---

## Content Skill

Write like a human. Professional but conversational. Never like a press release.

**Project context is loaded from the active CLAUDE.md. Apply tone, audience, language (UK/American English), and brand voice from that context.**

---

## When invoked

$ARGUMENTS tells you the content type and topic/brief.
If the brief is thin, make a labeled assumption and proceed. Do not stall.

---

## Writing principles

> For LinkedIn posts tied to a personal brand strategy (content pillars, positioning, tone), work from that brand strategy first. This skill handles one-off content tasks without a brand strategy context.

> For voice-matched output that sounds like the user, load whatever voice or tone reference they keep and apply its patterns before writing. If they have none, ask for two or three samples of their own writing and match those.

- One idea per sentence.
- Short sentences. Active voice.
- Every sentence earns its place. Cut anything that does not add value.
- Write to a smart person who has no time for filler.
- No em dashes. Use colons, periods, commas, or restructure.
- No forbidden words: strip LLM tells and corporate filler. If the human keeps a banned-word list, apply theirs; otherwise cut the usual offenders (delve, leverage, unlock, foster, elevate, seamlessly, groundbreaking, streamlined, and their neighbours).
- Output must be paste-ready with minimal editing needed.

---

## Content types

### Blog posts / articles

Structure:
1. Hook: first sentence must earn the read. Fact, question, or bold claim. Always sentence 1. Never bury it after context.
2. Problem statement: why this matters to the reader right now. Always sentence 2, after the hook.
3. Body: headers every 200-300 words. Bullets where list makes sense.
4. CTA: one clear next step. No vague "learn more."

SEO rules (when applicable):
- Primary keyword in H1, first 100 words, meta description.
- Internal links to at least 2 related pages.
- One clear conversion goal per post.

### Landing pages

Structure:
1. Headline: outcome-focused, not feature-focused.
2. Subheadline: clarifies who it is for and what they get.
3. Problem/pain: make them feel seen.
4. Solution: how this product/offer fixes the problem.
5. Proof: social proof, numbers, case study, testimonial.
6. Offer: what they get, what it costs, what happens next.
7. CTA: one button. One action. No decision paralysis.
8. Risk reversal: guarantee, trial, free tier, or refund policy.

Hormozi offer checklist:
- Dream outcome: stated clearly?
- Time to result: how fast do they see value?
- Effort required: how easy is it?
- Risk reversal: what removes the objection?

### Email sequences

- Subject line: curiosity, specificity, or personal angle. No clickbait.
- First sentence: no "I hope this finds you well." Get to the point.
- One goal per email. One CTA.
- Follow-up sequence: 3-5 touches max. Each adds value or changes angle.

### Ad copy

- Hook in the first 3 words.
- Problem or desire in line 2.
- Solution and CTA in line 3.
- Test angles: pain, aspiration, social proof, urgency, curiosity.

### Social posts (LinkedIn, X, etc.)

- LinkedIn: hook line, white space, value, soft CTA. No hashtag spam.
- X: punchy, opinion-forward, or contrarian. Under 280 characters for impact posts.
- Repurpose rule: long-form content → 3-5 social variants. Each stands alone.

### Outreach messages

- Short. Very short.
- Specific to the recipient. One reason why you are reaching out to them.
- One clear ask. Not a pitch, a request.
- Follow-up: different angle, not a repeat.

---

## Output format

Deliver the content ready to use. No preamble. No "here is your copy."

For longer pieces, include:
- Word count
- Primary keyword (if SEO content)
- Suggested meta description (if SEO content)
- Internal link suggestions (if applicable)

For repurposing requests, deliver all variants in one response, labeled by channel.

---

## Quality gate

Before delivering, check:
- Does it sound human?
- Is there a clear CTA?
- Has every forbidden word been avoided?
- No em dashes?
- Could it be published with minimal editing?

If any check fails, fix before delivering.

---

## Adjacent disciplines (where this skill stops)

- Personal brand strategy — LinkedIn posts tied to content pillars, positioning, and tone
- Dedicated social post production — format selection, visual direction, and voice matching go deeper than the social section here
- Hook craft — hook type taxonomy and testing framework for any content opening
- SEO — keyword research, content strategy, and technical SEO for blog content
- Email marketing — sequence strategy, segmentation, and deliverability
- Cold outreach — cold email copy and follow-up sequences
- Paid media — ad creative strategy and testing frameworks

---

## Reference files

| Task type | Reference file |
|---|---|
| Named page templates (alternatives, vs comparison, listicles, use-case), Manus 21-blog playbook, humanize ChatGPT content, content engines with practitioner numbers | `references/kb-distilled.md` |
