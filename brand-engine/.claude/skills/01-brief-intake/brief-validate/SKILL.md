---
name: brief-validate
description: Validates the active campaign brief against briefs/_TEMPLATE-campaign-brief.md field by field, flags every ASSUMPTION and OPEN ITEM, and stops-and-asks on any missing variable the campaign needs. Use as the first step of stream 1, before any scoping or strategy. Triggers on "validate the brief," "is the brief complete," "check the brief," "what is missing from the brief," "are there assumptions in the brief."
---

# Brief Validate (stream 1 sub-skill)

Reads the active brief against the template and produces a validation report that tells
strategy-lead exactly what is solid, what is an ASSUMPTION, what is an OPEN ITEM, and what
is missing entirely. The point is that no downstream stream is ever surprised by a gap.

Owner: strategy-lead. Mode: reasoning. Gate: skill eval only (internal artifact).

## When to use

First thing on any new or changed brief, before `kickoff-scope` and before stream 2. If the
brief is edited mid-run, validate again.

## Inputs

- The active `briefs/` file.
- `briefs/_TEMPLATE-campaign-brief.md` (the field list to validate against).
- `context/01-brand-brief.md` for stable facts (so a number in `context` is not flagged as
  missing from the brief).

## Steps

1. Walk the template section by section: Identity, Background and context, Entry point and
   objective, Audience, Offer, Channels and gate, Budget and schedule, Creative direction,
   Mandatories and constraints, Approvals.
2. For each field, classify it: PRESENT (a real confirmed value), ASSUMPTION (the brief
   marked it ASSUMPTION, a placeholder the engine must not act on), OPEN ITEM (unresolved,
   downstream must account for it), or MISSING (the template expects it and the brief is
   silent).
3. List every ASSUMPTION and every OPEN ITEM explicitly. Do not smooth them over. These ride
   forward so the human gate can surface them.
4. For any field classified MISSING that the campaign actually needs to proceed, stop and
   ask. Do not invent a value. State plainly which field, why it is needed, and what is
   blocked until it is supplied.
5. Note which fields are PRESENT but only as planning estimates (for example audience size),
   so downstream knows the exact value resolves from live data later.
6. Run the SMART check on `success_metric`. Test it against five criteria: Specific (one named
   outcome, not a vague aim), Measurable (a target NUMBER is present), Time-bound (a date by
   which it is measured is present), Attainable (plausible for the audience and budget), and
   Relevant (it captures real customer value, not a vanity count). A metric missing a number,
   missing a date, or phrased vaguely ("more signups", "grow awareness") FAILS the check. On a
   fail, raise it as an OPEN ITEM (stop-and-ask) naming exactly what is weak: do not invent a
   target number, a date, or a tighter wording. If the brief already marks the metric
   ASSUMPTION, report it as ASSUMPTION (the gap is acknowledged), not as a silent pass.
7. Check that the Background and context section (why_now, business_problem, prior_results) and
   the key_message field are each either PRESENT or explicitly flagged (ASSUMPTION or OPEN ITEM).
   These give strategy-lead the rationale to anchor the stream 2 angle. A silent gap on any of
   them is reported as MISSING; do not invent a rationale, a prior result, or a message.
8. Record the result in the validation report template, including the SMART check verdict on
   the success metric.

## Output

A completed `templates/brief-validation-report.md`: per-field status, the full ASSUMPTION
list, the full OPEN ITEM list, the stop-and-ask list, and a single readiness line (ready to
scope, ready to scope with flagged assumptions, or blocked).

## How this connects to the contract and gates

- Handoff: the report grounds the `strategy-artifact` strategy-lead builds in stream 2. The
  ASSUMPTION and OPEN ITEM lists map to the `open_items` and `brief_refs` fields of the
  common envelope in `runtime/handoff-contract.md`.
- Verification: internal artifact, so it runs this skill eval only, per
  `runtime/verification.md`. No brand or Arabic gate unless customer copy is drafted.

## Hard rules

- A missing variable the campaign needs is a stop-and-ask, never an invention. This is the
  core job of this skill, not a side note.
- The `success_metric` must pass the SMART check (a target number and a date, specific,
  attainable, relevant). A weak or unmeasurable metric is surfaced as an open item to Ahmed,
  never carried silently and never repaired by inventing a number, a date, or a wording.
- An ASSUMPTION is reported as an ASSUMPTION, never quietly promoted to a real value.
- No em dashes, no tatweel, Western numerals only. Empowering framing, no accreditation claims.
