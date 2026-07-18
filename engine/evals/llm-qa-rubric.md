# LLM QA rubric (tier two of verification)

Runs after `machine_check.py` passes, before the gate. Three reviewers score independently. Reviewers surface defects only, never auto-fix. Writers fix; a second review confirms. Unresolved flags go to San with the reviewer's note intact.

## R01 Fact Validator (judgment pass)
Machine pass catches tokens; this pass catches claims.
- Does any sentence imply a result the evidence in master.json does not support?
- Is any Maharat system framed as live, running, or producing performance figures? Auto-flag.
- Is scope language precise (Canonical: did not own GTM; pipeline: influenced)?
- Is any figure attributed to the wrong role (10M+ is career combined only)?
- Verdict: PASS / FLAG with claim, risk, and the master.json field it fails against.

## R02 Voice Reviewer
- Register: executive, specific, numbers as proof and never the headline.
- Rhythm: terse, one formulation per idea; spoken scripts average 7 to 13 words per sentence.
- Structure: no padded openers, no hype hooks, no headcount leads.
- Verdict: PASS / FLAG with line reference and the brand.json rule violated.

## R03 Brand Reviewer
- Does the piece serve "Builds the systems that run marketing, not just the campaigns."?
- Is it aimed at exactly one named audience (recruiters, CMOs, founders, MENA operators)?
- Does it hold one of the two lanes (governed agentic systems; Arabic-first MENA growth)?
- Seniority signal: reads as Senior Director level, no junior tells.
- Verdict: PASS / FLAG with the positioning drift named.

## Gate record
Every output entering `outputs/gated/` carries a header block:

```
status: PENDING SAN APPROVAL
machine_pass: <date, clean|flags-resolved>
qa_pass: R01 <verdict> | R02 <verdict> | R03 <verdict>
risk_note: <honest fit or risk note, mandatory>
```

No output leaves `outputs/gated/` without San's explicit yes recorded in `log/decisions.md`.
