# Contributing

A growing library of copy-paste AI skills. Here is the shape, so a new skill drops in cleanly.

## Repo layout

```
skills/
  <skill-slug>/
    INSTALL-PROMPT.md   # required: the paste-able runbook a user copies into their AI
    SKILL.md            # the method the AI installs (knowledge skills)
    references/         # optional: on-demand files a knowledge skill loads per task
    README.md           # short readme for the folder
```

## Adding a skill

1. Create `skills/<slug>/` with at least an `INSTALL-PROMPT.md` (the runbook a user pastes).
2. For a knowledge skill, add `SKILL.md`, and a `references/` folder if the method is large enough to split into on-demand parts.
3. Add a short `README.md` in the folder: the skill name, its type, what it does, and how to install it.
4. Add a row to the catalog table in the root [README](README.md), under the right category.

## What belongs here

Skills that are self-contained and safe to share: a stranger pastes the prompt and it works on their own machine and accounts. No secrets, no private paths, no account tokens. The reader always supplies their own.
