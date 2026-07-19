#!/usr/bin/env bash
# Runs via restic-backup.service. Requires /etc/restic/backup.env (root:root 0600)
# providing RESTIC_REPOSITORY, RESTIC_PASSWORD_FILE, and BACKUP_PATHS.
set -euo pipefail

: "${RESTIC_REPOSITORY:?}" "${RESTIC_PASSWORD_FILE:?}" "${BACKUP_PATHS:?}"

restic backup ${BACKUP_PATHS} \
  --exclude-caches \
  --exclude '**/.cache' \
  --exclude '**/node_modules' \
  --exclude '/opt/stack/**/tmp' \
  --one-file-system \
  --tag scheduled

restic forget --prune \
  --keep-daily 7 \
  --keep-weekly 4 \
  --keep-monthly 6 \
  --tag scheduled

restic check --read-data-subset=2%
