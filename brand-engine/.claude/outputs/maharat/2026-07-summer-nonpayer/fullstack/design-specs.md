# Design Specs: Summer of Skills, full-stack non-payer campaign

## Envelope

- campaign_id: 2026-07-summer-nonpayer
- produced_by: designer
- stream: 3 creative production (execution + design-qa)
- status: draft
- qa:
  - skill_eval: pass (structure, slot labeling, no Arabic baked in, brand constants applied,
    safe areas present, RTL marked, no em dashes, no tatweel, Western numerals only,
    no invented values, open items surfaced, copy variant ids bound)
  - arabic_qa: na (no Arabic authored in this stream; all ar slots empty, routed to
    copywriter-ar; Arabic copy-package variant ids bound to slots from copy-package.ar.md)
  - english_qa: na (no English copy authored in this stream; all en slots empty, routed to
    copywriter-en; English copy-package variant ids bound to slots from copy-package.en.md)
  - design_qa: pass (see verdict section at end of this document; six checks pass;
    final human design check remains before any build or publish)
  - brand_qa: pending (routes to brand-qa-reviewer after design-qa pass)
- open_items:
  - OI-1: Approved, rights-cleared instructor photography for each of the seven nameable
    instructors (Ragheb Alama, Salam Dakkak, Kosai Khauli, Bassam Fattouh, Toufic Kreidieh,
    Cedric Haddad, Elda Choucair). OPEN per instructor. DS3 (C3 per-field portrait) is
    build-blocked per instructor until confirmed. The campaign runs on DS1 (C1 hero grid),
    DS2 (C2 per-field abstract), DS4 (C4 abstract free-entry), DS5 (C5 breadth grid),
    DS7 (C7 thematic still), and DS6 (email and push crops from DS4 and DS7 sources)
    until each instructor's assets are confirmed. Surface at human gate, per instructor.
  - OI-2: Rights-cleared class footage from at least three instructor fields. OPEN. DS8
    (C6 multi-field breadth reel) is build-blocked until confirmed. If fewer than three
    fields are available, DS8 is blocked and DS4 motion runs as fallback. Surface at gate.
  - OI-3: BLOTATO_API_KEY credential. OPEN. DS8 repurpose cuts (15-second and 6-second)
    are cut manually until resolved. Not a blocker for the DS8 master cut spec itself.
  - OI-4: Per-instructor public-naming confirmation (confirm-at-gate for each of the seven).
    Profiles carry public_naming_cleared: yes with sign-off on file (2026-06-05) but the
    catalog public_status column still reads unconfirmed. Every overlay slot that references
    an instructor name is a confirm-at-gate item. If a name is not cleared at the gate,
    that slot drops to the unnamed breadth descriptor and is noted without rewriting the spec.
  - OI-5: Verify-before-public-use facts. Toufic Kreidieh's Brands For Less name and the
    $10,000-garage detail are excluded from all slots. Elda Choucair's Omnicom, Forbes,
    Cannes, and the 900-plus and 1000-plus figures are excluded from all slots. Only cleared,
    page-sourced credentials are used in overlay slots for these two instructors.
  - OI-6: Price and promotion. ASSUMPTION. No price chip slot in any spec. If Ahmed confirms
    a promo, a price-chip overlay slot must be added to the relevant specs and re-routed to
    both copywriters before build proceeds.
  - OI-7: Confirmed platform typeface. The confirmed Maharat platform typeface must be used
    at build time. If not confirmed before build, flag as a build-gate item. Do not substitute
    an unapproved font.
  - OI-8: App push platform. OPEN ITEM. DS6 push companion still (AB5 format) is specced to
    a safe base size; lifecycle-architect confirms the final push image spec once the platform
    is named. Build of the push-specific crop is gated until confirmed.
  - OI-9: Budget, schedule, gate and push platforms. OPEN ITEM from strategy-artifact.
    Carried forward. No absolute numbers, no spend, no send until confirmed.
  - OI-10: Saudi PDPL and data residency. OPEN ITEM. Compliance-privacy-reviewer runs on
    every data-touching asset downstream.
  - OI-11: Four non-nameable instructors (Rahma Riad, Sami Al Jaber, Mona Ataya, Mo Islam).
    Never named. Appear only inside the unnamed breadth descriptor in overlay slots where
    copywriters have written "and more" or "والمزيد عبر مجالات عديدة". Confirmed across all specs.
- brief_refs: campaign_id, creative_direction, channel_routing, channels, dimensions per
  placement (Meta and IG feed and story, TikTok, Google, YouTube, organic, email header,
  app push, landing hero), asset_briefs AB1 through AB9 from creative-package.md, concepts
  C1 through C7 from creative-package.md, copy variant ids from copy-package.ar.md and
  copy-package.en.md (AD-BREADTH-1 through AD-RETARGET-1, EMAIL-E1 through EMAIL-E5,
  SOCIAL-S1 through SOCIAL-S8, PUSH-P1 through PUSH-P5, LP-HEADLINE-1 and LP-HEADLINE-2,
  LP-SUBHEAD-1 and LP-SUBHEAD-2, LP-CTA-1 and LP-CTA-2)
- grounding_refs: CLAUDE.md; context/brand-voice.md;
  outputs/2026-07-summer-nonpayer/fullstack/strategy-artifact.md;
  outputs/2026-07-summer-nonpayer/fullstack/creative-package.md;
  outputs/2026-07-summer-nonpayer/fullstack/copy-package.ar.md;
  outputs/2026-07-summer-nonpayer/fullstack/copy-package.en.md;
  runtime/handoff-contract.md;
  skills/03-creative-production/SKILL.md;
  outputs/2026-06-bassam-fattouh-makeup/fullstack/design-specs.md (exemplar)

---

## Global design tokens (apply to every spec below)

| Token | Value | Usage |
|---|---|---|
| bg | #141414 | All background fills. Every canvas starts here. |
| surface | #1A1A1A | Card and panel surfaces. Elevated, not flooded. |
| accent | #009975 | Emerald. Accent bars, stripes, CTA chip fills, icon lines, progress marks. Used as a highlight, never the dominant color in any frame. |
| type-primary | #FFFFFF | Headlines and primary copy on overlays. |
| type-secondary | #D4D4D4 | Supporting lines, field chips, secondary overlay copy. |
| type-muted | #888888 | Tertiary labels, metadata, fine print. |

Numerals: Western only (0 through 9). No Eastern Arabic numerals anywhere in any rendered
layer or spec reference.

RTL: All Arabic overlay text layers are set right-to-left. Text anchors for ar slots are
right-aligned and pinned to the right safe-area boundary. Each language occupies its own
named slot. Mixed AR and EN is never combined within a single slot.

No Arabic text of any kind is baked into any generated image or motion export. All copy
arrives as a human-placed overlay from QA-passed copywriter-ar and copywriter-en output.

Build tool default: Canva (primary) unless otherwise noted. Figma is an acceptable
alternative for any spec at the same dimensions; it has not been formally adopted and runs
through build-vs-buy-eval before live adoption.

---

## DS1. Platform breadth hero grid, static (C1, source AB1, Prompts P1 and P2)

Concept: C1 "Many Fields, One Summer". No photography dependency. Ready to spec.

### Gate status

Ready to build after design-qa and brand-qa pass. No blocked open items for this spec.

### Formats and canvas dimensions

| Format ID | Dimensions (px) | Aspect | Primary use |
|---|---|---|---|
| DS1-A | 1080 x 1350 | 4:5 | Meta and IG feed primary, paid prospecting |
| DS1-B | 1080 x 1920 | 9:16 | IG Story and Reels cover |
| DS1-C | 1200 x 628 | 1.91:1 | Meta feed ad, news feed placement |
| DS1-D | 1080 x 1080 | 1:1 | Square feed, optional |
| DS1-E | 1920 x 1080 | 16:9 | YouTube channel art, landing hero source (AB9 also draws from P2) |

### Export settings

All formats: PNG at 72 dpi for digital delivery. JPEG at 90% quality as fallback. No
watermark. No bleed. Pixel dimensions as specified.

### Grid (DS1-A reference: 1080 x 1350)

- Canvas: 1080 x 1350, #141414 fill.
- Outer margin: 48px all sides.
- Gutter between cards: 16px.
- Inner canvas for grid: 984 x 1254px, origin at (48, 48).
- Card arrangement: 7 cards in an asymmetric mosaic. Reference layout below.
  Designer may refine within the safe-area constraints while maintaining the mosaic intent.

Reference mosaic (DS1-A, approximate card positions, back to front, all cards #1A1A1A):
- Card A (wide, upper left): X 48, Y 48, W 600, H 380. No accent.
- Card B (narrow, upper right): X 664, Y 48, W 368, H 380. No accent.
- Card C (mid-left, focal card): X 48, Y 444, W 392, H 440. Carries the 4px emerald
  left-border stripe (#009975, full card height, left edge of card). This is the visual
  focal point.
- Card D (mid-right tall): X 456, Y 444, W 576, H 440. No accent.
- Card E (lower left small): X 48, Y 900, W 276, H 402. No accent.
- Card F (lower center): X 340, Y 900, W 384, H 402. No accent.
- Card G (lower right): X 740, Y 900, W 292, H 402. No accent.
- Background field: pure #141414, visible in all gutters and outer margins.
- Card interiors: all empty flat #1A1A1A. No icon, no text baked in.
- Corner radius on all cards: 8px.

Safe areas (DS1-A):
- Top overlay zone: Y 0 to 160. Reserved for [ar headline] and [en headline] overlay.
- Card mosaic zone: Y 160 to 1190. The visual composition. No copy overlaid inside cards.
- Lower overlay zone: Y 1190 to 1300. Reserved for [ar subline] and [en subline] overlay.
- CTA zone: Y 1300 to 1350. Reserved for [ar cta chip] and [en cta chip] overlay.
- Left and right text margin: 80px from canvas edge inside any overlay zone.

Scale for DS1-B (1080 x 1920):
- Top overlay zone: Y 0 to 200.
- Lower overlay zone: Y 1680 to 1840.
- CTA zone: Y 1840 to 1920.
- Card mosaic zone: Y 200 to 1680. Cards reflow to fill the taller canvas, maintaining
  mosaic rhythm. 7 cards across two rows plus a third partial row.

Scale for DS1-C (1200 x 628):
- Top overlay zone: Y 0 to 100.
- Lower overlay zone: Y 490 to 580.
- CTA zone: Y 580 to 628.
- Card mosaic zone: Y 100 to 490. Cards reflow to a horizontal single-row or two-row layout.

Scale for DS1-D (1080 x 1080):
- Top overlay zone: Y 0 to 140.
- Lower overlay zone: Y 900 to 1020.
- CTA zone: Y 1020 to 1080.
- Card mosaic zone: Y 140 to 900.

Scale for DS1-E (1920 x 1080, Prompt P2 layout, landing hero source):
- Left overlay zone: X 0 to 240. Reserved for [ar landing hero headline] (RTL, right-reading
  from center outward) and [en landing hero headline]. In RTL web layout, AR headline anchors
  right; in LTR web layout, EN headline anchors left. Web-design-director resolves layout.
- Card mosaic zone: X 240 to 1680. Horizontal mosaic.
- Right overlay zone: X 1680 to 1920. Safe clearance.
- Top: 100px clearance from edge for UI.
- Bottom: 120px reserved for CTA button placement (web-design-director owns this zone).

### Layer structure (DS1-A, back to front)

1. Background fill: #141414, full canvas. Locked.
2. Cards A through G: #1A1A1A rectangles per positions above. Corner radius 8px. All interiors
   empty flat #1A1A1A. No text, no icon, no image inside any card.
3. Focal card accent stripe (Card C only): #009975 rectangle, 4px wide, full card height,
   flush with left edge of Card C. This is the sole accent element in the generated layer.
4. [ar headline] slot: empty. Type: 36 to 44px, semibold, #FFFFFF. RTL. Right-anchored at
   X 1000 (80px from right edge). Y 56 baseline within top overlay zone. Labeled for
   copywriter-ar fill. Copy variant binding: AD-BREADTH-1 headline (ar) for paid variants;
   LP-HEADLINE-1 or LP-HEADLINE-2 (ar equivalent from copy-package.ar.md: LP-HEADLINE-1)
   for the landing hero variant.
5. [en headline] slot: empty. Same size and weight as ar headline. LTR. Left-anchored at
   X 80. Y 56 baseline. Labeled for copywriter-en fill. Copy variant binding: AD-BREADTH-1
   headline (en) for paid; LP-HEADLINE-1 (en) for landing hero.
6. [ar subline] slot: empty. Type: 18 to 22px, regular, #D4D4D4. RTL. Right-anchored at
   X 1000. Y 1200 to 1270 within lower overlay zone. Labeled for copywriter-ar fill.
   Copy variant binding: AD-BREADTH-1 primary text (ar, secondary line) or SOCIAL-S1 (ar)
   depending on channel.
7. [en subline] slot: empty. Same size, LTR. Left-anchored X 80. Same Y range. Labeled for
   copywriter-en fill. Copy variant binding: AD-BREADTH-1 body (en, secondary) or SOCIAL-S1
   (en) depending on channel.
8. [ar cta chip] slot: empty. #009975 fill, #FFFFFF type, 12px corner radius, horizontal
   padding 20px, vertical padding 10px. RTL. Right-aligned in CTA zone at X 1000. Labeled
   for copywriter-ar fill. Copy variant binding: AD-BREADTH-1 cta (ar) / LP-CTA-1 (ar).
9. [en cta chip] slot: empty. Same style, LTR. Left-aligned at X 80 in CTA zone. Labeled
   for copywriter-en fill. Copy variant binding: AD-BREADTH-1 CTA (en) / LP-CTA-1 (en).
10. Maharat wordmark: small, top-right corner, 40px from top, 80px from right. #FFFFFF.
    Not competing with headline. Designer places the confirmed brand mark at build.

### Type scale (DS1-A reference)

| Role | Size | Weight | Color | Direction |
|---|---|---|---|---|
| AR headline | 36 to 44px | Semibold | #FFFFFF | RTL, right-anchored |
| EN headline | 36 to 44px | Semibold | #FFFFFF | LTR, left-anchored |
| AR subline | 18 to 22px | Regular | #D4D4D4 | RTL, right-anchored |
| EN subline | 18 to 22px | Regular | #D4D4D4 | LTR, left-anchored |
| CTA chip | 14px | Semibold | #FFFFFF | On #009975 fill, per direction |

Font: the confirmed Maharat platform typeface. If not confirmed at build time, flag as OI-7
and do not substitute an unapproved font.

---

## DS2. Per-field abstract card, paid prospecting (C2, source AB2, Prompt P3 base)

Concept: C2 "Your Field Is Here". Seven field variants plus an unnamed breadth variant.
No photography dependency. Each variant confirm-at-gate per instructor name in overlay slots.

### Gate status

Ready to build for the visual layer of all eight variants. Overlay slot population is
confirm-at-gate per instructor. The abstract visual layer does not depend on instructor assets.

### Variants

One base template, eight instances:

| Variant | Field | Instructor overlay (confirm-at-gate) | Icon shape |
|---|---|---|---|
| DS2-music | Music | Ragheb Alama, 40 years in the music industry | Smooth curved wave, single period of a clean sine wave, 2px line, #009975 |
| DS2-cook | Cooking | Salam Dakkak, Best Female Chef in MENA and owner of the Michelin award winning Bait Maryam | Rising arc with a dot above suggesting steam or a bowl profile, 2px line, #009975 |
| DS2-acting | Acting | Kosai Khauli, one of the biggest names in the Arab world in acting | Single downward light cone from above, 2px line, #009975 |
| DS2-makeup | Makeup | Bassam Fattouh, a leading most sought-after regional makeup artist | Single horizontal sweep arc suggesting a brush stroke, 2px line, #009975 |
| DS2-business | Business | Toufic Kreidieh, built a billion-dollar business from scratch (no Brands For Less, no garage detail) | Three ascending steps, 2px line, #009975 |
| DS2-styling | Styling | Cedric Haddad, celebrity stylist trusted by the Arab world's biggest stars | Single draped curve suggesting fabric, 2px line, #009975 |
| DS2-marketing | Marketing | Elda Choucair, one of the Arab world's most respected marketing leaders (no Omnicom, Forbes, Cannes, figures) | Clean radial node cluster, 2px open lines, #009975 |
| DS2-breadth | Breadth (unnamed) | No instructor name. "And more across many fields" breadth only. | Composite of three minimal arc segments at different heights, 2px lines, #009975, suggesting variety |

### Formats per variant

| Format ID | Dimensions (px) | Aspect | Primary use |
|---|---|---|---|
| DS2-[variant]-A | 1080 x 1080 | 1:1 | Square feed, Meta and IG primary |
| DS2-[variant]-B | 1080 x 1350 | 4:5 | Feed secondary |
| DS2-[variant]-C | 1080 x 1920 | 9:16 | IG Story and TikTok |

### Export settings

All formats: PNG at 72 dpi. JPEG at 90% fallback. No watermark. No text baked in.

### Grid (DS2-[variant]-A reference: 1080 x 1080)

- Canvas: 1080 x 1080, #141414.
- Card: #1A1A1A rectangle, 756px wide, 700px tall, centered at (540, 540).
  Corner radius 12px. Occupies approximately 70% of frame width, 65% of frame height.
- Card interior padding: 40px all sides. Inner content area: 676 x 620px.
- Icon zone: upper two-thirds of card interior (Y 40 to 453 within the card interior,
  relative to card top). Icon centered horizontally within the card.
- Lower copy zone: lower third of card interior (Y 453 to 620 within the card interior).
  Reserved for overlay copy. Empty flat #1A1A1A.
- Bottom accent bar: #009975 rectangle, full card width, 4px tall, flush with the bottom
  edge of the card. This is the brand anchor. The bar is part of the generated layer.

Safe areas (DS2-[variant]-A: 1080 x 1080):
- Top overlay zone: Y 0 to 140. Reserved for [ar field headline] and [en field headline].
- Card zone: Y 140 to 940. The card occupies this area centered.
- Lower overlay zone (outside card): Y 940 to 1010. Reserved for [ar cta chip] and [en cta chip].
- Left and right text margin inside overlay zones: 80px.
- Inside the card, the lower copy zone (Y 453 to 620 relative to card) carries:
  - [ar instructor name and credential]: lower zone within card, RTL.
  - [en instructor name and credential]: lower zone within card, LTR.
  - [ar free chapter callout]: below credential, smaller, RTL.
  - [en free chapter callout]: below credential, smaller, LTR.

Scale for DS2-[variant]-B (1080 x 1350):
- Top overlay zone: Y 0 to 140.
- Card zone: Y 140 to 1160, centered.
- Lower overlay zone: Y 1160 to 1280.
- CTA zone: Y 1280 to 1350.

Scale for DS2-[variant]-C (1080 x 1920):
- Top overlay zone: Y 0 to 160.
- Card zone: Y 160 to 1700, centered vertically within this band.
- Lower overlay zone: Y 1700 to 1840.
- CTA zone: Y 1840 to 1920.

### Layer structure (DS2-[variant]-A, back to front)

1. Background fill: #141414, full canvas. Locked.
2. Card surface: #1A1A1A rectangle, 756 x 700px, centered, corner radius 12px. Empty interior.
3. Abstract icon: per-field single-line abstract shape in #009975, 2px stroke, open line shape,
   no fill, centered in the upper two-thirds of the card interior. The icon shape is the only
   element that changes between variants. It must not touch the lower copy zone.
4. Bottom accent bar: #009975 rectangle, 756px wide, 4px tall, flush with card bottom edge.
5. [ar field headline] slot: empty. Type: 28 to 34px, semibold, #FFFFFF. RTL. Right-anchored
   at X 1000. Positioned in top overlay zone, Y 60 baseline. Labeled for copywriter-ar fill.
   Copy variant bindings (per variant): DS2-music binds AD-MUSIC-1 headline (ar);
   DS2-cook binds AD-COOK-1 headline (ar); DS2-acting binds AD-ACTING-1 headline (ar);
   DS2-makeup binds AD-MAKEUP-1 headline (ar); DS2-business binds AD-BUSINESS-1 headline (ar);
   DS2-styling binds no paid variant (organic only, see SOCIAL-S6 ar); DS2-marketing binds no
   paid variant (organic only, see SOCIAL-S7 ar); DS2-breadth binds AD-BREADTH-1 headline (ar).
6. [en field headline] slot: empty. Same size, LTR. Left-anchored X 80. Same Y. Labeled for
   copywriter-en fill. Bindings mirror the ar bindings using the en copy variants.
7. [ar instructor name and credential] slot: empty. Type: 18 to 22px, regular then semibold
   for the name, #D4D4D4 for credential, #FFFFFF for name. RTL. Right-anchored at X within
   card right edge minus 40px, within lower copy zone of card. Labeled for copywriter-ar fill.
   NOTE: confirm-at-gate per instructor. Verify-before-public-use restriction noted:
   Toufic Kreidieh (Brands For Less and $10,000-garage detail excluded),
   Elda Choucair (Omnicom, Forbes, Cannes, figures excluded).
   DS2-breadth: this slot reads "and more across many fields" (en) and the ar equivalent;
   no instructor name appears.
8. [en instructor name and credential] slot: empty. Same spec, LTR. Left-anchored within
   card left edge plus 40px. Same restrictions. Labeled for copywriter-en fill.
9. [ar free chapter callout] slot: empty. Type: 14 to 16px, regular, #D4D4D4. RTL.
   Right-anchored below the credential slot, 16px gap. Labeled for copywriter-ar fill.
   Copy variant binding (if present in copy-package.ar.md): the "ابدأ بالدرس الأول مجاناً" line
   from the relevant per-field ad primary text (e.g., AD-MUSIC-1 last line for DS2-music).
10. [en free chapter callout] slot: empty. Same size, LTR. Left-anchored. Same gap.
    Labeled for copywriter-en fill.
11. [ar cta chip] slot: empty. #009975 fill, #FFFFFF type, 12px corner radius, padding
    20px horizontal 10px vertical. RTL. Right-aligned in lower overlay zone. Labeled for
    copywriter-ar fill. Copy variant binding: AD-MUSIC-1 cta (ar) "ابدأ مجاناً" for DS2-music,
    matching per-field cta for each variant, AD-BREADTH-1 cta for DS2-breadth.
12. [en cta chip] slot: empty. Same style, LTR. Left-aligned. Labeled for copywriter-en fill.
    Copy variant binding: per-field "Start the free lesson" (en) for each variant.
13. Maharat wordmark: small, top-right corner, 32px from top, 80px from right. #FFFFFF.

### Type scale (DS2-[variant]-A reference)

| Role | Size | Weight | Color | Direction |
|---|---|---|---|---|
| AR field headline | 28 to 34px | Semibold | #FFFFFF | RTL |
| EN field headline | 28 to 34px | Semibold | #FFFFFF | LTR |
| AR instructor name | 18 to 22px | Semibold | #FFFFFF | RTL inside card |
| EN instructor name | 18 to 22px | Semibold | #FFFFFF | LTR inside card |
| AR credential | 16 to 18px | Regular | #D4D4D4 | RTL inside card |
| EN credential | 16 to 18px | Regular | #D4D4D4 | LTR inside card |
| AR free chapter callout | 14 to 16px | Regular | #D4D4D4 | RTL |
| EN free chapter callout | 14 to 16px | Regular | #D4D4D4 | LTR |
| CTA chip | 14px | Semibold | #FFFFFF | On #009975 fill |

---

## DS3. Per-field instructor portrait (C3, source AB3, photography-dependent)

Concept: C3 "The Standard". Build-blocked per instructor until approved, rights-cleared
photography or class still is confirmed for that instructor. Fallback for each: DS2 variant
for the same field.

### Gate status

BLOCKED per instructor. OI-1 must be resolved (rights-cleared photography confirmed)
before any instance is executed in build. The spec is complete; the build action is gated
per instructor. Fallback for all seven: the corresponding DS2 variant.

### Formats per instructor (when asset confirmed)

| Format ID | Dimensions (px) | Aspect | Primary use |
|---|---|---|---|
| DS3-[instructor]-A | 1080 x 1350 | 4:5 | IG feed, Meta feed |
| DS3-[instructor]-B | 1080 x 1920 | 9:16 | Story and Reels cover |
| DS3-[instructor]-C | 1200 x 628 | 1.91:1 | Meta feed ad |
| DS3-[instructor]-D | 1080 x 1080 | 1:1 | Square feed |

### Export settings

PNG at 72 dpi. JPEG at 90% fallback. No heavy color grading that alters skin tone or
clothing. No watermark.

### Grid (DS3-[instructor]-A reference: 1080 x 1350)

- Canvas: 1080 x 1350, #141414.
- Portrait placement: centered or two-thirds dominant, with a slight right-column bias on
  AR builds so the instructor's face reads correctly within the RTL framing direction. The
  designer determines exact placement once the approved asset is reviewed.
- Upper overlay zone: Y 0 to 150. [ar headline] and [en headline].
- Portrait zone: Y 150 to 1100. Rights-cleared instructor photograph or class still.
- Lower overlay zone: Y 1100 to 1280. [ar instructor name and field] and [en instructor name
  and field].
- Accent bar zone: Y 1280 to 1350. Emerald #009975 bar, full canvas width, 8px. [ar cta chip]
  and [en cta chip] float above or within this zone.
- Left and right text margin: 80px from canvas edge.

### Layer structure (DS3-[instructor]-A, back to front)

1. Background fill: #141414, full canvas. Locked.
2. Portrait asset: rights-cleared photograph or class still, placed in portrait zone.
   No generated likeness under any circumstances. No skin-tone shift, no fabric color
   alteration. Subtle vignette at edges only if required for field separation from the
   #141414 background, using #141414 at 60% opacity on a soft feathered edge layer.
3. Lower gradient wash: vertical gradient from transparent at Y 1050 to #141414 at 70%
   opacity at Y 1280. Ensures overlay legibility without obscuring the subject.
4. Emerald accent bar: #009975, full canvas width, 8px tall, Y 1272. Brand anchor.
5. [ar headline] slot: empty. Type: 36 to 44px, semibold, #FFFFFF. RTL. Right-anchored
   X 1000. Y 60 baseline in upper overlay zone. Labeled for copywriter-ar fill.
   Copy variant binding (per instructor): AD-MUSIC-1 headline (ar) for Ragheb Alama;
   AD-COOK-1 for Salam Dakkak; AD-ACTING-1 for Kosai Khauli; AD-MAKEUP-1 for Bassam Fattouh;
   AD-BUSINESS-1 for Toufic Kreidieh; SOCIAL-S6 (ar headline) for Cedric Haddad;
   SOCIAL-S7 (ar, single-instructor variant if Elda) for Elda Choucair.
6. [en headline] slot: empty. Same size, LTR. Left-anchored X 80. Y 60. Labeled for
   copywriter-en fill. Bindings mirror ar using en copy variants.
7. [ar instructor name and field] slot: empty. Type: 22 to 26px, semibold, #FFFFFF for
   name, 18px regular #D4D4D4 for field descriptor. RTL. Right-anchored X 1000, Y 1120
   baseline within lower overlay zone. Labeled for copywriter-ar fill.
   NOTE: confirm-at-gate per instructor. Verify-before-public-use restrictions apply to
   Toufic Kreidieh (Brands For Less and $10,000-garage detail excluded) and Elda Choucair
   (Omnicom, Forbes, Cannes, figures excluded). Only cleared, page-sourced credentials.
8. [en instructor name and field] slot: empty. Same spec, LTR. Left-anchored X 80. Y 1120.
   Same restrictions. Labeled for copywriter-en fill.
9. [ar cta chip] slot: empty. #009975 fill, #FFFFFF type, 12px corner radius, padding
   20px horizontal 10px vertical. RTL. Right-aligned, Y center of accent bar zone.
   Labeled for copywriter-ar fill. Copy variant binding: per-field cta (ar).
10. [en cta chip] slot: empty. Same style, LTR. Left-aligned, same Y. Labeled for
    copywriter-en fill.
11. Maharat wordmark: small, top-right corner, 40px from top, 80px from right. #FFFFFF.

Scale for DS3-[instructor]-B (1080 x 1920):
- Upper overlay zone: Y 0 to 200.
- Lower overlay zone: Y 1680 to 1850.
- Accent bar zone: Y 1850 to 1920.
- Portrait zone: Y 200 to 1680.

Scale for DS3-[instructor]-C (1200 x 628):
- Upper overlay zone: Y 0 to 100.
- Lower overlay zone: Y 470 to 580.
- Accent bar zone: Y 580 to 628.
- Left and right safe margin: 80px.

Scale for DS3-[instructor]-D (1080 x 1080):
- Upper overlay zone: Y 0 to 150.
- Lower overlay zone: Y 880 to 1020.
- Accent bar zone: Y 1020 to 1080.

### Type scale (DS3 reference, matches DS1 scale)

| Role | Size | Weight | Color | Direction |
|---|---|---|---|---|
| AR headline | 36 to 44px | Semibold | #FFFFFF | RTL |
| EN headline | 36 to 44px | Semibold | #FFFFFF | LTR |
| AR instructor name | 22 to 26px | Semibold | #FFFFFF | RTL |
| EN instructor name | 22 to 26px | Semibold | #FFFFFF | LTR |
| AR field descriptor | 18px | Regular | #D4D4D4 | RTL |
| EN field descriptor | 18px | Regular | #D4D4D4 | LTR |
| CTA chip | 14px | Semibold | #FFFFFF | On #009975 fill |

---

## DS4. Abstract free-entry re-engagement still and motion (C4, source AB4 and AB5, Prompts P4 and P7)

Concept: C4 "One Free Lesson". No photography dependency. Primary concept for owned
lifecycle flow. Also runs as organic re-engagement and secondary paid retargeting.

### Gate status

Ready to build. No blocked open items for this spec.

### Formats and canvas dimensions

| Format ID | Dimensions (px) | Asset type | Primary use |
|---|---|---|---|
| DS4-A | 1080 x 1350 | Still | IG feed (4:5), email header source |
| DS4-B | 1080 x 1920 | Still | Story, Reels cover |
| DS4-C | 1080 x 1920 | Motion, 7 to 10 seconds | Reels, TikTok, app push companion |
| DS4-D | 1080 x 1080 | Still | Square feed, app push companion primary |
| DS4-E | 1200 x 628 | Still | App push companion secondary, Meta retargeting |

DS4-C is the motion variant per Prompt P7 direction. The motion file export is text-free.
Copy layers are applied in the final composite after QA-passed copy is confirmed.

### Export settings

Still formats: PNG at 72 dpi. JPEG at 90% fallback.
Motion DS4-C: MP4, H.264, 30fps, no embedded audio (audio added at production if used).
No text baked into the motion export.

### Grid (DS4-A reference: 1080 x 1350)

- Canvas: 1080 x 1350, #141414.
- Card plane: #1A1A1A rectangle, 864px wide, 450px tall, centered horizontally (X 108 to 972),
  vertically centered in the lower-center portion, Y 620 to 1070. This is the grounding surface
  for the emerald path element.
- Above the card plane: clear #141414, Y 0 to 620. Upper overlay zone lives here.
- Below the card plane: clear #141414, Y 1070 to 1350. Lower overlay and CTA zones live here.
- Left and right text margin inside overlay zones: 80px.

Safe areas (DS4-A: 1080 x 1350):
- Upper overlay zone: Y 0 to 200. Reserved for [ar headline] and [en headline].
- Card composition zone: Y 200 to 1150. The visual composition. No overlay copy inside card.
- Lower overlay zone: Y 1150 to 1290. Reserved for [ar subline] and [en subline].
- CTA zone: Y 1290 to 1350. Reserved for [ar cta chip] and [en cta chip].

Scale for DS4-B (1080 x 1920):
- Upper overlay zone: Y 0 to 240.
- Card composition zone: Y 240 to 1620.
- Lower overlay zone: Y 1620 to 1800.
- CTA zone: Y 1800 to 1920.

Scale for DS4-C (motion, 1080 x 1920): same safe areas as DS4-B.

Scale for DS4-D (1080 x 1080):
- Upper overlay zone: Y 0 to 160.
- Card composition zone: Y 160 to 860.
- Lower overlay zone: Y 860 to 1000.
- CTA zone: Y 1000 to 1080.

Scale for DS4-E (1200 x 628):
- Center 60% horizontally (X 240 to X 960). Top and bottom 60px.
- All critical content within the inner zone.

### Layer structure (DS4-A still, back to front)

1. Background fill: #141414, full canvas. Locked.
2. Card plane: #1A1A1A rectangle per dimensions above. No corner radius.
3. Emerald path element: a single clean arc drawn from the left edge of the card to the right
   edge, slightly bowed upward at center, 3px line width, #009975, no fill. Geometry
   (DS4-A reference): left origin at approximately (108, 845), apex near (540, 760), right end
   at approximately (972, 820). A soft radial bloom at the right terminal point: #009975 at
   60% opacity, radius 25 to 30px, fading to transparent. The path is the single focal
   element of the composition.
4. [ar headline] slot: empty. Type: 36 to 44px, semibold, #FFFFFF. RTL. Right-anchored
   X 1000. Y 80 to 160 within upper overlay zone. Labeled for copywriter-ar fill.
   Copy variant bindings by channel: EMAIL-E1 subject (ar) for email header variant;
   SOCIAL-S2 caption (ar, first line) for organic; AD-RETARGET-1 headline (ar) for paid
   retargeting secondary.
5. [en headline] slot: empty. Same size, LTR. Left-anchored X 80. Same Y. Labeled for
   copywriter-en fill. Bindings mirror ar using en copy variants.
6. [ar subline] slot: empty. Type: 18 to 22px, regular, #D4D4D4. RTL. Right-anchored X 1000.
   Y 1170 to 1250 within lower overlay zone. Labeled for copywriter-ar fill.
   Copy variant binding: EMAIL-E1 body (ar, second line) or EMAIL-PREHEADER-E1 (ar).
7. [en subline] slot: empty. Same size, LTR. Left-anchored X 80. Same Y. Labeled for
   copywriter-en fill.
8. [ar cta chip] slot: empty. #009975 fill, #FFFFFF type, 12px corner radius, padding
   20px horizontal 10px vertical. RTL. Right-aligned in CTA zone. Labeled for copywriter-ar fill.
   Copy variant binding: EMAIL-CTA-E1 (ar) "ابدأ الدرس المجاني".
9. [en cta chip] slot: empty. Same style, LTR. Left-aligned in CTA zone. Labeled for
   copywriter-en fill. Copy variant binding: EMAIL-E1 CTA (en) "Explore the roster and start free".
10. Maharat wordmark: small, top-right corner, 32px from top, 80px from right. #FFFFFF.

### Motion spec (DS4-C: 1080 x 1920, 7 to 10 seconds at 30fps, reference duration 8 seconds = 240 frames)

Per Prompt P7 direction:

| Time | Frames (at 30fps) | Action |
|---|---|---|
| 0.0 to 0.3s | 0 to 9 | Fully dark #141414 field. No element visible. |
| 0.3s | 9 | #1A1A1A card plane fades in over 0.3 seconds (9 frames) to full opacity. |
| 0.6s to 0.6s | 18 | Card plane at full opacity, holds 0.4 seconds (12 frames). |
| 1.0s | 30 | Emerald path begins drawing from left to right across the card plane. Duration 1.0 second (30 frames), tracing the arc geometry. Stroke opacity builds 0 to 100%. |
| 2.0s | 60 | Path at full opacity, settled. Glow bloom at right terminal point intensifies over 0.3 seconds (9 frames). |
| 2.3s to 4.3s | 69 to 129 | Hold. Path and glow visible. Overlay copy slots visible in this window. |
| 4.3s | 129 | Clean fade to #141414 over 0.5 seconds (15 frames). |
| 4.8s to 8.0s | 144 to 240 | Hold clean #141414. |

Overlay text layers appear at frame 60 with a 10-frame fade-in. They exit with the composition
fade at frame 129. No text baked into the motion file export.

### Email header crop instructions (AB4 source, DS4-A or DS7-A source)

| Format ID | Dimensions (px) | Source | Primary use |
|---|---|---|---|
| DS4-email-A | 1200 x 480 | Center crop of DS4-A or DS7-A | Desktop email header, Emails E1 through E5 |
| DS4-email-B | 600 x 240 | Center-safe crop of DS4-email-A | Mobile email rendering |

Safe area for email header: center 60% horizontally (X 240 to X 960 on 1200px canvas).
Top and bottom 60px. All critical composition elements within this inner zone.

Background: #141414. Thin emerald #009975 bottom border, 3px tall, full canvas width at Y 477.

Overlay slots applied in email build by lifecycle-architect (not in the exported image):
- [ar email header line] slot: type 22 to 28px, semibold, #FFFFFF. RTL. Right-anchored X 960.
  Y 200 to 260. Labeled for copywriter-ar fill (from EMAIL-E1 through EMAIL-E5 ar variants,
  matched by message position per creative-package.md lifecycle routing table).
- [en email header line] slot: same size, LTR. Left-anchored X 240. Same Y. Labeled for
  copywriter-en fill (matched to the corresponding en email variant).

### App push companion still (AB5 source)

| Format ID | Dimensions (px) | Primary use |
|---|---|---|
| DS4-push-A | 1080 x 1080 | App push rich notification, primary |
| DS4-push-B | 1200 x 628 | App push, secondary |

Source: DS4-D (1080 x 1080 still) is the primary push image. DS4-E (1200 x 628) is the
secondary push image. No separate generation required.

Safe area: left and right 80px, top and bottom 80px.

Overlay slots (applied at build):
- [ar push line] slot: RTL, center-lower zone. Labeled for copywriter-ar fill.
  Copy variant binding: PUSH-P1 through PUSH-P5 body (ar) matched by push message position.
- [en push line] slot: LTR, center-lower zone. Labeled for copywriter-en fill.
  Copy variant binding: PUSH-P1 through PUSH-P5 body (en) matched by message position.

Note per OI-8: push platform is OPEN ITEM. The above covers a safe base size. Lifecycle-architect
confirms the final push image spec once the platform is named.

---

## DS5. Breadth field grid retargeting, static (C5, source AB6, Prompt P5)

Concept: C5 "This Summer, Choose Your Field". No photography dependency. Ready to spec.

### Gate status

Ready to build. No blocked open items for this spec.

### Formats and canvas dimensions

| Format ID | Dimensions (px) | Aspect | Primary use |
|---|---|---|---|
| DS5-A | 1080 x 1350 | 4:5 | Feed, paid retargeting primary |
| DS5-B | 1080 x 1080 | 1:1 | Square feed |
| DS5-C | 1080 x 1920 | 9:16 | Story |

### Export settings

PNG at 72 dpi. JPEG at 90% fallback. No text baked in.

### Grid (DS5-A reference: 1080 x 1350)

- Canvas: 1080 x 1350, #141414.
- Tile arrangement: seven tiles in a 3-4 pattern (3 tiles top row, 4 tiles bottom row).
- Tile size: 240 x 240px, #1A1A1A fill, corner radius 8px.
- Grid horizontal padding: (1080 - 3 x 240 - 2 x 32) / 2 = 148px each side for the top row.
  Bottom row: (1080 - 4 x 240 - 3 x 24) / 2 = 96px each side.
  Designer adjusts to maintain equal visual weight and generous centering.
- Tile spacing (gutter): 32px horizontal and vertical for the top row, 24px horizontal for
  the bottom row. Designer refines to achieve a balanced, premium feel.
- Grid vertical center: Y midpoint approximately at Y 675. The two rows together occupy
  approximately Y 400 to 960 on the 1350px canvas.
- Bottom accent bar: #009975 rectangle, full canvas width, 3px tall, Y 1320.

Safe areas (DS5-A: 1080 x 1350):
- Top overlay zone: Y 0 to 160. Reserved for [ar headline] and [en headline].
- Grid zone: Y 160 to 1170. Seven tiles plus generous background field.
- Lower overlay zone: Y 1170 to 1300. Reserved for [ar cta chip] and [en cta chip] plus
  the seven field label slots positioned over or below their respective tiles.
- Bottom accent bar: Y 1300 to 1350.
- Left and right text margin inside outer overlay zones: 80px.

Scale for DS5-B (1080 x 1080):
- Top overlay zone: Y 0 to 140.
- Grid zone: Y 140 to 860.
- Lower overlay zone: Y 860 to 1000.
- Bottom accent bar zone: Y 1000 to 1080.

Scale for DS5-C (1080 x 1920):
- Top overlay zone: Y 0 to 200.
- Grid zone: Y 200 to 1620.
- Lower overlay zone: Y 1620 to 1820.
- Bottom accent bar zone: Y 1820 to 1920.

### Layer structure (DS5-A, back to front)

1. Background fill: #141414, full canvas. Locked.
2. Seven tiles: #1A1A1A rectangles per grid above. Corner radius 8px. All interiors empty.
3. Field icons (one per tile, per the icon system from DS2, adapted for the smaller tile):
   - Tile 1 (music): wave arc, #009975, 2px line, 70% opacity.
   - Tile 2 (cooking): rising arc with dot, #009975, 2px line, 70% opacity.
   - Tile 3 (acting): light cone, #009975, 2px line, 70% opacity.
   - Tile 4 (makeup): sweep arc, #009975, 2px line, 70% opacity.
   - Tile 5 (business): ascending steps, #009975, 2px line, 70% opacity.
   - Tile 6 (styling): draped curve, #009975, 2px line, 70% opacity.
   - Tile 7 (marketing): radial node cluster, #009975, 2px line, 70% opacity.
   - One tile (center-bottom position, Tile 7 or designer's choice for visual balance):
     icon at 100% opacity #009975 as the focal point. All other tiles at 70%.
4. Bottom accent bar: #009975, full canvas width, 3px, at Y 1320.
5. [ar headline] slot: empty. Type: 32 to 40px, semibold, #FFFFFF. RTL. Right-anchored X 1000.
   Y 60 to 130 in top overlay zone. Labeled for copywriter-ar fill.
   Copy variant binding: AD-BREADTH-1 headline (ar) or AD-RETARGET-1 headline (ar) depending
   on whether this runs as prospecting or retargeting ad set.
6. [en headline] slot: empty. Same size, LTR. Left-anchored X 80. Same Y. Labeled for
   copywriter-en fill.
7. [ar field labels, 7 tiles] slots: one slot per tile, positioned centered below or inside
   each tile, approximately 8px below the tile bottom edge. Type: 13 to 15px, regular,
   #D4D4D4. RTL text anchor for each slot. Labels are field names only, no instructor names.
   Slots labeled [ar field label 1] through [ar field label 7], in tile order, all empty.
   Labeled for copywriter-ar fill.
   Copy variant binding: field names from AD-BREADTH-1 primary text (ar, the field list line).
8. [en field labels, 7 tiles] slots: same structure, LTR, positions mirroring the ar slots.
   Labeled [en field label 1] through [en field label 7], all empty. Labeled for
   copywriter-en fill.
9. [ar cta chip] slot: empty. #009975 fill, #FFFFFF type, 12px corner radius, padding
   20px horizontal 10px vertical. RTL. Right-aligned in lower overlay zone. Labeled for
   copywriter-ar fill. Copy variant binding: AD-RETARGET-1 cta (ar) "أكمل الآن" or
   AD-BREADTH-1 cta (ar) depending on channel placement.
10. [en cta chip] slot: empty. Same style, LTR. Left-aligned. Labeled for copywriter-en fill.
11. Maharat wordmark: small, top-right corner, 32px from top, 80px from right. #FFFFFF.

### Type scale (DS5-A reference)

| Role | Size | Weight | Color | Direction |
|---|---|---|---|---|
| AR headline | 32 to 40px | Semibold | #FFFFFF | RTL |
| EN headline | 32 to 40px | Semibold | #FFFFFF | LTR |
| AR field label | 13 to 15px | Regular | #D4D4D4 | RTL per tile |
| EN field label | 13 to 15px | Regular | #D4D4D4 | LTR per tile |
| CTA chip | 14px | Semibold | #FFFFFF | On #009975 fill |

---

## DS6. Campaign identity thematic still (C7, source AB7, Prompt P6)

Concept: C7 "Summer of Skills" campaign identity anchor. No photography dependency.
Campaign identity anchor across channels.

### Gate status

Ready to build. No blocked open items for this spec.

### Formats and canvas dimensions

| Format ID | Dimensions (px) | Aspect | Primary use |
|---|---|---|---|
| DS6-A | 1080 x 1350 | 4:5 | Feed primary, email launch header source |
| DS6-B | 1080 x 1080 | 1:1 | Square feed, app push companion |
| DS6-C | 1920 x 1080 | 16:9 | Landscape, landing hero fallback, email source |
| DS6-D | 1080 x 1920 | 9:16 | Story |

### Export settings

PNG at 72 dpi. JPEG at 90% fallback. No text baked in.

### Grid (DS6-A reference: 1080 x 1350)

- Canvas: 1080 x 1350, #141414.
- Central card: #1A1A1A rectangle, 756px wide, 607px tall (70% of width, approximately 45%
  of height). Centered horizontally and vertically: X 162 to 918, Y 371 to 978.
  Corner radius: 0 (per Prompt P6 direction, the card is a precise geometric element).
- Above card: thin emerald horizontal rule, full card width (756px), 3px tall, flush with
  top edge of card: X 162, Y 368 to 371.
- Below card: matching thin emerald horizontal rule, 3px tall, flush with bottom edge:
  X 162, Y 978 to 981.
- Card interior: entirely empty flat #1A1A1A. Generous padding. No icon, no text.

Safe areas (DS6-A: 1080 x 1350):
- Top safe zone: Y 0 to 200. Pure #141414. No critical element.
- Card zone: Y 200 to 1150. Card and emerald rules live within this band.
- Bottom safe zone: Y 1150 to 1350. Overlay zones as below.
- Left and right margin for all overlay text: 100px from canvas edge.

Within the card, two overlay zones:
- Upper card zone: top 40% of card interior. Reserved for [ar campaign theme label] and
  [en campaign theme label]. Y 411 to 614 (absolute canvas coordinates, DS6-A).
- Lower card zone: bottom 40% of card interior. Reserved for [ar supporting line] and
  [en supporting line]. Y 735 to 938 (absolute canvas coordinates, DS6-A).
- CTA zone: below card, Y 1010 to 1100. Reserved for [ar cta chip] and [en cta chip].

Scale for DS6-B (1080 x 1080):
- Card: 756 x 486px, centered at (540, 540). Card Y: 297 to 783.
- Upper card zone: Y 337 to 513.
- Lower card zone: Y 607 to 743.
- Emerald rules: flush top and bottom of card.
- CTA zone: Y 820 to 900.

Scale for DS6-C (1920 x 1080):
- Card: 1344px wide, 486px tall, centered: X 288 to 1632, Y 297 to 783.
- Emerald rules: full card width.
- Overlay zones scale proportionally.

Scale for DS6-D (1080 x 1920):
- Card: 756px wide, 864px tall, centered: X 162 to 918, Y 528 to 1392.
- Top safe zone: Y 0 to 200. Bottom safe zone: Y 1650 to 1920.
- Upper card zone and lower card zone proportionally scaled within the taller card.
- CTA zone: Y 1440 to 1530.

### Layer structure (DS6-A, back to front)

1. Background fill: #141414, full canvas. Locked.
2. Central card: #1A1A1A rectangle per dimensions above. No corner radius. Flat, precise.
3. Emerald rule above card: #009975, 756px wide, 3px tall, flush with card top.
4. Emerald rule below card: #009975, 756px wide, 3px tall, flush with card bottom.
5. [ar campaign theme label] slot: empty. This is the primary slot for the campaign label
   equivalent of "صيف المهارات" (copywriter-ar writes the final form). Type: 32 to 40px,
   semibold, #FFFFFF. RTL. Right-anchored at X 818 (card right edge minus 100px interior
   padding). Positioned in upper card zone. Labeled for copywriter-ar fill.
   Copy variant binding: the "صيف المهارات" campaign theme from copy-package.ar.md,
   specifically the EMAIL-SUBJECT-E1 primary (ar) or the social campaign label from SOCIAL-S1.
6. [en campaign theme label] slot: empty. Same size, LTR. Left-anchored at X 262 (card left
   edge plus 100px interior padding). Same zone. Labeled for copywriter-en fill.
   Copy variant binding: SOCIAL-S1 caption opener (en) "Summer of Skills." or EMAIL-E1
   subject primary (en) "This summer, build a skill you actually choose."
7. [ar supporting line] slot: empty. Type: 20 to 24px, regular, #D4D4D4. RTL. Right-anchored
   at X 818. Positioned in lower card zone. Labeled for copywriter-ar fill.
   Copy variant binding: EMAIL-PREHEADER-E1 (ar) or SOCIAL-S1 caption second line (ar).
8. [en supporting line] slot: empty. Same size, LTR. Left-anchored X 262. Same zone.
   Labeled for copywriter-en fill.
9. [ar cta chip] slot: empty. #009975 fill, #FFFFFF type, 12px corner radius, padding
   20px horizontal 10px vertical. RTL. Right-aligned in CTA zone. Labeled for copywriter-ar fill.
   Copy variant binding: SOCIAL-CTA-S1 (ar) "ابدأ مجاناً" for social; EMAIL-CTA-E1 (ar) for email.
10. [en cta chip] slot: empty. Same style, LTR. Left-aligned in CTA zone. Labeled for
    copywriter-en fill. Copy variant binding: SOCIAL-S1 CTA (en) "[Link in bio / Swipe up]"
    or EMAIL-E1 CTA (en).
11. Maharat wordmark: small, top-right corner, 40px from top, 80px from right. #FFFFFF.

### Type scale (DS6-A reference)

| Role | Size | Weight | Color | Direction |
|---|---|---|---|---|
| AR campaign theme label | 32 to 40px | Semibold | #FFFFFF | RTL, inside card |
| EN campaign theme label | 32 to 40px | Semibold | #FFFFFF | LTR, inside card |
| AR supporting line | 20 to 24px | Regular | #D4D4D4 | RTL, inside card |
| EN supporting line | 20 to 24px | Regular | #D4D4D4 | LTR, inside card |
| CTA chip | 14px | Semibold | #FFFFFF | On #009975 fill |

---

## DS7. Multi-field breadth reel, end card matte (C6, source AB8, Prompt P8)

Concept: C6 "Watch the First Lesson Free". The full video spec (DS7-MASTER) is blocked
pending multi-field footage confirmation. The end card matte is a Canva build, ready
to spec. Fallback for the full video is DS4 motion (C4) per field.

### Gate status

DS7-MASTER (the full edited reel): BLOCKED. OI-2 must be resolved (rights-cleared class
footage from at least three instructor fields confirmed) before the master is cut.
If fewer than three fields of footage are confirmed at the human gate, DS7-MASTER remains
blocked and DS4 motion runs as the campaign's video asset per field.

DS7-ENDCARD (the end card matte): Ready to build in Canva. No footage dependency.

### Formats

End card matte (DS7-ENDCARD):

| Format ID | Dimensions (px) | Primary use |
|---|---|---|
| DS7-ENDCARD-A | 1080 x 1920 | Vertical end card, Reels and TikTok |
| DS7-ENDCARD-B | 1920 x 1080 | Landscape end card, YouTube |

### Export settings for DS7-ENDCARD

PNG at 72 dpi. Also export as a 3-second still clip (looped or held frame) for NLE insertion.
No text baked in.

### Layer structure (DS7-ENDCARD-A: 1080 x 1920)

1. Background fill: #141414, full canvas. Locked.
2. Emerald accent bar: #009975, full canvas width, 4px tall, centered vertically at Y 960.
3. Maharat brand mark: position placeholder centered in the upper two-thirds of the canvas,
   approximately Y 400 to 800. Designer places the confirmed brand mark at build.
4. Lower third: Y 1150 to 1920, pure #141414, reserved for end card copy overlay.

Overlay slots:
- [ar end card copy] slot: empty. Type: 26 to 30px, #FFFFFF. RTL. Right-anchored at X 1000.
  Y 1200 (line 1), Y 1270 (line 2) for a two-line treatment. Labeled for copywriter-ar fill.
  Copy variant binding: best-fit from copy-package.ar.md; the PUSH-TITLE-P1 (ar) "صيف المهارات
  بدأ" as the first line and a "ابدأ مجاناً" CTA as line 2, or a custom end-card line authored
  at build once the video master structure is confirmed.
- [en end card copy] slot: empty. Same size, LTR. Left-anchored X 80. Same Y positions.
  Labeled for copywriter-en fill. Copy variant binding: PUSH-P1 title (en) "Summer of Skills
  starts now." as line 1 or equivalent end card phrasing confirmed at build.

Scale for DS7-ENDCARD-B (1920 x 1080): accent bar at Y 540. Brand mark centered in
left-center or right-center column. Lower third Y 750 to 1080 for overlay.

### Master reel spec (DS7-MASTER, blocked pending OI-2)

When OI-2 is resolved, the master reel is built per the following spec.

Build tool: NLE editor (designer's confirmed toolchain, Premiere Pro or equivalent).
End card matte (DS7-ENDCARD-A) is the pre-built Canva asset inserted as a clip.

Master formats:

| Format ID | Dimensions (px) | Duration | Primary use |
|---|---|---|---|
| DS7-MASTER-A | 1080 x 1920 | 20 to 30 seconds | Organic Reels and TikTok, Story |
| DS7-MASTER-B | 1920 x 1080 | 20 to 30 seconds | Organic YouTube master |
| DS7-MASTER-C | 1080 x 1920 | 15 seconds | Paid YouTube pre-roll, paid TikTok |
| DS7-MASTER-D | 1920 x 1080 | 6 seconds | YouTube TrueView bumper |

DS7-MASTER-C and DS7-MASTER-D are repurposed from DS7-MASTER-A (vertical) and DS7-MASTER-B
(landscape). Method: manual cut until OI-3 (BLOTATO_API_KEY) is resolved. When OI-3 is
resolved, the Blotato workflow handles the repurpose cuts from the master.

Safe areas (DS7-MASTER-A: 1080 x 1920):
- Top overlay zone: Y 0 to 200. Platform UI. Keep clear.
- Active overlay zone upper: Y 200 to 700. Hook overlay, opening card copy.
- Footage zone: Y 200 to 1620. Full-frame footage. Overlays float above.
- Active overlay zone lower: Y 1620 to 1820. Closing card copy, field label overlays.
- Bottom UI zone: Y 1820 to 1920. Platform chrome safe zone. Keep clear.
- Left and right overlay text margin: 80px from canvas edge.

Safe areas (DS7-MASTER-B: 1920 x 1080):
- Left and right: 160px reserved.
- Top and bottom: 100px reserved.
- Active overlay area: X 160 to 1760, Y 100 to 980.

Structure (DS7-MASTER-A, 27-second master reference at 30fps = 810 frames):

Segment 1: Opening card, 0 to 2 seconds (frames 0 to 60).
- Visual: #141414 matte. Maharat brand mark centered.
- Overlay slots:
  - [ar opening line] slot: empty. Type 32 to 38px, semibold, #FFFFFF. RTL. Right-anchored
    X 1000. Y 500. Labeled for copywriter-ar fill. Copy binding: AD-BREADTH-1 headline (ar).
  - [en opening line] slot: empty. Same size, LTR. Left-anchored X 80. Same Y. Labeled for
    copywriter-en fill. Copy binding: AD-BREADTH-1 headline (en).

Segment 2: Field sequence, 2 to 23 seconds (frames 60 to 690).
- Visual: 5 to 7 footage moments from rights-cleared class material, one per field.
  Each moment 2 to 3 seconds. Teaching instants only, no talking-head monologues.
  Between each moment: 0.5-second (15-frame) #141414 hard cut.
  Footage graded warm-neutral. Lift blacks slightly to integrate with #141414 mattes.
  No text baked into footage. Emerald #009975 accent mark on transition mattes only
  (a 4px horizontal line, 300px wide, centered horizontally, on each #141414 cut).
  Not a persistent overlay throughout.
- Per-moment overlay slots (one pair per field moment, 3 pairs shown, extend for more):
  - [field label 1 ar] and [field label 1 en]: lower-safe zone, Y 1680, 14px regular #D4D4D4.
    Labeled for copywriter-ar and copywriter-en fill. Field names only, no instructor names
    in this zone. Copy bindings from AD-BREADTH-1 field list (ar and en).
  - [field label 2 ar] and [field label 2 en]: same spec, same Y, second field moment.
  - [field label 3 ar] and [field label 3 en]: and so on for each field moment.
  Each field label overlay appears 12 frames into its footage moment, exits 12 frames before
  the next #141414 cut.

Segment 3: Closing moment, 23 to 25 seconds (frames 690 to 750).
- Visual: a final footage moment or clean #141414 matte. Invitation feel.
- Overlay slots:
  - [ar closing line] slot: empty. Type 30 to 36px, semibold, #FFFFFF. RTL. Right-anchored
    X 1000. Y 1700. Labeled for copywriter-ar fill.
    Copy binding: EMAIL-CTA-E1 (ar) "ابدأ الدرس المجاني" or AD-BREADTH-1 cta (ar).
  - [en closing line] slot: empty. Same size, LTR. Left-anchored X 80. Same Y. Labeled for
    copywriter-en fill.

End card: 25 to 30 seconds (frames 750 to 900). Pre-built DS7-ENDCARD-A inserted as a clip.
Overlay slots from DS7-ENDCARD-A slot map above.
No price, no promo in any end card slot.

### Color treatment notes

Footage grade: warm-neutral. Not cold or desaturated, not oversaturated. Lift blacks slightly
(target near-black #141414 at 15 to 20 IRE) to integrate smoothly with the #141414 matte cards.
No skin-tone shift. No fabric color alteration. LUT selection confirmed by designer once footage
is reviewed.

---

## DS8. Landing page hero image (C1 source, routes to web-design-director, source AB9)

Concept: C1 "Many Fields, One Summer", 16:9 variant, per Prompt P2. No photography dependency.

### Gate status

Ready to build (visual layer). The actual web layout, RTL/LTR breakpoint behavior, button
component, and typography are web-design-director's scope. This spec provides the background
image layer and slot positions as visual direction only.

### Formats

| Format ID | Dimensions (px) | Primary use |
|---|---|---|
| DS8-A | 1920 x 1080 | Landing hero primary, full breakpoint |
| DS8-B | 1440 x 810 | Landing hero, mid-breakpoint crop |

### Export settings

PNG at 72 dpi. The image is the background layer. No text baked in.

### Grid and safe areas (DS8-A: 1920 x 1080)

- Canvas: 1920 x 1080, #141414.
- Card mosaic zone: X 200 to 1720, Y 60 to 960. Seven cards in a horizontal mosaic,
  maintaining the asymmetric rhythm of DS1 adapted for 16:9. Cards reflow as a single
  flowing horizontal row or a 4-3 two-row arrangement at this aspect ratio.
- Left overlay zone: X 0 to 200. Clearance only. Web-design-director uses this zone for
  AR headline in RTL layout.
- Right overlay zone: X 1720 to 1920. Clearance only. Used for EN headline in LTR layout
  by web-design-director.
- Bottom CTA zone: Y 960 to 1080. Reserved for CTA button placement by web-design-director.

Overlay slots (passed to web-design-director and copywriters for web surface, not in image):
- [ar landing hero headline] slot: copywriter-ar, left-center zone on RTL layout, RTL.
  Copy variant binding: LP-HEADLINE-1 (ar) "هذا الصيف، اختر مجالك وابنِ مهارة حقيقية" (primary)
  or LP-HEADLINE-2 (ar) "صيف المهارات، تعلّم من نخبة العرب" (alternate).
- [en landing hero headline] slot: copywriter-en, right-center zone on LTR layout, LTR.
  Copy variant binding: LP-HEADLINE-1 (en) "Summer of Skills." (primary) or LP-HEADLINE-2 (en)
  "Build a real skill this summer." (alternate).
- [ar landing hero subline] slot: copywriter-ar, below headline, RTL.
  Copy variant binding: LP-SUBHEAD-1 (ar) or LP-SUBHEAD-2 (ar).
- [en landing hero subline] slot: copywriter-en, below headline, LTR.
  Copy variant binding: LP-SUBHEAD-1 (en) or LP-SUBHEAD-2 (en).
- [ar cta button label] slot: copywriter-ar, bottom CTA zone, RTL.
  Copy variant binding: LP-CTA-1 (ar) "ابدأ الدرس المجاني".
- [en cta button label] slot: copywriter-en, bottom CTA zone, LTR.
  Copy variant binding: LP-CTA-1 (en) "Start your free lesson".

Note: Web-design-director produces the build-ready landing page spec incorporating DS8-A as
the background image layer. Typography, button components, RTL/LTR breakpoints, and the
LP-CTA-2 secondary CTA placement are all web-design-director's scope.

---

## Copy-overlay slot index (complete, all specs)

All slots below are empty. Language label is the routing destination. Slots marked RTL require
right-to-left text direction in the build tool.

### DS1 slots

| Slot label | Formats | Zone | Dir | Copy variant binding |
|---|---|---|---|---|
| [ar headline] | DS1-A through DS1-E | Upper overlay | RTL | AD-BREADTH-1 headline (ar) or LP-HEADLINE-1 (ar) |
| [en headline] | DS1-A through DS1-E | Upper overlay | LTR | AD-BREADTH-1 headline (en) or LP-HEADLINE-1 (en) |
| [ar subline] | DS1-A through DS1-E | Lower overlay | RTL | AD-BREADTH-1 primary text ar line 2 or SOCIAL-S1 ar line 2 |
| [en subline] | DS1-A through DS1-E | Lower overlay | LTR | AD-BREADTH-1 body en line 2 or SOCIAL-S1 en line 2 |
| [ar cta chip] | DS1-A through DS1-E | CTA zone | RTL | AD-BREADTH-1 cta (ar) or LP-CTA-1 (ar) |
| [en cta chip] | DS1-A through DS1-E | CTA zone | LTR | AD-BREADTH-1 CTA (en) or LP-CTA-1 (en) |

### DS2 slots (per variant, eight variants)

| Slot label | Formats | Zone | Dir | Copy variant binding |
|---|---|---|---|---|
| [ar field headline] | DS2-[variant]-A through C | Top overlay | RTL | Per-field ad headline (ar), AD-BREADTH-1 for breadth variant |
| [en field headline] | DS2-[variant]-A through C | Top overlay | LTR | Per-field ad headline (en) |
| [ar instructor name and credential] | DS2-[variant]-A through C | Card lower zone | RTL | Per-field ad primary text (ar), instructor name line; confirm-at-gate; DS2-breadth: unnamed breadth only |
| [en instructor name and credential] | DS2-[variant]-A through C | Card lower zone | LTR | Per-field ad body (en), instructor name line; same gate restrictions |
| [ar free chapter callout] | DS2-[variant]-A through C | Card lower zone | RTL | Per-field ad primary text last line (ar) |
| [en free chapter callout] | DS2-[variant]-A through C | Card lower zone | LTR | "The first lesson is free." from per-field EN ad body |
| [ar cta chip] | DS2-[variant]-A through C | Lower overlay | RTL | Per-field cta (ar) |
| [en cta chip] | DS2-[variant]-A through C | Lower overlay | LTR | Per-field CTA (en) |

### DS3 slots (per instructor, seven instances when photography confirmed)

| Slot label | Formats | Zone | Dir | Copy variant binding |
|---|---|---|---|---|
| [ar headline] | DS3-[instructor]-A through D | Upper overlay | RTL | Per-field ad headline (ar); confirm-at-gate per instructor |
| [en headline] | DS3-[instructor]-A through D | Upper overlay | LTR | Per-field ad headline (en) |
| [ar instructor name and field] | DS3-[instructor]-A through D | Lower overlay | RTL | Instructor name and cleared credential (ar); confirm-at-gate; verify-before-use restrictions noted |
| [en instructor name and field] | DS3-[instructor]-A through D | Lower overlay | LTR | Instructor name and cleared credential (en); same restrictions |
| [ar cta chip] | DS3-[instructor]-A through D | Accent bar zone | RTL | Per-field cta (ar) |
| [en cta chip] | DS3-[instructor]-A through D | Accent bar zone | LTR | Per-field CTA (en) |

### DS4 slots

| Slot label | Formats | Zone | Dir | Copy variant binding |
|---|---|---|---|---|
| [ar headline] | DS4-A, DS4-B, DS4-D | Upper overlay | RTL | EMAIL-E1 subject (ar) or SOCIAL-S2 ar or AD-RETARGET-1 headline (ar) by channel |
| [en headline] | DS4-A, DS4-B, DS4-D | Upper overlay | LTR | EMAIL-E1 subject (en) or equivalent en variant |
| [ar subline] | DS4-A, DS4-B, DS4-D | Lower overlay | RTL | EMAIL-PREHEADER-E1 (ar) or EMAIL-BODY-E1 second line (ar) |
| [en subline] | DS4-A, DS4-B, DS4-D | Lower overlay | LTR | EMAIL-E1 preheader (en) |
| [ar cta chip] | DS4-A, DS4-B, DS4-D | CTA zone | RTL | EMAIL-CTA-E1 (ar) |
| [en cta chip] | DS4-A, DS4-B, DS4-D | CTA zone | LTR | EMAIL-E1 CTA (en) |
| [ar push line] | DS4-push-A, DS4-push-B | Center-lower | RTL | PUSH-P1 through PUSH-P5 body (ar) by message position |
| [en push line] | DS4-push-A, DS4-push-B | Center-lower | LTR | PUSH-P1 through PUSH-P5 body (en) |
| [ar email header line] | DS4-email-A, DS4-email-B | Center (applied in email build) | RTL | EMAIL-E1 through EMAIL-E5 ar subject/preheader by message position |
| [en email header line] | DS4-email-A, DS4-email-B | Center (applied in email build) | LTR | EMAIL-E1 through EMAIL-E5 en subject/preheader |

### DS5 slots

| Slot label | Formats | Zone | Dir | Copy variant binding |
|---|---|---|---|---|
| [ar headline] | DS5-A through C | Top overlay | RTL | AD-BREADTH-1 headline (ar) or AD-RETARGET-1 headline (ar) |
| [en headline] | DS5-A through C | Top overlay | LTR | AD-BREADTH-1 headline (en) or AD-RETARGET-1 headline (en) |
| [ar field labels, tiles 1 through 7] | DS5-A through C | Per-tile | RTL | Field names from AD-BREADTH-1 primary text (ar), field list line |
| [en field labels, tiles 1 through 7] | DS5-A through C | Per-tile | LTR | Field names from AD-BREADTH-1 body (en), field list line |
| [ar cta chip] | DS5-A through C | Lower overlay | RTL | AD-RETARGET-1 cta (ar) or AD-BREADTH-1 cta (ar) |
| [en cta chip] | DS5-A through C | Lower overlay | LTR | AD-RETARGET-1 CTA (en) or AD-BREADTH-1 CTA (en) |

### DS6 slots

| Slot label | Formats | Zone | Dir | Copy variant binding |
|---|---|---|---|---|
| [ar campaign theme label] | DS6-A through D | Upper card zone | RTL | SOCIAL-S1 caption opener (ar) or EMAIL-SUBJECT-E1 primary (ar) label form |
| [en campaign theme label] | DS6-A through D | Upper card zone | LTR | SOCIAL-S1 caption opener (en) "Summer of Skills." |
| [ar supporting line] | DS6-A through D | Lower card zone | RTL | EMAIL-PREHEADER-E1 (ar) or SOCIAL-S1 second line (ar) |
| [en supporting line] | DS6-A through D | Lower card zone | LTR | EMAIL-E1 preheader (en) or SOCIAL-S1 second line (en) |
| [ar cta chip] | DS6-A through D | CTA zone | RTL | SOCIAL-CTA-S1 (ar) "ابدأ مجاناً" or EMAIL-CTA-E1 (ar) |
| [en cta chip] | DS6-A through D | CTA zone | LTR | SOCIAL-S1 CTA (en) or EMAIL-E1 CTA (en) |

### DS7 slots

| Slot label | Segment | Dir | Copy variant binding |
|---|---|---|---|
| [ar end card copy] | DS7-ENDCARD-A and B | RTL | PUSH-TITLE-P1 (ar) as line 1; AD-BREADTH-1 cta (ar) as line 2 or custom end-card line at build |
| [en end card copy] | DS7-ENDCARD-A and B | LTR | PUSH-P1 title (en) as line 1 or equivalent |
| [ar opening line] | DS7-MASTER segment 1 | RTL | AD-BREADTH-1 headline (ar) |
| [en opening line] | DS7-MASTER segment 1 | LTR | AD-BREADTH-1 headline (en) |
| [field label N ar] (tiles 1 through 7) | DS7-MASTER segment 2 per moment | RTL | Field names from AD-BREADTH-1 primary text (ar) |
| [field label N en] (tiles 1 through 7) | DS7-MASTER segment 2 per moment | LTR | Field names from AD-BREADTH-1 body (en) |
| [ar closing line] | DS7-MASTER segment 3 | RTL | EMAIL-CTA-E1 (ar) or AD-BREADTH-1 cta (ar) |
| [en closing line] | DS7-MASTER segment 3 | LTR | EMAIL-E1 CTA (en) |

### DS8 slots (passed to web-design-director)

| Slot label | Zone | Dir | Copy variant binding |
|---|---|---|---|
| [ar landing hero headline] | RTL layout, center-left | RTL | LP-HEADLINE-1 (ar) primary or LP-HEADLINE-2 (ar) alt |
| [en landing hero headline] | LTR layout, center-right | LTR | LP-HEADLINE-1 (en) primary or LP-HEADLINE-2 (en) alt |
| [ar landing hero subline] | Below headline, RTL | RTL | LP-SUBHEAD-1 (ar) or LP-SUBHEAD-2 (ar) |
| [en landing hero subline] | Below headline, LTR | LTR | LP-SUBHEAD-1 (en) or LP-SUBHEAD-2 (en) |
| [ar cta button label] | Bottom CTA zone | RTL | LP-CTA-1 (ar) |
| [en cta button label] | Bottom CTA zone | LTR | LP-CTA-1 (en) |

---

## Asset sourcing and gate summary

| Asset ref | Source type | Rights basis | Build status |
|---|---|---|---|
| DS1 hero grid | Generated per Prompts P1 and P2 | Maharat-generated, no likeness | Ready |
| DS2 per-field abstract (8 variants) | Generated per Prompt P3 base, icon adapted | Maharat-generated, no likeness | Ready (visual layer); overlay slots confirm-at-gate per instructor |
| DS3 instructor portraits (7 instances) | Real rights-cleared photography or class still | Rights-cleared Maharat library | BLOCKED: OI-1 open per instructor. Fallback: corresponding DS2 variant |
| DS4 abstract path still and motion | Generated per Prompts P4 and P7 | Maharat-generated, no likeness | Ready |
| DS5 breadth field grid | Generated per Prompt P5 | Maharat-generated, no likeness | Ready |
| DS6 campaign thematic still | Generated per Prompt P6 | Maharat-generated, no likeness | Ready |
| DS7-ENDCARD matte | Canva build, #141414 matte plus brand mark plus emerald bar | Maharat-owned, no photography | Ready |
| DS7-MASTER multi-field reel | Real rights-cleared Maharat class footage | Rights-cleared Maharat library | BLOCKED: OI-2 open. Min 3 fields required. Fallback: DS4 motion |
| DS8 landing hero image | Generated per Prompt P2 (16:9) | Maharat-generated, no likeness | Ready (image layer). Web layout owned by web-design-director |

No generated instructor likeness is used anywhere in this campaign.
No Arabic text is baked into any generated image layer or motion export.
All copy arrives as a human-placed overlay from QA-passed copywriter-ar and copywriter-en output.

---

## Design QA verdict

Gate: design_qa
Date: 2026-06-12
Produced by: designer

### Check 1: RTL correct

Result: PASS

All Arabic overlay slots across DS1 through DS8 are labeled RTL with right-side text anchors
at X 1000 (or the equivalent right boundary at 80px from the right edge, scaled per format).
No mixed AR and EN within a single slot; each language occupies its own named slot. In every
spec, the ar slot anchor is at the right safe-area boundary and the en slot anchor is at the
left. No Arabic text is authored in any generated image layer or motion export. Copy is
overlaid at build time only, from QA-passed copywriter-ar output.

The seven per-field DS2 variant slots follow the same RTL structure as the breadth assets.
DS5 tile field-label slots each carry individual RTL or LTR anchors positioned to the
respective tile's safe area, maintaining directional integrity even in a grid layout.

### Check 2: Safe areas and dimensions present

Result: PASS

Every spec carries explicit safe-area measurements per format, with named zones (top overlay,
lower overlay, CTA zone, platform UI clearance) and Y-coordinate ranges. Platform UI zones
are respected: on 9:16 Story and Reels formats (DS1-B, DS2-[variant]-C, DS4-B, DS4-C,
DS5-C, DS6-D), the top 200px and bottom 100px (minimum) are kept clear of critical overlay
content. On Meta and IG feed formats, the top and bottom overlay zones are within the
established safe ranges. On email header formats (DS4-email-A and DS4-email-B), the center
60% of the canvas width is the safe zone and top and bottom 60px are respected. All nine
dimension sets from AB1 through AB9 are present in the specs.

### Check 3: Western numerals only in any rendered text

Result: PASS

No numeral characters appear in any generated layer of any spec. The only numeral reference
in the specs is within the type scale tables (pixel values for sizing), which are build
instructions, not rendered text. All overlay copy slots are empty and labeled, not yet filled.
The global design token section at the top of this document explicitly prohibits Eastern Arabic
numerals (U+0660 to U+0669) from any rendered layer. The instruction to copywriter-ar and
copywriter-en explicitly requires Western numerals (0 through 9) in all filled copy. The
copy-package.ar.md pre-handoff checklist confirms the only digit used in the AR copy is 40
(Western, for Ragheb Alama's years), and copy-package.en.md confirms the same. No tatweel
or kashida appears anywhere.

### Check 4: Visual constants applied

Result: PASS

Every spec uses #141414 as the canvas background fill. #1A1A1A is used as the card and
panel surface. #009975 is used as a highlight accent only: 4px border stripes (DS1, DS2),
3px horizontal rules (DS6), 3 to 4px bottom bars (DS2, DS5, DS7-ENDCARD), path and arc
elements (DS4), icon line shapes (DS2, DS5), CTA chip fills (all specs), and transition
accent marks (DS7-MASTER). The emerald accent does not flood any frame; it is the signal
element in each composition. Type on overlays is #FFFFFF for primary and #D4D4D4 for
secondary throughout. No spec uses #009975 as a background or dominant color. The design
token table at the top of this document records and governs these constants for all specs.

### Check 5: Premium and uncluttered

Result: PASS

DS1: seven-card mosaic on a clean #141414 field. Generous gutters between cards. One focal
accent stripe. No competing graphic elements. No text in the generated layer.

DS2: one card, one abstract icon shape, one bottom bar. Generous breathing room above, below,
and around the card. The icon is a single-line open shape, not a complex illustration. The
lower third of the card is empty and reserved for overlay copy.

DS3: editorial portrait, generous space above and below, one thin emerald accent bar, no
competing graphic elements. Premium treatment of the rights-cleared asset.

DS4: a single arc path on a clean dark field with one centered card plane. One focal element.
No clutter. The motion sequence (DS4-C) is deliberate: elements appear one at a time.

DS5: seven small tiles with generous spacing and a single focal highlight tile. The grid is
balanced with clear #141414 field visible between and around all tiles. No stacking of text
or overlapping icons.

DS6: one centered card with two thin emerald rules. The card interior is entirely empty in
the generated layer. Maximum space reserved for copy. No icon, no image, no decorative
element beyond the two rules.

DS7-ENDCARD: flat dark matte, one thin accent bar, brand mark. Spare and confident.

DS8: card mosaic in 16:9, same generous spacing as DS1. Image layer only; the web surface
above carries the type and interaction elements.

### Check 6: No Arabic text baked into any generated image

Result: PASS

All generated image layers (DS1 via Prompts P1 and P2, DS2 via Prompt P3, DS4 still via
Prompt P4, DS4 motion via Prompt P7, DS5 via Prompt P5, DS6 via Prompt P6, DS7-ENDCARD via
Prompt P8, DS8 via Prompt P2) are specified as text-free in both the original creative-package
prompts and in the layer structure of each spec in this document. No Arabic, no English copy
of any kind is baked into any generated layer. DS3 uses a real photograph with no text baked
in. DS7-MASTER uses real rights-cleared class footage with no text baked into the footage or
the matte elements.

Every copy element across all specs is an overlay slot. Slots are applied at build time from
QA-passed copywriter-ar and copywriter-en output, placed by the designer or lifecycle-architect
as named overlay layers and never as part of the generated image export.

The hard rule from CLAUDE.md and from the designer system instructions is confirmed: no Arabic
text inside a generated image, no exceptions. Generative tools mangle Arabic script and add
tatweel; overlay by a human or set in-build is the only permitted method.

### Overall design QA verdict: PASS

All six checks pass. No fix list required.

Human design check note: the final visual quality pass on each rendered asset (confirming
correct visual balance, text legibility at intended sizes, color accuracy of the generated
layer against the token values, and RTL rendering correctness with actual Arabic type in the
overlay) remains a human check before any asset advances to the human gate for build
approval. This design QA verdict covers the spec itself, not a rendered output, because no
live build tool has been executed in this reasoning step. That check is explicitly flagged
as pending at the human gate.

Open items flagged at this gate (procedural blockers for build, not design-qa failures):

- OI-1: DS3 all seven instructor portrait instances are build-blocked. Specs complete;
  build awaits confirmed rights-cleared photography per instructor.
- OI-2: DS7-MASTER is build-blocked. Spec complete; build awaits confirmed multi-field
  footage (minimum three fields). If fewer than three fields confirmed, DS4 motion runs
  as the campaign's video asset.
- OI-3: Blotato credential open. DS7-MASTER repurpose cuts (DS7-MASTER-C 15-second and
  DS7-MASTER-D 6-second) are cut manually until resolved. Not a blocker for the master cut.
- OI-4: Per-instructor naming confirm-at-gate for each of the seven. Overlay slots in DS2
  and DS3 that carry instructor names are labeled confirm-at-gate. If a name is not cleared,
  that slot drops to the unnamed breadth descriptor without rewriting the spec.
- OI-5: Verify-before-public-use restrictions for Toufic Kreidieh (Brands For Less,
  $10,000-garage detail) and Elda Choucair (Omnicom, Forbes, Cannes, figures). These facts
  do not appear in any overlay slot and must not be added until verified.
- OI-6: No promo confirmed. No price chip slot exists in any spec. If Ahmed confirms a promo,
  the relevant specs require a price-chip overlay slot addition before build proceeds.
- OI-7: Font confirmation open. The confirmed Maharat platform typeface must be used at build
  time. Designer must confirm the font before build. This is a build-gate item.
- OI-8: App push platform OPEN ITEM. DS4-push-A and DS4-push-B are specced to a safe base.
  Lifecycle-architect confirms the final push image spec once the platform is named.

Next gate: brand-qa-reviewer.
Human gate: nothing builds, publishes, or spends until Ahmed approves per action and per
campaign. All open items above are surfaced at the human gate. Instructor-naming discipline
travels with this artifact: the seven nameable instructors are confirm-at-gate with cleared,
page-sourced facts only; the four non-nameable instructors (Rahma Riad, Sami Al Jaber, Mona
Ataya, Mo Islam) never appear in any overlay slot and are referenced only as unnamed breadth.
