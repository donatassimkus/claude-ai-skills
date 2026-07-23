---
name: ui-ux-audit
argument-hint: [project or path/URL] [: extra angles for this run] [--quick | --fix]
description: "AUDIT: does the full user-facing experience behave coherently and match what was agreed? The runnable cross-surface audit for any project, website, app, portal, or tool. Inventories every surface (pages, forms, flows, PDFs, emails, notifications, signing/checkout pages, admin views, in-app guides), traces every field from input through storage and sync to every output, diffs the same facts across surfaces, checks behaviour against the agreed business model, then applies experience lenses (friction, copy drift, error and empty states). Read-only: produces a lens board, numbered findings with severity, a business-side checklist, and one approval popup; fixes run separately after approval under a safe live-write procedure. Loads usability heuristics as its knowledge lens; per-project specifics load from config. Invoke when the user says 'audit this project / app / site', 'do a UI/UX audit', 'scan for contradictions or redundancy', 'check the whole flow', 'anything wrong or duplicating before the demo', 'run the audit with these angles', or reports two surfaces disagreeing (a PDF vs an email, a form vs the CRM). Skip for: technical ship-safety QA, search performance, style-only text checks, blog-pipeline verification, and design generation or deep design judgment."
---

# UI/UX audit

One question: does everything a user sees and experiences behave coherently, and does it match what was agreed? "User" means every audience: customer, end user, staff member, signer, admin. Surfaces include documents and emails the system sends, not just screens.

This skill is the runnable PROCEDURE. A usability-knowledge layer (heuristics, cognitive load, error-state doctrine) is a separate discipline, loaded in phase 5 as a lens: if you have such a reference available, pull it in there. Project context loads from the active CLAUDE.md; per-project audit specifics load from a per-project config file (see Config contract).

## Invocation and modes

| Form | Behaviour |
|---|---|
| `/ui-ux-audit` | Resolve the project from the active context; if ambiguous, ask (never guess a context). |
| `/ui-ux-audit <project or path or URL>` | Explicit target. |
| `/ui-ux-audit <target>: <free text>` | Everything after the colon becomes ADDITIONAL lenses for this run. Foundations always run; the message only adds angles, never replaces phases. |
| `--quick` | Phases 0, 1, 3 on the highest-traffic surfaces, plus the lens board. No deep field trace. For a fast pre-demo pulse. |
| `--fix` | Execute a previously approved findings bundle. Never combined with the audit pass itself. |

Access tiers decide depth, and the report must say which tier ran:
- **Code access** (repo, mount, or SSH): full method, phases 0 to 7.
- **URL only**: surface inventory by crawling and clicking, cross-surface diff on what is reachable, lenses. No field trace, no storage or sync checks. Say so in the report.

## Hard rules (learned the hard way)

1. **One pass, hard core included.** Capture ground truth and validate against it in THIS run. Never ship "surface audit now, spec check later".
2. **Re-verify before reporting.** Every candidate finding gets re-checked against live state before it reaches the report. No findings from stale reads or old tracker entries.
3. **Honest coverage.** State what was NOT checked and why. A degraded run says it is degraded. Never imply full coverage.
4. **Read-only until approved.** The audit changes nothing. Fixes are a separate approved batch run under a safe live-write procedure: risk tag each change, back up what you touch, smoke test after, capture and actually LOOK AT a screenshot for anything visual, and append to a changelog.
5. **Suppress accepted caveats.** Decisions already made and recorded are not findings. Report only their count ("3 accepted caveats skipped").

## Phase 0: ground truth

Load, in order: the project's config block, changelog, findings tracker, decisions log entries, call transcripts or agreed-model notes named in config. This is what upgrades the audit from "is it consistent" to "is it what we agreed".

If no ground truth exists: announce "no ground truth found for [target]; running a consistency-only audit" and continue. Never pretend to validate a model you do not have.

## Phase 1: surface inventory

Enumerate every user-facing surface and the data layer behind it:
- Screens: pages, forms, multi-step flows, review steps, dashboards, admin views.
- Sent artifacts: PDFs, emails, notifications, invoices, receipts, exports.
- Handoff surfaces: signing pages, checkout, confirmation screens, magic links.
- Ambient copy: in-app guides, help text, empty states, error states, tooltips.
- Data layer: schema, sync targets (CRM, billing, analytics), background jobs that write user-visible state.

With code access, find them at the source: routes, page components, template renderers, email senders, document generators. With URL access, crawl and walk the visible paths. Output: a surface map used by every later phase.

## Phase 2: field-flow trace (code access only)

For each field: input, validation, storage, sync, then EVERY output surface. Failure classes to hunt by name:
- Hidden fields that receive values (from prefill or defaults) the user can never see or edit.
- Double typing: the same value entered twice in one flow.
- Dead paths: stored but never rendered anywhere, or rendered from a source nothing writes.
- Duplicate display: one fact printed twice on one surface under two labels.
- Validation asymmetry: client requires what the server does not, or the reverse.
- Defaults that lie: a hidden default that renders as a positive claim on an output.

## Phase 3: cross-surface diff

The same fact must be identical everywhere it appears: numbers, counters, statuses, scope lists, payment details, names, dates, terms wording. Then two more diffs:
- Copy vs behaviour: guides, tooltips, and helper text describing features that changed or no longer exist.
- Decision propagation: every recorded decision checked against EVERY surface it touches. The classic miss is fixing the document and forgetting the email that mirrors it.

## Phase 4: model vs reality

Does behaviour match the agreed business model from phase 0? Includes semantic truthfulness of outputs: a generated document must never assert a state the input never asserted (a ticked box for a check nobody performed, a "sent" that failed, an "included" that is not in the plan).

## Phase 5: experience lenses

- Load the usability lens: heuristics, cognitive load, feedback, error and empty and loading states, affordances.
- Apply your writing and style rules to user-facing copy in scope.
- Load a conversion lens only when a conversion surface (landing, pricing, signup, checkout) is in scope.
- Apply the config's standing angles (brand rules, language variant, naming constraints).
- Apply this run's extra angles from the invocation message.
Friction hunt: re-entry of known data, dead ends, missing feedback after actions, unclear labels, steps out of order relative to how the work actually happens.

## Phase 6: re-verify and rank

Re-check each candidate against the live system or current code. Then rank:
- **Critical**: a user-visible wrong fact, a compliance or legal assertion that is untrue, money or data loss.
- **High**: breaks trust or blocks a flow (a contract missing its scope, a broken handoff).
- **Medium**: inconsistency or friction a user will notice.
- **Low**: polish.
Drop anything that does not reproduce.

## Phase 7: report (locked format)

Same shape every run, readable in 60 seconds:

1. **Verdict line** first: ship-ready or not, and the single biggest risk.
2. **Lens board** table: `Lens | State | One-liner` for Fields and data flow, Cross-surface consistency, Agreed model, Copy and guides, Friction, Out-of-lane handoffs. State glyphs: ✓ ok, ! issues, ✗ broken.
3. **Numbered findings** (hierarchical 1.1 style), each with severity, what a user experiences in plain language, where it lives, and a one-line fix outline. No walls of text.
4. **Only you can check**: business-side items the code cannot answer (billing accounts, third-party settings, pending stakeholder decisions).
5. **Suggested final scan**: the short pre-ship or pre-demo checklist for this project's current state.
6. **One approval popup** with fix bundles grouped by severity, plus a "report only, no changes" option. Never auto-fix. Verdict popups stay neutral (no Recommended tag) and always include a stop option.

Update the project's findings tracker as part of the run: new findings added, fixed items closed, false positives marked.

## Fix mode (after approval only)

Runs as a normal live-writes batch: risk tag, backups, the project's baseline checks from config (for example a known typecheck error count), smoke test, a viewed screenshot for anything visual, changelog append, then the verdict popup. Re-run the affected phases on the touched surfaces, not the whole audit.

## Config contract

Keep per-project audit specifics in a config file beside this skill, one file per context and one block per project inside it. Each block may define:
- Surfaces list and entry points (seeds phase 1; the skeleton still sweeps for surfaces the list forgot).
- Ground-truth pointers: changelog, findings tracker, decisions, transcripts or agreed-model notes.
- Baselines: known error counts, where checks must run, verify recipe pointers.
- Accepted caveats: recorded decisions the audit must not re-flag.
- Standing angles: brand rules, language variant, naming constraints, forbidden content.
No config for the target: run the skeleton alone and say so. Runtime state (caches, last-run data) never lives in config.

## What this skill does NOT cover

- Technical ship-safety QA (broken links, overflow, meta, redirects, launch assets).
- Search performance and rankings.
- Style-only text review with no product in scope.
- Verification of an automated content or blog publishing pipeline.
- Design direction, composition, or generation, and deep usability doctrine.
- Code-diff correctness review: code review tooling.
Name these as handoffs in the lens board when they surface, do not absorb them.
