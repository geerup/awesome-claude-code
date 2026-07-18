# ansible-homelab

Ansible playbooks that rebuild my homelab from a fresh OS install: base hardening, Docker, the WireGuard overlay client, and the self-hosted service stack. The point is that nothing on the box is hand-configured — a wiped machine returns to service with one command.

**Status: in progress** — roles are written and lint-clean; the full run has not yet been executed against a freshly wiped machine. That end-to-end rebuild test is the acceptance gate before this is marked running.

## What it provisions

| Role       | Does                                                                        |
|------------|-----------------------------------------------------------------------------|
| `base`     | Packages, non-root admin user, SSH hardening (key-only, no root), UFW, tmux |
| `docker`   | Docker Engine + compose plugin from Docker's apt repo, daemon log limits    |
| `overlay`  | Tailscale client install and bring-up (auth key passed at runtime, never stored) |
| `services` | Deploys the compose service stack under `/opt/stack` and starts it          |

## Run

```bash
cp inventory.example.ini inventory.ini            # fill in your host
cp group_vars/all.example.yml group_vars/all.yml  # fill in your values
ansible-playbook -i inventory.ini site.yml
# overlay auth key is prompted or passed per-run, never committed:
ansible-playbook -i inventory.ini site.yml -e tailscale_authkey=REPLACE_WITH_TAILSCALE_AUTHKEY
```

Real `inventory.ini` and `group_vars/all.yml` are gitignored; only `.example` files ship.

## Decision + rationale

**Why roles instead of one big playbook:** the overlay and services roles change at a different cadence than base hardening. Splitting them means a service-stack update run (`--tags services`) cannot touch SSH config, which is the class of mistake that locks you out of a remote box.

**Why the auth key is a runtime variable:** a preauth key in group_vars ends up in git history eventually, gitignore or not. Passing it per-run (`-e`) keeps the repo clean by construction, which matters more than convenience on a machine you rebuild rarely.

## Idempotency notes

Every task uses state-declaring modules (`apt`, `user`, `ufw`, `systemd`, `copy` with checksums) rather than shell commands, so a second run reports zero changes. The compose deploy uses `docker compose up -d`, which is a no-op when the stack matches.

## Current state / next step

Next step is the acceptance test: wipe the spare SSD, install stock Debian, run the playbook, and record the elapsed time and any manual steps that remain. Anything manual becomes a new task or a documented exception.
