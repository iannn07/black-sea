#!/usr/bin/env bash
# BLACK SEA installer for Claude Code.
#   ./install.sh            -> personal skill at ~/.claude/skills/black-sea  (command: /black-sea)
#   ./install.sh --project  -> project skill at ./.claude/skills/black-sea
set -euo pipefail

HERE="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
SRC="$HERE/skills/black-sea"

if [ ! -f "$SRC/SKILL.md" ]; then
  echo "error: skill source not found at $SRC" >&2
  exit 1
fi

if [ "${1:-}" = "--project" ]; then
  DEST="$(pwd)/.claude/skills/black-sea"
  SCOPE="project ($(pwd)/.claude/skills)"
else
  DEST="$HOME/.claude/skills/black-sea"
  SCOPE="personal (~/.claude/skills)"
fi

mkdir -p "$(dirname "$DEST")"
rm -rf "$DEST"
cp -r "$SRC" "$DEST"

echo "BLACK SEA installed → $SCOPE"
echo "  path: $DEST"
echo "Restart Claude Code, then run:  /skills   and   /black-sea"
command -v python3 >/dev/null 2>&1 || echo "note: python3 not found on PATH — the forensics calculator needs it."
