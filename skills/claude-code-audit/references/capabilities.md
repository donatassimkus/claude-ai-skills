# Claude Code Capabilities Reference

Complete inventory of Claude Code primitives and advanced features. Use as the benchmark when auditing: compare what's available vs what's being used.

Last verified: 2026-06-17 (covers through v2.1.178)
Source: https://code.claude.com/docs/en/ (canonical; docs.anthropic.com/en/docs/claude-code/* redirects here)

---

## Recent additions (v2.1.139–v2.1.148, verified 2026-05-22)

Delta since the prior v2.1.137 baseline. Next audit should fold these into their numbered sections.

- **`/goal` (v2.1.139):** set a verifiable completion condition; Claude works across turns until a fast model confirms it holds. Works interactive, `-p`, Remote Control. (§3 bundled skills / §8 commands)
- **Agent view `claude agents` (v2.1.139, +`--json` v2.1.145):** one dashboard of every session (running/blocked/done); dispatch background jobs as rows. (§8)
- **`claude plugin details <name>` (v2.1.139):** component inventory + projected per-session token cost. (§5)
- **`/scroll-speed` (v2.1.139).** (§8)
- **`subagent_type` matching now case/separator-insensitive (v2.1.140):** `"Code Reviewer"` → `code-reviewer`. (§4)
- **`terminalSequence` hook output field (v2.1.141):** hooks emit desktop notifications/titles/bells without a controlling terminal. (§6)
- **`CLAUDE_CODE_PLUGIN_PREFER_HTTPS` (v2.1.141):** clone plugin sources over HTTPS not SSH. (§8 env)
- **`claude agents` config flags (v2.1.142):** `--add-dir`, `--settings`, `--mcp-config`, `--plugin-dir`, `--permission-mode`, `--model`, `--effort`, `--dangerously-skip-permissions` for dispatched background sessions. (§8)
- **Fast mode now defaults to Opus 4.7 (v2.1.142):** pin back via `CLAUDE_CODE_OPUS_4_6_FAST_MODE_OVERRIDE=1`. (§8 model/env)
- **Plugins with root-level `SKILL.md` and no `skills/` dir now surfaced as a skill (v2.1.142).** (§5)
- **`worktree.bgIsolation: "none"` (v2.1.143):** background sessions edit the working copy directly without EnterWorktree. (§8 worktree)
- **Plugin dependency enforcement (v2.1.143):** `plugin disable` refuses if depended-on; `plugin enable` force-enables transitive deps. (§5)
- **`--bg` flag + `/resume` for background sessions (v2.1.144).** (§8)
- **Stop / SubagentStop hook input adds `background_tasks` and `session_crons` fields (v2.1.145).** (§6 input)
- **`agent_id` + `parent_agent_id` on `claude_code.tool` OTEL spans (v2.1.145).** (§8 telemetry)
- **`/code-review` (v2.1.147):** reports correctness bugs at a chosen effort (`/code-review high`); `--comment` posts inline GitHub PR comments. `/simplify` was renamed to `/code-review`; its old cleanup-and-fix behaviour now requires `/code-review --fix` (v2.1.152). §3 body updated 2026-06-17. (§3)

---

## 1. CLAUDE.md (Memory Files)

Project-wide rules and identity loaded every conversation.

**File locations (priority order):**

| Scope | Location | Shared with |
|---|---|---|
| Managed policy | `/Library/Application Support/ClaudeCode/CLAUDE.md` (macOS) | All org users |
| Managed policy (modular) | `managed-settings.d/` directory | All org users (multiple policy files) |
| Project | `./CLAUDE.md` or `./.claude/CLAUDE.md` | Team via source control |
| User | `~/.claude/CLAUDE.md` | Just you, all projects |

**Features:**
- `@path/to/import` syntax: import additional files into CLAUDE.md (relative or absolute paths, max 5 hops deep)
- Path-specific rules: `.claude/rules/*.md` files with `paths` frontmatter to scope rules to file types
- `claudeMdExcludes` setting: skip irrelevant CLAUDE.md files in monorepos
- Auto-discovery from subdirectories: CLAUDE.md files in subdirs load on demand when Claude reads files there
- `--add-dir` flag + `CLAUDE_CODE_ADDITIONAL_DIRECTORIES_CLAUDE_MD=1` to load CLAUDE.md from additional directories
- `/init` command: auto-generate CLAUDE.md from codebase analysis
- `/memory` command: browse and edit all loaded memory files

**Auto memory system:**
- Claude writes its own notes to `~/.claude/projects/<project>/memory/`
- `MEMORY.md` index (first 200 lines loaded every session) + topic files loaded on demand
- Toggle with `/memory` or `autoMemoryEnabled` setting
- `autoMemoryDirectory` setting to customize storage location
- Subagents can have their own persistent memory (see Agents section)

**Best practices:**
- Under 200 lines per CLAUDE.md file
- Use `@imports` or `.claude/rules/` to split large files
- Specific, concrete instructions (not vague guidance)

**Signs it needs attention:** Over 150 lines, duplicating content from rules/context files, conflicting instructions across files.

---

## 2. Rules (`.claude/rules/*.md`)

Focused rule files on one topic, auto-loaded every conversation.

**Features:**
- Supports `paths` frontmatter for conditional loading:
  ```yaml
  ---
  paths:
    - "src/api/**/*.ts"
  ---
  ```
- Glob patterns: `**/*.ts`, `src/**/*`, `*.md`, `src/components/*.tsx`
- Brace expansion: `src/**/*.{ts,tsx}`
- Rules without `paths` load unconditionally (same priority as `.claude/CLAUDE.md`)
- User-level rules: `~/.claude/rules/` (lower priority than project rules)
- Supports symlinks for sharing rules across projects

**When to create a rule file:**
- A behavioral rule applies across all conversations but is not identity
- A correction keeps recurring (extract from lessons into a rule)
- A writing/style/format constraint applies universally
- A rule should only apply to specific file types (use `paths` frontmatter)

---

## 3. Skills (`.claude/skills/*/SKILL.md`)

Reusable task workflows invoked via `/name` or natural language.

**Frontmatter fields:**

| Field | Type | Default | Description |
|---|---|---|---|
| `name` | string | directory name | `/slash-command` name. Lowercase, numbers, hyphens only. Max 64 chars. |
| `description` | string | first paragraph | Trigger text. Claude uses for auto-invocation. Truncated at 250 chars. |
| `argument-hint` | string | none | Autocomplete hint in `/` menu |
| `disable-model-invocation` | boolean | false | Manual-only, removes from Claude's context |
| `user-invocable` | boolean | true | When false, hidden from `/` menu (Claude-only) |
| `allowed-tools` | string | all tools | Comma-separated tools with optional glob patterns |
| `model` | string | inherit | `sonnet`, `opus`, `haiku`, or full model ID (e.g. `claude-opus-4-7`) |
| `effort` | string | inherit | `low`, `medium`, `high`, `xhigh` (Opus 4.7), `max`. Controls thinking depth. |
| `context` | string | none | Set to `fork` for isolated subagent execution |
| `agent` | string | general-purpose | Subagent type when `context: fork` is set (e.g., `Explore`, `Plan`) |
| `hooks` | object | none | Lifecycle hooks scoped to this skill |
| `paths` | string/list | none | Glob patterns to auto-activate skill for specific files |
| `when_to_use` | string | none | Extra trigger context appended to `description` in the skill listing. Counts toward 1,536-char cap. |
| `shell` | string | bash | Shell for dynamic context commands. `bash` or `powershell`. |
| `maxTurns` | number | none | Maximum agentic turns before stop |
| `disallowedTools` | string | none | Tools to deny (removed from inherited list) |
| `background` | boolean | false | Run as background task |
| `isolation` | string | none | Set to `worktree` for git worktree isolation |
| `initialPrompt` | string | none | Auto-submit as first turn when skill is main session |

**Invocation control matrix:**

| Configuration | User invokes | Claude invokes | Context loading |
|---|---|---|---|
| Default | Yes | Yes | Description always loaded, full skill on invocation |
| `disable-model-invocation: true` | Yes | No | Description not in context, full on user invoke |
| `user-invocable: false` | No | Yes | Description always loaded, full skill on invocation |

**String substitutions:**

| Variable | Description |
|---|---|
| `$ARGUMENTS` | All args passed. Auto-appended if not present. |
| `$ARGUMENTS[N]` / `$N` | Specific arg by 0-based index |
| `${CLAUDE_SESSION_ID}` | Current session ID |
| `${CLAUDE_SKILL_DIR}` | Directory containing the skill's SKILL.md |

**Advanced features:**
- Dynamic context injection (`` !`command` ``): shell commands run before skill loads, output replaces placeholder
- `context: fork` + `agent`: run in isolated subagent
- `allowed-tools` with glob patterns: `Bash(git *)`, `Read, Grep, Glob`
- Skill-scoped hooks: PreToolUse, PostToolUse, Stop (auto-converts to SubagentStop)
- `once: true` in hooks: run once per session then remove (skills only)
- Supporting files: `references/`, scripts, templates alongside SKILL.md
- `ultrathink` keyword anywhere in content activates extended thinking
- `paths` field for auto-activation when Claude reads matching files (monorepo support)
- Nested `.claude/skills/` directories auto-discovered in monorepos

**Bundled skills (ship with Claude Code):**
- `/batch <instruction>`: parallel codebase changes across git worktrees
- `/claude-api`: Claude API/SDK reference (auto-activates for anthropic imports, covers Managed Agents)
- `/debug [description]`: enable debug logging and troubleshoot issues
- `/loop [interval] <prompt>`: run prompt on recurring interval (self-paces when interval omitted; can reach for Monitor tool to skip polling)
- `/code-review [effort]`: review changed files for correctness bugs at a chosen effort; `--comment` posts inline PR comments, `--fix` applies fixes (renamed from `/simplify`, v2.1.147)
- `/powerup`: interactive lessons with animated demos for Claude Code features
- `/team-onboarding`: generate teammate ramp-up guide from local usage
- `/effort`: interactive slider to tune speed vs intelligence (low/medium/high/xhigh/max)
- `/color`: set prompt-bar color
- `/copy`: enhanced with index parameter and `w` key to write-to-file
- `/fewer-permission-prompts`: scan transcripts, propose bash/MCP allowlist for project settings
- `/ultrareview`: comprehensive cloud-based code review with multi-agent analysis
- `/ultraplan`: research-preview cloud-based plan mode (v2.1.92+). Drafts plan in a Claude Code on the web session while CLI stays free; review/comment in browser, execute remotely or pull back to CLI. First run auto-creates default cloud env (v2.1.101+).
- `/autofix-pr`: enable PR auto-fix from terminal for current branch's open PR (v2.1.92+). Claude watches CI + review comments and pushes fixes until green.
- `/tui`: switch to flicker-free rendering in the same conversation
- `/schedule`: create/manage scheduled remote agents (cron triggers)
- `/btw`: ask a side question that sees full context but has no tool access; answer discarded rather than added to history
- `/usage`: merged `/cost` + `/stats` (v2.1.118). Per-model + cache-hit breakdown for subscription users.
- `/release-notes`: interactive version picker (v2.1.111+)
- `/cost`: per-model and cache-hit breakdown (still works alongside `/usage`)
- `/focus`: toggle focus-mode rendering (v2.1.110+)
- `/buddy`: hatch a small creature that watches you code (April 1 release; ignore in production audits)

**Deprecated/removed:**
- `/tag` (removed, v2.1.92)
- `/vim` (removed, v2.1.92; use `/config` editor mode)
- `/output-style` (removed; use `/config`)
- `/fork` renamed to `/branch` (alias still works)
- `/rewind` now aliased as `/undo`

**Character budget:** 1% of context window (fallback 8,000 chars) for ALL skill descriptions combined. Each entry's combined `description` + `when_to_use` capped at 1,536 chars. Override with `SLASH_COMMAND_TOOL_CHAR_BUDGET` env var.

**Skill content lifecycle:** once invoked, SKILL.md enters the conversation as a single message and stays for the rest of the session. Auto-compaction re-attaches the most recent invocation of each skill after summary (first 5,000 tokens each, 25,000 token combined budget, most-recent-first).

**File locations (priority order):** Enterprise > Personal (`~/.claude/skills/`) > Project (`.claude/skills/`) > Plugin

**Legacy:** `.claude/commands/*.md` still works, skills take precedence if same name.

---

## 4. Agents (`.claude/agents/*.md`)

Custom subagent types with specific roles, tools, and instructions.

**Frontmatter fields:**

| Field | Required | Description |
|---|---|---|
| `name` | Yes | Unique identifier, lowercase + hyphens |
| `description` | Yes | When Claude should delegate to this agent |
| `tools` | No | Allowed tools. `Agent(worker, researcher)` restricts which subagents can be spawned (Task tool renamed to Agent in v2.1.63; `Task(...)` still works as alias). |
| `disallowedTools` | No | Tools to deny (removed from inherited/specified list) |
| `model` | No | `sonnet`, `opus`, `haiku`, full model ID (e.g. `claude-opus-4-7`), or `inherit` |
| `permissionMode` | No | `default`, `acceptEdits`, `auto`, `dontAsk`, `bypassPermissions`, `plan` |
| `maxTurns` | No | Maximum agentic turns before stop |
| `skills` | No | Skills to preload into subagent context at startup |
| `mcpServers` | No | MCP servers scoped to this subagent (inline definition or name reference) |
| `hooks` | No | Lifecycle hooks scoped to this agent |
| `memory` | No | Persistent memory: `user`, `project`, or `local` scope |
| `background` | No | Set to `true` to always run as background task |
| `isolation` | No | Set to `worktree` for git worktree isolation. `worktree.sparsePaths` for large monorepos. |
| `effort` | No | `low`, `medium`, `high`, `xhigh` (Opus 4.7), `max`. Override session effort per agent. |
| `initialPrompt` | No | Auto-submit as first turn when agent is main session agent |
| `color` | No | Display color in task list/transcript: red/blue/green/yellow/purple/orange/pink/cyan |
| `prompt` | No | Used when agents are passed via `--agents` JSON (equivalent to markdown body) |

**Built-in agents:**
- `Explore`: Haiku, read-only. Codebase search and analysis. Invoked with thoroughness level (quick / medium / very thorough).
- `Plan`: Inherits model, read-only. Research during plan mode.
- `general-purpose`: Inherits model, all tools. Complex multi-step tasks.
- `Bash`: Inherits model. Terminal commands in separate context.
- `Claude Code Guide`: Haiku. Questions about Claude Code features.
- `statusline-setup`: Sonnet. Auto-invoked when you run `/statusline`.

**Agent scopes (priority order):**
1. `--agents` CLI flag (session only, JSON)
2. `.claude/agents/` (project, version-controlled)
3. `~/.claude/agents/` (personal, all projects)
4. Plugin `agents/` directory

**Management:**
- `/agents` command: interactive create/edit/delete
- `claude agents`: list all agents from CLI
- `--agent <name>`: run entire session as a specific agent
- `@agent-name` mention: guarantee specific agent for one task
- Background subagents: Ctrl+B to background a running task, `CLAUDE_CODE_DISABLE_BACKGROUND_TASKS=1` to disable

**Persistent memory:**
- `memory: user` stores at `~/.claude/agent-memory/<name>/`
- `memory: project` stores at `.claude/agent-memory/<name>/`
- `memory: local` stores at `.claude/agent-memory-local/<name>/`
- Auto-enables Read, Write, Edit tools
- First 200 lines of agent's MEMORY.md loaded at startup

---

## 5. Plugins

Third-party skill/agent/hook bundles from marketplaces.

**Plugin manifest (.claude-plugin/plugin.json):**
- `name` (required): unique identifier, used as skill namespace prefix
- `description` (required): shown in plugin manager
- `version` (required): semantic versioning
- `author`, `homepage`, `repository`, `license` (optional)

**Plugin structure:**
```
my-plugin/
├── .claude-plugin/plugin.json    # Manifest (name, description, version)
├── skills/                       # Skills with SKILL.md
├── agents/                       # Agent definitions
├── commands/                     # Legacy command files (use skills/ for new plugins)
├── hooks/hooks.json              # Hook configurations
├── monitors/monitors.json        # Background monitor configs (tail logs, watch files)
├── bin/                          # Executables added to Bash tool PATH while plugin enabled
├── .mcp.json                     # MCP server configs
├── .lsp.json                     # LSP server configs
└── settings.json                 # Default settings (`agent` + `subagentStatusLine` keys supported)
```

**Features:**
- Namespaced skills: `/plugin-name:skill-name`
- `/reload-plugins` for live reloading during development (reloads skills, agents, hooks, plugin MCP/LSP servers)
- `--plugin-dir` flag for local testing (repeatable for multiple plugins; local copy takes precedence over installed marketplace plugin of same name)
- Plugin marketplace: install/uninstall via `/plugin`; submit via claude.ai/settings/plugins/submit or platform.claude.com/plugins/submit
- LSP servers: `.lsp.json` for language server protocol integration (language-specific commands, extension mappings)
- Background monitors: `monitors/monitors.json` with stdout lines delivered to Claude as notifications; supports `when` trigger and variable substitution
- Security: plugin agents cannot use `hooks`, `mcpServers`, or `permissionMode`
- Migration path: convert existing `.claude/` configurations to distributable plugins
- Settings: plugin `settings.json` takes priority over plugin.json settings; supports `agent` (main-thread agent) and `subagentStatusLine` keys
- Inline plugin declaration: `source: 'settings'` allows declaring plugin inline in settings.json
- CLI plugin hints: `/plugin-hints` lets your CLI prompt Claude Code users to install your plugin

---

## 6. Hooks (`settings.json`)

Shell commands (or HTTP/prompt/agent calls) that auto-run on lifecycle events.

**5 handler types:**

| Type | Description | Default timeout |
|---|---|---|
| `command` | Shell command, receives JSON on stdin. Supports `async: true` (non-blocking) and `asyncRewake: true` (background, wakes Claude on exit code 2). `shell` field: `bash` or `powershell`. | 600s |
| `http` | POST to URL with JSON body. Supports `headers` with `$VAR` interpolation and `allowedEnvVars` allowlist for env var usage. | 30s |
| `prompt` | Send to Claude model for evaluation (yes/no decisions). Optional `model` field. | 30s |
| `agent` | Spawn subagent with tool access to verify. Optional `model` field. | 60s |
| `mcp_tool` | Invoke an MCP tool directly (v2.1.118+). Lets a hook fire a Notion/Slack/etc. MCP tool without spawning a subprocess. | 30s |

**26+ hook events:**

| Category | Events |
|---|---|
| Session | `SessionStart`, `SessionEnd`, `InstructionsLoaded` |
| User input | `UserPromptSubmit` |
| Tool execution | `PreToolUse`, `PostToolUse`, `PostToolUseFailure`, `PermissionRequest`, `PermissionDenied` |
| Agent lifecycle | `SubagentStart`, `SubagentStop`, `Stop`, `StopFailure` |
| Agent teams | `TeammateIdle`, `TaskCreated`, `TaskCompleted` |
| Context | `PreCompact`, `PostCompact`, `ConfigChange` |
| File system | `FileChanged`, `CwdChanged` |
| Notifications | `Notification` |
| MCP | `Elicitation`, `ElicitationResult` |
| Worktrees | `WorktreeCreate`, `WorktreeRemove` |

**Exit codes:** 0 = success, 2 = block/deny, other = non-blocking error

**Hook configuration fields:**

| Field | Description |
|---|---|
| `type` | Required. Handler type (command, http, prompt, agent) |
| `matcher` | Regex on tool name, session source, exit reason, notification type, MCP server name |
| `if` | Permission rule syntax filter (e.g., `Bash(rm *)`, `Edit(*.ts)`) |
| `timeout` | Seconds before canceling (defaults vary by type) |
| `statusMessage` | Custom spinner message shown during hook execution |
| `async` | `true` for background command hooks (non-blocking) |
| `once` | `true` for single-run hooks (skills only) |

**Configuration scopes:**
1. `~/.claude/settings.json` (all projects)
2. `.claude/settings.json` (project, shareable)
3. `.claude/settings.local.json` (project, gitignored)
4. Managed policy settings (org-wide, cannot be overridden)
5. `managed-settings.d/` directory (modular policy deployment)
6. Plugin `hooks/hooks.json`
7. Skill/agent frontmatter

**Decision control (JSON output from hooks):**
- `continue`: boolean (false stops Claude entirely)
- `stopReason`: string shown to user when continue=false
- `suppressOutput`: boolean (omit stdout from debug log)
- `systemMessage`: warning shown to user
- `decision`: `block`, `allow`, `deny`, `ask` (top-level; for UserPromptSubmit, PostToolUse, Stop, etc.)
- `reason`: explanation string
- `hookSpecificOutput`: event-specific data (`hookEventName`, `permissionDecision`, `additionalContext`)
- PreToolUse `permissionDecision`: `allow` | `deny` | `ask` | `defer` (defer pauses execution for external UI integration in headless mode)
- PermissionDenied `retry: true` allows retry

**Key capabilities:**
- MCP tool naming: `mcp__<server>__<tool>`, supports regex like `mcp__memory__.*`
- Environment variables: `$CLAUDE_PROJECT_DIR`, `${CLAUDE_PLUGIN_ROOT}`, `${CLAUDE_PLUGIN_DATA}`, `CLAUDE_ENV_FILE` (SessionStart, CwdChanged, FileChanged), `CLAUDE_CODE_REMOTE` (true in web environments)
- PreToolUse can modify tool input before execution (`updatedInput`) and defer for external UI
- PermissionRequest can update permission rules (`updatedPermissions`), modify input, or return structured decision
- PostToolUse can replace MCP tool output (`updatedMCPToolOutput`)
- Stop hook can prevent Claude from stopping (`decision: "block"`)
- Common hook input fields: `session_id`, `transcript_path`, `cwd`, `hook_event_name`, `permission_mode`, `duration_ms` (v2.1.119+); subagents additionally receive `agent_id`, `agent_type`
- UserPromptSubmit hooks can set the session title via `hookSpecificOutput.sessionTitle` (v2.1.92+)
- Hook output over 50K saved to disk with a path + preview instead of injected into context (v2.1.86-2.1.91)
- Matcher patterns: literal strings, `|`-separated OR lists, or JavaScript regex when non-standard characters are present
- `/hooks` command to browse configured hooks
- `disableAllHooks: true` setting
- Deduplication: identical handlers run once, all matching hooks run in parallel

---

## 7. Agent Teams (Experimental)

Multiple Claude Code instances coordinating via shared task list.

**Enable:** Set `CLAUDE_CODE_EXPERIMENTAL_AGENT_TEAMS=1` in settings or environment. Requires v2.1.32+.

**How it differs from subagents:**

| | Subagents | Agent Teams |
|---|---|---|
| Context | Own window, results return to caller | Own window, fully independent |
| Communication | Report back to main agent only | Teammates message each other directly |
| Coordination | Main agent manages all work | Shared task list, self-coordination |
| Token cost | Lower | Higher (each teammate = separate instance) |

**Components:**
- Team lead: main session that creates team and coordinates
- Teammates: separate Claude Code instances
- Task list: shared, with states (pending/in-progress/completed), dependencies, and file locking
- Mailbox: inter-agent messaging

**Display modes:**
- `auto` (default): split panes if in tmux, otherwise in-process
- `in-process`: all in one terminal, Shift+Down to cycle
- `tmux`: each teammate in own tmux pane

**Features:**
- Natural language team creation and coordination
- Plan approval workflow for teammates
- Direct messaging to individual teammates
- `TeammateIdle`, `TaskCreated`, and `TaskCompleted` hooks for quality gates
- `teammateMode` setting or `--teammate-mode` flag
- File locking to prevent race conditions between teammates

**File locations:**
- Team config: `~/.claude/teams/{team-name}/config.json`
- Task list: `~/.claude/tasks/{team-name}/`

---

## 8. Platform and Runtime Features

Features that span multiple primitives or exist at the platform level.

**Context and model:**
- 1M context window: Opus 4.6 defaults to 1M context for Max/Team/Enterprise plans
- Opus 4.7 (`claude-opus-4-7`, launched 2026-04-16) with `xhigh` effort level now default in Claude Code. Material gains on hard coding, long-running agents, vision, file-system memory. Same pricing as 4.6.
- `modelOverrides` setting: map model names to custom providers or endpoints
- `effortLevel` setting: `low`, `medium`, `high`, `xhigh`, `max` (controls thinking depth globally)
- Auto mode available for Max subscribers on Opus 4.7. Two-stage classifier (input-layer prompt-injection probe + output-layer transcript check). 0.4% FPR, 17% FNR on overeager actions. Tunable via `claude auto-mode defaults`.
- **Higher-resolution vision input** (2026-04-16): images up to 2,576 px long edge (~3.75 MP), ~3x prior models. Model-level, no new parameter. Relevant for computer-use agents, dense-screenshot reading, diagram/patent/life-science extraction.
- **Task budgets** (API public beta, 2026-04-16): cap/guide token spend across a task run, per request. API only, not Claude Code CLI.
- **Claude Design** (Anthropic Labs, 2026-04-17): research-preview product on Pro/Max/Team/Enterprise. Powered by Opus 4.7 vision.
  - **Inputs:** text prompt, image upload, DOCX/PPTX/XLSX, codebase reference, web capture tool (grab elements from any URL).
  - **Outputs:** internal organization URL, folder save, Canva, PDF, PPTX, standalone HTML.
  - **Design system:** auto-generated by reading codebase + design files. Reuses your colors/typography/components on every project after that. Teams can maintain multiple systems.
  - **Refinement:** conversation, inline comments, direct edits, custom sliders made by Claude.
  - **Claude Code handoff:** one-command bundle from Design → Code for implementation.
  - **Pricing:** included with Pro/Max/Team/Enterprise within plan limits. Extra usage requires opt-in. Enterprise admins must enable.

**CLI flags:**
- `--bare`: minimal overhead for scripted `-p` calls (skips hooks, LSP, plugin sync, CLAUDE.md, memory; requires API key)
- `--add-dir`: add additional working directories
- `--agent <name>`: run entire session as a specific agent (main thread takes on agent's system prompt, tool restrictions, and model)
- `--agents`: provide agent definitions as JSON at launch (distinct from `--agent`)
- `--plugin-dir`: load plugin from local directory (repeatable)
- `--resume`: resume a previous session by ID
- `--worktree` / `-w`: start session in isolated git worktree
- `--effort`: set model effort level (low/medium/high)
- `--model`: set specific model for session
- `--channels`: permission relay for channel servers
- `--console`: Anthropic Console (API billing) auth for `claude auth login`
- `-n` / `--name <name>`: set session display name
- `--exclude-dynamic-system-prompt-sections`: print-mode flag for cross-user prompt caching
- `--teleport`: pull a web or iOS task into the terminal session
- `--print` / `-p`: headless mode now honors agent frontmatter `tools:` / `disallowedTools:` (v2.1.119+) — restrictions match interactive mode

**v2.1.116-2.1.119 additions (April 2026):**
- `prUrlTemplate` setting: custom code-review URL template (v2.1.119+)
- `CLAUDE_CODE_HIDE_CWD` env var: suppress cwd in transcript (v2.1.119+)
- `--from-pr` accepts GitLab, Bitbucket, GitHub Enterprise URLs (v2.1.119+)
- PowerShell auto-approve in permission mode (v2.1.119+)
- Hooks include `duration_ms` for tool execution timing (v2.1.119+)
- MCP servers reconnect in parallel instead of serially (v2.1.119+)
- `owner/repo#N` links use git remote host instead of always github.com (v2.1.119+)
- Vim visual mode (`v`) and visual-line mode (`V`) (v2.1.118+)
- Custom themes: create from `/theme` or hand-edit JSON in `~/.claude/themes/` (v2.1.118+)
- `DISABLE_UPDATES` env var blocks all update paths (v2.1.118+)
- WSL inherits Windows-side managed settings (v2.1.118+)
- `claude plugin tag` for release git tags (v2.1.118+)
- `--continue` / `--resume` find sessions with `/add-dir` (v2.1.118+)
- Auto mode: include `"$defaults"` in rules alongside built-in list (v2.1.118+)
- Forked subagents enabled with `CLAUDE_CODE_FORK_SUBAGENT=1` (v2.1.117+)
- Native bfs/ugrep replace Glob/Grep tools (v2.1.117+)
- Default effort for Pro/Max on Opus/Sonnet 4.6 is now `high` (v2.1.117+)
- Default effort `high` for API-key, Bedrock, Vertex, Foundry, Team, Enterprise users (v2.1.92+)
- Advisor Tool (experimental) (v2.1.117+)
- `/release-notes` interactive version picker (v2.1.111+)
- OS CA certificate store trusted by default; `CLAUDE_CODE_CERT_STORE=bundled` to opt out (v2.1.92+)
- Amazon Bedrock powered by Mantle: set `CLAUDE_CODE_USE_MANTLE=1` (v2.1.92+)
- `Ctrl+O` toggles focus mode (collapses to last prompt + tool summary + final response) in flicker-free mode (v2.1.92+)
- `/agents` tabbed layout with Running tab and `● N running` count (v2.1.92+)
- Status line `refreshInterval` setting re-runs the command every N seconds (v2.1.92+)
- Status line `workspace.git_worktree` field in JSON input (v2.1.92+)
- `CLAUDE_CODE_PERFORCE_MODE`: Edit/Write fail on read-only files with `p4 edit` hint (v2.1.92+)
- `cleanupPeriodDays` covers tasks, shell snapshots, backups (v2.1.117+)
- `claude-cli://` deep links accept multi-line prompts (encoded `%0A`) (v2.1.86+)
- `--disallowedTools`: block specific tools at session launch
- `--teammate-mode`: configure agent team display (auto/in-process/tmux)

**Deprecated tools/parameters:**
- `TaskOutput` tool: deprecated. Use `Read` on the background task output file path instead.
- Agent tool `resume` parameter: removed. Use `SendMessage({to: agentId})`.
- `PreToolUse` top-level `decision`/`reason` with `"approve"`/`"block"` values: deprecated. Moved to `hookSpecificOutput.permissionDecision` with `"allow"`/`"deny"`.

**Commands:**
- `/effort`: set/view effort level with auto-reset
- `/context`: actionable context optimization suggestions (budget, loaded files)
- `/schedule`: create/manage scheduled remote agents (cron)
- `/tui`: switch to flicker-free alt-screen rendering
- `/ultrareview`: comprehensive cloud-based code review
- `/branch`: fork session (replaces `/fork`)
- `/undo`: alias for `/rewind`
- `/btw`: side question using full context, no tool access, answer discarded
- `/desktop`: hand off terminal session to Desktop app
- `claude doctor`: diagnostics and troubleshooting
- `claude remote-control`: bridge to browser/phone
- `claude agents`: list all subagents from CLI, grouped by source
- `claude --teleport`: pull a task from web or iOS into the terminal

**Tools:**
- `ExitWorktree`: leave `EnterWorktree` sessions and return to main context
- `PowerShell` (Windows): opt-in execution tool alongside Bash (requires `CLAUDE_CODE_USE_POWERSHELL_TOOL=1`, v2.1.84+)
- `Monitor`: built-in tool (v2.1.98+) that spawns a background watcher and streams its events into the conversation as new transcript messages — Claude reacts to each event immediately. Tail logs, watch CI, auto-fix dev server crashes, all without a Bash sleep loop holding the turn open. Pairs with `/loop` (which now self-paces and can reach for Monitor to skip polling).
- `SendMessage`: resume a stopped subagent with full history (requires `CLAUDE_CODE_EXPERIMENTAL_AGENT_TEAMS=1`)
- Push notifications tool (v2.1.110+): when Remote Control is enabled and "Push when Claude decides" is on, Claude can send mobile push at long-task milestones.

**MCP capabilities:**
- Per-tool result-size override: MCP server authors set `anthropic/maxResultSizeChars` in `tools/list` response, up to 500K chars (v2.1.91+). Replaces global truncation cap when a tool genuinely needs large payloads (DB schemas, full file trees).
- Computer use is exposed via the `computer-use` MCP — toggle in `/mcp` for native-app control from CLI (research preview, v2.1.86+). Web apps already had verification loops; native iOS/macOS GUI apps now do too.

**Surfaces:**
- Terminal CLI
- VS Code extension
- JetBrains IDE extension
- Desktop App (Mac/Windows)
- Web (claude.ai/code)
- Slack integration
- GitHub/GitLab Actions
- Chrome DevTools

**Scheduling and remote:**
- Routines: cron-based long-running automation on Anthropic-managed infrastructure (run even when your machine is off, can trigger on API calls/GitHub events). Create via web, Desktop, or `/schedule` in CLI.
- Desktop scheduled tasks: cron on your own machine with local file access
- `/loop`: repeat a prompt within a CLI session for quick polling
- Remote Control: continue sessions across devices
- Dispatch: send tasks from phone/chat to Desktop app
- Channels: route events from Telegram, Discord, iMessage, webhooks

**VCS support:**
- Git (primary)
- Jujutsu metadata exclusion
- Sapling metadata exclusion

**MCP (Model Context Protocol):**
- `.mcp.json` for server configuration (project-level or plugin-level)
- Environment variables for multi-server helpers
- RFC 9728 compliance
- Agent-scoped MCP servers via `mcpServers` frontmatter field
- MCP tool naming: `mcp__<server>__<tool>`

**Security and sandbox:**
- `sandbox.failIfUnavailable`: exit on sandbox failure (was silent)
- `sandbox.enableWeakerNetworkIsolation`: macOS TLS cert verification option
- `sandbox.network.deniedDomains`: block specific domains even under wildcard allow-lists (v2.1.113+)
- `CLAUDE_CODE_SUBPROCESS_ENV_SCRUB=1`: prevent credential leaks to subprocesses
- `allowedMcpServers` / `deniedMcpServers`: managed settings to control MCP server access
- `allowedChannelPlugins`: managed setting for channel plugin allowlist
- `forceRemoteSettingsRefresh`: block startup until remote settings fetched
- `disableSkillShellExecution`: disable inline `` !`command` `` shell execution in user skills
- `disableDeepLinkRegistration`: prevent `claude-cli://` protocol registration
- Bash permission hardening (v2.1.113+): macOS `/private/{etc,var,tmp,home}` treated as dangerous for `Bash(rm:*)`; deny rules match `env`/`sudo`/`watch`/`ionice`/`setsid` wrappers; `Bash(find:*)` no longer auto-approves `-exec`/`-delete`

**Other notable settings (added Feb-April 2026):**
- `autoScrollEnabled`: disable auto-scroll in fullscreen
- `refreshInterval`: re-run status line command every N seconds
- `feedbackSurveyRate`: enterprise feedback survey sampling
- `showClearContextOnPlanAccept`: show clear-context option after plan accept
- `showThinkingSummaries`: opt-in (default removed)
- Status line: `rate_limits` field (5-hour/7-day tracking), `workspace.git_worktree`

**Additional environment variables:**
- `CLAUDE_CODE_USE_POWERSHELL_TOOL`: enable PowerShell tool (Windows opt-in)
- `ENABLE_PROMPT_CACHING_1H` / `FORCE_PROMPT_CACHING_5M`: prompt cache TTL control
- `CLAUDE_CODE_PERFORCE_MODE`: fail on read-only with `p4 edit` hint
- `CLAUDE_CODE_PLUGIN_KEEP_MARKETPLACE_ON_FAILURE`: keep cache on git pull failure
- `CLAUDE_CODE_NO_FLICKER=1`: flicker-free alt-screen rendering
- `MCP_CONNECTION_NONBLOCKING=true`: skip MCP wait in `-p` mode
- `CLAUDE_CODE_DISABLE_CRON`: stop scheduled cron jobs
- `CLAUDE_CODE_SESSIONEND_HOOKS_TIMEOUT_MS`: SessionEnd hook timeout
- `CLAUDE_CODE_MCP_SERVER_NAME` / `CLAUDE_CODE_MCP_SERVER_URL`: multi-server MCP helper config
- `OTEL_LOG_RAW_API_BODIES`, `OTEL_LOG_USER_PROMPTS`, `OTEL_LOG_TOOL_DETAILS`, `OTEL_LOG_TOOL_CONTENT`: telemetry options

**Authentication (Agent SDK):**
- Anthropic API: `ANTHROPIC_API_KEY`
- Amazon Bedrock: `CLAUDE_CODE_USE_BEDROCK=1` + AWS credentials
- Google Vertex AI: `CLAUDE_CODE_USE_VERTEX=1` + Google Cloud credentials
- Microsoft Azure: `CLAUDE_CODE_USE_FOUNDRY=1` + Azure credentials

---

## Capability Adoption Signals

Use these signals to recommend specific adoptions during an audit:

| Signal observed | Recommend |
|---|---|
| Skill output bloats main conversation | `context: fork` on that skill |
| Skill generates files or calls APIs | `disable-model-invocation: true` |
| Same delegation instructions repeated | Custom agent in `.claude/agents/` |
| Writing rules violated in output | PostToolUse hook on Edit/Write to auto-check |
| Lessons.md never updated despite corrections | Stop hook to prompt lesson capture |
| Skill needs git/API data at start | Dynamic context injection (`` !`command` ``) |
| Skill should only read, not write | `allowed-tools: Read, Grep, Glob` |
| User corrects same thing 3+ times | Extract to a rule file in `.claude/rules/` |
| Manual workflow repeated 3+ times | New skill |
| Skill descriptions over budget | Trim descriptions or `disable-model-invocation` on low-frequency skills |
| Multiple skills need same pre-check | Shared hook in settings.json |
| Skill needs specialized QA on finish | Skill-scoped PostToolUse hook |
| Rules should only apply to certain file types | Path-specific rules with `paths` frontmatter |
| Agent needs to remember across sessions | `memory` field on agent (user/project/local) |
| Complex parallel work with inter-agent coordination | Agent teams (experimental) |
| Need to validate user prompts before processing | UserPromptSubmit hook |
| Want session startup setup (env vars, context) | SessionStart hook with CLAUDE_ENV_FILE |
| Need to enforce quality gates on agent output | Stop/SubagentStop hook with decision: block |
| CLAUDE.md growing too large | Split into `.claude/rules/` files or use `@imports` |
| Same rules needed across multiple projects | Symlink rules or package as plugin |
| Need real-time code intelligence | LSP plugin (.lsp.json) |
| Subagent needs MCP tools main session doesn't | `mcpServers` field on agent (inline definition) |
| Skill should auto-activate for certain file types | `paths` frontmatter on skill |
| Need file change detection (auto-format, auto-lint) | FileChanged hook |
| Want to react when working directory changes | CwdChanged hook |
| Recurring automation on schedule | Cloud Scheduled Tasks or `/loop` |
| Need to control thinking depth per skill | `effort` frontmatter field |
| Scripted/CI usage needs minimal overhead | `--bare` flag |
| Multiple policy files for org-wide settings | `managed-settings.d/` directory |
| Agent teams need task creation quality gates | TaskCreated hook |
| Agent used as main session entry point | `initialPrompt` field on agent |
| Large monorepo with slow worktree checkouts | `worktree.sparsePaths` on agent |
| Need context budget diagnostics | `/context` command |
| Want to tail logs or watch files into Claude as notifications | Plugin `monitors/monitors.json` or `Monitor` tool |
| Headless mode needs to pause tool for external UI approval | PreToolUse hook returning `permissionDecision: "defer"` |
| Session needs to be rerouted from web or iOS to terminal | `claude --teleport` or Dispatch |
| Want long-running cron automation without keeping machine on | Routines (managed infrastructure) |
| Plugin needs to ship executables on PATH | `bin/` directory in plugin |
| Quick context-aware side question | `/btw` (no tool access, answer discarded) |
| Custom subagent status line | `subagentStatusLine` in plugin settings.json |
| Need prompt caching window control | `ENABLE_PROMPT_CACHING_1H` / `FORCE_PROMPT_CACHING_5M` env vars |
| Disable skill shell execution org-wide | `disableSkillShellExecution: true` in managed settings |
| Doing visual design work (prototypes, slides, landing pages) before building | Claude Design (Labs) — prompt-to-prototype, then one-command handoff to Claude Code |
| Need dense screenshots or high-res images readable by vision | Opus 4.7 supports 2,576 px / 3.75 MP input — no manual downsampling |
| Building an API-based agent with token-spend caps | Task budgets (API public beta) |
| Running longer autonomous sessions with guardrails | Auto mode on Opus 4.7 (tunable via `claude auto-mode defaults`) |
| Need hard-block rules in auto mode that ignore user intent + skill `allowed-tools` | `settings.autoMode.hard_deny` (v2.1.136) |
| Worktree should branch from local HEAD (uncommitted refs) instead of `origin/<default>` | `worktree.baseRef: "head"` setting (v2.1.133) |
| Quick install plugin from any zip URL without marketplace | `--plugin-url <url>` flag (v2.1.129) |
| Distribute plugin as zip archive | `--plugin-dir` accepts `.zip` (v2.1.128) |
| Run cloud `/ultrareview` non-interactively (CI / scripted) | `claude ultrareview [target] --json` (v2.1.120) |
| Bulk-clean stale Claude Code project state | `claude project purge [path] --dry-run` / `-y` / `-i` / `--all` (v2.1.126) |
| Remove unused plugin caches | `claude plugin prune` or `plugin uninstall --prune` (v2.1.121) |
| Hook should know current effort level | `effort.level` JSON input + `$CLAUDE_EFFORT` env var on hooks + Bash subprocess (v2.1.133) |
| Bash subprocess needs current session ID | `CLAUDE_CODE_SESSION_ID` env var (v2.1.132) |
| Subagent progress should reuse the prompt cache | Auto in v2.1.128+ (~3x cache_creation reduction) |
| Disable `/dangerously-skip-permissions` from blocking key dirs | Already bypassed: `.claude/`, `.git/`, `.vscode/`, shell-config writes (v2.1.121, v2.1.126) — catastrophic rm still prompts |
| MCP server should always load even if not invoked | `alwaysLoad: true` on MCP server config (v2.1.121) |
| Hook needs to override tool output for ANY tool (not just MCP) | `hookSpecificOutput.updatedToolOutput` (v2.1.121) |
| Skill content needs current effort level | `${CLAUDE_EFFORT}` substitution in skill content (v2.1.120) |

---

## v2.1.120 – v2.1.137 deltas (added 2026-05-09)

Released between 2026-04-25 and 2026-05-09. Most relevant items already injected into adoption signals above. Full list:

**New CLI flags / commands:**
- `claude ultrareview [target] --json` (v2.1.120) — non-interactive code review
- `claude project purge [path] [--dry-run] [-y] [-i] [--all]` (v2.1.126) — bulk cleanup
- `claude plugin prune` + `plugin uninstall --prune` (v2.1.121)
- `--plugin-url <url>` (v2.1.129) — install from zip URL
- `--plugin-dir` accepts `.zip` archives (v2.1.128)
- `claude auth login` accepts pasted OAuth code (v2.1.126) — WSL2/SSH/containers
- `--channels` works with console (API-key) auth (v2.1.128); `channelsEnabled: true` for managed orgs

**New settings:**
- `worktree.baseRef`: `"fresh"` (default) or `"head"` (v2.1.133)
- `parentSettingsBehavior`: `"first-wins"` or `"merge"` (v2.1.133, admin-tier)
- `sandbox.bwrapPath`, `sandbox.socatPath` (v2.1.133)
- `settings.autoMode.hard_deny`: rules array (v2.1.136)
- `skillOverrides`: `"off"` / `"user-invocable-only"` / `"name-only"` (v2.1.129, now functional)
- `alwaysLoad: true` on MCP server config (v2.1.121)

**New env vars:**
- `CLAUDE_CODE_SESSION_ID` — exposed to Bash subprocess (v2.1.132)
- `CLAUDE_EFFORT` — exposed to hooks + Bash (v2.1.133); also `${CLAUDE_EFFORT}` substitution in skills
- `CLAUDE_CODE_DISABLE_ALTERNATE_SCREEN=1` (v2.1.132)
- `CLAUDE_CODE_FORCE_SYNC_OUTPUT=1` (v2.1.129)
- `CLAUDE_CODE_PACKAGE_MANAGER_AUTO_UPDATE` (v2.1.129)
- `CLAUDE_CODE_ENABLE_GATEWAY_MODEL_DISCOVERY=1` (v2.1.129) — opt-in for `/v1/models`
- `CLAUDE_CODE_ENABLE_FEEDBACK_SURVEY_FOR_OTEL` (v2.1.136)
- `ANTHROPIC_BEDROCK_SERVICE_TIER`: `default`/`flex`/`priority` (v2.1.122)
- `AI_AGENT` — set for subprocesses (gh attribution, v2.1.120)
- `CLAUDE_CODE_FORK_SUBAGENT=1` works in non-interactive `-p`/SDK (v2.1.121)

**Hook input/output changes:**
- `hookSpecificOutput.updatedToolOutput` works for ALL tools, not just MCP (v2.1.121)
- Hooks receive `effort.level` JSON input + `$CLAUDE_EFFORT` env var (v2.1.133)

**MCP changes:**
- `alwaysLoad: true` field (v2.1.121)
- `workspace` reserved server name (v2.1.128)
- Vertex AI X.509 cert-based Workload Identity Federation / mTLS ADC (v2.1.121)
- SDK `mcp_authenticate` `redirectUri` for custom-scheme/claude.ai connectors (v2.1.121)

**Telemetry / OTel:**
- `claude_code.skill_activated` event + `invocation_trigger` attribute (v2.1.126)
- `claude_code.at_mention` log event (v2.1.122)
- `claude_code.pull_request.count` metric (v2.1.129)
- `OTEL_LOG_USER_PROMPTS` gates `user_system_prompt` on LLM spans (v2.1.121)

**Plugin manifest:**
- Plugin `themes`/`monitors` move under `"experimental": {}` in plugin.json (v2.1.129); `plugin validate` warns
- `claude plugin validate` accepts `$schema`, `version`, `description` at top of `marketplace.json` (v2.1.120)

**UX:**
- Type-to-filter search box in `/skills` (v2.1.121)
- Bare `/color` (no args) picks random session color (v2.1.128)
- Ctrl+R history search defaults to all-projects (Ctrl+S to narrow) (v2.1.129)

**Behavior changes / regressions / fixes:**
- Sub-agent progress summaries hit prompt cache (~3x cache_creation reduction, v2.1.128)
- `EnterWorktree` branched from local HEAD in v2.1.128, reverted to `fresh` default in v2.1.133 (use `worktree.baseRef: "head"` to keep prior behavior)
- `--dangerously-skip-permissions` no longer prompts for `.claude/skills/`, `.claude/agents/`, `.claude/commands/` (v2.1.121); also bypasses `.claude/`, `.git/`, `.vscode/`, shell configs (v2.1.126)
- Read tool malware-assessment reminder removed (v2.1.126)
- Gateway `/v1/models` auto-discovery now opt-in (v2.1.129)

---

## v2.1.149 – v2.1.178 deltas (added 2026-06-17)

Released 2026-05-20 to 2026-06-17 (weekly digests w22–w24; raw CHANGELOG through v2.1.178). Verified against code.claude.com whats-new, the raw CHANGELOG.md, and the hooks/skills/agents/plugins docs. Week 25 not yet published (latest week is 24). Fold the high-impact items into their numbered sections on the next major rewrite. The §6 hooks doc now enumerates many additional per-event input/output field names beyond those listed below; only the structurally new events/fields are called out here.

**Models (most impactful):**
- **Claude Opus 4.8 (`claude-opus-4-8`), launched ~2026-05-28, now the default model** for Max, Team Premium, Enterprise pay-as-you-go, and the API. Stronger coding, agentic, and long-running consistency vs 4.7; high effort by default, `/effort xhigh` for the hardest tasks. Supersedes the "Opus 4.7 default" note in §8.
- **Fast mode now runs on Opus 4.8** at $10/$50 per MTok (Week 22); `/fast` toggles it.
- **Claude Fable 5 + Mythos 5** (2026-06-09, ~v2.1.170): new model family; Fable 5 selectable as a Claude Code model via `--model` / `/model`.
- `opusplan` / `opusplan[1m]` model alias (v2.1.172): Opus for planning, switches to the configured model for execution; `[1m]` keeps 1M context.
- `availableModels` allowlist (v2.1.172) + `enforceAvailableModels` managed setting (v2.1.175), which constrains the Default model too. `ANTHROPIC_DEFAULT_OPUS_MODEL` / `ANTHROPIC_DEFAULT_SONNET_MODEL` env (v2.1.174).
- `fallbackModel` setting + `--fallback-model` flag (v2.1.166): up to three fallbacks tried in order when the primary is overloaded; now applies to interactive sessions.

**Dynamic workflows (research preview, Week 22) — the `Workflow` tool:**
- Script-driven orchestration of dozens to hundreds of subagents that Claude authors and runs in the background, for work too large for one context (codebase-wide audits, large migrations, cross-checked research). Manage runs with `/workflows`.
- Trigger keyword changed from `workflow` to **`ultracode`** (Week 23), highlighted in violet in the prompt. `/effort ultracode` (v2.1.160).
- Sub-agents can spawn sub-agents (v2.1.172): background chains capped at five levels, foreground self-limiting; subagent panel shows the full tree with descendant count and path to main.

**New commands / CLI flags:**
- `/cd` (v2.1.169): move the session to another working directory without rebuilding the prompt cache; appends the new dir's CLAUDE.md and relocates project storage so `--resume` / `--continue` find it.
- `/diff` (v2.1.149), `/insights` (v2.1.149), `/voice` (v2.1.166), `/fast` (Week 22), `/bg` (v2.1.176, background the current turn), `/advisor` (v2.1.174), `/bug` (v2.1.178), `/reload-skills` (v2.1.152), `/plugin list` (v2.1.163), `/chrome` plus `--chrome` / `--ide` launch flags (v2.1.169).
- Built-in `/init`, `/review`, `/security-review`, `/run`, `/verify` are callable through the Skill tool; others such as `/compact` are not.
- `claude --bg` background sessions and `--bg --exec '<cmd>'`; `claude rm` / `claude stop` (v2.1.160); `claude daemon status` (v2.1.176); `claude agents --json --all` adds `id` / `state` and stops omitting blocked or newly dispatched sessions (v2.1.166).
- `--safe-mode` flag + `CLAUDE_CODE_SAFE_MODE` env (v2.1.169): launch with ALL customizations disabled (CLAUDE.md, skills, plugins, hooks, MCP, custom commands/agents) while auth, model selection, built-in tools, and permissions keep working. A clean diagnostic baseline.
- `--tools` flag (Week 23) to scope the available tools at launch.

**Skills:**
- `disallowed-tools` (hyphenated) frontmatter on skills and commands removes tools from the model while the skill is active (distinct from the camelCase `disallowedTools` already documented).
- `disableBundledSkills` setting + `CLAUDE_CODE_DISABLE_BUNDLED_SKILLS` env (v2.1.166): hide bundled skills, workflows, and built-in commands from the model.
- `skillListingMaxDescChars` (per-skill cap, default 1536) / `skillListingBudgetFraction` (fraction of context for the whole listing, default 0.01) settings tune the skill-description char budget. (Verified against the live settings schema 2026-06-17.)
- Directory-qualified nested skill names (e.g. `/apps/web:deploy`) coexist with the root `/deploy`. `Skill(name)` / `Skill(name *)` permission syntax. Live skill change detection auto-reloads edited skills.

**Permissions / hooks:**
- `WebFetch(domain:*.example.com)` domain-scoped permission rule (v2.1.172); `Tool(param:value)` parameter-scoped rule (v2.1.178); glob accepted in the deny-rule tool-name position so `"*"` denies all tools (v2.1.166); unknown tool names in deny rules warn at startup.
- **Safer automatic edits** (Week 23): prompts before writing files that can execute code even under `acceptEdits`; protected paths prompt even in `acceptEdits` (v2.1.160).
- New hook events in the docs: `PostToolBatch` (`tool_calls`), `MessageDisplay` (`displayContent`), `UserPromptExpansion`, `PostToolUseFailure`. New output: `hookSpecificOutput.additionalContext` on more events (v2.1.158), `reloadSkills: true` from SessionStart (v2.1.152), `if: "Bash(...)"` filter (v2.1.163); `mcp_tool` hooks available on every event.

**Auto mode:**
- Auto mode on Bedrock / Vertex / Foundry for Opus 4.7 and 4.8 (v2.1.158). No longer requires opt-in consent (v2.1.152); `CLAUDE_CODE_ENABLE_AUTO_MODE=1`.
- Cross-session messaging hardening (v2.1.166): `SendMessage` relays from other sessions carry no user authority and auto mode blocks them.

**MCP:**
- `claude mcp get <name>` / `list` / `serve` / `reset-project-choices` / `add-from-claude-desktop`; `claude mcp add --env KEY=value`.
- `managed-mcp.json` for org-managed servers (with `allowedMcpServers` / `deniedMcpServers`); `type: "ws"` websocket transport; `streamable-http` transport.
- `ToolSearch` tool for on-demand tool-schema loading + `ENABLE_TOOL_SEARCH`; deny via `permissions.deny: ["ToolSearch"]`. `MAX_MCP_OUTPUT_TOKENS`, `MCP_TOOL_TIMEOUT`, `MCP_TIMEOUT` env vars.
- `allowAllClaudeAiMcps` setting (v2.1.149); claude.ai connectors auto-available in Claude Code (v2.1.162); `ENABLE_CLAUDEAI_MCP_SERVERS=false` to disable.

**Plugins:**
- `claude plugin init <name>` scaffolder (v2.1.157); `claude plugin marketplace remove --scope` (v2.1.152); `defaultEnabled: false` per-plugin (v2.1.154); `skipLfs` (v2.1.153); `pluginSuggestionMarketplaces` setting (v2.1.152).
- Official marketplaces `claude-plugins-official` + `claude-community` with a community submission form. `security-guidance` plugin (Week 22) reviews Claude's changes for vulnerabilities as it works.

**Settings / env / behavior:**
- `footerLinksRegexes`, `wheelScrollAccelerationEnabled` (v2.1.174), `awsCredentialExport` (v2.1.176), `CLAUDE_CODE_TMPDIR` (v2.1.162), `CLAUDE_MEMORY_STORES` (v2.1.172), `MAX_THINKING_TOKENS=0` to disable thinking (v2.1.166).
- Session titles generated in the conversation's language (v2.1.166; pin with `language`). Bedrock region read from `~/.aws` when `AWS_REGION` is unset (v2.1.166). Streaming tool execution always on (Week 22). Lean system prompt default (v2.1.154). GFM task-list checkboxes render in markdown (v2.1.149).
- Telemetry: `tool_decision` / `tool_parameters` (v2.1.157), `claude_code.lines_of_code.count` (v2.1.172), `app.entrypoint` (v2.1.152).

**Renames / deprecations to honor in the audit:**
- `/simplify` renamed to `/code-review`; cleanup-and-fix behaviour now requires `/code-review --fix` (v2.1.152). Fixed in §3 body this run.
- Bundled skill is `/fewer-permission-prompts`, not `/less-permission-prompts`. Fixed in §3 body this run.
- Windsurf surface renamed to Devin Desktop (Week 23).

**New adoption signals (for the table above):**
| Signal observed | Recommend |
|---|---|
| Task too large for one context (codebase audit, mass migration, cross-checked research) | Dynamic workflows via the `Workflow` tool (`ultracode` keyword) |
| Want a clean diagnostic baseline with all customizations disabled | `--safe-mode` / `CLAUDE_CODE_SAFE_MODE` |
| Primary model overloaded mid-run, want graceful degradation | `fallbackModel` setting + `--fallback-model` (up to 3) |
| Skill should hide specific tools from the model while active | `disallowed-tools` skill frontmatter |
| Restrict which models a session or the Default may use | `availableModels` + `enforceAvailableModels` (managed) |
| Want a vulnerability check on Claude's own edits as it works | `security-guidance` plugin |
| Move a running session to another repo without losing cache/state | `/cd` |
