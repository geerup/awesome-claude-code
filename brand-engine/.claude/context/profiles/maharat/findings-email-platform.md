# FINDING: the incumbent email platform is Ortto

Extracted 2026-06-04 from 00- Maharat / 07 Email and WhatsApp Marketing. This closes
the highest-priority open item from the project brief and the board ("what is the
current email and WhatsApp platform? Block the platform decision until it is named").

## The evidence
- [Ortto Integration List of Questions](https://docs.google.com/document/d/1jEnXc54gXdFZZDRFoPqtWKTmErloiH9lb-fDZIS8RC4/edit)
  (Feb 2024): working integration questions about website lead capture into the
  platform, where leads land, extraction to the database, and adding a cart event at
  the plans page.
- [Email Marketing - Process Improvement](https://docs.google.com/document/d/1olDTDqs1U8aWubQ_Fk15Q2H1EjIT99J7rcjDFYz5hLA/edit)
  (Oct 2024): a design-and-build plan for a branded email component system "within
  Ortto (or other)": palette, type, buttons, header, footer, hero, list, video modules.

## What this changes
1. The build-vs-buy question is no longer greenfield selection. Per the board's hard
   precondition, the incumbent is named: the evaluation becomes validate-and-decide,
   Ortto vs the shortlist (MoEngage, Insider, Customer.io, Brevo, Zoho). The decisive
   filter is unchanged: send a real Arabic email test from Ortto first.
2. The "(or other)" in Maharat's own doc and the later platform research suggest the
   team itself was unsure about keeping it. The docs are from 2024; whether Ortto is
   still live in mid 2026 must be confirmed (queue item), not assumed.
3. The ManyChat handoff design (webhook to the engine ingest) now has a concrete
   target to test against.

## Confidence and caveats
Evidence is internal and unambiguous for 2024. Currency (still in use today) is the
one open question. Until confirmed: treat Ortto as the working assumption for
integration design, and as the first platform to run the Arabic test on.

## Also found in the same folder
- TPAY Announcement subfolder (Aug 2025): suggests a carrier-billing or payment
  announcement campaign; relevant to the payments side, peek in phase 2.
- WhatsApp subfolder (Jan 2025): present but empty via the connector (likely sheets
  or PDFs); the WhatsApp BSP question stays open. Read manually.
- Database, Cold Emailing, Failed Payments, Inspo subfolders: phase-2 targets.

## UPDATE 2026-06-04 (same run): the Feb 2025 CRM Requirements doc completes the story

Source: [Maharat CRM Requirements](https://docs.google.com/document/d/1WuDfyA_yyjdAJ6_PioxIfmNLkfqeyTduAjQzZLz9cag/edit)
(Feb 2025, owner-brief: George; technical advisor named: Vahakn).

1. Explicit, more recent confirmation: "We currently use Ortto to send our emails."
2. The stated direction is a FULL MIGRATION FROM ORTTO TO HUBSPOT (long-term), with an
   interim HubSpot MVP plan (5 steps: fields and custom objects mirroring the user and
   accounts sheets, database import via AWS integration research, automation workflows,
   data clean-up, team training).
3. TENSION TO RESOLVE, NOT PAPER OVER: the workshop's platform research verdict was
   skip HubSpot (reported weak Arabic RTL), while the team's own roadmap is HubSpot.
   Both are real inputs. The decision step must reconcile them: where is the migration
   today (mid 2026), and did an Arabic test on HubSpot ever run? Owner: Ahmed with
   George and Vahakn.
4. Retention trigger spec (adopt into stream 7): subscribers without saved payment info
   enter a retention flow starting 30 days before expiry.
5. Plan-structure discrepancy: this doc says class purchaser vs 6-month vs 12-month
   subscribers; the company brief says 1, 3, and 12 months. Confirm the real plan
   lineup; never assume either in copy.
6. Source-based flow routing precedent: a lead who came via the business-guide freebie
   routes into a business-oriented flow (Toufic's class, soft skills first). This is
   the lead-magnet-to-flow mapping pattern for stream 7.
7. Long-term items already on the team's list (the engine should align, not duplicate):
   Zendesk or Wati for support (Wati also sits on the WhatsApp BSP shortlist),
   B2B cold email, viewership-level triggers from the site backend (watched 30 percent
   of a class, send continue-watching), app notifications inside flows, omnichannel
   multi-touch flows (email then SMS or WhatsApp), per-email conversion attribution,
   A/B testing, click and scroll tracking.
