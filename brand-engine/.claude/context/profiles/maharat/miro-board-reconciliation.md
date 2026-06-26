# Miro board reconciliation: board-only specifics and one correction

This folds the workshop Miro board (https://miro.com/app/board/uXjVHLAFvMs=/) into the
source-of-truth layer, the same way `brainstorm-reconciliation.md` folds the five brainstorm
docs. No edits to agent or runtime files. Agents read `context/` first, so this is
authoritative at run time, and each item names the file it refines for an easy later patch.

The board is the most recent workshop artifact. Where it conflicts with an earlier
assumption (including one in `brainstorm-reconciliation.md`), the board wins. The bulk of
the board confirms what we already built: the funnel diagram, the orchestrator-plus-
specialists prompting strategy, the reasoning-vs-execution split, the QA-as-gate rule, and
borrow-before-inventing all match the agent and runtime layer as written. Only the deltas
below need capturing.

House rule unchanged: no em dashes, no tatweel, Western numerals, empowering framing,
Arabic-first Gulf-familiar MSA, Thmanyah tone, never imply accreditation.

---

## 1. CORRECTION: single-class buyers are a sub-segment of the non-payer flow, not a separate entry

This overrides item 5 in `brainstorm-reconciliation.md`.

The board's non-payer email SOP defines the trigger as a contact in the non-paying segment
(about 18,000) that is "never-activated, lapsed free-level, or single-class buyer." So
single-class buyers are one of three sub-groups inside the one non-payer flow, not a
separate sibling owned-audience entry as I earlier proposed.

What survives from my earlier note: the single-class sub-group still gets its own entry
message and proof point (the SOP requires at least 3 segments, each with its own entry
message and proof point), and its angle is still upsell into a subscription rather than
first conversion. It is a distinct treatment within the flow, not a distinct flow.

Suppression still matters: stop on conversion, honor unsubscribes, and the flow targets
non-payers, so the roughly 1,000 active subscribers are excluded.

Refines: `runtime/stream-ownership.md` (entry point B), `runtime/handoff-contract.md`
(`lifecycle-package` audience and suppression). Supersedes `brainstorm-reconciliation.md` item 5.

## 2. The stream-7 non-payer flow has concrete shape, not just abstract structure

The board pins down the numbers my agent files left general. Treat these as the
first-hypothesis defaults for the non-payer flow, refined against data, not invented per run:

- At least 3 segments, each with its own entry message and proof point.
- A 4 to 5 email arc per segment, with named beats: reconnect, proof, the daily-habit hook,
  the offer, optional last call (only with a real deadline).
- 2 subject variants and 1 preview per email.
- Cadence 3 to 4 days apart.
- Suppression: stop on conversion, honor unsubscribes.
- One CTA per email, matching the offer (the offer is a brief input, never invented).

The QA order is explicit: arabic-copy-qa, then brand-qa-reviewer, then package for Ahmed.
Nothing sends without sign-off.

Refines: `runtime/handoff-contract.md` (`lifecycle-package` flow body), and the eventual
stream-7 skill evals.

## 3. Conversion-path event taxonomy is now concrete

The board's conversion-path SOP names the actual event map, which should replace the generic
event names in the handoff contract:

`ad_click -> landing_view -> lead_signup -> free_start -> checkout_start`

Each event fires to four destinations: Meta Pixel and CAPI, GA4, ManyChat, and BigQuery
(the warehouse). The quality bar is that each event fires once and lands, verified not
assumed (no loss, no double-firing). Consent is captured at the gate. No personal data in URLs.

This confirms reconciliation item 2 (signup events feed lifecycle AND analytics) and makes
it specific: the warehouse (BigQuery) is the fourth destination alongside Pixel/CAPI, GA4,
and ManyChat.

Refines: `agents/conversion-engineer.md` (event list), `runtime/handoff-contract.md`
(`conversion-package` event_plan).

## 4. The ManyChat to engine handoff mechanism is now specified

Still an open item on ownership, but the board specifies the intended mechanism:

- ManyChat fires a webhook on signup to the engagement engine's ingest endpoint.
- Mirror the same events to BigQuery for reporting parity.
- Use middleware (Make, Zapier, or Pabbly) only if there is no native webhook.
- ManyChat stays the Instagram capture layer and hands off on signup. It does not send email.

Still unresolved: who owns the integration on the dev side. Carry in open items.

Refines: `agents/conversion-engineer.md`, `runtime/handoff-contract.md` (`conversion-package` gate wiring).

## 5. Email and WhatsApp platform: concrete shortlist with verdicts

The board's build-vs-buy table gives named candidates and trial verdicts. This is a
recommendation behind the human gate, not a decision. Decisive filter is Arabic: send a
real Arabic email and a WhatsApp template test before committing.

Engine layer (email, orchestration, segmentation):
- Trial Yes: MoEngage, Insider (both MENA-native strength).
- Developer-friendly: Customer.io.
- Budget: Brevo, Zoho.
- Skip: Mailchimp, HubSpot, Klaviyo (reported weak on Arabic RTL).

WhatsApp BSP layer (WhatsApp Business API):
- 360dialog (cleanest pass-through architecture, transparent pricing).
- Unifonic (if Saudi data residency is required).
- Others noted: Wati, Twilio, Gupshup.

Hard precondition from the board: name any incumbent platform before evaluating a switch.
The objective doc says one may already receive ManyChat data. Do not replace a working tool
we have not named.

Refines: `references/2026-06-email-whatsapp-platform-research.md` (deepens it), `agents/research-scout.md`.

## 6. Explicit out-of-scope, from the parking lot

The board's parking lot marks these out of scope or later-track. The swarm should not
produce work for them unless the user explicitly reopens scope:

- Enterprise and B2B (and by extension B2G) campaigns. Marketing's commercial job here is
  B2C subscriber acquisition and conversion; enterprise is a pipeline that awareness
  supports, not a campaign the engine runs now.
- Masterclass video creative. It needs creative derived from actual class footage, which is
  more complex and manual. Treat as a separate, later track. Skill Path creative (product-led,
  no footage dependency) is the in-scope creative path.

Refines: `agents/creative-director.md` (Skill Path creative in scope, Masterclass later),
`agents/strategy-lead.md` (B2C focus, enterprise out of scope for the engine).

---

## Board items that confirmed the build with no change needed

- Funnel diagram: two entry points (paid acquisition, owned non-payers), parallel creative
  and copy into build, signup gate, learnings feedback loop to strategy. Matches `SWARM.md`.
- Prompting strategy doc: orchestrator plus specialists, reasoning vs execution, context
  before generation, quality as a gate, borrow before inventing. Matches `_AGENTS-INDEX.md`
  and `SWARM.md` as written.
- Paid build SOP: greenfield for Skill Path ads, spend never without Ahmed's approval,
  staged for approval then launch on sign-off. Matches `agents/paid-build-engineer.md`.
- Recommended MCPs table and research-synthesis table: match the MCP strategy and the
  research-first posture already captured in the PROJECT brief and `brainstorm-reconciliation.md`.

## Open items the board leaves unresolved (unchanged from before)

- Name of the incumbent email and WhatsApp platform. Blocks the platform decision.
- Whether Saudi data residency (PDPL) is a hard requirement.
- Expected monthly email send and WhatsApp template volume.
- Who owns the ManyChat to engine integration on the dev side.
- The offer (price and promotion) for the first campaign. A brief input, never invented.
- Mobile (Apple IAP, Google Play, possibly RevenueCat) to event forwarding for the funnel.
- Access and approval process per tool, and GCC or Saudi data requirements.
- The marketing PM tool: Trello or Slack-based. The parking lot still holds placeholders the
  room has not filled.
