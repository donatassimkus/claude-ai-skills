---
name: chrome-extension
description: Build and publish Chrome extensions. Covers Manifest V3 scaffold, popup-only architecture, icon generation, and Chrome Web Store submission with every required form field pre-filled. Use when asked to build a Chrome extension, publish to the Chrome Web Store, create a browser extension, or set up a Manifest V3 project. Also use when troubleshooting Chrome extension rejections or preparing store listing assets.
user-invocable: true
argument-hint: [what the extension should do] [optional: target website for backlink]
---

## Chrome Extension Skill

You are building a Chrome extension optimised for fast Chrome Web Store approval. The default architecture is popup-only with zero permissions, which Google approves quickly with minimal review friction.

---

## When invoked

If $ARGUMENTS describes what the extension should do: build it end-to-end and prepare all store submission materials.
If $ARGUMENTS mentions a rejection or review issue: diagnose and fix.
If no arguments: ask what the extension should do and what website it should link back to (if any).

---

## Approved Architecture (Popup-Only)

This is the pattern Google has approved without friction. Use this as the default unless the extension genuinely requires content scripts.

### File Structure (flat, all files in root)
```
extension-name/
├── manifest.json
├── popup.html
├── popup.css
├── popup.js
├── [additional .js files as needed]
├── [data files like .json]
├── icon16.png
├── icon48.png
└── icon128.png
```

No subdirectories. No nested folders. Everything in the root.

### manifest.json Template
```json
{
  "manifest_version": 3,
  "name": "Extension Name",
  "version": "1.0",
  "description": "Under 132 characters. Be specific. Include a number if possible.",
  "homepage_url": "https://your-website.com/",
  "action": {
    "default_popup": "popup.html",
    "default_icon": {
      "16": "icon16.png",
      "48": "icon48.png",
      "128": "icon128.png"
    }
  },
  "icons": {
    "16": "icon16.png",
    "48": "icon48.png",
    "128": "icon128.png"
  },
  "permissions": []
}
```

Key rules:
- `manifest_version` must be 3 (V2 is deprecated)
- `description` max 132 characters
- `permissions: []` (empty array, zero permissions = fastest approval)
- `homepage_url` is where the Chrome Web Store links to (your backlink)
- No `host_permissions`, no `content_scripts`, no `web_accessible_resources` for V1
- No `background` service worker unless needed

### When Content Scripts Are Needed

Only add content scripts if the extension must modify or read pages on other websites. This triggers stricter review. If you need them:
1. Ship V1 as popup-only first to get the extension live
2. Add content scripts in V2 update after approval
3. Content scripts require `host_permissions` for each target domain
4. You will need a privacy policy explaining what data you access and why

---

## Icons

Three sizes required: 16px, 48px, 128px. All PNG format.

Generate programmatically with Python if no design tool is available:
```python
import struct, zlib, math

def create_icon(size, letter, bg_color_hex, filename):
    # bg_color_hex like "#3366CC"
    r = int(bg_color_hex[1:3], 16)
    g = int(bg_color_hex[3:5], 16)
    b = int(bg_color_hex[5:7], 16)
    # ... generate circle with letter
```

Icon guidelines:
- Use the brand colour as background
- White letter or simple symbol on coloured circle
- Must be recognisable at 16px (keep it simple)
- 128px version is also used as the store icon

---

## Popup Pattern

### popup.html
```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Extension Name</title>
  <link rel="stylesheet" href="popup.css">
</head>
<body>
  <div class="container">
    <!-- Main UI here -->

    <!-- CTA (optional, soft) -->
    <div class="cta">
      <p>Need help?</p>
      <a href="https://your-website.com/contact/" target="_blank" rel="noopener">Get in touch</a>
    </div>

    <!-- Footer with backlink -->
    <div class="footer">
      <a href="https://your-website.com" target="_blank" rel="noopener">Powered by Your Brand</a>
    </div>
  </div>

  <script src="popup.js"></script>
</body>
</html>
```

Rules:
- All external links use `target="_blank" rel="noopener"`
- Keep all links to a single domain (consistent, trustworthy)
- Width: 340-450px is standard for popup
- Load data files with `fetch(chrome.runtime.getURL('data.json'))`

---

## Chrome Web Store Submission

### Required Form Fields

| Field | What to Put |
|-------|-------------|
| **Title** | Pulled from manifest `name`. Max 75 chars. |
| **Summary** | Pulled from manifest `description`. Max 132 chars. |
| **Description** | Up to 16,000 chars. See template below. |
| **Category** | Usually "Tools". Other options: "Productivity", "Fun", "Search Tools" |
| **Language** | Match your target audience. Pick your market's locale, e.g. "English" or a country-specific English variant. |

### Description Template
```
[Extension Name] gives you [one-line value prop].

[How to use it — 2-3 sentences explaining the interaction]

Features:
- [Feature 1]
- [Feature 2]
- [Feature 3]

Useful for:
- [Use case 1]
- [Use case 2]
- [Use case 3]

No data is collected. No account required. Works entirely offline after installation.

Built by [Brand Name] ([website URL]).
```

### Graphic Assets

| Asset | Size | Format | Required? |
|-------|------|--------|-----------|
| Store icon | 128x128 | PNG | Yes (use icon128.png) |
| Screenshots | 1280x800 or 640x400 | JPEG or 24-bit PNG (no alpha) | Yes, at least 1 (max 5) |
| Small promo tile | 440x280 | JPEG or 24-bit PNG (no alpha) | No |
| Marquee promo tile | 1400x560 | JPEG or 24-bit PNG (no alpha) | No |
| Promo video | YouTube URL | N/A | No |

Screenshots: Load the extension in Chrome, click it, take a screenshot of the popup in use with results showing. Resize to 1280x800 or 640x400. Must be JPEG or 24-bit PNG with no alpha channel.

### URLs

| Field | What to Put |
|-------|-------------|
| **Official URL** | Select from Google Search Console if verified, otherwise "None" |
| **Homepage URL** | Your website URL (this is the backlink) |
| **Support URL** | Your website contact page URL |

### Privacy and Permissions

| Field | Value |
|-------|-------|
| **Single purpose description** | "[Extension name] lets users [one action]. [How it works in one sentence]. All data is bundled locally. No user data is collected, stored, or transmitted." |
| **Are you using remote code?** | "No" (unless you load external JS/Wasm) |
| **Permission justification** | Leave blank if no permissions and no remote code |
| **Data usage checkboxes** | All unchecked (for popup-only with no data collection) |
| **Three certifications** | Check all three (no data sold, no unrelated use, no creditworthiness) |
| **Mature content** | No (unchecked) |

### Privacy Policy

Google requires a privacy policy URL. Options:
1. Host a simple privacy policy page on your website (another backlink)
2. Use a free privacy policy generator
3. Content: state the extension collects no data, makes no network requests, stores nothing

---

## Backlink Opportunities

A Chrome extension can generate up to 4 backlinks:
1. `homepage_url` in manifest (shows on Chrome Web Store listing page)
2. Homepage URL in store submission form
3. Privacy policy page hosted on your website
4. CTA and footer links inside the popup (not crawled by Google, but user-facing)

---

## Common Rejection Reasons

1. **Too many permissions** — Request only what you use. Zero permissions = no friction.
2. **Missing single purpose** — Google wants a clear, narrow purpose. One thing, stated simply.
3. **Description mismatch** — What the description says must match what the extension does.
4. **Missing privacy policy** — Required even if you collect nothing.
5. **Content scripts on broad domains** — Avoid `*://*/*` matches. Be specific.
6. **Remote code** — Loading JS from external URLs gets flagged. Bundle everything locally.
7. **Deceptive install tactics** — CTA text, screenshots, and description must match actual functionality.

---

## Build Workflow

1. Define what the extension does (one purpose)
2. Create manifest.json with popup-only architecture
3. Build popup HTML/CSS/JS
4. Generate icons (16, 48, 128px)
5. Test: `chrome://extensions` → Developer mode → Load unpacked
6. Verify all links open correct URLs
7. Create a zip of the folder (exclude .DS_Store, .git, etc.)
8. Submit to Chrome Web Store Developer Dashboard ($5 one-time registration)
9. Fill all form fields per the tables above
10. Take and upload at least 1 screenshot
11. Submit for review (typically 1-3 business days)

---

## Output Format

When building an extension, deliver:
1. All source files ready to load as unpacked extension
2. A pre-filled table of every Chrome Web Store form field
3. A description block ready to paste
4. A single purpose description ready to paste
5. Instructions for taking screenshots and submitting
