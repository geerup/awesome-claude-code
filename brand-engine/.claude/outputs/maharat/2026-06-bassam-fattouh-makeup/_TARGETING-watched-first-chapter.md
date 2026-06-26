# Bassam Fattouh makeup: targeting the non-payers who watched the free first chapter

The targeting for the Bassam Fattouh 7-step drafts on Ortto. Grounded in live Ortto data read
2026-06-19 (get_audiences, get_schema, and the actual audience filters via get_contacts). Aggregate
only, no contact PII retained. No em dashes, Western numerals. Sends happen in Ortto: the MCP reads
and drafts, it cannot send.

## The short answer (corrected to the real mechanism, 2026-06-19)

The earlier plan assumed an Ortto field filter (NonPaying AND classId = Bassam). The live data shows
that is wrong, in two ways:
- The `Created Account - NonPaying` audience is defined as `signed_on has value AND classId has NO
  value AND planId has NO value`. It explicitly excludes anyone who has a classId, so "NonPaying AND
  classId = Bassam" returns zero.
- The proven per-instructor non-payer audience, `Accounts Created / Not Paid - Rahma` (238), is not a
  classId filter at all. Its filter is a Tag: `Accounts Created Post-Rahma Dec 3.csv`. It was built by
  uploading a CSV of Rahma's non-paying account-creators into Ortto and tagging them.

So the real mechanism, the one Maharat already uses, is a tagged CSV, not an Ortto field query. Ortto
also has no per-chapter watch event, so "watched the free first chapter" is not knowable inside Ortto.
That fact lives in Maharat's platform.

## How to build the Bassam non-payer segment (the Rahma pattern)

1. In Maharat's platform (not Ortto), pull the list: accounts that engaged the Bassam makeup class,
   that is watched chapter 1 "The Talent" (the free intro), AND have no active subscription. Include
   email, language, and country if available. This is the "watched the free first chapter and did not
   subscribe" population. It is a backend export, the one real dependency.
2. Upload that CSV into Ortto and tag it, for example `Bassam Makeup Non-Payers 2026-06`, exactly as
   the Rahma list was tagged. Keep the file name meaningful, Ortto records the tag from it.
3. Build the audience as that tag, minus the suppression set below. This is the entry segment for the
   journey.

If the platform cannot isolate "watched chapter 1" specifically, the next best list is "created an
account for the Bassam makeup class and did not subscribe," which is the same shape as the Rahma list.

## The closest Ortto-native segment (the chosen path, 2026-06-19)

Until the platform CSV can be pulled, the nearest segment Ortto can build today from owned data is
Bassam email-engagers who have not subscribed:

- Base: contacts who Opened or Clicked a past Bassam campaign already in the account, the 2024
  "Bassam Fattouh Class Launch" (id 66713c733503c1113ed94805) and "Bassam Fattouh Follow Up" (id
  667ec02deda650586186be02), plus the Bassam teasers. Build it with an email-activity condition
  (Opened or Clicked, those campaigns). This is the owned, Bassam-specific interest signal.
- AND not paying: `bol:cm:paying = false` (and `bol:cm:paidstatus = false`).
- Minus the suppression set below. Language split on `str::language` (ar and en).

What it is and is not: this is "showed interest in Bassam by email and has not subscribed," not
literally "watched the free first chapter." Those 2024 campaigns are older, so the signal is stale and
misses free-chapter watchers who never engaged the emails. It is the closest native proxy; the tagged
CSV from the platform (above) is the higher-fidelity version when it can be pulled. The broad fallback
is the whole NonPaying pool (13,281) as a brand-level nurture, but that is not Bassam-specific.

## The owned audience context (Ortto, 2026-06-19)

| Audience | Emailable | Role here |
|---|---|---|
| Accounts Created / Not Paid - Rahma | 225 (238 members) | The precedent. Build "Not Paid - Bassam" the same way, a tagged CSV. |
| Created Account - NonPaying | 13,281 (14,925 members) | NOT the target: it is the no-classId, no-planId cold pool, not the per-class non-payers. |
| Subscribers | 24,676 | Full base, not the target. |
| Unsubscribed | 3,891 | SUPPRESS |
| Bounced | 4,992 | SUPPRESS |
| Internal Team / BOT / Testing Flows | 22 / 0 / 3 | SUPPRESS |

## Language split (AR and EN), confirmed available

The contact schema has a Language field, so the split is real:
- `str::language` (Language). Split the journey: `ar` receives the Arabic variant of each step, `en`
  the English. One contact, one language, never both.
- The uploaded CSV should carry each contact's language so `str::language` is set on import. If a
  contact has no language, default Arabic-first (send the AR variant), or split the unknowns by
  `geo::country`. Confirm the default at the gate.

## Suppression (every step)

Exclude: payers (`bol:cm:paying = true` or `bol:cm:paidstatus = true`), the Unsubscribed audience
(3,891) or `act::u-all` or `bol::p = false`, the Bounced audience (4,992) or `act::b`, Internal Team
(22), BOT, Testing Flows (3), and any test contact. compliance-privacy-check confirms suppression and
consent before send.

## The journey (the 7-step in Ortto)

- Entry: contact enters the tagged Bassam non-payer audience (the CSV upload above), minus suppression.
- E1 on entry, E2 to E7 on a 2 to 3 day cadence, each with an open/click branch (`act::o` / `act::c`).
- Exit on success: `bol:cm:paying` becomes true. Also exit on `act::u-all` (unsubscribe).
- Failed-payment branch: `bol:cm:hasfailedpayment = true` interrupts with a billing-notice step.

## Measurement

Subscription conversion, the `bol:cm:paying` transition during or shortly after the sequence, read with
`get_email_report` (opens and clicks per step) plus the paying field movement. Opens are a health
signal, not the goal.

## Build it now: the exact audience (so the send is one click)

The Ortto MCP has no audience-creation tool (confirmed 2026-06-19: it can create assets, articles,
categories, and SMS, not audiences), so the engine cannot create the audience object. Here is the
exact definition to build once in the Ortto UI (Audiences, New audience). It takes about 2 minutes,
and Ortto shows the live count as you add each condition.

Name it: `Bassam Makeup Non-Payers (engaged) 2026-06`

Conditions (match ALL):
- Activity: `Opened email` OR `Clicked email`, where the email is from the campaign
  `Bassam Fattouh Class Launch` (id 66713c733503c1113ed94805) OR `Bassam Fattouh Follow Up`
  (id 667ec02deda650586186be02). These are the 2024 makeup-launch sends, the owned Bassam-interest
  signal. (Add the `Bassam_ColdEmail Outreach` send, id 66fd77951e14f7185f9434e6, only if you want a
  slightly wider net; it delivered to about 163.)
- AND `Paying` (`bol:cm:paying`) is false, AND `paid_status` (`bol:cm:paidstatus`) is false.
- AND `Email permission` (`bol::p`) is true (consent).
- EXCLUDE: the `Unsubscribed` audience, the `Bounced` audience, `Internal Team`, `BOT`, and
  `Testing Flows`.

Size: the two campaigns had about 5,229 and 1,875 opens (2024). Deduplicated and minus payers and the
suppression set, expect low thousands. The exact live count appears in the builder.

Language split (at the journey, not the audience): branch each step on `str::language`, `ar` to the
AR variant and `en` to the EN variant. One contact, one language.

Higher-fidelity upgrade: when the platform CSV of watched-free-chapter non-payers is available
(above), swap the engagement condition for `In audience: the tagged CSV` and keep the rest.

Then sending is straightforward: set the journey entry to this audience, attach the 14 enriched
drafts per step and language, apply the dates in `_SEND-SETUP-bassam.md`, and start Tuesday.

## What is needed to execute (the open items)

- The one real dependency: the Bassam non-payer CSV from Maharat's platform (the watched-free-chapter,
  not-subscribed list), uploaded to Ortto and tagged. Who can pull this export is the question to
  resolve. The classId Ortto field is NOT a reliable substitute (it is empty for non-payers).
- Suppression applied, consent valid, no personal or sensitive data in any URL or tracking parameter,
  Saudi PDPL and the US data-residency decision still open.
- Catalog status: bassam-fattouh and the three cross-sell card instructors (cedric-haddad,
  elda-choucair, ragheb-alama) are all confirmed by the owner 2026-06-19, so the send block is lifted
  and the cards stay as built. The rest of the roster stays unconfirmed.
- Stage the header and portrait cards from CloudFront to the Ortto CDN, and replace the stale
  2026-06-18 Bassam drafts (old pre-enrichment copy) with the gate-passed enriched assets. The send is
  a human action in Ortto.
