# Shift reports

The user reads these sleepy, at work, or on a phone. Write in plain words, start with the outcome, and keep each report to one phone screen. Every report goes to three places:
1. **Notion (the phone copy, the one the user reads):** one page per shift under the Handoffs page (40aaa86e-c6c7-81e5-8499-cca6a7248dde), titled `Night shift — <date>`. Create it with the morning brief, then add each later report to it (add only). Put its link in `contract.md`.
2. A file in the shift folder, sent with `SendUserFile` (status `proactive`).
3. One `PushNotification` under 200 characters, leading with what the user should act on and naming the Notion page. It is often skipped while the chat is open, so never rely on it alone.

Scheduled runs happen in their own new session, which the user does not watch. So also post the report's TL;DR and file path into the session the shift started from, with `mcp__ccd_session_mgmt__send_message` to the `Main session:` id in `contract.md`. That is where the user looks first. For the phone, also put each report on a Notion page under the Handoffs page (40aaa86e-c6c7-81e5-8499-cca6a7248dde): one page per shift, add only.

## Morning brief: `morning.md`, 06:15 (sleep shifts only)

At most 5 lines. The user has a minute before work.

```
**TL;DR:** <one line: state of tonight's task>
- Done: …
- Still running until <time>: …
- Needs you (only if blocking): … (or "nothing")
To add a task before work, reply from your phone in one line; I'll fit it into the contract.
```

## Break update: `break.md`, 11:45

At most 8 lines: what is finished, what is still running until the end, anything waiting on them, and what they will come home to. Remind them that replying starts a 5-hour window, so a reply is best kept to one line.

## Final report: `report.md`, when the shift ends

```
# Shift report — <date>
**TL;DR:** <one line, bold the key point>

## You asked for
<each contracted task in the user's own words, because they forget>

## Result
| Task | Status | Where | How to check it (phone or laptop) |

## Also done
<work picked under step 4.3, with the reason>

## Needs you
<decisions, skipped irreversible steps, with a recommended answer each>

## Usage
Claude 5h / weekly: …  ·  pace line: …  ·  Codex runs: …

## Next direction
<ONE recommended next step for tonight's session, and why>
```

"How to check it" names something concrete: a screen to open on the phone, a command to run, a file to look at.
