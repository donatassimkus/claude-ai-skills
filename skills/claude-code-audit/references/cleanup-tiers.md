# Cleanup tiers + auto-execute protocol

The audit's job is not just to diagnose. It closes the loop: safe maintenance executes itself, risky maintenance is batched into one decision, secret handling is surfaced only. This file is the classification engine for Step 4.

Risk model is a Green / Yellow / Red tiering: Green is local and reversible, Yellow changes live behaviour, Red touches secrets or anything irreversible. The audit operates ONLY inside the Claude Code config directory and the task files. Nothing under the working-output or code directories is ever Green.

## The three tiers

- **Green** — auto-execute immediately, log to `~/.claude/audits/cleanup-log.md`, NO pop-up. Local, reversible, system-cruft only.
- **Yellow** — back up the file first, then ONE batched pop-up covering the whole Yellow queue. Config edits, narrowing a live grant, deleting user data.
- **Red** — surface and propose only. NEVER auto-execute. Secrets, anything irreversible, anything public-facing.

## Classification table

| Action type | Tier | Why | Auto |
|---|---|---|---|
| Delete backup/disabled files in `.claude/` and `tasks/` (`*.bak-*`, `*.disabled-*`, `*.legacy-*`) **older than 48h** | Green | backups of git-tracked files, recoverable; the 48h age guard preserves active safety nets | yes |
| Prune broken symlinks in `.claude/skills/` | Green | dead links, carry no content | yes |
| Remove provably-dead permission entries (leading-slash patterns, paths to deleted dirs, tool names from removed MCPs) | Green | match nothing; removal is a no-op on live behaviour | yes |
| Rename a memory file to the `{type}_{project}_{topic}` convention + update its index entry | Green | local rename, fully reversible | yes |
| Move an orphan plan/strategy file into the project's own plans folder, per whatever output-file convention the setup documents | Green | local move | yes |
| Fix a dead router/index link where the target moved and exists at the new path (a file that changed directory in a reorganisation) | Green | mechanical path correction | yes |
| Delete absorbed feedback memories + stale graduated lessons | Green | only after Step 5 graduation is approved | yes |
| Archive merged/graduated/stale lessons to a per-context lessons-archive file | Green | local move within the task files, reversible; only after Step 5 graduation is approved | yes |
| Write the discovery inventory snapshot to `~/.claude/audits/inventory-latest.json` | Green | the audit's own derived baseline, overwritten each run | yes |
| Narrow a live broad permission grant (`Bash(*)`, unfiltered `Edit`) | Yellow | changes the live permission surface | ask |
| Edit `settings.json` hooks config | Yellow | could disable a working hook | ask |
| Delete non-system user data (build archives, accumulated session handoffs) | Yellow | user data, not system cruft | ask |
| Append a graduated rule to a playbook / context / skill | Yellow | changes future behaviour | ask (this is Step 5's gate) |
| Edit `CLAUDE.md` or a context file's content | Yellow | core config | ask |
| Anything touching a secret: `.env*`, `mcp.json` tokens, credentials, keys | Red | secret handling is the user's call | surface only |
| Any `api.anthropic.com` call or setting `ANTHROPIC_API_KEY` on a subscription plan | BLOCKED | bills the metered API on top of the plan already paid for; a guard hook should enforce it | never |
| Live-system write (a production CMS, prod DB, a deploy) | Red | out of audit scope | never |

## Secret handling (Red, specific)

Follow the setup's own secrets policy and rotation discipline. Absent one, these defaults hold:
- Locate the secret, report keys only (never echo values), classify HIGH/MEDIUM/LOW.
- Recommend the move (out of plaintext config, into the user's own secrets file or secret store, permissions locked to the owner) as the action.
- Recommend rotation ONLY with a concrete leak signal (committed to a public repo, shared in a screenshot, file regressed after a prior delete). Otherwise propose move + delete, not rotation.
- Never add "rotate quarterly" or any rotation cadence to the report.

## Auto-execute protocol (Step 4)

1. After the Step 3 report, sort every proposed maintenance action into Green / Yellow / Red queues.
2. **Execute the Green queue now.** For each action: perform it, then append one line to `~/.claude/audits/cleanup-log.md`:
   ```
   YYYY-MM-DD HH:MM | <action> | <target path> | revert: <how>
   ```
3. **Sanity-check after Green.** Re-run the cheap check that found each item (bak files gone? symlink resolved away? index still has no dead links?). If a Green action broke a reference (renamed a memory but missed an index entry), fix it before continuing.
4. **One batched pop-up for Yellow + Red.** Yellow items as approve/skip choices in a single interactive question; Red items surfaced as findings with a recommended manual step. Do not stack modals. One decision point per run.
5. Report what Green auto-fixed (count + the cleanup-log path) in the final summary.

## Guardrails

- Green is the default ONLY for the action types listed Green above. If an action does not clearly map to a Green type, it is Yellow. When unsure, escalate, never auto-execute.
- **48h age guard on backup deletion.** Never auto-delete a `*.bak-*` / `*.disabled-*` / `*.legacy-*` file modified in the last 48 hours. Recent backups are active safety nets for changes still being validated (including the audit's own edits this run). They age into the Green sweep on a later run. A backup that contains a secret stays Red regardless of age (surface for manual delete, never auto).
- Never auto-delete anything outside the Claude Code config directory and the task files. Those two are the entire Green blast radius; if an action needs to reach beyond them, it is not Green.
- Every Green action gets a cleanup-log line. The run stays fully auditable and reversible.
- If the user said "just report, don't change anything" this session, skip auto-execute and present the Green queue as a list instead.
