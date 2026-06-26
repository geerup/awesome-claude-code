# QA gate verdict: 2026-07-summer-bassam-led-sale (E1 to E7, AR + EN, 14 emails)

Gate stack per `runtime/verification.md`, run by independent reviewers on the rendered HTML.
Status: draft, nothing sends. All gates PASS after the fixes below. Open items are send-time
items for the human gate, not build blockers.

## Gate results

| Gate | Verdict | Notes |
|------|---------|-------|
| email-html-build (house-style sweep) | PASS | renderer exit 0; no em/en dash, no tatweel, Western numerals only |
| arabic-copy-qa (AR slots) | PASS | MSA Gulf-familiar, Thmanyah tone, feminine address on E1/E2 |
| english-copy-qa (EN slots) | PASS | plain, empowering, one CTA, no accreditation |
| email-asset-qa | PASS | rights-cleared, text-free, descriptive alt, brand constants, confirmed instructors; CloudFront staging is a send-time open item |
| accessibility-qa (WCAG 2.2 AA) | PASS | all 10 prior findings resolved by the renderer upgrade |
| compliance-privacy-check | PASS | no PII in URLs, unsubscribe + sender identity present, no accreditation; consent/PDPL/suppression surfaced as open items |
| brand-qa-reviewer | PASS | voice, constants, one CTA, cleared instructors, no held terms asserted |

## Fixes applied during the gate loop
- Offer terms genericized: removed 30%, code SUM30, and the 2026-07-06 date from all visible copy
  (E5-E7), removed the PromoLine; E2 dropped the "free" claim and points to the class page. Held
  values return on confirmation at the human gate.
- Accessibility upgrade to the shared renderer `scripts/email_render.py`: semantic `<h1>`/`<h2>`,
  `<ul role="list">`/`<li>`, logo `aria-label`, lightened footer/fine-print colors (MUTE #B9B9B9,
  FAINT #B3B3B3) to clear AA, promo badge solid fill. Re-rendered all 14.
- E1 reframed to "master the techniques" (removed a deficit-framed opener brand QA flagged).
- E2 reframed to "perfect the look".
- Cross-sell Arabic title changed to the gender-neutral "صفوف أخرى على مهارات" so it does not clash
  with the feminine address on E1/E2.

## Open items for the human gate (send-time, not build blockers)
1. Sale terms: confirm 30% / SUM30 / end date, then re-add the percentage, date, and PromoLine code to E5-E7.
2. E2 free tutorial: if the business unlocks a chapter free, restore the free framing + the free-chapter deep-link; otherwise E2 stays the current "perfect the look" teaser to the class page.
3. Images: E1/E2 hero is the Bassam class cover (CloudFront design proof); the 3 class-card portraits are on CloudFront. Stage to the Ortto CDN (m.autopilotapp.com) and swap before any send.
4. Hero imagery for E3-E7: now the real multi-instructor banner (Drive MultiInstructor_Unipal_Banner_16x9.png, fileId 1nskza7QCgQ0mcx1aonv5FhzcaRv5ZZZ4), text-free. The autopilot numbered images (1_7/2_7/3_6.png) were removed (generic carousel art with baked-in Arabic text, never headers). The banner is private in Drive: set it to anyone-with-link to render the preview, and stage it to the Ortto CDN before send.
5. Send platform (Ortto) not adopted: wire unsubscribe merge tag, ensure a plain-text MIME part, resolve consent and suppression (exclude paying, unsubscribed, hard-bounced).
6. Saudi PDPL / data residency, success-metric number+date, and audience size at send.
