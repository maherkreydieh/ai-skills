---
name: night-shift
description: Unattended work shift with Codex while the user sleeps or is at work, ending in a report. Use for "night shift", "going to sleep", "going to work", or "I'm back" (show the report).
---

The user is leaving. Run a **shift**: agree a **contract** in under two minutes, then work alone until the shift ends, and leave a report they can read half-asleep.

Shift folder: `D:\work\night-shift\<YYYY-MM-DD>\` (the date the shift started). It holds `contract.md`, `log.md`, and the reports. If the user says **"I'm back"**, skip to step 6.

## The user's day (local time, UTC+2)

| Time | User is | Shift rule |
|---|---|---|
| ~00:00–06:30 | asleep | work |
| 06:30 | waking, little time | **morning brief** ready by 06:15 |
| ~07:00–17:00 | at work | work until the **noon cutoff** |
| 13:00–14:00 | on break, checks phone | **break update** already on the phone |
| 17:00–24:00 | working with Claude and Codex | must find both 5-hour windows fresh |

- **Noon cutoff:** a 5-hour window started after 12:00 would still be running at 17:00. Neither tool may *start* a new window after 12:00. Work inside an already-open window may continue until it runs out or 16:30, whichever is first.
- **Pace line:** the share of the weekly limit that would be used if usage were spread evenly, `100 × hours since weekly reset ÷ 168`. Get the reset time from `get_usage`. The shift stops spending Claude usage once weekly `percentUsed` reaches the pace line, so the user's evenings stay covered.

## 1. Brief (yourself, about 1 minute)

Collect facts so the user only has to decide:
- the latest `report.md` in `D:\work\night-shift\` (the last shift's result and its "next direction");
- `git status --short` and `git log --oneline -8` in the current repo, plus `HANDOFF.md` and `.ai/auto-snapshot.md` if they exist;
- the 3 most recent chat transcripts (see [TASTE.md](TASTE.md) for where they live): what was the user working on, and what did they say was next?
- `get_usage`: Claude's 5-hour and weekly percentage, the weekly reset, and the pace line;
- Codex's weekly percentage and reset date (from the last shift's `log.md` or Codex's `/status`; if unknown, ask in question 2).

From these, **predict** the work the user most likely wants done next.

## 2. Grill (one round, the user answers in under 2 minutes)

Ask **one round** in the `grilling` format, at most 4 questions, each worded so "yes" accepts your recommendation:

1. **Tasks:** your predicted task(s), in one line each, with what "done" looks like.
2. **Split:** for each task, name the **lead**: Claude or Codex, whichever suits it better. The lead plans the task and may hand pieces to the other. Then choose how they share it: the lead alone, both in parallel (name who owns which files), or a **relay** (one starts, the other continues when its limit hits). Choose whatever finishes soonest within the limits. **Weekly limits decide who does the heavy work:** usage left before a reset is lost at the reset, so the tool whose weekly limit resets sooner (with room left) takes the bulk, and the tool with a later reset gets only small, separate pieces. State both percentages and reset dates in the question.
3. **Contract limits:** the things to avoid tonight. Start from the project's `AGENTS.md`/`CLAUDE.md` rules (for example: no commits/pushes, no production databases, no deleting user files, no spending money), and add anything the task needs. Also name the **access** the task needs that you lack, so it is settled before the user leaves: a test login to see signed-in screens, a running app or device, a file or link.
4. **End:** shift end time (default: the noon cutoff on a workday, or the time they name).

Close with: *"Reply 'yes' to accept all, or correct any number."* A reply of "yes", "go", or "sleep" accepts every recommendation. Do not ask a second round. Settle any leftover detail yourself and write it in the contract.

Then tell the user, in one line, to switch this session to **Bypass permissions** in the mode menu so no approval prompts block the night. Scheduled restarts inherit that mode. Changing it is the user's click, never yours.

## 3. Launch

1. Write `contract.md`: tasks with their done criteria, split, limits, end time, the pace line at the start, and the 5-hour reset time.
2. `request_keep_awake` with `until: "session_idle"`.
3. Schedule with `create_scheduled_task` (one-time `fireAt`, self-contained prompt: *"Use the night-shift skill. Continue the shift in `D:\work\night-shift\<date>\` from `contract.md` and `log.md`."*):
   - a **restart** at each upcoming Claude 5-hour reset that falls before the end time and before the noon cutoff;
   - a **break update** at 11:45 (before the noon cutoff, so it opens no new window). On a shift that ends sooner, send the break update at the end instead.
4. Give Codex its work as [CODEX.md](CODEX.md) describes, if the split includes Codex. Claude always stays the **supervisor**: grill, schedule, usage checks, review, and reports, even on tasks Codex leads.

## 4. Work loop

Repeat until the end time, the noon cutoff, or the pace line. These and the 85% window rule are the only reasons to stop; unused usage is wasted, and a large pile of work to review is handled by a clear report, not by stopping early:

1. Do the next piece of the current task. After each piece, append one line to `log.md`: time, what changed, files touched, and who did it.
2. When a task looks finished, **review it** before calling it done. It is done only when:
   - the project's checks pass: build, analyze/lint, and the tests that cover the change;
   - the `code-review-and-quality` skill finds nothing serious;
   - it fits the user's taste in `C:\Users\Lenovo\.claude\taste.md` (if that file exists);
   - you would show it to the user without excuses.
   If any check fails, fix it and review again. Codex's output gets the same review.
3. With the contracted tasks done, choose the **next** most useful thing inside the contract, in this order: what the finished work exposed (a bug, a missing test, a rough screen) → the repo's `HANDOFF.md` next steps → the "next direction" from the last report. Note the reason in `log.md`.
4. When there is nothing useful left inside the contract, or only usage is left, study the user's taste ([TASTE.md](TASTE.md)).
5. **Limits:** check `get_usage` after each task. At 85% of the 5-hour window, run the `low-usage` and `checkpoint` skills, relay to Codex ([CODEX.md](CODEX.md)) if the noon cutoff allows, and stop; the scheduled restart picks the work back up with the `resume` skill. When a restart fires, run `resume` against the repo's `HANDOFF.md`, read `log.md`, and check whether Codex is still running before touching its files.

Anything the contract does not settle and that you cannot undo: skip it, note it under "Needs you" in the report, and continue with something else.

## 5. Reports

Write and send the reports as [REPORT.md](REPORT.md) describes: the morning brief at 06:15 (sleep shifts), the break update at 11:45, and `report.md` when the shift ends.

## 6. "I'm back"

Open the newest `D:\work\night-shift\*\report.md`, send it with `SendUserFile`, and reply with its TL;DR and the one recommended next step.

The shift is done when `report.md` exists, every contracted task is either done (it passed review) or listed under "Needs you" with a reason, no window was started after the noon cutoff, and the user has been sent the report.
