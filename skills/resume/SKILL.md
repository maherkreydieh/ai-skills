---
name: resume
description: Pick up earlier work from its checkpoint and the auto git snapshot. Use for "resume", "where were we", or starting a new chat on unfinished work.
---

Rebuild context cheaply, then hand the user a three-line brief.

1. Find the checkpoint the **checkpoint** skill wrote:
   - in a git repo → `HANDOFF.md` at the repo root, plus `.ai/auto-snapshot.md` if it exists (a script writes it after each session);
   - otherwise → ask which task, then look in `D:\work\<task-name>\HANDOFF.md` or the matching sub-page under the Handoffs page named in the user's personal rules.
2. In a repo, run `git status --short` and `git log --oneline -5`. Trust git over the checkpoint when they disagree, and say so.
3. Read only the files or pages the "In progress" and "Next step" sections name.

Reply with exactly three lines:
- **Where we are:** …
- **Next step:** …
- **Waiting on you:** … (or "nothing")

Done when the user can say "go" without explaining anything. Start the next step only after they confirm.
