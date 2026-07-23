---
name: web-design
description: "Design or review marketing/product website layouts at a senior level. GENERATE mode locks an aesthetic direction from a reference first (fonts, colour, depth, motion), then composition, then component hygiene, so new pages come out distinctive instead of generic. REVIEW mode audits an existing page, diagnosing the level (direction vs composition vs component) before listing fixes. Use when designing, redesigning, or reviewing a marketing or product website, wireframe, or page layout. Conversion optimisation and A/B testing, usability, pre-launch QA, and page speed are adjacent disciplines handled separately. Use this for any new marketing or product page build, not only reviews: it owns the reference-first sequence, loading a committed project direction, else a reference, before any components, rather than letting a blank-prompt generator run first."
user-invocable: true
argument-hint: [page or section to design/review] [optional: URL, screenshot, reference, or goal]
---

## Web Design Skill

Design or review website layouts at a senior product-design level. Every recommendation is grounded in visual hierarchy, attention, and conversion intent, not preference.

**First, pick the mode for $ARGUMENTS:**
- **GENERATE** — building a new page or redesigning an existing one. Run the sequence below in order. Most "my designs look cheap" problems come from skipping straight to the component rules; do not.
- **REVIEW** — auditing an existing page. Diagnose the level first, then audit.

If no arguments: ask what we are designing or reviewing, the goal of the page, and the one action the visitor should take.

---

# MODE: GENERATE (new page or redesign)

A page comes out generic when it is built from a blank prompt and the component rules alone. Distinctive comes from locking a direction from a reference, then composition, before any component work. Run these in order.

## Step 0 — Direction intake (required, do not skip)

Get the direction before designing. Take it from the first available source in this order:

1. **A direction the project already committed.** Check whether the target project has a locked visual point of view already written down: a direction-lock file kept with the project, a brand or design-system document, or an equivalent record wherever this project keeps its design decisions. If one exists, LOAD it and treat its axes (type, colour, depth, spacing, composition, motion, signature move) as hard constraints. That IS your reference. Do not re-derive a direction or hunt for a new one. Restate it in the Step 1 block and go to Step 2.
2. **A reference the user supplies** (URL, screenshot, named site). Look at the actual image where possible. A named site with no image transfers a label, not composition, so fetch a screenshot before locking.
3. **A reference you propose** from a design-inspiration source such as Mobbin, Refero, Awwwards, Godly, or Lapa Ninja. If any of these is wired into this environment as a connected tool, pull a real screen through it and look at the image rather than working from the name alone.

Lock ONE direction; do not average competing styles. Name what to copy structurally (spacing rhythm, type contrast, depth, restraint), not literally.

**STOP guard:** never write page code with neither a committed direction-lock nor a real reference. If you have neither, stop and get one first. A blank-prompt build regresses to the median template, and that is the single biggest cause of cheap, generic output. When a project ships a strong page, consider capturing its direction as a `direction-lock.md` so future pages inherit it instead of re-rolling.

## Step 1 — Lock the aesthetic direction

If Step 0 loaded a committed direction-lock, the direction is already locked: restate it as the one short block below and move to Step 2. Run the derivation in this step only when no lock existed and you are locking a fresh reference.

Load `references/design-system-starter.md`, which carries the aesthetic point of view and the anti-slop tells in full. If this environment also has a dedicated aesthetic-direction generator available, run it here as well; the starter file is self-sufficient without one. Commit, before building:
- Two fonts (a distinctive display + a clean body). Ban Inter, Roboto, Arial, Poppins, system-ui, Space Grotesk.
- An OKLCH palette: one dominant colour + one sharp accent, neutrals tinted toward the brand hue, never pure black/white.
- A depth language (layered shadow scale, concentric radii), a motion signature (one orchestrated page-load reveal), and a named emotion ("calm and precise", "bold and editorial").

Output the locked direction in one short block before writing components, so it is a visible constraint.

## Step 2 — Composition (the layer most cheap pages miss)

Load `references/composition.md`. Design the page-level structure before the parts:
- One continuous canvas, not full-bleed colour bands stacked edge-to-edge (that is the dated, cheap-reading default).
- Accent/dark sections become floating rounded inset panels with side margins and layered shadows.
- Real depth and elevation; at least one deliberate overlap bridging a seam; layout variety across sections (vary inset vs full-bleed, column structure, density). Rhythm comes from variation, not repetition.

## Step 3 — Component hygiene

Now apply the component-level rules (Hero Patterns, Card and Grid Patterns, Metrics and Stats, Interactive Patterns, Content Placement, below). These prevent local mistakes. They make a page correct; Steps 0-2 make it distinctive. Both are needed.

## Step 4 — Hand off

After the build, sequence the specialist passes in this order, whether you run them yourself or hand them to someone else: conversion optimisation, then usability, then pre-launch QA covering interaction, forms and accessibility hygiene, then page speed. Verify by screenshotting the full page and looking at it as a whole, not by DOM metrics alone.

---

# MODE: REVIEW (audit an existing page)

## Diagnose the LEVEL first

Before listing any fixes, classify why the page underperforms or "feels cheap" (see `references/composition.md`):
- **Direction** — generic font, timid palette, no point of view. Usually a restart from the direction lock, not a tweak.
- **Composition** — repetitive band-stacking, flat, no depth/overlap/variety. Usually a structural restart.
- **Component** — a specific card, a long headline, a noisy label. Only here do the component rules below fix it.

Treating a composition problem with component tweaks is the granular treadmill: the page improves on paper and still feels cheap. Name the level, then fix at that level. A direction or composition problem needs a restart on a better base; you cannot tweak a generic base into a distinctive one.

## Audit output format

1. **Level diagnosis** — is the core issue direction, composition, or component?
2. **Hard violations** — things that break visual rules or create bugs.
3. **Composition issues** — page-level rhythm, depth, overlap, variety.
4. **Component issues** — hero text, grids to restructure, noisy labels.
5. **Quick wins** — content/minor restructuring, no redesign.
6. **Recommended tests** — worth A/B testing if traffic allows.

---

# Hard Rules (apply in both modes)

### No hard divider lines between sections
Never separate sections with horizontal rules or visible divider lines. Separate with whitespace, elevation, and floating panels on one continuous canvas (see `references/composition.md`). Do NOT default to alternating full-bleed colour bands: that is the dated pattern that reads cheap. Reserve a colour band for one deliberate moment (an offer/CTA panel), not as the per-section separator.

### Apply text casing consistently
Whatever casing the brand uses, apply it consistently across the same level of hierarchy. Do not mix casings on elements at the same level.

### Commit to a palette and hold it
Apply the locked palette (one dominant + one accent) consistently. No random accents outside the defined set.

---

# Component level (Step 3 / REVIEW component issues)

## Hero Patterns

### Headline: 4-8 words
Short and declarative. State the outcome, not the mechanism. "[Result] for [audience]" is reliable.

### Subtitle: 1-2 sentences maximum
One or two short sentences. Long subtitles push the CTA below the fold.

### Trust signals below CTAs
Place credibility signals (logos, badges, guarantees, ratings) directly below the primary CTA.

### Hero layout: match structure to content
Product visual to show: 2-column, text left, visual right. Single strong statement, no visual: centered. Pick one pattern per page type and hold it.

## Card and Grid Patterns

### Prefer 3 columns over 4 for key highlights
For headline metrics or primary benefits, default to 3. Four equal-weight items feel like a wall.

### 4 cards are fine when items are genuinely distinct
If all 4 are different categories that benefit from comparison, keep them; add a badge on the primary one.

### Break repetitive identical card grids
4+ identical cards: break the pattern with hierarchy (one hero stat), grouping, or a different layout (timeline, accordion). Vary radius/padding/height on purpose.

### Bullets over paragraphs in cards
Headline + 2-4 short bullets, not headline + paragraph.

### Remove labels that add no information
Delete a label the visitor could already infer from the content.

### Group 6+ similar items under category headings
6+ items of one type: group into 2-3 labeled columns.

## Metrics and Stats

### Hero stat + supporting list
Most striking number large on the left; the rest smaller on the right. A flat grid of equal numbers has no focal point.

### Group 5+ outcome metrics into labeled categories
Group under headings ("Speed", "Cost", "Quality") in 2-3 columns.

### Lead metric labels with the outcome number
"60% faster" beats "went from slow to fast in 60% less time."

## Interactive Patterns

### Use vertical timelines for sequential content
Stages/steps/layers: clickable vertical timeline, one step expanded at a time. Keeps sequence clear and the page compact.

### Tab navigation must not compete with primary CTAs
Tabs navigate, buttons convert. Tab visual weight stays below the primary action.

## Content Placement

### Homepage is a map, not a manual
Orient and route visitors. Keep deep product detail off the homepage.

### Product pages must add new information
Every section adds something the homepage did not have.

### Front-load the strongest claim
The hero gets the best stat or clearest framing. Most visitors do not scroll past the first content section.

---

## Scoring a page against these rules

To score a page rather than just audit it, treat every rule above as pass (1) or fail (0) per surface: the Hard Rules and the Component level always, plus whether the page holds to its direction lock and to the composition rules in `references/composition.md` in GENERATE contexts. The denominator is the number of surfaces scored multiplied by the number of rules that actually apply to them, so report it as "<M> surfaces x <N> applicable rules; <pass>/<total> pass" rather than as a bare percentage. A rule that does not apply to a surface is excluded from the denominator, never counted as a pass.

## References

- `references/design-system-starter.md` — lock fonts, OKLCH colour, depth, motion, the 7-pass build order, restart-beats-tweak. Load in Step 1.
- `references/composition.md` — page-level rhythm, continuous canvas + floating panels, level diagnosis. Load in Step 2 and at the start of any REVIEW.

## Adjacent disciplines (where this skill stops)

- Aesthetic direction generation, if this environment has a dedicated generator for it.
- Conversion optimisation and A/B testing.
- Usability and interaction design.
- Pre-launch QA, covering forms and accessibility hygiene.
- Page speed and performance scoring.
