# Studying the user's taste (idle time only)

Goal: a short, evidence-based profile in `C:\Users\Lenovo\.claude\taste.md` that makes future work match how the user thinks. Current focus areas: **app development** (Flutter, Spring Boot), **web design**, and **content creation**.

## Sources

- Claude Code chats: `C:\Users\Lenovo\.claude\projects\*\*.jsonl` (one file per chat). The user's own messages are the lines with `"type":"user"`.
- Codex chats: `C:\Users\Lenovo\.codex\sessions\<year>\<month>\<day>\*.jsonl`, with `session_index.jsonl` listing them.
- Feedback already given: `C:\Users\Lenovo\.claude\CLAUDE.md` and the memory folder. Capture only what these do not already say.

Read the user's messages, never secrets: skip anything that looks like a key, password, token, or personal data. Work in batches of about 10 chats, newest first, and note in `log.md` which chats were covered so the next shift starts where this one stopped.

## What counts as taste

Look for **patterns** backed by at least two moments: what they praised, what they rejected or asked to redo, words they repeat, design choices they made (colours, layout density, tone), and how they make decisions. A one-off remark is a note, not a pattern.

## File format

Keep `taste.md` under ~80 lines, grouped by area. Merge new findings into the existing lines instead of appending duplicates:

```
# How the user works and what they like
## Working style
- <pattern> — seen in <chat date/topic>, <chat date/topic>
## App development
## Web design
## Content creation
## Open guesses (one sighting; confirm later)
```

Each line is something an agent can act on ("prefers compact rows over cards in lists"), not a personality description.
