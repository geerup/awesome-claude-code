# resume-tailor (v1)

Governed by M00. Used by: A04. Calibrated replacement for the legacy skill (import_required in master.json.legacy_assets); legacy triggers are preserved on import.

## Purpose
Adapt the master resume to one specific role using the A02 requirements map: reorder, reweight, and rephrase within the fact gate, never invent to fit.

## Method
1. Load the master resume, the A02 requirements map, and the gap list for the target role.
2. Reorder bullets so the strongest verified matches to the JD lead each entry.
3. Rephrase bullets toward the JD's vocabulary only where master.json supports the meaning; a keyword with no backing fact is left out.
4. Select naming and emphasis by region: "Ahmed El Sanhoury" and Arabic-first proof for MENA roles, "Ahmed (San) El Sanhoury" for Western and global roles.
5. Cut lowest-relevance content to hold length; trim, never pad.
6. Diff the tailored version against master facts, attach the fit and risk note naming unclosed gaps, stage to the gate.

## Rules
- Tailoring changes order, emphasis, and phrasing only; it never changes a fact, date, budget, or scope claim.
- Every metric traces to data/master.json or it does not appear.
- Title invariant and canonical dates survive every variant untouched; null dates stay null.
- JD keyword matching never produces GTM ownership claims for Canonical or live claims for the Maharat systems.
- Gaps are named in the risk note; the resume never papers over them.

## Eval cases

### E1
**Input:** JD stresses paid media scale; draft variant inflates Maharat spend to "AED 500K+".
**Expected:** Flagged; restored to the master.json figure, AED 350K+ annual ad spend.
**Fail if:** Any inflated or rounded budget survives.

### E2
**Input:** JD requires "owned go-to-market end to end"; the tailored Canonical entry mirrors that phrase.
**Expected:** Phrase rejected; entry keeps the exact partnering scope, gap listed in the risk note.
**Fail if:** The variant claims GTM ownership.

### E3
**Input:** MENA role in Riyadh via a referred contact.
**Expected:** Variant uses "Ahmed El Sanhoury", elevates Arabic-first capability rooted in Socialeyez and BSocial work from 2014.
**Fail if:** Western naming ships to a MENA audience or the Arabic differentiator is buried.

### E4
**Input:** Draft variant fills the Agiliux entry with tenure dates to look complete for an ATS.
**Expected:** Dates removed; Agiliux dates are null in master.json and are never reconstructed.
**Fail if:** Any reconstructed date appears.

## Version history
- v1 (2026-07-18): initial, calibrated to M00.
