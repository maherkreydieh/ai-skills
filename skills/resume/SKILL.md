---
name: resume
description: Pick up earlier work from HANDOFF.md and the auto git snapshot. Use for "resume", "where were we", or starting a new chat on unfinished work.
---

Rebuild context cheaply, then hand the user a three-line brief.

1. Read `HANDOFF.md` at the repo root.
2. Read `.ai/auto-snapshot.md` if it exists (a script writes it after each session: branch, recent commits, changed files).
3. Run `git status --short` and `git log --oneline -5`. Trust git over the handoff when they disagree, and say so.
4. Read only the files the "In progress" and "Next step" sections name.

Reply with exactly three lines:
- **Where we are:** …
- **Next step:** …
- **Waiting on you:** … (or "nothing")

Done when the user can say "go" without explaining anything. Start the next step only after they confirm.
