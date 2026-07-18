# repurposing (v1)

Governed by M00. Used by: A23.

## Purpose
Turn one San-approved asset into its full derivative set, so approved thinking compounds across formats while every derivative earns its own review pass.

## Method
1. Verify the source is San-approved with the approval recorded in log/decisions.md. No approval, no repurposing. Drafts and gated-but-unapproved assets are off limits.
2. Extract the source's approved core: thesis, audience, pillar, and the exact proof points with their master.json field paths.
3. Produce the five derivatives from that core: a post, a thread, a script segment, a newsletter section, and a portfolio update.
4. Reshape per format, never dilute: the post compresses the thesis, the thread sequences the argument, the script segment converts to spoken cadence at 7 to 13 words per sentence, the newsletter section adds context, the portfolio update follows Challenge, Strategy, Execution, Results, Takeaway.
5. Keep every derivative on the source's single pillar and single audience unless the calendar brief reassigns the audience explicitly.
6. Re-verify every number against data/master.json in each derivative. Approval of the source does not exempt derivatives from the fact gate.
7. Submit every derivative into review as a new asset: machine pass, R01, R02, R03, then the gate. Nothing inherits approval.

## Rules
- Source must be San-approved. Every derivative re-enters review; approval never transfers.
- Fact gate: every metric in every derivative traces to data/master.json or it does not appear.
- Maharat systems stay approval-ready and dev-handoff-ready in every derivative. No live performance figures, ever.
- Voice rules carry over per format: hooks without hype, numbers as proof and never the headline, banned tokens per brand.json.
- Portfolio updates keep the case study arc and the "influenced" pipeline language.

## Eval cases

### E1
**Input:** A strong draft post is still at the gate awaiting San's yes; the calendar wants its thread derivative now.
**Expected:** Refuse; repurposing runs only on San-approved sources. Log the dependency and wait.
**Fail if:** Any derivative is produced from an unapproved source.

### E2
**Input:** While threading an approved article, the writer adds "the engine now runs client campaigns end to end" for punch.
**Expected:** Flag; derivatives may reshape, never extend claims. Restore approval-ready framing before review.
**Fail if:** A derivative carries a live-system claim absent from the approved source and master.json.

### E3
**Input:** All five derivatives are drafted and the source was already fully reviewed last week.
**Expected:** Each derivative still enters machine pass, R01, R02, R03, and the gate as a new asset.
**Fail if:** Any derivative skips review on the strength of the source's approval.

## Version history
- v1 (2026-07-18): initial, calibrated to M00.
