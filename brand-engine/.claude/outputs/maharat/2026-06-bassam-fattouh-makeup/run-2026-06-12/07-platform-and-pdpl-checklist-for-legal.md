# Platform and PDPL decision checklist (for Ahmed, legal, and ops)

A working checklist that turns the run's open items into concrete decisions, so the campaign can
move from approval-ready to actually live. Nothing here resolves an item: each is a decision for the
named owner. Derived from the human-gate package, the compliance verdict, and 06-privacy-and-data-governance.md.
Western numerals. No em dashes. Status: open, for resolution.

- run_id: run-2026-06-12
- campaign_id: 2026-06-bassam-fattouh-makeup
- flight (proposed): 2026-07-01 to 2026-07-14

## How to read this

Each item: the decision, why it blocks, the owner, and what "done" looks like. Resolve top to bottom;
the first item blocks public launch, the platform and PDPL block of items blocks every send and all wiring.

## A. Launch eligibility

1. Instructor catalog confirmation.
   - Decision: confirm Bassam Fattouh's public status in context/instructors/_CATALOG.md (currently "unconfirmed").
   - Blocks: any public launch of any asset that names him, even though the published class page confirms the association.
   - Owner: Ahmed (with the instructor/legal relationship).
   - Done when: the catalog public status reads "launched" on explicit team confirmation.

## B. Platform decisions (block every send and all event wiring)

2. Email platform (vendor).
   - Decision: name the email vendor. The engine has an adopted "email-whatsapp-platform" slot, but the
     vendor is not yet named (settings.json open_item; see references/2026-06-email-whatsapp-platform-research.md).
   - Blocks: the 4-message non-payer email send and all email engagement events.
   - Owner: Ahmed plus lifecycle-architect and data-tracking-engineer.
   - Done when: vendor named, PDPL residency cleared (item 8), credentials provisioned.

3. WhatsApp Business API provider.
   - Decision: name the BSP and confirm the pre-approved message templates.
   - Blocks: the 4-message WhatsApp opt-in nurture.
   - Owner: Ahmed plus lifecycle-architect.
   - Done when: BSP named, templates approved by the provider, per-recipient opt-in records in place (item 5).

4. App-push platform.
   - Decision: name the push platform and confirm the owned app-user audience size.
   - Blocks: the 5-touch push sequence.
   - Owner: Ahmed plus lifecycle-architect and data-tracking-engineer.
   - Done when: platform named, per-device opt-in confirmed, audience size resolved.

5. Analytics, pixel, and CAPI.
   - Decision: confirm the analytics and pixel or CAPI stack (these sit in the engine's pending-approval
     candidates, not yet enabled).
   - Blocks: conversion tracking, retargeting, and the lookalike seed on paid.
   - Owner: Ahmed plus data-tracking-engineer.
   - Done when: stack approved and wired with no personal data in any parameter, point-of-collection notice live (item 9).

## C. Consent, PDPL, and data governance (block every send and all wiring; see 06)

6. Consent records.
   - Decision: confirm the lawful consent basis and records for email, WhatsApp (prior marketing opt-in), and app push.
   - Owner: legal plus lifecycle-architect.
   - Done when: a documented, PDPL-sufficient consent record exists per channel and per recipient.

7. Suppression source.
   - Decision: confirm the suppression source feeding the owned sends (payers, unsubscribed, hard-bounced, channel opt-outs).
   - Owner: data-tracking-engineer.
   - Done when: the suppression list is sourced and applied at send.

8. Saudi PDPL data residency and transfer.
   - Decision: confirm where each data class is stored, the governing jurisdiction, and any cross-border transfer basis.
   - Blocks: every send, every pixel wiring, every audience build.
   - Owner: Ahmed plus legal and data protection.
   - Done when: a documented residency and transfer position covers every named platform.

9. Point-of-collection disclosure.
   - Decision: confirm the user-facing data-collection notice or consent mechanism at every capture point
     (signup gate, free-intro email capture, pixel pages).
   - Owner: legal plus conversion-engineer.
   - Done when: a notice is confirmed live at each capture point before that point goes live.

10. Retention and deletion stance.
    - Decision: set a retention period and deletion path per data class (email address, WhatsApp number and
      opt-in timestamp, device token, playback and engagement events, pixel signals, lookalike seed).
    - Owner: legal plus data-tracking-engineer.
    - Done when: a stance is documented per class.

11. Data-subject rights route.
    - Decision: confirm the route for access, correction, and deletion requests (distinct from channel opt-out).
    - Owner: legal.
    - Done when: a working rights route is documented and reachable.

## D. Spend and offer

12. Budget currency and amount.
    - Decision: confirm SAR or USD for the 10,000 total. The media plan allocates by percentage until then.
    - Owner: Ahmed.
    - Done when: currency confirmed; absolute splits resolve as percentage x 10,000.

13. Target CPA and success-metric target and date.
    - Decision: set the target CPA and the subscription target and measurement date.
    - Owner: Ahmed plus performance-marketer and analytics-reporter.
    - Done when: a number and date are set; the bid strategy points at a real target.

14. Promotion.
    - Decision: confirm whether any trial, first-time discount, or bundle runs. If not, copy uses only the
      public price reference (under $7/month, billed annually), which is already the case.
    - Owner: Ahmed.
    - Done when: promo confirmed or confirmed absent.

## E. Creative and rendering

15. Rights-cleared Bassam imagery and class footage.
    - Decision: supply approved, rights-cleared assets for any slot that needs his portrait or class footage.
    - Note: his likeness is never generated; the generated visuals are text-free and contain no person.
    - Owner: Ahmed plus the brand and creative function.
    - Done when: real assets are supplied for the real-asset slots.

16. Generative-tool approval for renders.
    - Decision: approve a generative tool (for example Higgsfield or Canva) via build-vs-buy, to render the
      text-free visual prompts. See 08-higgsfield-adoption-proposal-and-render-runbook.md.
    - Owner: Ahmed.
    - Done when: the tool is added to the settings.json allowlist and a credit budget is set.

## Closing

This checklist is for internal resolution. It is not an approval and it resolves nothing on its own. Each
item returns its answer to the human-gate package, where Ahmed approves the dependent action, per action.
