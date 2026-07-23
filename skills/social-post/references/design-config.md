# Social Post Design Config

Brand identity (colours, name, handle, website, fonts, asset paths) belongs in ONE brand config the image tooling reads, kept separate from this file so a second brand drops in its own copy without touching the method. The specs below are the universal layout method, which does not change per brand.

## Brand Colors (see config)
- Background dark: the brand background-dark colour (pure black, CTA slides)
- Background light: the brand background-light colour (white, content slides)
- Primary green accent: the brand green colour
- Heading text (name): the brand background-dark colour on white slides, the brand background-light colour on dark slides
- Body text light: the brand text-light colour
- Subtitle/bright text: the brand text-bright colour
- Muted/secondary text: the brand text-muted colour

## Image Dimensions
- Size: 1080 x 1350 (4:5 ratio)
- Optimal for LinkedIn and Instagram feed (maximum vertical screen space)
- **Optical center rule:** Shift all vertically centered content UP by 6% of canvas height (~81px on 1350px). True mathematical center looks visually low. This compensates. **Exception:** CTA slides use true center for the tagline block because the profile section already occupies the top, so optical offset would push content too high.

## Profile Section (Cover + CTA slides)

### Cover slides
- Photo: 220px circular, no ring/border
- Name: the brand name, 72pt brand-font Bold, black
- Verified badge: real PNG asset, cap height + 4px, baseline aligned
- Handle: the brand handle, 40pt brand-font Regular, the brand text-muted colour
- Layout: photo left, name + badge on first line, handle below, 20px name/handle gap

### CTA slides
- Photo: 200px circular, centered horizontally
- Name: 52pt brand-font Bold, white, centered
- Badge: cap height + 4px, next to name, baseline aligned
- Handle: 36pt brand-font Regular, the brand text-light colour, centered below name
- Background: pure black (the brand background-dark colour)
- Green accent bars top and bottom (8px)
- Green button: 360px wide, 80px tall, 40px border radius
- Button text: 44pt brand-font Medium, white
- **Profile position:** Fixed at 50px from top (never centered in upper space)
- **Minimum gap:** 80px between profile bottom and tagline block start
- **Tagline centering:** True vertical center (no optical offset). Profile already occupies top space, so optical offset pushes tagline too high.
- Tagline: 66pt brand-font Medium, white, 2 lines. Use the user's own one-line "I talk about X" statement, split across the two lines by topic rather than by character count, keeping natural topic groupings on the same line.
- "for more like this": 28pt brand-font Light, muted
- Website: 32pt brand-font Regular, green, bottom of slide

## Content Slides
- Green accent bar at top: 8px, the brand green colour
- Text: 66pt brand-font Medium, black, optical centered
- Slide numbers: bottom right, 28pt brand-font Regular, the brand text-muted colour
- One idea per slide

## Steps Slides
- Green accent bar at top: 8px, the brand green colour
- Numbered circles: 64px diameter, green fill, white number (38pt brand-font Medium)
- Step text: 50pt brand-font Regular, black
- 170px vertical spacing between steps
- Optical centered

## Asset Paths
All assets live in the user's own `assets/` folder; establish it once and persist the location.
- Headshot: a circular headshot PNG at 600px
- Verified badge: a small badge PNG (optional; skip it entirely if the user has no badge)
- Badge sizes to export if used: 48px, 64px, 96px PNGs

## Font
- Pick ONE family and hold it across every asset. A variable or multi-weight open-licence family works best: it ships the weights below in one download, and the licence permits embedding in generated images. Check the licence before shipping anything public.
- Weights needed: Light (300), Regular (400), Medium (500), Bold (700)
- Font files live in the user's `assets/fonts/` folder, one file per weight
- Usage: Bold for name/headings, Medium for content text/buttons/taglines, Regular for handle/body/step text, Light for subtle text ("for more like this")

## Accent (two voicings)
The accent colour is set per brand, but the TWO-VOICING RULE is fixed and is the part that matters: one accent almost never has enough contrast on both light and dark surfaces, so define two and pick by surface rather than reusing one everywhere.
- ON WHITE surfaces (content slides, bars, pills, circles, table headers): a DARK accent with white text. A bright or neon accent on white is the classic failure here; measure it, because a vivid light-on-white pairing can land near 1.3:1 and read as invisible.
- ON DARK surfaces (CTA slide, dark stat and quote variants): a near-black background, the BRIGHT accent, and near-black text on any bright accent button fill.
- Store both voicings in the brand config as named values (on-white accent, dark-surface accent, dark-surface text, dark background) and have the image tooling select by surface automatically, so no slide picks the wrong one by hand.

## Image Styles

All generator functions accept a `style=` parameter. Auto-selected based on content, user can override.

| Style | Description | Best for | Requires photo |
|---|---|---|---|
| `branded` (default) | Bold branded style. White content slides, dark CTA, green accents. | Opinion, framework, how-to, carousel, steps | No |
| `photo` | Real photo cropped to 4:5. Paired with caption. | Announcement, behind-the-scenes, personal, event | Yes |
| `overlay` | Card with green border on background photo. Sharp corners (2px). Light + dark variants. 5 positions x 2 = 10 files. | Announcement, quote, single-statement, personal | Yes |
| `screenshot` | Screenshot/graph on branded background. Rounded corners (8px), drop shadow. Light + dark. Auto-sizes any aspect ratio. | Tutorial, product-demo, data, comparison, before-after | Yes |

**Image inbox:** an `inbox/` folder in the user's social-posts working directory
- `inbox/` (root) = photos → generates photo + overlay + screenshot styles. Originals move to `inbox/processed/`.
- `inbox/screenshot/` = screenshots, graphs, charts → generates screenshot style only. Originals move to `inbox/screenshot/processed/`.

**Branded style always generates.** Other styles depend on which inbox folder has files. Output organized into `assets/{style}/` subfolders.

New styles: register the style in whatever style table the image tooling keeps, and add its style-specific slide renderers if the existing ones do not cover it.

## Slide Type Selection Rules (hard rules)

| Type | When to use | Photo | Background |
|---|---|---|---|
| Cover | First slide of carousel, single image post | Yes (220px) | White |
| Content | Middle slides with one idea (flowing text, single statement) | No | White |
| Highlight Content | Flowing text where 1-2 key terms need inline bold/underline emphasis | No | White |
| Steps | Lists, phases, processes, numbered items. ANY content with 2+ distinct items. | No | White |
| Screenshot | Embedded screenshot in carousel slide | No (screenshot image) | White |
| Stat | Hero number with subtitle, profile section | Yes (120px, centered) | Dark |
| Quote | Decorative quote mark, left-aligned quote with accent bar, profile | Yes (100px) | Dark |
| CTA | Last slide of carousel | Yes (200px, centered) | Dark |

**Steps vs Highlight Content (hard rule):** If the content is a list of items (phases, steps, features, tools), ALWAYS use `create_steps_slide`. Never use `create_highlight_content_slide` for list content. Highlight Content is only for flowing sentences where 1-2 key terms need inline emphasis. If in doubt, use Steps.

**Highlight Content spacing rule:** Every segment passed to `create_highlight_content_slide` must include trailing spaces when followed by another segment on the same line. Missing spaces cause words to run together.

## Save Prompt on Images

When the engagement strategy targets saves, add a subtle save prompt on the most reference-heavy slide or single image.

**When to add:**
- Steps slides with tool lists, process checklists, or numbered how-tos
- Screenshot slides showing tables, dashboards, or data
- Single images with tool comparisons, stat collections, or reference tables
- Any visual someone would want to come back to later

**When to skip:**
- Cover slides (hook is the priority, not save prompt)
- CTA slides (follow CTA is the priority)
- Opinion/hot take posts with no reference material
- Profile/quote/stat highlight standalone assets (these are shareable, not saveable)

**Design spec:**
- Text: "Save for later" or "Bookmark this"
- Font: 24pt brand-font Light
- Color: the brand text-light colour (muted, same as TEXT_LIGHT)
- Position: bottom left of slide, 80px from left, 50px from bottom
- On dark backgrounds: use the brand text-muted colour
- Must not compete with slide numbers (bottom right) or main content
- Subtle. It's a nudge, not a banner.

## Reference Card Slides

When the engagement strategy targets saves, structure at least one slide as a "reference card": dense, scannable information someone would screenshot or save.

**Reference card types:**
- **Tool list:** Tool name + one-line use case. 4-6 tools per slide. Use `create_steps_slide` with `numbered=False`.
- **Stat collection:** 3-5 numbers with one-line context each. Use `create_steps_slide` with `numbered=False`.
- **Process checklist:** Numbered steps someone can follow later. Use `create_steps_slide` with `numbered=True`.
- **Comparison table:** Side-by-side using `create_table_slide`.

Reference cards are dense by design. More information per slide = more reason to save. But still scannable: short lines, clear labels, no walls of text.

## Cover Variants (hard rules)

Every cover MUST generate 4 variants:
1. **Standard** (`slide-01-cover-a.png`): the plain cover, no highlighted words
2. **Underline** (`slide-01-cover-underline.png`): highlight style set to underline
3. **Bold** (`slide-01-cover-bold.png`): highlight style set to bold
4. **Pills** (`slide-01-cover-pills.png`): highlight style set to pills

Each variant gets its own PDF. Each gets a matching single image, rendered with the content optically centred for standalone use rather than positioned for a carousel.

**Highlight word selection:** Pick 1-2 words from the hook most relevant to the target audience. The words that make someone think "this is for me."

**Pills merge rule:** Adjacent highlighted words must render as ONE merged pill, not two touching pills. Build that into the renderer so it happens automatically.

## Cover B (screenshot-embedded, hard rule)

When screenshots exist in the inbox, ALWAYS generate Cover B, the screenshot-embedded cover layout:
- `slide-01-cover-b.png`: profile + hook + subtitle + screenshot bleeding off bottom
- `single-image-b.png`: same layout with `true_center=True`
- `carousel-b-linkedin.pdf`: Cover B + shared content slides + CTA

**Screenshot selection for Cover B:** Pick the most visually striking screenshot. Prefer complex, colorful visuals (automation flows, node diagrams) over tables or sparse layouts. The screenshot is a teaser, not documentation.

**Layout:** Profile at top, hook below, subtitle below hook, screenshot starts below subtitle and bleeds off the bottom edge. Top corners rounded (12px), no bottom border. The bleed is intentional design.

**Scaling:** Landscape screenshots fill width naturally. Portrait (ratio < 0.7) scale to ~55% width. The screenshot should feel like it's peeking in from below, not fully displayed.

## Subtitle Number Rendering

Cover subtitles auto-detect numbers and render them at 44pt brand-font Medium black. Non-number text renders at 36pt brand-font Regular muted gray. Build this as mixed-run subtitle rendering inside the cover renderers so it happens automatically, rather than formatting each subtitle by hand.

## Stat Highlight Slides
- Background: pure black (the brand background-dark colour)
- Green accent bars: top (8px) and bottom (8px)
- Hero number: 160pt brand-font Bold, the brand green colour, centered
- Horizontal divider: 160px wide, 4px, the brand text-muted colour, centered below number
- Gaps: 40px number-to-divider, 40px divider-to-subtitle
- Subtitle: 46pt brand-font Regular, the brand text-bright colour, centered
- Profile section: anchored ~340px from bottom. Photo 120px centered, name 42pt Bold white + badge, handle 30pt Regular the brand text-light colour, all centered
- Website: the brand website, 32pt Regular green, bottom center (65px from bottom)
- Number+divider+subtitle block is optical centered (shifted up by 6%)

## Quote Card Slides
- Background: pure black (the brand background-dark colour)
- Green accent bars: top (8px) and bottom (8px)
- Decorative open quote mark: 200pt brand-font Bold, green, positioned at left_margin (100px)
- Quote text: 60pt brand-font Medium, white, left-aligned at 100px, max width = WIDTH - 100 - 80
- Gap: 10px between quote mark bottom and quote text top (tight)
- No vertical accent bar (removed for cleaner look)
- Profile section: 50px below quote text. Photo 100px, name 42pt Bold white + badge, handle 30pt Regular the brand text-light colour, left-aligned to match quote indent
- Website: the brand website, 32pt Regular green, bottom center (65px from bottom)
- Entire quote mark + quote + profile block is optical centered