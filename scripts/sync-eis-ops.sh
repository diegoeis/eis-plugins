#!/usr/bin/env bash
#
# sync-eis-ops.sh — copies eis-ops/ (rules.md + eis_ops.py) into each plugin as src/eis-ops/.
#
# Usage:
#   ./scripts/sync-eis-ops.sh                 every sibling repo that already has src/eis-ops/
#   ./scripts/sync-eis-ops.sh ../my-plugin    one plugin (first adoption)

set -euo pipefail

ROOT="$(cd "$(dirname "$0")/.." && pwd)"
SOURCE="$ROOT/eis-ops"
PARENT="$(dirname "$ROOT")"

if [[ $# -gt 0 ]]; then
  targets=("$@")
else
  targets=()
  for d in "$PARENT"/*/ "$PARENT"/working/*/; do
    [[ -d "$d/src/eis-ops" ]] && targets+=("$d")
  done
fi

for t in "${targets[@]}"; do
  t="$(cd "$t" && pwd)"
  mkdir -p "$t/src/eis-ops"
  cp "$SOURCE/rules.md" "$SOURCE/eis_ops.py" "$t/src/eis-ops/"
  echo "synced: $t/src/eis-ops"
done
