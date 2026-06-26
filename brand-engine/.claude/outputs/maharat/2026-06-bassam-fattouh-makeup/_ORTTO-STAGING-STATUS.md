# Bassam makeup 7-step: Ortto staging status (2026-06-19)

All 14 enriched, send-correct emails are staged as drafts in the Maharat Ortto account. Nothing
sends. A draft is not a send and not a spend, so this sits inside the read-plus-draft scope. The
campaign-level human sign-off and the send wiring are still ahead (see the open items below).

## Staged: 14 of 14 (the enriched set, AR and EN)

Naming convention: `[INTERNAL DRAFT] Bassam Makeup 7-step E<n> <lang> (enriched 2026-06-19)`, so these
are never mistaken for a live campaign. Each imported with 5 image modules intact (logo, hero, and the
3 cross-sell card portraits as real images, not the dropped background-overlay) and the valid Ortto
unsubscribe token `{{ urls.unsubscribe }}`. No view-in-browser link (Maharat sends carry none).

| Step | Lang | Asset id | Subject |
|---|---|---|---|
| E1 | AR | `6a35138c1a0de4700244eb71` | أول صف لبسام فتّوح، على مهارات |
| E1 | EN | `6a351ba3a4d6188880f715c1` | His first-ever online class |
| E2 | AR | `6a351c23935e6818846d8a01` | مهارة، لا كومة منتجات |
| E2 | EN | `6a351d371a0de47002453d8e` | Skill, not a pile of products |
| E3 | AR | `6a351ddfad5312f0a733044c` | ماذا ستتعلّم، درساً بدرس |
| E3 | EN | `6a351e281a0de47002453e61` | What 20 lessons cover |
| E4 | AR | `6a351e6da4d6188880f71a10` | الدرس الأول، مجاناً |
| E4 | EN | `6a351ea51a0de47002453fe0` | Start free: The Talent |
| E5 | AR | `6a351ee4a4d6188880f71d17` | يعلّمك بنفسه، خطوة بخطوة |
| E5 | EN | `6a351f19ad5312f0a73309b5` | He teaches it himself |
| E6 | AR | `6a351f5a3801489584a5e43e` | إطلالة تصنعها بنفسك، لأي مناسبة |
| E6 | EN | `6a351f8c935e6818846d938e` | A look you do yourself |
| E7 | AR | `6a35205bcf9da6d8f0db021c` | الصف كاملاً، باشتراك واحد |
| E7 | EN | `6a35208e1a0de470024546ae` | Unlock the full Masterclass |

The committed HTML at `outputs/2026-06-bassam-fattouh-makeup/email-7step/bassam-fattouh/` (e1.ar.html to
e7.en.html) stays the source of truth; these Ortto drafts are the derived, editable copies.

## The owner is already in the editor (human-gate signal)

As of this sync, E1 AR, E1 EN, and E3 AR show `edited_by: Ahmed ElSanhoury` (the account owner opened
them in the Ortto editor; E1 AR and E1 EN also have a rendered screenshot). That is review activity, not
sign-off. The campaign-level approval is still an attributable, recorded act, never inferred from an edit
or from silence.

## Validation (the corrected build, proven end to end)

E1 AR was the reference: updated to the corrected build and validated in Ortto. The cross-sell cards
import as real portrait images (BeeFree keeps a standard `<img>`; it dropped the old background-image
overlay), and the unsubscribe link is the valid token `{{ urls.unsubscribe }}` (the `update_asset_mail`
Liquid validator accepted it). Every one of the 14 was staged to that identical, send-correct build.

## Cleanup before wiring the journey (Ortto UI; the MCP cannot delete)

Old pre-enrichment Bassam drafts from 2026-06-18 are still in the account and must not be attached to the
journey. Delete the 10 stale makeup drafts so the journey attaches only the enriched set:

- 8 named `Maharat - Bassam Makeup - E<1 to 4> <AR/EN> (draft)`: ids `6a33ec3f6aa307d819c4e8fd`,
  `6a33ec826aa307d819c4edcf`, `6a33ecc6f1781ca722f64072`, `6a33ed056aa307d819c4f551`,
  `6a33ed4a3e7e3880e1c66761`, `6a33ed8ac569b337404136d2`, `6a33edd0f1781ca722f64808`,
  `6a33ee13f1781ca722f648d2`.
- 2 named `Maharat - Bassam Makeup 7-step - E<1/2> AR (draft)`: ids `6a33ef0758c54fad446d07fd`,
  `6a33ef54f1781ca722f650cd`.

Separately, 5 stale `Maharat - Bassam Bridal 7-step` drafts from 2026-06-18 exist (ids
`6a33ef00ef0ae003f43ad298`, `6a33ef563e7e3880e1c677dd`, `6a33ef6b3e7e3880e1c678fb`,
`6a33ef66ef0ae003f43ad4a7`, `6a33ef76f1781ca722f65221`). Those belong to the bridal class, not this
makeup send. Leave them for the bridal campaign, or delete them too if clearing all old Bassam copy.

## Send-time wiring (Ortto UI)

- Stage the header (`BF_CLASSCOVER_LEFTRIGHTGRADIENT`) and the 3 card portraits from CloudFront to the
  Ortto CDN before send (CloudFront renders but is not the approved email host).
- Confirm the footer unsubscribe resolves (the `{{ urls.unsubscribe }}` token, or set Ortto's native
  unsubscribe link in the editor).
- Build the audience, then the journey, attach these 14 drafts per step and language, and start Tuesday.

The audience build-card (one-click target) is in `_TARGETING-watched-first-chapter.md`. The journey, the
Tuesday 2026-06-23 schedule, the language split, and suppression are in `_SEND-SETUP-bassam.md`.
