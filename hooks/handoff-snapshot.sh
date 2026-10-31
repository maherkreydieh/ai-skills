#!/usr/bin/env bash
# Zero-token safety net: after each Claude turn, save a small git snapshot
# to <repo>/.ai/auto-snapshot.md so work can be resumed if usage runs out.
# It overwrites the file each time (never grows) and is git-ignored locally.

dir="${CLAUDE_PROJECT_DIR:-$PWD}"
root=$(git -C "$dir" rev-parse --show-toplevel 2>/dev/null) || exit 0

mkdir -p "$root/.ai"

# Keep the snapshot out of git without touching the project's .gitignore.
exclude="$(git -C "$root" rev-parse --git-common-dir)/info/exclude"
case "$exclude" in /*|[A-Za-z]:*) ;; *) exclude="$root/$exclude" ;; esac
mkdir -p "$(dirname "$exclude")"
grep -qxF '.ai/auto-snapshot.md' "$exclude" 2>/dev/null || echo '.ai/auto-snapshot.md' >> "$exclude"

{
  echo "# Auto snapshot (written by script, not AI)"
  echo
  echo "- Time: $(date '+%Y-%m-%d %H:%M')"
  echo "- Branch: $(git -C "$root" branch --show-current)"
  echo
  echo "## Last commits"
  git -C "$root" log --oneline -3
  echo
  echo "## Uncommitted files (first 30)"
  git -C "$root" status --short | head -30
} > "$root/.ai/auto-snapshot.md"
