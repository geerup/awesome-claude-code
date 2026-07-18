# San Engine

Governed multi-agent system for Ahmed (San) El Sanhoury. Three domains: career growth, personal brand, content production. `M00.md` is the master contract; every file in this tree inherits from it.

## Layout
```
M00.md              master contract, governs everything below
data/master.json    canonical facts, single source of truth (status: PENDING_SAN_APPROVAL)
data/brand.json     voice rules, banned list, positioning, pillars, audiences
agents/             27 versioned contracts: A00 coordinator, A01-A10 career, A11-A16 brand, A17-A23 content, R01-R03 review tier
skills/             knowledge files, each with 3+ eval cases; failing skills are blocked
pipelines/          P01 application, P02 brand refresh, P03 content week
evals/              machine_check.py (tier one) and llm-qa-rubric.md (tier two)
outputs/gated/      packs waiting at the human-approval gate
log/decisions.md    binding amendments, overrides, stated assumptions
```

## Governance in one paragraph
Every output passes the machine pass (`python3 evals/machine_check.py <file>`), then LLM QA review by R01, R02, R03 (reviewers surface defects only; writers fix; a second review confirms), then stops at the gate. Nothing publishes, sends, submits, or spends without San's explicit yes, logged in `log/decisions.md`. No auto-send path exists in this codebase.

## Current state (2026-07-18)
- Phase 0 approved by San ("approve the plan and start working"); master.json at v1.1.0, APPROVED_TO_BUILD, with the CV and the 50-stat dashboard imported. Remaining conflicts in `master.json.meta.conflicts`.
- Phases 1 to 3 built as working increments; proof-run packs sit in `outputs/gated/` on v1.1.0 facts (application-001 uses a marked sample JD, see decisions log).
- Still import_required: the Node CV build chain, 8 legacy skill configs, portfolio HTML surfaces, linkedin-copy.md, the seven case study files.

## First actions for San
1. Rule on `master.json.meta.conflicts` (Goodwall 1M vs 2M is the material one) and confirm the Arabic name rendering.
2. Rule on the three gated packs and the title-step-down and relocation questions in `outputs/gated/application-001/fit-verdict.md`.
3. Import the remaining source-project assets named in `master.json.legacy_assets`.
