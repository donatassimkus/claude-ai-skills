---
name: save-session
argument-hint: [all | auto | yolo | save all]
description: Promote THIS CHAT's learnings into permanent memory. Scans ONLY the current conversation (plus this session's own staged blocks), categorizes, dedupes against the existing corpus by search, and writes memories/contexts/decisions/lessons/capabilities — each new reference/project memory gets recall cues so it is findable later. Surfaces only current-chat items; never pulls other chats' backlog into the chat (that belongs to a separate periodic maintenance pass). Default = review table + one approval pop-up. Pass `all` (or `auto` / `yolo` / `save all`) to skip the question and auto-write the provable-safe set, holding sensitive/secret/ambiguous items for a quick interactive pass. Distinct from a handoff brief (one-time, for the next chat) and from periodic memory maintenance (consolidation + backlog drain). User-invocable only.
user-invocable: true
---

# /save-session

User-invokable end-of-session graduation skill. Scans the current conversation, identifies promotable learnings, categorizes them, and writes the keepers into permanent state — the memory files, decisions log, lessons, contexts, and capability inventory that make up your persistent knowledge base.

**Machine config.** Everything specific to ONE person's memory architecture belongs in a small companion config file, not in this method: the memory targets (which files to read and write), the scope-detection keyword table, the per-category output paths, and the sensitivity (surfacing-restricted content) handling. Write that config once for your own setup and keep it beside this skill; the steps below are the universal method that reads it: scan the current chat, categorize, scope-route, dedupe, write, index, summarize.

**If no such config exists yet, the method still runs.** It promotes learnings generically to whatever local memory store the machine has, routes scope from the generic categories below, and exposes NO sensitivity-detection logic (it simply treats nothing as restricted). **Never invent a sensitivity rule the config did not declare** — a guessed rule either leaks what should have been held or holds everything and makes the skill useless.

## Invocation modes

The argument decides the mode:

| You type | Mode | Behavior |
|---|---|---|
| no argument | **Interactive** (default) | Scan → present a table → one `AskUserQuestion` approval → write approved items. |
| `all` (or `auto`, `yolo`, `save all`, `everything`) | **Auto** | Scan → write the **provable-safe set with NO questions** → HOLD the dangerous classes → print a written/held/blocked log. |

Auto mode exists because you usually click "Apply all" without reading, trusting the categorization. So auto mode **does the full pipeline** (scan, categorize, scope-route, dedupe, sensitivity + secret scan) and only skips the *question*. "All" means "stop asking me," not "dump the raw staging file." The items that genuinely need a human (sensitive content per the active config, secrets, ambiguous scope, new files/folders, contradictions) are never silently auto-written — they're held and reported in one line so you can clear them in a 10-second interactive pass when you choose.

## Scope: current chat only (hard rule)

This skill surfaces, tables, asks about, and reports ONLY what was learned in THE CURRENT conversation. Treat other chats as if they do not exist.

- **Never** pull the staging backlog from other sessions into this chat. Never report, summarize, table, or ask about items on different topics or from different memory that did not come up in this conversation.
- The cross-session backlog (everything from other chats) belongs to a SEPARATE periodic maintenance pass and is drained silently in the background. It is never surfaced here. If it needs processing, that is background work with a count-only acknowledgement, not a content dump.
- When folding in staging (Step 1), include only blocks whose `## Session <id>` header matches the **current** session id. All other blocks are out of scope for this skill.
- A bare invocation (no notes) may ask clarifying questions, but only about THIS chat's items — never about other chats' content.
- Writing other-chat items in the background is fine when explicitly asked; **surfacing** their content in this chat is not. Do the work, don't narrate it here.

The rule exists because the alternative is intolerable in practice: a session-capture skill that surfaces other chats' backlog turns a 30-second end-of-session step into a review of work the human has already mentally closed, and they stop running it.

## Different from a handoff brief and from memory maintenance

Three jobs are commonly confused. Keep them apart, whether or not you have a separate tool for each:

| Job | Purpose | Scope | Lifetime |
|---|---|---|---|
| **This skill** | Promote THIS session's learnings to permanent state | Recent / current conversation | Forever — all future sessions benefit |
| **Handoff brief** | Continue THIS thread in a fresh chat | This thread only | Single use |
| **Memory maintenance** | Periodic consolidation + drain the older staged **backlog** | Whole corpus | Ongoing hygiene |

Run this skill BEFORE writing a handoff brief, so permanent state is captured first and the brief only has to carry what is genuinely in-flight. The older staged backlog (everything before today) is **not** this skill's job; the periodic maintenance pass drains it. This skill stays scoped to the current session and today.

## When to invoke

- Before closing a session that touched real project work.
- Before writing a handoff brief (capture permanent state first, then create the brief).
- Periodically during long sessions (every ~100k tokens).
- When something was discovered or decided that's worth keeping but hasn't been saved yet.

User-invocable only. Never auto-invoke.

## Workflow

### Step 1: Pre-scan (silent, no output)

Find out what already exists so the skill doesn't propose duplicates.

1. **Authoritative dedupe via search.** For the session's main topics, query whatever search your memory store exposes (a semantic or hybrid search tool if you have one, otherwise a full-text grep across the corpus). This is the real "does this already exist" check, and it must run over every memory, decision, lesson and context — not just the index files. Prefer it over reading index files by hand: an index lists what someone remembered to index, while a search reads what is actually there.
2. **Read the targets you'll likely write to**, to confirm exact current wording before an APPEND/UPDATE. The exact target files (context files, memory indexes, decisions log, lessons files, capability inventory, project playbooks) are listed in the machine config under "Memory targets". With no config, read whatever local memory store this machine has before writing to it.
3. **Fold in only THIS session's staged candidates** (supplement, not primary source): from the staging file for today, include ONLY blocks under a `## Session <id>` header matching the current session id. Other sessions' blocks are out of scope — leave them for the periodic maintenance drain, never surface them here.

This step is silent. Do not narrate the reads.

#### How staging actually works (so Step 2 reads it right)

- Staging is optional, and only exists if you run a background grader: something that fires when a session ends, queues the transcript, and later grades it into candidate blocks. If you have no such producer, skip staging entirely and read the conversation directly — the method loses nothing essential.
- **If you do build one, throttle it and run it on a cheap model, and never let it call a metered API you are already paying for a plan to avoid.** A per-session grader that bills per call is the single easiest way to turn a free habit into a recurring charge nobody notices for a month.
- Because such a grader is throttled and lagged, **this session's items are usually NOT staged yet** when you run this skill. So the live conversation (Step 2) is the primary input; staging is a supplement of recent un-promoted items.
- Real staging format — parse these blocks (under `## Session <id> — <timestamp>` headers, after a `---`):
  ```
  SCOPE: <one of the active config's scopes>
  TYPE: fact | decision | reference | capability
  TITLE: <short>
  DETAIL: <the fact>
  SUGGESTED_PATH: <target file + section>  ← already computed; use it
  ```
- A grader like this typically stages only those **four TYPEs**, routing lessons and skill-candidates straight to their own files instead. So the staging file will **not** contain behavioral corrections, playbook items, or context updates — scan the conversation directly for those, always.

### Step 2: Scan the session

Scan THIS conversation (the live transcript no background grader has seen yet) for promotable items, and merge in only this session's staging candidates from Step 1 (current session id). Re-judge every candidate through the same gates as a fresh scan — never bulk-import staging, and never reach into other sessions' items.

Categorize each candidate into one of seven types:

| # | Category | What it is |
|---|---|---|
| 1 | **Project fact** | Non-obvious truth about project state, code, content, or operations |
| 2 | **Stack/tooling reference** | Operational detail about how a tool or the stack works in this setup |
| 3 | **Project decision** | A strategic choice between alternatives, with reasoning |
| 4 | **Behavioral correction** | The user corrected Claude's approach, framing, or output |
| 5 | **Playbook update** | A project-specific operational rule for the project playbook |
| 6 | **Context file update** | A fact about org chart, role, tools, ownership, current state |
| 7 | **Capability inventory update** | A new connected tool, API, or service, or a fresh rule about one → the capability-inventory memory |

For each candidate derive: **Category**, **Scope**, **Target file** (absolute path), **Action** (NEW / APPEND / UPDATE), **One-line summary** (concrete, lead with the fact), **Confidence** (0.0–1.0; surface items > 0.5), and **Flags** (sensitive / secret / ambiguous-scope / new-dir / new-file / contradiction — see the gate below).

#### Quality filters (drop a candidate if any are true)

- It already exists (Step-1 search returned a clear match).
- It's ephemera ("I used today's date", "we ran the audit", "ok", "done").
- It re-states a rule already in your always-on rules or a context file.
- It's first-pass content the user hasn't validated.
- It's vague with no anchor noun ("cache stuff is tricky"). Concrete beats vague — every summary must carry a distinctive anchor (project name, tool, path, number).

#### Scope detection

Route each candidate to a scope from the machine config's keyword-to-scope table ("Scope detection"). A tooling/stack detail with no project trigger is `global` with a `reference_` filename prefix; a cross-cutting framework-level item is `global`. If a specific project name is more specific than its scope, put the project in the filename (`project_<project>_*`, not `project_<scope>_*`). With no config, route by these generic buckets alone (project vs tooling vs cross-cutting) and use `global` when a session has no clear project owner.

### Step 3: Categorize + route by mode

**Interactive mode** — output the table BEFORE writing anything:

```
## /save-session — Found N promotable items

| # | Category | Scope | Target file | Action | Summary | Flags |
|---|---|---|---|---|---|---|
| 1 | Project fact | <project> | project_<project>_<topic>.md | NEW | <the concrete fact, leading with the anchor noun> | — |
| 2 | Decision | <scope> | decisions/log.md | APPEND | [date] <choice> over <alternative>, because <reason> | — |
| 3 | Stack/tooling reference | global | reference_<tool>_rate_limit.md | NEW | <tool> caps at N req/min; back off on 429 | — |

## Already covered (skipped)
| Item | Already in |
|---|---|
```

Then fire `AskUserQuestion`:
- `Apply all (Recommended)` — write every non-held item with default categorization
- `Review individually` — walk each candidate (accept / edit / recategorize / skip)
- `Apply selected` — comma-separated row numbers
- `Cancel` — no writes

**Auto mode (`all`)** — skip the pop-up. Split candidates into the **auto-write set** and the **held set** using the gate below, write the auto-write set, then go straight to the Step 5 log. No table, no question.

#### Auto-mode safety gate

Auto-write an item (no question) only when **ALL** are true:
- Not sensitive by the machine config's sensitivity rule. With no config, nothing is sensitive and this clause is a no-op.
- No credential-shaped content (no `sk-`, `Bearer `, `AKIA`, `ghp_`, `xox`, 32+ char hex/base64 blob, or `KEY=value` secret).
- Scope is unambiguous — matches exactly one context's triggers (not zero, not two).
- The target directory already exists (no `mkdir`).
- The fact does not contradict an existing memory (no supersession decision needed).

Everything else is **HELD**: written nowhere, listed in the log with its reason, and left for an interactive run. Specifically always held in auto mode:
- **Sensitive** content (see next section) — the one hard line `all` cannot cross.
- **Secret values** — blocked; you may still save the *fact* that a credential lives at path X (no value) interactively.
- **Ambiguous / multi-context scope** — never guess scope. Keeping contexts from bleeding into each other is a hard rule: a fact filed under the wrong context resurfaces in the wrong conversation later, which is exactly the failure a memory system is supposed to prevent.
- **New directory** required — never `mkdir` unattended.
- **Contradiction** of an existing memory — supersession (`superseded_by:`) is a human decision.

Notes that keep auto mode safe but simple:
- A surgical `UPDATE` (Edit into contexts/*.md or the capabilities table) is allowed in auto mode: the `Edit` tool requires an exact unique match, so a bad edit **fails loudly** rather than corrupting the file. A failed edit becomes a "failed" log line, not silent damage.
- Near-duplicates that slip past the Step-1 search should be caught post-write by a conflict check that compares each new memory against the rest of the corpus and files near-duplicates for the periodic pass. With that backstop in place a borderline write is recoverable rather than permanent noise; without it, tighten the Step-1 search instead of loosening this gate.

### Step 4: Execute (after approval, or for the auto-write set)

Before the first write in auto mode, record the current commit of the memory repository so the whole batch is one revert point: capture the current `HEAD` hash. Put it in the Step-5 log. This assumes the memory corpus is under version control; if it is not, put it under version control before running auto mode at all, because the pre-batch hash IS the rollback path.

For each item:

1. **Build content.**
   - NEW memory: frontmatter (`name`, `description`, `type`) + a **`Recall cues:`** line right after the H1 (mandatory for every `reference_` and `project_` memory — see template). Cues are symptom-phrased aliases, each clause carrying a distinctive anchor noun. This is the dominant retrieval-miss fix; a memory without cues won't be found later.
   - APPEND: a `---` separator + date stamp; for the decisions log and lessons files follow each file's existing entry format. Honour any per-file ordering rule (some files append-**top** rather than bottom; the file's own in-file rule and the active config's sensitivity destinations note which).
   - UPDATE: surgical `Edit` with enough context to match uniquely.
2. **Write the file** (native `Write`/`Edit` only — never via Bash/ctx).
3. **Update indexes (transactional):** a NEW `project_`/`reference_`/`feedback_` memory → one line in the matching per-context index; a global memory → the global index's own section. After writing, re-read the index to confirm the line landed. If the index update fails, delete the orphan memory file and log the item as failed — no unrouted memories. The transaction matters: an indexed memory that does not exist and an existing memory nothing indexes are both silent failures, and the second one is worse because it looks like success.
4. **Smoke check each write:** valid frontmatter, size > 0, no duplicate append line.

**Do NOT manually re-index if your setup re-indexes itself.** Where a file-write hook already re-embeds the corpus, runs the conflict check, and rebuilds any derived artefacts, adding a manual re-index step on top is redundant at best and racy at worst: two indexers over one corpus is the same one-mutator-per-resource problem as anywhere else. Confirm once whether your store re-indexes on write, record the answer in the machine config, and follow it.

**No scattered `.bak` files.** When the memory directory is version-controlled, every write is already revertable and that IS the rollback path. Do not litter an INDEXED corpus with `.bak-YYYYMMDD` files: unlike a normal backup, these get embedded and searched alongside the real memories, so each one becomes a permanent near-duplicate that pollutes every future retrieval. To undo a batch, check the affected files out at the recorded pre-batch hash.

### Step 5: Summary + log

Print, and in auto mode also append one run record to a persistent run log (a single append-only file, path recorded in the machine config):

```
## Saved — <timestamp> — mode: auto | interactive
- Version-control HEAD before batch: <hash>   (revert: check the listed files out at <hash>)
- Written: N across M files  [list paths]
- Held: K  [each with reason: SENSITIVE / SECRET / AMBIGUOUS-SCOPE / NEW-DIR / CONTRADICTION]
- Blocked: J  [credential-shaped, etc.]
- Index updates: [which index files were touched]
- Verification: frontmatter valid ✓ · indexes synced ✓ · recall cues present on new memories ✓
```

Surface held/blocked **prominently** — that's the high-signal part:
> Wrote 8. Held 3 (2 sensitive items, 1 ambiguous scope). Blocked 1 (credential-shaped). Re-run interactively to clear the 3 held.

Then, interactive mode only, fire `AskUserQuestion`:
- `Write the handoff brief now` — chain into the handoff brief, if the human uses one
- `Done — close session` — exit
- `Save more` — re-run

Auto mode just exits with the summary (re-invoke for the handoff brief if wanted).

## Sensitive content handling (the one line `all` never crosses)

Some memory corpora carry surfacing-restricted content: memories special-cased across the stack with a `sensitive: true` marker, excluded from whatever ambient injection feeds context into unrelated prompts, given **no synthesis or summary page**, and surfaced only on their own explicit topic. Getting this wrong leaks restricted personal information into unrelated work prompts on the next re-index, so it is the one line auto (`all`) mode never crosses.

**The machine config owns the detection and the destinations.** It declares: which items count as sensitive (the detection signal and token set), where each sensitive class is APPENDED (never widened), the marker requirements, and the "never synthesize / never widen recall / never alias" firewall rules. Keeping the detection OUT of this method is deliberate: what counts as sensitive is specific to one person's life and cannot be guessed from a generic list. This skill enforces the mechanics uniformly:

1. **Detect** per the machine config's sensitivity rule. When unsure, **treat as sensitive**. The asymmetry is the whole argument: over-flagging costs one confirmation, under-flagging leaks restricted personal information into unrelated prompts and cannot be un-leaked.
2. **Route** to the config's existing destination for that class; prefer APPEND, never create a new sensitive surface without the config's say-so.
3. **Marker:** apply the config's marker requirement, typically `sensitive: true` at the **TOP LEVEL** of the frontmatter, with the surfacing clause the config specifies. Top-level matters more than it looks: a filter that reads only top-level keys treats a nested marker as absent, so a nested `sensitive: true` reads as correctly-marked to a human and as unrestricted to the machine.
4. **Never** create or update a synthesis / summary page for a sensitive area, add a sensitive file to such a page's sources list, link it from a shared page, or add its aliases to any entity or alias table. Each of those is a different route by which restricted content reaches a surface that was never meant to carry it.
5. **Post-write verification:** after any sensitive write, confirm the marker is present AT TOP LEVEL by re-reading the written file. If it is missing or nested, treat the write as failed and roll it back rather than fixing it forward.
6. **Auto-mode rule:** in `all` mode, **hold every sensitive item** — do not auto-write. (Rationale: the high-risk classes are exactly the un-auto-judgeable ones. The recovery cost of a leak dwarfs one confirmation.) Even a defensible pure APPEND to an existing sensitive file is **still held by default**; clear it in the interactive pass.

**With no config present, there is no sensitive class:** the skill exposes no detection logic, treats nothing as restricted, and promotes every gate-passing item normally. Never invent a sensitivity rule the machine config did not declare.

## Memory frontmatter + recall cues template

For NEW `project_`, `reference_`, `feedback_` files:

```markdown
---
name: {memory name}
description: {one-line — used to decide relevance in future conversations}
type: {project | reference | feedback | user}    # summary/synthesis pages belong to the periodic maintenance pass, not this skill
---

# {H1 title}
Recall cues: {2–3 symptom-phrased ways you'd later ask for this, each with a distinctive anchor noun — e.g. "docker build ARG not expanding", "vercel preview 401 bypass"}

{memory content body}
```

## Output file targets (reference)

The per-category destination paths live in the machine config under "Output file targets". The category-to-action shape below is universal:

| Category | Action | Destination |
|---|---|---|
| Project fact | NEW | a `project_{scope_or_project}_{topic}.md` memory |
| Stack/tooling reference | NEW | a `reference_{scope_or_project}_{topic}.md` memory |
| Project decision | APPEND | the decisions log |
| Behavioral correction | APPEND | the scope's lessons file |
| Playbook update | APPEND | the active project's playbook |
| Context file update | UPDATE SECTION | the scope's context file |
| Capability inventory | UPDATE TABLE | the capability inventory memory |

With no config, write to the equivalent files in whatever local memory store the machine has, using the same category → action mapping.

## Quality bar

- **Concrete beats vague.** "Cache flush order: CDN first, then origin host" beats "cache stuff is tricky", and naming the two actual systems in your own stack beats both.
- **Lead with the fact.** Table summaries are scanned; the first 60 chars matter.
- **Make it findable.** Every new memory carries recall cues, or it won't surface later.
- **Don't duplicate.** The Step-1 search and the post-write conflict check both catch repeats.
- **Save what would stop the next chat re-asking.** That's the success metric.

## Edge cases

- **Zero promotable items** → "Found 0 worth saving. Session was ephemeral or already covered. Skip /save-session."
- **A new fact replaces an old memory** → don't delete the old one; mark its frontmatter `superseded_by: <new-slug>` (optionally `valid_until: YYYY-MM-DD`). The temporal layer re-derives this on rebuild. In auto mode this is a HOLD (human decides supersession).
- **Two new findings contradict each other** → present both with a CONFLICT tag (interactive); hold both (auto).
- **Hub-entity fact lands** (any recurring project or entity your store builds a summary page for) → that summary page may now be stale. Note it and move on; regenerating summary pages belongs to the periodic maintenance pass. This skill writes the atomic memory only.
- **Target dir doesn't exist** → interactive: `AskUserQuestion` before `mkdir`. Auto: HOLD (never `mkdir` unattended).
- **Item trips a house writing-style rule** (a banned word, a banned phrasing) → still save it. Memory, decisions and lessons files record what happened in the words it happened in; a style filter over them distorts the record, so exempt those paths from any style enforcement you run.
- **Credential value appears** → never save the value. Save only the fact that the credential exists at path X. Auto: blocked.
- **Big target file (>500 lines)** → still append; flag for splitting in the next maintenance pass.

## Why the method and the machine config are separate

This file is deliberately a universal promote-learnings METHOD: no account, no project name, no file path, and no sensitivity rule hardcoded. Everything specific to one machine's memory architecture lives in a companion config: the exact target paths, the scope-detection keyword table, the per-category destinations, and the sensitivity handling.

The split is not tidiness. A capture skill with someone's real memory architecture welded into it cannot be shared, cannot be moved to a second machine, and cannot be reviewed by anyone without handing over the shape of their private corpus. Keeping the method portable and the architecture local means the method can be improved in the open while the corpus it writes to stays entirely private.

## Safety

- All writes are local and reversible through version control; auto mode records the pre-batch HEAD so a whole batch is one revert.
- Interactive mode requires `AskUserQuestion` approval before any write.
- Auto mode writes only the gate-passing safe set; sensitive/secret/ambiguous/new-dir/contradiction items are held, never silently written.
- A persistent run log records every written, held, and blocked item, so even a silent auto-mode batch leaves an auditable trail. This is what makes auto mode defensible: the human can reconstruct exactly what was written without their approval, after the fact.

## Pairing

```
this skill          →  this session's learnings captured (recent / today)
handoff brief       →  one-time brief for the next chat
memory maintenance  →  periodic consolidation + drains the older staged backlog
```

Run the periodic maintenance pass on a schedule rather than on impulse, and let it own consolidation, conflicts, supersession, summary-page refresh, and the backlog drain. Keeping those OUT of this skill is what lets this one stay fast enough to actually run at the end of every session, which is the only way any of it gets captured at all.
