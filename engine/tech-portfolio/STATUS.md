# Portfolio Build Status
Owner: TBD (San to choose: personal account vs san-media-tech org)        Updated: 2026-07-18

Phase 0 inventory ran in the San Engine cloud session. Constraint: none of the source
material lives in this environment, and repo creation for the chosen owner is not
possible from this session (GitHub access here is scoped to the engine's fork). BUILD
repos can be scaffolded here; PUBLISH repos need source files from San's machine.

| Repo             | Status      | Source                              | Notes                                          |
|------------------|-------------|-------------------------------------|------------------------------------------------|
| homelab          | not-started | Mele compose files, NOT in session  | PUBLISH; needs files from San's machine         |
| uconsole         | not-started | setup guides + Desktop txt, absent  | PUBLISH; needs files                            |
| tor-rotate       | not-started | rotaton/rotatoff notes, absent      | partial BUILD possible once notes supplied      |
| dotfiles         | not-started | ~/.bashrc, ~/.tmux.conf, absent     | PUBLISH; needs files                            |
| kiwix-guide      | not-started | guide.html, absent                  | PUBLISH; needs file                             |
| ansible-homelab  | in-review   | scaffolded at repos/ansible-homelab | 4 roles, runtime-only auth key; acceptance test = wipe-and-rebuild on San's machine |
| monitoring-stack | in-review   | scaffolded at repos/monitoring-stack| overlay-bound stack; starter dashboard hand-authored and labeled; screenshots after real deploy |
| backup-restic    | in-review   | scaffolded at repos/backup-restic   | timers, prune policy, restore drill script; runbook says last-tested PENDING honestly |
| packet-analysis  | not-started | lab captures needed                 | BUILD; docs scaffoldable, pcaps from San        |
| headscale-stack  | not-started | blocked (not deployed)              | scaffold as planned/evaluated                   |
| node-stack       | not-started | blocked (RAM constraint)            | scaffold as planned; capacity analysis first    |
| profile          | not-started | build last                          | after several repos exist                       |

States: not-started -> scaffolding -> in-review -> published-private -> public

Scaffold pass ran 2026-07-18 on San's word ("scaffold"): the three BUILD repos are staged
under repos/ and sanitization-scanned clean. Next steps: San reviews the three scaffolds;
sets the GitHub owner; supplies source files for homelab and uconsole (the two PUBLISH
repos with the highest signal). Publishing runs from an environment with owner access,
private first, per CLAUDE.md Phase 2.
