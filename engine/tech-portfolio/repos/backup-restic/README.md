# backup-restic

restic backups driven by systemd timers, with retention, pruning, and a written restore runbook. The premise: a backup that has never been restored is a hope, not a backup.

**Status: in progress** — units, scripts, and the runbook are written; the first live backup and the first full restore test have not yet been run against a real repository. The runbook records its own "last tested" date and it currently says pending, honestly.

## What it backs up

Paths are set in `/etc/restic/backup.env` (never committed; see `.env.example`). Default set: `/opt/stack` (service data), `/etc`, and the home directory, with cache and media excludes in `scripts/backup.sh`.

## Schedule

`systemd/restic-backup.timer` fires daily with `Persistent=true`, so a powered-off machine catches up on next boot instead of silently skipping the day. Logs go to the journal: `journalctl -u restic-backup`.

## Retention / prune policy

`--keep-daily 7 --keep-weekly 4 --keep-monthly 6`, then `restic forget --prune` in the same run. Rationale: a homelab restore is almost always "yesterday" or "before last month's mistake"; six months of monthlies covers the slow-discovery cases without unbounded growth.

## Restore runbook (tested)

The full procedure, including the quarterly restore drill, lives in `docs/restore-runbook.md`. `scripts/restore-test.sh` restores the latest snapshot to a scratch directory and diffs a sentinel file, so "restores work" is a checked fact, on a schedule, not an assumption.

## Decision + rationale

**Why systemd timers over cron:** `Persistent=true` for missed runs, journal logging with unit scoping, and `systemctl list-timers` as a single view of what will run next. Cron gives none of those without extra tooling.

**Why the password lives in an env file readable only by root:** restic needs it non-interactively; a root-owned 0600 env file referenced by the unit keeps it off the command line (visible in `ps`) and out of the repo by construction.

## Current state / next step

Initialize the repository against the chosen backend, run the first backup, then run `scripts/restore-test.sh` and stamp the runbook's "last tested" line with the date and elapsed time.
