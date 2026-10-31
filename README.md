# ai-skills

My agent skills for working with Claude Code and Codex on a budget.

I'm a junior developer building a mobile app (Flutter + Spring Boot) with AI agents on $20 plans. These skills cover the gaps I kept hitting: losing context between chats and tools, running out of usage mid-task, long answers, and too many decisions at once.

They stand on the shoulders of three collections I use every day: [pstack](https://github.com/cursor/plugins/tree/main/pstack) by Lauren Tan, [Skills For Real Engineers](https://github.com/mattpocock/skills) by Matt Pocock, and [Agent Skills](https://github.com/addyosmani/agent-skills) by Addy Osmani. The full list of what I use, and why, is in [SKILLS.md](SKILLS.md).

## My skills

| Skill | Use it when |
|---|---|
| [handoff](skills/handoff/SKILL.md) | you're stopping, switching tools, or running out of usage |
| [resume](skills/resume/SKILL.md) | you're picking up earlier work in a new chat |
| [low-usage](skills/low-usage/SKILL.md) | your usage limit is close and you want to save tokens |
| [brain-dump](skills/brain-dump/SKILL.md) | your head is full and you need one next step |
| [plan-today](skills/plan-today/SKILL.md) | you want today's plan from your Notion Inbox |

`handoff` and `resume` work together across Claude Code, Codex, and your phone, because the handoff lives in the repo, not in a chat.

## Install

**Claude Code:** copy a skill folder into `~/.claude/skills/`, for example:

```bash
cp -r skills/handoff ~/.claude/skills/
```

**Codex:** copy it into `~/.codex/skills/`.

Type `/handoff` (Claude Code) or `$handoff` (Codex), or just say "handoff". The agent picks a skill up from its description.

## Optional: zero-token snapshot

`resume` also reads `.ai/auto-snapshot.md`, a tiny git summary written by a script after every Claude Code session. It uses no tokens. See [`hooks/handoff-snapshot.sh`](hooks/handoff-snapshot.sh).

## License

MIT. Fork it and make it yours.
