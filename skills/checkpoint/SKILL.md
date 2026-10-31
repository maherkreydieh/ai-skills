---
name: checkpoint
description: Save where the work stands so any agent or device can continue. Use for "checkpoint", "save my place", switching tools, ending a session, or when usage is running out.
argument-hint: "What will the next session focus on?"
---

Write a checkpoint so a fresh agent (Claude Code, Codex, or a phone session) can continue without re-explaining.

## Where it goes

- **Inside a git repo** → `HANDOFF.md` at the repo root. Overwrite the previous one; git history keeps old versions.
- **Code task with no repo** → create `D:\work\<task-name>` (or ask once for the user's preferred folder), run `git init`, put the work and `HANDOFF.md` there. It stays private on this machine. Push to a private remote only if the user asks.
- **Non-code task** (research, planning, writing) → a sub-page named `<task-name>` under the Handoffs page named in the user's personal rules. If no Notion tool is available, write `HANDOFF.md` in the current folder and say so.

## What it says

At most ~30 lines, in this shape:

```
# Checkpoint — <date> — <tool that wrote it>
## Goal
## Done
## In progress (exact file or page + what's half-finished)
## Next step (one concrete action)
## Open questions for the human
## Suggested skills for the next agent
```

- Point to artifacts by path or link (specs, commits, diffs, issues) instead of copying them.
- Redact secrets: API keys, passwords, tokens, personal data.
- If the user passed arguments, tailor "Next step" to that focus.
- Leave `.ai/auto-snapshot.md` alone; a script maintains it.

Done when the checkpoint exists, a stranger could name the next action from it alone, and you've told the user where it is in one line.
