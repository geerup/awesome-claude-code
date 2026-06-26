# context/instructors: the confirmed-instructor facts registry

Internal source of truth for instructor facts. One folder per instructor. This is the place the
copywriters, creative-director, and the class-trailer and credibility templates pull real,
sourced facts from, instead of inventing them. It is internal. Nothing here is customer-facing
on its own.

## Why this exists

Two hard rules drive it:
- Do not name instructors publicly without confirmation.
- Do not invent instructor credentials, awards, figures, or class lineups.

A profile here records only facts with a traceable source, tags each with that source, and
marks whether public naming is cleared. When a fact is not sourced, it is an OPEN ITEM, not a
guess.

## Folder shape

```
context/instructors/
  README.md                      this file
  _TEMPLATE-instructor-profile.md  the profile template
  <instructor-slug>/
    profile.md                   the confirmed facts, provenance-tagged
    (optional) assets.md         references to rights-cleared imagery and footage
```

## Confirmation status legend

- public_naming_cleared: yes only when the instructor is named on a published Maharat course
  page, or otherwise confirmed by Ahmed. A name appearing only in an internal doc is "to
  confirm", not cleared.
- Each credibility fact (award, title, figure) carries its source. Facts whose only source is
  the internal organic copy doc are marked "verify against the published course page or
  Ahmed before public use". They are usable internally, not yet cleared for a live claim.

## How agents use it

- copywriter-ar and copywriter-en: name an instructor in customer-facing copy only when
  public_naming_cleared is yes. Use only facts marked cleared. Never add a credential not in
  the profile.
- creative-director and designer: fill the class-trailer authority and credibility stacks
  (`skills/03-creative-production/creative-concepting/templates/class-trailer-structure.md`)
  only from cleared facts here. Portraits and footage must be real rights-cleared assets, never
  generated.
- brand-qa-reviewer: fail any customer-facing asset that names an instructor not cleared here,
  or that states a credential not in the profile.

## Clearance log

- 2026-06-05: Bassam Fattouh, public naming cleared via published Maharat course pages.
- 2026-06-05: Elda Choucair, Toufic Kreidieh, Rahma Riad, Ragheb Alama, Salam Dakkak, Cedric
  Haddad, Kosai Khauli, public naming cleared by Ahmed sign-off (hostmaster@maharat.com). All
  8 instructors are now cleared for public naming.
- 2026-06-05: course pages confirmed. The crawl reference
  `references/2026-06-maharat-instructor-products/` verified 9 class products across the 8
  instructors at HTTP 200 (Bassam Fattouh has 2: makeup and bridal makeup). Each profile now
  carries the confirmed title and the EN and AR `/class/` URLs, and the naming basis is
  upgraded from sign-off to published-page provenance. Note: Elda Choucair's `/class/` page is
  live but not linked in site nav. Credibility figures for Elda Choucair and Toufic Kreidieh
  remain verify-before-public-use until checked against a real source; names are cleared, those
  specific stats are not.
- 2026-06-16: instructor image catalog built. Added `_IMAGE-CATALOG.md` (central approved-image
  registry) and `_IMAGE-FOLDER-MAP.md` (slug to Drive photography-folder map, matched by folder
  name, not the NN prefix). Bassam Fattouh executed end to end: his `05 - PHOTOGRAPHY / RETOUCHED`
  tree (16 images including the `ON BLACK` subfolder) enumerated live via the Drive MCP and written
  to the catalog and `bassam-fattouh/assets.md`, prefer-retouched dedup applied. The other 8
  instructors with Drive folders are seeded "pending enumeration" (folder ids known). sami-al-jaber
  and mo-islam have no Drive folder, recorded as no imagery. Generated likenesses never get a
  catalog row, so resolving a "REAL ASSET REQUIRED" slot from the catalog cannot return one.
  rights_status per image is `confirm with Ahmed` (approved vs internal-only is a human call), and
  faces_present and orientation are `auto, verify` (the Drive vision read returned empty this
  session). The Google Drive MCP server is NOT adopted in settings.json: that is a build-vs-buy plus
  Ahmed decision, flagged in the catalog header.
- 2026-06-16: image catalog completed for all remaining instructors (Tier 2). Enumerated each
  photography tree live via the Drive MCP and wrote the rows plus a per-instructor `assets.md`,
  prefer-retouched dedup applied, all passing `image_catalog_check.py all` (384 rows, 350 stem
  groups, one preferred each). Counts: ragheb-alama 10, salam-dakkak 18, kosai-khauli 18,
  rahma-riad 20, toufic-kredieh 10, cedric-haddad 5, elda-choucair 7, mona-ataya 202,
  bassam-fattouh-bridal 78. Each profile Assets line now binds to its `assets.md` and the catalog.
  Notable cases flagged for Ahmed: Mona Ataya has NO retouched set (her 02 - PHOTOGRAPHY holds only
  CR3 camera-raw HIGHRES, excluded as non-image, plus 195 LOWRES jpg selects, retouched=no, the only
  catalogable source, so her hero comes from LOWRES). Cedric Haddad's RETOUCHED holds only ROMARIO
  (clean) and FACEAPP (AI face-edited) subfolders; the FACEAPP AI-edited variants are deliberately
  excluded from the registry (real photography only, no AI likeness), so only the 5 clean ROMARIO
  frames are catalogued. The bridal class (bassam-fattouh-bridal) has no photography folder, so its
  source is `05 - BANK OF STILLS` (video stills, image_type class-still, not studio portraits).
  rights_status per image remains `confirm with Ahmed`; faces_present and orientation are
  `auto, verify` (the Drive `read_file_content` vision read returned empty again this session). The
  Google Drive MCP server is still NOT adopted in settings.json (unchanged, build-vs-buy plus Ahmed).
- 2026-06-05: topic lists reconciled. Pulled the live class-page content from the crawl
  reference for the 7 non-Bassam instructors and recorded the confirmed chapter lists,
  descriptions, and page-sourced credibility lines, each marked cleared. Where the live page
  confirmed an internal-doc claim it was promoted to cleared (Toufic billion-dollar from
  scratch, Rahma digital empire millions, Ragheb 40 years, Salam Best Female Chef in MENA and
  Michelin restaurant Bait Maryam, Cedric celebrity stylist, Kosai one of the biggest names,
  Elda decades and respected leader). Claims on the internal doc only and absent from the page
  stay flagged (Elda Omnicom, Forbes, Cannes, 900+, 1000+; Toufic Brands For Less name and the
  $10,000 garage detail). Salam page heading reads "Levantine Home Cooking" while the slug is
  levantine-cooking.

## Hard rules

- No invented facts, awards, figures, titles, or lineups. Source or OPEN ITEM.
- Never imply a certificate or class is accredited.
- No em dashes, no tatweel, Western numerals only.
- Provenance on every fact. If the source is the internal doc, say so and mark it to confirm.
