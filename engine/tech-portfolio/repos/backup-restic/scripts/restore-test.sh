#!/usr/bin/env bash
# Quarterly restore drill: restore latest snapshot to scratch, verify a sentinel.
# The sentinel (~/.backup-sentinel) is a dated file the backup set must contain.
set -euo pipefail

: "${RESTIC_REPOSITORY:?}" "${RESTIC_PASSWORD_FILE:?}"
SCRATCH="$(mktemp -d /var/tmp/restic-restore-test.XXXXXX)"
trap 'rm -rf "$SCRATCH"' EXIT

echo "Restoring latest snapshot to $SCRATCH ..."
restic restore latest --target "$SCRATCH"

SENTINEL="$(find "$SCRATCH" -name '.backup-sentinel' -print -quit)"
if [[ -z "$SENTINEL" ]]; then
  echo "FAIL: sentinel file not found in restored data" >&2
  exit 1
fi

echo "PASS: sentinel restored, dated $(cat "$SENTINEL")"
echo "Record this run in docs/restore-runbook.md (date, elapsed, snapshot id)."
