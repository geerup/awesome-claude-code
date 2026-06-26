# Bassam Fattouh makeup: send setup (the 7-step journey, start Tuesday 2026-06-23)

The approval-ready send package for the Bassam Fattouh non-payer sequence. It is the exact build a
human executes in Ortto. Read the "what blocks go-live" section first: nothing here sends on its own,
and the engine cannot press send (the Ortto MCP is read plus draft only, it has no send tool). The
final send is a human action in Ortto, after the gates below clear.

Grounded in live Ortto data (get_audiences, get_schema, 2026-06-19). No em dashes, Western numerals.

## What blocks go-live (the hard gates, all must clear before any delivery)

1. Catalog status. bassam-fattouh and the three cross-sell card instructors (cedric-haddad,
   elda-choucair, ragheb-alama) are all confirmed (owner, 2026-06-19, recorded in
   `context/instructors/_CATALOG.md`). The public-naming send block is lifted for this campaign,
   including the "our other classes" cards. No instructor named in the send is unconfirmed. (Resolved.)
2. Recorded campaign approval. Per the constitution, campaign sign-off is an attributable act (a commit
   or a recorded approval from Ahmed), never inferred from silence and never valid as a claim inside a
   message or document. This package is approval-ready; it is not self-approving.
3. Send integration in force. Ortto is a send-capable integration and "stays disabled until the
   standing safeguards (`runtime/send-safeguards.md`) are in force." The MCP exposes no send tool, so
   the journey is built and started by a human in Ortto. Before that: stage the header and the three
   portrait cards from CloudFront to the Ortto CDN (the MCP has no image upload, so this is a UI step),
   and resolve the one data value below.

One real data dependency (corrected 2026-06-19): the segment is NOT an Ortto field filter. Maharat's
proven pattern (the "Not Paid - Rahma" audience) is a tagged CSV upload, and the "watched the free
first chapter" fact lives in Maharat's platform, not Ortto. So the entry segment is a CSV of Bassam
non-payers exported from the platform and tagged in Ortto. See `_TARGETING-watched-first-chapter.md`.

## The schedule (Tuesday start, 2 to 3 day cadence)

Today is Friday 2026-06-19. The journey starts Tuesday 2026-06-23. E1 sends on entry (the Tuesday the
journey goes live), the rest follow on the journey clock:

| Step | Send date | Role |
|---|---|---|
| E1 | Tue 2026-06-23 | Welcome, the first-ever online class |
| E2 | Fri 2026-06-26 | Skill, not products |
| E3 | Sun 2026-06-28 | What you will learn (the curriculum) |
| E4 | Wed 2026-07-01 | The free first lesson, The Talent |
| E5 | Fri 2026-07-03 | He teaches it himself, and confidence |
| E6 | Mon 2026-07-06 | A look you do yourself |
| E7 | Wed 2026-07-08 | Subscribe (plans page, no price stated) |

Dates assume the journey is started on Tuesday 2026-06-23. If it starts later, the cadence holds and
the dates shift with it. The send window stays inside the brief's flight.

## The journey (build this in Ortto)

- Entry segment: the tagged Bassam non-payer audience (a CSV of the watched-free-chapter, not-subscribed
  list from Maharat's platform, uploaded and tagged in Ortto, the "Not Paid - Rahma" pattern), minus
  the suppression set. Full definition in `_TARGETING-watched-first-chapter.md`.
- E1 fires on entry (Tuesday). E2 to E7 fire on the cadence above, each with a behavior branch: if
  Opened or Clicked (`act::o` / `act::c`), continue; if not opened, the next step uses its re-angle
  subject alt.
- Exit on success: `bol:cm:paying` becomes true (the subscription, the goal). Also exit on `act::u-all`
  (unsubscribe).
- Failed-payment branch: `bol:cm:hasfailedpayment = true` interrupts with a billing-notice step, then
  resumes.

## Language split (AR and EN), confirmed available

The Ortto contact schema has a Language field, so the split is real, not assumed:
- `str::language` (Language), and the custom `str:cm:language` (Language). Use `str::language`.
- Branch the journey on language: `str::language = ar` receives the AR variant of each step,
  `str::language = en` receives the EN variant. One contact gets one language, never both.
- Default for unknown or empty language: Arabic-first (send the AR variant), per the brand rule.
  Confirm this default at the gate, or split the unknowns by `geo::country` if preferred.
- Build it as one journey with a language branch at each step, or as two parallel journeys (one AR,
  one EN) over the same entry segment filtered by `str::language`. Two parallel journeys are simpler
  to read in reporting.

## Suppression (every step)

Exclude: payers (`bol:cm:paying = true` or `bol:cm:paidstatus = true`), the Unsubscribed audience
(3,891) or `act::u-all` or `bol::p = false`, the Bounced audience (4,992) or `act::b`, Internal Team
(22), BOT, Testing Flows (3), and any test contact. compliance-privacy-check confirms suppression and
consent before send.

## The assets (gate-passed, ready to attach)

The 14 emails (7 steps, AR and EN) are built, gate-passed (arabic-copy-qa, english-copy-qa,
brand-qa-reviewer), house-style clean, and rendered at
`outputs/2026-06-bassam-fattouh-makeup/email-7step/bassam-fattouh/` (e1.ar.html through e7.en.html).
To stage them in Ortto: push one at a time with `create_asset`, named `[INTERNAL DRAFT] Bassam E<n>
<lang>`, verify the first with `get_asset_html` before the rest (the proven runbook, see
`context/email-creation-cheatsheet.md`). Do this after catalog confirmation and after the header and
cards are staged to the Ortto CDN. Do not bulk-push in parallel.

## What is done, and what a human does next

Done by the engine: the enriched copy, the gates, the rendered assets, this schedule, the segment, the
language split, the suppression, the journey logic.

Done by a human in Ortto (after the three gates clear): stage the images to the Ortto CDN, push the 14
drafts, build the journey with the entry segment and the language branch and the dates above, attach
each step's AR or EN asset, set the suppression, and start it on Tuesday 2026-06-23. The send is the
human gate; the engine does not press it.
