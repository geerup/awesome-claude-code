# Design Specs: Bassam Fattouh Teaches Makeup

## Envelope

- campaign_id: 2026-06-bassam-fattouh-makeup
- produced_by: designer
- stream: 3 creative production
- status: draft
- qa:
  - skill_eval: pending
  - arabic_qa: na (no Arabic authored in this stream; all ar slots routed to copywriter-ar)
  - english_qa: na (no English copy authored in this stream; all en slots routed to copywriter-en)
  - design_qa: see verdict section at end of this document
  - brand_qa: pending (routes to brand-qa-reviewer after design-qa pass)
- open_items:
  - OI-1: Bassam Fattouh rights-cleared photography and class stills. OPEN. AB1 (C1) and AB4
    (C4) are build-blocked until this is confirmed. Interim campaign runs on AB2 and AB3.
  - OI-2: Bassam Fattouh rights-cleared class footage and timecodes for C4 segments 1 and 4.
    OPEN. AB4 is build-blocked independently of OI-1. Both must be resolved before the
    trailer build begins.
  - OI-3: BLOTATO_API_KEY credential. OPEN. C4 repurpose cuts (15s, 30s) are manually
    edited until resolved. Not a blocker for the 35-second master cut spec.
  - OI-4: Confirmed approved promo or trial offer. None stated in the brief. No price chip
    is included in any spec. If Ahmed confirms a promo, a price-chip overlay slot must be
    added to DS1 and DS3 and re-routed to both copywriters before build proceeds.
  - OI-5: C4 segment 2 authority facts. Profile clears "leading regional makeup artist,
    teaches makeup on Maharat." No awards, career figures, or additional credentials are
    cleared. Slot labeled [ar authority line] and [en authority line] may only be filled
    with cleared facts from profile.md. If cleared facts do not fill the beat, segment 2 is
    compressed to a name card only, and the gap is flagged at the gate.
- brief_refs: channels, dimensions, safe_areas, channel_routing, concepts C1 through C4,
  asset_briefs AB1 through AB5, prompts P1 through P6, instructor profile (cleared facts),
  visual_constants, content_lineup (confirmed lesson names)

---

## Global design tokens (apply to every spec below)

| Token | Value | Usage |
|---|---|---|
| bg | #141414 | All background fills. The canvas starts here. |
| surface | #1A1A1A | Card and panel surfaces. Elevated, not flooded. |
| accent | #009975 | Emerald. Accent bars, CTA chip fills, transition marks. Used as a highlight, not a flood. Never the dominant color in any frame. |
| type-primary | #FFFFFF | Headlines and primary copy on overlays. |
| type-secondary | #D4D4D4 | Supporting lines, lesson name chips, secondary overlay copy. |
| type-muted | #888888 | Tertiary labels, metadata, fine print. |

Numerals: Western only (0 through 9). No Eastern Arabic numerals anywhere in any rendered layer.
RTL: Arabic overlay text layers are set right-to-left. Text anchors for ar slots are right-aligned
and pinned to the right safe-area boundary. Mixed AR and EN within one slot is not used; each
language occupies its own named slot.

---

## DS1. Hero portrait static (C1, source AB1)

Build tool: Canva (primary) or Figma (alternative, same spec).

### Gate status

Build-blocked. OI-1 must be resolved (rights-cleared Bassam Fattouh photography confirmed)
before this spec is executed in build. The spec is complete and ready; the build action is gated.

### Formats and canvas dimensions

| Format ID | Dimensions (px) | Aspect ratio | Primary use |
|---|---|---|---|
| DS1-A | 1080 x 1350 | 4:5 | IG feed, Meta feed ad |
| DS1-B | 1080 x 1920 | 9:16 | IG Story, Reels cover |
| DS1-C | 1600 x 900 | 16:9 | X/Twitter card |
| DS1-D | 1200 x 628 | 1.91:1 | Meta feed ad (alternate) |

### Export settings

All formats: PNG at 72 dpi for digital delivery. Also export JPEG at 90% quality as fallback.
No watermark. No bleed. Actual pixel dimensions as specified above.

### Grid (DS1-A as reference, scale proportionally to other formats)

- Canvas: 1080 x 1350 px, #141414 fill.
- Columns: 12 columns, 20px gutter, 40px outer margin left and right.
- Column width: (1080 - 80 - 220) / 12 = approximately 65px per column.
- Rows: 3 named horizontal zones (see Safe Areas below).

### Safe areas (DS1-A: 1080 x 1350)

| Zone | Y start | Y end | Height | Purpose |
|---|---|---|---|---|
| Upper overlay zone | 0 | 150 | 150px | [ar headline] and [en headline] copy slots |
| Portrait zone | 150 | 1100 | 950px | Bassam Fattouh asset, centered or right-two-thirds dominant |
| Lower overlay zone | 1100 | 1280 | 180px | [ar subline / lesson chips] and [en subline / lesson chips] |
| Accent bar zone | 1280 | 1350 | 70px | Emerald #009975 bar, [ar cta chip] and [en cta chip] |

Left and right text margin inside any overlay: 80px from canvas edge.
No copy or critical visual element within 80px of left or right edge.

Scale for DS1-B (1080 x 1920): upper overlay zone 0 to 200px, lower overlay zone 1650 to 1830px,
accent bar 1830 to 1920px. Portrait zone 200 to 1650px.

Scale for DS1-C (1600 x 900): upper overlay zone 0 to 120px, right safe zone (right-side 400px
column for portrait dominant on left or right). Accent bar: full-width bottom 60px.

Scale for DS1-D (1200 x 628): upper overlay zone 0 to 100px, lower overlay zone 480 to 560px,
accent bar 560 to 628px.

### Layer structure (back to front)

1. Background fill: #141414, full canvas. Locked.
2. Portrait asset: rights-cleared Bassam Fattouh photograph or class still. Placed centered or
   two-thirds dominant (right column bias on AR builds, so face reads correctly in RTL framing).
   No heavy color grading. No skin-tone shift. No fabric color alteration. Subtle vignette at
   edges only if the source photo requires it for clean field separation, using #141414 at 60%
   opacity on a soft feathered edge layer.
3. Lower gradient wash: a vertical gradient from transparent to #141414 at 70% opacity,
   occupying the lower 30% of the canvas. Ensures overlay text is legible without obscuring
   the portrait subject.
4. Emerald accent bar: full-width rectangle, height 8px, #009975, positioned at Y 1272 on
   DS1-A (8px above the bottom of the lower overlay zone). This is the brand anchor, not a
   decorative flood.
5. [ar subline / lesson chips] slot: empty. Type: label chips, 14 to 16px, surface #1A1A1A
   fill, type-secondary #D4D4D4, 8px corner radius, horizontal padding 12px. RTL. Anchored
   right at X 1000 (80px from right edge). Stack vertically if more than one chip. Labeled
   for copywriter-ar fill.
6. [en subline / lesson chips] slot: empty. Same chip style, LTR. Anchored left at X 80.
   Labeled for copywriter-en fill.
7. [ar headline] slot: empty. Type: headline. Recommended type size 36 to 44px. Bold or
   semibold weight. Color #FFFFFF. RTL. Anchored right at X 1000. Positioned in upper overlay
   zone, Y 48 baseline. Labeled for copywriter-ar fill.
8. [en headline] slot: empty. Same size and weight as ar headline. LTR. Anchored left at X 80.
   Y 48 baseline. Labeled for copywriter-en fill. Note: on AR-language variants the ar headline
   slot is primary and the en slot may be hidden; on EN-language variants the reverse applies.
   The designer labels both and the copywriters fill both; language selection is a campaign
   decision made at the human gate.
9. [ar cta chip] slot: empty. Emerald #009975 fill, #FFFFFF type, 12px corner radius,
   horizontal padding 20px, vertical padding 10px. RTL. Positioned in accent bar zone,
   right-aligned at X 1000, vertically centered in the zone. Labeled for copywriter-ar fill.
10. [en cta chip] slot: empty. Same style, LTR. Left-aligned at X 80. Labeled for
    copywriter-en fill.
11. Maharat wordmark: top-left or top-right corner (designer places per art direction of each
    format variant). Small, not competing with the headline. Color #FFFFFF.

### Type scale (DS1-A reference)

| Role | Size | Weight | Color | Notes |
|---|---|---|---|---|
| AR headline | 36 to 44px | Semibold | #FFFFFF | RTL, right-anchored |
| EN headline | 36 to 44px | Semibold | #FFFFFF | LTR, left-anchored |
| AR subline / chip | 14 to 16px | Regular | #D4D4D4 | RTL, chip treatment |
| EN subline / chip | 14 to 16px | Regular | #D4D4D4 | LTR, chip treatment |
| CTA chip | 14px | Semibold | #FFFFFF | On #009975 fill |

Font: the confirmed platform typeface must be used. If not yet confirmed, flag as open item at
build time. Do not substitute an unapproved font.

---

## DS2. Abstract brushstroke still and motion (C2, source AB2)

Build tool: Canva (primary). Motion version: After Effects or Canva animation, following the
motion brief in Prompt P3. No generated-likeness dependency.

### Gate status

Ready to build. No blocked open items for this spec. Proceed after design-qa pass.

### Formats and canvas dimensions

| Format ID | Dimensions (px) | Asset type | Primary use |
|---|---|---|---|
| DS2-A | 1080 x 1350 | Still | IG feed (4:5) |
| DS2-B | 1080 x 1920 | Still | IG Story, Reels cover |
| DS2-C | 1080 x 1920 | Motion, 7 seconds | Reels, TikTok |
| DS2-D | 1080 x 1080 | Still (optional) | Square feed, app push companion |

### Export settings

Still formats: PNG at 72 dpi. Also JPEG 90%.
Motion DS2-C: MP4, H.264, 30fps, no embedded audio (audio is added at production if used).
Overlay text is not baked into the motion file. Overlay text is added as a text layer in the
final composite at build, after copy from copywriter-ar and copywriter-en is confirmed.

### Grid (DS2-A reference: 1080 x 1350)

- Canvas: 1080 x 1350, #141414.
- No column grid needed for abstract composition. Use the following horizontal thirds as guides:
  upper third 0 to 450px, center third 450 to 900px, lower third 900 to 1350px.
- The brushstroke arc occupies the center third vertically, with its leftmost point at
  approximately X 270 and rightmost point at approximately X 810. Upward arc, apex near
  center X 540.

### Safe areas (DS2-A: 1080 x 1350)

| Zone | Y start | Y end | Height | Purpose |
|---|---|---|---|---|
| Upper overlay zone | 0 | 200 | 200px | [ar headline] and [en headline] |
| Stroke composition zone | 200 | 1100 | 900px | Abstract brushstroke. No copy here. |
| Lower overlay zone | 1100 | 1300 | 200px | [ar supporting line] and [en supporting line] |
| CTA zone | 1300 | 1350 | 50px | [ar cta chip] and [en cta chip] |

Text margin: 80px left and right inside any overlay zone.

Scale for DS2-B (1080 x 1920): upper overlay zone 0 to 250px, lower overlay zone 1600 to 1820px,
CTA zone 1820 to 1920px. Stroke zone 250 to 1600px.

Scale for DS2-D (1080 x 1080): upper overlay zone 0 to 160px, lower overlay zone 860 to 1000px,
CTA zone 1000 to 1080px. Stroke zone 160 to 860px.

### Layer structure (back to front, still version)

1. Background fill: #141414, full canvas. Locked.
2. Card plane: rectangle, #1A1A1A, occupying the middle third of the canvas vertically
   (Y 450 to 900 on DS2-A). Full canvas width. This is the grounding surface behind the stroke.
3. Brushstroke element: generated per Prompt P2 description. Single clean curved arc,
   #009975, soft organic texture at edges. Arc geometry: left origin at approximately
   (270, 720), apex near (540, 560), right end at approximately (810, 680). The stroke
   is the single focal element. It must not touch the upper or lower overlay zones.
4. Soft glow: a radial gradient centered on the apex of the stroke, #009975 at 15% opacity,
   radius approximately 200px. Subtle, not flooding. Blending mode: Screen.
5. [ar headline] slot: empty. Type: headline, 36 to 44px, semibold, #FFFFFF. RTL.
   Right-anchored at X 1000. Positioned Y 80 to 160 within upper overlay zone. Labeled for
   copywriter-ar fill.
6. [en headline] slot: empty. Same size, LTR. Left-anchored at X 80. Same Y position.
   Labeled for copywriter-en fill.
7. [ar supporting line] slot: empty. Type: 18 to 22px, regular, #D4D4D4. RTL.
   Right-anchored at X 1000. Y 1130 on DS2-A. Labeled for copywriter-ar fill.
8. [en supporting line] slot: empty. Same size, LTR. Left-anchored X 80. Same Y.
   Labeled for copywriter-en fill.
9. [ar cta chip] slot: empty. #009975 fill, #FFFFFF type, 12px radius, RTL.
   Right-aligned in CTA zone. Labeled for copywriter-ar fill.
10. [en cta chip] slot: empty. Same style, LTR. Left-aligned in CTA zone. Labeled for
    copywriter-en fill.
11. Maharat wordmark: small, top-right corner (or top-left on EN variants). #FFFFFF.

### Motion spec (DS2-C: 1080 x 1920, 7 seconds at 30fps = 210 frames)

| Time | Frames | Action |
|---|---|---|
| 0.0 to 0.4s | 0 to 12 | Hold fully dark #141414 field. No stroke visible. |
| 0.4s to 1.6s | 12 to 48 | Emerald stroke draws on from left to right. Path follows the arc geometry above. Duration 1.2 seconds, as if painted by a confident hand. Stroke opacity builds from 0 to 100%. |
| 1.6s to 3.0s | 48 to 90 | Stroke at full opacity, settled. No movement. Overlay slots for headline and supporting line are visible in this window. |
| 3.0s to 3.4s | 90 to 102 | Soft glow pulse: the #009975 radial gradient intensifies from 15% to 45% opacity, then fades back to 15%. Duration 0.4 seconds. |
| 3.4s to 5.0s | 102 to 150 | Hold. Stroke and overlays remain. |
| 5.0s to 5.4s | 150 to 162 | Fade-out: entire composition fades to #141414, 0.4 seconds. |
| 5.4s to 7.0s | 162 to 210 | Hold clean #141414 black. End. |

Overlay text layers (ar and en headline, ar and en supporting line, ar and en cta chip) appear
at frame 48 with a 15-frame fade-in. They exit with the composition fade at frame 150.
No text is baked into the motion file export. Text layers are applied in the final composite.

### Type scale (DS2-A reference, same as DS1 scale)

Same token table as DS1. Apply proportionally to DS2-D (1080 x 1080): reduce headline to 32
to 38px, supporting line to 16 to 18px.

---

## DS3. Curriculum card feed static and carousel (C3, source AB3)

Build tool: Canva (primary). Carousel via Canva multi-page or Figma frames.

### Gate status

Ready to build. No blocked open items for this spec.

### Formats and canvas dimensions

| Format ID | Dimensions (px) | Asset type | Primary use |
|---|---|---|---|
| DS3-A | 1080 x 1350 | Still, multi-card | IG feed (4:5) |
| DS3-B | 1080 x 1920 | Still, curriculum rundown | IG Story |
| DS3-C-slides 1 to 8 | 1080 x 1080 | Carousel slides | IG and Facebook carousel |
| DS3-D-slides 1 to 8 | 1600 x 900 | Carousel slides | X carousel |

Total carousel slides: 8. Slide 1 is the intro card. Slides 2 through 7 are lesson cards.
Slide 8 is the close card.

Lesson names for slots (confirmed, cleared, in fill order):
- Slide 2: Foundation 101
- Slide 3: The No-Makeup Makeup
- Slide 4: The Day to Night
- Slide 5: The Smokey Eyes
- Slide 6: The Color Glam
- Slide 7: The Graphic Metallic Look

### Export settings

All still formats: PNG at 72 dpi. JPEG 90% fallback.
Carousel: export all 8 slides per format as a numbered sequence. Example: DS3-C-01.png through
DS3-C-08.png.

### Safe areas (DS3-C carousel reference: 1080 x 1080)

All edges: 100px safe area. No copy or critical element outside this boundary.

Inner safe canvas: 880 x 880px, centered.

Scale for DS3-D (1600 x 900): all edges 100px safe area. Inner safe canvas: 1400 x 700px.

Scale for DS3-B story (1080 x 1920): top and bottom 150px. Left and right 80px.

### Grid (DS3-C: 1080 x 1080)

- Canvas: 1080 x 1080, #141414.
- Single card: #1A1A1A rectangle, 880 x 880px, centered at (540, 540). Corner radius 12px.
- Emerald accent: vertical stripe on left edge of card, 4px wide x 880px tall, #009975,
  positioned at X 100 (flush with left edge of card). This is the brand accent, not a flood.
- Card interior padding: 40px all sides within the 880px card. Inner content area: 800 x 800px.
- Text content area: center of card interior, vertically centered within the inner 800px zone.

### Layer structure for a lesson card (back to front, DS3-C slides 2 through 7)

1. Background fill: #141414, full canvas. Locked.
2. Card surface: #1A1A1A rectangle, 880 x 880px, centered. Corner radius 12px.
3. Emerald accent stripe: #009975, 4px x 880px, left edge of card (X 100 to 104, Y 100 to 980).
4. [ar lesson name] slot: empty. Type: 32 to 40px, semibold, #FFFFFF. RTL. Right-aligned
   within the card interior, right edge at X 940 (880 + 100 - 40), vertically centered in
   the card. Labeled for copywriter-ar fill. This is the primary text element for AR variants.
5. [en lesson name] slot: empty. Same size and weight. LTR. Left-aligned within the card
   interior at X 140. Same vertical center. Labeled for copywriter-en fill. On AR-language
   carousel the ar slot is primary and the en slot is hidden or secondary; on EN-language
   carousel the reverse. Designer labels both; language selection is resolved at the human gate.
6. Lesson number indicator (optional, visual only): a small Western numeral in the top-left
   corner of the card interior. Color #009975, 14px, regular weight. This is a visual
   sequence marker, not customer-facing copy. Example: slide 2 shows "2". Confirm with
   creative director before including; if not confirmed, omit and note as open item.

### Layer structure for the intro card (DS3-C slide 1)

1. Background fill: #141414. Locked.
2. Card surface: #1A1A1A rectangle, 880 x 880px, centered. Corner radius 12px.
3. Emerald accent bar: #009975, full card width x 6px, top edge of card (Y 100 to 106).
   (Intro card uses a horizontal top bar instead of the vertical left stripe, to visually
   differentiate it as the entry point.)
4. [ar intro headline] slot: empty. Type: 32 to 40px, semibold, #FFFFFF. RTL.
   Right-aligned within card interior. Vertically positioned upper third of card interior.
   Labeled for copywriter-ar fill.
5. [en intro headline] slot: empty. Same size, LTR. Left-aligned within card interior.
   Same vertical zone. Labeled for copywriter-en fill.

### Layer structure for the close card (DS3-C slide 8)

1. Background fill: #141414. Locked.
2. Card surface: #1A1A1A rectangle, 880 x 880px, centered. Corner radius 12px.
3. Emerald accent bar: #009975, full card width x 6px, bottom edge of card (Y 974 to 980).
   (Close card uses a horizontal bottom bar, mirroring the intro card's top bar, to signal
   conclusion and forward motion.)
4. [ar cta] slot: empty. Type: 28 to 34px, semibold, #FFFFFF. RTL. Right-aligned within
   card interior, vertically centered or slightly above center. Labeled for copywriter-ar fill.
5. [en cta] slot: empty. Same size, LTR. Left-aligned. Same vertical zone. Labeled for
   copywriter-en fill.
6. [ar free chapter callout] slot: empty. Type: 16 to 18px, regular, #D4D4D4. RTL.
   Right-aligned, below the [ar cta] slot, 24px gap between baseline of cta and top of
   callout. Labeled for copywriter-ar fill.
7. [en free chapter callout] slot: empty. Same size, LTR. Left-aligned. Same vertical
   position below the [en cta] slot. Labeled for copywriter-en fill.
8. Emerald CTA chip container (optional): if the close card carries an interactive chip
   element (platform-dependent), a #009975 filled rounded rectangle (height 44px,
   corner radius 8px, width auto per copy) sits below the [ar free chapter callout] /
   [en free chapter callout] slot with a 20px gap. Confirm with lifecycle-architect
   whether this is applicable for the carousel format on each platform.

### Multi-card still spec (DS3-A: 1080 x 1350)

4 cards in vertical procession on the #141414 field.

| Card | Y start | Y end | Height | Card width | Accent |
|---|---|---|---|---|---|
| Card 1 (lead, emerald accent) | 80 | 380 | 300px | 960px, centered | #009975 top bar, 4px |
| Card 2 | 420 | 690 | 270px | 920px, centered | No accent |
| Card 3 | 730 | 1000 | 270px | 920px, centered | No accent |
| Card 4 | 1040 | 1280 | 240px | 880px, centered | No accent |

Each card: #1A1A1A fill, corner radius 10px. Card interiors are empty for overlay.
The procession is unhurried. Space between cards is breathing room, not filler.
Left and right margins on cards: 60px from canvas edge for Card 1, scaling inward for
Cards 2 through 4 to create a subtle depth or stagger effect.

Copy overlay slots on DS3-A (one ar and one en slot per card, same structure as DS3-C
lesson card slots). Copywriters fill in priority order: Foundation 101, No-Makeup Makeup,
Day to Night, Smokey Eyes.

### Type scale (DS3-C reference: 1080 x 1080)

| Role | Size | Weight | Color | Notes |
|---|---|---|---|---|
| AR lesson name | 32 to 40px | Semibold | #FFFFFF | RTL, right-anchored inside card |
| EN lesson name | 32 to 40px | Semibold | #FFFFFF | LTR, left-anchored inside card |
| AR intro headline | 32 to 40px | Semibold | #FFFFFF | RTL |
| EN intro headline | 32 to 40px | Semibold | #FFFFFF | LTR |
| AR / EN CTA | 28 to 34px | Semibold | #FFFFFF | per language |
| AR / EN free chapter callout | 16 to 18px | Regular | #D4D4D4 | per language |

Scale type proportionally for DS3-D (1600 x 900). Headline: 36 to 44px. Lesson name: 36
to 44px. Callout: 18 to 20px.

---

## DS4. Class trailer master cut video (C4, source AB4)

Build tool: NLE editor (designer's confirmed toolchain, Premiere Pro or equivalent).
Canva for static end card matte element.

### Gate status

Build-blocked. OI-1 and OI-2 must both be resolved (rights-cleared class footage confirmed,
timecodes identified for segments 1 and 4) before this spec is executed. The spec is complete;
the build action is gated.

### Formats and canvas dimensions

| Format ID | Dimensions (px) | Duration | Primary use |
|---|---|---|---|
| DS4-A | 1080 x 1920 | 35s master | Reels, TikTok, Story primary |
| DS4-B | 1920 x 1080 | 35s master | YouTube |
| DS4-C | 1080 x 1080 | 35s master | Square feed |
| DS4-D | 1080 x 1920 | 15s cut | Paid pre-roll |
| DS4-E | 1080 x 1920 | 30s cut | Organic social short version |

DS4-D and DS4-E are repurposed from DS4-A. Method: manual edit until OI-3 (Blotato credential)
is resolved. When OI-3 is resolved, the Blotato workflow handles the repurpose cuts.

### Export settings

MP4, H.264. DS4-A and DS4-B: 30fps. DS4-A, DS4-C, DS4-D, DS4-E: 1080px wide.
DS4-B: 1920px wide. No embedded subtitles in the video file; subtitles added at platform
upload if required by platform settings. Overlay text slots are applied in post as a
compositor text layer, not baked into the exported video file.

### Safe areas (DS4-A: 1080 x 1920)

| Zone | Y start | Y end | Height | Reserved for |
|---|---|---|---|---|
| Top overlay zone | 0 | 200 | 200px | Platform UI, top nav |
| Active overlay zone (upper) | 200 | 700 | 500px | Hook, authority, lesson name overlays |
| Footage zone | 200 | 1620 | 1420px | Full-frame footage. Overlays float above. |
| Active overlay zone (lower) | 1620 | 1820 | 200px | Close line, end card copy |
| Bottom UI zone | 1820 | 1920 | 100px | Platform bottom nav, safe |

Left and right overlay text margin: 80px from canvas edge.

Safe areas for DS4-B (1920 x 1080): left and right 160px reserved. Top and bottom 80px.
Overlay text lives within the 1600 x 920px inner area.

### Segment timing and overlay slot map (DS4-A master, 35 seconds at 30fps)

#### Segment 1: Hook (0 to 5 seconds, frames 0 to 150)

Visual: opening moment from cleared class footage. Teaching action, brush movement, or
direct-to-camera instructor moment. Real instructor energy. #141414 letterbox or vignette
at the very first frame (1 to 2 frames) then cut to footage.

Footage slot: [footage timecode segment 1]. OPEN. Designer identifies from actual footage
once footage is confirmed (OI-2).

Overlay slots (appear at frame 12, fade in over 8 frames):
- [ar hook line]: type 36 to 42px, semibold, #FFFFFF, RTL, right-anchored at X 1000,
  positioned Y 250. Labeled for copywriter-ar fill.
- [en hook line]: same size, LTR, left-anchored X 80, Y 250. Labeled for copywriter-en fill.

Overlay exits: fade out over 8 frames at frame 130.

#### Segment 2: Authority card (5 to 10 seconds, frames 150 to 300)

Visual: full-screen #141414 matte card. Generated via Canva as a static card exported and
inserted as a clip. No footage. The card is clean, dark, with the Maharat wordmark small
and centered.

Overlay slots (appear at frame 165, fade in over 10 frames):
- [ar authority line]: type 28 to 34px, regular, #FFFFFF, RTL, right-anchored at X 1000,
  Y 880 (vertically centered on a 1080 x 1920 canvas, offset slightly above center).
  Content must use only cleared facts from profile.md: "leading regional makeup artist,
  teaches makeup on Maharat." No awards, no figures, no accreditation. If cleared facts are
  insufficient, slot is compressed to a name card only. Flag at gate per OI-5.
  Labeled for copywriter-ar fill.
- [en authority line]: same size and position logic, LTR, left-anchored X 80, Y 880.
  Labeled for copywriter-en fill.
- [ar instructor name]: type 24 to 28px, semibold, #009975, RTL, right-anchored X 1000,
  Y 940. The name set in the slot is the confirmed public name "بسام فتوح". Labeled for
  copywriter-ar; the value is the confirmed name, no invention needed.
- [en instructor name]: type 24 to 28px, semibold, #009975, LTR, X 80, Y 940. Value is
  "Bassam Fattouh". Labeled for copywriter-en.

Overlay exits: fade out over 10 frames at frame 285. Segment cuts to footage at frame 300.

#### Segment 3: Curriculum scroll (10 to 22 seconds, frames 300 to 660)

Visual: editorial footage from the class. #141414 transition mattes (8 frames) between
each lesson beat. Emerald #009975 accent mark (a 4px horizontal line, 320px wide, centered
horizontally) animates on between each slot, appearing over the transition matte for 6
frames then fading.

4 lesson beats. Each beat spans approximately 3 seconds (90 frames).

Beat 1 (frames 300 to 390): Foundation 101.
- [ar lesson 1] slot: type 32 to 38px, semibold, #FFFFFF, RTL, right-anchored X 1000, Y 920.
  Labeled for copywriter-ar fill.
- [en lesson 1] slot: same size, LTR, X 80, Y 920. Labeled for copywriter-en fill.
- Overlay appears at frame 312, exits at frame 378.
- #141414 transition matte, frames 378 to 390.

Beat 2 (frames 390 to 480): The No-Makeup Makeup.
- [ar lesson 2] slot: same type spec as beat 1. RTL. Labeled for copywriter-ar fill.
- [en lesson 2] slot: LTR. Labeled for copywriter-en fill.
- Same timing pattern: appear at frame 402, exit frame 468. Transition frames 468 to 480.

Beat 3 (frames 480 to 570): The Smokey Eyes.
- [ar lesson 3] slot: same spec. RTL. Labeled for copywriter-ar fill.
- [en lesson 3] slot: LTR. Labeled for copywriter-en fill.
- Appear frame 492, exit frame 558. Transition frames 558 to 570.

Beat 4 (frames 570 to 660): The Graphic Metallic Look.
- [ar lesson 4] slot: same spec. RTL. Labeled for copywriter-ar fill.
- [en lesson 4] slot: LTR. Labeled for copywriter-en fill.
- Appear frame 582, exit frame 648. Transition frames 648 to 660.

If pacing allows additional beats (The Day to Night, The Color Glam), each adds 2.5 to 3
seconds. Total segment 3 duration extends accordingly and segment 4 start shifts. Designer
adjusts once actual footage pacing is known. Note the additional slots if used:
- [ar lesson 5], [en lesson 5]: The Day to Night.
- [ar lesson 6], [en lesson 6]: The Color Glam.

#### Segment 4: Closing moment (22 to 30 seconds, frames 660 to 900)

Visual: closing instructor moment from footage. Invitation feel, not pitch. Real class energy.
Footage slot: [footage timecode segment 4]. OPEN. Designer identifies from actual footage
once confirmed (OI-2).

Overlay slots (appear at frame 672, fade in over 10 frames):
- [ar close line]: type 30 to 36px, semibold, #FFFFFF, RTL, right-anchored X 1000, Y 1700
  (lower third of 1920px canvas, above UI safe zone). Labeled for copywriter-ar fill.
- [en close line]: same size, LTR, X 80, Y 1700. Labeled for copywriter-en fill.

Overlay exits at frame 888.

#### Segment 5: End card (30 to 35 seconds, frames 900 to 1050)

Visual: end card matte from Prompt P6 direction. Full-frame #141414. Maharat wordmark
centered in upper two-thirds. Thin emerald #009975 horizontal accent bar, 6px tall, full
canvas width, positioned at Y 1824 on 1920px canvas (lower fifth).

End card is a static clip, built separately in Canva per Prompt P6 and inserted as a
3-second clip (frames 960 to 1050 hold the matte; frames 900 to 960 are a 2-second fade
from footage to matte).

Overlay slots (appear at frame 960, fade in over 15 frames):
- [ar end card copy]: type 26 to 30px, regular then semibold for the class title portion,
  #FFFFFF, RTL, right-anchored X 1000. Two lines: line 1 the class name, line 2 the
  platform CTA. Y 850 for line 1, Y 910 for line 2. No price, no promo. Labeled for
  copywriter-ar fill.
- [en end card copy]: same structure, LTR, X 80. Same Y positions. Labeled for
  copywriter-en fill.

### Color treatment notes for footage

Footage grade: warm-neutral. Not cold or desaturated, not oversaturated. Lift the blacks
slightly (target near-black #141414 at 15 to 20 IRE) to integrate smoothly with the
#141414 matte cards. Do not shift skin tone or fabric color. LUT selection to be confirmed
by designer once footage is reviewed.

### 15-second cut spec (DS4-D)

Includes: Segment 1 (hook, 0 to 5s) plus Segment 3 excerpt (2 lesson beats, 5 to 12s) plus
Segment 5 end card condensed (12 to 15s). All overlay slots carry through from master.
Method: manual edit until OI-3 resolved. When OI-3 resolved, Blotato workflow handles the cut.

### 30-second cut spec (DS4-E)

Includes: Segments 1 through 4 at full pacing, Segment 5 condensed to 2 seconds.
All overlay slots carry through. Method: same as DS4-D.

---

## DS5. Email header banner (V4, source AB5)

Build tool: Canva. No separate generation required.

### Gate status

Ready to spec. Source asset is a crop from DS1 (if OI-1 is resolved) or from DS2 (fallback,
available now). The fallback version (DS2 source) is ready to build. The DS1-source version
is blocked pending OI-1.

### Formats and canvas dimensions

| Format ID | Dimensions (px) | Responsive crop | Primary use |
|---|---|---|---|
| DS5-A | 1200 x 480 | Desktop email header | Emails E1 through E4 |
| DS5-A-mobile | 600 x 240 | Center-safe crop of DS5-A | Mobile email rendering |

### Export settings

PNG at 72 dpi. Also export JPEG at 85% quality for email delivery (file size control).
Total file target: under 200KB for JPEG version to maintain email load performance.

### Safe area

Center 60% horizontally (X 240 to X 960 on a 1200px canvas). Top and bottom 60px.
All critical content within this inner zone.

### Layer structure (back to front)

1. Background fill: #141414, full 1200 x 480px canvas. Locked.
2. Source asset: either a crop from DS1 (rights-cleared portrait, centered on the right half
   of the banner, fading to #141414 at the left edge using a horizontal gradient overlay at
   70% opacity) or the DS2 abstract brushstroke (centered, scaled to fill the middle third
   of the banner height, with left and right field remaining clean #141414).
3. Emerald bottom border: #009975, 3px tall, full canvas width, Y 477 to 480. Brand anchor.
4. [ar email header line] slot: empty. Type: 22 to 28px, semibold, #FFFFFF. RTL.
   Right-anchored at X 960 (right boundary of safe zone), vertically centered at Y 200 to
   260. Labeled for copywriter-ar fill. Applied in email build by lifecycle-architect.
5. [en email header line] slot: empty. Same size, LTR. Left-anchored X 240. Same Y range.
   Labeled for copywriter-en fill. Applied in email build by lifecycle-architect.
6. Maharat wordmark: small, top-right within the safe zone. #FFFFFF.

Note: copy overlay slots for the email header are applied in the email build, not in the
exported image file. The exported image is text-free. lifecycle-architect applies the
overlay in the email template.

---

## Asset sourcing summary

| Asset ref | Source type | Rights basis | Status |
|---|---|---|---|
| DS1 photography | Real Bassam Fattouh photograph or class still | Rights-cleared Maharat library | BLOCKED: OI-1 open |
| DS2 brushstroke | Generated per Prompt P2 / P3 direction | Maharat-generated, no likeness | Ready |
| DS3 curriculum cards | Generated per Prompt P4 / P5 direction | Maharat-generated, no likeness | Ready |
| DS4 footage | Real rights-cleared Maharat class footage | Rights-cleared Maharat library | BLOCKED: OI-2 open |
| DS4 end card matte | Canva build per Prompt P6 | Maharat-owned, no photography | Ready |
| DS5 header | Crop from DS1 or DS2 | Same as source | DS1 source blocked; DS2 fallback ready |

No generated likeness of Bassam Fattouh is used anywhere. No Arabic text is baked into any
generated image layer. All copy is overlaid by the designer at build time from QA-passed
copywriter-ar and copywriter-en output.

---

## Copy overlay slot index (complete, all specs)

All slots below are empty. Language label is the routing destination. Slots marked RTL require
right-to-left text direction in the build tool. Slots marked LTR are left-to-right.

### DS1 slots

| Slot label | Spec | Zone | Direction | Routes to |
|---|---|---|---|---|
| [ar headline] | DS1-A through DS1-D | Upper overlay | RTL | copywriter-ar |
| [en headline] | DS1-A through DS1-D | Upper overlay | LTR | copywriter-en |
| [ar subline / lesson chips] | DS1-A through DS1-D | Lower overlay | RTL | copywriter-ar |
| [en subline / lesson chips] | DS1-A through DS1-D | Lower overlay | LTR | copywriter-en |
| [ar cta chip] | DS1-A through DS1-D | Accent bar | RTL | copywriter-ar |
| [en cta chip] | DS1-A through DS1-D | Accent bar | LTR | copywriter-en |

### DS2 slots

| Slot label | Spec | Zone | Direction | Routes to |
|---|---|---|---|---|
| [ar headline] | DS2-A through DS2-D | Upper overlay | RTL | copywriter-ar |
| [en headline] | DS2-A through DS2-D | Upper overlay | LTR | copywriter-en |
| [ar supporting line] | DS2-A through DS2-D | Lower overlay | RTL | copywriter-ar |
| [en supporting line] | DS2-A through DS2-D | Lower overlay | LTR | copywriter-en |
| [ar cta chip] | DS2-A through DS2-D | CTA zone | RTL | copywriter-ar |
| [en cta chip] | DS2-A through DS2-D | CTA zone | LTR | copywriter-en |

### DS3 slots (carousel, per slide)

| Slot label | Slide(s) | Zone | Direction | Routes to |
|---|---|---|---|---|
| [ar intro headline] | Slide 1 | Upper zone | RTL | copywriter-ar |
| [en intro headline] | Slide 1 | Upper zone | LTR | copywriter-en |
| [ar lesson name] | Slides 2 through 7 | Card center | RTL | copywriter-ar |
| [en lesson name] | Slides 2 through 7 | Card center | LTR | copywriter-en |
| [ar cta] | Slide 8 | Center-upper | RTL | copywriter-ar |
| [en cta] | Slide 8 | Center-upper | LTR | copywriter-en |
| [ar free chapter callout] | Slide 8 | Below cta | RTL | copywriter-ar |
| [en free chapter callout] | Slide 8 | Below cta | LTR | copywriter-en |

### DS4 slots (video trailer, by segment)

| Slot label | Segment | Direction | Routes to |
|---|---|---|---|
| [ar hook line] | Segment 1 | RTL | copywriter-ar |
| [en hook line] | Segment 1 | LTR | copywriter-en |
| [ar authority line] | Segment 2 | RTL | copywriter-ar |
| [en authority line] | Segment 2 | LTR | copywriter-en |
| [ar instructor name] | Segment 2 | RTL | copywriter-ar |
| [en instructor name] | Segment 2 | LTR | copywriter-en |
| [ar lesson 1] | Segment 3, beat 1 | RTL | copywriter-ar |
| [en lesson 1] | Segment 3, beat 1 | LTR | copywriter-en |
| [ar lesson 2] | Segment 3, beat 2 | RTL | copywriter-ar |
| [en lesson 2] | Segment 3, beat 2 | LTR | copywriter-en |
| [ar lesson 3] | Segment 3, beat 3 | RTL | copywriter-ar |
| [en lesson 3] | Segment 3, beat 3 | LTR | copywriter-en |
| [ar lesson 4] | Segment 3, beat 4 | RTL | copywriter-ar |
| [en lesson 4] | Segment 3, beat 4 | LTR | copywriter-en |
| [ar lesson 5] | Segment 3, beat 5 (if pacing allows) | RTL | copywriter-ar |
| [en lesson 5] | Segment 3, beat 5 (if pacing allows) | LTR | copywriter-en |
| [ar lesson 6] | Segment 3, beat 6 (if pacing allows) | RTL | copywriter-ar |
| [en lesson 6] | Segment 3, beat 6 (if pacing allows) | LTR | copywriter-en |
| [ar close line] | Segment 4 | RTL | copywriter-ar |
| [en close line] | Segment 4 | LTR | copywriter-en |
| [ar end card copy] | Segment 5 | RTL | copywriter-ar |
| [en end card copy] | Segment 5 | LTR | copywriter-en |
| [footage timecode segment 1] | Segment 1 | Build ref | designer |
| [footage timecode segment 4] | Segment 4 | Build ref | designer |

### DS5 slots

| Slot label | Applied by | Direction | Routes to |
|---|---|---|---|
| [ar email header line] | In email build, not in image export | RTL | copywriter-ar, lifecycle-architect |
| [en email header line] | In email build, not in image export | LTR | copywriter-en, lifecycle-architect |

---

## Design QA verdict

Gate: design_qa
Date: 2026-06-05
Produced by: designer

### Check 1: RTL correct

Result: PASS

All Arabic overlay slots are labeled RTL with right-side text anchors. No mixed AR and EN
text within a single slot. Slots are distinct by language and direction. In each spec, the
ar slot anchor is at the right safe-area boundary and the en slot anchor is at the left.
No Arabic text is authored in any generated image layer. Copy is overlaid at build time.

### Check 2: Safe areas

Result: PASS

Each format carries explicit safe-area measurements. Platform UI zones (top 200px, bottom
100px on 9:16 Story and Reels formats) are clear of critical overlay content. On DS1 and
DS4, the lower gradient wash and matte transitions ensure readability without elements
bleeding into platform chrome. DS3 carousel cards maintain 100px all-edge safe area. DS5
email header reserves 60px top and bottom and restricts content to the center 60% of the
canvas width.

### Check 3: Western numerals only

Result: PASS

No numeral characters appear in any generated layer of any spec. The only numeral reference
in the spec is the optional sequence marker on DS3 lesson cards, which uses a Western numeral
(1 through 6) in #009975 as a visual indicator. All overlay copy slots are empty, labeled,
and not yet filled. The gate instruction to copywriter-ar and copywriter-en explicitly
requires Western numerals (0 through 9) in all filled copy. Eastern Arabic numerals and
tatweel are prohibited by the global token rules at the top of this document.

### Check 4: Visual constants applied

Result: PASS

Every spec uses #141414 as the canvas fill. #1A1A1A is used as the card surface. #009975
is used as a highlight accent only (bars, stripe, glow, chip fill, transition mark, accent
line) and does not flood any frame. Type on overlays is #FFFFFF (primary) and #D4D4D4
(secondary). No spec uses #009975 as a background or dominant color.

### Check 5: Premium and uncluttered

Result: PASS

DS1: single focal point (the instructor portrait), generous field above and below, one thin
accent bar, no competing graphic elements.
DS2: single brushstroke on a clean dark field. One focal element. No clutter.
DS3: cards with generous interior padding, even breathing room between cards in the multi-card
still, and a clean single-element card in the carousel. No stacking, no busy patterns.
DS4: segment structure is deliberate, each card or footage moment is single-purpose. The
curriculum scroll uses one lesson name per beat, not simultaneous text lines.
DS5: slim banner, minimal, text-free as an image, copy applied at email build.

### Check 6: No Arabic text baked into any generated image

Result: PASS

All generated layers (DS2 via Prompt P2 and P3, DS3 via Prompt P4 and P5, DS4 end card
matte via Prompt P6) are specified as text-free. DS1 uses a real photograph with no text
baked in. The prompts referenced in the creative-package all explicitly state no text baked
into the image. Every copy element is an overlay slot, applied at build time from QA-passed
copy provided by copywriter-ar and copywriter-en.

### Overall design QA verdict: PASS

All six checks pass. No fix list required.

Open items flagged at this gate (not design-qa failures; procedural blockers for build):
- OI-1: DS1 and DS4 are build-blocked. The specs are complete; the build awaits confirmed
  rights-cleared assets.
- OI-2: DS4 footage timecodes are open. The [footage timecode segment 1] and [footage
  timecode segment 4] slots are build references, not copy slots, and will be resolved by
  the designer when footage is reviewed.
- OI-3: Blotato credential open. Repurpose cuts (DS4-D, DS4-E) built manually until resolved.
- OI-4: No promo confirmed. No price chip slot exists. If a promo is confirmed, specs DS1 and
  DS3 require a price-chip slot addition before build proceeds.
- OI-5: C4 segment 2 authority content limited to cleared profile facts. The slot is labeled
  and the constraint is documented. Copywriter-ar and copywriter-en must not exceed cleared
  facts when filling the [ar authority line] and [en authority line] slots.
- Font confirmation open: this spec references the confirmed platform typeface without naming
  a specific font family, because no confirmed font name is available in the brief or context
  files. The designer must confirm the font before build. This is flagged as a build gate item.

Next gate: brand-qa-reviewer.
Human gate: nothing builds, publishes, or spends until Ahmed approves. All open items above
are surfaced at the human gate.
