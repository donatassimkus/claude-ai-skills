---
name: agent-team
argument-hint: what you need built or reviewed (e.g. "website for my kid", "landing page for SaaS", "debug this with competing hypotheses")
description: Auto-spawn a coordinated team of Claude Code teammates (each with own context, can DM each other, share a task list) when the user describes work that spans multiple domains and would benefit from specialists working in parallel with feedback loops. Triggers on phrases like "create a website for X", "build me an app for Y", "spin up a landing page for Z", "make me a site about W", "I need this built end-to-end", "review this from multiple angles", "debug this with competing hypotheses", or any request that implies multi-specialist parallel work with a quality loop. Auto-classifies the request, picks team composition + model-per-role + file ownership + hand-off graph, then spawns. Skip for single-domain tasks (use matching specialist skill), sequential pipelines (use subagents), or simple one-shot work. Requires the host's multi-agent team feature to be enabled; on Claude Code that means setting CLAUDE_CODE_EXPERIMENTAL_AGENT_TEAMS=1 in settings.json.
---

# Agent Team

Auto-orchestrates a parallel team of Claude Code teammates against a user goal. The user states what they want; this skill picks the team, the model per role, file ownership, hand-off graph, and the spawn prompt — without the user having to remember any of that.

**Platform note.** The mechanics below are written against Claude Code's agent-teams feature, which is what the paths, the spawn phrasing, the plan-approval switch and the limitations section describe. The METHOD is not tied to it: classifying the request into a team shape, sizing the team, assigning file ownership, drawing the hand-off graph, tiering models by role, monitoring and redirecting early, and shutting down cleanly all transfer to any system that can run several agents in parallel with messages passing between them. On a different one, substitute its own spawn syntax, its config location, and its equivalent of plan approval, and treat the limitations section as a list of questions to answer about that platform rather than as facts about it.

## When to invoke

User describes work that meets ANY of these:
- **Multi-domain build:** "create / build / spin up / make me [a website / app / landing page / portal / dashboard / tool] for [topic / person / audience]." Spans front-end + back-end + content + QA.
- **Quality loop:** "write me [content] with reviews," "build this with QA," "I want [thing] reviewed from multiple angles." Writer + reviewer(s) + verifier.
- **Competing-hypothesis debug:** "this is broken, multiple things could be wrong, test them in parallel," "investigate from these N angles."
- **Multi-context review:** "review this [plan / decision / strategy] across [contexts]." One teammate per context.
- **Cross-layer change:** "change spans frontend, backend, and tests, each owned by a different teammate."
- **Explicit ask:** "create / spin up a team to [...]"

## When NOT to invoke

- Single-domain audit → use whatever specialist skill covers that one domain, or a cross-skill audit pass if you have one. A team adds coordination cost and buys nothing when only one specialism is in play.
- Sequential pipeline (step 2 needs step 1's output) → use subagents in chain, not a team.
- Simple one-shot work (rename, search, lookup, single edit) → just do it.
- Live-system writes against shared infrastructure (a production CMS, a live email send, anything with real users on the other side) → the slow-shutdown limitation matters here, because you cannot stop a teammate mid-write. Use a single verification subagent and a careful sequence instead of parallel writers.
- User wants single conversation history → teams break this; use main session.

## How it works

### Step 1: Extract the goal

From the user's natural language, pull out:
- **Subject** (what is being built / reviewed / debugged) — e.g. "website for [person/thing]"
- **Topic / theme** — what it's about
- **Domain or URL** if mentioned
- **Audience** if mentioned (and inferable, e.g. kid, family, internal team, public)
- **Constraints** (style, scope, deadline, must-have features) if mentioned
- **Success criteria** — what "done" looks like

If any of subject / topic / success criteria is missing AND not inferable from context, ASK ONCE via `AskUserQuestion` for the smallest set that unblocks the team. Otherwise proceed with labeled assumptions.

### Step 2: Classify into a team template

Map the goal to one of the templates below. If it doesn't fit cleanly, fall back to **General build team**.

### Step 3: Customize team

For the picked template, fill in:
- **Team name** — short, descriptive, derived from the subject (e.g. "kidsite" if it's a website for the user's kid, "blog-loop" for a blog quality loop). Lowercase, no spaces.
- **Per-teammate role** — concrete responsibility, written in plain language.
- **File ownership** — each teammate owns specific files / sections to prevent overwrites.
- **Hand-off graph** — who messages whom and when.
- **Model per role** — sonnet by default; opus for arbiters / critics / architecture decisions; haiku for mechanical verifiers (link-check, accessibility-scan, JSON-validate).
- **Final deliverables** — what gets handed back to the user.

### Step 4: Surface the plan, spawn

Before spawning, show the user the proposed team in a single compact block:

```
TEAM: <name> (<N> teammates, <plan-approval mode>)
1. <role>  — <model> — owns: <files> — talks to: <recipient>
2. <role>  — <model> — owns: <files> — talks to: <recipient>
3. <role>  — <model> — owns: <files> — talks to: <recipient>
GOAL: <one sentence>
DELIVERABLES: <what user gets at the end>
```

If user is in auto mode and the plan looks reasonable, proceed. Otherwise `AskUserQuestion` with options: approve / adjust roles / use solo session / cancel.

### Step 5: Spawn

Use natural language to the lead session, NOT a pre-built CLI command. Pattern:

```
GOAL: <one sentence goal with subject, topic, audience, success criteria>

Create a team called <name> of <N> teammates using <model>:

1. <Role 1>: <one-paragraph job description>. Owns: <files>. When done with <X>, message <recipient>.

2. <Role 2>: <one-paragraph job description>. Owns: <files>. Wait for <input> from <Role 1>, then do <Y>. Message <recipient> when done.

3. <Role 3>: <one-paragraph job description>. Owns: <files>. Wait for <input>, then do <Z>.

Plan approval: ON. Each teammate must get its plan approved by you (the lead) before executing.

Final deliverables:
- <thing 1>
- <thing 2>
- <thing 3>
```

### Step 6: Monitor + intervene

While the team runs, surface key updates from the lead to the user:
- When a teammate finishes a major hand-off
- When QA / reviewer finds critical issues
- When a teammate gets stuck waiting for a dependency

If a teammate goes down a wrong path early, tell the lead to redirect rather than letting it burn tokens.

### Step 7: Cleanup

On user "looks good" or task completion, instruct lead to shut down teammates cleanly:
- Each teammate saves work-in-progress to a temp file
- Lead waits for shutdown confirmation from each
- Lead generates final summary

## Team templates

### Website / landing page / app build (most common for "create a website for X")

```
TEAM: <subject>-site (3-4 teammates, plan-approval ON)
1. front-end-dev  — sonnet — owns: index.html + all CSS + UI JS — talks to: content-writer, qa
2. content-writer — sonnet — owns: copy.md, content sections — talks to: front-end-dev
3. qa             — sonnet — owns: test report — talks back to: front-end-dev, content-writer

GOAL: Build a <type> for <audience> about <topic>. <Domain if mentioned.>
DELIVERABLES:
- Working static site at <path or local-host>
- Copy reviewed and on-tone for the audience
- QA report with pass/fail
```

If dynamic / API-backed, add a 4th teammate: `back-end-dev — sonnet — owns: server code, API endpoints`.

### Quality loop (writer + reviewers)

```
TEAM: <topic>-loop (4 teammates, plan-approval ON)
1. writer            — sonnet — owns: draft.md — talks to: all reviewers
2. style-reviewer    — sonnet — owns: style-feedback.md — talks back to: writer
3. seo-reviewer      — sonnet — owns: seo-feedback.md — talks back to: writer
4. factual-verifier  — haiku  — owns: facts-check.md — talks back to: writer

GOAL: Produce a <piece> on <topic>, iterated until all reviewers approve.
DELIVERABLES: Final draft + review log showing each reviewer's pass.
```

### Competing-hypothesis debug

```
TEAM: <bug>-debug (3 teammates + arbiter, plan-approval OFF)
1. hypothesis-1-tester — sonnet — owns: hypothesis-1-test.md — talks to: arbiter
2. hypothesis-2-tester — sonnet — owns: hypothesis-2-test.md — talks to: arbiter
3. hypothesis-3-tester — sonnet — owns: hypothesis-3-test.md — talks to: arbiter
4. arbiter             — opus   — owns: verdict.md — collects all three, ranks evidence

GOAL: Identify root cause of <bug> by testing N independent hypotheses in parallel.
DELIVERABLES: Verdict with ranked hypothesis evidence.
```

### Multi-context strategic review

```
TEAM: <decision>-review (N+1 teammates, plan-approval OFF)
1. context-A-reviewer  — sonnet — owns: context-A-feedback.md — talks to: synthesizer
2. context-B-reviewer  — sonnet — owns: context-B-feedback.md — talks to: synthesizer
3. context-C-reviewer  — sonnet — owns: context-C-feedback.md — talks to: synthesizer
4. synthesizer         — opus   — owns: synthesis.md — produces final recommendation

GOAL: Stress-test <decision/plan> from each relevant context before commit.
DELIVERABLES: Synthesis with each context's position + recommended path forward.
```

### General build team (fallback)

If no template fits, spin up a generic 3-teammate team: builder + reviewer + verifier. Builder owns the artifact, reviewer challenges quality, verifier checks the deliverable matches spec.

## Defaults

- **Team size:** 3-5 teammates. More than 5 = coordination overhead exceeds parallelism gain.
- **Default model:** sonnet for builders, opus for arbiters / synthesizers / critics where reasoning matters most, haiku for mechanical verifiers. The tier names are this platform's; the principle is what carries. Spend the strongest model where a judgement call gets made and one wrong ranking poisons the whole run, spend the mid tier on the work that produces the artifact, and spend the cheapest on anything mechanical and checkable (link checks, schema validation, accessibility scans). Map those three bands onto whatever model tiers the platform offers.
- **Plan approval:** ON for build tasks, OFF for hypothesis-tests and reviews where each teammate's job is independent.
- **File ownership:** ALWAYS assigned. No teammate edits another's files.
- **Permissions:** Inherited from lead session at spawn. Don't change mid-flight unless user explicitly asks.
- **Working directory:** Same as lead unless user specifies a separate workspace.

## Common pitfalls and fixes

- Teammates ask permission constantly → preapprove the tools they need in the project's local permission settings before spawn, rather than approving each request mid-run.
- Deliverables don't feel coherent → file ownership wasn't enforced; re-spawn with explicit owners per file.
- One teammate sits idle → role wasn't given a clear dependency or task; either remove the teammate or give them a real job.
- Token burn too high → reduce teammates, or downgrade some from opus to sonnet, or sonnet to haiku for mechanical work.
- Teammate loses work → tell teammates to write progress to `<role>-wip.md` periodically so it persists.
- Wrong approval routing → switch plan-approval target from auto to user-approved temporarily.

## Limitations to remember

- `/resume` and `/rewind` do NOT restore in-process teammates. After resume, lead spawns new ones.
- One team at a time per session. Clean up before creating a new one.
- No nested teams. Teammates can't spawn their own teams.
- Slow shutdown (teammates finish current request first).
- Permissions set at spawn; per-teammate changes only after spawn.

## Output locations

- Team config and the shared task list are managed by the platform automatically, in its own state directory under the user's home config — don't edit those by hand.
- Final deliverables go to the working directory or to the path the user specified in their goal.
- Append a run summary to the project's changelog if the work touches a project that keeps one.

## Related

- A cross-skill audit pass with an arbiter, for improving an existing target against several rubrics at once.
- Subagents for sequential or one-shot delegation without inter-agent dialogue.
- Solo session for simple single-domain work.
