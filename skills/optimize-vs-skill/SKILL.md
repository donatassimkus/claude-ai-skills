---
name: optimize-vs-skill
argument-hint: [target] [--scope pages] [--skills skill-list] [--rounds N] [--mode lite|full] [--apply]
description: Multi-skill autonomous quality optimizer. Analyzes a target (website, codebase, copy, campaign, document), locks an objective function, proposes relevant skills, fans out to parallel per-skill auditors, arbitrates cross-skill conflicts via a dedicated arbiter subagent, stops at diminishing returns or max rounds, produces a detailed scorecard and recommendation report with reject list and tradeoffs named. Invoke when the user says "make this as good as possible", "iterate on quality", "optimize this to world class", "run a multi-skill audit", "push this to its ceiling", "auto-optimize", or "run the optimizer".
user-invocable: true
---

# Auto-Optimizer

Orchestrates a full-quality improvement pass across multiple skills, autonomously but transparently. Uses a fan-out + arbiter architecture so no cross-skill conflict is silently resolved.

## Architecture

```
[optimize-vs-skill skill]      drives rounds, handles touchpoints, streams progress
          ↓ parallel spawn (Agent tool, one message, N subagent calls)
[optimize-vs-skill-auditor × N]  one per skill in play; each returns a proposal bundle
          ↓ feeds into
[optimize-vs-skill-arbiter]    strongest available model + extended thinking; merges bundles
                            against the objective function; returns plan + reject list
          ↓
[optimize-vs-skill skill]      Touchpoint 3 preview → Touchpoint 4 commit decision
```

Two architecture modes, picked at Touchpoint 2:
- **Full** (default): fan-out + arbiter. Each skill runs in its own subagent context; arbiter mediates all cross-skill conflicts. Use for websites, codebases, full campaigns.
- **Lite**: single `optimize-vs-skill` subagent audits all skills internally. Cheaper, loses specialist depth. Use for small copy or doc targets.

## When to invoke

- User asks to "make X as good as possible", "optimize X to world class", "push X to ceiling", "iterate on quality", "run the optimizer", "auto-optimize".
- User has an artifact (site, repo, page, doc, campaign, ad copy, social post, email sequence, etc.) and wants it sharpened across multiple disciplines.
- User wants autonomous execution with visible progress and single approval touchpoints before apply.

## When NOT to invoke

- User wants a single-skill audit only (invoke that skill directly).
- User wants a quick answer without iterative refinement (overkill).
- Target is one sentence of copy (use the matching skill directly).

## Five user touchpoints total

The skill orchestrates these. Everything between is autonomous but streams progress to chat.

### Touchpoint 1: scope lock

Before any audit, ask which pages / sections / files are in scope. Never assume. Use `AskUserQuestion`.

For a website: list every shipped page (including components). Offer "all shipped pages", "homepage only", "custom subset". If only one page exists, state it and ask if that's the intended scope.

For a codebase: ask which modules / directories.

For copy / docs: ask which documents / social posts / emails.

**Scope is a hard boundary.** Per-skill auditors may identify improvements outside the confirmed scope, but must put them in `scope_expansion_proposals`. The arbiter does not bundle those into the accepted plan; they surface as a separate user decision.

### Touchpoint 1.5: objective function lock

After scope, pin down the decision criteria the arbiter will use. Without this, mediation is vibes. Use `AskUserQuestion` with three questions:

1. **Primary metric** (single choice): conversion / organic traffic / activation / retention / revenue-per-visitor / other (free text).
2. **Floor constraints** (multi-select): examples include "don't drop any skill score below N", "CTA never below fold", "LCP under 2.5s", "mobile parity", "no copy over grade-9 reading level", "no claims containing specific numbers", other (free text).
3. **Creative-lever tolerance** (single choice): aggressive (bend convention freely within legal) / moderate (bend for social proof only) / conservative (no creative levers at all).

Persist the locked objective function wherever this setup keeps durable notes, one file per target, so reruns against the same target reuse it instead of re-asking. Re-asking the objective every run is how a multi-round optimizer quietly drifts: the arbiter mediates against whatever was last said rather than against a stable criterion.

### Touchpoint 2: skill proposal + architecture mode + cost estimate

Analyze the scoped target. Propose relevant skills with HIGH / MEDIUM / LOW confidence tiers. Show the proposal, the chosen mode, and the cost estimate BEFORE kicking off rounds.

Format:

```
Scope: <confirmed pages/sections/files>
Objective: <primary metric> | Floors: <floor constraints> | Levers: <tolerance>

Proposed skills (confidence-tagged):

HIGH (recommend include):
- /skill-a — reason
- /skill-b — reason

MEDIUM (include if you want):
- /skill-c — reason

LOW (skip):
- /skill-d — reason

Architecture mode: Full (fan-out + arbiter) | Lite (single subagent)
Run mode: dry-run (default) | apply (commits after preview)
Max rounds: 10
Convergence threshold: 2 points (round stops when total delta < 2)
Priority order (tie-breaker only): <your own discipline ladder, strongest-weighted first; e.g. a conversion-first ladder puts conversion work above design, then usability, then copy, then search>

Estimated cost:
- Full mode: N skills × M rounds of auditor calls + M arbiter rounds = ~$X total
- Lite mode: 1 subagent × M rounds = ~$Y total
- Typical wall time: Full ~15-25 min; Lite ~6-12 min
```

User confirms skills, architecture mode, run mode, and max rounds in a single `AskUserQuestion` pop-up.

### Touchpoint 3: live preview before commit

After the final round's arbitrated plan is ready:
1. Apply accepted changes to local files (not committed, not pushed).
2. Render the preview in the mode matching the target type (see Preview variants below).
3. Show preview + scorecard delta table + reject list + creative-lever surfacing in chat.
4. Ask: commit / further tweaks / revert. Use an interactive question, and apply verdict-pop-up hygiene: no `(Recommended)` tag on a verdict choice (it biases the human toward rubber-stamping a result they should judge independently), and always include a stop-or-pivot option so they can exit the flow rather than being funnelled onward.

**Never commit anything without this step.**

### Touchpoint 4: commit decision

After live preview:
- Approve → commit to a new branch `optimize-vs-skill/<YYYY-MM-DD-HHMM>`, push, open PR.
- Tweak → stay local, apply adjustments, preview again, back to this touchpoint.
- Revert → discard local changes, keep the run report.

## Target-type preview variants (Touchpoint 3)

Different targets need different previews. Do not force screenshots onto a doc target.

- **Website** — start a local preview and screenshot at desktop (1440×900), mobile (375×812), tablet (768×1024), using whatever browser-preview tooling this environment provides. Also capture console output and network requests for regressions: a change that looks right and throws in the console is not done.
- **Codebase** — unified diff view + test run results + type check (project equivalents). No screenshots.
- **Copy / doc** — rendered markdown side-by-side (before / after) + a banned-words and banned-pattern scan against the house style list + reading-grade estimate.
- **Campaign / email sequence / social post set** — variant matrix table: rows = versions, columns = projected metrics (CTR, primary-metric lift, banned-word count, tone alignment).
- **Mixed** (e.g., codebase with copy changes) — run all applicable previews sequentially; present all in one Touchpoint 3 message.

## Progress updates during the loop (between Touchpoints 2 and 3)

Subagents run in isolated context; main thread cannot stream from them. The skill drives the round loop itself. Each round: the skill spawns N per-skill auditors in parallel (single message with N Agent calls), waits for all bundles, then spawns the arbiter, then emits a delta table.

Cadence: after every completed round, emit:

```
Round N/M complete (≈X min elapsed, ≈Y remaining).
| Skill       | Start | Round N | Δ this round | Score denominator                |
|-------------|-------|---------|--------------|----------------------------------|
| /skill-a    | 62    | 75      | +13          | <explicit denominator>          |
| /skill-b    | 68    | 78      | +10          | <explicit denominator>          |
Accepted: K changes | Rejected: J (X conflicts + Y floor violations)
Creative levers surfaced for review: Z
Convergence so far: +T total. Continuing.
```

Target gap between updates: under 2 minutes. If a single round exceeds that, emit a half-round "still working" ping.

Before the first round, tell the user: "Running N rounds × M skills in Full mode; typical X min. I'll post a delta table after each round."

## Operational gates (kill switch + safety)

Two automated pauses that force user sign-off mid-loop.

### Kill switch

After any round where the arbiter returns `kill_switch_triggered: true`, STOP before the next round. Conditions that trip the switch:
- Total round delta > 20 points (possible overfit or fabrication).
- Any change tagged Red risk (anything that can break the build, the deploy, auth, or a schema).
- Any floor constraint violation in proposed accepted state.
- More than 8 conflicts resolved in one round.
- Any accepted change targets a surface outside confirmed scope.

Pop-up options (verdict style — no `(Recommended)` tag): `Continue` / `Pause and let me review` / `Revert this round`.

### Creative-lever per-lever approval

Creative levers never auto-apply. After the arbiter returns `creative_levers_surfaced`, before any edit commits, iterate per-lever with a pop-up showing:
- Proposed claim / change.
- Convention being bent.
- Legal-safety check reasoning.
- Expected lift on primary metric.
- Options: `Ship it` / `Skip this one` / `Skip all creative levers for this run`.

## Rules for what the optimizer considers

### Rule 1: propose additions, not just edits

Consider what is **missing** from the target, not only what is **wrong**. Per-skill auditors must surface at least one additive candidate per round unless the target is feature-complete for that skill's domain. See `agents/optimize-vs-skill-auditor.md` for categories.

### Rule 2: creative rule-bending within legal limits

Creative levers are allowed if:
- Legal (no fraud, no false advertising, no FTC violation, no GDPR/CCPA breach).
- Not obviously fake (plausibly true under a broad-but-defensible interpretation).
- Flagged explicitly and separated from standard edits.
- The user's creative-lever tolerance (Touchpoint 1.5) allows them.

Never auto-shipped. Per-lever pop-up is required.

### Rule 3: never silently resolve conflicts

Every cross-skill conflict appears in the arbiter's `conflict_log` with both positions stated, the resolution chosen, and the tradeoff named in a single sentence. If the arbiter cannot justify a resolution against the objective function, it surfaces the conflict to the user for a decision.

### Rule 4: honest scoring with explicit denominator

Every score MUST state its denominator. Examples of valid scoring:
- `score 75/100 — measured across 5 pages × 18 heuristics = 90 cells; 68/90 pass`
- `score 82/100 — 5 pages × 12 on-page + 8 tech = 68 cells; 55/68 pass; 3 n/a (i18n locked)`

Invalid: `score 82` (no denominator).

When a dimension is out of scope, mark it `n/a` rather than inflating the score.

Never claim "100% coverage" unless the denominator is explicitly the full universe of the user's actual concern, not a subset. If the user's concern is "all images have alt text on this page", the denominator is all imgs on the page, not only the ones rendered by one template or component.

### Rule 5: scope is a hard boundary

Per-skill auditors may identify value outside the confirmed scope, but route it through `scope_expansion_proposals`. The arbiter does not bundle these into accepted changes. The skill surfaces them as a separate user decision after the round, offering: `Expand scope and rerun this round with additions` / `Save as follow-up for later` / `Reject`.

### Rule 6: safety rails

- Dry-run is default. Apply mode commits to a fresh branch, never main.
- Yellow / Red risk changes require explicit confirmation inside apply mode. Green is read-only or trivially reversible; Yellow is a config, content, or data write; Red is anything that can take the target down.
- Banned words and banned sentence patterns are enforced on every copy change, from whatever house style list this setup maintains. If no list exists, ask for one rather than inventing it.
- Never ship a link to a non-existent page. Gate the link or stub a page, do not ship broken.

## Invocation grammar

```
/optimize-vs-skill                                   # full flow; asks scope + objective + skills
/optimize-vs-skill [target]                          # target specified
/optimize-vs-skill [target] --scope=page1,page2
/optimize-vs-skill [target] --skills=seo,cro,writing
/optimize-vs-skill [target] --rounds=20
/optimize-vs-skill [target] --mode=lite              # single-subagent architecture mode
/optimize-vs-skill [target] --apply                  # skip dry-run (still shows preview before commit)
```

Defaults:
- `rounds`: 10
- `threshold`: 2 points (convergence)
- `mode` (architecture): Full (fan-out + arbiter)
- `run mode`: dry-run
- `priority_order`: conversion-first by default (conversion > design > usability > copy > search); set your own ladder to match your primary metric

## Output locations

- Per-run reports: one timestamped markdown file per run, in the project's own working-docs folder.
- Branch (apply mode): `optimize-vs-skill/<YYYY-MM-DD-HHMM>`.
- Objective function persisted to memory (one file per target).
- Never write to skill or agent definition files during a run.

## Subagent reference

- `optimize-vs-skill-auditor` — per-skill auditor. One invocation per skill per round, in parallel. Used in Full mode.
- `optimize-vs-skill-arbiter` — cross-skill arbiter. One invocation per round after all auditors return. Used in Full mode.
- `optimize-vs-skill` — single-subagent fallback. Audits all skills internally. Used in Lite mode only.

## Interaction with your other rules

This optimizer sits UNDER whatever standing rules the setup already has, and defers to them rather than restating them. Wire it to the four classes that matter, if you maintain them:

- **Live-write safety** — risk tags, backup before change, smoke test after, auto-revert on failure, verdict pop-up hygiene. The optimizer's apply mode is a live write like any other.
- **Build / verification workflow** — pre-flight checks, gates, recommendation format, root-cause discipline over symptom patching.
- **House writing style** — the banned words and patterns enforced on every copy change.
- **Generic-skill rules** — the optimizer stays domain-agnostic; anything specific to one project comes from that project's context, never hardcoded here.
- **Deliverable presentation** — how a long run report is structured, typically at two or three zoom levels so the reader can stop at the depth they need.

If a setup has none of these, the optimizer still runs; it simply has fewer standing constraints to respect, and the objective function's floor constraints carry more of the weight.
