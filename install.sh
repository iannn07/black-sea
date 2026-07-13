#!/usr/bin/env bash
# BLACK SEA installer for Claude Code — installs the whole unit (every skill in this plugin:
# the black-sea orchestrator, the WAYPOINT front door, the operatives, and BULKHEAD).
#   ./install.sh            -> personal skills at ~/.claude/skills/   (commands: /black-sea, /waypoint, ...)
#   ./install.sh --project  -> project skills at ./.claude/skills/    (commit for your team)
set -euo pipefail

HERE="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
SRC="$HERE/skills"

if [ ! -d "$SRC" ] || [ ! -f "$SRC/black-sea/SKILL.md" ]; then
  echo "error: skills source not found at $SRC" >&2
  exit 1
fi

if [ "${1:-}" = "--project" ]; then
  DEST="$(pwd)/.claude/skills"
  SCOPE="project ($(pwd)/.claude/skills)"
else
  DEST="$HOME/.claude/skills"
  SCOPE="personal (~/.claude/skills)"
fi

mkdir -p "$DEST"
count=0
for skill in "$SRC"/*/; do
  [ -f "$skill/SKILL.md" ] || continue
  name="$(basename "$skill")"
  rm -rf "$DEST/$name"
  cp -r "$skill" "$DEST/$name"
  echo "  installed: $name"
  count=$((count + 1))
done

echo "BLACK SEA unit installed ($count skills) → $SCOPE"
echo "Restart Claude Code, then run:  /skills   and   /black-sea"
command -v python3 >/dev/null 2>&1 || echo "note: python3 not found on PATH — PLIMSOLL's forensics calculator needs it."
