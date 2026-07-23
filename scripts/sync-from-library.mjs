// Syncs this public repo from the operator's skill library + the site catalog. Idempotent:
// it (re)generates skills/<slug>/ (kit files + a per-skill README) for every catalog card that
// is "ready", and rebuilds the root README (badge count + grouped tables). Run after new skills
// are packaged and their site cards flip to ready.
//
//   node scripts/sync-from-library.mjs           # sync everything ready
//   node scripts/sync-from-library.mjs --check   # report what WOULD change, write nothing
//
// Sources (read-only): the site catalog for taxonomy + public blurbs, and the portable-prompt
// library for the actual kit files. Kit files are copied byte-for-byte; nothing is re-authored.

import fs from 'node:fs';
import os from 'node:os';
import path from 'node:path';
import { fileURLToPath } from 'node:url';

const REPO = path.resolve(path.dirname(fileURLToPath(import.meta.url)), '..');
const CATALOG = path.join(os.homedir(), 'ClaudeCode/code/donatassimkus-com/src/data/aiSkillsCatalog.ts');
const LIB = path.join(os.homedir(), 'ClaudeCode/work/shared/portable-prompts');
const SKILLS_DIR = path.join(REPO, 'skills');
const check = process.argv.includes('--check');

const GROUP_ORDER = [
  'Build & Automation', 'Growth & Acquisition', 'SEO & Search', 'Content & Writing',
  'Sales & Revenue', 'Brand, Product & UX', 'AI Systems & Ops', 'BizOps & Finance', 'Tactics & Hacks',
];

// --- parse the catalog: ready cards only, with slug from href ---
const cat = fs.readFileSync(CATALOG, 'utf-8');
const rowRe = /\{ title: "([^"]+)", blurb: "([^"]+)", group: "([^"]+)", type: "(\w+)", status: "ready", href: "\/ai-skills\/([a-z0-9-]+)" \}/g;
const cards = [];
let m;
while ((m = rowRe.exec(cat)) !== null) {
  cards.push({ title: m[1], blurb: m[2], group: m[3], type: m[4], slug: m[5] });
}
if (!cards.length) throw new Error('no ready cards parsed from the catalog');

// --- per-skill sync ---
const changes = [];
function syncKit(card) {
  const dest = path.join(SKILLS_DIR, card.slug);
  const srcFolder = path.join(LIB, card.slug);
  const flat = path.join(LIB, `${card.slug}-portable-setup-prompt.md`);

  fs.mkdirSync(dest, { recursive: true });
  let files = [];

  if (card.type === 'agent') {
    // agent = one flat runbook, shipped as INSTALL-PROMPT.md
    if (!fs.existsSync(flat)) throw new Error(`agent ${card.slug}: missing ${flat}`);
    if (!check) fs.copyFileSync(flat, path.join(dest, 'INSTALL-PROMPT.md'));
    files = ['INSTALL-PROMPT.md'];
  } else {
    // knowledge = copy the whole kit folder verbatim (INSTALL-PROMPT.md + SKILL.md + references/…)
    if (!fs.existsSync(srcFolder)) throw new Error(`knowledge ${card.slug}: missing ${srcFolder}`);
    const walk = (dir, base = '') => {
      for (const e of fs.readdirSync(dir, { withFileTypes: true })) {
        const rel = base ? `${base}/${e.name}` : e.name;
        if (e.isDirectory()) walk(path.join(dir, e.name), rel);
        else files.push(rel);
      }
    };
    walk(srcFolder);
    if (!check) {
      for (const rel of files) {
        const to = path.join(dest, rel);
        fs.mkdirSync(path.dirname(to), { recursive: true });
        fs.copyFileSync(path.join(srcFolder, rel), to);
      }
    }
  }

  // per-skill README
  const typeLabel = card.type === 'agent' ? 'Agent skill' : 'Knowledge skill';
  const installLine = card.type === 'agent'
    ? 'It detects what you already have, builds the skill on your own machine, and runs it.'
    : 'It installs the skill files unchanged, asks one question to calibrate, then runs the method on your own material. No accounts, no keys.';
  const topFiles = files.filter((f) => f !== 'README.md');
  const hasRefs = topFiles.some((f) => f.startsWith('references/'));
  const whatsHere = [];
  if (topFiles.includes('INSTALL-PROMPT.md')) whatsHere.push('- `INSTALL-PROMPT.md`: the runbook you paste.');
  if (topFiles.includes('SKILL.md')) whatsHere.push('- `SKILL.md`: the router your AI installs. It loads the reference each task needs.');
  if (hasRefs) whatsHere.push('- `references/`: the deeper method, loaded on demand.');
  for (const f of topFiles) {
    if (['INSTALL-PROMPT.md', 'SKILL.md'].includes(f) || f.startsWith('references/')) continue;
    whatsHere.push(`- \`${f}\`: shipped with the kit.`);
  }
  const readme = `# ${card.title} for Claude Code

**${typeLabel}.** ${card.blurb}

## Install

Copy [\`INSTALL-PROMPT.md\`](INSTALL-PROMPT.md) and paste it into your AI agent (Claude Code, Cursor, or similar). ${installLine}

## What's here

${whatsHere.join('\n')}

Live preview: [donatassimkus.com/ai-skills/${card.slug}](https://donatassimkus.com/ai-skills/${card.slug})
`;
  if (!check) fs.writeFileSync(path.join(dest, 'README.md'), readme);
  changes.push(`${card.slug} (${card.type}, ${files.length} files)`);
}

for (const card of cards) syncKit(card);

// --- rebuild the root README ---
let root = fs.readFileSync(path.join(REPO, 'README.md'), 'utf-8');
root = root.replace(/!\[Skills\]\(https:\/\/img\.shields\.io\/badge\/skills-\d+-blue\.svg\)/,
  `![Skills](https://img.shields.io/badge/skills-${cards.length}-blue.svg)`);

const byGroup = {};
for (const c of cards) (byGroup[c.group] ||= []).push(c);
let tables = '## The skills\n';
for (const g of GROUP_ORDER) {
  const rows = byGroup[g];
  if (!rows || !rows.length) continue;
  tables += `\n### ${g}\n\n| Skill | Type | What it does |\n|---|---|---|\n`;
  for (const c of rows) {
    tables += `| [${c.slug}](skills/${c.slug}/) | ${c.type === 'agent' ? 'Agent' : 'Knowledge'} | ${c.blurb} |\n`;
  }
}
// any group not in GROUP_ORDER (safety)
for (const g of Object.keys(byGroup)) {
  if (GROUP_ORDER.includes(g)) continue;
  tables += `\n### ${g}\n\n| Skill | Type | What it does |\n|---|---|---|\n`;
  for (const c of byGroup[g]) tables += `| [${c.slug}](skills/${c.slug}/) | ${c.type === 'agent' ? 'Agent' : 'Knowledge'} | ${c.blurb} |\n`;
}

root = root.replace(/## The skills[\s\S]*?(?=\n## Adding more)/, tables + '\n');
if (!check) fs.writeFileSync(path.join(REPO, 'README.md'), root);

console.log(`${check ? '[--check] ' : ''}synced ${cards.length} skills across ${Object.keys(byGroup).length} groups`);
console.log(changes.join('\n'));
