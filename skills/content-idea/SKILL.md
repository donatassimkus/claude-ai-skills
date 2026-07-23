---
name: content-idea
description: "Capture a content idea fast, mid-work, into your content board as a channel-agnostic seed: one insight that could become a blog, a social post, or a video. Captures first, asks 1-2 questions only when the card would otherwise be cryptic later, then shows the card back so you can correct it in one line. Use when the user says /content-idea, 'capture this as a post idea', 'save that as a content idea', 'that would make a good post / video / article', or wants to log an idea without stopping to draft it."
user-invocable: true
argument-hint: [the idea in one line] [optional: blog | video | tweet | thread | carousel | short | a pillar | a context]
---

## /content-idea — fast, channel-agnostic idea capture

Capture a content idea into the operator's **content board** and return.

**Capture settings.** This skill reads a small settings note held beside it for the values that are yours rather than the method's: the board target, the project list, the content pillars, the primary channel, and any naming rule about what must stay out of public copy. The steps below are the universal capture method; your specific values live in the settings. If no settings note exists yet, run the method and leave project/pillar blank.

**Capture the insight, not the post.** An idea arrives channel-agnostic: the same point can become a blog article, a LinkedIn post, a short, or all three. Record the seed (the insight, the pillar it serves, which channels it could fill). Format, hook, and final channel are decided later at production, per channel. Do NOT lock it to one platform on capture.

### The governing bar: the 6-month test

A card must stand alone. Before you file, check: **reading this card cold in 6 months, with the originating chat long gone, would the operator know exactly what it meant and why it was worth posting?** And: could the future repurpose step build from it without the chat?

- Passes → file silently, fast. (Usually true mid-work in a rich chat.)
- Fails → first pull more from the current context (the example, the data point, the realization that sparked it) INTO the card. If it still fails, ask 1-2 targeted questions to close the gap.

This bar is what decides when to ask. It is not a fixed Q&A step.

### The contract: capture, confirm, move on

The operator fires this mid-work. Grab the idea, structure it, file it, show it back, hand control straight back. Hard rules:

- **Default to silent capture.** Ask questions ONLY when the 6-month test fails or the pillar/channel is genuinely ambiguous. Maximum 1-2 questions, one batch, never a string. If you find yourself wanting a third question, stop and just capture what you have.
- **Do NOT draft the full post.** That is production, later, when the idea is promoted past Idea.
- **Do NOT switch the operator's current task.** They are in the middle of something else.
- **Confirm by showing the card, then stop.** No next-step menu, no "want me to draft it?". The card is saved; the operator drives the next move.

Speed is still the feature. The clarification path exists to prevent cryptic cards, not to turn capture into an interview.

### Capture modes (all land in the same board)

The board is a shared global sink: wherever you capture from, the card lands in the Content tab. Three ways in:

- **Fresh chat** — "here's a content idea: X". No surrounding context, so the 6-month test fails more often; expect to pull from memory about the operator and to ask 1-2 questions. This is the thinnest mode by nature; that is fine.
- **Mid-work, inline** — "capture this". Richest context. Pull the relevant proof, example, or realization from the conversation INTO the card so it stands alone after the chat is gone. Usually passes the test, so capture silently.
- **Forked branch (no-interrupt)** — the operator forks the conversation and runs `/content-idea` in the branch; the main thread stays untouched. A conversation fork inherits the full chat, so capture is as good as inline, and the card still lands in the same shared board. Capturing concurrently is safe (the engine is a single atomic writer). Do NOT capture via a spawned subagent: a subagent only sees the prompt and loses the live context, which is why subagent-capture was abandoned. Branch = good; subagent = not.

### Step 1 — read the fragment + any signals

The argument is the raw idea, in the operator's words. If it is a voice dump (from any dictation tool) or a long ramble, extract the core insight; capture the point, not a verbatim transcript, and mine the extra material to enrich the card. Pull explicit signals:

- **Candidate channels** → set Channels (multi). Detect every channel the idea could serve, not one:
  - "blog / article / guide" → `Blog` (usually also `LinkedIn`)
  - "tweet / X / twitter" → `X`; "thread" → `X` + `LinkedIn`
  - "youtube / video / demo / walkthrough" → `YouTube` (often also a `Short`-type clip)
  - "reel / short / tiktok" → add a short-form channel
  - "newsletter / email" → `Newsletter`
  - default primary → your configured primary channel, but never as the ONLY channel if the idea is clearly bigger.
- **Format / type words** → set Type (optional, the eventual primary format): "video" → `Video`, "tweet/thread" → `Thread`, "carousel" → `Carousel`, "short/reel" → `Short`, "article/blog/guide" → `Article`, else `Post`. Leave Type blank if the format is genuinely undecided.
- **Pillar words / topic** → set Pillar to one of your configured content pillars. Leave blank if off-pillar (e.g. a passing personal thought). If you cannot infer it confidently, leave it blank rather than mis-file, or make it one of your 1-2 questions.
- **Context words** → set Context: match the fragment to one of your own contexts, meaning the separate spheres of work you keep firewalled from each other (a day job, a venture, your own personal output). Use the short code you chose for that sphere in your settings, spelled exactly as configured. When unsure, default to the personal one rather than guessing, since a mis-filed card can surface work material in a personal channel.
- **Project** → which property the idea is for. Route to the matching project from your settings project list; use the default project when the fragment does not signal one.
- **A date** ("post Friday", "next week") → set Timeline. Otherwise leave it blank; it stays in the backlog.

If the fragment is genuinely empty (just `/content-idea` with nothing), ask ONE short question: "What's the idea?" Then proceed.

### Step 2 — enrich + dedup-check

Fill these from the fragment + the surrounding work:

- **Task name** — the idea as a short working title (a handful of words). The card's headline in every view.
- **Angle** — the channel-neutral take or structure in one line ("the counterintuitive bit", "3-step teardown", "before/after"). The heart of the seed.
- **Summary** — one-line gist, written to pass the 6-month test on its own.
- **Pillar** — which of your pillars it serves, or blank if off-pillar.
- **Channels** — the 1-3 candidate channels from Step 1.
- **Audience** — who it is for, if clear ("founders", "SEO operators", "AI builders"). Optional.
- **Hook** — one rough first line, OPTIONAL. The final hook is written per channel at production; only jot a rough one if it came out with the idea.
- **Source** — where it came from. Name the live context ("from the X build", "the Y bug today") or "standalone".
- **Status** — always `Idea`.

**Dedup-check before filing:** scan the board's existing titles/angles. If this is close to an existing card, do not silently create a near-duplicate; flag it and ask whether to fold into that card or keep it separate.

**Multiple ideas in one message:** file each as its own card. But do not shatter ONE idea with several facets into several thin cards; one insight is one card.

Apply your own writing rules to Angle / Hook / Summary (whatever house style, banned words, and voice rules you keep; active voice by default). Keep it fast and rough. Seeds to react to, not finished copy.

**Content pillars, voice, and any naming rule** come from your settings. Set Pillar to one of your pillars, or blank if off-pillar. Follow your voice rule and, where you keep one, your naming rule: the names you have decided must stay out of public copy stay out of Angle and Hook too, because those fields feed the post later and a name that reaches the card tends to reach the draft.

### Step 3 — ask only if the card would be cryptic

Run the 6-month test on the card you just built. If it passes, skip straight to Step 4. If it fails (or pillar/channel is genuinely ambiguous), ask 1-2 targeted questions, one batch, then file. Good question shapes: "What's the core point in one line?", "Which pillar?", "Any proof or example behind it?". Never more than two.

### Step 4 — file it through a single writer

Never blind-edit the board's underlying file. Go through whatever single write path the board exposes (its API, its CLI, or one script that owns the file) so the write is serialized, atomic, and option-validated. If the board is a plain file you own, put ONE writer in front of it rather than editing it from several places: concurrent capture is a normal case here, and last-writer-wins silently loses cards. Build the op as JSON, write it to a temp file (avoids shell-quoting issues with apostrophes), then mutate:

1. Write the op to a temp JSON file. Channels is a multi-select: pass it as a comma-separated string.
   ```json
   {"op":"add","allow_new":true,"props":{
     "Task name":"...","Status":"Idea","Pillar":"<one of your pillars>","Project":"<your default project>",
     "Channels":"LinkedIn, Blog","Type":"Post","Context":"Personal",
     "Angle":"...","Audience":"","Hook":"...","Source":"...","Summary":"..."}}
   ```
   Include `"Timeline":"MM/DD/YYYY"` only if a date was given. Omit Type or Pillar (leave out or "") when undecided/off-pillar. An `allow_new` flag lets a new Channel/Type/Context option register if the operator coins one; keep that behaviour, since capture stalls the moment a new option is rejected.
2. Send the op through your board's write path, passing the temp file rather than inlining the JSON on the command line.

   Whatever the write path returns, keep the new card's ID: Step 5 needs it to build the mandatory card link. Have the writer stamp an `Updated at` value itself rather than setting it by hand.

For several ideas, file each as its own `add` op (loop), then confirm the batch.

### Step 5 — show the card back WITH its link, then stop

The card is already saved. Show it back compactly so the operator can eyeball it and correct in one line. **The card's direct link is MANDATORY: every capture ends with it, no exceptions.** Build it from the new card's ID using your board's own link scheme (whatever URL or deep link opens that one card). If the ID was somehow not captured, look the card up and get the link before replying: never reply without it, because a card the operator cannot open in one click is a card they will not correct.

```
Captured: "<title>"
<Pillar> · <Channels> · <Type or —> · <Context>
Insight: <the one-line point / Summary>
Angle: <the take>
<the card link, a bare URL on its own line, built from your board's link scheme and the new card's ID>
```
- If you asked a question or guessed the pillar/channel, add a one-line note ("guessed pillar = <pillar>; say the word to change").
- If you genuinely have a sharper angle than the operator's, add ONE line: "sharper angle if useful: ...". Only when it is actually better; never a weak one to look helpful.
- Close with: "Saved to the Content tab (link above). Correct anything in one line, or carry on."

Then STOP. Do not wait, do not open a menu, do not draft. Correction is optional and non-blocking: if the operator says nothing, the card stands.

### Content board schema (valid values)

| Field | Type | Options / format |
|---|---|---|
| Task name | title | free text (the working title) |
| Status | select | `Idea` (always, on capture) → Drafting → Ready → Posted / Killed (Scheduled merged into Posted while posting is manual) |
| Pillar | select | one of your content pillars, or blank if off-pillar |
| Channels | multi_select | any of `LinkedIn`, `X`, `YouTube`, `Instagram`, `Blog`, `Newsletter` (comma-separated; the candidate channels this seed could serve) |
| Type | select | `Post`, `Carousel`, `Video`, `Short`, `Thread`, `Article` (the eventual primary format; optional) |
| Context | select | one option per sphere of work you keep separate, plus a personal one (the firewall axis: which world) |
| Project | select | your settings project list; default = your default project |
| Audience | text | who it is for (optional) |
| Hook | text | one rough first line (optional; final hook is written per channel at production) |
| Angle | text | the channel-neutral take / structure, one line |
| Source | text | where the idea came from, or "standalone" |
| Summary | text | one-line gist, self-contained (passes the 6-month test) |
| Timeline | date_range | `MM/DD/YYYY` (only if a date was given) |
| Updated at | datetime | auto-stamped by the engine, do not set |

### Why this exists

The operator's strongest content is the work they are already doing; without fast capture, those ideas evaporate by the weekly review and they are left brainstorming from zero. Capturing channel-agnostic seeds (one insight, tagged by pillar and candidate channels, legible 6 months later) makes the board the single front door for every channel: blog, social, and video all start here, and one seed can later fan into several assets. A board view per job does the rest: a Kanban for the Idea-to-Posted flow, a calendar view for anything with a date, and a table for the full backlog.
