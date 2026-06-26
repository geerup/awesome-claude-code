# Privacy and data governance: open items for the human gate

This file surfaces the privacy, data-governance, and Saudi PDPL open items that the
compliance-privacy gate requires to be visible to Ahmed at the human gate. It is the package's
answer to the compliance gate's three structural findings (retention stance, data-subject rights,
point-of-collection disclosure) and the cross-cutting PDPL and data-residency item. Nothing here is
resolved or invented: each item is surfaced as an open decision for Ahmed and the legal function.
Western numerals. No em dashes. Nothing sends, publishes, spends, or wires.

- run_id: run-2026-06-12
- campaign_id: 2026-06-bassam-fattouh-makeup
- raised_by: compliance-privacy-reviewer (qa-compliance-verdict.md)
- status: open items, unresolved. Required visible before any send, pixel, audience build, or publish.
- resolution_owner: Ahmed, with the legal and data-protection function.

## Why this exists

The campaign collects and processes personal data of GCC users, primarily Saudi residents (email
addresses, WhatsApp numbers and opt-in timestamps, device push tokens, playback and engagement
events, and paid-pixel behavioral signals). The Saudi Personal Data Protection Law (PDPL) applies.
The compliance gate passed the design-level checks (no personal data in any URL or tracking
parameter, suppression rules stated, consent gating in place, no accreditation implication, nothing
actually sends) but failed the package on three governance gaps that must be surfaced, not left
silent. They are surfaced below. The fix is confirmation by Ahmed and legal, not invention here.

## 1. Point-of-collection disclosure (data-flows-disclosed): OPEN

Before any capture point goes live, a user-facing data-collection notice or consent mechanism must
be confirmed in place at the point of capture. The capture points in this campaign are:

- The signup gate (email or WhatsApp) that paid, organic, and blog traffic all route to.
- The free-intro-viewer email capture (free chapter entry without an account).
- The paid pixel or CAPI on the class page and any landing page (feeds retargeting and the lookalike seed).

For each, confirm: which platform receives the data, and that the user is shown a clear notice and,
where required, gives consent at that point. The platform being unconfirmed (open item 5) defers the
wiring, not the disclosure requirement.

## 2. Retention and deletion stance (retention-stance): OPEN

No retention or deletion period is confirmed for any data class. Confirm a period and a deletion path
for each, before go-live. Data classes in scope: email address; WhatsApp number and opt-in timestamp;
device push token; playback and engagement events; paid-pixel behavioral signals; the subscriber seed
used to model the lookalike. An unconfirmed period is an open item for Ahmed, not a reason to omit the
stance. The PDPL requires that personal data is not kept longer than its stated purpose needs.

## 3. Data-subject rights route (data-subject-rights): OPEN

No route is confirmed for a data subject to access, correct, or request deletion of their data. The
email unsubscribe and the WhatsApp reply-STOP are channel suppression mechanics, not rights routes.
Confirm the access and deletion route before any data-collection action goes live. The PDPL grants
data subjects rights of access, correction, and deletion.

## 4. PDPL and data residency: OPEN (cross-cutting)

- Data residency and cross-border transfer. The email, WhatsApp Business API, app-push, analytics, and
  pixel or CAPI platforms are all unconfirmed. The PDPL imposes data-residency and cross-border
  transfer requirements. Where data is stored, the governing jurisdiction, and any transfer basis are
  unresolved. Confirm before any platform is wired.
- Legal basis for processing. A lawful basis for marketing processing is required. Consent records for
  email, WhatsApp, and app-push are open items; their existence, form, and sufficiency are unconfirmed.
- Data minimization. Confirm each data class is limited to what the stated purpose requires.

## 5. What is correct at the design level (for context, not a resolution)

- No personal or sensitive data in any URL or tracking parameter. UTM wiring is deferred to
  data-tracking-engineer with an explicit no-personal-data requirement.
- Suppression for owned email sends: paying contacts, unsubscribed, hard-bounced, and channel-specific
  opt-outs, all stated.
- WhatsApp: prior marketing opt-in and pre-approved templates required, with an opt-out line on every
  message. Gated, not wired.
- App push: opt-in required per device. Gated.
- Paid retargeting and the lookalike seed: explicitly gated on a confirmed, consented pixel signal and
  the gate platform. No audience is built here.
- No accreditation implication anywhere. Nothing sends, publishes, spends, or renders.

## 6. Actions hard-blocked until the preconditions are confirmed

Regardless of human-gate approval, these cannot proceed until the named items land:

1. Any email send: email platform, PDPL residency, consent records, retention stance, rights route.
2. Any WhatsApp send: WhatsApp Business API provider, pre-approved templates, per-recipient opt-in
   records, PDPL residency, retention stance, rights route.
3. Any app-push send: push platform, per-device opt-in, PDPL residency, retention stance, rights route.
4. Any pixel or CAPI wiring: gate platform, point-of-collection notice, PDPL residency and transfer
   basis, retention stance, rights route.
5. Lookalike and retargeting audience build: consented pixel signal live, subscriber-seed consent,
   PDPL residency.
6. Signup gate live (email or WhatsApp capture): platform, point-of-collection notice, PDPL residency,
   retention stance, rights route.
7. Blog publish with a live signup-gate CTA: items 4 and 6.
8. Organic social publish routing to the signup gate: items 4 and 6.
9. Rendering the visual prompts: generative-tool build-vs-buy approval, rights-cleared Bassam imagery.

## Closing

These items are surfaced for the human gate. They are not resolved, and this file is not an approval.
Only the human gate approves, per action and per campaign. Silence is not approval.
