---
name: technical-audit
argument-hint: [project path or live URL] [--old-sitemap URL] [--widths 320,360,375...]
description: "AUDIT: is this website technically safe to ship? Comprehensive technical QA of a website that builds to static output (Astro, Next.js export, Hugo, Eleventy, plain HTML, anything producing a dist/out/build folder) or a reachable URL; main moment is pre-launch / pre-cutover, but it runs on any live URL anytime. Checks responsive horizontal overflow across device widths, internal link and image integrity, page-title and meta-description uniqueness and length, noindex leaks, sitemap + robots.txt + structured-data presence, launch assets (favicon circular-crop safety, Open Graph 1:1-crop safety, custom 404 page), and placeholder / dev-speak copy. For a rebuild or CMS migration it also cross-references the OLD site's sitemap to confirm every old URL still resolves or redirects, so nothing 404s after the DNS cutover. Produces a verdict table. Invoke when the user says \"technical audit\", \"do a website check\", \"launch audit\", \"is the site ready to launch\", \"pre-launch QA\", \"check the site across devices\" or \"across screen sizes\", \"check for broken links or overflow\", \"did anything get cut off on mobile\", \"check everything before we go live\", or \"verify before the DNS cutover\". Skip for design or copy critique (a design or writing skill), single-page spot checks, and logic / consistency / experience audits (a dedicated UX or experience audit)."
---

# Technical audit

A repeatable pre-launch technical sweep for any static-built or live website. Runs the same battery every time so nothing slips before go-live. Project context is loaded from the active CLAUDE.md.

## Inputs to confirm first

Infer what you can; ask only what you cannot:
- **Project / repo path** (where the site builds).
- **Build command + output dir** (e.g. `npm run build` then `dist/`). Read `package.json` / the framework config to infer.
- **Live deploy URL** (optional, to verify the deployed state and analytics).
- **Old site's sitemap URL** (only for a rebuild or CMS migration, to check URL parity).
- **Device widths** if the user names specific targets; otherwise default to 320, 360, 375, 414, 768, 1024, 1280, 1440.

## Golden rule: test the BUILD, not the dev server

Dev servers compile on demand (slow, will time out an audit) and can serve stale hot-reload state. Always:
1. Build fresh with the project's build command.
2. Serve the built output statically, in the background, with whatever static file server the machine has: `cd <output-dir> && python3 -m http.server 4333 --bind 127.0.0.1`, or `npx serve -l 4333`, or `npx http-server -p 4333`, or any equivalent bound to localhost on a free port. The server is interchangeable; only "static, local, not the dev server" matters.
3. Run all browser checks against `http://localhost:4333` (use whichever port you served on). Stop the server when done (`pkill -f "http.server 4333"`, or whatever stops the one you started).

## The checks

### 1. Responsive overflow (nothing sticking out)

True overflow is `document.documentElement.scrollWidth > viewport width`. An element that looks "off-screen" is often NOT the cause: measure the document, then find every offending element. With the static server running, drive a browser (Playwright MCP, Chrome MCP, a Playwright or Puppeteer script, or any headless browser you can navigate and evaluate JavaScript in): navigate to `http://localhost:4333/`, then evaluate the sweep below. It loads each page once into a hidden iframe and resizes across widths (CSS reflows, no reload, so it is fast), reporting only pages with real overflow plus the offending elements.

```js
async () => {
  const pages = [/* list every distinct template + any pages the user flagged */];
  const widths = [320,360,375,414,768,1024,1280,1440];
  const f = document.createElement('iframe');
  f.style.cssText='position:fixed;top:0;left:0;border:0;visibility:hidden;height:1400px;z-index:-1;width:1280px;';
  document.body.appendChild(f);
  const tick=ms=>new Promise(r=>setTimeout(r,ms));
  const load=u=>new Promise(res=>{f.onload=()=>setTimeout(res,40);f.onerror=()=>res();f.src=u;});
  const out=[];
  for(const p of pages){
    await load(p); const d=f.contentDocument; if(!d||!d.body){out.push({page:p,error:'no doc'});continue;}
    for(const w of widths){
      f.style.width=w+'px'; await tick(30);
      f.style.height=Math.max(1400,d.body.scrollHeight)+'px'; await tick(15);
      const ov=d.documentElement.scrollWidth-w;
      if(ov>1){
        const offs=[];
        d.querySelectorAll('body *').forEach(el=>{
          const cs=d.defaultView.getComputedStyle(el);
          if(cs.display==='none'||cs.visibility==='hidden')return;
          const r=el.getBoundingClientRect();
          if(r.width>w+1||r.right>w+1.5){const c=(el.className||'').toString().trim().split(/\s+/).filter(Boolean).slice(0,2).join('.');offs.push(el.tagName.toLowerCase()+(c?'.'+c:'')+'[w'+Math.round(r.width)+']');}
        });
        out.push({page:p,vw:w,ov,offenders:[...new Set(offs)].slice(0,6)});
      }
    }
  }
  f.remove(); return {overflows:out.length,out};
}
```

Common causes and fixes: a single long word at a fixed large font (make the font `clamp(min, vw, max)`); a fixed-width element (`max-width:100%`); a wide table (`table-layout:fixed` + `overflow-wrap:anywhere` on small breakpoints); an image (`max-width:100%; height:auto`).

### 2. Link + image integrity, meta, noindex

Run `node scripts/audit-build.mjs <output-dir>`. Reports: broken internal links, broken local image sources, missing or duplicate `<title>` / meta description, titles over 60 chars, descriptions over 160, and any pages carrying `noindex`.

### 3. Sitemap + robots + structured data

- Sitemap exists, regenerates on every build, excludes the 404, includes all real pages.
- `robots.txt` allows crawl and references the sitemap.
- Each template emits JSON-LD (Organization + WebSite sitewide; Article / BreadcrumbList / CollectionPage / etc. per type). Confirm present and well-formed; recommend the user run Google's Rich Results Test for formal validation.

### 4. Launch assets

- **Favicon:** the mark must sit INSIDE the inscribed circle, because search engines and mobile OSes crop favicons to a circle. If the mark reaches the corners, pad it (scale the artwork to ~66% of the canvas, centered). A legacy `.ico` may stay full-bleed (it only renders in square contexts).
- **Open Graph image:** 1200x630, but keep the logo, headline, and key text within the central 1:1 square (about 580 to 600px wide) so a square crop never cuts content. Background can be full-bleed.
- **Custom 404 page** exists, branded, links back home (not the host's default).
- Favicon + OG files referenced in `<head>` actually exist on disk.

### 5. Placeholder / dev-speak scan

Grep the built HTML for internal or placeholder copy that should never ship:
```
grep -rilE "lorem|coming soon|content pass|placeholder|TODO|FIXME|arrives in|ships shortly|playbook coming|in the next content" <output-dir>
```
Triage every hit: some ("coming soon" on a roadmap feature) are legitimate; internal-note phrasing ("arrives in the next content pass") is not.

### 6. Old-sitemap parity (rebuilds / migrations only)

Run `node scripts/sitemap-parity.mjs <old-sitemap-url> <output-dir> [redirects.json]`. For every old URL it reports: exists in the new build / covered by a redirect / MISSING. Any MISSING page will 404 after cutover and lose its rankings: add a 301 (or recreate the page) before going live. Obsolete non-page files (e.g. a `.kml`) are acceptable drops, but flag them.

### 7. Interaction, forms & accessibility hygiene

A static-build pass plus a quick code grep over the source/components. These are common, shippable defects most builds get wrong.

**Source and credit:** the checks in this section are adapted from Vercel's publicly published Web Interface Guidelines; the credit for them belongs to Vercel, not to this skill. Keep the principle behind each check; the stack-specific library names are examples, not requirements.

**Forms** (the highest-value group):
- Submit button stays ENABLED until the request starts; do not pre-disable it. Show a spinner in-flight and use an idempotency key. Pre-disabled submits hide validation.
- On submit, focus the first error; show errors inline next to their field.
- Never block paste (`onPaste` + `preventDefault`). Allow pasting OTP codes; trim trailing whitespace.
- `spellcheck={false}` on email/code/username fields.
- `autocomplete="off"` (or `one-time-code`) on non-auth fields so password managers do not trigger on a "Search" box.
- Mobile `<input>` font-size >= 16px (stops iOS auto-zoom).
- Warn before navigating away with unsaved changes.

**Images / CLS**: every `<img>` has explicit `width`+`height`; below-fold `loading="lazy"`; above-fold `fetchpriority="high"`.

**Focus**: flag any `outline: none` without a `:focus-visible` replacement. Prefer `:focus-visible` over `:focus`.

**Animation**: flag `transition: all` (list properties explicitly); flag animations missing `prefers-reduced-motion`; animate `transform`/`opacity` only.

**Touch / scroll**: `overscroll-behavior: contain` on modals/drawers; `touch-action: manipulation` on tap controls.

**Dark mode**: `color-scheme` set on `<html>`; `<meta name="theme-color">` present and matching the background; explicit `background-color`+`color` on native `<select>` (Windows dark-mode bug).

**i18n**: dates/numbers via `Intl.*`, not hardcoded; wrap brand/code tokens in `translate="no"`.

**Typography lint**: `...` -> `…`; straight quotes -> curly; `font-variant-numeric: tabular-nums` on aligned number columns; `text-wrap: balance` on headings.

**State**: destructive actions need a confirm modal or undo window, never immediate; reflect filter/tab/pagination state in the URL.

## Output: verdict table

Lead with a one-line verdict (launch-ready or not). Then a scannable table: `Area | Status | Notes`, using checkmarks for good, an hourglass for items pending a user decision or action, and a warning sign for items not measured. Be explicit about what was NOT measured rather than implying full coverage.

## What this skill does NOT cover

Runtime performance (for a local page-speed optimization loop run a dedicated page-speed pass; for field numbers run Lighthouse, PageSpeed Insights, WebPageTest, or an equivalent against the live domain after deploy, since local numbers do not reflect the CDN), formal WCAG accessibility (section 7 covers common hygiene, not a full audit), and live form-submission testing. Name these as gaps and offer a dedicated pass if the user wants them.
