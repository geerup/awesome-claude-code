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
| ansible-homelab  | not-started | none needed                         | BUILD; scaffoldable in-session on San's word    |
| monitoring-stack | not-started | screenshots needed later            | BUILD; compose/config scaffoldable in-session   |
| backup-restic    | not-started | none needed                         | BUILD; scaffoldable in-session                  |
| packet-analysis  | not-started | lab captures needed                 | BUILD; docs scaffoldable, pcaps from San        |
| headscale-stack  | not-started | blocked (not deployed)              | scaffold as planned/evaluated                   |
| node-stack       | not-started | blocked (RAM constraint)            | scaffold as planned; capacity analysis first    |
| profile          | not-started | build last                          | after several repos exist                       |

States: not-started -> scaffolding -> in-review -> published-private -> public

Next step (per CLAUDE.md Phase 0): San picks the first repo and sets the owner. Priority
order says homelab or uconsole; both need source files supplied to whichever session
does the scaffold. If San wants in-session progress now, the BUILD repos
(ansible-homelab, monitoring-stack, backup-restic) are startable without any uploads.
