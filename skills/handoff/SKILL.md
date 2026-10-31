---
name: handoff
description: Save the current work to HANDOFF.md in the repo so any agent or device can continue. Use for "handoff", ending a session, or when usage is running out.
argument-hint: "What will the next session focus on?"
---

Write `HANDOFF.md` at the repository root so a fresh agent (Claude Code, Codex, or a phone session) can continue without re-explaining. Overwrite the previous one; git history keeps old versions.

Use this shape, at most ~30 lines:

```
# Handoff — <date> — <tool that wrote it>
## Goal
## Done
## In progress (exact file + what's half-finished)
## Next step (one concrete action)
## Open questions for the human
## Suggested skills for the next agent
```

Rules:
- Point to artifacts by path or link (specs, commits, diffs, issues) instead of copying them.
- Redact secrets: API keys, passwords, tokens, personal data.
- If the user passed arguments, tailor "Next step" to that focus.
- Leave `.ai/auto-snapshot.md` alone; a script maintains it.

Done when the file exists, a stranger could name the next action from it alone, and you've told the user its path in one line.
