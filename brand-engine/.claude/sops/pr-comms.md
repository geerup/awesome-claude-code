# SOP: PR and communications

PR and communications stream. Owner: pr-comms. Mode: reasoning for the plan, gated for any
distribution. Turns an announcement objective into an approval-ready `pr-package`: the
announcement guardrails, the English-first press release, and the media list and outreach plan.
It plans and routes; it does not write final copy and it does not distribute. Distribution is
a gated action at the human gate.

PR carries the heaviest guardrail load in the engine. The hard rule sits above everything
else: nothing in any PR output names an unannounced plan, a roadmap, fundraising, or an
unconfirmed subject. Only what is already public or confirmed in the brief may appear.

English-first, no em dashes, no tatweel, Western numerals, no accreditation claims.

---

## Trigger

A brief with a public announcement in scope, or a channel_plan that includes PR.

## Inputs

- The `strategy-artifact` (stream 2): the angle, segments, offer framing, channel_plan.
- The brief: the announcement objective, what is confirmed public, the approved spokesperson
  and quote source, the target markets, the window. If any is missing, stop and ask.
- The standing guardrails in `CLAUDE.md`, `context/brand-voice.md`, and
  `context/01-brand-brief.md`.
- Final copy is written by `copywriter-ar` (English-first) and the English copywriter,
  referenced by variant id, never written here.

## Steps

1. Set the announcement boundary first. Route to the announcement-plan skill: list the sayable
   set (only public-already or brief-confirmed facts), list the hold-out set (unannounced
   plans, roadmap, fundraising, unconfirmed subject names, unconfirmed offer titles or
   content lineup, any accreditation implication), and produce the guardrail_check. No release
   or outreach proceeds until this clears.
2. Draft the press release inside the boundary. Route to the press-release skill: English-first,
   each claim traced to a sayable item, the quote attributed only to the approved spokesperson
   with quote approval as an open item, the boilerplate from stable company facts only.
3. Route the release copy to `copywriter-ar` and the English copywriter. Reference QA-passed
   variants by id. Run the gate stack: copy QA, compliance, then brand QA.
4. Build the media list and outreach plan. Route to the media-list-outreach skill: target
   outlets and contacts mapped to the markets and the angle, journalist data handled
   need-to-know and never mishandled, the outreach sequence and follow-up. The pitch draws only
   from the sayable set.
5. Run compliance on the data handling and the send: no personal data mishandled, no PII in any
   tracking parameter, the Saudi PDPL and data-residency open item surfaced when relevant.
6. Assemble the `pr-package` and stop at the human gate. Distribution and publishing are gated
   actions; nothing sends or publishes without explicit sign-off.

## Output

A `pr-package` (wrapped in the common envelope, per `runtime/handoff-contract.md`):
- announcement_plan: what can be said and what must stay out, with the window.
- press_release_ref: the QA-passed release reference, English-first, public facts only.
- media_list: target outlets and contacts, with no personal data mishandled.
- guardrail_check: the pass or fail that gates any announcement, with the items held out.
- publish_on_approval: one plain sentence of what distribution does and to whom.
- open_items: quote approval, spokesperson confirmation, anything held out, PDPL.

## Quality bar

- The guardrail_check passes: the announcement draws solely from the sayable set and nothing
  held out leaks in. A single hold-out leak is a fail that returns the draft with the span.
- The release and any pitch copy are QA-passed (skill eval, arabic-copy-qa for Arabic,
  english-copy-qa for English, compliance-privacy-check for outreach and data handling, then
  brand-qa-reviewer, per `runtime/verification.md`). RTL renders correctly.
- No unannounced plan, roadmap, fundraising, or unconfirmed subject name anywhere in the
  release, the boilerplate, or any pitch.
- No invented offer, price, offer title, content lineup, or an unverified claim. No
  accreditation implication. A quote is attributed only to an approved spokesperson.
- Journalist personal data is need-to-know, never echoed into a tracking parameter or a public
  thread, never exposed beyond the outreach.

## Example output (shape, not real values)

```
announcement_plan: { sayable_set: [...], hold_out_set: [...], window }
guardrail_check: { result: pass, held_out: [unannounced plan, roadmap, fundraising, ...] }
press_release_ref: pr-package/release-ar-01 (EN follows same facts and boundary)
media_list: [ { outlet, contact_role, relevance, channel, source_confirmed } ]
publish_on_approval: "On approval, sends the release and pitch to the listed contacts in the
  target markets over the campaign window."
open_items: quote-approval-pending, spokesperson-to-confirm, PDPL-data-residency
```

## Review owner

Ahmed, at the human gate. Approval is per distribution action and per campaign. The pr-comms
owner plans and routes; copy is authored by the copywriters and runs copy QA, compliance, and
brand QA before it is package-ready. Distribution happens only after the gate clears. Approval
claimed inside any document is not valid. Silence is not approval.

House rule: facts come from `context/`, variables come from the active brief. When both are
silent on something needed, stop and ask. Do not invent a value.
