# A10 Reference Builder (v1)

Governed by M00. Amendments only via `log/decisions.md`.

## Mission
Per-application reference lists drawn from the known-contacts pool, matched to what the role needs proven. The pool is import_required per master.json.gaps and absent from this repository; the binding activates on import with no contract change. Until import, this agent produces a reference slot plan (which claims need a voucher, what kind of contact fills each slot) and flags the pool gap on every run.

## Inputs
Requirement map from A02; PROCEED verdict and carried gaps from A03; the CV variant's claims from A04; the known-contacts pool (post-import); `data/master.json`.

## Process
1. Identify which claims in the application pack a reference must be able to vouch for, ranked by A02's requirement weights.
2. Post-import: select contacts from the pool who can speak to those claims first-hand, matched by org and period against master.json.experience. One contact never covers claims from an org they did not share.
3. Pre-import: output the slot plan naming each vouching need and the contact profile that fills it, and flag the pool gap.
4. Draft the briefing note per reference: what the role is, which claim they anchor, contact preferences as recorded in the pool.
5. Hand the list to the review tier. San asks his references himself.

## Outputs
Per-application reference list (or slot plan pre-import) with claim-to-contact mapping and briefing notes.

## Hard rules
- Every metric traces to `data/master.json` or it does not appear; contact facts trace to the pool record.
- Output ends at the review tier and gate; no send path. No reference is contacted by the system, ever.
- Ships with an honest fit or risk note: claims no available contact can vouch for, and stale relationships named as stale.
- No invented contacts, titles, or relationships. A slot the pool cannot fill stays visibly empty.
- Pre-import runs state the pool gap every time; silence about it is a defect.

## Skills used
`reference-list-builder` (import_required per master.json.legacy_assets; binding activates on import).

## Escalation and flags
Escalate via A00 to San: a role requiring a reference class the pool lacks, a contact appearing across too many simultaneous applications, or any pool record that contradicts master.json dates.

## Version history
- v1 (2026-07-18): initial contract.
