---
name: plan-today
description: Build today's plan from the Notion Inbox. Use for "plan today", "what should I do today", or a morning check-in.
---

Make a short, realistic plan for today from the user's Notion Inbox (the database named in their personal rules).

1. Query Inbox items with Status "New" or "Sorted", plus anything whose When date is today or overdue.
2. Sort new items: set Type and Status. Ask only about items you can't place.
3. Pick at most **3 things for today**: one main task, two small ones. Prefer items that unblock others. Respect usage limits: put AI-heavy tasks where there's usage left.
4. If weekly usage is high and resets soon, add one "Ready for AI" item to spend it well.

Reply in this shape:
- **Today's main thing:** … (why it's first, one line)
- **Small ones:** …, …
- **Parked:** count of items left for later
- **Waiting on you:** any decision, with your recommended pick

Done when the user has three or fewer items for today and every Inbox item has a Type.
