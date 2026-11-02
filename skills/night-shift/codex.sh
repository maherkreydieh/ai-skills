#!/usr/bin/env bash
set -euo pipefail
CODEX=$(command -v codex 2>/dev/null || ls -t /c/Users/Lenovo/AppData/Local/OpenAI/Codex/bin/*/codex.exe 2>/dev/null | head -1)
[ -n "$CODEX" ] || { echo "codex CLI not found" >&2; exit 1; }
"$CODEX" exec ${CODEX_MODEL:+-m "$CODEX_MODEL"} --dangerously-bypass-approvals-and-sandbox --skip-git-repo-check -C "$1" -o "$2" - < "$3"
