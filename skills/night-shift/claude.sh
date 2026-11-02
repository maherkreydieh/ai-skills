#!/usr/bin/env bash
# Let Codex hand Claude a task during a night shift (no approval pop-ups; auto mode's safety check still applies).
# Usage: claude.sh <work-dir> <output-file> <prompt-file>
set -euo pipefail
CLAUDE=$(command -v claude 2>/dev/null || echo /c/Users/Lenovo/.local/bin/claude.exe)
[ -x "$CLAUDE" ] || { echo "claude CLI not found" >&2; exit 1; }
cd "$1"
"$CLAUDE" -p --permission-mode auto < "$3" > "$2"
