# Skill config contract

The convention for splitting a skill into a universal SKELETON plus context-specific CONFIG. This is the single source of truth: the skill scaffolder builds to it, and every skill that carries context-specific behaviour follows it. The always-on loading behaviour lives in `config-loading-rule.md`; this doc is the full reference.

## Why
A skill welded to one account is not portable, leaks personal data anywhere the skill is copied or synced, and forces a fork per new context. Splitting the method (skeleton) from the context (config) makes the skeleton reusable, work-safe, and scalable: a new project or account becomes a config drop-in, not a new skill.

## The four homes
1. **Skeleton** = `skills/<skill>/SKILL.md` + `scripts/`. The method. Universal, work-safe, no account or personal data, no hardcoded context.
2. **Skill config** = `skills/<skill>/config/<ctx>/` (or `config/<ctx>.md`). Context-specific facts, rules, optional code. Per-skill, per-context.
3. **Shared context** = `contexts/<ctx>.md`. Facts many skills need (org, brand voice, ICP). Config REFERENCES it; it does not duplicate it.
4. **State** = runtime data (ledgers, checkpoints, caches). Local, never synced. Lives OUTSIDE config, in a runtime directory beside your skills rather than inside the skill folder. It is rebuilt locally on any machine that needs it, never carried between machines.

## Config vs state (the line)
- **Config:** portable, declarative, per-context, changes rarely, safe to sync by context. Inbox address, VIP list, brand colours, project list, triage rules, voice.
- **State:** per-run, mutates every execution, machine-local, never synced. Processed UIDs, learned routing map, awaiting ledger, caches.
- Test if unsure: would you hand this to another machine as-is? Config yes, state no.

## Config folder layout
```
skills/<skill>/config/
  <ctx>.md                # simple: rules + facts as markdown
  <ctx>/                  # rich: when code or data is needed
    rules.md              # the context-specific instructions the skeleton reads
    run.py                # OPTIONAL: context-specific logic the skeleton calls
    data.json             # OPTIONAL: lookup tables, mappings
```
Context names (`<ctx>`) are your own: one per account, client, brand, or project you operate in (`acme`, `client-b`, `personal`, `work-gmail`, and so on). Pick them once and match the vocabulary you already use elsewhere in your setup, so the same context name means the same thing in every skill.

## Extension points (the contract between skeleton and config)
A skeleton declares what it consumes from the active config:
- **Reads:** `config/<ctx>.md` or `config/<ctx>/rules.md`, always, if present.
- **Calls (optional):** `config/<ctx>/run.py`, only where the skeleton defines a hook for it.
- Anything the skeleton needs that varies by context comes THROUGH the config, never hardcoded in SKILL.md.

## Context resolution
1. Explicit arg: `/<skill> <ctx>` sets the context explicitly.
2. Else inferred: the session's active context (CLAUDE.md context router).
3. Else skeleton-only: no config, run the universal method. Never error on a missing config.

## Loading
Any skill invocation auto-loads its config for the resolved context if present. This is a global always-on rule (`config-loading-rule.md`), so a config dropped into ANY skill folder works with no skill edit. That rule holds the exact behaviour.

## Shared context reference
When several skills need the same fact (one context's brand voice, its ICP), it lives once in `contexts/<ctx>.md` and configs point to it. Duplicate into a skill config only when the fact is truly skill-specific. Lift a duplicated fact up to the shared context on the SECOND skill that needs it, not before.

## Secrets
Config code (`run.py` and similar) sources credentials from your own secret store, read by variable name at runtime. Never inline a secret in a config file, and never commit one.

## Sync boundary
If you run this setup on more than one machine, the boundary falls out of the three homes above. The skeleton is safe to carry everywhere, because it holds no context. Config filters by context: a given machine receives only the contexts that belong on it, and the rest stay home. State never crosses at all. Automate that filter rather than applying it by hand, have it content-scan config code for tokens and secrets, and make an unrecognised config HELD rather than passed: fail-safe, so a new config never crosses a boundary just because nobody had classified it yet.

## Non-breaking rule
Splitting a skill must not change its behaviour when the config is present. Prove it: snapshot the skill, build the split, A/B the split against the snapshot on real tasks, ship only if equal or better. A missing config degrades cleanly to the skeleton, never to a broken half-output.

## For the skill scaffolder
New skills scaffold with SKILL.md (skeleton) + `config/` (empty, ready) + a pointer to this contract. If the skill has context-specific behaviour at birth, create `config/<ctx>/` per known context. Never inline a project list, brand kit, or account detail into SKILL.md.
