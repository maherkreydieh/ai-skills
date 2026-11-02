# Skills catalog

Every skill I use, where it comes from, and why. Last reviewed: 2026-10-31.

**Legend:** 🟢 using now · 🟡 later (when I have more usage or need it) · ⚪ considered, skipped

---

## A. My own skills

These live in [`skills/`](skills/). They were written after studying the three collections below, and borrow their ideas where credited.

| Skill | What it does | Starts when | Inspired by | Status |
|---|---|---|---|---|
| [checkpoint](skills/checkpoint/SKILL.md) | Saves where the work stands: `HANDOFF.md` in the repo, a local private folder for code with no repo, or a Notion page for non-code tasks | "checkpoint", ending a session, usage running out | Matt Pocock's `handoff` (redact secrets, point to artifacts, suggest skills). Mine saves where Codex and my phone can read it, and is named differently to avoid clashing with his | 🟢 draft |
| [resume](skills/resume/SKILL.md) | Reads the checkpoint + auto git snapshot and says in 3 lines where things stand | "resume", starting a new chat on old work | pstack's `recall` and session-pickup playbook | 🟢 draft |
| [low-usage](skills/low-usage/SKILL.md) | When usage is low, guides me to do easy steps myself instead of spending tokens | "low", "usage is low" | Nothing similar exists | 🟢 draft |
| [brain-dump](skills/brain-dump/SKILL.md) | Takes a messy worried brain dump, sorts it, picks one next step | "brain dump", "I'm overwhelmed" | Matt Pocock's `grilling` (one recommendation per question) | 🟢 draft |
| [plan-today](skills/plan-today/SKILL.md) | Builds today's plan from my Notion Inbox | "plan today", morning | pstack's `ketchup` (decisions listed with a pick) | 🟢 draft |
| [night-shift](skills/night-shift/SKILL.md) | Unattended work shift with Codex while I sleep or work: 2-minute grill, contract, Claude/Codex split by limits, review loop, reports on Notion | "night shift", "going to sleep", "going to work", "I'm back" | Matt Pocock's `grilling` + `writing-for-agents`; Addy's `code-review-and-quality` for the review loop | 🟡 tested once |

Dropped from my original list because a borrowed skill already does the job:
- *explain-review* → covered by pstack `blast-radius` + `bro`
- *model-router* → covered by pstack `setup-pstack`

---

## B. Skills I use from others

All three collections are **MIT licensed**. pstack is installed as a plugin. From Matt and Addy I copy only the skills I use (🟢), each with its license and a SOURCE.md crediting the author, and refresh them monthly.

### Lauren Tan (poteto) — pstack
**Repo:** [cursor/plugins/pstack](https://github.com/cursor/plugins/tree/main/pstack) · **License:** MIT · **61 skills** · Built for Cursor, with a Claude Code adapter.
**Install (Claude Code):** `/plugin marketplace add cursor/plugins` then `/plugin install pstack@cursor-plugins`

| Skill | What it does | Why I use it | Status |
|---|---|---|---|
| `ketchup` | Catches me up on what changed, in plain words, with every decision waiting on me and a recommended pick | Long replies lose me; this gives me just the decisions | 🟢 |
| `bro` | Restates the last message in plain language | When a reply is too technical | 🟢 |
| `in-your-own-words` | Agent repeats back my goal before starting | Catches misunderstandings early, before tokens are spent | 🟢 |
| `sharpen` | Makes my prompt deeper (what a pro would add) without doing the task | I'm not sure what to ask for | 🟢 |
| `teach` | Explains a change or system step by step with diagrams | I want to learn, not only ship | 🟢 |
| `blast-radius` | Finds what a small change could break, proven by running code | I can't spot bugs by reading code yet | 🟢 |
| `setup-pstack` | Picks which model does which job | Stops me thinking about model choice | 🟢 |
| `principle-prove-it-works` | Verify the real result before saying "done" | Trust | 🟢 |
| `create-verification-skill` | Builds a project skill that tests the app like a user would | Builds trust before running agents in parallel | 🟡 |
| `automate-me` | Drafts a personal skill from how I actually work | The December habit review | 🟡 |
| `correct` | Finds mistakes agents repeat and blocks them for good | After a month of use | 🟡 |
| `poteto-mode` | Full rigorous workflow with 23 playbooks | Heavy: many subagents and models. Wait until I have more usage | 🟡 |
| `interrogate`, `arena`, `swarm` | Several agents or models attack or compete on the same task | Expensive on a $20 plan | 🟡 |
| `make-bot-ui` | Dashboards that wake a Grok Bot | Grok Bot isn't something I can use yet | ⚪ |
| `typescript-best-practices` | TypeScript rules | My app is Dart + Java | ⚪ |

### Matt Pocock — Skills For Real Engineers
**Repo:** [mattpocock/skills](https://github.com/mattpocock/skills) · **License:** MIT · **39 skills** · Works with Claude Code **and Codex**.
**How I install:** copy `grilling`, `grill-me`, `diagnosing-bugs`, `writing-for-agents` into `~/.claude/skills/` and `~/.codex/skills/`. To try his full set instead: `codex plugin marketplace add mattpocock/skills` then `codex plugin add mattpocock-skills@mattpocock`.

| Skill | What it does | Why I use it | Status |
|---|---|---|---|
| `grill-me` / `grilling` | Interviews me in rounds, with a recommended answer for every question | I struggle with decisions | 🟢 |
| `writing-for-agents` | How to write skills and AGENTS.md well | The guide I followed to write my own skills | 🟢 |
| `diagnosing-bugs` | Step-by-step loop for hard bugs | Debugging without guessing | 🟢 |
| `improve-codebase-architecture` | Scans for weak structure, shows a visual report | Is my architecture OK for the future? | 🟡 |
| `prototype` | Throwaway prototype to test an idea cheaply | Deciding UI or logic | 🟡 |
| `handoff` | Handoff doc saved to a temp folder | Replaced by my own `checkpoint` (saved where every tool can read it) | ⚪ |
| `code-review` | Review against standards + spec | Needs an issue tracker set up; Addy's review fits better now | ⚪ |
| `wait-what` | Re-pitch the last message | Needs a GLOSSARY.md; pstack `bro` does this | ⚪ |
| `tdd` | Test-first development | Overlaps with others; add later | 🟡 |

### Addy Osmani — Agent Skills
**Repo:** [addyosmani/agent-skills](https://github.com/addyosmani/agent-skills) · **License:** MIT · **25 skills** · Long, detailed skills (200–400 lines each), so they cost more tokens when they run.
**How I install:** copy `code-review-and-quality` (with its two checklists) and `security-and-hardening` into `~/.claude/skills/` and `~/.codex/skills/`. To try his full set instead: `/plugin marketplace add addyosmani/agent-skills` then `/plugin install agent-skills@addy-agent-skills`.

| Skill | What it does | Why I use it | Status |
|---|---|---|---|
| `code-review-and-quality` | Five-axis review before merging | A senior-style review I can't do myself yet | 🟢 |
| `security-and-hardening` | Checks inputs, auth, data storage | My app has logins and user data | 🟢 |
| `api-and-interface-design` | Stable API contracts | Keeps Flutter and Spring Boot in sync | 🟡 |
| `performance-optimization` | Measures and fixes slowness | When the app has more users | 🟡 |
| `interview-me` | One-question-at-a-time interview | Matt's `grilling` gives recommendations, which suits me better | ⚪ |
| `using-agent-skills` | Meta-skill that routes to other skills | Claude Code and Codex already route skills | ⚪ |

---

## Keeping it lean

Every installed skill's description loads into every chat, so I install only what I use.
- Claude Code's `skillOverrides` setting does **not** switch off skills from plugins you install yourself (checked on v2.1.309), so for Matt's and Addy's collections I copy just the skills I want instead.
- pstack stays a plugin: most of its skills are type-only by design, so they cost almost nothing until used.
- To use a 🟡 skill, copy it in when I need it.
- Review this catalog monthly and refresh the copied skills from their source.
