# Audit checklist (Step 2 rubric)

Apply each block against the state read in Step 1. Mark every item OK / WARNING / ACTION NEEDED. Every ACTION feeds Step 4, where it is sorted into a cleanup tier (`references/cleanup-tiers.md`).

Two principles keep this from going stale:
- **Discovery over hardcoding.** Validate against what the live config actually points at (read the routers, read `settings.json`), not against file names baked into this checklist. File names drift; discovery does not.
- **Consume, don't re-derive.** Where another tool already produced findings (a system-inventory pass writing to the findings tracker, a token/context dashboard), read its output and validate. Do not re-run the full scan from scratch.

## 0. Process findings-tracker.md (handoff from any other pass that files findings)

Before any other check, read `~/.claude/findings-tracker.md`. For each `Open` entry:
- Re-check the underlying condition. Still present? Queue for Step 4, set Status `In progress`. Resolved? Set `Fixed` (dated). Wrong on inspection? Set `False positive` + reason. Shipping later? Set `Deferred` + reason.
- De-duplicate: if a later checklist block would surface the same condition, skip the duplicate and trust the tracker entry; just update Last verified.
- `Fixed` / `False positive` / `Deferred` entries are read-only.

If the tracker is missing, the audit creates it on first write. Schema: `| ID | Status | Severity | Source | Last verified | Issue | Proposed fix |`. Give each source its own ID prefix (`A-` for this audit, a different letter for any other pass that files findings) so provenance survives.

## 0.5 Liveness canary (run FIRST, every trigger; this is the anti-"broken for days" layer)

Fast reachability probes, run before the deep checklist. Each returns ALIVE or BROKEN with the evidence command. A BROKEN probe goes to the TOP of the report ("Broken now") with days-broken = today's date minus its findings-tracker ID date (open a today-dated finding if it is new, so the age grows next run). Read the newest system-inventory document first, where one exists, and fold in any liveness finding it surfaces; a pass that walks the live system catches reachability the static list below can miss.

Probe every background service the setup actually runs. The list below is the shape, not a fixed inventory: build it from what this setup has, and drop any line that names something it does not run.

- [ ] Each local model or embedding service the setup depends on answers on its own port. BROKEN usually means something silently degrades rather than failing loudly (semantic memory falling back to keyword-only, for example), which is exactly why it needs a probe.
- [ ] Memory or vector index healthy: its stats show the embedding service up, recall not regressed, chunk/vector counts not collapsed.
- [ ] Each long-running local server responds on its port, or its background service is loaded per the OS service manager. Record the exact restart command next to the probe so recovery is one paste.
- [ ] Hook chain: every hook in `settings.json` exists and is executable; per-hook log freshness (event fired but log silent 7 days means it may be dead); any health-check script exits 0.
- [ ] Scheduled tasks: every ENABLED task ran within its cadence (last run fresh, next run not in the past); flag any task that flipped to disabled on its own.
- [ ] Backup pushed: the newest successful push in the backup log is under ~24h old.
- [ ] JSON configs valid: `jq empty` on `settings.json`, `settings.local.json`, `~/.claude.json`. A parse error means hooks, permissions and MCP servers silently do not load, with no error shown.
- [ ] Metered-API guard wired: the hook that blocks commands calling the API endpoint is present in `settings.json` PreToolUse[Bash]. Missing means the guard is gone. Skip this probe where the user genuinely builds on the API.
- [ ] No live API key in project dotfiles: grep the code directories' `.env*` files for key-shaped values and for public-prefixed build variables that would ship to a client bundle. Any hit is HIGH.
- [ ] Background writer not stuck: any queue or embed log tail has no repeated `database is locked` or repeated `500` storm.
- [ ] MCP reachable: configured servers connect; a needs-auth server is degraded, not dead, and should be reported as needing a reconnect.

The probes most often skipped are the highest-value ones, because they are exactly the failures that stay silent: service reachability, index health, background-service loaded state, scheduled-task cadence, and backup-push freshness.

## 0.6 Dynamic discovery (so the scan does not go blind to new things)

Discovery over hardcoding, extended. Enumerate at runtime instead of trusting a fixed list.
- [ ] Enumerate every artifact class live: `ls -d ~/.claude/*/` plus the top-level surfaces of the user's own working root, skills, hooks (from `settings.json`), scripts, agents, plugins (marketplaces + installed), MCP servers (`~/.claude.json` + project), scheduled tasks, OS-level background services (filtered to the ones this setup owns, or the exact names a per-setup config lists), rules, playbooks, contexts, memory-type prefixes.
- [ ] Diff that inventory against `~/.claude/audits/inventory-latest.json` (written by the previous run). For anything NEW: identify what it is, probe it generically (referenced/wired? producing fresh output? erroring?), and report "new since last audit, works?, needs a standing check?".
- [ ] Generic probe for EVERY executable artifact (hook, script, LaunchAgent, scheduled task, server), not a per-item hardcode: (a) wired/referenced somewhere, (b) fresh output, (c) not erroring.
- [ ] Close with the meta-question: "what exists that no block in this checklist covers?" Whatever surfaces becomes a new checklist item next revision.
- [ ] Step 4 writes the fresh inventory back to `~/.claude/audits/inventory-latest.json`.

## File health
- [ ] `priorities.md` has real content, not template placeholder.
- [ ] The global lessons file has entries. Per-context lessons files (every other one found live) may be empty; flag one only if that context was active in recent transcripts yet its lessons file has zero entries.
- [ ] The decisions log has entries beyond the first.
- [ ] The todo file is active or clean, not stale.
- [ ] Memory files current (flag content referencing dates >60 days old).
- [ ] The memory index matches the actual files in the memory directory.

## Configuration health
- [ ] `CLAUDE.md` is under 100 lines (current lean baseline ~80).
- [ ] No duplicate rules between `CLAUDE.md` and the playbook or rule files it routes to.
- [ ] No duplicate content between `CLAUDE.md` and context files.
- [ ] Hooks configured in `settings.json` (or noted as not yet needed).

## Directory structure integrity
Universal check, generic on any system: no plan or strategy file loose at a context root when a project folder exists for it; folder hygiene per whatever output-file convention the setup documents, for any folder with 5+ output files (an index or README present, numbered final files, an archive subfolder for superseded ones).

If a per-setup config names an expected project-folder list or per-context subfolder convention, cross-check against it: every context root contains only its named projects, with orphan files at the root flagged; every active project named in a context file has a matching folder; and any context covering several distinct businesses or clients has a subfolder per one. With no config, skip the expected-folder-list check; the generic checks above still run.

## Router + index consistency (discovery-based)
Read the actual router tables in `CLAUDE.md` and the memory index. Do not assume a directory name: a rules directory gets renamed or split during a reorganisation, and every hardcoded reference to it silently rots the moment it does. The router is the only thing that stays true.
- [ ] Every target in the `CLAUDE.md` context router exists.
- [ ] Every target in the `CLAUDE.md` rules/playbooks router exists at the path the router states.
- [ ] Every always-on file named in `CLAUDE.md`'s router (read the list live; do not assume which files) exists.
- [ ] Every per-context index in the memory index exists.
- [ ] Every project playbook referenced in any context file exists.
- [ ] Every memory file has an index entry; every index entry points to a real file. Flag orphans and dead links both ways.

## MCP inventory and redundancy
- [ ] List configured MCP servers from `settings.json` (or `.mcp.json`).
- [ ] Flag duplicate servers in the same tool family (e.g. two Notion installs).
- [ ] Flag any MCP whose namespace never appears in skills, decisions log, or recent transcripts. Propose removal.
- [ ] Flag MCPs deprecated or superseded by a newer install.

## Hook integrity + runtime health (discovery-based)
Do not hardcode hook names; they drift. Enumerate hooks from `settings.json`, then for each:
- [ ] Script exists and is executable (`chmod +x`).
- [ ] Find its log via `>> "$LOG_FILE"` in the script. Count `ERROR` lines in the last 7 days; surface the last 5 verbatim. >0 errors → ACTION.
- [ ] If the event fired (transcripts exist for those days) but the log shows nothing for 7 days → "may not be running".
- [ ] Where a hook enforces a word list or style rule, its list matches the rule file it enforces, exactly. Flag any term in one but not the other: a drifted pair means the hook blocks things the rules allow, or waves through things they ban.

**Subscription-vs-API invariant.** On a subscription plan, any background capture or automation that needs a model call runs through the CLI on that plan, or on a local model, never the metered API. If a hook references `api.anthropic.com` or `ANTHROPIC_API_KEY`, that is a HIGH finding to REMOVE, not a fix-the-key action, because it bills separately on top of the plan and does so on every turn it fires. A guard hook blocking any command that references the API endpoint should be present and active. NEVER recommend setting an API key or running a background script that calls the API. Skip this block entirely for a user who genuinely builds on the API.

Report shape:
```
| Hook | Last successful run | Recent errors | Status |
```

## Memory vs current state
- [ ] For each memory file, scan for claims contradicting the current context files. Flag contradictions (e.g. memory says "X on WordPress" while context says "X migrating to Replit").
- [ ] Memories with absolute dates older than 90 days: flag for "still accurate?" review.

## Security (consume any recent prior scan first)
If another pass populated `findings-tracker.md` with secret findings in the last 7 days, CONSUME them: validate each against current state, do not re-scan from scratch. Run the full scan below ONLY if no recent secret scan exists. Report every finding HIGH/MEDIUM/LOW with a specific remediation. Never echo secret values.

Full scan (when needed):
- [ ] Scan the whole working root for `.env*`, `*credentials*`, `*secret*`, `*.pem`, `*.p12`, `id_rsa*`, `*.key`, `*token*`, and any `*.mcp.json` with embedded auth. Weight this scan heavily if that root is synced to cloud storage or backed up off-machine, since a secret there has left the laptop.
- [ ] For each `.env*` found: report keys only, classify (HIGH: write-scope secrets, private keys, bearer tokens, DB creds; MEDIUM: read-only keys, host+user tuples; LOW: public URLs/IDs).
- [ ] Flag any private key sitting inside a synced or backed-up folder; a private key belongs in the local-only SSH directory and nowhere else.
- [ ] Flag hardcoded tokens in `.mcp.json` / settings / non-env config.
- [ ] `settings.local.json` permissions: flag over-broad grants (`Bash(*)`, unfiltered `Edit`) and stale entries (removed tools, moved paths).
- [ ] Grep memory/context/lessons/plans for token-shaped strings (`sk-`, `pk-`, `ghp_`, `ntn_`, `Bearer `, long hex/base64 > 32 chars). Report file + line, never value.
- [ ] For each code repo: `.gitignore` covers `.env*`, any private-env directory, `credentials*`, `*.pem`, `*.key`, `secrets*`. If it has a remote, scan the last 20 commits for committed secrets; flag by commit SHA, never echo the value.

Remediation follows `references/cleanup-tiers.md` Red rules: surface + propose move, rotation only on a concrete leak signal.

## Skills health
- [ ] Total skill count + estimated description character usage against the budget.
- [ ] Overlapping descriptions that could misfire.
- [ ] Skills not updated in a long time (file dates).
- [ ] All skills follow the generic rule (no hardcoded project, currency, or geography), EXCEPT environment-specific operational skills like this audit, which have to name the real environment to do their job.
- [ ] Invocation frequency (60d): top 10 + counts. Flag any skill with 0 invocations in 60d as a deletion candidate (document any kept-as-reference exception).

## Workflow + pattern mining
- [ ] Decisions log: repeated decision types that could become a rule or skill.
- [ ] Lessons: repeated corrections that could become a hook or rule (feeds Step 5).
- [ ] Lesson buildup: count near-duplicate clusters (3+ entries on one theme) and flat-file size per lessons file. A file past roughly 1,500 lines, or a theme with 3+ near-dupes, feeds Step 5 consolidation (merge to canonical + archive). The metric is duplicate-clusters and ungraduated-clusters, not raw count.
- [ ] Memory: feedback entries hinting at missing automation.
- [ ] A manual process described in multiple places is a sign it should be a skill.

**Transcript patterns (user-side, last 30d, `~/.claude/projects/**/*.jsonl`).** Report only 3+ occurrences or a clear pain signal:
- [ ] Repeated prompt shapes used 3+ times → candidate skill/command. `{prefix, count, sessions}`.
- [ ] Long multi-turn resolutions (10+ user messages to one task) → candidate compression. `{task, turns, proposal}`.
- [ ] Copy-paste friction (500+ char pasted blocks repeated 3+ times) → candidate MCP/skill. `{type, count, proposal}`.

**Tool-call failure modes (AI-side).** For the metrics dashboard (token spend, tool-time, cache, per-context), use whatever context/usage dashboard is installed rather than re-deriving it here. From the JSONL logs surface ONLY the actionable failure modes such a dashboard does not:
- [ ] Retry storms: same tool, same args, 3+ times in a session.
- [ ] Silent errors: a tool returned `is_error`/non-zero and Claude continued without recovering.
- [ ] Permission-denial loops: same prompt denied 2+ times across sessions (allowlist vs change-approach).

Report top 5-7 with `{pattern, ≤3 example sessions, proposed change, expected saving}`. If nothing met the bar: "No optimization patterns surfaced this period." Do not manufacture findings.

## Lesson follow-through (closes the loop)
For each entry in each lessons file, extract the pattern and the how-to-apply line, then derive a test from them.
- [ ] Scan last 30d transcripts for violations (scoped lessons only in their context's transcripts).
- [ ] Report each violation: `{scope, lesson, date, session, did-vs-said}`.
- [ ] A lesson with 2+ violations since written → promote it to a stronger location (playbook for global, context file for scoped, hook, or skill instruction). Add to Step 5 graduation candidates.

## Capability gap (feeds the "what you're not using" report)
Read `references/capabilities.md`. Cross-reference the 7 primitives against actual usage:
- [ ] Skills: any using `context: fork`, `allowed-tools`, `disable-model-invocation`, dynamic `!`command`` injection, or skill-scoped hooks? If not, name candidates.
- [ ] Hooks: rules in `CLAUDE.md`/playbooks describing automated behaviour are hook candidates.
- [ ] Agents: does `~/.claude/agents/` exist? Repeated delegation instructions are agent candidates.
- [ ] Plugins: installed? Note available-but-not-needed.

Rank each unused-but-fitting capability High / Medium / Low fit against active projects. Use the Capability Adoption Signals table in `references/capabilities.md` to map patterns to recommendations.
