---
name: replit-quality
description: Quality, UX/QA, and debugging reference for Replit React + Vite + Express apps. Covers two needs. Pre-ship UX behavior rules and a pre-delivery QA checklist for websites built in Replit (navigation, loading, mobile, forms, links, accessibility, visual consistency, deployment). And post-ship debugging patterns and fixes (SSR/hydration, meta tags, server stability, build/deploy, CSS, layout, routing, performance, email, PDF, image handling, OG/social, analytics, database, component patterns). Living document updated as new Replit-specific issues surface. Invoke when building or QAing a Replit website, running a pre-delivery checklist, or debugging a recurring bug in a React + Vite + Express Replit project.
user-invocable: true
argument-hint: [site/page you are building, or bug you are debugging]
---

Two halves. Pre-ship UX & QA validation comes first: the UX behavior rules and the pre-delivery checklist you run before presenting any finished Replit website. Debugging-by-pattern comes second: a reference of recurring bugs, root causes, and fixes across React + Vite + Express Replit projects, organized by category. Use the first half while building and before delivery. Use the second half when something breaks.

For any new content-heavy, SEO-focused website on Replit, the recommended stack is React + Vite + TypeScript + Tailwind. Write a short project-specific stack-and-SEO document up front (the chosen stack, the SEO infrastructure the site needs, and the performance targets) and attach it to the first Replit prompt, so the build starts from your standards rather than the platform's defaults.

---

## Pre-ship UX & QA checklist

### Website UX Rules

These are the UX rules for the website. Follow all "Always Apply" rules on every page. Follow "Check When Relevant" rules when the context applies.

If additional instruction files are provided for design, SEO, or conversion, follow those as well. If no additional files are provided, this section is the complete set of rules.

---

### Always Apply: Navigation Behavior

- Every page navigation scrolls to the top of the new page. Users expect to start at the top, not land halfway down.
- The back button works as expected. It returns to the previous page, not to some internal app state.
- Every internal link can be opened in a new tab (right-click > open in new tab must work). No JavaScript-only navigation that blocks this.
- Every page has a real, shareable URL. Copying the URL and pasting it in a new browser loads that exact page. It must not redirect to the homepage.
- Refreshing any page reloads that same page. No blank screen, no 404, no redirect to the homepage.
- The navigation menu highlights which page the user is currently on.
- All links in the nav point to real, working pages. No dead links.

---

### Always Apply: Page Loading

- No blank white screens while content loads. Show a loading indicator or skeleton.
- The page should not visually jump or shift as content loads in. No layout shift.
- Images should not cause the page to reflow when they finish loading. Space must be reserved for them.
- If a page has no content (empty list, no results), show a clear message. Never render an empty container with nothing in it.

---

### Always Apply: Mobile Behavior

- Every page works on a phone screen (375px width minimum).
- Tap targets (buttons, links) are large enough to tap with a thumb.
- No horizontal scrolling on any page.
- Forms have full-width inputs on mobile.
- Navigation collapses to a menu (hamburger or similar) on small screens.
- The keyboard does not cover input fields when typing on mobile. The page scrolls so the active field is visible.

---

### Always Apply: Forms

- Every form field has a visible label. Placeholder text alone is not enough.
- After submitting a form, the user sees clear confirmation it worked.
- If submission fails, the user sees an error message explaining what to do next.
- Required fields are visually marked before the user tries to submit.
- The submit button is disabled while the form is submitting. No double submissions.
- Email fields bring up the email keyboard on mobile. Phone fields bring up the number pad.

---

### Always Apply: Links and Buttons

- External links open in a new tab.
- Internal links navigate within the site without a full page reload (unless necessary).
- Buttons look different from links. If it navigates somewhere, make it a link. If it performs an action, make it a button.
- No dead links. Every link goes somewhere real.
- No orphan pages. Every page is reachable from the navigation or from another page.

---

### Always Apply: Visual Consistency

- Company name, phone number, email, and address are identical everywhere they appear across the site.
- No placeholder or dummy content anywhere. No "Lorem ipsum", no "Your Company", no example@email.com.
- Favicon is set. The browser tab shows your icon, not the default Replit icon.
- Page titles are set and descriptive. Each page shows a relevant title in the browser tab.

---

### Check When Relevant: Images

- All images have alt text describing what the image shows.
- Images below the fold load lazily so they do not slow down the initial page load.
- The main hero image loads immediately, not lazily.
- If separate SEO rules are provided, defer to those for full image optimisation.

---

### Check When Relevant: Accessibility

- All interactive elements (buttons, links, form fields) are reachable using the Tab key.
- Users can see which element is currently focused (visible outline or highlight).
- Animations respect the user's "reduced motion" system setting.
- Text is readable against its background. Sufficient colour contrast.

---

### Check When Relevant: Third-Party Tools

- Analytics, chat widgets, or booking tools should not slow down the page load. They load after the main content.
- No more than 3 third-party scripts on any page.
- If a third-party script breaks, the rest of the site still works normally.

---

### Check When Relevant: Multi-Page Content

- When a site has many similar pages (services, locations, team members), they should all use the same layout template.
- Adding a new page of the same type should not require building it from scratch. New page = new content entry.
- If separate SEO rules are provided, defer to those for structured data and meta tags on these pages.

---

### Deployment

- Test the live deployed URL separately from the development preview. They can behave differently.
- Custom domain: set up in Replit deployment settings with a CNAME DNS record pointing to the Replit URL.
- Run the full pre-delivery checklist before deploying, not after.

---

### Pre-Delivery Checklist

Run this before presenting any finished work.

**Navigation and routing:**
- [ ] Every link works and goes to the right page
- [ ] Every page scrolls to the top when navigated to
- [ ] Every page can be opened in a new tab
- [ ] Every page has a shareable URL that loads correctly in a new browser
- [ ] Refreshing any page reloads that page correctly
- [ ] Back button returns to the previous page
- [ ] Navigation menu includes all pages, no orphans
- [ ] Current page is highlighted in the nav

**Content and visuals:**
- [ ] No placeholder or dummy content anywhere
- [ ] Company details consistent across all pages
- [ ] Favicon set (not the default Replit icon)
- [ ] Page titles set and descriptive in browser tab
- [ ] OG tags set (title, description, image) for social sharing
- [ ] All images have alt text

**Mobile:**
- [ ] Every page tested at 375px width
- [ ] No horizontal scrolling
- [ ] All tap targets are thumb-sized
- [ ] Forms usable on mobile

**Forms:**
- [ ] Forms submit successfully with visible confirmation
- [ ] Error messages show on failed submissions
- [ ] Required fields are marked
- [ ] No double-submit possible

**Performance and loading:**
- [ ] No blank white screens while loading
- [ ] No visible layout shift as content loads
- [ ] Page loads in under 3 seconds on mobile
- [ ] Third-party scripts do not block page load

**Error handling:**
- [ ] Unknown URLs show a 404 page (not a blank screen)
- [ ] 404 page has a link back to the homepage

**Deployed site:**
- [ ] Deployed URL tested independently from dev preview
- [ ] No console errors on any page

---

### Known Issues Log

Log Replit-specific issues here as they surface. Reference these when starting new projects to avoid repeating the same mistakes.

#### Issue: Pages do not scroll to top on navigation
**Symptom:** User clicks a link to a new page but lands partway down the page instead of at the top.
**Cause:** Replit web apps often use single-page app (SPA) routing. SPAs do not automatically scroll to the top when navigating between views.
**Fix:** Tell Replit Agent: "Add a global scroll-to-top handler that fires on every route change. Every page navigation must scroll the viewport to the top."

#### Issue: Internal links cannot be opened in a new tab
**Symptom:** Right-clicking a link and selecting "Open in new tab" either does nothing or opens a broken page.
**Cause:** SPA navigation often uses JavaScript click handlers instead of real anchor tags with href attributes. Without a real href, the browser cannot open the link in a new tab.
**Fix:** Tell Replit Agent: "All internal links must use real anchor tags with proper href attributes pointing to the actual URL path. Navigation should work both as an in-app transition and as a standard link that can be opened in a new tab."

---

## Debugging patterns

Reference for recurring bugs, root causes, and fixes across React + Vite + Express projects built in Replit. Organized by pattern category. Each entry: symptom, root cause, fix, prevention.

Upload this file into new Replit projects to avoid repeat troubleshooting.

Two scope notes, so you match entries correctly. First, most entries below are React + Vite + Express bugs that happen to have been catalogued on this platform: an entry that does not name the platform in its symptom, cause, or fix applies to the same stack on any host, so do not skip it because the project is hosted elsewhere. The genuinely platform-specific ones say so explicitly (platform-injected component customizations, deployment settings, prompts written for the platform's build agent). Second, where a symptom names a specific audit tool, read it as any equivalent audit: the same flag from PageSpeed Insights, WebPageTest, or a browser's built-in audit points at the same entry. Entries that name a specific library in their title or checklist item (the router, the ORM, the component library, the query library) are scoped to that library on purpose, and the alternative behaves differently, so check which one the project uses before applying the fix.

---

### 1. SSR & Hydration

#### 1.1 Browser API in useState default

- **Symptom:** Hydration mismatch warning. Server HTML differs from client HTML. Form fields pre-filled on client but empty in page source.
- **Root cause:** `localStorage.getItem()` or `sessionStorage.getItem()` used as `useState` default value. Server returns empty/undefined, client returns stored value.
- **Fix:** Use empty defaults + `useEffect` to populate after mount:
  ```tsx
  const [value, setValue] = useState("");
  useEffect(() => {
    const stored = localStorage.getItem("key");
    if (stored) setValue(stored);
  }, []);
  ```
- **Prevention:** Never use browser storage in `useState` defaults. Always start with SSR-safe values (`""`, `false`, `[]`, `{}`).

#### 1.2 Browser API in react-hook-form defaultValues

- **Symptom:** Same hydration mismatch but on forms using `react-hook-form`.
- **Root cause:** `defaultValues` populated from `localStorage` during render.
- **Fix:** Empty defaults + `useEffect` with `form.setValue()`:
  ```tsx
  const form = useForm({ defaultValues: { name: "", email: "" } });
  useEffect(() => {
    try {
      const saved = JSON.parse(localStorage.getItem("saved") || "{}");
      if (saved.name) form.setValue("name", saved.name);
    } catch {}
  }, []);
  ```
- **Prevention:** Same rule. Never derive `defaultValues` from browser storage.

#### 1.3 Browser API at module level

- **Symptom:** `ReferenceError: sessionStorage is not defined` or `window is not defined` during SSR. Crash happens on import, not on render.
- **Root cause:** Top-level module code runs during SSR import:
  ```tsx
  // Runs on import, crashes SSR
  sessionStorage.setItem("key", window.location.href);
  ```
- **Fix:** Guard with `typeof window`:
  ```tsx
  if (typeof window !== "undefined") {
    sessionStorage.setItem("key", window.location.href);
  }
  ```
- **Prevention:** Every module-level statement touching `window`, `document`, `localStorage`, `sessionStorage`, or `navigator` needs a `typeof window !== "undefined"` guard. Better: move to `useEffect`.

#### 1.4 Browser API in utility functions

- **Symptom:** SSR crash from a utility file in `lib/` or `hooks/`. The function is only called from `useEffect`, but the module is still evaluated during SSR.
- **Root cause:** Helper functions access browser APIs without guards. Module evaluation runs all top-level code including function definitions that reference globals.
- **Fix:** Every exported function that touches browser APIs gets its own guard:
  ```tsx
  export function getPageUrl() {
    if (typeof window === "undefined") return "";
    return window.location.href;
  }
  ```
- **Prevention:** Even if a function is only called client-side, if its module is imported during SSR, all code in that module executes. Guard every function independently.

#### 1.5 Browser-only library static import

- **Symptom:** `ReferenceError: window is not defined` during SSR. The crash comes from a third-party library, not your code.
- **Root cause:** Library accesses `window` or `document` at import time. Static `import` evaluates the library during SSR.
- **Fix:** Dynamic import inside the function that needs it:
  ```tsx
  async function convertFile(file: File) {
    const lib = (await import("browser-only-lib")).default;
    return lib.process(file);
  }
  ```
- **Prevention:** Check any new dependency: does it reference `window`/`document` at the top level? If yes, dynamic import only.

#### 1.6 window.matchMedia in render

- **Symptom:** SSR crash from `useReducedMotion()` (framer-motion) or any hook that calls `window.matchMedia` during render.
- **Root cause:** `window.matchMedia` does not exist on the server.
- **Fix:** Custom hydration-safe hook:
  ```tsx
  const [prefersReduced, setPrefersReduced] = useState(false);
  useEffect(() => {
    const mql = window.matchMedia("(prefers-reduced-motion: reduce)");
    setPrefersReduced(mql.matches);
    const handler = (e: MediaQueryListEvent) => setPrefersReduced(e.matches);
    mql.addEventListener("change", handler);
    return () => mql.removeEventListener("change", handler);
  }, []);
  ```
- **Prevention:** Never use `useReducedMotion()` from framer-motion or any library hook that accesses `window.matchMedia` during render. Write your own with `useState(false)` + `useEffect`.

#### 1.7 Provider tree mismatch

- **Symptom:** "Invalid hook call" errors during SSR or hydration. Hooks crash unpredictably.
- **Root cause:** SSR entry wraps app in providers (Router, HelmetProvider, QueryClientProvider) but client entry has different providers or different order.
- **Fix:** Make SSR and client provider trees identical in structure and order.
- **Prevention:** Keep a single shared `AppProviders` wrapper or audit both entry files after any provider change.

#### 1.8 Shared QueryClient/context across SSR requests

- **Symptom:** Data from one user's request leaks into another user's response. Stale cache between requests.
- **Root cause:** `QueryClient` or `HelmetProvider` context is a module-level singleton, shared across all SSR requests.
- **Fix:** Create fresh instances per request. Call `queryClient.clear()` on stream end.
- **Prevention:** Never use module-level singletons for per-request state in SSR.

#### 1.9 SSR grep checks

Run these to find unsafe patterns:
```bash
# localStorage/sessionStorage outside useEffect
grep -rn "localStorage\.\|sessionStorage\." src/ --include="*.ts" --include="*.tsx" | grep -v "useEffect\|// SSR\|typeof window"

# window/document at module level
grep -rn "^window\.\|^document\.\|= window\.\|= document\." src/ --include="*.ts" --include="*.tsx"

# Static imports of known browser-only libraries
grep -rn "^import.*heic2any" src/ --include="*.ts" --include="*.tsx"
```

---

### 2. Meta Tags & SEO

#### 2.1 Meta tags missing from streamed HTML

- **Symptom:** Page source shows default/empty title and description. Crawlers see wrong metadata.
- **Root cause:** Streaming SSR (`onShellReady`) sends `<head>` before lazy-loaded page components can set their Helmet tags.
- **Fix:** Resolve metadata server-side before the stream starts. Create a route metadata map that injects `<title>`, `<meta>`, `<link rel="canonical">` into the HTML template before React renders.
- **Prevention:** Never rely solely on React components (Helmet or otherwise) to set `<head>` tags in streaming SSR. Server-side metadata injection is the only reliable approach.

#### 2.2 Dual-source meta drift (SSR vs client)

- **Symptom:** JS-executing crawlers see different title/description than what's in the initial HTML. Search Console shows conflicting metadata.
- **Root cause:** Two sources of SEO metadata: server-side map (used during SSG/SSR) and client-side component props (used during SPA navigation). When they diverge, client JS overwrites correct SSR values.
- **Fix:** Single source of truth. Client-side SEO component should read from the same metadata map used by the server. For dynamic pages, import and use the shared lookup function.
- **Prevention:** When adding a new page, add metadata to the server-side map first, then use the same values in the client component.

#### 2.3 Meta tags stale after SPA navigation

- **Symptom:** Navigate between pages using client-side links. Title, description, canonical, OG tags still show previous page's values.
- **Root cause:** `react-helmet-async` v3+ uses `requestAnimationFrame` for deferred DOM updates. This fails silently with React Suspense + lazy-loaded routes.
- **Fix:** Replace Helmet with direct DOM manipulation via `useEffect`:
  ```tsx
  useEffect(() => {
    document.title = title;
    document.querySelector('meta[property="og:title"]')?.setAttribute("content", title);
    // ... update all managed meta tags
  }, [title, description, path]);
  return null;
  ```
- **Prevention:** Never use `react-helmet-async` with Suspense + lazy routes. Direct DOM manipulation is the only reliable approach.

#### 2.4 Missing page in metadata map

- **Symptom:** Pre-render build crashes with "No metadata defined for route." Or page shows default homepage title.
- **Root cause:** New page added to router but not to the metadata map.
- **Fix:** Add entry to the metadata map for every routable page.
- **Prevention:** New page checklist: (1) create component, (2) add route, (3) add metadata, (4) test pre-render.

#### 2.5 Unreplaced template tokens in HTML

- **Symptom:** Pages show raw `__META_TITLE__` tokens instead of actual values.
- **Root cause:** `express.static` auto-serves `index.html` before the catch-all route can inject meta.
- **Fix:** `express.static(dir, { index: false, redirect: false })` prevents auto-serving index.html.
- **Prevention:** Always disable index serving on the static middleware.

#### 2.6 Duplicate JSON-LD from SSR + client

- **Symptom:** Page source shows duplicate `<script type="application/ld+json">` blocks.
- **Root cause:** Using JSX `<script>` tags or Helmet to inject JSON-LD. Server renders one, client renders another after hydration.
- **Fix:** Client-side JSON-LD via `useEffect` + `document.createElement`:
  ```tsx
  useEffect(() => {
    const script = document.createElement("script");
    script.type = "application/ld+json";
    script.textContent = JSON.stringify(data);
    document.head.appendChild(script);
    return () => { script.parentNode?.removeChild(script); };
  }, [data]);
  return null;
  ```
  Server-side JSON-LD injected separately by the metadata resolver.
- **Prevention:** JSON-LD in streaming SSR must use `useEffect` on client, separate injection on server. Never use JSX `<script>` tags for structured data.

#### 2.7 Sitemap lastmod using current date

- **Symptom:** Search engine re-crawls unchanged pages excessively.
- **Root cause:** `lastmod` set to `new Date()`, making every page appear freshly modified on each crawl.
- **Fix:** Hardcode `lastmod` per page. Update only when content actually changes.
- **Prevention:** Never use dynamic dates in sitemaps.

#### 2.8 robots.txt invalid directives

- **Symptom:** Search Console reports warnings about unrecognized directives.
- **Root cause:** Non-standard directives added. Only `User-agent`, `Disallow`, `Allow`, `Sitemap`, `Crawl-delay` are valid.
- **Fix:** Remove non-standard directives. Use HTML `<link>` tags or sitemap for other references.
- **Prevention:** Verify every robots.txt line is a standard directive before deploying.

#### 2.9 Internal pages indexed by search engines

- **Symptom:** Admin/internal pages appear in search results.
- **Root cause:** Missing `noindex` meta tag and `robots.txt` disallow.
- **Fix:** Add both: `<meta name="robots" content="noindex, nofollow" />` on the page AND `Disallow` rules in `robots.txt`.
- **Prevention:** Never rely on just one mechanism. Internal pages need both noindex and robots.txt.

#### 2.10 Canonical redirect not working

- **Symptom:** Non-canonical domains (www, replit.app subdomains) serve content instead of 301 redirecting to the canonical domain.
- **Root cause:** The non-canonical hostname is not listed in the redirect hosts configuration, or the canonical host is misconfigured.
- **Fix:** Maintain a `CANONICAL_HOST` constant and a `REDIRECT_HOSTS` list. In Express middleware, check `req.hostname` against `REDIRECT_HOSTS` and 301 redirect to `CANONICAL_HOST` with the same path.
- **Prevention:** After adding custom domains or subdomains, add all non-canonical variants to the redirect list. Test with `curl -sI https://non-canonical-domain.com/page` and verify 301 + correct Location header.

#### 2.11 SSG prerender fails or produces empty HTML

- **Symptom:** Build fails, or pre-rendered pages have empty `<div id="root"></div>` with no content.
- **Root cause:** Import error in the SSR bundle. Common causes: browser-only API used at module level, missing alias for SSR stubs, or unresolvable dependency in the SSR build.
- **Fix:** Check the SSR build output for errors. Ensure any SSR-specific stubs (e.g., Helmet noop) are aliased in the build config. Ensure no browser-only code runs at import time (see section 1).
- **Prevention:** Always check pre-render output for the expected route count with zero failures. Any missing route is a bug.

#### 2.12 JSON-LD @type doesn't support property

- **Symptom:** Search Console shows structured data errors. Properties like `aggregateRating` are flagged as unsupported.
- **Root cause:** The JSON-LD `@type` doesn't officially support the property. For example, `"PestControlService"` alone doesn't support `aggregateRating`, but `"LocalBusiness"` does.
- **Fix:** Use a dual-type array to satisfy both semantic specificity and property support:
  ```json
  "@type": ["LocalBusiness", "SpecificBusinessType"]
  ```
- **Prevention:** When adding structured data properties, verify the `@type` supports them in Google's Rich Results Test. Use dual-type arrays when needed.

#### 2.13 data-rh attribute coverage for managed meta tags

- **Symptom:** Duplicate meta tags after React hydration. Template tags and React-managed tags coexist.
- **Root cause:** Template meta tags lack a marker attribute. Client-side updater adds its own tags instead of replacing existing ones.
- **Fix:** Add a marker attribute (e.g., `data-rh="true"`) to all managed meta tags in the HTML template. Client-side updater queries and replaces tags with this marker.
- **Prevention:** Every managed meta/title/canonical tag in the template must have the marker attribute.

---

### 3. Server Stability & Lifecycle

#### 3.1 process.exit in error handlers

- **Symptom:** Server restart loop. Process dies on every minor error (CSS warnings, TypeScript issues).
- **Root cause:** Vite error handler or custom logger calls `process.exit(1)` on any error.
- **Fix:** Log the error and continue. Never call `process.exit()` in error handlers.
- **Prevention:** Grep for `process.exit` in error handlers after any Vite config change.

#### 3.2 No global error handlers

- **Symptom:** Server crashes and stays down after a transient error.
- **Root cause:** No `uncaughtException` or `unhandledRejection` handlers. One unhandled error kills the process.
- **Fix:** Add both handlers in the server entry point:
  ```tsx
  process.on("uncaughtException", (err) => { console.error("Uncaught:", err); });
  process.on("unhandledRejection", (err) => { console.error("Unhandled rejection:", err); });
  ```
- **Prevention:** Always include both handlers in server entry points.

#### 3.3 SIGHUP kills server in Replit

- **Symptom:** Server terminates unexpectedly with no error. No uncaught exception in logs.
- **Root cause:** Replit sends `SIGHUP` during environment operations. Node.js default behavior: terminate.
- **Fix:** Add empty handler: `process.on("SIGHUP", () => {});`
- **Prevention:** Always add this at the top of the server entry in Replit projects.

#### 3.4 EADDRINUSE on restart

- **Symptom:** Server fails to start after restart. Port already in use.
- **Root cause:** No graceful shutdown. Old process still holds the port.
- **Fix:** Register `SIGTERM` and `SIGINT` handlers at module top level (before any async setup). Close HTTP server, Vite dev server, and DB pool. Add force-exit timeout (5s). Use `isShuttingDown` flag to prevent double-shutdown.
- **Prevention:** Signal handlers must be registered at module top level, not inside async functions.

#### 3.5 Signal handler registered too late

- **Symptom:** Crash log shows STARTUP-STARTUP with no SHUTDOWN between. Direct `kill -TERM <pid>` works but workflow restart doesn't.
- **Root cause:** Signal handlers registered inside async IIFE, after server setup. If SIGTERM arrives during setup, it's not caught. Also, `sh -c` wrapper in workflow command swallows signals.
- **Fix:** Register handlers at module top level. Use `exec` in workflow command to eliminate shell wrapper: `NODE_ENV=development exec tsx server/index.ts`
- **Prevention:** Always register signal handlers before any async code. Always use `exec` in workflow commands.

#### 3.6 reusePort causing conflicts

- **Symptom:** Port conflicts on restart. Multiple processes bound to same port.
- **Root cause:** `reusePort: true` in Express `.listen()` allows multiple processes on same port. Previous process hasn't terminated yet.
- **Fix:** Remove `reusePort: true`.
- **Prevention:** Don't use `reusePort` in Replit projects.

#### 3.7 Memory crash from repeated ssrLoadModule

- **Symptom:** Server crashes ~20s after startup with out-of-memory.
- **Root cause:** `vite.ssrLoadModule()` called multiple times for different data files, each loading the entire module graph.
- **Fix:** Re-export all data from the SSR entry point. Call `ssrLoadModule()` once. Cache the extracted data.
- **Prevention:** One `ssrLoadModule()` call per entry point. Re-export data, don't load modules individually.

#### 3.8 Vite HMR crash loop in Replit

- **Symptom:** Site reloads every 10-20 seconds. Server restarts continuously.
- **Root cause:** Vite HMR WebSocket can't connect through Replit proxy. Needs explicit `clientPort: 443` and `protocol: "wss"`.
- **Fix:** Configure HMR for Replit proxy:
  ```tsx
  hmr: {
    server,
    path: "/vite-hmr",
    ...(isReplit ? { clientPort: 443, protocol: "wss" } : {}),
  }
  ```
- **Prevention:** Always configure HMR WebSocket settings for the Replit proxy environment.

#### 3.9 Preview pane caching

- **Symptom:** Changes deployed but Replit preview still shows old content.
- **Root cause:** Replit proxy caches aggressively. No `Cache-Control` headers in dev.
- **Fix:** Add cache-busting headers in dev mode:
  ```tsx
  if (process.env.NODE_ENV !== "production") {
    res.setHeader("Cache-Control", "no-cache, no-store, must-revalidate");
  }
  ```
- **Prevention:** Always add no-cache headers for dev/preview environments.

#### 3.10 keepAliveTimeout too low for Replit proxy

- **Symptom:** Preview says "not running" but `curl /api/health` returns 200. `[vite] connecting...` cycles in browser console.
- **Root cause:** Default `keepAliveTimeout` (5s) is too low. Replit's proxy drops idle connections, causing preview disconnects that look like crashes.
- **Fix:** Set `httpServer.keepAliveTimeout = 65000` (65 seconds) after creating the HTTP server.
- **Prevention:** Always set keepAliveTimeout above 60s in Replit projects. If preview shows "not running," check `/api/health` first before assuming a crash.

#### 3.11 Cold start slow first load

- **Symptom:** First page load after restart takes 3+ seconds.
- **Root cause:** SSR warm-up not running. Cold `ssrLoadModule()` on first request.
- **Fix:** Add SSR warm-up request after server starts. Log "SSR warm-up complete."
- **Prevention:** Always warm up SSR after server initialization.

---

### 4. Build & Deploy

#### 4.1 import.meta.url in CJS bundle

- **Symptom:** Deployment crash. `import.meta.url` is undefined.
- **Root cause:** ESM syntax in a CJS-bundled server file. `import.meta.url` doesn't exist in CommonJS.
- **Fix:** Use `process.cwd()` for file path resolution. Never use `fileURLToPath()` either.
- **Prevention:** No `import.meta.url` or `fileURLToPath()` in server code that gets bundled as CJS.

#### 4.2 Deep imports from lucide-react

- **Symptom:** esbuild crashes during bundling. Error references `lucide-react/dist/esm/icons/...`.
- **Root cause:** Deep/internal import paths are not stable across versions.
- **Fix:** Always use named imports from package root: `import { Icon } from "lucide-react"`.
- **Prevention:** Never import from sub-paths of `lucide-react`.

#### 4.3 Transient esbuild service crash

- **Symptom:** Build fails with cryptic esbuild errors. No code changes caused it.
- **Root cause:** esbuild's background service enters a corrupted state in containerized environments.
- **Fix:** Restart the workflow. No code changes needed.
- **Prevention:** If esbuild errors appear without code changes, restart before debugging.

#### 4.4 Deployment target misconfigured

- **Symptom:** API endpoints return 404 in production. Static pages work but dynamic routes fail.
- **Root cause:** `.replit` has `deploymentTarget = "static"` but project needs `"autoscale"` for server routes.
- **Fix:** Set `deploymentTarget = "autoscale"`, add `run` command pointing to server entry, set `mockupState = "FULLSTACK"`.
- **Prevention:** When adding server-side functionality, update `.replit` deployment config.

#### 4.5 Production-only layout bugs

- **Symptom:** Components work in dev but break in production SSG builds. Navbar overlap, missing styles.
- **Root cause:** SSG rendering order, CSS extraction, and chunk splitting differ from dev server. Styles in lazy-loaded chunks may not be in initial HTML.
- **Fix:** Always test production builds locally before deploying:
  ```bash
  npm run build && node dist/index.cjs
  ```
- **Prevention:** Run production build check for every PR touching layout, navigation, or global styles.

#### 4.6 CSS plugin breaking SSG

- **Symptom:** Flash of unstyled HTML (FOUC) on page load. Raw HTML visible before styles.
- **Root cause:** A CSS deferral plugin converts `<link rel="stylesheet">` to `<link rel="preload" onload="...">`. Correct for SPAs, wrong for SSG where HTML is visible before JS runs.
- **Fix:** Remove any CSS deferral plugin. Standard blocking `<link rel="stylesheet">` is correct for SSG.
- **Prevention:** Never defer CSS loading in SSG projects.

---

### 5. CSS & Styling

#### 5.1 shadcn/ui Button visibility

- **Symptom:** Buttons invisible, unstyled, or text not visible.
- **Root cause:** shadcn/ui `Button` default variant styles override Tailwind utility classes.
- **Fix:** Use inline `style` for color control, or `!important` Tailwind prefix:
  ```tsx
  <Button style={{ background: "#000", color: "#fff" }}>Click</Button>
  // or
  <Button className="!bg-black !text-white">Click</Button>
  ```
- **Prevention:** Always verify Button visibility after adding. Prefer inline styles for explicit color control on shadcn/ui Buttons.

#### 5.2 Replit-injected component overrides

- **Symptom:** Buttons have unexpected hover effects, wrong borders, non-standard shadows.
- **Root cause:** Replit injects customizations (marked with `// @replit` comments) into shadcn/ui components that conflict with your design system.
- **Fix:** Review and clean up scaffolded components. Remove `// @replit` comments and their associated custom classes.
- **Prevention:** After scaffolding shadcn/ui components, always review for platform-injected customizations.

#### 5.3 Text gradient produces invisible text

- **Symptom:** Heading text disappears against the background.
- **Root cause:** `text-gradient` CSS class produces text color that matches background.
- **Fix:** Use explicit color classes instead of gradient classes for headings.
- **Prevention:** Never use text gradient classes on headings without verifying contrast.

#### 5.4 Sticky nav disappears on scroll

- **Symptom:** Navigation bar scrolls out of view on long pages.
- **Root cause:** `sticky top-0` positioning fails in some layouts/browsers.
- **Fix:** Use `fixed top-0 left-0 right-0` with a spacer div using `ResizeObserver`:
  ```tsx
  <div style={{ height: headerHeight }} aria-hidden="true" />
  ```
- **Prevention:** Always use `fixed` positioning for persistent nav bars. Always pair with a dynamic spacer.

#### 5.5 Design token drift (color inconsistency)

- **Symptom:** Buttons, links, accents use slightly different shades across pages.
- **Root cause:** Colors hardcoded in components instead of using CSS custom properties.
- **Fix:** Define brand colors as CSS custom properties. All components reference variables, never hardcode hex/hsl.
- **Prevention:** When adding any color, use the CSS variable. Never pick from a color picker or let AI suggest a "similar" shade.

#### 5.6 clip-path for border effects

- **Symptom:** Border cutouts render incorrectly across browsers and zoom levels.
- **Root cause:** `clip-path: polygon(...)` clips the entire element including border, making precise border-only cutouts unreliable.
- **Fix:** Use pseudo-elements with `box-shadow` tricks instead of `clip-path` for border effects. Add mobile breakpoint fallback.
- **Prevention:** Avoid `clip-path` for border-only visual effects.

#### 5.7 WCAG AA contrast on muted text

- **Symptom:** Lighthouse flags low-contrast text.
- **Root cause:** Opacity modifiers on already-muted text colors (e.g., `text-muted-foreground/80`) drop below 4.5:1 contrast ratio.
- **Fix:** Use muted text colors at full opacity. Never append opacity modifiers.
- **Prevention:** If text needs to be more subtle, use smaller font size or lighter weight, not reduced opacity.

#### 5.8 Grid content not vertically centered

- **Symptom:** Empty vertical space in two-column grid. One column's content is shorter and sits at the top, leaving a gap at the bottom.
- **Root cause:** Grid uses `items-start` (or default alignment) instead of `items-center`.
- **Fix:** Change `items-start` to `items-center` on the grid container.
- **Prevention:** When creating two-column grids where columns may have different heights, use `items-center`.

#### 5.9 Section visual separation using borders

- **Symptom:** Hard horizontal lines between page sections. Sections look boxy and rigid.
- **Root cause:** Using `border-y`, `border-b`, or `border-t` on `<section>` elements instead of alternating backgrounds.
- **Fix:** Remove border classes from sections. Alternate between two background colors (e.g., white and light grey) for visual separation.
- **Prevention:** Never use border classes on sections for visual separation. Use alternating backgrounds.

#### 5.10 Font preload / @font-face mismatch

- **Symptom:** PageSpeed flags "unused preload" for fonts.
- **Root cause:** `<link rel="preload" as="font">` exists but no matching `@font-face` in critical CSS.
- **Fix:** Every preloaded font must have a corresponding inline `@font-face` declaration.
- **Prevention:** When adding/removing font weights, update both preload tags and `@font-face` together.

---

### 6. Layout & Mobile

#### 6.1 Flex overflow on metadata rows

- **Symptom:** On mobile, date lines, CTA blocks, or horizontal metadata rows have text squeezed, overflowing, or overlapping.
- **Root cause:** `flex items-center gap-4` without responsive stacking. Flex items compress instead of wrapping.
- **Fix:** Always use responsive stacking:
  ```
  flex flex-col sm:flex-row sm:items-center gap-1 sm:gap-4
  ```
  For pipe separators, hide on mobile: `<span className="hidden sm:inline">|</span>`
- **Prevention:** Every flex row with variable-length text content must use `flex-col sm:flex-row`. Never use bare `flex items-center` for content rows.

#### 6.2 Footer link columns misaligned on mobile

- **Symptom:** Footer link columns have each link individually centered, creating jagged appearance.
- **Root cause:** Grid cells center content but links center independently without an inner wrapper.
- **Fix:** Wrap links in inner div with `flex flex-col items-start`. Outer grid cell centers the block, inner div left-aligns links.
- **Prevention:** Always test footer at 375px width.

#### 6.3 Text overflow on mobile

- **Symptom:** Text extends past screen edge or causes horizontal scrolling.
- **Root cause:** Fixed-width elements (code blocks), long unbroken strings, or padding pushing past container bounds.
- **Fix:** Add `overflow-wrap: break-word` to body containers, `overflow-x: auto` to code blocks, `max-w-full` and `truncate` for navigation links.
- **Prevention:** Test all content pages at 375px width.

#### 6.4 Animated elements causing overflow

- **Symptom:** Horizontal scrollbar on pages with CSS animations.
- **Root cause:** `transform: scale()` on absolute elements overflows their parent container.
- **Fix:** Sized parent container with `overflow-hidden`.
- **Prevention:** Always contain animated elements within sized parents with overflow hidden.

#### 6.5 Embedded component wrapper conflict

- **Symptom:** Double card/border effect when a form component is embedded inside a card.
- **Root cause:** Component renders its own card wrapper. When placed inside another card, both wrappers are visible.
- **Fix:** Accept a `variant` prop. Use `"embedded"` to skip the wrapper when inside another card.
- **Prevention:** Components used in multiple contexts should accept a variant prop for wrapper styling.

#### 6.6 Content width drift between pages

- **Symptom:** Content appears shifted or different width across pages.
- **Root cause:** Inconsistent container widths (`max-w-7xl` vs `max-w-6xl`), missing padding, or nested containers both applying `max-w-*`.
- **Fix:** Use a shared layout component with standardized container and padding.
- **Prevention:** Every new page must use the shared layout container.

#### 6.7 Touch target vs parent inflation

- **Symptom:** After fixing Lighthouse touch target audit (48px minimum), parent container looks bloated.
- **Root cause:** Adding `min-h-12` to small elements increases parent height combined with existing padding.
- **Fix:** Keep `min-h-12` on the interactive element but reduce parent padding to compensate.
- **Prevention:** After adding touch target sizing, check parent container visual proportions.

---

### 7. Navigation & Routing

#### 7.1 Wouter Link uses href, not to

- **Symptom:** Links don't navigate, do nothing, or cause full page reload.
- **Root cause:** Wouter's `<Link>` uses `href` (not `to` like React Router). `<Link to="/blog">` silently fails.
- **Fix:** Always use `href`:
  ```tsx
  // WRONG
  <Link to="/blog">Blog</Link>
  // CORRECT
  <Link href="/blog">Blog</Link>
  ```
- **Prevention:** Search for `<Link to=` in the codebase. Must return zero results. This is the #1 AI-generated mistake with Wouter.

#### 7.2 Nested anchor tags from Link wrapping <a>

- **Symptom:** Console warnings about nested `<a>` elements. Links behave unpredictably.
- **Root cause:** Wouter's `<Link>` renders as `<a>`. Wrapping it around another `<a>` creates invalid `<a><a>...</a></a>`.
- **Fix:** Pass className directly to Link:
  ```tsx
  // WRONG
  <Link href="/about"><a className="hover:text-primary">About</a></Link>
  // CORRECT
  <Link href="/about" className="hover:text-primary">About</Link>
  ```
- **Prevention:** Never wrap `<Link>` around an `<a>` tag. Search for `<Link.*><a` patterns.

#### 7.3 Navigation items as buttons

- **Symptom:** Right-click "Open in new tab" doesn't work on nav items. Middle-click does nothing.
- **Root cause:** Nav items implemented as `<button>` with `onClick` navigation instead of `<Link>` or `<a>`.
- **Fix:** Use `<Link>` or `<a>` for all navigable items.
- **Prevention:** Navigable items must always be link elements, never buttons.

#### 7.4 Broken internal links after route rename

- **Symptom:** Links lead to 404 or wrong page.
- **Root cause:** Link `href` doesn't match the registered route path after a rename.
- **Fix:** Search all files for old path and update every reference. Verify labels match page headings.
- **Prevention:** When renaming routes, search all files for the old path.

---

### 8. Performance

#### 8.1 LCP regression from CSS background-image

- **Symptom:** Lighthouse LCP > 4s on hero sections.
- **Root cause:** CSS `background-image` is not discoverable by the browser's preload scanner. Only starts loading after CSSOM.
- **Fix:** Replace with `<img fetchpriority="high">` + `<link rel="preload" as="image">`:
  ```tsx
  <img
    src={heroImage}
    alt={altText}
    fetchPriority="high"
    width={1920}
    height={1080}
    className="absolute inset-0 w-full h-full object-cover"
  />
  ```
- **Prevention:** LCP images must use `<img>` tags with `fetchpriority="high"`, never CSS `background-image`.

#### 8.2 CLS from hero image load

- **Symptom:** Layout shifts when hero image loads, pushing content down.
- **Root cause:** No reserved space for the image. No explicit `width`/`height` attributes.
- **Fix:** Explicit `width` and `height` attributes. Absolute positioning within a container with `min-h-[...]`.
- **Prevention:** Hero images need explicit dimensions + absolute positioning within a known-height container.

#### 8.3 Hero image not loading on first visit

- **Symptom:** Hero shows solid color on first visit, normal on refresh.
- **Root cause:** Image `load` event fires before React attaches the handler. `loaded` stays false.
- **Fix:** Check `img.complete` after mount:
  ```tsx
  useEffect(() => {
    const img = imgRef.current;
    if (img && img.complete && img.naturalWidth > 0) {
      setLoaded(true);
    }
  }, [src]);
  ```
- **Prevention:** Always check `img.complete && img.naturalWidth > 0` in a `useEffect` for fade-in patterns.

#### 8.4 Hero image alt text gaps

- **Symptom:** Lighthouse and SEO audits flag hero images with missing or generic alt text (e.g., empty `alt=""` or `alt="hero image"`).
- **Root cause:** When migrating from CSS `background-image` to `<img>` tags (see 8.1), alt text is omitted or set to meaningless placeholders.
- **Fix:** Each page passes a descriptive `heroImageAlt` prop. Use a fallback derived from the page title: `alt={heroImageAlt || \`${title} hero image\`}`.
- **Prevention:** Every `<img>` must have descriptive alt text. Hero images should describe the scene, not use generic text like "hero" or "banner."

#### 8.5 Auto-scroll jumping in streaming/chat components

- **Symptom:** Viewport yanks to the streaming component during output. Auto-scroll pulls the user back to the bottom when they scroll up to read earlier content.
- **Root cause:** Using `scrollIntoView()` on every update, or unconditionally setting `scrollTop = scrollHeight`.
- **Fix:** Scroll-only-if-at-bottom logic:
  ```tsx
  const isAtBottom = el.scrollHeight - el.scrollTop - el.clientHeight < threshold;
  if (isAtBottom) {
    el.scrollTop = el.scrollHeight;
  }
  ```
  Never use `scrollIntoView()` for streaming output. Use explicit height constraints on the container.
- **Prevention:** Any streaming/auto-updating component must check scroll position before auto-scrolling. User manual scroll up = stop auto-scrolling.

#### 8.6 Logo visibility across dark/light themes

- **Symptom:** Logo invisible or barely visible in one theme (e.g., dark logo on dark background).
- **Root cause:** Applying blanket `invert dark:invert-0` to all logos. Different logos need different strategies based on their source colors.
- **Fix:** Per-logo strategy:
  - White-on-transparent: `invert dark:invert-0`
  - Black-on-transparent: `dark:invert`
  - Colored logo: no filter (or create two variants)
  - Multi-color with transparency: `brightness`/`contrast` adjustments
- **Prevention:** Never apply a blanket invert rule to all logos. Evaluate each individually. Toggle between themes to verify visibility.

#### 8.7 Analytics blocking initial render

- **Symptom:** Third-party scripts competing with app JS, hurting PageSpeed scores.
- **Fix:** Defer loading with `requestIdleCallback` and gate to production hostname:
  ```js
  if (window.location.hostname === "yourdomain.com") {
    requestIdleCallback(() => { /* analytics bootstrap */ }, { timeout: 3000 });
  }
  ```
- **Prevention:** Never load analytics synchronously. Always hostname-gate and defer.

#### 8.8 CSP blocking third-party scripts

- **Symptom:** Console shows "Refused to load the script... violates Content-Security-Policy."
- **Root cause:** `script-src` doesn't include the third-party domain.
- **Fix:** Add required domains to CSP directives (`script-src`, `connect-src`, `img-src`, `frame-src`).
- **Prevention:** After adding third-party scripts, check browser console for CSP violations.

---

### 9. Email Delivery

#### 9.1 SendGrid CC equals TO rejection

- **Symptom:** Emails silently fail to send. No error thrown.
- **Root cause:** `cc` field contains same address as `to`. SendGrid rejects silently.
- **Fix:** Compare addresses case-insensitively before setting `cc`:
  ```tsx
  if (clientEmail.toLowerCase() !== notificationEmail.toLowerCase()) {
    msg.cc = notificationEmail;
  }
  ```
- **Prevention:** Never set `cc` to the same address as `to`.

#### 9.2 SendGrid errors silently caught

- **Symptom:** Emails fail but no useful error information logged.
- **Root cause:** Error caught but response body discarded.
- **Fix:** Log full SendGrid response body on errors. Show user-facing error messages for failures.
- **Prevention:** Never silently catch email delivery errors.

---

### 10. PDF Generation

#### 10.1 Checkbox conditional on wrong field

- **Symptom:** PDF checkbox shows wrong state.
- **Root cause:** Conditional uses wrong field name or inverted logic.
- **Fix:** Use `!!formData.correctFieldName` for each checkbox. Verify field name matches the form schema.
- **Prevention:** Verify every checkbox mapping against the actual form field names.

#### 10.2 Canvas annotations missing from exported PDF

- **Symptom:** Annotations visible on screen but missing in PDF export.
- **Root cause:** Scale mismatch between display canvas and export canvas.
- **Fix:** Apply proportional scale factors: `drawAnnotations(ctx, scaleX, scaleY)`.
- **Prevention:** When canvas display size differs from image resolution, always apply scale factors in export.

#### 10.3 Excessive blank pages

- **Symptom:** PDF has blank or mostly empty trailing pages.
- **Root cause:** Excessive `moveDown()` calls and premature page breaks from oversized `checkPageSpace()` reserves.
- **Fix:** Audit cumulative vertical spacing. Use compact photo sizes. Strip trailing empty pages before `doc.end()`.
- **Prevention:** Track cumulative vertical space. Make reserves proportional to actual remaining content.

---

### 11. Image Handling

#### 11.1 HEIC/HEIF photos from iPhones

- **Symptom:** iPhone photos show broken image icon. Compressor fails silently.
- **Root cause:** Browsers don't natively support HEIC format.
- **Fix:** Detect by both MIME type and extension (iOS sometimes reports empty MIME). Convert with dynamic import:
  ```tsx
  function isHeicFile(file: File): boolean {
    const type = file.type.toLowerCase();
    if (type === "image/heic" || type === "image/heif") return true;
    return file.name.toLowerCase().endsWith(".heic") || file.name.toLowerCase().endsWith(".heif");
  }

  async function convertHeicToJpeg(file: File): Promise<File> {
    const heic2any = (await import("heic2any")).default;
    const blob = await heic2any({ blob: file, toType: "image/jpeg", quality: 0.85 });
    const resultBlob = Array.isArray(blob) ? blob[0] : blob;
    return new File([resultBlob], file.name.replace(/\.heic$/i, ".jpg"), { type: "image/jpeg" });
  }
  ```
- **Prevention:** Always check both MIME and extension. Dynamic import for `heic2any`. Handle array-or-single return. Show progress indicator (conversion takes 1-3s).

#### 11.2 Photo annotator blank canvas

- **Symptom:** Canvas shows nothing after image selection.
- **Root cause:** Drawing before image has finished loading. `drawImage()` called before `load` event.
- **Fix:** Track image load state. Only draw after `imageReady` flag is true. Use `useLayoutEffect` for redraws.
- **Prevention:** Always check image load state before canvas operations.

#### 11.3 Upload promise hanging

- **Symptom:** Photo upload doesn't complete, no error shown.
- **Root cause:** Missing `onerror` handler on `new Image()` or `FileReader`. Promise never resolves on failure.
- **Fix:** Every `new Image()` and `FileReader` must have both `onload` and `onerror`. Add timeout (30s). Show toast on individual failures.
- **Prevention:** Every image/file promise needs error handlers and a timeout.

#### 11.4 Server-side upload validation

- **Symptom:** Malicious files accepted by upload endpoint.
- **Root cause:** Validation checks MIME type from headers only, which is spoofable.
- **Fix:** Check magic bytes: JPEG `FF D8 FF`, PNG `89 50 4E 47`, WebP `52 49 46 46...57 45 42 50`.
- **Prevention:** Always validate file content (magic bytes), not just MIME type.

---

### 12. Content & Copy

#### 12.1 Em-dash reintroduction

- **Symptom:** Em-dashes appear in content after AI edits.
- **Root cause:** AI models default to em-dashes.
- **Fix:** Replace all em-dashes with regular dashes or rewrite sentence.
- **Check:** `grep -rn '—' src/ --include='*.tsx' --include='*.ts'` must return zero.
- **Prevention:** After any AI-generated edit, run the grep check.

#### 12.2 AI filler words

- **Symptom:** Copy sounds artificial or machine-generated.
- **Fix:** Search and replace against the project's banned word list.
- **Prevention:** After generating copy, search for every filler word defined in the project's content writing guide.

#### 12.3 Banned words list scope creep

- **Symptom:** Content reads awkwardly because common words were unnecessarily banned.
- **Root cause:** Banned list grew to include normal vocabulary that humans use naturally.
- **Fix:** Test each word: "Would a professional use this in a meeting without it sounding like AI?" If yes, don't ban it.
- **Prevention:** Before adding a word to the banned list, apply the human-use test.

#### 12.4 Sensitive personal info in public content

- **Symptom:** Blog/content references private relationships or arrangements.
- **Fix:** Remove or generalize. Use generic terms instead of specific relationships.
- **Prevention:** Scan all new public content for private details before publishing.

---

### 13. Social Sharing / Open Graph

#### 13.1 Missing OG image dimensions

- **Symptom:** Social previews show no image or wrong image size. WhatsApp doesn't show preview.
- **Root cause:** Missing `og:image:width`, `og:image:height`, `og:image:type` tags.
- **Fix:** Every page needs all four OG image tags: `og:image`, `og:image:width`, `og:image:height`, `og:image:type`.
- **Prevention:** Include all four tags for every page.

#### 13.2 Page missing from SSR metadata map

- **Symptom:** Sharing a specific page shows wrong/default OG tags.
- **Root cause:** Page not in the server-side metadata map.
- **Fix:** Add entry to the metadata map.
- **Prevention:** Every public page needs a metadata entry.

#### 13.3 OG image cache not invalidated

- **Symptom:** Updated OG image but old preview still shows on social platforms.
- **Root cause:** Platform caches OG data aggressively.
- **Fix:** Use Facebook Sharing Debugger to scrape fresh. Share in a fresh WhatsApp chat (not existing thread).
- **Prevention:** After OG changes, always validate with platform debugging tools.

#### 13.4 Static file cache regex not matching new OG images

- **Symptom:** New OG image served without cache headers.
- **Root cause:** Static file cache-control regex doesn't match the new filename pattern.
- **Fix:** Update the regex to match all OG image filenames.
- **Prevention:** After adding new static assets, verify cache headers.

#### 13.5 Blog cover image asset mismatch

- **Symptom:** Blog covers show as broken images. SVG rendering errors.
- **Root cause:** File reference, actual file, and OG image type derivation are out of sync.
- **Fix:** When changing cover format, update all three: the file, the reference in data, and the OG type derivation.
- **Prevention:** After any cover change, verify all three locations match.

---

### 14. Analytics & Tracking

#### 14.1 Dev traffic in analytics

- **Symptom:** Analytics events firing in development/preview environments.
- **Root cause:** Analytics scripts load unconditionally across all environments.
- **Fix:** Gate all tracking behind production hostname check:
  ```js
  if (location.hostname === "yourdomain.com") { /* load tracking */ }
  ```
- **Prevention:** Never load analytics without a production hostname gate. If using a tag manager, gating the tag manager gates everything managed by it.

---

### 15. Database & API

#### 15.1 Raw SQL ANY() with JS arrays (Drizzle)

- **Symptom:** API 500: "requires array on right side."
- **Root cause:** Using raw SQL `ANY()` with JavaScript arrays instead of Drizzle's `inArray()`.
- **Fix:** Use `inArray()` from `drizzle-orm`.
- **Prevention:** Never use raw SQL `ANY()` with JS arrays. Search for `sql`...`ANY(` to find violations.

#### 15.2 Array column definition (Drizzle)

- **Symptom:** Column type mismatch errors.
- **Root cause:** Using `array(text())` (wrapper) instead of `text().array()` (method).
- **Fix:** Define array columns as `text().array()`.
- **Prevention:** Always use the method syntax for array columns in Drizzle.

---

### 16. Component Patterns (shadcn/ui)

#### 16.1 Missing context provider

- **Symptom:** Runtime error: "must be used within a Provider."
- **Root cause:** shadcn/ui components (Sidebar, Chart, Form, Carousel) require their context provider.
- **Fix:** Wrap in the required provider.
- **Prevention:** Check component docs for required providers before using.

#### 16.2 TanStack Query retry disabled

- **Symptom:** API requests fail immediately with no retry.
- **Root cause:** Intentional config: `retry: false` for both queries and mutations.
- **Fix:** Not a bug. Handle errors explicitly. Configure retry at query level if needed for specific cases.

---

### Pre-flight Checklists

#### New Page

- [ ] Component created
- [ ] Route registered in route manifest
- [ ] Metadata added to SEO/metadata map
- [ ] Pre-render test passes
- [ ] Internal links use correct path
- [ ] Links use `<Link href=...>`, not `<Link to=...>` or `<button>`

#### New Component with Browser APIs

- [ ] No `localStorage`/`sessionStorage` in `useState` defaults
- [ ] No `window`/`document`/`navigator` in component body
- [ ] All browser access inside `useEffect` or guarded with `typeof window === "undefined"`
- [ ] No static imports of browser-only libraries

#### Before Deploy

- [ ] Production build succeeds with all routes pre-rendered
- [ ] No unreplaced template tokens in built HTML
- [ ] Production server test: correct titles and meta tags
- [ ] Mobile layout check at 375px width
- [ ] No em-dashes in source files
- [ ] No `<Link to=` (Wouter projects)
- [ ] Analytics hostname-gated
- [ ] Signal handlers registered for graceful shutdown

#### After AI-Generated Edits

- [ ] No em-dashes introduced
- [ ] No AI filler words introduced
- [ ] No `<Link to=` (Wouter projects)
- [ ] No browser APIs in render path
- [ ] Button visibility preserved (shadcn/ui projects)
</content>
</invoke>
