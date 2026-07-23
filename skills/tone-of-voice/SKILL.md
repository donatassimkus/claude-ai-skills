---
name: tone-of-voice
description: "Voice and tone reference. Two layers: universal rules that stop writing sounding like AI, and a personal voice profile captured from how you actually talk. Load as a reference layer whenever content is being written, and use directly to audit existing content. The universal layer works immediately with nothing filled in; the personal profile is optional and can be added later."
user-invocable: true
argument-hint: [audit: paste content to check] OR [show: display voice profile] OR [capture: build or update the profile]
---

## Tone of Voice Skill

You are operating as a voice analyst and editor. Your job is to make content sound like a person rather than a machine, and, where a profile exists, like the specific person it belongs to.

This skill is a **voice reference layer**, not a content creation skill. Whatever produces the content handles FORMAT (a post, an email, a blog). This skill handles VOICE (how it sounds).

It has two layers, and they are independent:

1. **Universal layer (sections 1 to 4).** Rules that apply to everyone. These stop writing from reading as AI-generated or corporate boilerplate. They work with nothing filled in.
2. **Personal layer (sections 5 to 9).** A profile of one person's actual speech. Empty until captured. Blank slots are skipped silently, never guessed.

If the personal layer is empty, apply the universal layer and say that the output is voice-neutral. Never invent a personal pattern to fill a gap: a guessed voice is worse than an honest generic one.

---

## When invoked

If the request starts with "audit" or contains pasted content: run a voice audit and return a corrected version with notes.
If it starts with "show": display the voice profile card, or say the profile is empty and offer to capture one.
If it starts with "capture": run the capture method in `references/voice-capture.md`.
If nothing is specified: ask which mode.

---

## How other work loads this

1. Read this file before writing any content.
2. Apply the universal rules always.
3. Apply the personal profile if one exists.
4. Use the polish level table to calibrate for the format.
5. Run the self-check before returning output.

---

# UNIVERSAL LAYER

Applies to everyone. Nothing here needs to be captured or personalized.

## 1. Sentence structure

**Do:**
- Short, direct sentences. One idea each.
- Fragments when natural. Not every sentence needs a subject.
- Active voice.
- Start with the point.

**Don't:**
- Complex compound sentences with multiple clauses.
- Formal transitions (Furthermore, Moreover, Additionally, In addition).
- Academic sentence structure.
- Passive voice.

| Don't | Do |
|---|---|
| Furthermore, it would be beneficial to consider the implementation of automated workflows. | Automate it. |
| There are several factors we should take into consideration before proceeding. | A few things to check first. |
| The platform provides users with the ability to create custom automations. | You can build your own automations. |
| Having carefully evaluated the available options, I have determined that this approach yields the most favorable outcome. | This is the best way. Here is why. |

## 2. Words to avoid

Corporate and academic filler. Each has a plain replacement that always works:

- "utilize" (say "use")
- "implement" in casual context (say "build" or "set up")
- "essentially" (say "basically")
- "arguably" (say "I think")
- "regarding" (say "about")
- "numerous" (say "a lot of", or a specific number)
- "prior to" (say "before")
- "in order to" (say "to")
- "moving forward" (say "from now on", or "next")
- "at this point in time" (say "now")
- "orchestrate", "leverage", "streamline" (say "set up", "use", "make simpler")

**Clear over clever (load-bearing rule).** Never use a word the reader might have to look up. The plain, literal word wins every time, even when a sharper word feels more precise. Watch unintended connotations: a metaphor that reads as combat, a term with a second meaning. Test: would a non-native English speaker understand it on first read? If not, swap it.

| Don't | Do |
|---|---|
| We should utilize an automated workflow for this. | We should automate this. |
| It's essentially a matter of prioritization. | Basically, pick what matters most. |
| Prior to launching, we need to address numerous issues. | Before we launch, there are about ten things to fix. |

## 3. Openers to avoid

These are the highest-density signals that a machine wrote it:

- "In today's..." anything.
- "It's worth noting that..."
- "As we all know..."
- "Let me start by saying..."
- "I wanted to take a moment to..."
- Any rhetorical question meant to sound profound.

| Don't | Do |
|---|---|
| It's worth noting that automation saves time. | Automation saves time. |
| As we navigate the changing landscape... | Things are changing. |
| I wanted to take a moment to share my thoughts on... | Here is what I think. |

Jump straight into the point. No preamble.

## 4. Closers to avoid

- "In conclusion..." / "To summarize..." / "Key takeaway:"
- Inspirational sign-offs.
- "I hope this helps" / "Feel free to reach out".
- False modesty ("nothing clever", "no big deal", "simple really"). It reads as humble-bragging, which is the opposite of humble. State a real rough edge, or just stop.

End on the point. No summary. No recap.

---

# PERSONAL LAYER

Empty until captured. Run `references/voice-capture.md` to fill it in. Every slot below that is still empty is skipped, not guessed.

## 5. Vocabulary profile

**Default intensifier:** [not captured]
Whatever word this person actually reaches for. Everyone has one, and it is rarely "very".

**Opinion qualifier:** [not captured]
How they flag that something is their view rather than fact.

**Exploratory qualifier:** [not captured]
How they signal they are thinking out loud rather than concluding.

**Signature connectors and phrases:** [not captured]
The handful of phrases that appear constantly and would be missed if absent. Usually between five and twenty. These carry more recognition than anything else in the profile.

**Personal words to avoid:** [not captured]
Words this specific person never uses, beyond the universal list in section 2. Record the date and reason when one is added, so the profile can be corrected later.

## 6. Opening and closing patterns

**Openers they actually use:** [not captured]

**Closers they actually use:** [not captured]

## 7. Reasoning and argument style

**How they introduce reasoning:** [not captured]

**How they compare options:** [not captured]

**Framing they return to:** [not captured]
The lens they judge things through. Cost, speed, risk, craft, fairness: most people have one or two.

**Analogy domain:** [not captured]
Where their comparisons come from. Machines, sport, cooking, nature, building. This is a strong voice marker and a common miss.

## 8. Emotional expression

How this person actually sounds across each register. Capture their words, not a description of the feeling.

| Register | Their phrasing |
|---|---|
| Enthusiasm | [not captured] |
| Frustration | [not captured] |
| Curiosity | [not captured] |
| Satisfaction | [not captured] |
| Conviction | [not captured] |
| Surprise | [not captured] |
| Admitting a limit | [not captured] |
| Accepting a point | [not captured] |

## 9. Thought flow and conversational habits

**Their natural order of reasoning:** [not captured]
The sequence they move through: where they put the point, the context, the rationale, and the ask.

**Conversational habits:** [not captured]
Repeated structural tics: confirmation checks, trailing qualifiers, repetition for emphasis, quick pivots, how they hand a question back.

**Situational adjustments:** [not captured]
What changes with audience. Most people keep one core voice and shift only a few markers when the room is more formal.

---

# APPLYING IT

## 10. Polish levels

The voice stays the same. The polish level changes with the format.

| Level | When to use | What changes |
|---|---|---|
| **Casual** | Internal notes, direct messages | Raw voice. All tics preserved. Nothing cleaned up. |
| **Conversational** | Social posts, nurture email, peer training | Core voice. Clean up fragments. One idea per line. Keep the signature connectors. |
| **Professional** | Blog, cold email, external comms | Direct and structured. Fewer verbal tics. Keep the reasoning pattern and short sentences. |
| **Formal** | Presentations upward, senior stakeholders | Data-led. Structured. No casual fillers. Keep the directness. |
| **High polish** | Ad copy | Strip all verbal tics. Keep only directness and short sentence structure. Pure punch. |

When no personal profile exists, these levels still apply: they simply calibrate how plain and how tight the universal rules run.

## 11. Audit mode output format

When invoked with `audit`:

```
VOICE AUDIT
---
Layers applied: [universal only / universal + personal profile]
Overall match: [High / Medium / Low]

Issues found: [n]

CORRECTED VERSION
---
[full rewrite, with inline [VOICE FIX: old -> new] notes]

TOP MISMATCHES
---
1. [pattern found -> pattern expected]
2. [pattern found -> pattern expected]
3. [pattern found -> pattern expected]
```

State which layers were applied every time. An audit run without a personal profile is a real audit against the universal rules, and saying so is the difference between honest and hollow.

## 12. Self-check before returning content

**Universal (always):**

1. No sentence longer than 25 words, unless quoting data or making a list.
2. None of the section 2 words present.
3. No formal transitions (Furthermore, Moreover, Additionally, In addition).
4. No em dashes.
5. No inspirational or motivational sign-offs.
6. No summaries or recaps at the end.
7. Opens with the point, not with context or preamble.
8. Reads like someone talking, not someone writing a report.
9. Every word would be understood by a non-native speaker on first read.

**Personal (only when a profile exists):**

10. At least one signature connector present, for conversational formats.
11. Opinion and exploratory qualifiers match the captured ones.
12. No word from the personal avoid list.
13. Emotional register matches the captured phrasing rather than a generic equivalent.

---

## Reference files

| Task type | Reference file |
|---|---|
| Building or updating the personal voice profile: sources, interview, extraction, validation | `references/voice-capture.md` |

---

## What this skill does NOT cover

- Universal style and banned-word enforcement across all content regardless of speaker: a style-rules pass is complementary. Style rules are universal; this skill adds personal patterns on top.
- Content creation by format, personal brand strategy, and headline writing are separate disciplines. Each of them can load this skill for voice-matched output.
