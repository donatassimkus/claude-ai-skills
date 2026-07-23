# Skill config loading

Skills split into a universal SKELETON (`skills/<skill>/SKILL.md`) and context-specific CONFIG (`skills/<skill>/config/<ctx>`). On any skill invocation:

1. Resolve context: explicit arg (`/skill <ctx>`) > the session's active context (however your setup infers it) > none.
2. If `skills/<skill>/config/<ctx>/` or `config/<ctx>.md` exists, load it and apply it on top of the skeleton. Read `config/<ctx>/rules.md`; if the skeleton defines a hook and `config/<ctx>/run.py` exists, use it.
3. If there is no config for the resolved context, run the skeleton alone. Never error on a missing config, never half-apply one.

Runtime STATE (ledgers, caches, processed-IDs) is not config: it lives outside `config/`, in a runtime directory beside your skills, and is never loaded as context. Full contract: `skill-config-contract.md`.
