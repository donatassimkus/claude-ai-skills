---
name: manual
description: Live descriptive inventory of your entire AI-assistant system. Scans the assistant's configuration tree and working tree fresh on every invocation and produces a strategic bird's-eye-view manual: what makes this setup unique, the stack architecture, configuration surfaces, request flow, capability surface, plus an inventory layer (skills, hooks, connected tools, rules, contexts, memory) and an operational layer (decisions, scheduled tasks, health Pareto, open issues). Read it to understand how the system runs end to end. Self-discovering: every run delta-scans for new top-level surfaces and reads each subsystem's own architecture doc, so the report stays current as the system grows instead of being capped by this skill's section list. Where the operator keeps a dashboard or explainer page carrying hardcoded system counts, every run also SYNCS what it discovered into it, so the explainer never drifts from the real system. Use when onboarding a new operator, sharing the setup, or when the mental model has gone stale. Triggers, /manual, "show system manual", "system inventory", "how is this set up", "what skills do I have".
user-invocable: true
argument-hint: "[--depth exec|full|deep] [--section <name>] [--no-sync]"
---

# /manual

User-invocable live system handbook. Reads the filesystem fresh every invocation. Produces a layered report: strategic bird's-eye view first, detailed inventory second, operational state and open issues third, reproduce/operate fourth, and a coverage self-check that proves the report is current.

## Keep this separate from auditing and optimizing

| Job | Purpose | Output |
|---|---|---|
| This manual | Describe the system (strategic + inventory + state) | Full manual file with bird's-eye top, detail middle, open-issues bottom |
| A system audit | Find drift, dead refs, security issues, redundancy | Action plan with top 3 fixes |
| An optimization pass | Optimize a target across multiple rubrics | Scorecard + reject list, multi-round commit |

This skill answers "how is this set up". The other two answer "what should we change". Keep the lanes separate: the moment a descriptive pass starts fixing things, it stops being a trustworthy baseline. It does perform ONE mechanical write-back: Step 5.7 refreshes a dashboard's live counts to match what it just discovered. That is a derived-data sync (make the explainer match reality), not judgment-based fixing.

## When to invoke

- Onboarding a new operator who needs to understand the system end to end
- Sharing the setup with someone else (the report is ready to paste)
- After a long stretch of changes when the mental model has gone stale
- Before a session-capture or audit pass, to see the baseline first
- Periodically (weekly is fine) to keep a snapshot of state

User-invocable only. Never auto-invoke.

## Depth modes (reader altitudes)

One report, three altitudes. Parse the optional `--depth` arg; default `full`.

- `--depth exec` — one page for a decision-maker: Header + §1 Snapshot + §2 What's different + §7 Capability surface + the §28 Coverage self-check delta. Nothing else.
- `--depth full` (default) — every section below.
- `--depth deep` — full report PLUS the raw dynamic-discovery output (Step 1.5) appended as an appendix, so a rebuilder sees exactly what was scanned and what was unmapped.

Also accept `--section <name>`: regenerate and print only that one section against a fresh scan (no file write). Useful for spot-refreshing a single area without a full run.

Also accept `--no-sync`: run the descriptive manual ONLY, skipping the Step 5.7 dashboard sync. By default the sync runs (the manual is the best moment to refresh those counts); pass `--no-sync` for a pure read-only pass. If the operator keeps no dashboard, the sync step is a no-op and this flag does not matter.

## Step 0: Freshness + discovery contract

This skill never reads memory or any cached state for content. Every invocation runs fresh filesystem reads. Memory routing files (MEMORY.md, MEMORY-{context}.md) are read as data to inventory, not as conversational memory.

Do not rely on prior session context. Re-scan everything.

**Discovery contract (this is what keeps the manual from going stale):** the section list below is a STARTING template, not a ceiling. The system grows faster than this skill is edited, so every run must actively look for what the template does not yet name. Two non-negotiable rules:

1. **The subsystem's own doc is the source of truth, not this skill's mental model.** When a subsystem ships its own architecture/reference doc (memory stack, the front-end console, the graph viz, the capabilities inventory, any `reference_*` doc describing system internals), READ it and summarize from it. Never describe a subsystem from a hardcoded paragraph in this skill: that paragraph rots the moment the subsystem changes.
2. **Unmapped surfaces are reported, never dropped.** Any top-level surface that does not map to a section is surfaced in the Coverage self-check (§28), and if material, gets a provisional section drafted this run. Silence is failure: a surface the template forgot must still appear.

## Step 1: Parallel filesystem scan

Issue this as ONE batched call if your environment has a tool that runs many shell commands in parallel and keeps their output out of the main context; otherwise run them directly. Batching matters at this size: this is roughly twenty reads, and firing them one at a time floods the context window with raw listings you only need summarised.

Resolve every target below against THIS host's actual layout before scanning. Two trees matter: the assistant's CONFIGURATION tree (where skills, subagents, hooks, settings, and connected-tool config live) and the operator's WORKING tree (where their projects, trackers, and archives live). Detect both rather than assuming; on some hosts they are the same directory, on others the config tree is a hidden folder in the home directory and the working tree is a separate project root. Everything below is a responsibility, not a path: find the equivalent on this host and read it.

Scan, in parallel:

- **host info**: date, OS/kernel, current working directory. Stamps the report.
- **skills**: every skill definition, with file dates. Also resolve any SYMLINKED skill to its target, since a symlinked skill lives somewhere else and that is worth showing.
- **subagents**: every subagent definition.
- **settings**: the assistant's settings file, plus any local or override settings file beside it.
- **connected tools**: the config listing connected tool servers, both globally and per-project. Capture the keys, not the values (see Safety: config values can hold secrets).
- **rules and playbooks**: the always-on rule files and the operation-triggered playbook files.
- **contexts**: the context files, plus the routing tables that decide when each loads. If those routers live inside a top-level instructions file, extract just those sections rather than reading the whole file.
- **memory**: the memory corpus, as a total file count and a count broken down by filename prefix.
- **decisions**: the tail of the decision log.
- **scheduled tasks**: the scheduled-task definitions on disk.
- **plugins and marketplaces**: installed plugin sources, if the host has a plugin system.
- **hooks**: every hook script on disk.
- **working tree**: the task and tracker files, the per-context project folders, the code repos, and the archives.

**Memory-count gotcha, and it is a real one:** if the host stores memory under a per-project directory, a wildcard across all project directories OVER-COUNTS, because stale or duplicate project directories linger and get summed. Count only the CANONICAL directory: the one matching the current working directory, equivalently the one holding the most files. Never sum the wildcard.

**Parse frontmatter and hook config with a real parser, not line-oriented shell.** For per-skill invocation flags, plugin-provided skills, and the settings hooks block, run a small script that parses the YAML/JSON properly. Line-oriented tools truncate multi-line YAML descriptions and multi-line hook arrays, so a shell-only pass silently under-reports both. The same script should pull each hook script's first-comment description, which is what fills the "What it does" column later.

If the operator keeps a telemetry or capabilities inventory (a file recording most-used skills and tools), read it here: it supplies the usage counts several sections below depend on.

## Step 1.5: Dynamic discovery and delta scan (do NOT skip)

This is the phase that future-proofs the manual. The static section list cannot describe what was added after it was written, so this step finds it. Run a second batched scan and a set of targeted reads. For an `--depth exec` run, still do 1.5a and 1.5d (they feed the Coverage self-check); 1.5b/1.5c can be lighter.

**1.5a Surface enumeration + delta-vs-known.** Enumerate every top-level surface and diff against the KNOWN-SURFACES list below.

List every immediate subdirectory of the assistant's configuration tree and of the operator's working tree. That listing is the raw surface set.

KNOWN-SURFACES is the list of surfaces this template already has a home for. Maintain it as a list inside this skill, and seed it on first run from whatever the operator's system actually has. A typical starting set: skills, subagents, hooks, rules, playbooks, contexts, decisions, scheduled tasks, generated manuals, plugins, the memory corpus, supporting scripts, an ingested-sources knowledge base, per-domain automation folders, templates; and in the working tree: active work, code repos, task trackers, archives. Treat that as an example rather than the answer, because the whole point of this step is that the real list is whatever the scan returns.

Anything in the scan that is NOT in KNOWN-SURFACES is "unmapped" and must be investigated this run and listed in §28: inspect it (list it, read any README or doc inside), then either map it to an existing section or draft a provisional section for it. If the same unmapped surface shows up across two runs, that is the signal to add it to KNOWN-SURFACES and give it a permanent section (note that in §28 as a skill-maintenance to-do).

**1.5b Read each subsystem's own doc.** The subsystem's doc beats this skill's memory. Discover and read them:
- List the operator's internal-architecture docs (wherever they keep reference documentation) and skim the names for system-internals docs: the retrieval or memory stack, any front-end console or dashboard, a visualization layer, the deploy stack, per-integration references.
- ALWAYS read, if present: the capabilities or tooling inventory, the memory/retrieval architecture doc, and any doc describing a front-end the operator built over their own system.
- Summarize each section FROM its doc and link the doc. If a subsystem has no doc, note that gap in §28 (a subsystem without its own doc is a documentation risk).

**1.5c Delta vs the previous manual.** Read the most recent previously generated manual (by timestamp) from wherever this skill writes them. Compute the structural delta since then: new/removed top-level surfaces, skill-count change, new/removed connected tools, renamed components, new scheduled tasks, new subsystems. This is NOT a file-churn log (those are explicitly excluded); it is a list of STRUCTURAL changes a reader of the last manual needs to know. Feed it into §28.

**1.5d Data-layer probe.** If the operator runs an indexed memory or retrieval layer, query its stats: indexed file and chunk counts, any entity/edge counts, whether the embedding service is up, and the last evaluation result. This grounds §18 (retrieval health) and confirms the data layer is actually current, not just the filesystem. If there is no such layer, say so in §18 rather than omitting the section.

## Step 2: Targeted MCP queries

After the batches return:

1. Query the live scheduler for its actual state (enabled flag, next run, last run). The definitions on disk are not the same as what is really scheduled; a task can exist as a file and be disabled, or be scheduled and past due.
2. Query the memory/retrieval layer for live index health and last evaluation, if not already pulled in 1.5d.
3. Optional: run a focused search against indexed content for any follow-up question the scan raised.

## Step 3: Synthesise the manual report

Build a markdown document in layers, top-to-bottom. The top layer is strategic (the bird's-eye view the operator scans first). Inventory is for lookup. Operational layer surfaces open issues with proposed fixes. Reproduce/Operate is for a rebuilder. The final Coverage self-check proves currency.

**Plain-English requirement:** every section using assistant-platform internals (hooks, connected tool servers, subagents, symlinks, frontmatter, cron, matcher, transport, deferred tools, plugin vs user-defined, embeddings, knowledge graph, etc.) must start with a one-or-two-line explainer in plain English. End the report with a Glossary section.

**"What + why" requirement for non-obvious capabilities:** any feature where the BENEFIT is not obvious to a first-time reader needs a brief "why this exists" or "why beneficial" subsection. Two-three sentences max. Don't over-explain obvious things. Specifically include "what + why" for:

- The stack architecture (why each layer exists, what would break without it). Read the CURRENT layer model from the memory-stack reference doc; do NOT assume a fixed number of layers, the stack evolves. Render whatever layers the doc defines today.
- Any front-end console the operator built over their own corpus and work trackers (why a local console: removes the assistant-to-external-tool context switch, one front door).
- Retrieval evals (why a golden-query suite exists: it is the proof retrieval still works after any ranking/index change; without it, regressions ship silently).
- Subagents (why fan-out instead of one assistant doing everything: lean main chat, parallelism, isolation)
- Hooks (why automate via hooks instead of asking the assistant to remember: reliability, background execution, blocking power, cross-session continuity)
- Sandboxed-execution and indexed-search tooling, where present (why such tools fire constantly: running commands in a subprocess and searching their indexed output keeps raw output out of the main context window; one batched call replaces dozens of individual shell calls)
- Connected tool servers vs raw API calls (native feel, managed auth, schemas loaded on demand)
- Local CLI tools vs connected servers (perf-critical, offline, no wiring needed)
- Operation-triggered rule loading (why lazy-load instead of always-on: minimal context window weight)
- Context routing + separation (why per-context instead of always-on: prevent confidential leakage across business contexts, plus context-budget)
- Typed memory prefixes (why `user_/project_/reference_/feedback_` instead of flat: the prefix encodes loading rules)
- Synthesis pages (why compiled hub pages on top of atomic memories: a current integrated view per entity without losing the atomic source)
- Decision log separate from lessons (why two files: lessons = corrections, decisions = strategic choices with reasoning trail)
- The findings-tracker handoff between this descriptive pass and whatever audit pass acts on it (why a shared file: avoids re-discovery, keeps each in its lane)

Keep each "why" to 2-3 sentences. The goal is "first-time reader understands not just WHAT but WHY", not "exhaustive technical document". Skip "why" for self-explanatory features (a snapshot table needs no rationale).

**Verbatim source content stays as-written:** skill descriptions, decision-log entries, hook commands, connected-server names, and any other content quoted from source files keep their exact wording even if they contain words the operator's own style rules ban. If a writing-style check runs automatically on written files, exempt the generated manuals directory from it, otherwise every run fights the check over text it only quoted.

**Live layer counts, never hardcoded numbers:** when a count can drift (layers in the stack, tabs on a console, boards in a tracker, sections in this report), read it live and render what you find. Do not write "4 layers" or "6 tabs" from memory; the whole point of this skill is that those numbers change.

### Section list (29 sections across 5 layers + glossary)

This is the STARTING template (see the Discovery contract in Step 0). Add provisional sections for any unmapped material surface found in Step 1.5.

#### Header
- Generated timestamp + host + active context (best guess) + depth mode
- "How to read this manual" intro pointing at the layers

#### STRATEGIC layer (§1-§8)

1. **Snapshot** — top-line counts table. Include rows for: user-defined skills, plugin skills, subagents, hooks, connected tool servers (broken down by how each is configured and authenticated), **local CLI tools**, **external service accounts**, rules, playbooks, contexts, memory files, **indexed chunks + last eval**, scheduled tasks, decisions logged, plugin sources, **unmapped surfaces this run** (from §28). The tools and services counts are the difference from a stock install, which is what a reader wants to see at a glance.
2. **What makes this setup different from a stock install** — the customisations that carry weight, listed from what this run actually found (custom skills/subagents/hooks against a default of zero, any retrieval stack and front-end over it, forked or custom plugins, context routing, operation-triggered rule loading, typed memory, a decision log, a lessons loop, scheduled tasks, evals). This is the section a reader scans to understand what was BUILT here rather than what came in the box.
3. **Stack architecture** — text diagram of the layer cake. READ the current layer model from the memory-stack reference doc and render exactly those layers (each: what it does, what breaks without it). Do not assume a count.
4. **Any front-end the operator built over their own system** — SKIP this section if there is none. Where one exists (a local console over the memory corpus and the work trackers), read its own doc plus the memory-stack doc and cover: how the server stays up and on what local address, its views or tabs enumerated live rather than hardcoded, the tracker engine behind it (how many boards it drives, read live), the write discipline it enforces (a single writer, never blind-editing the underlying data file), and any calculated dashboard rolling per-project numbers up to a headline. Why it exists: one front door over the corpus plus the work trackers, with no context switch to an external tool.
5. **Configuration surfaces (ranked by reach)** — the surfaces ranked by how far each one reaches (the top-level instructions file, the settings file, rules and playbooks, contexts, skills, subagents) with what each controls and when to touch it. Rank by blast radius, since that is what tells a reader where a change is risky.
6. **Request flow** — text diagram of one prompt end-to-end: prompt submit → UserPromptSubmit hooks (count + name them live) → Claude routes → tool calls → PreToolUse → execute → PostToolUse → response → Stop hooks
7. **Capability surface** — what the system can DO end-to-end, by outcome (ship SEO blog post = blog-post + SERP + scrape + WP; render social post = social-post + design + browser-verify; etc.)
8. **Session-start load sequence** — what fires when a chat opens: always-on context, SessionStart hooks (count + order them live), conditional context (per-keyword), operation-triggered rules, "what you can prune" subsection

#### INVENTORY layer (§9-§18)

9. **File structure** — compact 4-5-level tree of the configuration tree and the working tree (task trackers, work organized by context and project, code, archives, plugins, supporting scripts, any ingested-sources knowledge base, templates). Trim aggressively, don't list every file. Every KNOWN-SURFACE appears here.
10. **Skills (grouped by domain)** — domain categories (Meta, Strategy, Acquisition, Conversion, Retention, SEO, Content, Email, UX, Build, Hacks, plus any new group discovered). Each row: name, description, **Invocation** (manual / both). NO argument-hint column in the per-skill tables (noise for bird's-eye reading). Add a short legend explaining invocation modes at the top. Then open the section with a short **How to invoke a skill (arguments + examples)** subsection: the `/skill-name [arguments]` pattern, a note that `both` skills also auto-fire on description match while `manual` skills are slash-only, the count of skills declaring an `argument-hint`, and 4-6 real worked examples pulled live from skills' `argument-hint` frontmatter (the `argument-hint` is each skill's usage contract). Always include at least one example that passes a multi-word quoted value and one flag-only example (e.g. `--depth`). Tell the reader to quote multi-word argument values that contain punctuation.
11. **Plugin skills (operator-relevant only)** — group by source plugin/marketplace. Note heavy cross-marketplace duplication (same skill under multiple marketplaces) and give a unique-vs-on-disk count. Trim Anthropic-internal dev tools (skill-development, plugin-structure, hook-development, etc.) into a single line: "+N internal dev tools available, see file at runtime if you ever build plugins".
12. **Subagents (combined: built-in + plugin + user)** — single merged table with Source column. Include subsections in this order: (a) "Why subagents instead of one Claude" — benefits (lean main chat, parallelism, isolation). (b) "How they get invoked" — three trigger patterns. (c) "How a subagent reasons (inside-the-process)" — brief → system prompt = description → tool whitelist → standard reasoning loop → returns summary. (d) "Which subagents can edit" — table showing edit capability per subagent + the discipline (auditors deliberately lack edit tools so they can't self-apply conclusions). (e) "Fan-out + arbitrate pattern" — text diagram of the optimize-vs-skill flow showing how parallel specialists + neutral arbiter + objective-function decision + operator approval prevent silent compromises and dominant-voice bias.
13. **Hooks** — per event type (SessionStart / PreToolUse / PostToolUse / UserPromptSubmit / Stop) with matcher + "What it does" column for each. Pull description from first comment in hook script. Note any script present in the hooks dir but NOT wired in settings.json (orphaned/consolidated) so the reader knows what is live vs legacy.
14. **Integrations & tools** — four subsections, NOT just MCP:
    - **14.1 Connected tool servers (decoded)**: every connected namespace, including any that appear under an opaque machine-generated id, each with its PLAIN name, auth method, and recent call count from telemetry. NEVER list an opaque id without its plain name: an inventory of unreadable identifiers is not an inventory. Mark redundant or duplicate installs and any connector currently failing authentication.
    - **14.2 Local CLI tools**: organize as 3 subgroups: (a) "What's installed and ready (specialty tooling)" — whatever specialist binaries this run actually found (media, transcription, model runtimes, runtimes, version-control CLIs, JSON and database tools, the operator's own script suites). (b) "Always available (OS-bundled)" — archive tools, HTTP clients, image tools, text-processing tools, the system scripting runtime, remote-access tools, grouped by capability. (c) "Installable on request" — categories the operator can install when needed (document conversion, PDF, image, HTTP, cloud CLIs, database, container) with example install commands for THIS machine's package manager. The point: capability-oriented, not tool-oriented. The operator should be able to answer "can I do X?" quickly.
    - **14.3 External services & API access**: full inventory with account location, access mechanism (connected server / API / web UI / SSH), and notes. Include sites, hosting, CRMs, design tools.
    - Cross-reference the operator's capabilities inventory, if they keep one, as the canonical auto-refreshed source for this section.
    - **14.4 Connectors by context (dynamic, never merge)**: a per-context view so the operator can see at a glance what belongs to which sphere of work (14.1 is the by-type view and deliberately merges them; this is the complement). Skip this subsection entirely for a single-context system. Otherwise read the live connected-tool config, the account map, and whatever file classifies each connector to a context. Render ONE table: one row group **per context discovered live** (from the context router parsed in §16, never a hardcoded list here) plus a "cross-cutting tooling" group for connectors serving no single context. **CRITICAL, no silent merging:** any live server, account, or granted property that the classification file does NOT cover gets its own **"unassigned, needs classifying"** row; surface the unassigned count in §1 Snapshot and add each one to §22 as a Low-severity "classify by context" item. Because the grouping is read from that file every run, it stays current as connectors are added, removed, or reclassified, with no edit to this skill. The reason to be strict: an unclassified connector silently folded into the wrong context is exactly how material from one sphere of work reaches another.
15. **Rules & playbooks** — two tables: always-on rules (file, first heading); operation-triggered playbooks (file, which operation loads it, parsed from the rules-routing table in the top-level instructions file).
16. **Contexts & separation model** — the router table (file, trigger keywords, parsed from the context-routing table in the top-level instructions file) PLUS the separation model: the never-mix rule, asking before loading when a topic is ambiguous, per-context memory router files that load lazily, and any context axis carried elsewhere in the system (a context field on the work trackers, a context mode in any visualization). Why: confidentiality across separate spheres of work, plus keeping the context window light.
17. **Memory layout** — naming convention legend (`{type}_{project}_{topic}.md`), counts by prefix, router files, **synthesis pages** (what they are: compiled hub pages over atomic memories, weekly-refreshed), and the **`kb/` knowledge base** (ingested raw sources: count + what's in it).
18. **Retrieval health & evals** — read from the memory-stack doc + memory_stats. Cover: the golden-query eval suite (recall@K + MRR, current baseline, when it runs), degradation behavior (embedder down → keyword-only) + disaster drill (DB rebuilds from markdown, how fast), and live index state (files/chunks/entities/edges + embedding service up/down + last eval) from memory_stats. Why it exists: this is the proof retrieval works, the "is it bulletproof" evidence.

#### OPERATIONAL layer (§19-§22)

19. **Decisions log** — last 5 entries from the decision log. Skip the full log.
20. **Scheduled tasks** — task ID, schedule (human-readable), enabled flag, next run, last run. Flag any disabled or past-due task for §22.
21. **Operational health (Pareto)** — pull whatever usage telemetry the system records: most-used skills over a fixed recent window, most-used connected tools over the same window with actual numbers, critical hooks (those that fire constantly or can block), and active versus orphaned items. If no telemetry exists, say so rather than estimating.
22. **Open issues (actionable, with proposed fixes)** — concrete items where action would clear noise or fix bugs. Each entry: where, impact, proposed fix, Severity (mandatory). **Must include any security findings** (tokens or keys sitting outside the designated secrets location, orphan or unidentifiable connectors, duplicate installs) AND anything surfaced by Step 1.5 (an unmapped surface that looks like dead state, a subsystem with no doc, a disabled scheduled task). Order by severity (Critical to High to Medium to Low). End by pointing at whatever audit pass acts on these, since this skill surfaces them and does not fix them.

#### REPRODUCE / OPERATE layer (§23-§27)

23. **Replicate this setup on a fresh machine** — step-by-step, derived from what THIS run actually found rather than a fixed list: copy the configuration and working trees, install the local tooling the system depends on (name the actual packages found in §14.2), start any local model or embedding service and pull its model, rebuild any index from source rather than copying the old database (re-embed from the markdown, so a corrupt index cannot travel), make hook scripts executable, configure credentials for each connected tool, install plugins, then verify by re-running this manual plus whatever health checks exist. End with a portable-vs-machine-specific table, since the split between what copies and what must be recreated per machine is the part people get wrong.
24. **Failure modes & canary commands** — for each load-bearing dependency this run found (a local model or embedding service, the vector store, hooks, each connected server, any plugin the workflow leans on, a local console server), state what stops working when it fails and how the failure presents. Include a canary command per dependency that the operator can run to verify health, since "is it broken?" is the question this section exists to answer in one command.
25. **Maintenance cadence** — the recurring rhythm, built from what this system actually has: per-session capture, a handoff before clearing context, whatever consolidation and briefing jobs run on a schedule, a periodic audit pass, this manual as needed, a periodic decisions-log review, on-issue health checks, and the operator's stated stance on secret rotation.
26. **Security & secrets** — single consolidated reference for every credential: location, blast radius if leaked, rotation stance. Group rotation discipline (preferred location, acceptable, avoid, never) and per-machine vs per-account distinction. Scan the connected-tool config, the settings files, the operator's secrets directory, OAuth grants, and SSH keys. Report LOCATIONS and never values. Follow whatever rotation stance the operator has actually set rather than imposing one: if they have decided against scheduled rotation for a single-operator local machine, respect that and flag only on a concrete leak signal.
27. **Limitations & deliberate exclusions** — two parts: (a) "Design trade-offs" — the bounded context window, local model startup time, indexing lag behind edits, per-machine re-authentication, the token cost of fanning out to subagents, schedulers that need the machine awake, and hook false-positives. (b) "Deliberate exclusions" — no CI/CD orchestration, no auto PR reviewer, no Slack output bot, no team workspace, no OpenAI default, no multi-machine sync, no external observability, no auto-graduation of memory to rules. Knowing the boundary prevents debugging into corners that aren't bugs.

#### META layer (§28) + Glossary (§29)

28. **Coverage self-check (blind-spot honesty)** — the capstone that proves currency. Include: (a) surfaces scanned: N; mapped to a section: M; **unmapped: K, each listed with a one-line "what it is + provisional home"** (from Step 1.5a); (b) **delta since the last manual** (its date): structural new/changed/removed (from Step 1.5c); (c) subsystem docs read this run (list), and any subsystem WITHOUT its own doc (a gap to close); (d) any KNOWN-SURFACES list maintenance the next skill edit should make (e.g. a recurring unmapped surface to promote to a permanent section). This section is mandatory. It is the difference between "complete for the template" and "current".
29. **Glossary** — alphabetical plain-English definitions for every jargon term used in the report.

### Sections explicitly NOT to include

- Trigger map (operator assumes routing is solved; cut)
- File-churn logs / "files modified in the last 7 days" (operator wants current state, not history). NOTE: this is distinct from §28's structural delta-since-last-manual, which IS included — that is "what components changed", not "which files were touched".
- Lesson file line counts as a standalone section (line counts are noise; lesson files appear in §1 counts and §8 conditional load)

### Layout discipline

- Compact tables, no prose padding
- Section 1 (Snapshot) MUST fit on one screen
- Strategic layer (§1-§8) is the most-scanned, lead with structure not detail
- Inventory layer is for lookup, not reading top-to-bottom
- Open issues (§22) is the only actionable section; surface 3-5 specific issues with proposed fixes, then point at the audit pass for anything deeper
- Coverage self-check (§28) is short and honest, not padded

## Step 4: Top-line summary in chat

After the file is written, post under 25 lines to chat:

```
Manual generated. Top-line state:

| Surface | Count |
| Skills | N user + N plugin |
| Subagents | N |
| Hooks | N entries / N events |
| MCP servers | N config + N runtime |
| Rules + playbooks | N + N |
| Contexts | N |
| Memory files | N (M indexed, eval recall@5 X%) |
| Scheduled tasks | N |
| Unmapped surfaces this run | N (in §28) |
| Open issues | N (in §22) |

Full report: <the manuals directory>/manual-YYYY-MM-DD-HHMM.md

Strategic layer at top (§1-§8), inventory in middle (§9-§18), open issues at §22, coverage self-check at §28. To act on §22 issues, run the audit pass.
```

Use markdown link format for the file path so the user can click through. If `--depth exec`, say so and note the deep sections were skipped by design.

## Step 5: Write the full report

Write to a dedicated `manuals/` directory inside the configuration tree, filename `manual-YYYY-MM-DD-HHMM.md`. Create the directory if missing.

Never overwrite an older manual. The timestamp in the filename is what preserves history, and the prior manual is what Step 1.5c diffs against on the next run: overwrite it and the delta check silently becomes a no-op.

## Step 5.5: Update findings-tracker.md (handoff to the audit pass)

After writing the manual, sync the §22 open issues to a `findings-tracker.md` at the root of the configuration tree. This is the structured handoff file an audit pass reads.

### Schema

Single markdown table at the top of the file:

```
| ID | Status | Severity | Source | Last verified | Issue | Proposed fix |
|---|---|---|---|---|---|---|
```

- **ID format**: `M-YYYY-MM-DD-NNN` for manual-discovered, `A-YYYY-MM-DD-NNN` for audit-discovered. NNN is sequential within that day-source.
- **Status values**: `Open` | `In progress` | `Fixed` | `False positive` | `Deferred`
- **Severity values**: `Critical` | `High` | `Medium` | `Low`
- **Source**: which skill run discovered it (e.g., `/manual run 2026-05-08 17:03`)
- **Last verified**: ISO date when finding was last confirmed present

### Behavior on each /manual run

For each finding currently surfaced in §22:

1. **Match against existing tracker entries by description hash.** If a similar M-prefixed entry exists with status `Open`:
   - Update its `Last verified` to today.
   - Don't create a duplicate.

2. **If the finding is new (no match):**
   - Append a new row with next available ID (`M-YYYY-MM-DD-NNN`).
   - Status = `Open`, today's date for both Source timestamp and Last verified.

3. **For existing M-prefixed Open entries NOT surfaced this run:**
   - Re-verify the underlying condition (run the same check that would surface it).
   - If condition is no longer present: mark `Fixed (auto-detected YYYY-MM-DD)`.
   - If condition still present but not picked up this run: leave alone, may be noise.

4. **Never touch entries that are:**
   - `A-` prefixed (audit's territory)
   - Status `In progress`, `False positive`, or `Deferred` (operator or audit set these intentionally)

### File location

At the root of the configuration tree, so it sits at system level. If the operator already keeps per-project findings trackers, this is the same convention applied once at the system root rather than per project.

If the file doesn't exist, create it with this header:

```
# Claude Code System Findings Tracker

Single source of truth for known issues discovered by the descriptive manual pass or the audit pass.
- The manual writes M-prefixed entries (descriptive scan)
- The audit writes A-prefixed entries and updates statuses (active fixing)
- Both read this file. Both follow the schema below.

| ID | Status | Severity | Source | Last verified | Issue | Proposed fix |
|---|---|---|---|---|---|---|
```

After updating: do NOT report a long diff in chat. Just include in the chat top-line summary the count of open findings and the file path.

## Step 5.7: Sync any dashboard that displays system counts

SKIP THIS STEP ENTIRELY if the operator keeps no dashboard, status page, or README that displays counts about their own system. It is a no-op then, not a gap. Where such a page DOES exist, this step matters, because a hand-maintained count is the fastest-rotting thing in any system: nobody notices it is wrong.

The manual is the system's most thorough discovery pass, so it is the right moment to refresh those figures. Anything the page derives dynamically already takes care of itself; the targets here are the counts and prose figures HARDCODED in the page source, which drift silently. Runs by default; skip with `--no-sync`. Confirm the revert path before editing (version control is enough) and say what it is.

**First, re-read the source of truth, and do not trust any map of it kept in this skill.** Same anti-rot rule as the discovery contract (Step 0): read the page's own architecture or reference doc before editing, to find where the data currently lives. Any table you keep here is a starting guide, not a ceiling, because the page evolves independently of this skill.

**What to sync:** every datum this run established as truth that the page states as a fixed number. Typically: the skill count, subagent count, hook count (total AND the per-event breakdown), connected-tool count, context count, scheduled-job count, and the memory breakdown by type. Plus one structural case: a newly discovered connected tool that the page's inventory does not list yet.

**How:**
1. **Locate by pattern, never by line number** (the page evolves). Search the page for the rendering function or the label near the number, and confirm the live token before editing.
2. **Update only on mismatch.** Compare discovered truth against the hardcoded value; if equal, do nothing. Most runs change nothing, and a step that rewrites unchanged files produces noise in version control that hides the real changes.
3. **A newly discovered tool is the one structural add.** Add it wherever the page's inventory is sourced from, preferring a data file the page parses at serve time over the page source itself, so the row appears without a code edit. Give it a short plain-English purpose so its description cell is not blank.
4. **Keep any breakdown summing to its total.** If a total moves, update BOTH the total and the per-category rows behind it. An inconsistent total is the single most common drift, and it is worse than a stale number because it destroys trust in every other figure on the page.
5. **Anything else hardcoded counts too.** If you find another fixed figure (a new tab, a new card), update it and note it in §28. Silence is failure, same as the discovery contract. Leave anything that rebuilds itself alone.

**A caution if the page has a filtered or scoped view.** Where the page can be viewed scoped to one audience or context while hiding others, keep every description you write generic and tool-level, with no detail private to one context. A description written for the full view leaks into the scoped view, because the scoping hides rows, not the words inside a row that is still shown.

**Verify + report:**
- Confirm how the page picks up changes (served fresh per request, re-parsed at serve, or needing a restart) and act accordingly. If a local server is running, reload and confirm the new counts render with no console error.
- Never invent a number: if a count cannot be derived this run, leave it alone and note the gap.
- One line in the chat top-line, naming what moved: for example `dashboard synced: skills 70 to 72, added one connected tool`, or `dashboard: already current`.

## Step 6: Final chat message

End with a single sentence inviting the operator to drill in if needed. Do not summarise the report, the chat top-line already did.

## Output file format

Plain markdown. No frontmatter required. Sections matching the list above (plus any provisional sections discovered this run).

The file is shareable with someone running a similar setup: they can read it and learn how the system is wired without asking questions. Before sharing it outside the operator's own machine, re-read §14 and §26 with fresh eyes, because an inventory of accounts, connected services, and credential LOCATIONS is exactly the document you would least want to hand to the wrong person.

## Path display rule

Follow whatever path-display convention the operator's writing rules set: chat output uses their preferred display form, while internal scan commands use the resolved real path. Keep the two consistent within one report.

## Edge cases

- **Memory directory glob resolves to multiple project dirs**: count only the CANONICAL dir (the one matching the working directory, equivalently the one with the most files). NEVER sum a wildcard across all project directories: stale duplicate directories inflate the total, and this is a real observed failure, not a hypothetical one. It reports a memory corpus roughly a fifth larger than it is, and because the number looks plausible nobody catches it.
- **No scheduled-tasks directory on disk**: rely on the live scheduler query only.
- **A rule file has no first-line heading**: use the filename as the summary.
- **A skill SKILL.md has no `description`**: list as "(no description)" and surface in §22 if material.
- **A subagent is granted all tools via a wildcard**: render as "all tools" rather than the literal wildcard character.
- **A scheduled task's `nextRunAt` is in the past, or it is disabled**: surface in §22 as actionable (proposed fix: re-enable or delete).
- **Settings file is malformed JSON**: report parse error in the relevant section, do not abort the run.
- **Plugin skills count differs from session-prompt skill list**: cross-check both, prefer the live filesystem.
- **An unmapped top-level surface is found (Step 1.5a)**: never drop it. Inspect it, map or draft a provisional section, and list it in §28. If it recurs across runs, flag it as a KNOWN-SURFACES addition for the next skill edit.
- **A subsystem has no own doc**: summarize from direct inspection of its files, and record the missing-doc gap in §28.
- **`memory_stats` MCP unavailable**: report index health as "unverified this run" in §1 and §18; do not fabricate counts.
- **No previous manual exists (first run)**: §28 delta says "baseline run, no prior manual to diff".

## Quality bar

- **Strategic content first**: §1-§8 must be reader-scannable in under 5 minutes.
- **Concrete > vague**: every row has a name, a count, a path.
- **Compact tables over prose**: a manual is scannable, not narrative.
- **Live numbers, not remembered ones**: layer counts, tab counts, board counts, section counts are read this run, never carried from a prior manual or this skill's text.
- **Subsystem doc beats mental model**: every subsystem section summarizes that subsystem's own doc and links it.
- **Open issues are actionable**: §22 entries have a "where + impact + proposed fix" structure. Anything purely informational does NOT belong in §22.
- **Coverage is honest**: §28 names what was not mapped. A run that maps everything still states "0 unmapped" explicitly.
- **No redundancy**: don't list the same fact in 3 sections. The Snapshot has counts; deep tables have details.

## Safety

- Every write is low-risk by construction: local only, reversible, and never overwriting a prior manual. Follow whatever live-write rules the operator keeps.
- No memory writes.
- No skill or settings file modification.
- No external API call. Every connected-tool call is READ-ONLY: the scheduler list and the index stats, nothing else. If you find yourself wanting a write call, you have left this skill's lane.
- **Secrets are redacted before the report is written.** Connected-tool config routinely holds tokens and keys in environment blocks, so read those config files for their KEYS and never render their values. Report where a credential lives, never what it is. This is the one place a descriptive skill can do real damage: the report is a file, files get shared, and a manual that quotes an environment block has published a secret.

## Pairing with other skills

| Pair | When |
|---|---|
| This manual, then an audit pass | Snapshot first, then look for issues; the audit's findings become readable against the manual's structure |
| This manual, then a session capture | Snapshot the system, then capture session learnings on top of a known baseline |
| This manual standalone | Just want to understand the current state |

This skill is read-only apart from the manual it writes, the findings tracker it syncs, and the optional dashboard count refresh. It never triggers an audit or an optimization pass automatically. §22 surfaces actionable items so the operator can choose.
