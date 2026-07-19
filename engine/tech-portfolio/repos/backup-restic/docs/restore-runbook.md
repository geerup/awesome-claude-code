# Restore runbook

**Last tested: PENDING** (stamp date, elapsed time, and snapshot id after each drill; a runbook without a test date is a draft)

## Scenario A: single file or directory

```bash
source /etc/restic/backup.env
restic snapshots                       # pick the snapshot id
restic restore <id> --target /var/tmp/restore --include /path/you/need
```

Copy the restored path into place, verify ownership and permissions, done.

## Scenario B: full service-stack recovery on a rebuilt host

1. Reprovision the host (see the ansible-homelab repo) so Docker and the overlay are up.
2. Recreate `/etc/restic/backup.env` from the password manager (repo URL, password file, paths).
3. `restic restore latest --target /` for `/opt/stack`, or restore to scratch and rsync if you want to inspect first (safer, default choice).
4. `cd /opt/stack && docker compose up -d`.
5. Verify each service against its own data (log in, check recent records), then re-enable the backup timer: `systemctl enable --now restic-backup.timer`.

## Scenario C: repository sanity when something smells wrong

```bash
restic check --read-data-subset=10%
restic snapshots --compact             # confirm the cadence has no gaps
```

Gaps in the snapshot list mean the timer failed silently somewhere: `journalctl -u restic-backup` before anything else.

## Drill schedule

Quarterly: run `scripts/restore-test.sh`, stamp the header line above, and note anything that surprised you. Surprises become runbook edits.
