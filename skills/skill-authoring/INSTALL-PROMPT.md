# Skill-authoring conventions: install directive (for the AI receiving this folder)

You, the AI reading this, have received a set of skill-authoring conventions as 3 files: `skill-config-contract.md` (the skeleton/config/state split, in full), `master-skill-rules.md` (what may never be hardcoded into a reusable skill, and how to verify it), and `config-loading-rule.md` (the always-on rule that loads the right config at invocation time). They are ready to install AS-IS. Your job is to install them unchanged, wire them into whatever skill-creation tooling this environment already has, calibrate them to the human's own contexts, and prove them on a real skill. You do not rewrite, summarize, or restructure the files.

These conventions are an OVERLAY. They do not replace a skill scaffolder and they do not ship one. They govern the SHAPE of every skill that gets built here, whoever builds it.

**As your FIRST action, tell the human in chat, in one or two lines:** you are installing a set of conventions for how reusable skills should be structured (a universal method separated from per-context config, with runtime state kept out of both), that you will apply whenever they create or edit a skill; nothing is needed beyond writing three files, no accounts or keys; about a minute plus one question. Ask them to confirm before you proceed. Do not start until they say go.

## Install the files unchanged

1. Detect where this environment keeps reusable skills or instructions. If it supports a folder per skill (a skills directory), create ONE folder named `skill-authoring` and write all three files into it at the folder root, preserving their names.
2. If this environment can hold only a single instruction blob, concatenate them in this order into one document: `config-loading-rule.md`, then `skill-config-contract.md`, then `master-skill-rules.md`. The loading rule goes first because it is the part that must be live at every invocation; the other two are consulted when a skill is being written.
3. **`config-loading-rule.md` wants to be ALWAYS-ON, the other two load on demand.** If this environment distinguishes between instructions that are always in context and instructions loaded when a task calls for them, put the loading rule in the always-on tier and the other two in the on-demand tier. That split is the whole point: config resolution has to happen on EVERY skill invocation, whereas the contract and the genericity rules only matter while authoring. If the environment has no such distinction, load all three together and say so.
4. If a skill or file named `skill-authoring` already exists here, do NOT overwrite it. Back it up beside itself first, then ask the human whether to replace it.
5. If this environment already carries comparable skill-structure conventions, STOP and reconcile with the human: extend the existing set, replace it, or keep both under clearly distinct names. Two conventions both claiming to define where config lives will send skills to two different places, and the resulting split is worse than either convention alone.
6. Write nothing anywhere else.

## Integrate with the skill scaffolder that is already here

These conventions are designed to sit UNDER a skill-creation tool, not beside it. Do this after installing:

1. **Detect what this environment uses to create skills.** Several AI coding environments ship or offer a first-party skill-creation tool that interviews the human, scaffolds the folder, writes the frontmatter, and sometimes runs evals: Claude Code publishes one called `skill-creator`, and other agentic environments have their equivalent under their own name. Check the installed skills, plugins, and marketplace for whichever applies here. Use whatever you find; do not assume the environment has none just because the name differs.
2. **If a skill scaffolder IS present**, wire these conventions into it rather than duplicating it. Concretely: whenever that tool scaffolds a new skill, the folder it produces must satisfy `skill-config-contract.md` (a `config/` directory created empty and ready alongside `scripts/`, `references/`, and `assets/`; no context-specific value written into `SKILL.md`), and whatever it produces must pass the verification scan in `master-skill-rules.md` before it is called done. Tell the human in one line that the two are now working together and which one owns which decision: the scaffolder owns the interview, the frontmatter, and the eval loop; these conventions own where context-specific values are allowed to live.
3. **If NO skill scaffolder is present**, say so plainly and tell the human that a first-party one may be available for this environment and is worth installing separately, from whoever publishes this environment. Do NOT attempt to reproduce a skill scaffolder yourself, and do not treat these three files as one. They are conventions about structure, and they are fully useful without any scaffolding tool: you apply them by hand when you write a skill.
4. Either way, these conventions apply to every skill created here from now on, including ones the human writes by hand and ones they already have.

## Calibrate (one question)

Ask the human ONE question via your interactive question UI, and persist the answer next to the files:

> "Which contexts do you operate in? Name each account, client, brand, employer, or project you would want a skill to behave differently for. (For example: one per client you serve, one per brand you run, one for your employer, one for personal.)"

This single answer fills two slots the files deliberately leave empty. First, it becomes their `<ctx>` vocabulary: the context names in `skill-config-contract.md` are theirs to choose, and picking them once means the same context name means the same thing in every skill they ever write. Second, it seeds the verification scan in `master-skill-rules.md`: the pattern in that file is a template precisely because the names it must catch are the human's own, and their answer here is most of that list already. Build the scan pattern from their answer, add their currency symbol and any regulator or jurisdiction they cite regularly, and store it where you can reuse it on every future skill.

The calibration is re-runnable, and it needs re-running more often than most: offer to re-run it whenever they take on a new client, brand, or employer, since a name that is not in the scan pattern is a name the scan cannot catch.

## Standing behavior

- Apply these conventions unprompted whenever the human creates, edits, splits, or reviews a skill, and say in one line that you are doing so.
- **Enforce the never-hardcode rule at write time, not at review time.** The moment you are about to write a project name, client name, person, currency symbol, jurisdiction, or personal constraint into a skill's method, stop and put it in that skill's config instead. Catching it later means the skill was already wrong.
- **Run the verification scan before calling any skill done**, using the pattern built at calibration. A skill that has never been scanned is not verified. Report the result rather than assuming it passed.
- **Hold the config-versus-state line.** Anything that mutates on every run (ledgers, caches, processed IDs, learned maps) is state, never config, and belongs outside the skill folder entirely. The test in the contract is the one to use: would you hand this to another machine as-is?
- **Never inline a secret in a config file**, and never write one into a skill. Config code reads credentials from the human's own secret store by variable name at runtime.
- **When splitting an EXISTING skill, treat the non-breaking rule as a hard gate.** Snapshot the skill first, build the split, A/B the split against the snapshot on real tasks, and ship only if the result is equal or better. A refactor that silently degrades a working skill is the main risk this whole convention introduces, and the A/B is what contains it.
- A missing config degrades to the skeleton alone. Never error on a missing config, and never half-apply one.

## Prove it, then hand over

After installing, integrating, and calibrating, ask the human for ONE real skill of theirs: either a new one they want to build, or an existing one that has context-specific values baked into it. Apply the conventions to it end to end.

For a NEW skill, scaffold it to the contract and show them the resulting shape: what went in the skeleton, what went in `config/<ctx>/`, what would be state, and the verification scan coming back clean.

For an EXISTING skill, do the more useful thing: run the verification scan on it first and show them exactly which hardcoded values it catches, then propose the split (what moves to config, what stays), and name the A/B you would run before shipping it. Do not perform the split in the same breath as proposing it unless they ask you to.

Then confirm your own work in one line: the three files landed unchanged in the right place, the loading rule is in the always-on tier if this environment has one, nothing existing was overwritten, and whether you found a skill scaffolder to integrate with.

Close by telling the human: how these conventions will fire from now on, which skill-creation tool they are working alongside (or that none was found), how to re-run the calibration when they add a context, where the verification pattern is stored so they can extend it, and how to remove the conventions (delete the one `skill-authoring` folder or section you created; name its exact location).
