#!/usr/bin/env node
/**
 * URL-parity check for a rebuild / CMS migration. Fetches the OLD site's
 * sitemap (index or single), then for every old URL reports whether it exists
 * in the new build, is covered by a redirect, or is MISSING (would 404 after
 * cutover). Framework-agnostic.
 *
 * Usage: node sitemap-parity.mjs <old-sitemap-url> <output-dir> [redirects-file]
 *   redirects-file: optional, host-agnostic. Understands three shapes:
 *     - JSON object, e.g. { "redirects": [{ "source": "/old" }] }  (source | from)
 *     - JSON array of paths, e.g. ["/old", "/older"]
 *     - `_redirects` text, one rule per line "from  to  [status]", # comments ignored
 *   It prints how many rules it parsed and in which shape, so a format it cannot
 *   read is visible instead of silently reporting every redirect as MISSING.
 */
import fs from 'node:fs';
import path from 'node:path';

const [oldSitemap, distArg, redirectsArg] = process.argv.slice(2);
if (!oldSitemap || !distArg) {
  console.error('Usage: node sitemap-parity.mjs <old-sitemap-url> <output-dir> [redirects.json]');
  process.exit(1);
}
const DIST = path.resolve(distArg);
if (!fs.existsSync(DIST)) { console.error('Output dir not found:', DIST); process.exit(1); }

function walk(d, a = []) {
  for (const e of fs.readdirSync(d, { withFileTypes: true })) {
    const p = path.join(d, e.name);
    if (e.isDirectory()) walk(p, a);
    else if (e.name.endsWith('.html')) a.push(p);
  }
  return a;
}
const norm = u => {
  try { let p = new URL(u, 'https://placeholder.invalid').pathname; if (!p.endsWith('/') && !/\.[a-z0-9]+$/i.test(p)) p += '/'; return p.toLowerCase(); }
  catch { return u; }
};
const built = new Set(walk(DIST).map(f => norm('/' + path.relative(DIST, f).replace(/index\.html$/, '').replace(/\\/g, '/'))));

let redirectSrcs = new Set();
if (redirectsArg && fs.existsSync(redirectsArg)) {
  const raw = fs.readFileSync(redirectsArg, 'utf8');
  const add = s => { if (typeof s === 'string' && s.trim()) redirectSrcs.add(norm(s.trim())); };
  let shape;
  try {
    const j = JSON.parse(raw);
    const entries = Array.isArray(j) ? j : (j.redirects || j.rewrites || []);
    entries.forEach(r => add(typeof r === 'string' ? r : (r.source || r.from)));
    shape = 'json';
  } catch {
    raw.split('\n').forEach(line => {
      const t = line.trim();
      if (!t || t.startsWith('#')) return;
      add(t.split(/\s+/)[0]);
    });
    shape = 'text';
  }
  console.log(`Redirect rules parsed: ${redirectSrcs.size} (${shape} shape, from ${redirectsArg})`);
  if (!redirectSrcs.size) console.log('  WARNING: parsed 0 rules. Check the file shape, or every redirected URL below will report as MISSING.');
}

const UA = { 'User-Agent': 'Mozilla/5.0 (compatible; sitemap-parity)' };
const ft = async u => { try { const r = await fetch(u, { headers: UA }); return r.ok ? await r.text() : null; } catch { return null; } };
const locs = x => [...x.matchAll(/<loc>([^<]+)<\/loc>/g)].map(m => m[1].trim());

(async () => {
  const root = await ft(oldSitemap);
  if (!root) { console.error('Could not fetch', oldSitemap); process.exit(1); }
  let urls = [];
  const subs = locs(root).filter(x => /\.xml/i.test(x));
  if (subs.length) { for (const s of subs) { const t = await ft(s); if (t) urls = urls.concat(locs(t)); } }
  else urls = locs(root);
  const oldPaths = [...new Set(urls.map(norm))];
  const exists = [], redir = [], missing = [];
  for (const p of oldPaths) {
    if (built.has(p)) exists.push(p);
    else if (redirectSrcs.has(p)) redir.push(p);
    else missing.push(p);
  }
  console.log(`Old URLs: ${oldPaths.length} | exist in new build: ${exists.length} | redirected: ${redir.length} | MISSING: ${missing.length}`);
  if (redir.length) { console.log('\nRedirected (ok):'); redir.forEach(p => console.log('  ' + p)); }
  console.log('\nMISSING (will 404 after cutover — add a 301 or recreate the page):');
  if (!missing.length) console.log('  none');
  else missing.forEach(p => console.log('  ' + p));
  // new pages not in the old sitemap (informational)
  const oldSet = new Set(oldPaths);
  console.log(`\nNew pages not in the old sitemap (expected for a richer rebuild): ${[...built].filter(p => !oldSet.has(p)).length}`);
})();
