# Working with Codex during a shift

Codex runs through `bash ~/.claude/skills/night-shift/codex.sh <work-dir> <output-file> <prompt-file>`. If that script is missing, the shift is Claude-only: say so in the grill, under "Split". Starting it requires the session to be in **Bypass permissions** mode. In auto mode the launch is blocked: keep the shift Claude-only, and add "switch to Bypass before leaving" under "Needs you" in the report. Start it with `run_in_background: true` so you are told when it finishes. Its last message lands in `<output-file>`. It runs with no approvals and no sandbox, so the **contract** is its only limit: always paste the contract's limits into its prompt.

## Brief

Write the prompt to `D:\work\night-shift\<date>\codex-<n>.md`:

```
You are on a night shift for the user; they are away and cannot answer.
Read ~/.codex/skills/night-shift/SKILL.md, then D:\work\night-shift\<date>\contract.md.
Your task: <task and its done criterion>
Files you own: <list>. Do not edit any other file. Claude owns the rest.
Limits: <contract limits, copied>
After each piece of work, append one line to D:\work\night-shift\<date>\log.md
(time, change, files, "codex"), and keep HANDOFF.md at the repo root current
using the checkpoint skill, so a sudden stop loses at most one piece.
Finish with a 5-line summary: done, checks run and their results, open problems.
```

## Parallel

Split by **file ownership**, so the two never edit the same file: for example, Codex takes the backend endpoint and its tests while Claude takes the Flutter screen. Both work in the same checkout and nobody commits. When Codex finishes, review its diff the way step 4.2 says before building on it.

## Codex leads

For a task the contract gives to Codex as lead, add to its brief:

```
You lead this task: plan it, do it, and decide what to hand to Claude.
To give Claude a piece, write its prompt to D:\work\night-shift\<date>\claude-<n>.md
(task, files Claude owns, contract limits, done criterion) and run:
bash ~/.claude/skills/night-shift/claude.sh <work-dir> <output-file> <prompt-file>
Claude's answer lands in <output-file>. Review it before building on it.
Hand Claude only pieces with their own files, so you never edit the same file at once.
```

Claude, as supervisor, still checks usage, writes the reports, and reviews the finished task. While Codex leads, Claude edits nothing in Codex's files and stays out of the task unless Codex hands it a piece.

## Relay

- **Claude → Codex** (Claude's window at 85%): write the checkpoint, then brief Codex with *"Continue the work in HANDOFF.md using the resume skill"* plus the contract. Start it only before 12:00, because Codex's 5-hour window must also be fresh at 17:00.
- **Codex → Claude:** Codex stops by itself when its limit hits. Claude's next scheduled restart reads `HANDOFF.md` and `log.md` and continues.
- A Codex run that exits with a limit or login error is a normal stop: note it in `log.md` and continue with Claude.
