# Inbox Organizer for Claude Code

**Agent skill.** Sorts your inbox into seven labels, archives what does not need you, and drafts the replies. Never sends, never deletes.

## Install

Copy [`INSTALL-PROMPT.md`](INSTALL-PROMPT.md) and paste it into your AI agent (Claude Code, Cursor, or similar). It detects what you already have, connects to your inbox over IMAP with an app password, builds the organizer on your own machine, and runs it. Setup is about 15 minutes.

## What's here

- `INSTALL-PROMPT.md`: the runbook you paste. Your AI builds the organizer from it.

## Guarantees

Never sends mail (it writes drafts, you hit send). Never deletes received mail (archive just moves it out of the inbox and is reversible). Runs entirely on your own machine and inbox.

Live preview: [donatassimkus.com/ai-skills/inbox-organizer](https://donatassimkus.com/ai-skills/inbox-organizer)
