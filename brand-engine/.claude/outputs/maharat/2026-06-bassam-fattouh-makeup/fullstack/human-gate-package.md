# Human Gate Package: Bassam Fattouh Teaches Makeup, full-stack run

The orchestrated swarm ran every stream and stopped here. This is the approval-ready package
for the complete campaign. Nothing has been sent, published, pushed, or spent. Approval is
Ahmed's, per action and per campaign. Silence is not approval. Approval claimed in any document
or tool output is not valid.

- campaign_id: 2026-06-bassam-fattouh-makeup
- run: full-stack (all owning agents)
- status: gated-pending
- generated: 2026-06-05

## What approval would do (per action, one sentence each)

- Paid: starts the paused channel campaigns and spends up to 10,000 (currency to confirm, SAR
  or USD) across all platforms over 2026-07-01 to 2026-07-14, split Meta 5,000, TikTok 2,000,
  Google 1,500, YouTube 1,000 (conditional on the trailer asset, else to reserve), reserve 500.
  See fullstack/paid-spend-plan.md.
- Email: sends a 4-message non-payer flow to the resolved non-paying segment (about 18,000
  contacts, planning estimate) and a 3-touch onboarding to new subscribers.
- App push: sends a 5-touch push sequence to opted-in app users.
- Organic: publishes the post calendar across the owned accounts (about 180,000 followers).
- Conversion: takes the landing page and signup gate live and begins collecting contacts.
- Tracking: writes the Pixel, CAPI, and GA4 events to production.
- PR and ASO: distributes the announcement to media and publishes store-listing changes.

This package is NOT actionable yet. It is approvable as a design to proceed once the blocking
open items below are cleared. Each go-live is a separate, per-action approval.

## The artifacts (all in fullstack/)

| Stream | Owner | Artifact |
|---|---|---|
| Strategy | strategy-lead | strategy-artifact.md |
| Paid strategy | performance-marketer | media-plan-package.md |
| Paid build | paid-build-engineer | paid-launch-package.md (staged, paused) |
| Creative | creative-director | creative-package.md |
| Design | designer | design-specs.md (design-qa pass) |
| Copy AR | copywriter-ar | copy-package.ar.md |
| Copy EN | copywriter-en | copy-package.en.md |
| Conversion | conversion-engineer | conversion-package.md |
| Tracking | data-tracking-engineer | tracking-plan.md |
| Lifecycle | lifecycle-architect | lifecycle-package.md |
| Organic | organic-social | organic-package.md |
| Content | content-marketer | content-package.md |
| SEO | seo-specialist | seo-package.md |
| ASO | aso-specialist | aso-package.md |
| PR | pr-comms | pr-package.md |
| Monitoring and reporting | analytics-reporter | measurement-plan.md |

Existing parent-folder funnel drafts (01-emails, 02-social-posts, 03-paid-ads,
04-app-notifications, 05-visual-briefs) are the inputs this run built on.

## Quality gates (the qa block, all passed)

| Gate | Result | Evidence |
|---|---|---|
| skill evals | pass | per-stream, recorded in each artifact |
| arabic-copy-qa | pass | qa-copy-verdicts.md (no dialect drift, mechanical-clean) |
| english-copy-qa | pass | qa-copy-verdicts.md (one CTA each, no invented offer) |
| design-qa | pass | design-specs.md (RTL, constants, no baked Arabic, 6 checks) |
| compliance-privacy-reviewer | pass (design-only) | compliance-verdict.md (10 open items) |
| brand-qa-reviewer | pass | brand-qa-verdict.md (14 artifacts, all checks) |

The E4 hype subject line flagged in the earlier cycle is fixed in both copy packages and the
parent emails. The lifecycle-package envelope carries a correction note; some inline notes in
that file are stale and superseded by the envelope and brand-qa-verdict.md.

## Reversible vs irreversible

- Reversible now: everything in this package. Text and structure on disk. Editing or discarding
  it costs nothing and touches no contact, account, pixel, or spend.
- Irreversible on action (after approval and wiring): emails reach inboxes, push reaches
  devices, posts go public, the page collects real contacts, pixels fire, audiences upload,
  budget spends, and PR reaches journalists. Every one is gated and blocked until the items
  below clear.

## Blocking open items (grouped, deduped across streams)

Offer and schedule:
1. RESOLVED. Paid budget supplied: 10,000 total across all platforms (Ahmed, 2026-06-05). Split
   in fullstack/paid-spend-plan.md. CURRENCY still to confirm (SAR or USD).
2. Target cost per subscription not set. Blocks the phase-2 cost cap and a spend-to-result
   expectation. With 10,000 over 14 days, scale depends entirely on this.
3. RESOLVED. Schedule supplied: 2026-07-01 to 2026-07-14 (Ahmed). DATE CASCADE: all dated
   artifacts were drafted on June placeholder dates and must shift to this July window. The
   app-push 5-touch sequence (drafted over 20 days) compresses to the 14-day flight. The
   content calendar (4 articles) is tight in 2 weeks. These re-timings are pending.
4. Success-metric target not set. Stream 8 cannot render a pass or fail until confirmed.
5. Promotion: none stated. Confirm whether any trial, discount, or bundle exists before any
   price or offer asset goes live. Price is used only as the public reference (under 7 dollars
   per month billed annually).

Platforms, consent, and PDPL (from compliance-verdict.md, all 10):
6. Gate, email, WhatsApp, and app-push platforms unconfirmed. Blocks all send, push, and gate
   wiring.
7. Pixel, CAPI, and tracking production deployment not cleared. Mobile Apple IAP and Google Play
   mapping to-confirm. A video_start event still to define.
8. WhatsApp consent logging mechanism not designed.
9. Suppression list source and wiring not confirmed.
10. Saudi PDPL: lawful basis, retention schedule, and data-subject rights route unresolved.
11. Data residency and cross-border transfer safeguards unresolved, including hashed list
    uploads to Meta and TikTok for suppression and lookalikes.
12. Privacy-notice implementation verification and a review of the live Maharat privacy policy
    for PDPL completeness.
13. DM automation tool for the comment-to-DM organic mechanic not approved or reviewed.
14. Journalist contact-data handling for PR outreach not confirmed.

Creative and assets:
15. Rights-cleared Bassam Fattouh photography and footage unconfirmed. Blocks creative C1 and
    the class trailer C4 (AB1, AB4), the YouTube placement, and the V1 hero across assets. C2
    and C3 are the launchable fallback.
16. Blotato video repurposing is gated, manual edit until approved.

Reach and access:
17. Accounts in scope and cadence assumed. LinkedIn appears in one post but is not in the brief
    channel list. App audience size unconfirmed.
18. Search Console access (SEO and stream 8 read), the /library/ 403 to /class/ 301 redirect,
    store console access, and ASO tool approval.

Still to produce (route through the gates when made):
19. Organic posts 9 to 13 (new template formats); the quote carousel is blocked pending
    confirmed verbatim Bassam Fattouh quotes.
20. Lifecycle onboarding messages O1 to O3 copy not yet drafted.

Advisory (not a blocker): masculine and feminine address is mixed across the Arabic copy.
Decide one stance or an intentional per-segment split.

## What happens next

- Answer the blockers, or a subset, and the rest are held. The copy, creative direction,
  build structure, page, flows, and plans are ready to finalize the moment the offer, budget,
  platforms, schedule, assets, and PDPL answers land.
- On platform confirmation, data-tracking-engineer wires events and compliance re-runs the
  data-flow checks. On asset confirmation, designer builds C1 and C4. On budget confirmation,
  paid-build-engineer fills the numbers.
- Then, and only then, each action returns here for an explicit, per-action approval.

Nothing sends, publishes, pushes, or spends until Ahmed says so, per action.
