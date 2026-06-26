# Build vs Buy Scorecard

Research readout. Owned by research-scout, run via /research. A proposal, never an adoption.
Adoption is Ahmed's call and lands as a settings.json allowlist change made by a human.

## Capability and constraints

- capability needed:
- stream(s) served:
- constraints: (English-first, GCC data / PDPL, budget, expected volume)
- what the brief and context already say:

## Existing-tool check (borrow before building)

- Is there an existing framework, platform, or tool that already does this? (yes / no)
- If yes, what, and does it fit? If no, what is the gap that would justify building?

## Arabic gate (decisive for generative tools)

For any generative tool, this is applied first. A candidate that fails it is ruled out
regardless of its other strengths.

- Produces clean Arabic (no tatweel, Western numerals, RTL-safe)? (pass / fail / n/a)
- Real Arabic output sample tested? (yes / no, with a note on the result)

## Criteria weights and must-have flags (set before scoring)

Before scoring, set a weight and a must-have versus nice-to-have flag per criterion, so a
deal-breaker is not averaged away by extras. This is MoSCoW-style gating layered on the
weighted score, it does not replace the Arabic gate.

- Weight: a relative importance per criterion (for example 1 to 5, or a percentage that sums
  to 100). Tie the weight to what this stream and the brief actually need.
- Must-have vs nice-to-have: mark each criterion must-have (a candidate that fails it is ruled
  out, regardless of total score) or nice-to-have (it contributes to the weighted score but
  does not by itself disqualify).
- Arabic capability stays the existing hard gate. For any generative tool it is applied first
  and a fail rules the candidate out regardless of weight, flag, or total score. It is the
  decisive filter, not just a high-weighted must-have.

| Criterion | Weight | Must-have / nice-to-have |
|---|---|---|
| Arabic (decisive, generative tools) | (hard gate, above weighting) | must-have (hard gate) |
| SOP fit |  |  |
| GCC/PDPL data fit |  |  |
| Cost vs volume |  |  |
| Integration effort |  |  |
| Lock-in / exit |  |  |
| Maturity / support |  |  |

## Scored shortlist

Score each candidate 1 to 5 per criterion. Multiply each score by the criterion weight above
for a weighted total. A candidate that fails any must-have criterion is ruled out regardless
of its weighted total. For generative tools, a failed Arabic gate is a hard no, applied before
weighting and never offset by other columns.

| Candidate | Arabic (decisive) | SOP fit | GCC/PDPL data fit | Cost vs volume | Integration effort | Lock-in / exit | Maturity / support | Weighted total | Must-have failed? | Notes |
|---|---|---|---|---|---|---|---|---|---|---|
|  |  |  |  |  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |  |  |  |  |

## Recommendation (one path)

- recommendation: (buy a named candidate / build / hold pending an open item)
- rationale:
- this is a proposal: adoption requires Ahmed's approval and a settings.json allowlist change.

## Open items that block a final decision

- (e.g. current platform not confirmed, PDPL residency requirement unknown, volume unknown,
  access and approval process unclear)
