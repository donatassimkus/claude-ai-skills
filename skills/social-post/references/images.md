# Visual direction and image generation

Loaded at Step 4 of the social-post skill. Visual specs (colours, fonts, dimensions, slide types) live in `references/design-config.md`.

## Step 4: Visual direction

For carousel and image posts, provide:

- **Slide count** (carousels): recommended number of slides
- **Slide-by-slide outline** (carousels): title + key point per slide
- **Visual concept** (image posts): describe what the image should show
- **Text overlay** (if any): exact text for on-image copy
- **Style notes**: clean/minimal, dark/light, data-heavy, quote-style

For text-only posts: skip this section entirely.

## Step 4a: Image direction confirmation checkpoint

**Before generating any images, show the complete asset plan. Then ask confirmation.**

Show the user:
- Complete list of every asset to be generated (carousel slides, stat highlights, quote cards, standalone images, overlay variants)
- Exact hook text on all images
- Photo source (library category, inbox, or none)
- For carousels: confirm slide count and slide-by-slide content
- For photo posts: confirm overlay positions and variants
- For screenshot posts: confirm how screenshots will be used (embedded in slides, standalone variants)

Use AskUserQuestion to confirm after showing the plan.

**Minimum 1 question at this checkpoint.**

Only after confirmation: generate all images.

**Photo-topic matching (when a photo or screenshot is used):**
Before confirming, preview the selected photo (generate a small crop if HEIC) and assess the match:
- **Direct match:** photo setting reinforces the topic (working-on-laptop for productivity post). Give feedback: "This photo works because [reason]."
- **Intentional contrast:** photo creates curiosity by contrasting the topic (drinking coffee for hustle critique). Give feedback: "This photo contrasts with the topic. The tension creates curiosity if intentional."
- **Poor fit:** photo neither matches nor creates useful contrast. Flag it: "This photo does not fit the topic. Suggest: [alternative category] or no photo."
- **Technical check:** Is there enough clear space for overlay text? Is the photo front-facing (preferred for LinkedIn)? Is the lighting appropriate for the tone?
- **Screenshot check:** If screenshots are in inbox, review what they show and confirm they match the post content. Flag any that seem unrelated.
Use AskUserQuestion to let the user confirm, swap, or skip the photo.

---

## Step 4b: Generate images

After writing the caption and visual direction, generate **all styles and formats** in one go. The user picks whichever works best. Same captions, different visuals.

### Image inbox

**IMPORTANT: the inbox lives in the user's social-posts working directory, as `inbox/`, NOT inside the skill directory. Always check that exact path, and whatever image tooling gets built must point at the same one.**

Before generating, run `check_inbox()` to see what's available:

**`inbox/`** (root) = photos. Generates: photo + overlay + screenshot styles.
- Run `process_inbox(post_assets_photo_dir)` to crop to 1080x1350 and move originals to `inbox/processed/`.

**`inbox/screenshot/`** = screenshots, graphs, charts. Generates: screenshot style only (no photo/overlay).
- Run `process_screenshot_inbox()` to get paths, then generate screenshot style. Move originals to `inbox/screenshot/processed/`.

If both folders have files, generate all applicable styles for each. If neither has files, generate branded only.

### Photo library

**Path:** an `assets/photo-library/` folder in the user's working directory

The user bulk-uploads personal photos here. Photos are organized by category and stay until used in a social post.

**Categories:**

| Folder | Contents | User prompt |
|---|---|---|
| `solo/` | Personal/professional shots (just the user) | "use my photo" |
| `with-kid/` | Photos with kid | "use a photo with my kid" |
| `with-wife/` | Photos with wife | "use a photo with my wife" |
| `family/` | All three together | "use a family photo" |
| `fitness/` | Gym, workouts, fitness | "use a fitness photo" |
| `lifestyle/` | Hotels, travel, cars, nice locations | "use a lifestyle photo" |

Each category has a `used-on-social/` subfolder where photos move after being used.

**When the user requests a photo:**
1. Parse the prompt for a category. "use my photo" defaults to `solo`. "use a photo with my kid" maps to `with-kid`. Etc.
2. Call `pick_library_photo(category)` to get an unused photo path and category.
3. Use `smart_crop()` to crop it to 1080x1350 and save to post assets.
4. Generate photo + overlay styles from this photo (in addition to all other styles).
5. After generation, call `mark_library_photo_used(photo_path, category)` to move it to the category's `used-on-social/` folder.

**Priority order:**
1. Inbox photo (intentional, per-post) → consumed as normal via `process_inbox()`
2. Library photo (when user requests a photo) → moved to category's `used-on-social/` after use
3. No photo requested → branded styles only

**When a category is empty:** notify the user. Do not silently fall back to another category.

**Photo requests are additive.** Generate ALL asset types (branded, photo, overlay, stat, quote, standalone). The photo adds variety on top. It does not replace other styles.

**Lifestyle photo usage (hard rule):** Lifestyle photos (hotels, cars, travel, nice locations) are used sparingly: maximum 1 in every 8-10 posts. The photo is always the background, never the subject. The caption is always about a tactic, lesson, or insight. The lifestyle setting adds aspiration without bragging. Never mention the location, car, or setting in the caption. Never use lifestyle photos for posts where the content is lightweight (polls, questions). Only pair with strong tactical or results content. If the user requests a lifestyle photo, still follow these rules.

**Inbox cleanup (hard rule):** After ALL image generation is complete, move every processed photo and screenshot from inbox to its respective `processed/` folder. Photos from `inbox/` move to `inbox/processed/`. Screenshots from `inbox/screenshot/` move to `inbox/screenshot/processed/`. Never leave originals in the inbox after a post is produced. This prevents duplicate processing on the next post.

**Use every screenshot (hard rule):** Every screenshot in `inbox/screenshot/` MUST appear in the carousel. No exceptions. If the user added it, it matters. Each screenshot gets its own slide with a contextual caption. Adjust slide count, flow, and captions to accommodate all screenshots. Never drop a screenshot to keep slide count low. Build the narrative to flow naturally through all provided visuals.

### Required assets

These files must exist for image generation to work. If missing, the script raises a clear error with the expected path.

- **Headshot:** a circular headshot PNG at 600px, in the user's `assets/` folder
- **Verified badge:** a small badge PNG at 96px, in the same folder (optional; skip the badge if the user does not have one)
- **Fonts:** the brand's font family in Light, Regular, Medium and Bold weights, as font files in `assets/fonts/` (falls back to a system font if missing)

### Generate all styles

1. Read `references/design-config.md` for current design settings.

2. **Branded style** (always generated): save to `assets/branded/`
   - The standard cover renderer, taking the hook, the subtitle, and an output path.
   - **Cover highlight variants (always generate 3):** After the standard cover, generate 3 additional covers with different highlight styles. Pick 1-2 words from the hook most relevant to the target audience (the word that makes someone think "this is for me"). If the post has data, call out the strongest number in the subtitle (medium weight 44pt black, rest regular 36pt muted gray). Max 2 highlighted words. Non-highlighted text uses light weight for contrast.
     - `slide-01-cover-underline.png` (Variant A): highlighted words bold + green underline
     - `slide-01-cover-bold.png` (Variant B): highlighted words bold only, no color accents
     - `slide-01-cover-pills.png` (Variant C): highlighted words in green pill backgrounds, white text
     - The standard `slide-01-cover-a.png` is still generated (medium weight, no highlights) as the baseline
   - `create_content_slide(text, output_path, slide_num, total_slides)` for content slides
     - **Content slide rules (skimmable, not paragraph walls):**
       - 1-3 sentences max per slide. If content has more than 3-4 lines of flowing text, restructure it.
       - Short punchy statement fits `create_content_slide` as-is.
       - Key terms need emphasis → use `create_highlight_content_slide` (inline bold/underline).
       - List of items, phases, features → use `create_steps_slide`.
       - Dense comparison → use `create_table_slide`.
       - If a slide still feels dense after choosing the right format, split it into two slides.
       - Don't force structure where it doesn't fit. A strong 2-sentence slide beats a forced list.
   - `create_steps_slide(steps, output_path, slide_num, total_slides, start_num=1, title=None, numbered=True)` for steps slides
     - **Step slide rules:**
       - Add a short title (2-3 words) to every step slide via `title` parameter, so the reader knows what the list is about (e.g. "How it works", "What powers it").
       - Use `numbered=True` (default) for sequences where order matters (step 1 before step 2).
       - Use `numbered=False` for unordered lists (tech stacks, features, benefits). Renders small green dots instead of numbered circles.
       - When steps continue across slides, use `start_num` to keep numbering continuous. Numbers must never restart from 1 mid-sequence.
     - Dynamic vertical spacing (auto-adjusts to text height). No fixed step height.
     - Best practice: keep each step to 1-2 lines at 50pt. 3 lines works but gets tight with 5+ steps. If steps are long, consider splitting across two slides or using a content slide instead.
   - `create_cta_dark(cta_text, taglines, output_path, slide_num, total_slides)` for CTA
     - CTA tagline: always 2 lines. Line 1 = "I talk about growth marketing,", Line 2 = "AI, and automation."
   - `assemble_carousel_pdf(slide_paths, output_path)` to combine all slides into a single PDF
   - **Assemble one PDF per cover variant (hard rule):** Each cover highlight variant gets its own PDF with the same content slides. This lets the user pick a cover and have the ready-to-upload PDF immediately.
     - `carousel-underline.pdf`: underline cover + content slides + CTA
     - `carousel-bold.pdf`: bold cover + content slides + CTA
     - `carousel-pills.pdf`: pills cover + content slides + CTA
     - The standard `carousel-a-linkedin.pdf` (no highlights) is still generated as baseline
   - **Two carousel PDFs when Cover B exists:**
     - `carousel-a-linkedin.pdf`: Cover A (text-only) + shared content slides + CTA
     - `carousel-b-linkedin.pdf`: Cover B (screenshot-embedded) + shared content slides + CTA
     - When no Cover B (no screenshots): generate only `carousel-a-linkedin.pdf`
   - **Single image A/B:** `single-image-a.png` (text-only cover) + `single-image-b.png` (screenshot-embedded cover, when Cover B exists)
   - **Single image highlight variants (always generate 3):** Same highlight logic as cover variants but with `true_center=True`. Save to `assets/images/`:
     - `single-image-underline.png` (Variant A): highlighted words bold + green underline
     - `single-image-bold.png` (Variant B): highlighted words bold only
     - `single-image-pills.png` (Variant C): highlighted words in green pill backgrounds
     - The standard `single-image-a.png` is still generated as the baseline
     - Single images use `true_center=True` (true vertical center). Carousel cover slides use optical center (shifted up 6%). Single images are standalone posts with no swipe context, so true center looks better.
   - Carousel slides + carousel PDFs
   - **Cover A/B variants (when screenshots exist in inbox):**
     - **Cover A** (`slide-1-cover-a.png`): Standard text-only cover (profile + hook + subtitle)
     - **Cover B** (`slide-1-cover-b.png`): Screenshot-embedded cover (profile + hook + subtitle + screenshot bleeding off bottom edge)
     - Cover B layout: profile at top, hook text below, subtitle below hook, screenshot starts below subtitle and bleeds off the bottom (no bottom border). Round only top corners of screenshot.
     - Scaling by screenshot aspect ratio: portrait/mobile (ratio < 0.7) scale to ~55% of width showing top+middle; square (~1:1) scale to near-full width, crop bottom 10-15% for bleed; landscape fits naturally, still bleed bottom slightly.
     - The bleed is a design choice, not a constraint. Always intentional.
     - When no screenshots in inbox, generate only Cover A.

3. **Photo style** (if photo(s) in inbox): process ALL photos from `process_inbox()`
   - Each photo gets: `single-image.png` (cropped 1080x1350) + `carousel-cover.png` (as slide 1)
   - 1 photo → save to `assets/photo/`. Multiple → `assets/photo-1/`, `assets/photo-2/`, etc.
   - `carousel-linkedin.pdf`: first photo as cover + branded content slides + CTA (hybrid carousel)

4. **Overlay style** (if photo(s) in inbox): process ALL photos
   - Each photo gets: `create_overlay(photo_path, hook_text, output_dir)` → 5 positions x 2 variants = 10 files
   - 1 photo → save to `assets/overlay/`. Multiple → `assets/overlay-1/`, `assets/overlay-2/`, etc.
   - White card with green border on background photo. Card contains headshot, name+badge, handle (the brand handle), and the hook/statement. Light + dark card variants.

5. **Screenshot style** (if screenshot(s) in inbox): process ALL screenshots as standalones
   - Loop over ALL screenshots from `process_screenshot_inbox()`
   - All screenshots go flat in `assets/screenshot/`, prefixed by a descriptive name (e.g., `scraper-screenshot-website-light.png`, `funnel-screenshot-profile-dark.png`)
   - No subfolders. Prefix identifies the screenshot.
   - Each gets: `create_screenshot(image_path, output_dir, title=contextual_title)` → website light + dark variants
   - **Every screenshot gets standalone treatment, not just one.** If 6 screenshots are in the carousel, all 6 get standalone variants.
   - Auto-detects aspect ratio (portrait/landscape/square), scales to fit
   - Rounded corners + drop shadow for polished look
   - Title text centered above screenshot if provided
   - **Generate TWO sub-variants per screenshot:**
     - **Website variant** (`screenshot-website-light.png`, `screenshot-website-dark.png`): Title top, screenshot center, the brand website bottom.
     - **Profile variant** (`screenshot-profile-light.png`, `screenshot-profile-dark.png`): Title top, screenshot center, profile section bottom (100px photo left, 42pt name+badge and 30pt handle right, 24px gap, whole block horizontally centered on canvas).

6. **Screenshot carousel** (if screenshots in inbox AND format is carousel): embed in `assets/branded/`
   - Read each screenshot to understand its content
   - Use `create_screenshot_slide(image_path, output_path, caption, caption_position, slide_num, total_slides)` to embed screenshots in branded carousel slides
   - Build a mixed slide sequence: cover → text slide(s) → screenshot slide → text slide(s) → CTA
   - Not every screenshot needs text before AND after. Some are self-explanatory with just a caption.
   - Caption position: "above" (default) or "below". Use "above" to set context, "below" for a takeaway.
   - Multiple screenshots = multiple screenshot slides. Order them logically.
   - Assemble all slides into the carousel PDF alongside cover and CTA

7. **Stat highlight** (if format is stat highlight OR post contains a hero number): save to `assets/branded/`
   - Generate both variants: `create_stat_slide(..., dark=True)` saved as `stat-highlight-dark.png` and `create_stat_slide(..., dark=False)` saved as `stat-highlight-light.png`
   - Also works as a carousel slide with `slide_num` and `total_slides` params
   - The number is the hero (160pt bold, green). Dark variant: black bg, white subtitle. Light variant: white bg, black subtitle.

8. **Quote card** (if format is quote card or a strong one-liner exists): save to `assets/branded/`
   - Generate both variants: `create_quote_card(..., dark=True)` saved as `quote-card-dark.png` and `create_quote_card(..., dark=False)` saved as `quote-card-light.png`
   - Green decorative quote mark, profile section below quote, website at bottom. Dark variant: black bg, white text. Light variant: white bg, black text.
   - Best for punchy closing statements or standalone opinions.

### Bonus asset enforcement (hard rule)

After generating the primary format (carousel, text post, image post), always run a bonus asset check:

1. **Scan for hero numbers** in the post content (stats, percentages, counts, time metrics). If any exist, generate stat highlights for the strongest 1-2 numbers. Both light + dark variants.
2. **Scan for strong one-liners** (punchy statements, quotable lines, closing statements). If any exist, generate quote cards for the strongest 1-2 quotes. Both light + dark variants.
3. **These are not optional.** If qualifying content exists, generate them as bonus standalone assets regardless of the primary post format.
4. Save to `assets/branded/` with descriptive names: `stat-highlight-{slug}-light.png`, `quote-card-{slug}-light.png`, etc.

These bonus assets give the user extra content to repurpose as standalone posts, story cards, or engagement pieces. Never skip them.

**Standalone quality rules (hard rules):**
- **Stat highlights must be self-explanatory.** Number + subtitle together must tell a complete story. If someone sees only this image with zero context, they should understand what happened and why it matters. Bad: "27% / survival rate from 740 SEO-tagged hacks." Good: "1,509 → 197 / Only 27% of scraped SEO hacks survived quality filtering."
- **Quote cards must be universally meaningful.** The statement must make sense and land on its own. It should be a truth about the topic, not a fragment that needs the carousel for context. Include the topic (SEO, AI, etc.) in the quote. Use concrete words, not abstract ones ("SEO as a discipline" not "an entire domain").
- **Test:** Cover the rest of the post. Does this single image make someone stop, understand, and want to engage? If not, rewrite.

**Text rendering rule:** Only use ASCII characters in stat highlights, quote cards, and all image text. The brand font may not cover every unicode arrow, em dashes, or special symbols. They render as rectangles. Use plain text alternatives: "to" instead of an arrow, colons instead of em dashes. If a character might not render in the brand font, replace it.

### Repurposable single images

After generating the primary carousel and bonus assets, generate standalone single images that can be used as independent posts later. Save to `assets/branded/singles/`.

**Always generate these types when content qualifies:**

1. **Standalone text cards** — take the 2-3 strongest text slides and add a profile section at the top so they work as independent posts. Each must make sense with zero context. Include a subtitle that adds context (e.g., "I built two SEO skills for Claude Code. Both free.").
2. **Process summary card** — if the post describes a multi-step process, create a single image showing all steps with profile section. Compact version of the steps slide.
3. **Before/after card** — if the post has a transformation (X in, Y out), create a visual showing both numbers side by side with "to" between them.
4. **Standalone table card** — if the post contains a table slide (e.g., before/after comparison), generate a standalone version with profile section at the top. Use `create_table_slide()` with a full descriptive title. Save as `standalone-table-{slug}.png`.

These are in addition to stat highlights and quote cards (which are already generated as bonus assets). The goal: every post produces 5-10 standalone images the user can schedule as separate posts over the following weeks.

**Each standalone image must:**
- Include profile section (photo + name + handle) so it's branded
- Make complete sense on its own with zero carousel context
- Have a clear point or takeaway in one glance
- **Title must include the full topic (hard rule).** Never use generic titles like "What changed", "How it works", "The results." Always include the subject: "What changed on LinkedIn in 2026", "How the Chrome extension backlink works." Test: if someone sees only this image with zero context, do they know what it is about? If not, rewrite the title.

### Output structure

```
assets/
  carousel/                             (slides + PDFs, everything for swiping)
    slide-01-cover-a.png
    slide-01-cover-underline.png         (highlight variant A)
    slide-01-cover-bold.png              (highlight variant B)
    slide-01-cover-pills.png             (highlight variant C)
    slide-01-cover-b.png               (if screenshots exist)
    slide-02-*.png ... slide-N-cta.png
    carousel-a-linkedin.pdf
    carousel-b-linkedin.pdf            (if Cover B exists)

  images/                               (all standalone images, prefixed by type)
    single-image-a.png
    single-image-underline.png           (highlight variant A)
    single-image-bold.png                (highlight variant B)
    single-image-pills.png               (highlight variant C)
    single-image-b.png                 (if Cover B exists)
    quote-{slug}-light.png
    quote-{slug}-dark.png
    stat-{slug}-light.png
    stat-{slug}-dark.png
    standalone-{slug}.png              (repurposable text cards, process summaries, before-after)

  screenshot/                           (flat, prefixed by screenshot name)
    {name}-screenshot-website-light.png
    {name}-screenshot-website-dark.png
    {name}-screenshot-profile-light.png
    {name}-screenshot-profile-dark.png

  photo/                                (empty until photos are provided)
    (overlay and photo style images go here when inbox/ has photos)
```

File naming: prefixes identify type at a glance. No subfolders needed inside `images/` because prefixes (`quote-`, `stat-`, `standalone-`, `single-image-`) are enough.

Always generate images when the format is carousel, image post, or single image. Skip only for text-only posts.
