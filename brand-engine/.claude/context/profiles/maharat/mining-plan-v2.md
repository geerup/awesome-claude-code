# STATUS 2026-06-04: phases 1 and 2 COMPLETE (see references/drive-extraction-log.md final round). Phase 3 backlog defined: campaign-folder depth, instructor campaign trees, Ad Campaign Reports, Inspo studies, blocked-item manual reads.

# Mining plan v2: the content-mining swarm (regenerated from pilot A)

Supersedes `instructor-mining-plan.md` as the operational plan and updates the
instructor phase of `drive-content-mining-plan.md`. Those files remain as design
history; this file is what runs. Built from what pilot A (Mona Ataya) actually taught.

Scope: phase 1 mines the instructor folders into per-product packs; phase 2 mines the
00- Maharat department archive. Both phases run on the same swarm below.

House rules on everything extracted: no em dashes, no tatweel, Western numerals,
empowering framing, Arabic-first, never imply accreditation. Raw Drive content violates
these; extraction always rewrites, never copies through.

---

## 1. What pilot A taught (the learnings this v2 encodes)

1. Claims verification is the highest-value step. The external check caught a real
   discrepancy (60M claimed vs over 50M sourced) and a disputed stat (90 percent
   first-year failure). Verification is now a mandatory pipeline stage with its own
   agent role, and the claims table is a first-class artifact with a held-back ledger.
2. Machine checks make the gates executable. Prose-only evals depend on an attentive
   reviewer; regex checks catch blocked claims and style violations deterministically.
   Every pack eval now has two layers: machine_checks (run by scripts/eval_runner.py)
   and llm_checks (judged by the reviewing agent). Checks that block claims apply to
   assets only; governance docs that document blocked claims run with --docs.
3. Inventory needs two passes. The connector sometimes fails to enumerate subfolders or
   read certain files (docx-style items). Pass 1: API enumeration. Pass 2: follow
   direct links and record what stays unreadable as blocked, never as absent.
4. Status evidence can be gathered, not just awaited. A public-site check for the
   instructor's class page is cheap and informative. No listing is evidence-neutral;
   a listing is strong launch evidence. Either way the catalog status changes only on
   team confirmation. The check is now a pipeline step.
5. Provenance discipline applies to the miner too. Anything filled from general
   knowledge (catalog domains) gets marked as such, same as any other unverified claim.
6. Dual-language from the start. Every copy library ships AR and EN renders; the brand
   is Arabic-first, not Arabic-only.
7. Source register may diverge from brand register (Levantine one-liners vs MSA rule).
   Interim policy: extract hook patterns, render in brand register, record source
   register as reference. The policy decision (Arman with Ahmed) does not block mining.
8. Promised templates get created in the same run. Pilot A initially flagged the shot
   list as a template candidate without creating it; the pipeline now treats every
   "template candidate" flag as a to-do inside the same run, not a note for later.

## 2. The mining swarm

Mining runs on the same four shapes as campaigns (runtime/SWARM.md), with a dedicated
role split. One pipeline per Drive area (an instructor folder, or a 00- Maharat
subfolder), fanned out in parallel where areas are independent, merged at the registry.

Roles (these are hats the orchestrator or existing agents wear, defined here so a
Claude Code run can dispatch them as subagent tasks):

| Role | Job | Maps to |
|---|---|---|
| inventory-miner | Two-pass enumeration of the area; writes the extraction-log table; marks unreadables as blocked | research-scout |
| extractor | Reads every readable doc fully; pulls facts, claims, patterns, examples | research-scout |
| verifier | External verification of every marketing claim; status-evidence check; outputs the claims table with sources | research-scout |
| distiller | Writes the pack: fact file, voice, SKILL, templates (all of them), evals (machine + llm layers) | copywriter-ar guidance + the pack author |
| gatekeeper | Runs eval_runner on the pack (--docs for governance files), validates JSON, validates house style on every produced file | brand-qa-reviewer |
| registrar | Updates _CATALOG.md, the extraction log, and PATCHES.md if repo wiring is needed | orchestrator |
| human gate | Status confirmation, claims confirmation, register policy; per agents/human-gate.md | Ahmed (campaigns), Arman (brand) |

Pipeline per area (verify-then-advance wraps every step):

```
inventory (2-pass) -> extract -> verify claims + status evidence
   -> distill pack -> gatekeeper (eval_runner + JSON + style)
        fail -> back to distiller with exact fixes
        pass -> registrar updates catalog + log
   -> HUMAN GATE: confirm status, confirm held-back claims
```

Fan-out: up to 3 instructor areas in parallel (verification searches are the bottleneck;
more than 3 concurrent areas degrades source quality). Merge point: the registrar, which
serializes catalog writes.

## 3. The per-instructor pack (the v2 anatomy)

As piloted, plus the v2 additions marked (+):

```
context/instructors/
  _CATALOG.md            registry; provenance-marked; status changes only on confirmation
  <slug>.md              fact file: bio, product, claims table (verified | unverified |
                         disputed, each with source), assets and surfaces, audience notes
                         (+) status-evidence line recording the public-site check result

skills/instructor-marketing/
  SKILL.md               hub: routing, status gate, claims discipline, register policy
  <slug>/
    SKILL.md             segments, angles, promise discipline, stream routing, blockers
    voice.md             register finding, traits, beliefs, hook patterns, brand renders
    templates/
      one-liner-library.md   AR renders by segment (+) EN renders section
                             (+) held-back ledger (blocked claims and their substitutes)
      organic-shot-list.md   (+) or whatever asset templates the folder yields; every
                             flagged template candidate is created in the same run
    evals/evals.json     (+) machine_checks (applies_to scoped) + llm_checks + goldens
```

Definition of done for a pack (the gatekeeper checks all of it):
- [ ] every readable doc in the folder extracted; unreadables logged as blocked
- [ ] claims table complete, every row sourced or marked, held-back ledger present
- [ ] status-evidence check performed and recorded
- [ ] AR and EN renders present; all renders use verified claims only
- [ ] all flagged template candidates created
- [ ] evals.json valid, both layers, golden pass and fail cases
- [ ] eval_runner passes: --docs on governance files, plain on golden pass case,
      and the golden fail case exits 1
- [ ] catalog row updated; extraction log section written; PATCHES.md updated if needed

## 3.5 Unattended batch mode

The whole roster can run in one unattended session via /mine-all-instructors under
runtime/batch-mining-protocol.md: the human gate becomes the asynchronous
references/REVIEW-QUEUE.md, packs stay internal-only and unconfirmed, state lives in
the catalog pack-status column (idempotent resume), and each pack lands as a local git
commit. The deterministic QA gate is scripts/pack_check.py.

## 4. Execution order

1. Pilot B: Ragheb Alama (thin-folder + product-asset path: the Music Cheatsheets).
2. Team review (30 minutes): register policy, claims-confirmation owner, catalog
   statuses, connector access to blocked items.
3. Batch the remaining 9, newest folders first (Elda Choucair, Mo Islam, Cedric Haddad,
   Sami Al Jaber, Toufic Kredieh, Rahma Riad, Bassam Fattouh, Kosai Khauli, Salam
   Dakkak), fan-out 3 at a time.
4. Phase 2: 00- Maharat, starting with 07 Email and WhatsApp Marketing (first-build
   fuel, possible incumbent-platform name), then Guidelines, Campaigns and Research,
   then the rest per drive-content-mining-plan.md sections 3.2 to 3.8.

## 5. Standing open items (the human-gate queue)

1. Register policy (Levantine instructor voice vs brand MSA). Owner: Arman with Ahmed.
2. Claims-confirmation owner; first queue: Mona rows 4, 6, 11, 12 replacement, 20.
3. Catalog public statuses, all 11.
4. Unreadable Drive items (connector scope or format); first: Mona's Research and Strategy.
5. Official AR name spellings against campaign assets.
6. Per-instructor landing pages, handles, footage locations.
