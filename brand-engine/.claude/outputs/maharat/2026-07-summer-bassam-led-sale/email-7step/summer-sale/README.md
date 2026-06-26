# Summer of Skills, Bassam-led non-payer sale (E1 to E7)

Campaign: `2026-07-summer-bassam-led-sale`. Bilingual (Arabic primary, English matched), 14 emails
plus an `index.html` preview. Built with the slotted live-component renderer
(`scripts/email_render.py` from `spec.json`). Status: draft, approval-ready, nothing sends.

## Files
- `spec.json` : render source of truth (campaign fields + 14 email entries).
- `e1.ar.html ... e7.en.html` : the 14 upload-ready Ortto emails. `index.html` : preview sheet.
- `emails-review.md` : the human-readable copy of all 7 emails (the review doc).
- `qa-verdict.md` : gate stack results (all PASS) + open items.
- `rubric-conversion.md`, `rubric-conversion-scorecard.md`, `rubric.evals.json`,
  `rubric-scorecard.md` : the conversion rubric and scoring history.
- `insights.md`, `research-notes.md`, `strategy-artifact.md` : the inputs.
- Brief: `briefs/2026-07-summer-bassam-led-sale.md`.

## The 7-email arc (2 / 2 / 3)
1. E1 Bassam, master the techniques (CTA to the class page)
2. E2 Bassam, perfect the look (CTA to the class page)
3. E3 Maharat, build real skills this summer (CTA to the classes page; skill-domain list)
4. E4 Maharat, learn any skill, one subscription (CTA to the plans page)
5. E5 Summer sale, announce (CTA to the plans page)
6. E6 Summer sale, ends tomorrow (CTA to the plans page)
7. E7 Summer sale, ends today (CTA to the plans page)

Every email: logo, eyebrow + headline, body, one emerald CTA, the 3 cross-sell instructor cards
(Cedric Haddad, Elda Choucair, Ragheb Alama), footer with sender identity + unsubscribe. E1 and E2
carry the Bassam class-cover hero; E3-E7 are text-led (hero is an open item).

## Lifecycle-package (for the human gate)
- channel: email (owned). audience: owned non-payers (about 18,000), Arabic-speaking GCC adults,
  Bassam makeup as the lead hook. Resolve exact size from live data at send.
- flow and proposed cadence (start about 2026-06-23, over about 14 days): E1 Jun 23, E2 Jun 25,
  E3 Jun 28, E4 Jul 01, E5 Jul 03 (sale on), E6 Jul 05 (ends tomorrow), E7 Jul 06 (ends today).
  Time-based foundation; engagement branches (openers vs non-openers) layered at build.
- suppression: exclude paying contacts, unsubscribed, and hard-bounced.
- success_metric: subscription conversions in the flight window (target number + date = open item).
- send_on_approval (one line): "Sends a 7-email Arabic-and-English flow to about 18,000 non-paying
  contacts over about 14 days, starting on the confirmed date." Nothing sends until Ahmed approves
  and the open items below are resolved.

## Open items ledger (resolve at the human gate before any send)
1. Sale terms HELD: confirm 30% / code SUM30 / end date, then re-add the percentage, date, and the
   PromoLine code to E5-E7 (currently generic relative urgency only).
2. E2 free tutorial: if a chapter is unlocked free, restore the free framing + free-chapter
   deep-link; else E2 stays the "perfect the look" teaser to the class page.
3. Images: E1/E2 use the Bassam class cover; E3-E7 use the real multi-instructor banner
   (Drive MultiInstructor_Unipal_Banner_16x9.png, fileId 1nskza7QCgQ0mcx1aonv5FhzcaRv5ZZZ4). The
   autopilot numbered images (1_7/2_7/3_6.png) are removed (generic carousel art with baked-in
   Arabic text, never headers). Single manual step to make the banner display: set the Drive file
   to anyone-with-link (the spec's Drive hotlink then renders in the preview), or drag-drop it into
   the Ortto Asset Library. For send, stage the banner, the Bassam cover, and the 3 class-card
   portraits to the Ortto CDN (m.autopilotapp.com) and swap the srcs (Drive and CloudFront are not
   hot-linkable in the inbox).
4. Send platform: Ortto not yet adopted. Wire the unsubscribe merge tag, ensure a plain-text MIME
   part per send, and confirm consent basis and suppression source.
5. Saudi PDPL and data residency. Success-metric target number and date. Audience size at send.
6. Instructor public-naming reconfirm at the gate (Bassam plus the 3 cross-sell names are recorded
   confirmed 2026-06-19).

## Rebuild
`python3 .claude/scripts/email_render.py .claude/outputs/2026-07-summer-bassam-led-sale/email-7step/summer-sale/spec.json`
