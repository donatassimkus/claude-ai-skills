# Composition — the page-level layer most "cheap" pages are missing

Load this in a GENERATE pass after the direction is locked, and FIRST whenever a page "feels cheap" despite clean parts. The principle it encodes: composition beats components.

## The two levels of design

1. **Component level** — tokens, cards, typography, spacing of a single element. Most AI work (and most checklists, including the base web-design rules) operates here.
2. **Page / composition level** — full-page rhythm, depth, spatial relationships, how panels relate, where the eye lands and travels.

A page with correct components and tokens that still reads "amateur / 10-year-old template / cheap" is a **composition failure, not a component failure.** Fixing card shadows and heading lengths on a broken composition is futile. The smoking case: a homepage with correct tokens, clean cards, and proper spacing was rated cheap because of 13 full-bleed colour bands welded edge-to-edge, zero layout variation, flat cards with hairline borders, and nothing bridging the section seams. The parts were fine. The composition was the problem.

## Diagnose the LEVEL before listing any fixes

When a page reads as cheap, classify the problem BEFORE proposing changes:
- **Direction problem?** Generic font, timid palette, no point of view. Fix in the direction lock (design-system-starter.md). Usually a restart, not a tweak.
- **Composition problem?** Repetitive band-stacking, flat, no depth, no overlap, no rhythm variation. Fix here. Usually a restart of the page structure.
- **Component problem?** A specific card, a too-long headline, a noisy label. Only here do the base web-design component rules apply.

Treating a composition problem with component fixes is the granular-tweak treadmill: the page improves on paper and still feels cheap. Name the level first.

## The modern composition pattern (for SaaS / positioning / marketing pages)

The dated default is **full-bleed colour bands stacked edge-to-edge** (section, section, section, each a different background, welded together). It reads as a 2018 template even with rounded corners. Replace it with:

- **One continuous canvas.** A single warm-neutral or white background runs the whole page. Sections are not separate coloured slabs.
- **Floating inset panels.** Accent/dark sections become rounded panels that sit ON the canvas with side margins and soft layered shadows, like cards on a desk, not full-bleed bands.
- **Depth and elevation.** Cards and panels have real elevation (layered shadows), larger radii, and sit at different visual heights. Flat-on-flat is the cheap tell.
- **Deliberate overlap.** At least one element bridges a seam: a card that overlaps two sections, an image that crosses a panel edge, a stat that breaks the grid. Overlap kills the rigid stacked-slab feel.
- **Layout variety across sections.** Do not repeat the same band shape down the page. Vary: full-bleed vs inset, 2-col vs asymmetric vs centered, dense vs airy. Rhythm comes from variation, not repetition.

## Rhythm without the dated band system

You still need separation between sections, just not via stacked solid bands:
- Separate with whitespace and elevation (a floating panel reads as distinct without a coloured slab behind it).
- Use a colour band sparingly, as a deliberate moment (one offer/CTA panel), not as the default per-section separator.
- If two adjacent sections feel identical, the fix is a layout change (inset vs full-bleed, different column structure), not just a different background colour.

## Verify by looking, not by metrics

A DOM check confirms elements exist with correct values; it cannot tell you a page looks cheap. After a composition pass, screenshot the full page and LOOK at it as a whole: does it have depth, rhythm, and a focal path, or is it flat repetitive slabs? The feedback that matters comes from the eye, so put the eye in the loop, not just the metrics.

## Scope a redesign safely

Put all redesign changes under a `.{page}-v{n}` root class so other pages and templates are not affected by a composition restart.
