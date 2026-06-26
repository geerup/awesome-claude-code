# Maharat user lists: the segmentation backbone (mined)

Source: [User Lists Required](https://docs.google.com/document/d/18fWRgXlStW1V5Wyr12p3yGlvhE_w5h1amRXrREDowG8/edit)
(00- Maharat / 07 Email and WhatsApp Marketing, last updated Oct 2024). Extracted
2026-06-04. This is the team's own list architecture; the engine adopts it rather
than inventing one. Drop-in for the real repo's segmentation-logic skill.

## The six automated lists (tag, fields, exclusions)

| # | Tag | Who | Fields | Removed when |
|---|---|---|---|---|
| 1 | Failed Payments | failed a payment, no purchase within the following 2 hours | email, country, attempted plan, promo code, registration date, purchase date | purchased any plan |
| 2 | Non-paying users | created an account, never paid | email, country, registration date | failed payment (moves to list 1) |
| 3 | Non-paying newsletter members | gave an email via any site form or newsletter, no purchase | email, country, registration date | n/a recorded |
| 4 | Class Purchasers | bought a single class | adds plan, promo, minutes watched, gift | n/a recorded |
| 5 | Paying Subscribers | active subscription | adds plan, promo, minutes watched, first cycle, renewed, gift | n/a recorded |
| 6 | Gifters | bought a gift | adds gift purchased, gift date, minutes watched | n/a recorded |

## How this maps to the non-payer email flow (the first build)

- The flow's audience is lists 2 + 3 + 4 (never-activated accounts, newsletter leads,
  single-class buyers as the upsell sub-segment), matching the board's three
  sub-groups exactly.
- Suppression comes free: list 5 (paying subscribers) is the exclusion set; list 1
  (failed payments) is its own recovery flow with a 2-hour urgency window, distinct
  from the non-payer arc.
- "Minutes watched" is the engagement field: it splits list 4 (and 2 where data
  exists) into engaged vs dormant, which is the entry-message split the SOP requires.
- Gifters (list 6) are an unmined play: gift buyers know the product and have a
  natural repeat occasion. Park as a future campaign idea.

## Open engineering item (carried from the source doc)
The doc's own note: historical data must be pulled without disrupting existing email
lists, and the pulls must be automated going forward. Ownership of that automation is
unassigned (joins the ManyChat-integration open item).
