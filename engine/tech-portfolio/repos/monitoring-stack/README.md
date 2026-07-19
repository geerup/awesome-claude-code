# monitoring-stack

Prometheus + Grafana + node_exporter + smartctl_exporter as a compose stack for a single-node homelab. Surfaces host metrics (CPU, memory, disk, network) and SMART disk health, which is the failure mode that actually kills home servers.

**Status: in progress** — the stack definition and scrape config are written; deployment to the homelab host, dashboard export, and screenshots are the remaining steps. No screenshots appear here until they are real.

## Stack

| Service            | Purpose                                        | Port (overlay-bound) |
|--------------------|------------------------------------------------|----------------------|
| Prometheus         | Metrics store and scrape engine, 30d retention | 9090                 |
| Grafana            | Dashboards                                     | 3000                 |
| node_exporter      | Host metrics                                   | 9100                 |
| smartctl_exporter  | SMART attributes per disk                      | 9633                 |

## Deploy

```bash
cp .env.example .env       # set the Grafana admin password
docker compose -f compose/monitoring.yml up -d
```

Bind services to the overlay interface only (see `compose/monitoring.yml` comments); nothing here is meant to be reachable from the LAN or WAN.

## Decision + rationale

**Why smartctl_exporter and not just node_exporter:** node_exporter tells you a disk is full; SMART tells you it is dying. Reallocated-sector and pending-sector counts trend upward before failure, and a dashboard line you glance at weekly is the cheapest early-warning system a homelab can have.

**Why 30-day retention:** long enough to see weekly patterns and a slow SMART trend, short enough that Prometheus storage stays trivial on a small NVMe. Longer-horizon capacity questions belong in a separate exported snapshot, not in the hot store.

## What each exporter surfaces

- `node_exporter`: load, memory pressure, filesystem fill rates, network errors.
- `smartctl_exporter`: temperature, reallocated/pending sectors, power-on hours, per-device health flag.

## Current state / next step

Deploy on the homelab host, import the starter dashboard (`grafana/dashboards/node-overview.json`, hand-authored, labeled as such), let it run a week, then export the tuned dashboard JSON back into this repo and add scrubbed screenshots to `docs/screenshots/`.
