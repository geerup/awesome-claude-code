# P01 Application swarm (v1)

Governed by M00. Domain 1. One live application, JD to gate.

## Sequence
1. **A01 Role Scout** → role card (source channel named; off-channel roles flagged, not processed).
2. **A02 JD Analyzer** → requirement map: every requirement bound to a master.json field or a named gap.
3. **A03 Fit Assessor** → verdict. KILL ends the run and logs the reason. PROCEED names the gaps carried forward.
4. Parallel:
   - **A04 CV Variant Builder** → variant config + built CV (validator must pass before an output file exists).
   - **A05 Cover Letter Writer** → one case study letter, case chosen from A02's mapping.
   - **A10 Reference Builder** → per-application reference list.
5. **A07 Outreach Writer** → recruiter or referral message plus follow-up cadence.
6. Review tier: machine pass (`evals/machine_check.py`) → R01 → R02 → R03. Flags return to the writing agent; second review confirms fixes.
7. **A00** assembles the pack in `outputs/gated/application-<n>/` with the gate header. Stops.
8. San's yes → send is manual, by San. **A08 Pipeline Tracker** records state either way.

## Hard rules
- No auto-send path. Step 8 has no automation.
- A03 KILL is overridable only by San; override logged.
- A06 Interview Prep and A09 Offer Analyzer join on state transitions (interview scheduled, offer received), same review tier.
