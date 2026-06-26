# Benchmark: conversion and lifecycle

Internet benchmark for streams 6 (conversion path) and 7 (lifecycle messaging) of the
Maharat Marketing Engine. It pulls real-world frameworks for landing page structure,
event tracking plans (GA4 and Meta CAPI), onboarding and welcome flows, and winback and
reactivation flows, compares them to our skills, SOPs, templates, and handoff contract,
and lists prioritized gaps and recommendations.

Scope note: this is a comparison document only. It does not edit any skill, SOP, template,
or contract. Every recommendation is a proposal for Ahmed to weigh, consistent with the
do-not-adopt-without-approval rule.

Date of review: June 2026. All figures below are reported as the sources state them.

---

## Sources reviewed (web)

Landing page structure and conversion best practices:
- [Leadfeeder, 12 Landing Page Best Practices of 2026](https://www.leadfeeder.com/blog/conversion-optimization/landing-pages-convert/)
- [ALM Corp, Landing Page Optimization: 12 Data-Backed Strategies (2026)](https://almcorp.com/blog/landing-page-optimization/)
- [Branded Agency, Anatomy of a High Converting Landing Page, 14 Elements (2026)](https://www.brandedagency.com/blog/the-anatomy-of-a-high-converting-landing-page-14-powerful-elements-you-must-use-in-2026)
- [Genesys Growth, Landing Page Conversion Rates, 40 Statistics (2026)](https://genesysgrowth.com/blog/landing-page-conversion-stats-for-marketing-leaders)
- [Unicorn Platform, Landing Page Conversion Optimization in 2026](https://unicornplatform.com/blog/landing-page-conversion-optimization-in-2026/)

Measurement and event tracking plan (GA4 and Meta CAPI):
- [Google Analytics Help, GA4 Recommended events](https://support.google.com/analytics/answer/9267735?hl=en)
- [CodeLoom, Track Every Lead 2026: GA4 + Meta Pixel + UTMs](https://codeloomtechnologies.com/blogs/ga4-meta-pixel-utm-server-side-tracking-2026/)
- [DumbData, DataLayer Governance: 13 Checks for Healthy Measurement](https://dumbdata.co/post/datalayer-governance-practices-for-healthy-measurement/)
- [Addingwell, GA4 to Meta event mapping table for CAPI](https://docs.addingwell.com/ga4-meta-event-mapping-capi)
- [owntag, Set up Meta Conversion API (CAPI) with Server Side GTM](https://www.owntag.eu/blog/meta-capi-sgtm/)

Lifecycle, onboarding and welcome flows:
- [Bloomreach, Welcome Email Series Best Practices](https://www.bloomreach.com/en/blog/start-the-customer-journey-right-with-an-automated-welcome-email-series)
- [Mailsoftly, SaaS Onboarding Email Best Practices in 2026](https://mailsoftly.com/blog/user-onboarding-email-best-practices/)
- [Userpilot, Essential Onboarding Email Best Practices](https://userpilot.com/blog/onboarding-email-best-practices/)

Winback, reactivation, and sunset / drip cadence:
- [Klaviyo, 5 Win-Back Email Examples and Strategies](https://www.klaviyo.com/blog/winback-email-campaign-examples)
- [Shopify, Win-Back Campaigns: 7 Strategies to Re-Engage Lapsed Customers](https://www.shopify.com/enterprise/blog/running-winback-campaigns)
- [Recurly, Customer Winback Strategies for Subscriptions](https://recurly.com/blog/customer-winback-strategies-for-subscriptions/)
- [Polaris Growth, Sunset Flow Manual](https://www.polarisgrowth.com/en/blog/sunset-flow-manual)

---

## Best-in-class elements

### Landing page structure
- One stable content sequence: relevance (is this page for me), mechanism (how the offer
  creates value), confidence (proof and risk clarity), action (one next step). Headline
  answers "what is in it for me" within 5 seconds.
- A single primary CTA per page, no competing actions. Removing main navigation has been
  measured to lift conversion by 100 percent or more, because every extra link is an exit.
- Form length is the single largest lever in the sources: reducing fields delivers up to a
  120 percent lift, headline optimization 27 to 104 percent. 3 to 5 fields is the lead-gen
  sweet spot.
- Page speed: a 0.1 second improvement raises conversions 8 to 10 percent. 53 percent of
  mobile users abandon a page that takes over 3 seconds. 83 percent of traffic is mobile,
  yet mobile converts lower (about 2.5 to 2.9 percent) than desktop (about 4.8 to 5.1
  percent), so mobile friction is where the loss concentrates.
- Trust and proof elements (testimonials, badges, risk clarity) placed near the CTA.
- Personalization by source or segment is now table stakes; generic pages underperform.

### Event tracking plan (GA4 and Meta CAPI)
- A measurement plan links four things: the events tracked, the business objective each
  serves, the custom dimensions and parameters, and developer implementation notes.
- Standard GA4 lead-and-purchase events: page_view, generate_lead (or sign_up), and
  purchase. GA4 mapping to Meta is conventional: page_view to PageView, generate_lead to
  Lead, purchase to Purchase.
- Naming governance: snake_case, lowercase, under 40 characters, a parameter dictionary,
  one trigger per event, and event versioning to prevent collisions and regressions.
- Server-side plus browser sending (Pixel plus CAPI) requires a shared event_id for
  deduplication so the same action is not counted twice.
- Validation in GA4 DebugView and realtime before launch, plus consistent UTMs.
- A defined event taxonomy spanning web and mobile (app events) so the funnel is one
  picture, not two disconnected ones.

### Onboarding and welcome flows
- The welcome message should fire within seconds of signup; a delayed welcome can lose
  half its open rate. Welcome series carry the highest engagement of any email type.
- Typical onboarding length: 3 to 7 emails over 1 to 2 weeks (SaaS often 5 to 8). 3 to 5
  is the common sweet spot.
- Cadence: tighter early (near-daily in the first 3 to 4 days to hold momentum), then
  spacing out to every 2 to 3 days.
- Behavior-triggered sends outperform pure time-based drips: respond to whether the user
  took the first activation step, branch accordingly.

### Winback, reactivation, and sunset
- Winback sequence length: 3 to 5 emails, commonly triggered at 30, 60, and 90 days of
  inactivity.
- Segment lapsed contacts by recency, frequency, and value (RFM) rather than treating all
  the same; offer relevance drives reactivation.
- Sunset discipline: if a contact has not opened or clicked in roughly 90 to 180 days, or
  after 3 to 4 winback attempts, run a short final sunset flow (1 to 3 emails, no more than
  3) then suppress. Sunsetting protects sender reputation and deliverability, and it keeps
  the list to consenting, engaged contacts.
- 1 in 4 new subscriptions can come from previously lapsed contacts, so the lapsed base is
  a real channel, not dead weight.

---

## Our coverage

Conversion path (stream 6):
- `skills/06-conversion-path/SKILL.md` is the hub: validates the incoming envelope, routes
  page to `landing-page` and measurement to `event-tracking`, runs operational verification
  (RTL render, events fire, gate submits), surfaces open items, assembles the
  `conversion-package`, routes go-live to the human gate.
- `skills/06-conversion-path/landing-page/SKILL.md` and
  `.../landing-page/templates/landing-page-spec.md`: hero headline, optional subhead, body,
  one primary CTA, each region bound to a QA-passed copy variant id (no free text). Visual
  constants #141414, #1A1A1A, #009975. RTL primary, Western numerals, fast first render,
  CTA above the fold on mobile. One-CTA rule and cut-anything-that-does-not-move-the-click
  are explicit.
- `skills/06-conversion-path/event-tracking/SKILL.md` and
  `.../event-tracking/templates/event-tracking-plan.md`: four funnel events page_view,
  gate_view, submit, confirm; each mapped to Meta Pixel or CAPI and to GA4; non-identifying
  parameters only; mobile (Apple IAP, Google Play) flagged to-confirm; a test plan firing
  each event once in order before go-live.
- `sops/06-conversion-path.md`: same shape, plus the ManyChat note (captures Instagram
  leads, does not send email; email handoff is an open integration item).

Lifecycle messaging (stream 7):
- `skills/07-lifecycle-messaging/SKILL.md` is the hub: routes segmentation first, then the
  flow sub-skill; resolves audience size at send; marks the package not-sendable until the
  platform is confirmed; stops at the human gate.
- `skills/07-lifecycle-messaging/segmentation-logic/SKILL.md` and its template: entry
  trigger, segments (never-engaged vs lapsed-engaged, prior interest, recency of last
  open), engagement branches (opened or clicked vs not opened), inter-message timing inside
  the send window, and a non-optional suppression set (paying, unsubscribed, hard-bounced)
  with a source.
- `skills/07-lifecycle-messaging/nonpayer-email-flow/SKILL.md` and its template: a 4 to 5
  message ordered flow (entry, value, offer, engagement branch, optional last call), each
  bound to a QA-passed copy variant id, with `send_on_approval` and suppression.
- `skills/07-lifecycle-messaging/onboarding-sequence/SKILL.md` and its template: a reusable
  3-message shape (welcome, first step, activation branch on whether the first step
  happened), behavior-branched, copy by id.
- `sops/07-lifecycle-nonpayer-email.md`: the full non-payer SOP with the proposed message
  shape and the gate discipline.

Contract:
- `runtime/handoff-contract.md` defines `conversion-package` (page, gate, event_plan,
  open_items), `lifecycle-package` (flow, audience_size, send_on_approval, suppression),
  and `tracking-package` (events, pixel_capi_map, ga4_map, mobile_map, warehouse_refs,
  open_items). The common envelope carries status, a full QA block, open_items, brief_refs.

---

## Gaps and missing elements (prioritized)

P1, highest impact:
1. Winback and reactivation flow is missing as a named flow. Stream 7 has non-payer and
   onboarding sub-skills but no lapsed or churned-payer reactivation flow with RFM-style
   recency segmentation and the 30 / 60 / 90 day trigger pattern. The sources treat the
   lapsed base as a top acquisition channel (1 in 4 new subscriptions).
   Sources: Klaviyo, Shopify, Recurly.
2. No sunset flow and no engagement-decay suppression rule. Our suppression set is
   paying, unsubscribed, hard-bounced. The best-in-class adds: not opened or clicked in
   roughly 90 to 180 days, or after 3 to 4 attempts, run a 1 to 3 email sunset then
   suppress. This protects deliverability and keeps the list to consenting contacts, which
   is also a PDPL-friendly hygiene practice.
   Sources: Polaris Growth, Klaviyo.
3. Event-tracking plan omits a post-signup conversion event. We track to `confirm` (the
   opt-in). For a course product the revenue moment is a purchase or subscription start,
   which maps to GA4 purchase and Meta Purchase, and is the event paid optimization and CAPI
   actually need. The four-event model stops at lead, not value.
   Sources: Google GA4 recommended events, CodeLoom, Addingwell.

P2, meaningful:
4. No event-id deduplication requirement for dual Pixel-plus-CAPI sending. Without a shared
   event_id the same action is double counted across browser and server. This is a concrete,
   testable line the event-tracking template should carry.
   Sources: owntag, Addingwell, CodeLoom.
5. No explicit naming-convention and parameter-dictionary governance for events. Best
   practice is snake_case, lowercase, under 40 chars, one trigger per event, a parameter
   dictionary, and versioning. Our template names destination events per side but does not
   state the convention or a dictionary, which is where drift and collisions start.
   Source: DumbData.
6. Landing page lacks a social-proof / trust region and a form-length rule. Our spec has
   hero, subhead, body, CTA, but no proof-near-CTA region and no guidance to minimize gate
   fields (3 to 5, the single largest measured lever). The page is correctly minimal but
   has no place to put evidence, which the sources rank as a core conversion driver.
   Sources: Branded Agency, ALM Corp, Genesys Growth.
7. Onboarding welcome has no send-latency rule. Best practice fires the welcome within
   seconds of signup; a delayed welcome loses about half its open rate. Our shape says
   "new signup confirmed" but sets no latency target.
   Sources: Bloomreach, Userpilot.

P3, refinements:
8. No page-speed or render budget number. The landing page spec says "fast first render"
   and "minimal blocking assets" but sets no target. The sources quantify it: under 3
   seconds, and 0.1s improvements move conversion 8 to 10 percent. A stated budget makes the
   operational check objective.
   Sources: Genesys Growth, Unicorn Platform.
9. Cadence numbers are left to the brief without a default recommendation. Onboarding 3 to 7
   over 1 to 2 weeks, winback at 30 / 60 / 90, tighter-early then spacing. Keeping cadence a
   brief variable is correct and campaign-agnostic, but the skills could cite a default range
   as guidance, the way the non-payer SOP already proposes a message shape.
   Sources: Mailsoftly, Userpilot, Klaviyo.
10. No remove-navigation instruction on the landing page. Implied by "one clear CTA, cut
    anything that does not move the click" but not stated, despite a measured 100 percent
    lift. Worth making explicit.
    Source: Leadfeeder.

---

## Where ours is stronger

Our engine is more disciplined than the public best-practice content on every axis below.
The sources optimize for conversion rate; they are largely silent on correctness, privacy,
and consent, which our engine treats as hard stops.

- RTL correctness. The landing-page spec sets document direction rtl, Arabic primary, and
  requires that mixed Arabic, English, and numerals do not break direction, tested on the
  rendered page. None of the conversion sources address right-to-left layout at all.
- No PII in URLs or tracking. A hard stop across `event-tracking`, `segmentation-logic`,
  and the SOP: never email, phone, name, or sensitive values in a URL parameter. The
  tracking sources discuss UTMs and parameters freely without this constraint.
- Suppression and consent discipline. Suppression is non-optional and stated with a source
  (paying, unsubscribed, hard-bounced). The sources mention suppression mainly as a
  deliverability tactic; we make it a structural precondition of any send.
- Platform-open-item blocking. Until the email or WhatsApp send platform is named and
  approved, the package is design-only and not-sendable, and the gate wiring is blocked.
  The sources assume a platform is already in place and never gate on it.
- Human gate before send or go-live. Nothing publishes, sends, or spends without explicit
  per-action, per-campaign sign-off, and silence is never approval. The sources optimize for
  automated, always-on sends.
- Not-sendable design state. The lifecycle package can be fully designed and QA-passed yet
  explicitly marked not-sendable, separating creative readiness from authority to send. This
  has no equivalent in the public material.
- Copy-by-id, never invented. Every page region and every flow message binds to a QA-passed
  copy variant id; the conversion and lifecycle skills never write copy. This traceability
  is stronger than the source guidance, which mixes copywriting into the same step.

---

## Recommendations (prioritized, tied to sources)

These are proposals for Ahmed. They name the file that would change; none are applied here.

1. Add a winback / reactivation flow sub-skill to stream 7 (proposal for a new
   `skills/07-lifecycle-messaging/winback-flow/`). RFM-style recency segmentation, triggers
   at 30 / 60 / 90 days of inactivity, 3 to 5 messages, offer relevance per segment, all copy
   by id, behind the human gate with the same not-sendable discipline.
   Tied to: Klaviyo, Shopify, Recurly.
2. Add a sunset rule and engagement-decay suppression to `segmentation-logic/SKILL.md` and
   its template: after roughly 90 to 180 days with no open or click, or 3 to 4 attempts, run
   a 1 to 3 email sunset then suppress. Frame it as deliverability and consent hygiene, which
   also strengthens the PDPL posture.
   Tied to: Polaris Growth, Klaviyo.
3. Extend the event model in `event-tracking/SKILL.md` and `event-tracking-plan.md` with a
   post-confirm value event (purchase or subscription start), mapped to GA4 purchase and Meta
   Purchase, kept consistent with the existing no-PII rule. This is the event paid
   optimization and CAPI need.
   Tied to: Google GA4 recommended events, CodeLoom, Addingwell.
4. Add an event-id deduplication line to the event-tracking template: when an event is sent
   by both Pixel and CAPI it must share one event_id, verified in the test plan.
   Tied to: owntag, Addingwell.
5. Add an event naming-and-parameter governance note: snake_case, lowercase, under 40 chars,
   one trigger per event, a short parameter dictionary, and a version field, so naming does
   not drift across campaigns.
   Tied to: DumbData.
6. Add a proof / trust region and a gate-field-count rule to `landing-page-spec.md`: an
   optional evidence region near the CTA, and a 3 to 5 field maximum on the gate. Keep the
   minimal aesthetic; this adds a place for proof, not clutter.
   Tied to: Branded Agency, ALM Corp, Genesys Growth.
7. Add a welcome send-latency target to `onboarding-sequence/SKILL.md`: fire message 1
   within seconds to minutes of signup confirmation.
   Tied to: Bloomreach, Userpilot.
8. Add a page-speed budget to the landing-page spec performance section: target under 3
   seconds, prioritize the CTA in first render, as an objective operational check.
   Tied to: Genesys Growth, Unicorn Platform.
9. Add default cadence guidance (as proposals, not hard-coded values) to the onboarding and
   non-payer skills, mirroring how the non-payer SOP already proposes a message shape:
   onboarding 3 to 7 over 1 to 2 weeks, tighter-early then spacing; winback 30 / 60 / 90. The
   brief still overrides.
   Tied to: Mailsoftly, Userpilot, Klaviyo.
10. State the remove-navigation rule explicitly in the landing-page spec, alongside the
    existing one-CTA rule.
    Tied to: Leadfeeder.
