# SOP 01: Brief intake

Stream 1. Owner: strategy-lead. Mode: reasoning. Turns a raw brief into a validated, scoped
starting point before any strategy work begins. It validates the brief against the template,
flags every ASSUMPTION and OPEN ITEM, confirms the entry point, and stops and asks on any
missing variable. It produces nothing customer-facing. It never invents a value to fill a gap.

No em dashes, no tatweel, Western numerals, English-first for any customer-facing text drafted.

---

## Trigger

A new or updated brief lands in `briefs/`, or a run starts and the active brief has not yet
been validated. The orchestrator dispatches stream 1 before any other stream runs.

## Inputs

- The active `briefs/` file, the only per-campaign input.
- `briefs/_TEMPLATE-campaign-brief.md` as the structure to validate against.
- `context/` for facts that are not campaign variables, so intake can tell a true gap from a
  fact that already lives in context.

## Steps

1. Validate structure. Walk the brief section by section against the template: identity,
   entry point and objective, audience, offer, channels and gate, budget and schedule,
   creative direction, constraints, approvals. Note any missing or malformed section.
2. Flag every ASSUMPTION. List each field marked ASSUMPTION (price, promotion, budget,
   target). An ASSUMPTION is a placeholder the engine must not act on. Record which downstream
   stream needs each one, so the cost of leaving it open is visible.
3. Flag every OPEN ITEM. List each unresolved item (for example gate_platform not confirmed,
   mobile event mapping, audience size pending live data). State which stream it blocks.
4. Confirm the entry point. Read `entry_point` and confirm it is paid acquisition or owned
   audience. If it is missing or ambiguous, stop and ask. The entry point decides which
   streams run, so it cannot be guessed.
5. Check the offer against guardrails. The offer must come from the brief, never invented. No
   offer title, subject name, price, or promotion is assumed here. Confirm no
   accreditation claim is implied anywhere in the brief.
6. Decide stop-or-proceed. If a variable a needed stream depends on is missing, stop and ask
   Ahmed. Do not fill the gap. If the gaps are only in streams this campaign does not run, the
   brief can proceed with those gaps recorded.
7. Write the validated brief and scope note. Record the entry point, which streams run, every
   ASSUMPTION, every OPEN ITEM, and the explicit stop-and-ask questions, if any.

## Output

A validated brief plus a scope note (internal; skill eval only, per `verification.md`). It
carries the common envelope from `runtime/handoff-contract.md` with `stream: 1 brief intake`
and an `open_items` list that downstream streams read before they start. The scope note
states the entry point, the streams in scope, and the list of unresolved ASSUMPTIONS and OPEN
ITEMS by owning stream. This is the input that strategy-lead consumes in stream 2.

## Quality bar

- Every brief section is checked against the template. Nothing is skipped.
- Every ASSUMPTION and every OPEN ITEM is listed, with the stream it affects.
- The entry point is confirmed, not inferred. If missing, the run stops here.
- No value is invented to close a gap. A missing needed variable is a stop-and-ask.
- Gate: skill eval for structure and completeness. No arabic-copy-qa or brand-qa, since the
  output is internal and carries no customer-facing copy (see `verification.md`).

## Example output (shape, not real copy, no invented values)

```
validated_brief:
  campaign_id: [from brief filename]
  entry_point: owned audience
  streams_in_scope: [1, 2, 4, 7, 6, 8, 9]
  streams_skipped: [3 unless visuals needed, 5 paid build]
scope_note:
  assumptions:
    - field: price        needed_by: stream 7   status: ASSUMPTION, stop before send
    - field: promotion    needed_by: stream 7   status: ASSUMPTION, stop before send
  open_items:
    - item: gate_platform not confirmed   blocks: stream 7 send wiring, stream 6 gate
    - item: audience_size pending live data   blocks: stream 7 send count
  stop_and_ask:
    - "Confirm price and promotion before any send-related stream proceeds."
```

## Review owner

strategy-lead owns the validated brief. Any stop-and-ask goes to Ahmed before the run
advances. The intake never approves its own gaps and never proceeds on a needed variable that
is still an ASSUMPTION.

No em dashes, no invented values. A missing variable is a stop-and-ask, not a guess.
