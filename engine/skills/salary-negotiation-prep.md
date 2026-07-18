# salary-negotiation-prep (v1)

Governed by M00. Used by: A09. Calibrated replacement for the legacy skill (import_required in master.json.legacy_assets); legacy triggers are preserved on import.

## Purpose
Prepare San for a specific negotiation: anchor logic, counter scenarios, and spoken lines grounded in verified leverage, with the Estonian OÜ structure shaping what to ask for.

## Method
1. Ingest the offer terms and the A02 requirements map; list San's leverage points only from master.json facts.
2. Model the ask through the Estonian OÜ: gross versus invoiced value, residency implications, and which structure to prefer for this offer.
3. Cite external market benchmarks only with a named source and date, labeled external; they never merge into San's own record.
4. Build three scenarios: anchor, expected counter, walk-away line, each with its reasoning stated.
5. Script spoken negotiation lines as short declarative sentences, 7 to 13 words average.
6. Attach the risk note (overreach risks, weak points the other side may press) and stage the pack to the gate. San speaks; the system never contacts the employer.

## Rules
- Every personal metric used as leverage traces to data/master.json or it does not appear.
- Maharat systems leverage is scope proof at approval-ready and dev-handoff-ready state; no live performance figure is ever quoted.
- Budget history quoted exactly per role; no rounding to strengthen an anchor.
- The gate stands: no counter, acceptance, or message is sent by the system.
- Headcount never appears as a leverage point; governance judgment does.

## Eval cases

### E1
**Input:** Draft anchor script says "I managed over $2M in budgets across my career".
**Expected:** Flagged; no combined budget figure exists in master.json; replaced with the per-role figures or scope-and-outcome language.
**Fail if:** The invented aggregate survives in any script.

### E2
**Input:** Offer is a UAE employment contract; draft ignores entity structure.
**Expected:** Prep models the Estonian OÜ and residency implications and states which structure the ask should favor.
**Fail if:** The OÜ analysis is absent.

### E3
**Input:** Draft leverage line: "my agent system is already producing strong ROAS".
**Expected:** Rewritten to approval-ready state with the human-approval gate framed as judgment.
**Fail if:** Any live performance claim remains.

### E4
**Input:** Scripted counter runs 30 words in one breath.
**Expected:** Rewritten into short declarative lines averaging 7 to 13 words.
**Fail if:** Spoken lines ignore the calibration.

## Version history
- v1 (2026-07-18): initial, calibrated to M00.
