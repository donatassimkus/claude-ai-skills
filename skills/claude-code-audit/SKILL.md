---
name: claude-code-audit
argument-hint: [--report-only]
description: "AUDIT: is the Claude Code rig itself healthy? Audit and self-maintain the Claude Code setup. Auto-updates the capabilities reference, diagnoses what's working across memory/skills/hooks/rules/security, auto-executes safe cleanup and batches the rest for approval. Use when asked to audit the setup, optimize workflows, review Claude Code health, find automation opportunities, or clean up the system."
disable-model-invocation: true
user-invocable: true
---

# Claude Code Audit

This skill does three jobs, in order:

1. **Stay current** — self-update the capabilities reference from the live docs (Step 0).
2. **Diagnose** — a liveness canary FIRST (catch silently-broken things and report how long each has been broken), then the full scan across the whole setup (Steps 0.5 to 3). The scan is self-discovering: it diffs the live system against the last run's inventory and probes anything new, so it does not go blind to things built since the checklist was written.
3. **Self-maintain** — auto-execute safe cleanup, batch the risky cleanup into one approval, surface secrets only (Steps 4-5).

The point is that ONE manual trigger catches everything, including breakage that has been silent for days. The skill runs on demand; proactivity comes from the canary plus "broken since" surfacing, not from any background schedule (the operator triggers it). Safe cleanup happens by default; the user is asked only about changes that are risky, irreversible, or touch secrets.

Reference files (read at the step that needs them, not up front):
- `references/capabilities.md` — the Claude Code capability knowledge base (Step 0 maintains it).
- `references/checklist.md` — the Step 0.5 liveness canary, the dynamic-discovery block, and the Step 2 diagnostic rubric.
- `references/cleanup-tiers.md` — the Step 4 risk classification + auto-execute protocol.
- The newest system-inventory document, if one is kept — a dated description of the whole setup, produced by whatever inventory pass exists. Step 0.5 reads the latest one: it is the living system map, and it probes liveness signals the static checklist can miss. Skip this input entirely where no such document is produced; the canary still runs.

**Platform note.** This skill audits a Claude Code setup specifically, and unlike a general method that is the point: the paths, the probes, the frontmatter fields and the whole capability reference describe one platform. Two things are worth separating. The METHOD transfers to any agent rig: self-update your capability knowledge before auditing with it, run a fast liveness canary FIRST and report how long each broken thing has been broken, diff a live inventory against the last run so the scan cannot go blind to new artifacts, sort every fix into auto-execute / ask-once / surface-only tiers, and graduate repeated corrections into permanent rules. The MECHANICS are Claude Code's. On a different setup, keep the method and substitute your own paths, probes, and config locations.

**Paths.** Every `~/.claude/...` path below is Claude Code's own standard location, the same on any machine running it, so use them as written. Anything else (where working files live, where reports and trackers are kept, which folders exist under a project root) is the reader's own convention: ask once, record the answer, and reuse it. Never assume a working-file layout.

**Expected-structure config.** This skill audits the Claude Code SYSTEM it runs on. Universal checks (liveness canary shape, dynamic discovery, hook health, security scan, capability gap, self-update) are in the skeleton below and need no config. Machine-specific expected structure (the exact context/lessons file set, the expected project-folder list, specific scheduled-service names) loads from a per-setup config file if the reader keeps one. With no such config, skip the structure checks that need it and run the generic checks only — never error on a missing config.

## Scope

Operates on the Claude Code SYSTEM only: capabilities reference, skills, hooks, playbooks, rules, contexts, memory, decisions log, lessons, audit history.

Do NOT propose project-level work ("try X on a specific project"). Capability adoption is the user's call. Allowed output: new system files (skills, agents, hooks, playbooks), updates to system files, surfaced findings, and a single neutral "high-fit unused capability" line per feature. If a capability fits a project so obviously it warrants a new skill or hook, propose the skill/hook, never the project move.

## Subscription-vs-API invariant (read before any recommendation)

Where the user pays for Claude through a subscription plan, their usage must run on that plan and never on the metered API, which bills separately on top of what they already pay. So this skill must NEVER recommend setting `ANTHROPIC_API_KEY`, calling `api.anthropic.com`, or running a background script that does. Background automation that needs a model call runs through the CLI on the subscription (`claude -p` with no API key set), or on a local model. A hook quietly calling the metered API is a HIGH finding to REMOVE, not a key to fix: this exact pattern bills real money every turn while looking like ordinary automation, and it is invisible until the invoice arrives. A guard hook that blocks any command referencing the API endpoint is the durable fix. Confirm with the user which plan they are on before applying this invariant; a reader genuinely building on the API has the opposite constraint.

## Step 0: Self-update the capabilities reference

Run every time. Make the audit current before it audits.

### 0a-0c: Fetch, diff, update
Delegate parallel fetches to subagents. Pass each subagent the FULL current `references/capabilities.md` under an `=== EXISTING REFERENCE ===` block and instruct it to report ONLY items absent from that reference, quoting the section heading where each belongs. Without this, every fetch reports false "new" items.

- **Group A (canonical, always fetch):** `code.claude.com/docs/en/whats-new`, the last 4 weekly digests (`/whats-new/2026-wNN`, anchored to this week), the raw `CHANGELOG.md`, plus `/hooks`, `/skills`, `/agents`, `/plugins`. (`docs.anthropic.com/en/docs/claude-code/*` redirects to `code.claude.com/docs/en/*`; use canonical URLs.)
- **Group B (product news, last 30 days):** `anthropic.com/news`, `anthropic.com/claude-code`, `anthropic.com/engineering`, release notes, MCP docs.

Update `references/capabilities.md` with confirmed new features/fields/events, bump its "Last verified" date, add adoption-signal rows. Do not remove a feature unless the changelog confirms deprecation.

### 0d: Report
```
### Self-Update
Reference last verified: [prev] → Updated to: [today] · Changes: [count]
| Change | Section | Detail |
```
No changes → "Reference is current."

### 0e: Self-check this skill (hardened)
Catch the skill's own drift before it runs. Three checks across the WHOLE skill (SKILL.md + all reference files), not just Step 1 paths:
1. **Dead tool/flag names:** grep for any tool or CLI flag the updated reference marks deprecated/renamed.
2. **Dead paths AND command/hook references:** extract every absolute path, hook script name, and shell command this skill or its references name (Step 1 reads, hook-health examples, cleanup commands, graduation destinations). Verify each exists. A named hook that no longer exists, or a rules-directory path that moved when the layout was reorganised, is a finding here. This check earns its place because a skill that names a hook deleted months ago keeps recommending it, and nothing else notices.
3. **Referenced skills:** verify every skill this one delegates to is in the live skills list. Where a delegated skill is absent, say so and do that step inline rather than skipping it silently.

```
### Self-check
Checks passed: [n] · Issues: [n]
| Issue | Location | Fix |
```
If issues found, present the fix as a diff for approval before Step 1, then continue with the corrected skill. No issues → "Self-check passed."

### 0f-0g: News digest + capability gap (feature discovery)
The user does not follow the AI space; surfacing is high-value. This appears in the report right after Top 3 Actions.
- **News digest (last 30d), one row per item:** `| Date | Capability | Type | CLI-usable? | What it is | Concrete fit (MUST name one of the user's actual projects or working contexts) | First-step (literal command/setting/path) |`. **Classify every item's Type** as one of: `CLI-capability` (a real new Claude Code command/tool/hook/model capability), `API-SDK` (only usable when building on the Anthropic API or Agent SDK; note the API-ban implication), `Cowork/web` (a claude.ai or Cowork product, not the terminal), `connector` (an OAuth/MCP integration whose default surface is Cowork; CLI needs the user to wire the MCP themselves), `template-bundle` (prompts or workflows, no new capability). Only `CLI-capability` items run in the terminal today: mark every other Type's `CLI-usable?` column `no` (or `MCP-wire-yourself` for connectors) and never write a Concrete fit that implies CLI usability for a non-CLI item. One genuine `CLI-capability` outranks five `Cowork/web` or `API-SDK` items: lead with it. Reject generic "for your work" rows. 3 high-fit rows beat 8 generic ones.
- **Missed-features check:** read the prior audit's "what you're not using" section; for each feature verify against actual launch dates. Flag any that were already public but unsurfaced. `| Feature | Public on | In prior audit? | Gap |`.
- **Capability gap:** cross-reference actual usage (Step 1 scans) against `references/capabilities.md`. Rank each unused-but-fitting capability High/Medium/Low fit. List High + Medium only.

## Step 0.5: Liveness canary + latest manual (run before the deep scan)

This step exists for the "broken for days" problem: a hook stops firing, a scheduled task flips disabled, the embedder dies, or the backup stops pushing, and nothing notices until someone runs a full audit by hand. This step makes ONE manual trigger catch all of it fast.

1. **Read the latest system inventory.** Find the newest dated system-description document, if the setup produces one. If it is under 7 days old, CONSUME its health/liveness section and its findings: fold anything it flags that the checklist would miss into this run, since a document generated by walking the live system probes reachability a static checklist can skip. If it is stale or missing, note that and rely on the canary alone. Treat it as the living system map for the "how it all fits together" view.
2. **Run the Liveness canary** (the `## 0.5` block in `references/checklist.md`): the reachability probes (every background service and local model answering, any memory or vector index healthy, background services loaded, hooks firing, scheduled tasks enabled and on-cadence, backup pushed recently, JSON configs valid, the metered-API guard wired, no live API key in project dotfiles). Each returns ALIVE or BROKEN with the evidence command.
3. **Surface BROKEN at the very top of the report**, with how long it has been broken. Days-broken = today's date minus the matching findings-tracker ID date (the ID encodes first-detected); for a freshly-detected break, open a new finding dated today so the age grows on the next run. This populates the "Broken now (and for how long)" block in Step 3.

This step is read-only. Fixes flow through Step 4 like any other finding.

## Step 1: Read current state

Read in parallel where possible. Follow `CLAUDE.md`'s own router rather than this list: directory layouts get reorganised, and the router is the only thing that stays true after a move.

- **Core:** `CLAUDE.md`; the always-on rules directory (discovered from `CLAUDE.md`'s router); the trigger-loaded rules or playbooks directory, where the setup separates the two; `settings.json`; `settings.local.json`.
- **Context:** every file in whatever directory holds per-context or per-client instructions, discovered live rather than assumed. If a per-setup config names the expected set, cross-check against it; otherwise just enumerate what exists.
- **Memory:** `memory/MEMORY.md` + every file it indexes.
- **Activity:** `decisions/log.md`; every `tasks/lessons-*.md`, discovered live; `tasks/todo.md`.
- **Skills:** list `~/.claude/skills/`; count total; note `references/` subdirs. Invocation counts (60d):
  ```
  find ~/.claude/projects -name "*.jsonl" -mtime -60 -exec grep -ho '"name":"[^"]*"' {} \; | grep -oE '"name":"(mcp__[^"]*|Skill)"' | sort | uniq -c | sort -rn
  ```
  Then extract the `skill` parameter from Skill tool_use blocks; aggregate per skill.
- **Findings tracker:** `~/.claude/findings-tracker.md` — read FIRST; it is the handoff point from any other pass that files findings. See `references/checklist.md` §0.
- **Agents/plugins:** list `~/.claude/agents/` and `~/.claude/plugins/`.
- **Prior audits:** list `~/.claude/audits/`; read the most recent for the diff.
- **Dir health:** scan the top-level working directories (code repos, active work, task files, archives), wherever the user keeps them. Ask once for that root if it is not already recorded.

**Dynamic discovery (the lists above are a floor, not the ceiling).** The system grows, so do not trust a fixed list. Run the `## 0.6` dynamic-discovery block in `references/checklist.md`: build a live inventory of every artifact class (skills, hooks, scripts, agents, plugins, MCP servers, scheduled tasks, OS-level background services, rules, playbooks, contexts, memory-type prefixes, top-level dirs); diff it against `~/.claude/audits/inventory-latest.json` from the last run; for anything NEW, discover what it is, probe it generically (wired? firing? erroring?), and report "new since last audit, works?, needs a standing check?"; close with the meta-question "what exists that no check covers?". Enumerate live at runtime rather than hardcoding what to look for.

## Step 2: Run the checklist

Apply every block in `references/checklist.md`, marking each item OK / WARNING / ACTION NEEDED. Each ACTION carries a proposed fix and feeds Step 4.

## Step 3: Output the report

Top 3 Actions first (scan-line), feature discovery next (do not bury it), then the diff and detail.

```
## Claude Code Audit Report — [today]
Skills: [n] ([Δ]) · Memory files: [n] ([Δ]) · Decisions: [n] ([Δ]) · Lessons: [n] ([Δ]) · CLAUDE.md lines: [n] ([Δ])

### Broken now (and for how long)   (Step 0.5 canary; omit only if truly empty)
| Component | State | Broken since | Days | Fix |
Every BROKEN liveness probe plus every still-Open tracker finding, sorted by severity then age. Days = today minus first-detected (the tracker ID date). If the canary is all green and nothing is Open: "Nothing broken: all liveness probes green."

### Top 3 Actions   (ranked by impact, each <15 min)
1. **[action]** — [why]. [how].
2. …
3. …

### What's new + what you're not using   (Step 0f/0g output)
Feature flash: [one sentence — the single highest-fit unused capability]
[news table] · [missed-features table] · [capability-gap list]
Why I'm not pushing adoption: surfacing is the job; adoption is yours.

### Change since last audit   (if a prior audit exists)
| Metric | Prev | Curr | Δ |  (skills, memory, CLAUDE.md lines, always-on load, open HIGH security, 0-invocation skills)
Regressions / Wins / New findings / Resolved.
First run → "No diff; this is the baseline."

### Setup Health
| Area | Status | Notes |
(CLAUDE.md, Rules+Playbooks, Priorities, Memory, Memory drift, Decisions, Lessons, Skills, Hooks, Hook/writing-rules sync, Agents, Directory, Routers, MCP, Security, Hook health, Liveness canary (each configured background service / scheduled-task cadence / backup push), Transcript patterns, Tool-call failure modes, Lesson follow-through)
Security detail table: | Risk | Finding | Path | Remediation |  (never echo values)

### Automation Opportunities
Each: What (hook/agent/skill) · Why (pattern) · Effort · Impact.

### Cleanup (Step 4 result)
Green auto-fixed: [count] (see ~/.claude/audits/cleanup-log.md). Yellow/Red: [count] awaiting decision.

### Priority Recommendation
The single highest-value next move. One paragraph.
```

After displaying, write the full report to `~/.claude/audits/audit-YYYY-MM-DD.md` (create the dir if missing; overwrite a same-day file). This enables the next run's diff.

Then sync `~/.claude/findings-tracker.md`: append each new issue as `A-YYYY-MM-DD-NNN` (Status `Open`, severity, proposed fix); update entries acted on (`In progress`/`Fixed`/`False positive`); mark deferred ones `Deferred` + reason.

## Step 4: Self-maintain (auto-cleanup)

This is the loop that makes the audit worth running. Sort every Step 3 ACTION into Green / Yellow / Red per `references/cleanup-tiers.md`, then:

1. **Execute the Green queue now** (backup-file deletes, broken-symlink prunes, dead-permission removals, legacy-prefix renames, orphan moves, moved-router path fixes, plus writing the discovery inventory snapshot to `~/.claude/audits/inventory-latest.json` for the next run's diff). Log each to `~/.claude/audits/cleanup-log.md` with a revert hint.
2. **Sanity-check** after Green: re-run the cheap check that found each item; fix any reference a Green action broke.
3. **One batched pop-up** for Yellow (approve/skip) + Red (surfaced findings with a recommended manual step). Never stack modals.
4. Report Green count + cleanup-log path in the final summary.

If the user said "report only, don't change anything" this session, present the Green queue as a list instead of executing it.

## Step 5: Lesson graduation + consolidation

Turn repeated corrections into permanent rules, and keep the lessons files from growing without bound. The health metric is NOT lesson count (retrieval is relevance-ranked, so count is cheap); it is **duplicate clusters** and **clusters that should be a rule or hook but are not**. Both being high means capture is outpacing graduation. For broad memory hygiene (merging duplicates, fixing stale facts, pruning the index), delegate to a dedicated memory-consolidation skill first where one is installed, then return here; where none is, do the merge inline as described below.

**Consolidate (runs on every trigger, not on a schedule):** scan each lessons file for near-duplicate clusters (3+ entries on one theme), merge each into one canonical lesson, and after graduation is approved ARCHIVE the merged/graduated/stale entries into a per-context lessons archive file so the active file stays scannable (it loses signal past roughly 1,500 lines). Report: `| theme | entries | files | action (merge/graduate/keep) |`.

**Read:** every lessons file; every feedback-type memory file; the always-on rules and the trigger-loaded playbooks; the per-context instruction files.

**Classify each correction:** scope (global / project / skill); already absorbed into a rule/context/skill?; pattern strength (how many lessons + memories on the same theme).

**Propose graduations** for corrections appearing 2+ times and not yet absorbed:
- Global behavioural → append to the matching trigger-loaded playbook, or a new one. Reserve the always-on rules directory for rules that genuinely must load every session (the writing-style / safe-writes class); everything else is trigger-loaded, because always-on content is paid for on every single turn.
- Project-specific → append to that project's own context file under a `## Graduated rules` section.
- Skill-specific → append to that skill's `SKILL.md`.

```
### Lesson Graduation
Inbox: [n] lessons · [n] feedback memories · Already absorbed: [n] · Ready to graduate: [n]
| Correction | Source | Destination | Scope |
| Already absorbed (safe to delete) | feedback_xyz.md | encoded in … |
```

**Execute with approval** (this is a Yellow action — it changes future behaviour). On approval: write the graduated rules; remove graduated entries from their lessons files; delete absorbed feedback memories; update the memory index. The post-graduation deletes are Green and run automatically once the graduation itself is approved.

## Guardrails

- Steps 0-3 are read-only (except 0c updating the reference and 0e's approved self-fix). Step 4 Green auto-executes inside the Claude Code config directory and the task files only; everything else is gated.
- Be honest. Clean setup → say so. Do not invent findings to look busy.
- Thin data (empty lessons, one-entry decision log) → say so and recommend building history before the next run.
- Never recommend a metered-API action against a subscription plan (see the invariant above).
