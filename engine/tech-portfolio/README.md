# tech-portfolio/ (Domain T)

Integrated into the engine per San, 2026-07-18: "include the out of scope."

Technical job-search portfolio: 12 public-repo candidates targeting NOC, Linux sysadmin,
DevOps, SOC, and datacenter roles. `CLAUDE.md` (how to work) and `PROJECTS.md` (what to
build) are San's own governing documents, held verbatim; `A24-tech-portfolio-v1.md` in
`agents/` binds them to the engine.

Governance split, deliberate:
- Domain T runs on CLAUDE.md's rules: the no-secrets scan before every commit, repos
  created private and flipped public only on San's explicit word, honest status labels,
  plain technical voice.
- Engine brand voice rules (brand.json bans, register) do NOT apply here. CLAUDE.md
  forbids rewriting the operator's voice into marketing; that clause wins.
- Shared law across all four domains: the human gate, and no invented facts.

State lives in `STATUS.md`. Nothing in this directory creates a remote repository;
scaffolds are staged under `repos/` (gitignored candidates reviewed before any publish).
