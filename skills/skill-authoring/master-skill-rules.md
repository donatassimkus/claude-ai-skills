# Master skills rules

Master skills in your skills directory must be fully generic. They run against any industry, product, geography, or business without modification. Project-specific detail lives in your shared context files, not in the skill.

## Never put in a master skill
- Hardcoded project, business, or person names. Every one of your own brands, clients, and colleagues belongs in a context file, never in the method.
- Industry defaults presented as universal (whichever vertical you happen to work in most).
- Currency symbols as defaults: use `[currency symbol]` or neutral language.
- Geography-specific content as defaults (one country's phone formats, tax authority, employment law, or directory sites).
- Specific tool assumptions (whichever CRM or automation platform you personally use, written in as the default).
- Personal constraints (your own weekly hours, budget ceiling, or capacity limits).

## Acceptable patterns
- Examples labelled as one option among many ("if in [country]: [the two directories that matter there]").
- Conditional platform sections ("If using [CRM]:").
- Generic placeholders: `[service]`, `[product]`, `[currency symbol]`, `[result]`, `[your CRM]`.
- The line "Project context is loaded from the active CLAUDE.md".

## Verification
After any skill update, run before marking done. Build the pattern once from YOUR OWN specifics (every brand, client, employer, and person you work with, plus your currency symbol and any regulator you cite), keep it in one place, and reuse it on every skill:
```
grep -iE "<brand-1>|<brand-2>|<employer>|<person>|<currency>[0-9]|<regulator>" <skills-dir>/[skill-name]/SKILL.md
```
Zero results for hardcoded specifics. A skill that has never been scanned is not verified, and the list is worth extending the moment a new name enters your world: one edit there protects every skill you will ever write.
