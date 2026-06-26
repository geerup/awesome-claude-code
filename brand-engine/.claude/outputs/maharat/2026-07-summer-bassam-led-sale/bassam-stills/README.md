# Summer of Skills, branded landscape banners (P001)

Branded, copy-overlaid landscape banners (web and promo use) built from the uploaded P001
still set for the `2026-07-summer-bassam-led-sale` campaign. Each frame is a real masterclass
still of a Maharat instructor with the brand treatment baked on: emerald eyebrow, white
headline, white Maharat wordmark, and (on confirmed-public instructors only) a name and skill
line, over a near-black bottom scrim.

House style on this file: no em dash, Western numerals only.

## What is in this folder

| Path | Contents |
|---|---|
| `originals/` | The 9 stills as delivered (jpg, JPG, webp, tif). Source of truth, untouched. |
| `branded/` | The 18 finished banners: `{01..09}.ar.jpg` and `{01..09}.en.jpg`, 1200 x 630. |
| `overlay-copy.json` | Per-frame copy, alt text, author, named/campaign kind, and per-frame scrim. The render source of truth. |
| `make_overlays.py` | The renderer. Re-run to rebuild every overlay from the originals + copy. |
| `work/normalized/` | EXIF-corrected, web-safe full-size conversions (the tif and webp normalized to jpg). |
| `work/preview/` | Downscaled previews of the originals. |
| `work/copy.ar.json`, `work/copy.en.json` | The QA-passed copywriter output (merged into `overlay-copy.json`). |
| `work/contact-sheet.jpg` | All 18 overlays on one sheet for review (AR left, EN right). |

## The 9 frames

| # | Kind | Author (status) | AR headline | EN headline |
|---|---|---|---|---|
| 01 | named | Ragheb Alama (confirmed public) | تعلّم الموسيقى من صانعها | Your music journey starts here. |
| 02 | campaign | held, name-free | تعلّم من نخبة العرب | Learn from the Arab world's best. |
| 03 | campaign | held, name-free | ابدأ مهارتك هذا الصيف | One subscription. Every masterclass. |
| 04 | named | Bassam Fattouh (confirmed public) | أتقني تقنيات المكياج بنفسك | Build the skill behind every look. |
| 05 | campaign | held, name-free | المكتبة كاملة باشتراك واحد | Your skills, your pace, your summer. |
| 06 | named | Ragheb Alama (confirmed public) | الأداء فنّ، أتقنه من رائد | Step into music and performance. |
| 07 | campaign | held, name-free | مهارة تبنيها بنفسك | Build something that lasts. |
| 08 | named | Bassam Fattouh (confirmed public) | اصنعي أي إطلالة بثقة | Create any look. Own the technique. |
| 09 | campaign | likely Toufic Kreidieh, name-free pending clearance | مهارة تبقى معك | The whole library is open. |

Named-frame name lines (baked verbatim from approved phrasings):
- Bassam: `بسام فتّوح، يعلّم المكياج` / `Bassam Fattouh, Teaches Makeup`
- Ragheb: `راغب علامة، يعلّم الموسيقى والأداء` / `Ragheb Alama, Teaches Music and Performance`

The eyebrow `صيف المهارات` / `Summer of Skills` repeats on every frame as the campaign kicker
(by design). AR and EN headlines are each optimized in their own language (not literal
translations), so each language reads naturally on its own banner.

## Design treatment

- Canvas 1200 x 630 (1.91:1 web/promo landscape banner). Cover-fit from the 1920 x 1080 source, minimal top/bottom crop, faces preserved.
- Colors: near-black scrim `#141414`, emerald eyebrow `#009975`, white headline/wordmark `#FFFFFF`, name line `#E5E5E5`.
- Type: AR headline Lyon Arabic Display Black, AR eyebrow/name 29LT Azer; EN Acumin Pro Bold / Regular. Arabic is natively shaped (RTL, letter joining, bidi) via Pillow + raqm.
- Layout: bottom-anchored copy block, right-aligned (AR) or left-aligned (EN); wordmark top-right (AR) or top-left (EN). Bottom gradient scrim plus a faint top scrim for wordmark legibility. Frames 07 and 09 carry a denser scrim (lighter backgrounds).
- Reproduce: `python3 make_overlays.py` (all) or `python3 make_overlays.py 04 ar` (one).

## Quality gates (all passed)

- `arabic-copy-qa` (copywriter-ar self-check): PASS. No em dash, no tatweel/kashida, Western numerals, empowering, RTL-safe.
- `english-copy-qa` (copywriter-en self-check): PASS. No em dash, Western numerals, empowering, one clear idea.
- `design-qa`: PASS. No hard-stop fixes. Two advisories on 07 and 09 background contrast, addressed with a stronger scrim.
- `brand-qa-reviewer`: PASS. Named-instructor guardrail satisfied (only Bassam and Ragheb named; all 5 campaign frames name-free), visual constants clean, gender address correct, no invented titles, no accreditation implication.

## Use, and a note on email

These are standalone branded landscape banners for web and promo placements (link previews,
social and web banners, landing-page headers). Baked copy is the right treatment for this use,
and the engine's text-free rule does not apply here because these are not email images.

- The 7-email templates were left untouched (requested): these banners are not wired into any email.
- If a banner is ever repurposed as an email header, two engine rules then apply: email images
  must be text-free with the headline as a live HTML copy slot (`context/email-design-system.md`,
  `context/instructors/_EMAIL-IMAGE-MANIFEST.md`), and the image must sit on the approved Ortto
  CDN (`m.autopilotapp.com`). In that case use a text-free still and place the copy as live HTML.

## Open items for the human gate

1. Identity confirmation. Named frames (Bassam 04/08, Ragheb 01/06) are confirmed public. Held
   faces need confirmation before any named version: 02/05 (a bearded man, possibly Kosai
   Khauli), 03/07 (a woman, possibly Rahma Riad), and 09 (likely Toufic Kreidieh). Each also
   needs a public-naming clearance check, none is cleared in-repo today.
2. Email use is out of scope by design. If a banner is later wanted as an email header, use a
   text-free version with live HTML copy and stage it to the Ortto CDN (see the note above).
3. Email templates unchanged. The de-duplication of the live email image set was not done
   (requested to skip); these banners stand alone as web/promo assets.
4. Nothing here sends or spends. Approval is Ahmed's, at the campaign level.
