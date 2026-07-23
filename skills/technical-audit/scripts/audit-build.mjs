#!/usr/bin/env node
/**
 * Static-build audit: broken internal links, broken local images, title/meta
 * uniqueness + length, and noindex leaks. Framework-agnostic — point it at any
 * built output folder (dist/out/build/public).
 *
 * Usage: node audit-build.mjs <output-dir>
 */
import fs from 'node:fs';
import path from 'node:path';

const DIST = path.resolve(process.argv[2] || 'dist');
if (!fs.existsSync(DIST)) { console.error('Output dir not found:', DIST); process.exit(1); }

function walk(d, a = []) {
  for (const e of fs.readdirSync(d, { withFileTypes: true })) {
    const p = path.join(d, e.name);
    if (e.isDirectory()) walk(p, a);
    else if (e.name.endsWith('.html')) a.push(p);
  }
  return a;
}

const files = walk(DIST);
const broken = {}, brokenImg = {}, titles = {}, descs = {}, noindex = [], missing = [], overT = [], overD = [];

for (const f of files) {
  const html = fs.readFileSync(f, 'utf8');
  const rel = path.relative(DIST, f);
  for (const m of html.matchAll(/href="([^"]+)"/g)) {
    let h = m[1];
    if (/^(https?:|mailto:|tel:|\/\/|#|data:)/.test(h)) continue;
    h = h.split('#')[0].split('?')[0];
    if (!h || !h.startsWith('/')) continue;
    const cands = [path.join(DIST, h), path.join(DIST, h, 'index.html'), path.join(DIST, h + '.html')];
    if (!cands.some(c => fs.existsSync(c))) (broken[h] = broken[h] || new Set()).add(rel);
  }
  for (const m of html.matchAll(/<img[^>]+src="([^"]+)"/g)) {
    let s = m[1];
    if (/^(https?:|data:|\/\/)/.test(s) || !s.startsWith('/')) continue;
    s = s.split('?')[0];
    if (!fs.existsSync(path.join(DIST, s))) (brokenImg[s] = brokenImg[s] || new Set()).add(rel);
  }
  const t = (html.match(/<title[^>]*>([\s\S]*?)<\/title>/i) || [])[1];
  const d = (html.match(/<meta[^>]+name="description"[^>]+content="([^"]*)"/i) || [])[1];
  if (!t) missing.push(rel + ' [no title]'); else { (titles[t] = titles[t] || []).push(rel); if (t.length > 60) overT.push(rel + ' (' + t.length + ')'); }
  if (!d) missing.push(rel + ' [no description]'); else { (descs[d] = descs[d] || []).push(rel); if (d.length > 160) overD.push(rel + ' (' + d.length + ')'); }
  if (/<meta[^>]+name="robots"[^>]+content="[^"]*noindex/i.test(html)) noindex.push(rel);
}

const dup = o => Object.entries(o).filter(([, v]) => v.length > 1);
const list = (label, arr) => { console.log(`\n${label}: ${arr.length}`); arr.slice(0, 25).forEach(x => console.log('  ' + x)); };

console.log('HTML pages:', files.length);
console.log('\nBROKEN internal links:', Object.keys(broken).length);
Object.entries(broken).slice(0, 25).forEach(([h, s]) => console.log('  ' + h + ' <- ' + [...s].slice(0, 3).join(', ')));
console.log('\nBROKEN image sources:', Object.keys(brokenImg).length);
Object.entries(brokenImg).slice(0, 25).forEach(([s, r]) => console.log('  ' + s + ' <- ' + [...r].slice(0, 2).join(', ')));
list('Missing title/description', missing);
console.log('\nDuplicate titles:', dup(titles).length);
dup(titles).slice(0, 15).forEach(([t, v]) => console.log('  "' + t.slice(0, 45) + '" x' + v.length));
console.log('\nDuplicate descriptions:', dup(descs).length);
dup(descs).slice(0, 15).forEach(([d, v]) => console.log('  x' + v.length + ' "' + d.slice(0, 45) + '"'));
list('Titles over 60 chars', overT);
list('Descriptions over 160 chars', overD);
list('noindex pages', noindex);

const clean = !Object.keys(broken).length && !Object.keys(brokenImg).length && !missing.length && !dup(titles).length && !dup(descs).length;
console.log('\n' + (clean ? 'PASS: links, images, and meta are clean.' : 'See findings above.'));
