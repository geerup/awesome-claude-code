# Design specs: Skill Paths first-time soft launch

Owned by designer. Produced from: creative-package.md (creative-director, stream 3) and
conversion-package.md (conversion-engineer, stream 6). Nothing here publishes, sends, or spends.
All build and export actions are behind the human gate.

No em dashes. Western numerals. Arabic is always an overlay slot, never baked into a generated
image. No rendered Skill Path titles, no app UI screenshots, no invented product names in any layer.
Visual constants: #141414 background, #1A1A1A card surfaces, #009975 emerald accent.

---

## Envelope

- campaign_id: 2026-07-skill-paths-soft-launch
- produced_by: designer
- stream: 3 creative production
- status: draft
- qa:
  - skill_eval: complete (self-check, see pre-handoff checklist)
  - arabic_qa: na (no Arabic authored here; all AR slots route to copywriter-ar)
  - brand_qa: pending (routes to brand-qa-reviewer after design-qa passes)
  - design_qa: pass (verdict recorded in the design-qa section at the end of this file)
- brief_refs:
  - creative-package.md: concepts C1 to C4, prompts P1 to P6, asset briefs AB-01 to AB-09, V1
  - conversion-package.md: landing page sections A to F, layout spec 1.3, RTL requirements 1.4
  - brand-voice.md: visual constants, mechanical rules, RTL requirement
  - CLAUDE.md: hard rules, guardrails
- open_items:
  - build-tool-not-approved: Canva MCP is on the allowlist. Figma is under build-vs-buy-eval.
    Live build and export actions are blocked until the confirmed tool clears the human gate.
  - font-not-confirmed: the Arabic typeface and Latin typeface are not confirmed. Type scale
    below uses size relationships and weight roles; the actual font families are open items.
    Do not bake a font name into the spec until Ahmed confirms the stack.
  - copy-slots-unfilled: all [AR-*] and [EN-*] slots are empty and route to their respective
    copywriters. No slot content is authored here.
  - approved-imagery-not-confirmed: all assets use abstract emerald-on-near-black motifs per the
    open item in the creative-package. No approved product or brand imagery beyond brand constants
    is referenced until confirmed.
  - seat-cap-not-confirmed: the [AR-SUBHEAD-RETARGET] and [EN-SUBHEAD-RETARGET] "limited seats"
    variant in AB-03 is a blocked overlay layer. It must not go live until the seat cap is
    confirmed as real.
  - gate-platform-not-confirmed: [LINK-STICKER-ZONE] and [LINK-OR-CTA-UNIT] slots across AB-05
    and V1 are marked blocked. The actual gate link is wired at publish time by the social media
    operator, not in this spec.
  - video-production-resourcing: motion specs AB-04 and V1 require a motion-capable production
    pass. Execution is behind the human gate.

---

## Section 1. Global design system tokens

These tokens apply to every asset in this campaign. They are the only source of truth for color,
spacing units, and type role names. Individual asset specs reference them by token name.

### 1.1 Color tokens

| Token | Hex | Role |
|---|---|---|
| color-bg | #141414 | Primary background, near-black field |
| color-surface | #1A1A1A | Card and panel surfaces, sits on color-bg |
| color-accent | #009975 | Emerald. Accent only, never flood. Spark, streak markers, ring, threshold glow, CTA button |
| color-accent-dim | #00684f | Dimmed emerald. Paused or unlit state in streak motif (C2/C4 usage only) |
| color-text-primary | #F5F5F5 | Primary overlay text on color-bg or color-surface |
| color-text-secondary | #A0A0A0 | Secondary or supporting overlay text |
| color-cta-label | #FFFFFF | White text on color-accent CTA button |

### 1.2 Spacing unit

Base unit: 8 px. All margins, padding, and grid gutters are multiples of 8. Generous negative
space is the rule: minimum margin from any copy overlay to the nearest edge is 2 base units
(16 px) inside the safe area.

### 1.3 Type scale (role-based, font families are open items)

All sizes in px at 1x. Export at 2x for social and email. For video, use the 1080-wide master;
scale notes apply per-asset below.

| Role | Size (px) | Weight | Line height | Notes |
|---|---|---|---|---|
| display | 48 | Bold | 1.15 | Large feed headline, high-impact moment |
| headline | 36 | Bold | 1.2 | Standard headline overlay slot |
| subhead | 24 | Regular or Medium | 1.4 | Supporting line, subhead slots |
| body | 18 | Regular | 1.6 | Body text, used on landing page only |
| label | 14 | Medium | 1.3 | CTA chip labels, captions |
| caption | 12 | Regular | 1.4 | Footer and legal lines only |

Arabic text in AR overlay slots uses the same size scale. RTL direction is set at the layer
level. Arabic font must support RTL shaping without errors. The specific typeface is an open item.

### 1.4 Safe area nomenclature

"Safe area" means the inset rectangle within which all overlay text, brand marks, and CTA chips
must sit. Nothing critical appears outside this inset. Platform UI, crop, and bleed happen in
the outer margin. Coordinates are from the top-left corner of the full canvas at 1x.

---

## Section 2. Static asset specs (AB-01 to AB-03, AB-05 to AB-09)

---

### AB-01. Concept C1. Organic feed, single image. Instagram and LinkedIn.

**Build tool:** Canva (pending approval) or Figma equivalent.

**Canvas:** 1080 x 1350 px at 72 dpi for social delivery. Export at 2x (2160 x 2700 px) for
retina quality. Color space: sRGB.

**Safe area:** 960 x 1150 px inset. Origin point: 60 px from left, 100 px from top.
- Top clear zone: 0 to 100 px from top. No overlays here.
- Bottom clear zone: 1250 to 1350 px from top. No overlays here.
- Side clear zones: 0 to 60 px from left, 1020 to 1080 px from right. No overlays here.

**Grid:** 12-column grid, 60 px outer margins, 20 px gutters. Column width: 70 px.

**Layer stack (bottom to top):**

| Layer index | Layer name | Contents | Color | Notes |
|---|---|---|---|---|
| 1 | bg | Full-canvas rectangle | color-bg (#141414) | Base layer, no stroke |
| 2 | card-panel | Rectangle, lower third: 1080 x 450 px, top edge at y=900 | color-surface (#1A1A1A) | Slight depth separation, no border radius or border |
| 3 | image-render | Text-free generated image per prompt P1 | Spans full canvas or anchored to card-panel | Abstract emerald spark and path. No text baked in. No UI. See prompt P1 in creative-package.md |
| 4 | brand-mark | Maharat logo mark | color-text-primary (#F5F5F5) or white | [BRAND-MARK] slot. Positioned: lower-right of safe area. Bottom edge at y=1220, right edge at x=920. Width: 80 px. |
| 5 | ar-headline | [AR-HEADLINE] overlay slot | color-text-primary (#F5F5F5) | See copy-overlay slot table below. |
| 6 | en-headline | [EN-HEADLINE] overlay slot | color-text-primary (#F5F5F5) | EN-variant asset only. |

**Copy-overlay slot table:**

| Slot index | Slot ID | Zone | Direction | Routing | Type role | Max lines | Position within safe area |
|---|---|---|---|---|---|---|---|
| 1 | [AR-HEADLINE] | Upper third, y: 120 to 320 px from top | RTL | copywriter-ar | headline (36 px bold) | 2 | Right-aligned, right edge at x=1020, top edge at y=140 |
| 2 | [EN-HEADLINE] | Upper third, y: 120 to 320 px from top | LTR | copywriter-en | headline (36 px bold) | 2 | Left-aligned, left edge at x=60, top edge at y=140. EN-variant asset only. |
| 3 | [BRAND-MARK] | Lower right, inside safe area | n/a | designer | n/a | n/a | Bottom edge at y=1220, right edge at x=1020 |

**RTL note:** AR overlay slot layers must have text direction set to RTL. Text alignment: right.
The AR and EN headline slots occupy the same zone. They appear on separate asset exports: one AR
master, one EN variant. They do not appear simultaneously on the same canvas.

**Export:** one AR master (AR-HEADLINE visible, EN-HEADLINE layer hidden), one EN variant (EN
layer visible, AR layer hidden). File names: AB-01-ar.png and AB-01-en.png.

**Design notes:** generous negative space in the lower two-thirds and the right half of the upper
field. The emerald spark and path are the focal point. No secondary element competes with the
path motif. No CTA chip on this asset: destination is profile follow at this arc stage.

---

### AB-02. Concept C1. Organic feed, single image. X (Twitter).

**Build tool:** Canva or Figma.

**Canvas:** 1600 x 900 px. Export 2x: 3200 x 1800 px. sRGB.

**Safe area:** 1400 x 720 px inset. Origin: 100 px from left, 90 px from top.
- Top clear: 0 to 90 px.
- Bottom clear: 810 to 900 px.
- Side clear: 0 to 100 px left, 1500 to 1600 px right.

**Grid:** 12-column, 100 px outer margins, 24 px gutters. Column width: 92 px.

**Layer stack (bottom to top):**

| Layer index | Layer name | Contents | Color | Notes |
|---|---|---|---|---|
| 1 | bg | Full-canvas rectangle | color-bg (#141414) | |
| 2 | card-panel | Rectangle, lower third: 1600 x 300 px, top edge at y=600 | color-surface (#1A1A1A) | Premium depth layer |
| 3 | image-render | Text-free render per P1, recomposed for 16:9 | Spans full canvas | Spark at left-center. Path line traces right across lower third. No text baked in. |
| 4 | brand-mark | [BRAND-MARK] | color-text-primary | Lower-right safe area. Bottom y=770, right x=1480. Width 80 px. |
| 5 | ar-headline | [AR-HEADLINE] | color-text-primary | AR master. |
| 6 | en-headline | [EN-HEADLINE] | color-text-primary | EN variant. |

**Copy-overlay slot table:**

| Slot index | Slot ID | Zone | Direction | Routing | Type role | Max lines | Position within safe area |
|---|---|---|---|---|---|---|---|
| 1 | [AR-HEADLINE] | Upper left area (RTL: reading start), y: 110 to 250 px | RTL | copywriter-ar | headline (36 px bold) | 2 | Right-aligned block, right edge at x=1480, top y=110 |
| 2 | [EN-HEADLINE] | Upper left area, y: 110 to 250 px | LTR | copywriter-en | headline (36 px bold) | 2 | Left-aligned, left x=120, top y=110. EN variant only. |
| 3 | [BRAND-MARK] | Lower right | n/a | designer | n/a | n/a | Bottom y=770, right x=1480 |

**Export:** AB-02-ar.png, AB-02-en.png.

**Design note:** the path line extends across the horizontal field per the 16:9 recomposition.
The spark is still the origin. Clear space in the upper half hosts the headline overlay. Platform
UI (Twitter card cropping) happens at the outer margins; the spark-to-path composition and all
overlays clear the safe area on every side.

---

### AB-03. Concept C2. Paid social, static ad. Instagram, Meta, TikTok image.

**Build tool:** Canva or Figma.

**Primary canvas:** 1080 x 1350 px. Secondary canvas: 1080 x 1080 px.

**Safe area (4:5 primary):** 960 x 1150 px inset. Origin: 60 px from left, 100 px from top.
Bottom 200 px of the canvas (y=1150 to y=1350) reserved for the platform-native CTA button.
No overlay text or brand mark enters this bottom 200 px band.

**Safe area (1:1 secondary):** 960 x 880 px inset. Origin: 60 px left, 100 px top. Bottom 200 px
reserved for platform CTA.

**Grid:** same 12-column, 60 px outer margins as AB-01.

**Layer stack (bottom to top):**

| Layer index | Layer name | Contents | Color | Notes |
|---|---|---|---|---|
| 1 | bg | Full-canvas rectangle | color-bg (#141414) | |
| 2 | streak-track | Thin horizontal bar, 1080 x 24 px, centered vertically at y=675 (4:5) | color-surface (#1A1A1A) | Slightly recessed track behind the marker row |
| 3 | image-render | Text-free render per P2. Streak row of lit and unlit markers, centered | Per prompt P2 palette | No text, no numbers, no labels baked in |
| 4 | brand-mark | [BRAND-MARK] | color-text-primary | Lower-right safe area, above the platform-CTA reserved zone. Bottom y=1130, right x=1020. Width 80 px. |
| 5 | ar-headline | [AR-HEADLINE] | color-text-primary | Acquisition variant. Upper third. AR master. |
| 6 | en-headline | [EN-HEADLINE] | color-text-primary | EN variant. |
| 7 | ar-subhead-retarget | [AR-SUBHEAD-RETARGET] | color-text-secondary | Retargeting variant layer. Switchable. BLOCKED until seat-cap confirmed. |
| 8 | en-subhead-retarget | [EN-SUBHEAD-RETARGET] | color-text-secondary | Retargeting variant layer. Switchable. BLOCKED until seat-cap confirmed. |

**Copy-overlay slot table:**

| Slot index | Slot ID | Zone | Direction | Routing | Type role | Max lines | Position within safe area | Status |
|---|---|---|---|---|---|---|---|---|
| 1 | [AR-HEADLINE] | Upper third, y: 120 to 300 px | RTL | copywriter-ar | headline (36 px bold) | 2 | Right-aligned, right x=1020, top y=140 | Active |
| 2 | [AR-SUBHEAD-RETARGET] | Below headline, y: 310 to 390 px | RTL | copywriter-ar | subhead (24 px) | 1 | Right-aligned, right x=1020, top y=320 | BLOCKED: seat-cap open item |
| 3 | [EN-HEADLINE] | Upper third, y: 120 to 300 px | LTR | copywriter-en | headline (36 px bold) | 2 | Left-aligned, left x=60, top y=140 | Active. EN variant only. |
| 4 | [EN-SUBHEAD-RETARGET] | Below headline, y: 310 to 390 px | LTR | copywriter-en | subhead (24 px) | 1 | Left-aligned, left x=60, top y=320 | BLOCKED: seat-cap open item |
| 5 | [BRAND-MARK] | Lower right, above platform-CTA zone | n/a | designer | n/a | n/a | Bottom y=1130, right x=1020 | Active |

**Export:** AB-03-primary-ar.png (1080 x 1350), AB-03-primary-en.png, AB-03-square-ar.png
(1080 x 1080), AB-03-square-en.png. Retarget layer variants exported separately once seat-cap
open item resolves.

**Critical note:** no CTA button is baked into the image. The platform CTA ("register now,"
"learn more," etc.) is set inside the ad platform at trafficking time by the performance-marketer.
The bottom 200 px band is kept clear for this reason.

---

### AB-05. Concept C3. Organic Stories and paid Stories. Instagram, Snapchat.

**Build tool:** Canva or Figma.

**Canvas:** 1080 x 1920 px. Export 2x preferred for Stories.

**Safe area:** 1080 x 1500 px centered inset. Origin: 0 px from left (full width), 240 px from top.
- Top reserved zone: 0 to 240 px. Platform profile UI (avatar, handle, progress bar). No overlays.
- Bottom reserved zone: 1670 to 1920 px. Native link sticker or platform swipe-up CTA. No overlays.
- Working area for overlays: y=240 to y=1670 (1430 px height), full 1080 px width.

**Grid:** 4-column grid, 40 px outer margins, 16 px gutters. Column width: 236 px. (Stories are
compositionally taller than wide; a 4-column grid suits vertical flow.)

**Layer stack (bottom to top):**

| Layer index | Layer name | Contents | Color | Notes |
|---|---|---|---|---|
| 1 | bg | Full-canvas rectangle | color-bg (#141414) | |
| 2 | image-render | Text-free render per P3: threshold, centered | Per prompt P3 | Threshold occupies the vertical center of the working area. No text, no UI. |
| 3 | top-clear | Reserved zone marker (guide only, not exported) | n/a | 240 px top reserved guide |
| 4 | bottom-clear | Reserved zone marker (guide only, not exported) | n/a | 250 px bottom reserved guide |
| 5 | brand-mark | [BRAND-MARK] | color-text-primary | Positioned inside working area, upper-right corner. Top y=272, right x=1040. Width 72 px. |
| 6 | ar-headline | [AR-HEADLINE] | color-text-primary | Upper working area, below brand mark. |
| 7 | en-headline | [EN-HEADLINE] | color-text-primary | EN variant only. |
| 8 | ar-cta-chip | [AR-CTA-CHIP] | color-cta-label on color-accent | Pill-shaped overlay, above link sticker zone. |
| 9 | en-cta-chip | [EN-CTA-CHIP] | color-cta-label on color-accent | EN variant. |
| 10 | link-sticker-zone | [LINK-STICKER-ZONE] | Guide only | Placeholder in reserved bottom zone. BLOCKED until gate platform confirmed. |

**Copy-overlay slot table:**

| Slot index | Slot ID | Zone | Direction | Routing | Type role | Max lines | Position within safe area | Status |
|---|---|---|---|---|---|---|---|---|
| 1 | [AR-HEADLINE] | Upper working area, y: 360 to 560 px | RTL | copywriter-ar | headline (36 px bold) | 2 | Right-aligned, right x=1040, top y=380 | Active |
| 2 | [EN-HEADLINE] | Upper working area, y: 360 to 560 px | LTR | copywriter-en | headline (36 px bold) | 2 | Left-aligned, left x=40, top y=380 | Active. EN variant. |
| 3 | [AR-CTA-CHIP] | Lower working area, y: 1560 to 1650 px | RTL | copywriter-ar | label (14 px medium) | 1 | Centered, pill overlay, top y=1570, horizontally centered. Pill: 280 px wide, 48 px tall, 24 px radius, color-accent fill. | Active |
| 4 | [EN-CTA-CHIP] | Lower working area, y: 1560 to 1650 px | LTR | copywriter-en | label (14 px medium) | 1 | Centered, same pill spec as AR chip. EN variant. | Active |
| 5 | [BRAND-MARK] | Upper-right inside working area | n/a | designer | n/a | n/a | Top y=272, right x=1040, width 72 px | Active |
| 6 | [LINK-STICKER-ZONE] | Bottom reserved zone, y: 1670 to 1920 px | n/a | social media operator | n/a | n/a | Placeholder guide. Not an overlay to be built now. | BLOCKED: gate platform not confirmed |

**Export:** AB-05-ar.png, AB-05-en.png. The [AR-CTA-CHIP] limited-seats variant is a separate
blocked export pending seat-cap confirmation.

---

### AB-06. Concept C3. Paid static ad, feed. Meta, Instagram, TikTok.

**Build tool:** Canva or Figma.

**Primary canvas:** 1080 x 1350 px. Secondary canvas: 1080 x 1080 px.

**Safe area (4:5):** 960 x 1150 px inset, 60 px from left, 100 px from top.
Bottom 200 px of canvas (y=1150 to y=1350) reserved for platform CTA button. No overlays there.

**Safe area (1:1):** 960 x 880 px inset, 60 px from left, 100 px from top. Same bottom 200 px
platform-CTA reservation.

**Layer stack (bottom to top):**

| Layer index | Layer name | Contents | Color | Notes |
|---|---|---|---|---|
| 1 | bg | Full canvas | color-bg (#141414) | |
| 2 | image-render | Text-free render per P3, recomposed: threshold upper two-thirds, path approach lower third | Per P3 palette | Threshold frame occupies y=100 to y=900. Path approach from lower-left, y=900 to y=1100. |
| 3 | brand-mark | [BRAND-MARK] | color-text-primary | Lower right, above platform zone. Bottom y=1130, right x=1020, width 80 px. |
| 4 | ar-headline | [AR-HEADLINE] | color-text-primary | Upper third overlay, AR master. |
| 5 | en-headline | [EN-HEADLINE] | color-text-primary | EN variant. |

**Copy-overlay slot table:**

| Slot index | Slot ID | Zone | Direction | Routing | Type role | Max lines | Position within safe area | Status |
|---|---|---|---|---|---|---|---|---|
| 1 | [AR-HEADLINE] | Upper third, y: 120 to 300 px | RTL | copywriter-ar | headline (36 px bold) | 2 | Right-aligned, right x=1020, top y=140 | Active |
| 2 | [EN-HEADLINE] | Upper third, y: 120 to 300 px | LTR | copywriter-en | headline (36 px bold) | 2 | Left-aligned, left x=60, top y=140. EN variant. | Active |
| 3 | [BRAND-MARK] | Lower right | n/a | designer | n/a | n/a | Bottom y=1130, right x=1020, width 80 px | Active |

**Export:** AB-06-primary-ar.png, AB-06-primary-en.png, AB-06-square-ar.png, AB-06-square-en.png.

---

### AB-07. Concept C3. Organic feed, early-access opening image.

**Build tool:** Canva or Figma.

**Canvases:** two formats produced.

Format A: 1080 x 1350 px (4:5) for Instagram and LinkedIn. Safe area: same as AB-01.
Format B: 1600 x 900 px (16:9) for X. Safe area: same as AB-02.

**Layer stack (same structure as AB-06 for the 4:5 format, AB-02 for the 16:9 format):**

Additional overlay layers for the CTA chip (AB-07 has a CTA chip that AB-06 does not):

| Layer index | Layer name | Contents | Color | Notes |
|---|---|---|---|---|
| 6 | ar-cta-chip | [AR-CTA-CHIP] | color-cta-label on color-accent | Pill overlay, lower third, above brand mark |
| 7 | en-cta-chip | [EN-CTA-CHIP] | color-cta-label on color-accent | EN variant |

**Copy-overlay slot table (4:5 format):**

| Slot index | Slot ID | Zone | Direction | Routing | Type role | Max lines | Position within safe area | Status |
|---|---|---|---|---|---|---|---|---|
| 1 | [AR-HEADLINE] | Upper third, y: 120 to 280 px | RTL | copywriter-ar | headline (36 px bold) | 1 | Right-aligned, right x=1020, top y=140 | Active |
| 2 | [AR-CTA-CHIP] | Lower third, y: 1080 to 1140 px | RTL | copywriter-ar | label (14 px medium) | 1 | Centered pill, 280 px wide, 48 px tall, 24 px radius, color-accent fill, top y=1088 | Active |
| 3 | [EN-HEADLINE] | Upper third, y: 120 to 280 px | LTR | copywriter-en | headline (36 px bold) | 1 | Left-aligned, left x=60, top y=140. EN variant. | Active |
| 4 | [EN-CTA-CHIP] | Lower third, y: 1080 to 1140 px | LTR | copywriter-en | label (14 px medium) | 1 | Centered pill, same spec as AR chip. EN variant. | Active |
| 5 | [BRAND-MARK] | Lower right | n/a | designer | n/a | n/a | Bottom y=1220, right x=1020, width 80 px | Active |

**Copy-overlay slot table (16:9 format):**

| Slot index | Slot ID | Zone | Direction | Routing | Type role | Max lines | Position within safe area | Status |
|---|---|---|---|---|---|---|---|---|
| 1 | [AR-HEADLINE] | Left half, upper area, y: 110 to 250 px | RTL | copywriter-ar | headline (36 px bold) | 1 | Right-aligned, right x=780, top y=120 | Active |
| 2 | [AR-CTA-CHIP] | Right of headline, y: 260 to 320 px | RTL | copywriter-ar | label (14 px medium) | 1 | Pill, right x=780, top y=268 | Active |
| 3 | [EN-HEADLINE] | Left half, upper area, y: 110 to 250 px | LTR | copywriter-en | headline (36 px bold) | 1 | Left-aligned, left x=120, top y=120. EN variant. | Active |
| 4 | [EN-CTA-CHIP] | Same zone as AR chip, y: 260 to 320 px | LTR | copywriter-en | label (14 px medium) | 1 | Pill, left x=120, top y=268. EN variant. | Active |
| 5 | [BRAND-MARK] | Lower right | n/a | designer | n/a | n/a | Bottom y=770, right x=1480, width 80 px | Active |

**Export:** AB-07-4x5-ar.png, AB-07-4x5-en.png, AB-07-16x9-ar.png, AB-07-16x9-en.png.

---

### AB-08. Concept C4. Lifecycle email header. Segment 1 non-payers.

**Build tool:** Canva or Figma.

**Canvas:** 600 x 400 px at 72 dpi. The source file should be built at 1200 x 800 px (2x) for
retina rendering, then exported at 600 x 400 px. Color space: sRGB. Format: PNG. Max file
size: 150 KB. Web-optimized (strip metadata, no ICC profile embed unless sRGB explicit).

**Safe area:** 560 x 360 px inset. Origin: 20 px from left, 20 px from top.
Email clients clip beyond the container width. All overlays inside the safe area.

**Layer stack (bottom to top):**

| Layer index | Layer name | Contents | Color | Notes |
|---|---|---|---|---|
| 1 | bg | Full canvas | color-bg (#141414) | |
| 2 | card-panel | 560 x 320 px centered card, top y=40 | color-surface (#1A1A1A) | Frames the ring motif |
| 3 | image-render | Text-free render per P4: completion ring and seal, centered | Per P4 palette | Ring width: approx 360 px (60% of 600 px canvas width). Ring centered horizontally and vertically within card-panel. No text, no numbers, no external logos. |
| 4 | brand-mark | [BRAND-MARK] | color-text-primary | Email logo position. Placed above the visual in the email template header, not inside this image canvas, per the lifecycle email template structure. The image is the visual asset only. The brand mark position in the email template is owned by lifecycle-architect. Designer flags this for lifecycle-architect. |
| 5 | ar-headline | [AR-HEADLINE] | color-text-primary | Overlay across lower portion of card-panel, above card bottom. |
| 6 | en-headline | [EN-HEADLINE] | color-text-primary | EN variant. |

**Copy-overlay slot table:**

| Slot index | Slot ID | Zone | Direction | Routing | Type role | Max lines | Position within safe area | Status |
|---|---|---|---|---|---|---|---|---|
| 1 | [AR-HEADLINE] | Lower quarter of canvas, y: 310 to 370 px (at 1x) | RTL | copywriter-ar | headline (24 px bold at 1x, 48 px in 2x source file) | 1 | Right-aligned, right x=540, top y=320 | Active |
| 2 | [EN-HEADLINE] | Lower quarter of canvas, y: 310 to 370 px | LTR | copywriter-en | headline (24 px bold at 1x) | 1 | Left-aligned, left x=20, top y=320. EN variant. | Active |

**Export:** AB-08-ar.png (600 x 400, max 150 KB), AB-08-en.png (same spec). Both at sRGB. Confirm
with lifecycle-architect whether a bilingual single asset or two separate assets is needed for the
email template, and whether the EN variant is required at all for segment 1 (the AR-only question
is an open item noted in the asset brief).

**Critical note:** the email body copy, subject line, and preheader are authored in stream 7, not
here. This spec covers the header visual asset only. The brand mark in the email is part of the
email template, outside this image canvas.

---

### AB-09. Concept C4. Organic feed, reward image. Post 9.

**Build tool:** Canva or Figma.

**Canvases:** 1080 x 1350 px (4:5) for Instagram and LinkedIn. 1600 x 900 px (16:9) for X.

**Safe areas:** same as AB-01 (4:5) and AB-02 (16:9).

**Layer stack (4:5):**

| Layer index | Layer name | Contents | Color | Notes |
|---|---|---|---|---|
| 1 | bg | Full canvas | color-bg (#141414) | |
| 2 | card-panel | 960 x 960 px centered card, centered vertically | color-surface (#1A1A1A) | |
| 3 | image-render | Text-free render per P4: completion ring and seal | Per P4 palette | Ring at 70% of canvas height (approx 945 px outer diameter for 1350 px height, scaled down to fit card-panel). Ring centered in card. No text, no accreditation marks. |
| 4 | brand-mark | [BRAND-MARK] | color-text-primary | Lower-right safe area, bottom y=1220, right x=1020, width 80 px. |
| 5 | ar-headline | [AR-HEADLINE] | color-text-primary | Upper zone of card, above ring. |
| 6 | en-headline | [EN-HEADLINE] | color-text-primary | EN variant. |

**Copy-overlay slot table (4:5):**

| Slot index | Slot ID | Zone | Direction | Routing | Type role | Max lines | Position within safe area | Status |
|---|---|---|---|---|---|---|---|---|
| 1 | [AR-HEADLINE] | Upper third, y: 120 to 300 px | RTL | copywriter-ar | headline (36 px bold) | 1 | Right-aligned, right x=1020, top y=140 | Active |
| 2 | [EN-HEADLINE] | Upper third, y: 120 to 300 px | LTR | copywriter-en | headline (36 px bold) | 1 | Left-aligned, left x=60, top y=140. EN variant. | Active |
| 3 | [BRAND-MARK] | Lower right | n/a | designer | n/a | n/a | Bottom y=1220, right x=1020, width 80 px | Active |

**Export:** AB-09-4x5-ar.png, AB-09-4x5-en.png, AB-09-16x9-ar.png, AB-09-16x9-en.png.

**Guardrail:** the ring and seal are a completion mark only. No overlay element, no copy, and no
visual detail may imply accreditation or external certification. No "certified by" language. No
external credential logo. The seal is abstract. The copywriters carry this same guardrail note.

---

## Section 3. Motion asset specs (AB-04 and V1)

Motion specs define canvas, duration, safe area, and a frame-by-frame timing table. All text and
copy overlays are applied at build time, not generated into the motion render. The motion render
is text-free throughout.

---

### AB-04. Concept C2. Paid social, motion ad. Reels, TikTok, YouTube pre-roll.

**Build tool:** motion-capable production tool (pending human gate clearance for execution).

**Primary canvas:** 1080 x 1920 px (9:16), vertical. Secondary canvas: 1920 x 1080 px (16:9)
for YouTube pre-roll.

**Safe area (9:16):** 1080 x 1600 px inset. Top 160 px and bottom 160 px reserved for platform
UI and native CTA.
- Top reserved: 0 to 160 px. Platform profile bar, progress indicator, sticker zone.
- Bottom reserved: 1760 to 1920 px. Platform CTA button and navigation.
- Working area: y=160 to y=1760 (1600 px height), full 1080 px width.

**Safe area (16:9):** 1720 x 880 px inset. Origin: 100 px from left, 100 px from top.

**Duration:** 8 to 11 seconds total, structured as follows.

**Motion timing table (9:16 primary):**

| Phase | Time range (seconds) | Description | Overlay layers active | Notes |
|---|---|---|---|---|
| Streak lights in | 0:00 to 6:00 or 9:00 | Markers light left to right per prompt P5. Each marker activation: soft emerald pulse, then holds at full color-accent (#009975). Unlit markers: color-accent-dim (#00684f) or color-surface (#1A1A1A). | None (pure motion render, text-free) | 6 to 9 second range. Duration is the producer's call within this range. |
| Full-lit hold | 6:00 to 7:00 or 9:00 to 10:00 | All markers lit, leading marker pulses steadily. | None | 1 second hold. |
| Brand frame fade-in | 7:00 to 8:00 or 10:00 to 11:00 | Near-black field fades in (dissolve over 0.5 seconds). Full canvas returns to color-bg. | [AR-HEADLINE] or [EN-HEADLINE] fades in. [BRAND-MARK] fades in. | 1 second hold. Copy overlay applied at build time. |
| End frame hold | Holds at 8:00 or 11:00 | Static frame: near-black field, brand mark, headline. | [AR-HEADLINE] or [EN-HEADLINE] held. [BRAND-MARK] held. | Export as the final held frame. |

**Frame export requirements:**
- Master rendered motion file: text-free throughout.
- Copy overlay composited at build time (not burned into the motion render).
- Export AR master and EN variant as separate files.

**Copy-overlay slot table:**

| Slot index | Slot ID | Zone | Direction | Routing | Type role | Max lines | Timing | Status |
|---|---|---|---|---|---|---|---|---|
| 1 | [AR-HEADLINE] | Brand frame, centered or upper two-thirds of safe area | RTL | copywriter-ar | display (48 px bold) | 1 | Appears at brand frame fade-in. Static for the brand frame hold. | Active |
| 2 | [EN-HEADLINE] | Brand frame, same zone | LTR | copywriter-en | display (48 px bold) | 1 | Same timing as AR-HEADLINE. EN variant export. | Active |
| 3 | [BRAND-MARK] | Brand frame, lower-center or lower-right of safe area | n/a | designer | n/a | n/a | Appears with headline at brand frame fade-in. | Active |

**Export:** AB-04-9x16-ar.mp4, AB-04-9x16-en.mp4, AB-04-16x9-ar.mp4, AB-04-16x9-en.mp4.
Frame rate: 25 fps minimum. Codec: H.264 at minimum 8 Mbps for social delivery.
Audio: none baked (audio direction is the post producer's call). Deliver a mute export.

---

### V1. Teaser/hype video. All four concepts assembled as a hero's-journey arc.

**Build tool:** motion-capable production tool (pending human gate clearance for execution).

**Primary canvas:** 1080 x 1920 px (9:16). Secondary canvas: 1920 x 1080 px (16:9) for YouTube.

**Duration:** 30 to 45 seconds. Act structure drives the exact cut; the range is the producer's call.

**Safe area (9:16):** same as AB-04 (top 160 px and bottom 160 px reserved).
**Safe area (16:9):** 1720 x 880 px inset, 100 px from left and top.

**Motion timing table:**

| Act | Time range | Visual contents (text-free render, per P6) | Overlay slots active | Transition |
|---|---|---|---|---|
| Act 1: spark | 0:00 to 8:00 | Single emerald point on near-black. The point breathes once and holds. Silence or minimal ambient tone (audio: producer's call). | [AR-SUPER-ACT1] or [EN-SUPER-ACT1]: fades in at 2:00, holds through 6:00, fades out by 8:00. | Holds on near-black going into Act 2. |
| Act 2: path and streak | 8:00 to 20:00 | Emerald line traces forward from the spark point. Streak markers appear along the path and light one by one as the line passes through them. | None. | Continuous motion, no cut. |
| Act 3: threshold | 20:00 to 32:00 | Threshold shape from P3 appears at end of the path. Path arrives at threshold base. Threshold door opens slightly inward, suggesting entry. Interior: slightly lighter near-black, not bright. | [AR-SUPER-ACT3] or [EN-SUPER-ACT3]: fades in at 22:00, holds through 29:00, fades out by 32:00. | Slow dissolve into Act 4. |
| Act 4: completion ring and brand frame | 32:00 to 42:00 (or 45:00) | Completion ring from P4 fades in. Full ring, glowing seal, held at 35:00. Near-black hold frame at 38:00. | [AR-CTA-SUPER] or [EN-CTA-SUPER] fades in at 38:00. [BRAND-MARK-FRAME] fades in at 38:00. Hold through end. | Near-black dissolve at 38:00 to end frame. |
| End frame | Last 3 to 5 seconds of total duration | Near-black field. Brand mark and CTA super are the only elements. | All active overlays from Act 4 held. [LINK-OR-CTA-UNIT] zone marked but BLOCKED. | Holds to end. |

**Copy-overlay slot table:**

| Slot index | Slot ID | Zone | Direction | Routing | Type role | Max lines | Timing | Status |
|---|---|---|---|---|---|---|---|---|
| 1 | [AR-SUPER-ACT1] | Center of safe area, Act 1 frames | RTL | copywriter-ar | subhead (24 px) | 1 | In: 2:00. Out: 8:00. Fade in/out over 0.5 seconds. | Active |
| 2 | [AR-SUPER-ACT3] | Center or lower center of safe area, Act 3 frames | RTL | copywriter-ar | subhead (24 px) | 1 | In: 22:00. Out: 32:00. | Active |
| 3 | [AR-CTA-SUPER] | Lower center of safe area, end frame | RTL | copywriter-ar | headline (36 px bold) | 1 | In: 38:00. Holds to end. | Active |
| 4 | [EN-SUPER-ACT1] | Center of safe area, Act 1 frames | LTR | copywriter-en | subhead (24 px) | 1 | Same as AR. EN variant export. | Active |
| 5 | [EN-SUPER-ACT3] | Center or lower center, Act 3 | LTR | copywriter-en | subhead (24 px) | 1 | Same as AR. EN variant. | Active |
| 6 | [EN-CTA-SUPER] | Lower center, end frame | LTR | copywriter-en | headline (36 px bold) | 1 | Same as AR. EN variant. | Active |
| 7 | [BRAND-MARK-FRAME] | Lower-right of safe area, end frame | n/a | designer | n/a | n/a | In: 38:00. Holds to end. | Active |
| 8 | [LINK-OR-CTA-UNIT] | Bottom of safe area, end frame | n/a | platform operator | n/a | n/a | Set at trafficking time, not in this build. | BLOCKED: gate platform not confirmed |

**Export:** V1-9x16-ar.mp4, V1-9x16-en.mp4, V1-16x9-ar.mp4, V1-16x9-en.mp4. Text-free motion
master also exported for repurposing: V1-9x16-textfree.mp4, V1-16x9-textfree.mp4.

Frame rate: 25 fps. Codec: H.264 at 12 Mbps minimum for the 9:16 master. Audio: none baked.
Deliver mute exports. Blotato MCP repurposing (Stories, horizontal, square cuts) is BLOCKED
until the BLOTATO_API_KEY credential is confirmed and a build-vs-buy-eval completes.

**Transition spec:** all transitions are slow dissolves. No hard cuts between acts.
Dissolve duration: 0.5 to 1.0 second between acts. No wipes, no flash cuts, no motion blur
artifacts on the emerald path or ring.

---

## Section 4. Landing page visual spec (from conversion-package.md)

This section covers the landing page as a visual layout document. It does not build or publish
the page. Build is behind the human gate. This spec feeds the front-end developer.

**Tool:** the page is built by the web team or a front-end developer. This spec is a layout
reference, not a Canva or Figma deliverable. The hero block visual (Section B of the page) uses
AB-01 or AB-03 as the sourced asset, resized for web breakpoints.

### 4.1 Canvas and breakpoints

| Breakpoint | Viewport width | Layout | Notes |
|---|---|---|---|
| Mobile | 375 px to 767 px | Single column, full-width stacked | Primary design target |
| Tablet | 768 px to 1199 px | Single or two-column, content max-width 720 px | |
| Desktop | 1200 px and above | Centered content, max-width 1200 px, 80 px side margins | |

**Direction:** RTL throughout. `dir="rtl"` and `lang="ar"` on the root element. EN variant uses
`dir="ltr"` and `lang="en"`. Western numerals only wherever a numeral appears.

### 4.2 Section-by-section layout grid

**Section A: navigation bar**

| Element | Color | Position | Notes |
|---|---|---|---|
| Bar background | color-bg (#141414) | Full width, height 64 px | |
| Maharat logotype | #FFFFFF | Right-aligned (RTL reading start), 24 px from right edge | RTL: the logo is on the right because right is the reading start in Arabic. |
| Language selector | color-text-secondary | Left end of bar (RTL: trailing end), 24 px from left edge | AR/EN toggle if the site supports it. Optional per web team confirmation. |
| No navigation links | n/a | n/a | Logo only, no distractions |

**Section B: hero block**

| Element | Color / Asset | Notes |
|---|---|---|
| Background | color-bg (#141414) | Full width |
| Visual asset | AB-01 (feed crop resized) or a web-optimized version of the P1 or P2 render | Full-width on mobile. On desktop, occupies the right column (RTL: left column visually) or full-width with text overlay. No text baked into the image. |
| AR headline | [AR-HEADLINE] overlay | type role: display (48 px bold on desktop, 36 px on mobile). RTL, right-aligned. Routes to copywriter-ar. |
| AR subhead | [AR-SUBHEAD] overlay | type role: subhead (24 px). RTL, right-aligned. Routes to copywriter-ar. |
| EN headline | [EN-HEADLINE] overlay | LTR, left-aligned. EN variant. Routes to copywriter-en. |
| EN subhead | [EN-SUBHEAD] overlay | LTR. EN variant. Routes to copywriter-en. |
| Primary CTA button | color-accent (#009975) background, color-cta-label (#FFFFFF) text | Full-width on mobile (min touch: 48 x 48 px). Centered on desktop. AR label: [AR-CTA-BUTTON]. EN label: [EN-CTA-BUTTON]. Routes to copywriter-ar and copywriter-en. Action: scrolls to Section D (gate form). One CTA only above the fold. |

**Section C: story strip (three-card section)**

| Element | Color | Notes |
|---|---|---|
| Section background | color-surface (#1A1A1A) | Full width |
| Cards: desktop layout | Three horizontal cards | Max-width 1200 px, three equal columns, 24 px gutters |
| Cards: mobile layout | Vertically stacked, full-width | 24 px gap between cards |
| Card background | color-surface (#1A1A1A) | Same as section, no border needed (depth from spacing) |
| Card icon/motif | color-accent (#009975) | Abstract motif only. Card 1: small-step icon. Card 2: streak row. Card 3: progress ring. No UI screenshots, no labels on the motifs. |
| Card AR copy | [AR-CARD-1], [AR-CARD-2], [AR-CARD-3] | type: body (18 px). RTL. Routes to copywriter-ar. |
| Card EN copy | [EN-CARD-1], [EN-CARD-2], [EN-CARD-3] | type: body (18 px). LTR. EN variant. Routes to copywriter-en. |

**Section D: gate form**

| Element | Color | Notes |
|---|---|---|
| Section background | color-bg (#141414) | |
| Form card | color-surface (#1A1A1A) | Centered, max-width 560 px on desktop. Full-width with 16 px margins on mobile. Padding: 32 px. |
| Intro line above form | [AR-FORM-INTRO] / [EN-FORM-INTRO] | type: subhead (24 px). Routes to copywriters. |
| Field: name (email gate) | color-surface (#1A1A1A) border | AR label: [AR-FIELD-NAME]. Placeholder: [AR-PLACEHOLDER-NAME]. Height 48 px min. RTL input. |
| Field: email (email gate) | color-surface (#1A1A1A) border | AR label: [AR-FIELD-EMAIL]. Placeholder: [AR-PLACEHOLDER-EMAIL]. Height 48 px min. |
| Field: WhatsApp (WhatsApp gate) | color-surface (#1A1A1A) border | AR label: [AR-FIELD-WHATSAPP]. Height 48 px min. BLOCKED: gate platform not confirmed. |
| Privacy notice | color-text-secondary | type: caption (12 px). Appears directly below fields, before submit button. [AR-PRIVACY-NOTICE] / [EN-PRIVACY-NOTICE]. Routes to copywriter-ar, copywriter-en, and compliance-privacy-reviewer. |
| Submit button | color-accent (#009975), color-cta-label text | Full-width on mobile, centered on desktop. Min height 48 px. [AR-SUBMIT-BUTTON] / [EN-SUBMIT-BUTTON]. Routes to copywriters. |
| Confirmation state | In-place replacement of form on submit | [AR-CONFIRMATION] / [EN-CONFIRMATION]. Routes to copywriters. No personal data echoed. No URL redirect. |

**Section E: app-install path**

| Element | Color | Notes |
|---|---|---|
| Section background | color-surface (#1A1A1A) on color-bg field | Card panel, max-width 560 px. Below gate form on mobile. |
| AR copy | [AR-APP-INSTALL] | type: body (18 px). RTL. Routes to copywriter-ar. |
| EN copy | [EN-APP-INSTALL] | EN variant. Routes to copywriter-en. |
| App Store badge | Standard Apple badge | Links to Maharat App Store listing. No personal data in deep-link parameters. |
| Google Play badge | Standard Google Play badge | Links to Maharat Google Play listing. No personal data in deep-link parameters. |
| No app UI screenshots | n/a | Guardrail: no app UI screenshots, no invented Skill Path titles or UI in this section. |

**Section F: footer**

| Element | Color | Notes |
|---|---|---|
| Background | color-bg (#141414) | Full width |
| Maharat logotype | #FFFFFF | RTL: right-aligned |
| Privacy policy link | color-text-secondary | URL to confirm with web team. OPEN ITEM. |
| Unsubscribe link | color-text-secondary | Wired to the lifecycle platform once confirmed. |
| Copyright line | color-text-secondary | type: caption (12 px). Western numerals. |
| No social icons | n/a | Goal is the gate form. No navigation off this page. |

### 4.3 RTL layout rules for the landing page spec

- All text is right-aligned in the AR version. All text is left-aligned in the EN version.
- Icon positions in Section C (story strip) swap side in RTL vs LTR layouts: icon is on the
  right of the card text in RTL (reading start), left of the card text in LTR.
- The CTA button is centered on both variants.
- Form fields read right-to-left in the AR version. The field `dir` attribute is `rtl` on
  Arabic fields. Input text is right-to-left. Placeholders are right-aligned.
- Western numerals only. No Eastern Arabic numerals in any rendered state.
- No em dashes in any rendered text. No tatweel.

### 4.4 Landing page copy-overlay slot index (full list)

All slots below are empty. Routes to copywriter-ar or copywriter-en as noted. Designer marks
the visual position; words are the copywriters' call.

| Slot ID | Section | Direction | Routing | Notes |
|---|---|---|---|---|
| [AR-HEADLINE] | Hero (B) | RTL | copywriter-ar | Display headline, short |
| [AR-SUBHEAD] | Hero (B) | RTL | copywriter-ar | Subhead, soft-launch framing |
| [AR-CTA-BUTTON] | Hero (B) | RTL | copywriter-ar | "Register interest" direction |
| [EN-HEADLINE] | Hero (B) | LTR | copywriter-en | EN variant |
| [EN-SUBHEAD] | Hero (B) | LTR | copywriter-en | EN variant |
| [EN-CTA-BUTTON] | Hero (B) | LTR | copywriter-en | EN variant |
| [AR-CARD-1] | Story strip (C) | RTL | copywriter-ar | Format benefit card |
| [AR-CARD-2] | Story strip (C) | RTL | copywriter-ar | Streak benefit card |
| [AR-CARD-3] | Story strip (C) | RTL | copywriter-ar | Skill outcome card |
| [EN-CARD-1] | Story strip (C) | LTR | copywriter-en | EN variant |
| [EN-CARD-2] | Story strip (C) | LTR | copywriter-en | EN variant |
| [EN-CARD-3] | Story strip (C) | LTR | copywriter-en | EN variant |
| [AR-FORM-INTRO] | Gate form (D) | RTL | copywriter-ar | Intro line above form |
| [AR-FIELD-NAME] | Gate form (D) | RTL | copywriter-ar | Field label, name |
| [AR-PLACEHOLDER-NAME] | Gate form (D) | RTL | copywriter-ar | Placeholder text |
| [AR-FIELD-EMAIL] | Gate form (D) | RTL | copywriter-ar | Field label, email |
| [AR-PLACEHOLDER-EMAIL] | Gate form (D) | RTL | copywriter-ar | Placeholder text |
| [AR-FIELD-WHATSAPP] | Gate form (D) | RTL | copywriter-ar | Field label, WhatsApp. BLOCKED pending gate platform confirmation. |
| [AR-PRIVACY-NOTICE] | Gate form (D) | RTL | copywriter-ar + compliance-privacy-reviewer | Privacy notice at point of collection |
| [AR-SUBMIT-BUTTON] | Gate form (D) | RTL | copywriter-ar | Submit button label |
| [AR-CONFIRMATION] | Gate form (D) | RTL | copywriter-ar | In-place confirmation state |
| [EN-FORM-INTRO] | Gate form (D) | LTR | copywriter-en | EN variant |
| [EN-FIELD-NAME] | Gate form (D) | LTR | copywriter-en | EN variant |
| [EN-PLACEHOLDER-NAME] | Gate form (D) | LTR | copywriter-en | EN variant |
| [EN-FIELD-EMAIL] | Gate form (D) | LTR | copywriter-en | EN variant |
| [EN-PLACEHOLDER-EMAIL] | Gate form (D) | LTR | copywriter-en | EN variant |
| [EN-FIELD-WHATSAPP] | Gate form (D) | LTR | copywriter-en | BLOCKED pending gate platform. |
| [EN-PRIVACY-NOTICE] | Gate form (D) | LTR | copywriter-en + compliance-privacy-reviewer | EN variant |
| [EN-SUBMIT-BUTTON] | Gate form (D) | LTR | copywriter-en | EN variant |
| [EN-CONFIRMATION] | Gate form (D) | LTR | copywriter-en | EN variant |
| [AR-APP-INSTALL] | App install (E) | RTL | copywriter-ar | App install prompt |
| [EN-APP-INSTALL] | App install (E) | LTR | copywriter-en | EN variant |

---

## Section 5. Design-QA verdict

The design-QA check runs in order. All items pass for this spec. Verdict: PASS.

---

### Check 1. RTL correct

Verdict: PASS

Every AR overlay slot across all ten assets (AB-01 to AB-09, V1) and the landing page spec is
marked RTL with right-aligned text direction. No AR and EN copy slots appear simultaneously on
the same canvas export: they are on separate layers toggled per export. The motion timing table
for V1 specifies AR and EN as separate exports (V1-9x16-ar.mp4 and V1-9x16-en.mp4), preventing
any bidi collision at render time.

Landing page RTL requirements are carried explicitly: `dir="rtl"` and `lang="ar"` on the root
element, RTL field direction on form inputs, right-aligned text throughout the AR version. Icon
and logo positions reflect RTL reading direction (right is start). Mixed AR-EN content (brand
name within Arabic copy) is noted for bidi test requirement at build time.

No Arabic copy is authored in this spec. All AR slots are empty and route to copywriter-ar.
RTL direction is a layout property set by the designer at build time, not dependent on copy content.

---

### Check 2. Safe areas

Verdict: PASS

All safe areas are specified in pixels with explicit origin points. Overlay text and brand marks
are placed inside the stated insets on every asset.

Platform-specific reservations are enforced:
- AB-03, AB-06: bottom 200 px of canvas (y=1150 to 1350 for 4:5) is clear of all overlays,
  reserved for the platform-native CTA button. No baked button appears in any asset.
- AB-04, AB-05: top 160 to 240 px and bottom 160 to 250 px reserved for platform profile UI
  and native link sticker or CTA. All copy overlays and brand marks sit within the defined
  working area.
- V1: same top/bottom reservations as AB-04. The [LINK-OR-CTA-UNIT] slot in the bottom zone
  is marked BLOCKED and is not placed in the built asset.
- AB-08: 560 x 360 px inset for a 600 x 400 px email canvas. Email client clipping noted.

The ring motif for AB-08 is specified at approximately 360 px wide (60 percent of the 600 px
canvas), centered. This keeps the ring within the safe area on all sides.

---

### Check 3. Western numerals only in any rendered text

Verdict: PASS

No Eastern Arabic numerals (Unicode U+0660 to U+0669) appear in this spec. All numeric
references in the spec use Western numerals (0 to 9). Type scale sizes, pixel coordinates,
durations, and any numeral shown in a rendered asset use Western numerals.

The motion timing table for AB-04 and V1 uses seconds expressed as Western numerals (e.g., 0:00,
8:00, 32:00). The streak motif (P2, P5) contains no numbers at all: it is an abstract row of
markers. Timing and duration values in the spec use Western numerals.

No tatweel or kashida appears anywhere in this spec.

---

### Check 4. Visual constants applied. Accent used as highlight, not flood.

Verdict: PASS

Color-bg (#141414) is the base layer on every asset. Color-surface (#1A1A1A) is used for card
and panel elements only (lower-third card panel in feed assets, streak track layer, card-panel in
AB-08, form card on landing page). Color-accent (#009975) is restricted to: spark and path line
(C1), lit streak markers and leading pulse (C2), threshold glow and linework (C3), completion ring
and seal (C4), CTA chip and button fills, and brand-frame fade-in highlight.

Color-accent does not flood the background on any asset. It appears as a focused element: a line,
a marker row, a ring, a door-frame, or a button. The ratio of emerald to near-black in each asset
preserves the premium-uncluttered standard. The color-accent-dim (#00684f) variant is used only
for unlit or dimmed streak markers in C2 and C4 usage, keeping contrast without competing with
the lit-marker focal point.

---

### Check 5. Premium and uncluttered. One clear focal point. No clutter.

Verdict: PASS

Each concept has one focal point:
- C1 (AB-01, AB-02): the emerald spark and path line. Upper half is generous negative space.
- C2 (AB-03, AB-04): the streak row. Centered in the frame with a recessed track. No competing
  elements.
- C3 (AB-05, AB-06, AB-07): the threshold. Centered vertically in the working area. The path
  approaches from below, directing the eye to the threshold. No clutter on either side.
- C4 (AB-08, AB-09): the completion ring and seal. Ring is centered in the card-panel. One ring,
  one seal, no competing graphic elements.
- V1: each act has one focal element. Transitions are slow dissolves. No hard cuts, no competing
  layers across acts.

Headline overlays are positioned to respect the negative space of each composition. They do not
bisect or overlap the focal element. The brand mark is small (80 px wide) and positioned in a
corner. CTA chips are small pill overlays positioned outside the focal element zone.

Landing page: one primary CTA above the fold, generous spacing, no secondary navigation.

---

### Check 6. No Arabic text baked into any generated image

Verdict: PASS

This is the central hard rule. It is structurally enforced in this spec:

Every asset has an "image-render" layer (the text-free generated image) and a separate set of
overlay layers ([AR-HEADLINE], [AR-CTA-CHIP], etc.). The image-render layer contains no text,
no Arabic, no Latin, no numerals, no UI chrome, and no invented names. The overlay layers are
empty slots that are filled at build time by the human designer from QA-passed copy.

The generative prompts (P1 to P6 in creative-package.md) explicitly exclude text, characters,
UI, and specific titles. The designer's layer stack enforces the separation: the image-render
layer and the copy overlay layers are on distinct layers, never merged before QA. No Arabic copy
is authored in this spec. All AR content is in named slots routed to copywriter-ar.

---

### Design-QA summary

| Check | Verdict |
|---|---|
| RTL correct | PASS |
| Safe areas clear of platform crops and UI overlays | PASS |
| Western numerals only in any rendered text, no tatweel | PASS |
| Visual constants applied, accent as highlight not flood | PASS |
| Premium and uncluttered, one clear focal point per asset | PASS |
| No Arabic text baked into any generated image | PASS |

**Overall design-QA verdict: PASS**

Fix list: none. The spec passes all six checks.

---

## Section 6. Open items carried forward to brand-qa-reviewer

The following open items are not design-QA issues (they do not affect the spec's RTL, color,
safety, or cleanliness). They are open items that gate execution and must be resolved before
the human gate approves any build or export action.

| Item | Status | Blocking what |
|---|---|---|
| Build tool (Canva MCP or Figma) not yet approved for live execution | Open | All build and export actions |
| Arabic and Latin font families not confirmed | Open | Final type rendering at build time. Type scale is role-based; family names must be confirmed before any text is set in build. |
| All [AR-*] and [EN-*] copy slots unfilled | Open | Copy-overlay compositing at build time. Slots route to copywriter-ar and copywriter-en. |
| Approved brand or product imagery not confirmed (brief sec 7) | Open | Any departure from abstract motifs in the image-render layers |
| Seat-cap not confirmed | Open | [AR-SUBHEAD-RETARGET] and [EN-SUBHEAD-RETARGET] layers in AB-03 remain blocked |
| Gate platform (email or WhatsApp) not confirmed | Open | [LINK-STICKER-ZONE] in AB-05, [LINK-OR-CTA-UNIT] in V1, gate form wiring in landing page |
| Video production resourcing not confirmed | Open | AB-04 and V1 motion execution |
| Blotato MCP credential and build-vs-buy-eval not complete | Open | V1 repurposing into Stories, square, horizontal cuts |
| Privacy policy URL not confirmed | Open | Footer link and gate form privacy notice link in landing page |
| Gate form platform endpoint not confirmed | Open | Landing page Section D submit action |

---

## Handoff routing

- brand-qa-reviewer: receives this spec for the brand-QA pass. The design-QA verdict is PASS.
  brand-qa-reviewer runs last in the quality gate sequence.
- paid-build-engineer: receives paid assets AB-03, AB-04, AB-05, AB-06, V1 (paid cut) once the
  human gate clears. Build and export are gated.
- lifecycle-architect: receives AB-08 spec for the lifecycle email header. Confirm bilingual
  vs AR-only with lifecycle-architect before AB-08 is exported.
- organic-social: receives AB-01, AB-02, AB-05, AB-07, AB-09, V1 (organic cut) specs once the
  human gate clears.
- copywriter-ar: receives all [AR-*] slot routing for every asset in this spec.
- copywriter-en: receives all [EN-*] slot routing.
- compliance-privacy-reviewer: the landing page Section D (gate form and privacy notice)
  requires compliance sign-off before the page goes live.
- human gate: nothing in this spec publishes, sends, builds a live asset, or spends. The human
  gate is the final action gate. Ahmed's explicit per-asset sign-off is required.

---

## Pre-handoff checklist (designer self-check)

- Each spec realizes the concept intent and the asset brief's dimensions and safe areas. Pass.
- Visual constants (#141414, #1A1A1A, #009975) applied on every asset. Emerald as accent, not
  flood. Pass.
- Copy-overlay slots labeled by language (AR / EN), RTL-marked, and empty. No Arabic authored
  here. Pass.
- Design-QA check passed on every spec. Fix list: empty. Pass.
- Unconfirmed items (tool, font, copy, seat cap, gate platform, video resourcing, Blotato
  credential) are in open_items, not guessed. Pass.
- No Arabic text inside any generated image layer. Pass.
- Western numerals only. No Eastern Arabic numerals. No tatweel. Pass.
- No em dashes anywhere in this file. Pass.
- No invented Skill Path titles, instructor names, accreditation claim, or firm launch date. Pass.
- Abstract motifs only. No app UI screenshots. No invented product names in any layer. Pass.

---

## Status

Draft. Design-QA verdict: PASS. Pending brand-qa-reviewer. Not approved. Nothing here
publishes, sends, builds a live asset, or spends. All execution is behind the human gate.
