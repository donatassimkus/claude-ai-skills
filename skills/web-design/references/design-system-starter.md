# Design-system starter — lock the look before you build

Load this at the START of any GENERATE pass (new page or redesign). It turns "fast AI output" into "fast distinctive output" by committing a visual direction before a single component is written. Generic by design: fill the specifics from the active project's brand and CLAUDE.md.

The core law: **AI builds the statistical median of its training data unless you constrain it first.** The median is the generic 2019-era template ("purple oatmeal"). What you feed in before the build decides the quality, not the model and not the tool.

---

## 0. The anti-slop tells, and the antidote for each

If the output has any of these, it will read as cheap. Each has a direct fix.

| Slop tell | Antidote |
|---|---|
| Generic font (Inter, Roboto, Arial, Poppins, system-ui, Space Grotesk) | Pick a distinctive display face + a clean body face (see §2). This is the single fastest jump. |
| Indigo/purple-to-blue gradient on white; timid evenly-spread palette; pure `#000`/`#fff` | One dominant colour + one sharp accent, OKLCH, neutrals tinted toward the brand hue (§3). |
| Centered badge + headline + 3 icon-card grid; everything centered | Asymmetry, a real grid, varied section layouts (see composition.md). |
| Every card same height / radius / padding | Vary size, radius, padding on purpose to build hierarchy. |
| Flat cards, or one generic drop-shadow on everything | Layered elevation scale (§4); often a 1px tinted border reads more premium than a shadow. |
| No motion, or `fade-in-up` sprayed on every element | One orchestrated page-load reveal with rhythm; reserve other motion for state + attention (§5). |
| Flat solid-colour backgrounds | Atmosphere: subtle gradient mesh, grain/noise, soft pattern (§6). |

---

## 1. Reference first (do not skip)

Pick ONE reference before designing. A reference replaces "median of the internet" with "this specific shipped thing." Sources:
- Product UX that actually shipped: **Mobbin**, **Refero**. If either is wired into this environment as a connected tool, pull a real screen through it and look at the image.
- Award-grade visual inspiration: **Awwwards**, **Godly**, **Lapa Ninja** (landing pages).

Lock ONE direction. Averaging a minimalist and a maximalist reference yields neither. Name what you are copying structurally (spacing rhythm, type contrast, depth, restraint), not literally.

---

## 2. Typography (commit two fonts)

- **Ban**: Inter, Roboto, Arial, Poppins, system-ui, Space Grotesk. These are the default-AI fonts.
- **Pick**: one distinctive display/heading face with character + one refined, readable body face. Examples as starting points, not defaults: Playfair Display / a strong grotesque / a humanist serif for headings; a clean neutral sans for body. Variable fonts ship many weights in one file (cheap character). Self-host the font files rather than loading them from a third-party CDN: it removes a render-blocking third-party request and keeps the page independent of an outside service.
- **Type scale**: a modular scale (e.g. ratio ~1.2 to 1.333), not ad-hoc sizes. Generous heading sizes. Tight letter-spacing on large headings.
- `text-wrap: balance` on headings (kills widows), `text-wrap: pretty` on body.
- `font-variant-numeric: tabular-nums` for any aligned number columns.

---

## 3. Colour (one dominant + one accent, OKLCH)

- Build in **OKLCH**, light and dark.
- One dominant colour, one sharp accent applied with discipline. Not a timid even spread.
- Never pure `#000`/`#fff`. Tint neutrals toward the brand hue so the page feels designed, not default.
- Contrast: WCAG AA minimum (4.5:1 body, 3:1 large headings); prefer **APCA** for perceptual accuracy where you can.
- Interactive states (`:hover`/`:active`/`:focus`) carry MORE contrast than the rest state.
- Dark mode: deep neutral background + elevated surface colours, not true black everywhere; avoid oversaturation.

---

## 4. Depth, spacing, radii (the craft layer)

- **Spacing scale**: a single base unit (4px or 8px) and a token scale; section padding generous (80-120px vertical on marketing pages).
- **Radius scale**: nested radii must be **concentric** — a child's radius is less than or equal to its parent's. Mismatched radii look amateur.
- **Shadow / elevation scale** (xs to 2xl), not one shadow everywhere. Real shadows are **layered**: at least two (an ambient soft layer + a tighter direct-light layer).
- **Hue consistency**: on a non-neutral background, tint borders, shadows, and muted text toward the background hue.
- Avoid gradient banding (use a background image or dithered gradient, not a hard CSS mask fading to dark).
- Optical alignment: nudge +/-1px where perception beats geometry.

---

## 5. Motion (one big moment, not confetti)

- Library: **`motion`** (imported `motion/react`; formerly framer-motion) for React; **motion-one** for lighter/vanilla. On another framework, use its established animation library, or CSS transitions where they suffice; the rules below hold whichever you pick.
- **Animate `transform` and `opacity` only.** Never `width`/`height`/`top`/`left`/`margin`. Never `transition: all` (list properties).
- One well-orchestrated page-load reveal with staggered delays and real rhythm beats more than micro-interactions everywhere.
- Put the remaining motion on the primary CTA and form inputs (state + attention), not on every element.
- Always honour `prefers-reduced-motion`. Animations must be interruptible.

---

## 6. Texture and atmosphere

- Subtle grain/noise overlay on solid or gradient backgrounds adds a tactile, finished quality. Keep it subtle; it is a finish, not a feature.
- Glassmorphism 2.0: `backdrop-filter: blur()` layered with noise + a gradient border + a soft shadow. Accessibility: put a ~30% opacity film behind text over glass so it stays legible.
- Multi-layer gradient backgrounds + a faint dot/grid pattern beat flat fills.

---

## 7. Build in layers, never one mega-prompt

Run the build as ordered passes. Each pass is its own step; do not bury layout or motion inside a feature list.

1. **Direction + tokens** — brand vibe, the chosen reference, the token scales above, the named emotion.
2. **Colour** — exact OKLCH values, light + dark.
3. **Typography** — the two fonts + the scale.
4. **Layout + composition** — grid, section rhythm, spacing (see composition.md). Its own pass.
5. **Components** — buttons, cards, forms, modals, refined individually.
6. **Motion + polish** — the page-load reveal, hover/focus/loading states.
7. **Mobile pass** — explicit; the build defaults desktop-first.

---

## 8. Restart beats tweak

A generic base sits in a local maximum. Small edits climb that hill: a slightly better generic page. The distinctive design is on a different hill (different composition, font character, depth, motion), and every step between looks worse before it looks better, so tweaking cannot reach it. When the base reads generic, **regenerate from a corrected direction** rather than nudging. Scope a redesign under a `.{page}-v{n}` root class so other pages are untouched.

---

## 9. Name the emotion

Before building, state the feeling in plain words: "calm and precise" / "bold and editorial" / "clinical and trustworthy" / "warm and human". A named emotion is a constraint the model can design toward; "make it modern" is not.
