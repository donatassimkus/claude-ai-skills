# Publish gate checklist template (Phase 11)

Print this checklist at ship time, following the evidence rules in SKILL.md Phase 11: paste the actual commands and their real output, never a bare "PASS"; the registry must show N > 0 entries scanned or the gate FAILS; never claim a mechanism present when the grep does not find it. In KNOWLEDGE mode, build-shaped lines record their collapsed knowledge analogs (persist-safely on the build-safety line, proof-of-absorption on the go-live line), never a false "n/a".

```
PUBLISH GATE
- Registry: loaded, N entries scanned  (N must be > 0, else FAIL)
- Leak gate: 4/4 PASS
  - pass 1 registry-name scan:   <command run>  → <output: 0 hits>
  - pass 2 default-deny scan:    <command run>  → <output: 0 suspected>
  - pass 3 semantic review:      <reviewer note: no who/what tells; no human-facing prose; knowledge: third-party-IP check ran>
  - pass 4 secret-scan (Tier 0): <command run>  → <output: 0 secret-shaped hits>
- _README diff scanned (default-deny + secret, as the gate defines): <command run> → <output: 0 hits>
- Catalog-card stub written + scanned (default-deny + secret): yes
- Voice-quality scan: <clean | N hits rephrased | no operator scan configured>
- AI-runbook voice confirmed: no human-facing pitch / preamble / "tell your agent" note, no internal-meta / provenance block, no audience label in the body (pass-3 confirmed)
- CORE/SHELL split applied: CORE reproduced faithfully | SHELL recast as host-mapped responsibilities
- Output size: <LEAN (one-file/one-step) | FULL (multi-script / multi-dependency / hard-guarantee)>
- Output type: <AGENT (build + run) | KNOWLEDGE (absorb + apply; build-shaped gate lines record their collapsed knowledge analogs; third-party-IP check ran)>
- Deliverable form: <single paste | kit (N parts; ingestion-order + part-count directive present; every part gate-scanned)>
- Knowledge only — diff-fidelity audit: <N changed lines of M source lines, per-file counts pasted; changes = intended redactions only>
- Knowledge only — residual-target sweep: <command> → 0 | isolation check (no external skill / rig / excluded-file refs): <command> → 0
- Final per-file sweep (after the LAST write; every shipped file × all scan classes): <N files, per-file table pasted, all 0 | judged exceptions named>. Invalid if any file was edited after the sweep.
- No internal meta in shipped body: no provenance / version / generator / date / audience-label block anywhere; capability is named only in-band by the interactive OPEN (grep-confirmed): yes
- Manifest sidecar written (_manifests/<slug>.json, operator-side, NOT shipped): yes
- Interactive OPEN present (AI's first action: brief human on what/needs/effort + ask to proceed): yes
- Host-detection STEP 0 present (detect-first, ask-to-disambiguate): yes
- Build-safety contract present (manifest+go/no-go, no-clobber, never overwrite secrets file, uninstall-on-ask): yes
- Extend-don't-duplicate rule present (one mutator per resource): yes
- Dependency onboarding present: detect → ASK-when-undetectable → SUGGEST-connectable-options → GUIDE-the-connection, plus per-dependency recovery (AI relays fix interactively) and minimum-viable-path first move: yes
- Re-tune entry point present (AI offers to re-run interactively; diff-style re-run; no human-facing note): yes
- Prompt-injection guard present: <yes | n/a — ingests no third-party content>
- Go-live present: AI self-verifies (working-state + placeholder sweep + one self-check per guarantee — AI-run, not a human test) AND a usage handoff (run / schedule / undo / correct) closes the runbook: <yes — grep-confirmed>
- Capability type: <skill | tool | hook | script | automation | workflow | process | config | prompt>
- Audience applied: <public-safe default | named: [audience]>  (Tier 0 + Tier A stripped: yes)
- NET-NEW additions: <none | labeled list>
- Widen test run on EVERY named tool: <N named · W widened to equivalents · I kept as structurally inherent, each named with what it stands in for · X silent-wrong-answer sites (a named tool's format/path/API the capability READS) found and fixed>. Counts or it did not run: a bare "yes" is invalid here. In KNOWLEDGE mode widenings are additive edits recorded in the manifest as their own change class, separate from redactions.
- Dependencies tiered: <required-core | required-for-feature | optional, each listed>
- Machine-readable dependency list + optional-feature choice directive: <yes — grep-confirmed | one-line collapse (single dependency)>
- Index row: <projection of manifest — capability / output type / version / last-generated / source-status>
- Ship report block printed first: one SHARE THIS deliverable rendered as a CLICKABLE markdown link (NOT a fenced/bare path) + every internal path a clickable link purpose-labeled with never-share markers: yes
- Output: <path>  (manifest: _manifests/<slug>.json; card stub: _manifests/<slug>.card.md)
```
