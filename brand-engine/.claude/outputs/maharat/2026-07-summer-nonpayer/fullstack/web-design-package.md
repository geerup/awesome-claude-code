# Web Design Package: Summer of Skills, full-stack non-payer campaign

Direction half produced by web-design-director. Build-ready design_spec and web_design_qa
are stub sections for web-designer to complete in Wave 3.

---

## Common Envelope

- campaign_id: 2026-07-summer-nonpayer
- produced_by: web-design-director (direction); web-designer (design_spec and web_design_qa)
- stream: 6 conversion path (web design direction + build-ready spec)
- status: qa-passed (web_design_qa pass after accessibility fixes applied 2026-06-12; brand_qa pending brand-qa-reviewer)
- qa:
  - skill_eval: pass
  - arabic_qa: na (no Arabic authored in this stream; words are authored by copywriter-ar and checked at arabic-copy-qa)
  - english_qa: na (no English copy authored in this stream; words are authored by copywriter-en and checked at english-copy-qa)
  - design_qa: na (not a visual asset stream)
  - web_design_qa: pass (web-designer verdict 2026-06-12, revised after accessibility-reviewer fix list applied 2026-06-12; all 10 checks pass; addressable accessibility items resolved in spec; two render-block open items carried below; human design check remains before any publish; two gated dependencies carried to human gate: copy-region-unbound pending copy-package QA, gate-platform-not-confirmed)
  - compliance: na (direction and spec only; compliance-privacy-reviewer runs on the conversion-package when data collection is wired; Saudi PDPL open item surfaced)
  - brand_qa: pending (brand-qa-reviewer to run on the full direction plus design_spec before it advances to conversion-engineer)
- open_items:
  - gate-platform-not-confirmed: email and WhatsApp capture platforms are unconfirmed (brief section 7, strategy-artifact section 6). The page is designed for both paths; live wiring is blocked until the platform is named.
  - instructor-photography-not-confirmed: rights-cleared photography for the 7 nameable instructors is OPEN ITEM (brief section 9). The hero and field-card assets use abstract brand-constant art as the confirmed fallback. No generated instructor likeness at any point.
  - price-not-confirmed: no price appears in the direction. A plans section placeholder is included; price copy regions are bound to copywriter slots that will only be filled if Ahmed confirms price and currency.
  - plan-not-confirmed: which plan or plans (1, 3, or 12 month) the campaign leads with is ASSUMPTION. The plans section is structured to accommodate the answer once confirmed; no plan name or price is invented here.
  - promotion-not-confirmed: posture is value-led. A promo slot exists in the plans section; it remains empty unless Ahmed confirms a summer trial, discount, or bundle.
  - per-instructor-naming-confirm-at-gate: all 7 nameable instructors (Ragheb Alama, Salam Dakkak, Kosai Khauli, Bassam Fattouh, Toufic Kreidieh, Cedric Haddad, Elda Choucair) are drafted as confirm-at-gate per the strategy-artifact. The field grid uses instructor-field labels (Music, Cooking, Acting, Makeup, Business, Styling, Marketing) that are grounded in cleared, page-sourced facts and do not require the instructor name to display. Name display in any field card is a confirm-at-gate slot, not a default.
  - verify-before-public-use facts: Toufic Kreidieh's Brands For Less name and the $10,000-garage detail must not appear until verified. Elda Choucair's Omnicom, Forbes, Cannes, and the 900-plus and 1000-plus figures must not appear until verified. These are excluded from all copy slot definitions here.
  - Saudi-PDPL-and-data-residency: OPEN ITEM. Must be confirmed before wiring any data collection or signup gate.
  - accessibility-focus-order-render-check: focus order across all 5 gate states and the FAQ accordion at all 3 breakpoints requires verification on the rendered, interactive page before go-live. Programmatic focus moves to the success heading (gate-submitted), error container (gate-error), and FAQ answer content becoming keyboard-focusable on expand cannot be confirmed at spec level. Carry as open item to the rendered build check.
  - accessibility-email-template-render-check: full email template render verification (semantic heading structure, plain-text alternative, alt text on header imagery, CTA contrast at rendered size, CTA tap target, RTL rendering at 375 px) is blocked pending send-platform confirmation. Resubmit rendered template to accessibility-qa before any send action.
- brief_refs:
  - offer: product (Maharat B2C subscription, masterclass roster as hook), plan (ASSUMPTION), price (ASSUMPTION), promotion (ASSUMPTION), offer_framing_notes
  - gate_type: email or WhatsApp capture (brief section 7, gate_platform OPEN ITEM)
  - page_direction: breadth-led, value-led summer landing experience; pick-a-field, free-first-lesson flow; roster-breadth motif; brand constants; RTL-correct Arabic; generated imagery text-free; instructor likeness never generated (brief sections 9 and 10)
  - instructor_roster: 7 nameable (confirm-at-gate), 4 never named (brief section 6)
  - creative_direction: premium uncluttered, near-black #141414, card surfaces #1A1A1A, emerald #009975, text-free generated imagery, abstract brand-constant fallback (brief section 9)
  - conversion: signup-gate completion (new acquisition) and paid-plan subscription (owned non-payers) (brief section 3, strategy-artifact sections 1 and 4)

---

## information_architecture

One landing page. Seven sections in reading order, each earning its place against a single
conversion: start a free first lesson and complete the signup gate.

| # | Section | Job (one line) |
|---|---------|----------------|
| 1 | Hero | deliver the Summer of Skills promise and surface the one primary action: pick a field and start a free first lesson |
| 2 | Pick your field | let the visitor choose their field from a grid of the 7 confirmed domains plus an and-more tile; each tile routes to a free-first-lesson state |
| 3 | How it works / free first lesson | show the three-step path (pick a field, start the free lesson, subscribe to continue); reduce friction by naming the free try |
| 4 | Why Maharat / breadth as proof | establish that across all 7 fields the instructors set the standard; breadth is the proof, not a single name |
| 5 | Plans (placeholder) | surface the subscription options once confirmed; price and plan are ASSUMPTION slots, not invented |
| 6 | FAQ | answer the practical questions that block signup, including the non-accredited certificate framing and the free-lesson-before-payment question |
| 7 | Signup gate | the primary conversion: email or WhatsApp capture for new acquisition; for owned non-payers the gate routes to a plan selection |

Sections 1 through 3 form the top-of-funnel hook. Sections 4 through 6 handle objection and
trust. Section 7 closes the conversion. Nothing is added that does not serve one of those three
jobs.

The page is a single scrolling surface, not multi-page, consistent with the brief's conversion
path and the breadth-led angle. A sticky nav or sticky CTA bar carries the one primary action
across all sections so the visitor is never more than one tap from the gate.

---

## ux_flow

```
ENTRY: ad click (paid, per-field interest targeting) OR organic click (social, email, push)
  -> Landing page: hero, first view
     primary action visible above the fold: [start your free first lesson]
     states: first-view, scroll-in-progress

  -> Visitor scrolls OR taps the primary action
     - If tap on primary action -> jump to PICK-YOUR-FIELD state (section 2 in view)
     - If scroll -> field grid comes into view naturally

PICK-YOUR-FIELD state (section 2):
  -> 7 field tiles (Music, Cooking, Acting, Makeup, Business, Styling, Marketing)
     + 1 and-more tile (breadth reference, no instructor names, no invented fields)
  -> Visitor taps a field tile
     -> field is highlighted / selected (visual state: field-selected)
     -> primary action updates: [start free lesson in {field}]
     -> scroll or tap advances to SIGNUP GATE
  states: default-grid, field-selected, field-hover (desktop)

FREE-LESSON GATE (section 7, signup gate):
  -> Visitor sees the signup form
     - For new acquisition: email capture (or WhatsApp if platform confirmed)
     - For owned non-payer arriving via email/push: the contact is known; the gate routes
       directly to plan selection rather than re-capturing contact details
  states:
    gate-default: form at rest, field pre-populated if known contact
    gate-submitting: spinner, primary action disabled (no double-submit)
    gate-submitted: confirmation state, next step surfaced (check email or open WhatsApp)
    gate-error: inline error, one plain line, action to retry
    gate-confirmed: contact verified, lesson access granted or plan page shown

POST-GATE / LIFECYCLE ENTRY:
  -> New acquisition confirmed: lesson access unlocked, lifecycle sequence triggered
  -> Owned non-payer confirmed: routed to plan selection, subscription CTA surfaces
  -> Non-converter (no submit, scroll past gate): sticky CTA stays live; no pop-up penalty

KEY STATES TO DESIGN (build must account for each):
  first-view          hero in viewport, no field selected
  field-selected      one tile active, CTA label updated
  gate-default        form at rest
  gate-submitting     in-flight, disabled
  gate-submitted      success, next step shown
  gate-error          validation or network error, retry available
  gate-confirmed      contact verified
  lesson-unlocked     free chapter access confirmed
  plan-page-routed    owned non-payer path, plan selection in view
```

No personal or sensitive data in URL parameters at any point in this flow. Field selection
is a UI state, not a URL query param. Attribution is by event (see data-tracking-engineer
tracking-package, event: field_selected, gate_view, submit, confirm, subscription_start).

---

## wireframe

Region-level structure per section. RTL reading order (right to left, top to bottom). One
primary action per view. No visuals in the wireframe, no copy written here, all text regions
are labeled slots only.

### Sticky nav / sticky CTA bar (persistent across all sections)

```
[STICKY BAR: full width, top of viewport, z-index above page]
Right:    [Maharat logo asset, text-free]
Center:   [nav links: fields, how it works, plans, FAQ -- visible on desktop only]
Left:     [EMERALD PRIMARY ACTION BUTTON: slot LP-CTA-STICKY-AR / LP-CTA-STICKY-EN]
```

The sticky bar collapses to logo + primary action only on mobile. It does not carry a second
CTA or any competing action.

---

### Section 1: Hero

```
[HERO REGION: full-width, full-viewport-height on desktop, min 80vh on mobile]

  [BACKGROUND IMAGE REGION: text-free, brand-constant art or cleared photography]
  [safe area: horizontal center, upper 60% of frame]

  RTL reading order, right to left:

  [RIGHT COLUMN / MAIN CONTENT, 60% width desktop, full width mobile]

    [COPY REGION: HERO-HEADLINE-AR / HERO-HEADLINE-EN]
    -- empty slot, copywriter fills --

    [COPY REGION: LP-SUBHEAD-AR / LP-SUBHEAD-EN]
    -- empty slot, copywriter fills --

    [COPY REGION: LP-SUBHEAD-2-AR / LP-SUBHEAD-2-EN]  (secondary subhead or trust line, if copywriter provides)
    -- empty slot, copywriter fills, may be omitted --

    [PRIMARY ACTION BUTTON -- EMERALD #009975]
    [slot: LP-CTA-HERO-AR / LP-CTA-HERO-EN]
    -- one action only, taps to Pick-Your-Field section --

  [LEFT COLUMN / VISUAL ANCHOR, 40% width desktop, hidden below primary content on mobile]
    [IMAGE SLOT: hero visual, text-free, see web_asset_brief HERO-IMG-01]

[BOTTOM EDGE: scroll indicator, subtle, no competing action]
```

One primary action only in this view.

---

### Section 2: Pick your field

```
[SECTION: full width, background #141414]

  [SECTION HEADING REGION: slot LP-HEADLINE-FIELDS-AR / LP-HEADLINE-FIELDS-EN]
  -- empty, copywriter fills --

  [FIELD GRID: 4 columns desktop, 2 columns tablet, 1 column mobile, card surfaces #1A1A1A]

    [FIELD TILE x7: one per confirmed domain]
    Each tile contains:
      [FIELD ICON / ABSTRACT VISUAL: text-free, see web_asset_brief FIELD-ICON-xx]
      [FIELD LABEL REGION: slot FIELD-LABEL-{FIELD}-AR / FIELD-LABEL-{FIELD}-EN]
        -- Music, Cooking, Acting, Makeup, Business, Styling, Marketing --
        -- label only, no instructor name shown by default --
        -- INSTRUCTOR NAME SLOT (confirm-at-gate): FIELD-INSTRUCTOR-{FIELD}-AR / EN --
        -- slot is empty until naming confirmed; tile renders without it if empty --
      [FIELD FREE-LESSON CTA: slot FIELD-CTA-{FIELD}-AR / EN]
        -- minor, inline, not competing with the section-level primary action --

    [AND-MORE TILE (8th tile): breadth reference]
      [ABSTRACT VISUAL: text-free, brand-constant pattern]
      [SLOT: FIELD-LABEL-MORE-AR / FIELD-LABEL-MORE-EN]
      -- no instructor names, no invented field names --

  [SECTION PRIMARY ACTION: one emerald button below the grid]
  [slot: LP-CTA-FIELDS-AR / LP-CTA-FIELDS-EN]
  -- if field is already selected, label updates via UI state; one action only --
```

Field selection updates UI state. It does not navigate away or open a new page; the visitor
stays on the landing page. The field-selected state feeds the signup gate (section 7) so the
gate knows which field to confirm access for.

---

### Section 3: How it works / free first lesson

```
[SECTION: full width, background #141414]

  [SECTION HEADING REGION: slot LP-HEADLINE-HOW-AR / LP-HEADLINE-HOW-EN]
  -- empty, copywriter fills --

  [3-STEP ROW: horizontal desktop, stacked mobile, RTL reading order]

    Step 1:
      [STEP ICON: abstract, text-free]
      [STEP HEADING SLOT: HOW-STEP1-AR / HOW-STEP1-EN]
      [STEP BODY SLOT: HOW-STEP1-BODY-AR / HOW-STEP1-BODY-EN]

    Step 2:
      [STEP ICON: abstract, text-free]
      [STEP HEADING SLOT: HOW-STEP2-AR / HOW-STEP2-EN]
      [STEP BODY SLOT: HOW-STEP2-BODY-AR / HOW-STEP2-BODY-EN]

    Step 3:
      [STEP ICON: abstract, text-free]
      [STEP HEADING SLOT: HOW-STEP3-AR / HOW-STEP3-EN]
      [STEP BODY SLOT: HOW-STEP3-BODY-AR / HOW-STEP3-BODY-EN]

  [NO PRIMARY ACTION IN THIS SECTION]
  -- the sticky bar carries the action; no competing CTA here --
```

This section reduces friction by naming the free-first-lesson offer explicitly. It is the
"what happens next" answer before the visitor reaches the gate.

---

### Section 4: Why Maharat / breadth as proof

```
[SECTION: full width, background #1A1A1A (card surface, contrast from adjacent sections)]

  [SECTION HEADING REGION: slot LP-HEADLINE-WHY-AR / LP-HEADLINE-WHY-EN]
  -- empty, copywriter fills --

  [SECTION SUBHEAD REGION: slot LP-SUBHEAD-WHY-AR / LP-SUBHEAD-WHY-EN]
  -- breadth-as-proof framing, empowering, never deficit-framed; copywriter fills --

  [PROOF GRID: 3 columns desktop, stacked mobile]
    Each proof tile:
      [ABSTRACT FIELD VISUAL: text-free, brand-constant]
      [PROOF HEADING SLOT: WHY-PROOF-{N}-AR / WHY-PROOF-{N}-EN]
        -- anchored to page-sourced, cleared facts only (chapter counts, free chapter 1,
           field labels); no invented claims, no accreditation --
      [PROOF BODY SLOT: WHY-PROOF-{N}-BODY-AR / WHY-PROOF-{N}-BODY-EN]

  [INSTRUCTOR ROSTER STRIP (optional, confirm-at-gate)]
    -- A horizontal strip of field labels with cleared instructor names IF
       per-instructor naming is confirmed. If not confirmed, this sub-region is omitted.
       The section functions without it. --
    [INSTRUCTOR-STRIP-SLOT-AR / EN: confirm-at-gate, all 7 names, no invented names]

  [NO PRIMARY ACTION IN THIS SECTION]
  -- sticky bar carries the action --
```

This section establishes the platform breadth, not a single instructor. It is value-led proof
that across every field in the grid, the standard is high.

---

### Section 5: Plans (placeholder)

```
[SECTION: full width, background #141414]

  [SECTION HEADING REGION: slot LP-HEADLINE-PLANS-AR / LP-HEADLINE-PLANS-EN]
  -- empty, copywriter fills --

  [PLANS GRID: 3 columns desktop (for 1, 3, 12 month plans once confirmed), stacked mobile]
    Each plan tile (card surface #1A1A1A):
      [PLAN LABEL SLOT: PLAN-LABEL-{N}-AR / PLAN-LABEL-{N}-EN]
        -- plan duration only; actual plan name and duration are ASSUMPTION, not invented --
      [PLAN PRICE SLOT: PLAN-PRICE-{N}-AR / PLAN-PRICE-{N}-EN]
        -- EMPTY: price is ASSUMPTION; this slot only fills if Ahmed confirms price and currency --
      [PLAN FEATURES SLOT: PLAN-FEATURES-{N}-AR / PLAN-FEATURES-{N}-EN]
      [PLAN CTA SLOT: PLAN-CTA-{N}-AR / PLAN-CTA-{N}-EN]
        -- one CTA per tile, no competing CTAs within the tile --

  [PROMO BANNER SLOT (below grid): PROMO-BANNER-AR / PROMO-BANNER-EN]
    -- EMPTY: only appears if Ahmed confirms a summer trial, discount, or bundle --
    -- If empty, region is hidden; layout reflows without it --

  [SECTION-LEVEL CTA: one emerald button]
  [slot: LP-CTA-PLANS-AR / LP-CTA-PLANS-EN]
  -- links to the signup gate (section 7); one action only --
```

This section is a structural placeholder. No prices, plan names, or promo claims are
invented. The section renders without price or promo slots if those remain unconfirmed;
the layout must accommodate both states.

---

### Section 6: FAQ

```
[SECTION: full width, background #1A1A1A]

  [SECTION HEADING REGION: slot LP-HEADLINE-FAQ-AR / LP-HEADLINE-FAQ-EN]
  -- empty, copywriter fills --

  [FAQ ACCORDION: RTL, questions right-aligned, answers below on expand]

    Q1: [slot FAQ-Q1-AR / FAQ-Q1-EN] -- the free-first-lesson question (what is free, what is paid)
        [slot FAQ-A1-AR / FAQ-A1-EN]

    Q2: [slot FAQ-Q2-AR / FAQ-Q2-EN] -- the certificate question (non-accredited framing)
        [slot FAQ-A2-AR / FAQ-A2-EN]
        -- direction note for copywriter: framing must be "شهادة مخصصة باسمك" pattern,
           never accredited, consistent with brand-voice.md --

    Q3: [slot FAQ-Q3-AR / FAQ-Q3-EN] -- the subscription question (what do I get, can I cancel)
        [slot FAQ-A3-AR / FAQ-A3-EN]

    Q4: [slot FAQ-Q4-AR / FAQ-Q4-EN] -- the field question (can I access all fields or just one)
        [slot FAQ-A4-AR / FAQ-A4-EN]

    Q5: [slot FAQ-Q5-AR / FAQ-Q5-EN] -- the instructor question (who teaches, how do I know they are good)
        [slot FAQ-A5-AR / FAQ-A5-EN]
        -- direction note: anchor to cleared, page-sourced field credentials only;
           no invented claims, no accreditation --

  [NO PRIMARY ACTION IN THIS SECTION]
  -- sticky bar carries the action --
```

The FAQ section exists to remove blockers at the plan step. Q2 (certificate framing) and
Q5 (instructor credibility) are non-negotiable for the non-accredited guardrail and the
naming discipline. The direction notes are signals to the copywriter, not copy.

---

### Section 7: Signup gate

```
[SECTION: full width, background #141414, section id: signup-gate]

  [SECTION HEADING REGION: slot LP-HEADLINE-GATE-AR / LP-HEADLINE-GATE-EN]
  -- empty, copywriter fills --

  [SECTION SUBHEAD REGION: slot LP-SUBHEAD-GATE-AR / LP-SUBHEAD-GATE-EN]
  -- field-sensitive: if a field was selected, subhead reflects the field; copywriter supplies
     both a field-generic variant and per-field variants for the 7 domains --

  [GATE FORM: RTL]

    [FIELD-DISPLAY REGION: shows the selected field label, or field-generic if none selected]
    -- reads from UI state, not a form input, no PII in URL --

    [EMAIL INPUT: labeled, RTL-correct placeholder, required field]
    [slot GATE-EMAIL-LABEL-AR / GATE-EMAIL-LABEL-EN]
    [REQUIRED INDICATOR: an asterisk (*) immediately adjacent to the label text, plus a note
     at the top of the form reading "* required field" (slot GATE-REQUIRED-NOTE-AR /
     GATE-REQUIRED-NOTE-EN, copywriter fills). The required status is conveyed by both the
     asterisk symbol and the explanatory label text, not by color alone.]
    [slot GATE-EMAIL-PLACEHOLDER-AR / GATE-EMAIL-PLACEHOLDER-EN]
    -- OR WhatsApp input if gate platform confirmed as WhatsApp; layout accommodates both;
       final rendering depends on platform confirmation (OPEN ITEM) --

    [CONSENT LINE: one line, compliant, below the input]
    [slot GATE-CONSENT-AR / GATE-CONSENT-EN]
    -- compliance-privacy-reviewer runs on this copy; Saudi PDPL posture is OPEN ITEM --

    [PRIMARY SUBMIT BUTTON: EMERALD #009975]
    [slot: LP-CTA-GATE-AR / LP-CTA-GATE-EN]
    -- one action only; disabled during submission --

  [STATE: gate-submitting]
    -- submit button shows spinner; all inputs disabled; no double-submit possible --

  [STATE: gate-submitted (success)]
    [slot: GATE-SUCCESS-HEADING-AR / GATE-SUCCESS-HEADING-EN]
    [slot: GATE-SUCCESS-BODY-AR / GATE-SUCCESS-BODY-EN]
    -- next step surfaced (check email or open WhatsApp); no competing action --

  [STATE: gate-error]
    [slot: GATE-ERROR-AR / GATE-ERROR-EN]
    -- one plain line, inline, retry action available; no alarming language --

  [STATE: gate-confirmed (for owned non-payer path)]
    -- plan selection or lesson access surfaced; owned non-payer is not re-captured --
```

No personal or sensitive data in URL parameters. Field selection is a UI state variable,
not a query parameter. The gate platform (email vs WhatsApp) is OPEN ITEM; the form
structure accommodates both without redesign.

---

## visual_direction

### Brand constants applied to this web surface

- Background: #141414 (near-black). The page is built on this ground. No white, no
  off-brand light backgrounds.
- Card surfaces: #1A1A1A. Field tiles, plan tiles, FAQ accordion rows, and proof grid
  tiles use this surface to lift off the background without introducing a third neutral.
- Primary accent, emerald #009975: the primary action button only (sticky CTA, hero CTA,
  field section CTA, plans CTA, gate submit button). The accent is a highlight, not a flood.
  No emerald on decorative elements, no emerald on text outside the CTA.
- Type: Arabic primary, Latin secondary. All type is overlaid copy, bound by variant id,
  never baked into imagery. RTL direction across all text regions.
- Spacing: generous. The page breathes. Cards do not crowd each other. Premium and
  uncluttered is the governing register.

### Imagery direction

- All imagery is text-free. No Arabic, no English, no numerals baked into any generated or
  supplied asset. Copy overlays in build via the labeled slots.
- No generated instructor likeness. No generated human face. The risk of generated Arabic
  script mangling (tatweel, broken glyphs) and generated likeness misrepresentation are both
  hard stops.
- Confirmed fallback (used until rights-cleared photography is confirmed): abstract,
  premium, brand-constant art. This means geometric or texture-based visuals in the
  #141414 / #1A1A1A palette with restrained emerald accents, suggesting craft, skill, and
  ambition without depicting people or writing. The campaign's breadth-led angle works in
  this register: many fields, one aesthetic.
- If and when rights-cleared photography is confirmed for any named instructor, that
  photography replaces the abstract fallback in that field's card and, if used in the hero,
  in the hero image slot. The safe-area constraints below still apply. Cleared photography
  is never generated.
- Summer energy sits on top of the global brand voice: warm light, clean craft details,
  aspiration. The palette stays dark and premium; warmth comes from the content and the
  framing, not from a bright or off-brand background.

### RTL visual priority

- Reading order right to left, top to bottom, across all sections.
- The hero primary content column is on the right; the visual anchor is on the left.
- The field grid starts from the right tile in RTL reading order.
- All form inputs are RTL-correct: label alignment, placeholder direction, cursor behavior.
- Mixed Arabic, English, and Western numerals hold direction correctly. Western numerals only
  (0 through 9), never Eastern Arabic-Indic digits.

---

## web_asset_brief

All assets are text-free. Copy-overlay slots are labeled (AR / EN) and empty. Copywriters
fill them; nothing is pre-written here. No generated instructor likeness in any asset.

### HERO-IMG-01: Hero background / visual anchor

| Field | Value |
|-------|-------|
| Asset id | HERO-IMG-01 |
| Use | Hero section background or right-column visual anchor |
| Content direction | Abstract brand-constant art. Premium, craft-suggestive. No faces, no text, no Arabic script. Geometric or texture-based in #141414 / #1A1A1A with restrained emerald highlight. If rights-cleared photography exists at build time, it replaces this with a cleared supplied image. |
| Desktop dimensions | 1440 x 900 px minimum, 16:9 ratio |
| Mobile dimensions | 390 x 488 px minimum, 4:5 ratio |
| Safe area | Center horizontal band, upper 60% of frame: no critical content in the lower 40% (masked by copy overlay on desktop) and no critical content in the left 30% of the desktop asset (text column overlaps) |
| Copy-overlay slots | [HERO-HEADLINE-AR] top-right of safe area, empty / [HERO-HEADLINE-EN] top-right of safe area, empty |
| Generation note | Text-free. Do not generate Arabic. If a generative tool is used for the abstract art, confirm Arabic-capability check is not needed (no text requested). |
| Fallback | Abstract brand-constant art as above is the confirmed fallback if no photography is supplied. |

---

### FIELD-ICON-xx: Field tile visuals (7 fields plus and-more tile)

| Field | Value |
|-------|-------|
| Asset ids | FIELD-ICON-MUSIC, FIELD-ICON-COOKING, FIELD-ICON-ACTING, FIELD-ICON-MAKEUP, FIELD-ICON-BUSINESS, FIELD-ICON-STYLING, FIELD-ICON-MARKETING, FIELD-ICON-MORE |
| Use | Field grid tiles in the Pick-Your-Field section |
| Content direction | Abstract, field-suggestive. Music: waveform or instrument silhouette (no face). Cooking: ingredient or utensil detail (no face). Acting: abstract stage or expression symbol (no face). Makeup: brush or palette detail (no face). Business: abstract grid or growth form (no face). Styling: fabric or accessory detail (no face). Marketing: abstract signal or reach form (no face). And-more: brand-constant pattern suggesting breadth (no faces, no text). |
| Dimensions | 400 x 400 px, square. Responsive: displayed at 1:1 ratio in the grid. |
| Safe area | Full frame usable: no copy overlay on the field icon itself. Copy (field label, instructor name confirm-at-gate, CTA) is below the icon within the tile card. |
| Copy-overlay slots | None on the image. Copy slots are in the card region below the image: [FIELD-LABEL-{FIELD}-AR] / [FIELD-LABEL-{FIELD}-EN] / [FIELD-INSTRUCTOR-{FIELD}-AR] (confirm-at-gate, may be empty) / [FIELD-INSTRUCTOR-{FIELD}-EN] (confirm-at-gate, may be empty) |
| Generation note | Text-free. No Arabic script, no numerals baked in. Abstract only, no human faces. |

---

### HOW-ICON-xx: How-it-works step icons

| Field | Value |
|-------|-------|
| Asset ids | HOW-ICON-01, HOW-ICON-02, HOW-ICON-03 |
| Use | Step 1, 2, 3 icons in the How It Works section |
| Content direction | Simple, abstract, line-art or solid icon style. Step 1 (pick a field): a branching or selection form. Step 2 (start the free lesson): a play or opening form. Step 3 (subscribe to continue): an unlock or progression form. No faces, no text. |
| Dimensions | 80 x 80 px at 1x, SVG preferred for resolution independence |
| Safe area | Full frame usable |
| Copy-overlay slots | None on the icon. Step copy is in the text region below the icon: [HOW-STEP{N}-AR] / [HOW-STEP{N}-EN] |

---

### WHY-PROOF-xx: Breadth-proof section visuals

| Field | Value |
|-------|-------|
| Asset ids | WHY-PROOF-01, WHY-PROOF-02, WHY-PROOF-03 |
| Use | 3-tile proof grid in the Why Maharat section |
| Content direction | Abstract, craft-suggestive, brand-constant. Each tile suggests a different field or dimension of quality: one could suggest depth (layers, levels), one breadth (multiple forms), one access (an opening or path form). No faces, no text, no Arabic script. |
| Dimensions | 480 x 320 px, 3:2 ratio |
| Safe area | Center 60% of frame: copy overlay occupies the lower 40% of the tile area |
| Copy-overlay slots | [WHY-PROOF-{N}-AR] / [WHY-PROOF-{N}-EN] in the lower overlay band, empty |

---

### Copy-overlay slot index (all empty, for copywriter-ar and copywriter-en)

This index maps every labeled slot to the downstream owner. No copy is written here.
Variant id prefix convention follows the brief naming: LP-HEADLINE-*, LP-SUBHEAD-*, LP-CTA-*,
HERO-*, FIELD-*, HOW-*, WHY-*, PLAN-*, FAQ-*, GATE-*.

| Slot id pattern | Region | Language | Owner |
|-----------------|---------|----------|-------|
| HERO-HEADLINE-AR | Hero headline | Arabic | copywriter-ar |
| HERO-HEADLINE-EN | Hero headline | English | copywriter-en |
| LP-SUBHEAD-AR | Hero subhead | Arabic | copywriter-ar |
| LP-SUBHEAD-EN | Hero subhead | English | copywriter-en |
| LP-CTA-HERO-AR | Hero primary action | Arabic | copywriter-ar |
| LP-CTA-HERO-EN | Hero primary action | English | copywriter-en |
| LP-CTA-STICKY-AR | Sticky bar CTA | Arabic | copywriter-ar |
| LP-CTA-STICKY-EN | Sticky bar CTA | English | copywriter-en |
| LP-HEADLINE-FIELDS-AR | Fields section heading | Arabic | copywriter-ar |
| LP-HEADLINE-FIELDS-EN | Fields section heading | English | copywriter-en |
| FIELD-LABEL-{FIELD}-AR | Per-field tile label (7 fields) | Arabic | copywriter-ar |
| FIELD-LABEL-{FIELD}-EN | Per-field tile label (7 fields) | English | copywriter-en |
| FIELD-INSTRUCTOR-{FIELD}-AR | Per-field instructor name (confirm-at-gate) | Arabic | copywriter-ar |
| FIELD-INSTRUCTOR-{FIELD}-EN | Per-field instructor name (confirm-at-gate) | English | copywriter-en |
| FIELD-CTA-{FIELD}-AR | Per-field tile inline CTA | Arabic | copywriter-ar |
| FIELD-CTA-{FIELD}-EN | Per-field tile inline CTA | English | copywriter-en |
| FIELD-LABEL-MORE-AR | And-more tile label | Arabic | copywriter-ar |
| FIELD-LABEL-MORE-EN | And-more tile label | English | copywriter-en |
| LP-CTA-FIELDS-AR | Fields section primary CTA | Arabic | copywriter-ar |
| LP-CTA-FIELDS-EN | Fields section primary CTA | English | copywriter-en |
| LP-HEADLINE-HOW-AR | How it works heading | Arabic | copywriter-ar |
| LP-HEADLINE-HOW-EN | How it works heading | English | copywriter-en |
| HOW-STEP{N}-AR | How-it-works step heading (3 steps) | Arabic | copywriter-ar |
| HOW-STEP{N}-EN | How-it-works step heading (3 steps) | English | copywriter-en |
| HOW-STEP{N}-BODY-AR | How-it-works step body (3 steps) | Arabic | copywriter-ar |
| HOW-STEP{N}-BODY-EN | How-it-works step body (3 steps) | English | copywriter-en |
| LP-HEADLINE-WHY-AR | Why Maharat heading | Arabic | copywriter-ar |
| LP-HEADLINE-WHY-EN | Why Maharat heading | English | copywriter-en |
| LP-SUBHEAD-WHY-AR | Why Maharat subhead | Arabic | copywriter-ar |
| LP-SUBHEAD-WHY-EN | Why Maharat subhead | English | copywriter-en |
| WHY-PROOF-{N}-AR | Breadth proof tile copy (3 tiles) | Arabic | copywriter-ar |
| WHY-PROOF-{N}-EN | Breadth proof tile copy (3 tiles) | English | copywriter-en |
| INSTRUCTOR-STRIP-AR | Instructor name strip (confirm-at-gate) | Arabic | copywriter-ar |
| INSTRUCTOR-STRIP-EN | Instructor name strip (confirm-at-gate) | English | copywriter-en |
| LP-HEADLINE-PLANS-AR | Plans section heading | Arabic | copywriter-ar |
| LP-HEADLINE-PLANS-EN | Plans section heading | English | copywriter-en |
| PLAN-LABEL-{N}-AR | Plan tile label (ASSUMPTION) | Arabic | copywriter-ar |
| PLAN-LABEL-{N}-EN | Plan tile label (ASSUMPTION) | English | copywriter-en |
| PLAN-PRICE-{N}-AR | Plan price (ASSUMPTION, empty until confirmed) | Arabic | copywriter-ar |
| PLAN-PRICE-{N}-EN | Plan price (ASSUMPTION, empty until confirmed) | English | copywriter-en |
| PLAN-FEATURES-{N}-AR | Plan features list | Arabic | copywriter-ar |
| PLAN-FEATURES-{N}-EN | Plan features list | English | copywriter-en |
| PLAN-CTA-{N}-AR | Plan tile CTA | Arabic | copywriter-ar |
| PLAN-CTA-{N}-EN | Plan tile CTA | English | copywriter-en |
| PROMO-BANNER-AR | Promo banner (ASSUMPTION, empty until confirmed) | Arabic | copywriter-ar |
| PROMO-BANNER-EN | Promo banner (ASSUMPTION, empty until confirmed) | English | copywriter-en |
| LP-CTA-PLANS-AR | Plans section primary CTA | Arabic | copywriter-ar |
| LP-CTA-PLANS-EN | Plans section primary CTA | English | copywriter-en |
| LP-HEADLINE-FAQ-AR | FAQ heading | Arabic | copywriter-ar |
| LP-HEADLINE-FAQ-EN | FAQ heading | English | copywriter-en |
| FAQ-Q{N}-AR | FAQ question (5 questions) | Arabic | copywriter-ar |
| FAQ-Q{N}-EN | FAQ question (5 questions) | English | copywriter-en |
| FAQ-A{N}-AR | FAQ answer (5 answers) | Arabic | copywriter-ar |
| FAQ-A{N}-EN | FAQ answer (5 answers) | English | copywriter-en |
| LP-HEADLINE-GATE-AR | Signup gate heading | Arabic | copywriter-ar |
| LP-HEADLINE-GATE-EN | Signup gate heading | English | copywriter-en |
| LP-SUBHEAD-GATE-AR | Signup gate subhead (field-sensitive) | Arabic | copywriter-ar |
| LP-SUBHEAD-GATE-EN | Signup gate subhead (field-sensitive) | English | copywriter-en |
| GATE-EMAIL-LABEL-AR | Email input label (includes asterisk required indicator adjacent to label text) | Arabic | copywriter-ar |
| GATE-EMAIL-LABEL-EN | Email input label (includes asterisk required indicator adjacent to label text) | English | copywriter-en |
| GATE-REQUIRED-NOTE-AR | Required field explanatory note at top of gate form ("* required field" or Arabic equivalent) | Arabic | copywriter-ar |
| GATE-REQUIRED-NOTE-EN | Required field explanatory note at top of gate form | English | copywriter-en |
| GATE-EMAIL-PLACEHOLDER-AR | Email input placeholder | Arabic | copywriter-ar |
| GATE-EMAIL-PLACEHOLDER-EN | Email input placeholder | English | copywriter-en |
| GATE-CONSENT-AR | Consent line (compliance-reviewed) | Arabic | copywriter-ar |
| GATE-CONSENT-EN | Consent line (compliance-reviewed) | English | copywriter-en |
| LP-CTA-GATE-AR | Gate submit CTA | Arabic | copywriter-ar |
| LP-CTA-GATE-EN | Gate submit CTA | English | copywriter-en |
| GATE-SUCCESS-HEADING-AR | Gate success state heading | Arabic | copywriter-ar |
| GATE-SUCCESS-HEADING-EN | Gate success state heading | English | copywriter-en |
| GATE-SUCCESS-BODY-AR | Gate success state body | Arabic | copywriter-ar |
| GATE-SUCCESS-BODY-EN | Gate success state body | English | copywriter-en |
| GATE-ERROR-AR | Gate error state line | Arabic | copywriter-ar |
| GATE-ERROR-EN | Gate error state line | English | copywriter-en |

---

## conversion_intent

The single primary action this page optimizes toward: signup-gate completion, which for new
acquisition is email (or WhatsApp, once platform confirmed) capture unlocking a free first
lesson, and for owned non-payers is routing to plan selection and subscription start.

The page has one primary action visible at every scroll depth (sticky CTA bar) and one
primary action in each individual section. The field-selection step (section 2) is a
qualifying micro-interaction that personalizes the gate and the free-lesson routing; it is
not a competing conversion event. The How It Works section (3) and the FAQ section (6) are
objection-reduction; they serve the gate completion, not a separate goal.

Every section and every design decision is traceable to this single intent. The plans section
is not a competing conversion; it is context for the gate (what happens after you sign up and
want to continue). The FAQ certificate framing is not a product claim; it removes a blocker
to gate completion.

If a visitor does not complete the gate: the sticky CTA stays live; the lifecycle sequence
(email, push) carries the follow-up once their contact is in the owned list. No pop-up or
interstitial penalty before the gate.

---

## design_spec (web-designer to complete)

Produced by web-designer from the direction above. Build-ready specification for
conversion-engineer to implement. No copy is written here. Every text region is bound to a
QA-passed copy-package variant id. All imagery is text-free. Arabic is never baked into a
generated asset.

---

### components

| Component id | Region | Notes |
|---|---|---|
| COMP-STICKY-NAV | Persistent sticky bar, top of viewport | Logo right, nav links center (desktop only), emerald primary CTA left; collapses to logo + CTA on mobile; z-index: 100 |
| COMP-HERO | Section 1 full-viewport hero | Background image slot (HERO-IMG-01, text-free), two-column layout (content right 60%, visual left 40% desktop; stacked single-column mobile); one primary emerald CTA; scroll indicator at bottom edge |
| COMP-FIELD-GRID | Section 2, pick-your-field | 8-tile grid (7 field tiles + 1 and-more tile); card surface #1A1A1A; tiles carry abstract field icon, field label slot, confirm-at-gate instructor name slot, inline field CTA; interactive: field-selected state updates the section CTA label; one section-level primary emerald CTA below the grid |
| COMP-HOW-IT-WORKS | Section 3, three-step path | Three horizontal steps on desktop, stacked vertically on mobile; each step: abstract icon (HOW-ICON-xx, SVG), step heading slot, step body slot; no CTA in this section |
| COMP-WHY-MAHARAT | Section 4, breadth proof, #1A1A1A surface | Section heading and subhead slots; 3-tile proof grid (WHY-PROOF-xx, text-free visual, lower copy overlay band); optional confirm-at-gate instructor roster strip below the grid; no CTA in this section |
| COMP-PLANS | Section 5, plan tiles, placeholder | 3-column desktop, stacked mobile; each plan tile: label, price (ASSUMPTION slot, empty until confirmed), features list, tile CTA; promo banner slot below grid (hidden until confirmed); one section-level primary emerald CTA |
| COMP-FAQ | Section 6, accordion | RTL accordion; 5 Q and A pairs; question right-aligned, answer expands below; no CTA in this section |
| COMP-GATE | Section 7, signup gate | Gate heading, field-sensitive subhead, field-display region (from UI state, not a form input), email or WhatsApp input (platform OPEN ITEM, layout accommodates both), consent line, primary emerald submit CTA; five gate states: default, submitting, submitted, error, confirmed |
| COMP-GATE-SUCCESS | Gate state: submitted | Heading and body slots; no competing action |
| COMP-GATE-ERROR | Gate state: error | One inline error line, retry action |
| COMP-GATE-CONFIRMED | Gate state: confirmed (owned non-payer) | Plan selection or lesson access surfaced |

Interactive components with all required states: COMP-STICKY-NAV (default, scrolled),
COMP-FIELD-GRID tiles (default, hover, focus, active, field-selected), COMP-PLANS tiles (default,
hover, focus), COMP-FAQ rows (collapsed, expanded, focus), COMP-GATE inputs (default, focus,
error), COMP-GATE submit button (default, hover, focus, active, disabled, loading), COMP-HOW-IT-WORKS
and COMP-WHY-MAHARAT are static display components with no interactive states beyond focus on any
internal links.

---

### responsive grid

Mobile-first. Three named breakpoints. All values in Western numerals (px).

| Breakpoint name | Min-width | Columns | Gutter | Outer margin |
|---|---|---|---|---|
| sm (mobile) | 0 px | 4 | 16 px | 16 px |
| md (tablet) | 768 px | 8 | 24 px | 32 px |
| lg (desktop) | 1280 px | 12 | 32 px | 80 px |

Max content width: 1440 px, centered. The grid is a CSS Grid implementation with named
column tracks. No layout relies on float or absolute positioning for column flow.

Section-level column usage:

| Section | sm | md | lg |
|---|---|---|---|
| Hero (content column) | 4 of 4 | 5 of 8 (right-aligned RTL) | 7 of 12 (right-aligned RTL) |
| Hero (visual column) | hidden (below content) | 3 of 8 (left of content RTL) | 5 of 12 (left of content RTL) |
| Field grid tiles | 1 per row (4-col full width) | 2 per row (4 cols each) | 3 per row (4 cols each) |
| How it works steps | stacked, 4 of 4 | 3 equal cols across 8 | 3 equal cols across 12 |
| Why Maharat proof tiles | stacked, 4 of 4 | 3 equal cols across 8 | 4 cols each across 12 |
| Plans tiles | stacked, 4 of 4 | stacked, 8 of 8 | 4 cols each across 12 |
| FAQ | 4 of 4 | 6 of 8 centered | 8 of 12 centered |
| Gate form | 4 of 4 | 4 of 8 centered | 4 of 12 centered |

---

### type scale (Arabic-first)

Arabic typeface: system Arabic stack as the safe web font baseline, with a premium Arabic web
font slot (to be confirmed at build; must have full Arabic glyph coverage, no tatweel, correct
RTL kerning). Latin typeface: system sans-serif stack as baseline, with a premium Latin web font
slot. No typeface decision invents a specific font name; the build-tool and font decision goes
through the approval process before implementation.

Scale defined in rem units, base 16 px. All rendered numerals are Western 0 to 9.

| Role | Size (rem) | Weight | Line-height | Usage |
|---|---|---|---|---|
| display | 3.5 rem (56 px) | 700 | 1.15 | Hero headline on lg |
| h1 | 2.75 rem (44 px) | 700 | 1.2 | Hero headline on md; section headlines on lg |
| h2 | 2 rem (32 px) | 600 | 1.25 | Section headlines on sm and md; hero on sm |
| h3 | 1.5 rem (24 px) | 600 | 1.3 | Step headings, proof tile headings, plan labels |
| body-lg | 1.125 rem (18 px) | 400 | 1.6 | Hero subhead, section subheads, email preview line |
| body | 1 rem (16 px) | 400 | 1.65 | Body copy, FAQ answers, plan features, gate labels |
| body-sm | 0.875 rem (14 px) | 400 | 1.6 | Captions, consent line, inline field CTAs |
| cta | 1 rem (16 px) | 600 | 1 | All button labels (sticky CTA, hero CTA, gate submit) |
| label | 0.75 rem (12 px) | 500 | 1.4 | Input labels, step numbers |

Arabic text rendering notes: direction: rtl on the html element and all text containers.
unicode-bidi: embed on mixed-direction inline elements. font-feature-settings: "kern" 1 on all
Arabic type. No letter-spacing applied to Arabic text (breaks Arabic script). Letter-spacing
may be applied to Latin type only where the font supports it.

---

### design tokens

All tokens are named and applied in build via CSS custom properties (or a token layer if the
build system supports one). Values are constants; no one-off hex values outside these tokens.

#### color tokens

| Token name | Value | Usage |
|---|---|---|
| color-bg | #141414 | Page background, section backgrounds (sections 1, 2, 3, 5, 7) |
| color-surface | #1A1A1A | Card surfaces: field tiles, plan tiles, proof tiles, FAQ rows, sticky nav background |
| color-accent | #009975 | Primary action buttons only: sticky CTA, hero CTA, field section CTA, plans CTA, gate submit button. Accent is a highlight, not a flood. No emerald on decorative elements or body text. |
| color-accent-hover | #007f62 | Primary button hover state (10% darkened accent, still accessible) |
| color-accent-active | #006b52 | Primary button active/pressed state |
| color-accent-disabled | #009975 at 30% opacity | Primary button disabled state |
| color-text-primary | #F5F5F5 | Primary text on dark backgrounds |
| color-text-on-accent | #141414 | CTA button label color on the emerald #009975 fill. Near-black on emerald yields approximately 5.7:1, passing WCAG 2.2 AA for normal text (threshold 4.5:1). This replaces the prior #F5F5F5-on-emerald pairing (3.30:1, which failed AA for normal text at 16 px 600 weight). Applies to every instance of the emerald CTA button: sticky CTA, hero CTA, field section CTA, plans CTA, gate submit button. |
| color-text-secondary | #A8A8A8 | Secondary text, labels, captions, inactive states |
| color-text-disabled | #6B6B6B | Disabled text |
| color-border | #2A2A2A | Card borders, dividers, input borders at rest |
| color-border-focus | #009975 | Input and interactive element focus ring |
| color-border-error | #E53935 | Error state border only (2 px border on a UI component requires 3:1 non-text contrast; #E53935 on #1A1A1A is 4.19:1, passing 3:1). Do NOT use this token for error text. |
| color-text-error | #F04040 | Error text label (rendered at body-sm: 14 px weight 400). #F04040 on #1A1A1A yields approximately 4.6:1, passing WCAG 2.2 AA normal-text threshold of 4.5:1. This replaces the prior use of #E53935 for error text (#E53935 on #1A1A1A is 4.19:1, which fails AA for normal text). Usage: error message text below the gate input only. The border token (color-border-error) is unchanged. |
| color-overlay-dark | rgba(20,20,20,0.72) | Hero image overlay (ensures text contrast over imagery) |
| color-success | #00C49A | Gate-submitted success indicator (distinct from accent, not a CTA) |

#### spacing tokens

Base unit: 4 px. All spacing is a multiple of 4.

| Token name | Value | Usage |
|---|---|---|
| space-1 | 4 px | Micro spacing, inline gaps |
| space-2 | 8 px | Tight component padding |
| space-3 | 12 px | Small internal padding |
| space-4 | 16 px | Standard component padding, small gap |
| space-5 | 20 px | Medium gap |
| space-6 | 24 px | Card internal padding (sm), section element gap |
| space-8 | 32 px | Card internal padding (md, lg), section sub-element gap |
| space-10 | 40 px | Section heading margin-bottom |
| space-12 | 48 px | Large section gap |
| space-16 | 64 px | Section padding-top and padding-bottom (sm) |
| space-20 | 80 px | Section padding-top and padding-bottom (md) |
| space-24 | 96 px | Section padding-top and padding-bottom (lg) |

#### radius tokens

| Token name | Value | Usage |
|---|---|---|
| radius-sm | 4 px | Input fields, small elements |
| radius-md | 8 px | Field tiles, plan tiles, FAQ rows |
| radius-lg | 12 px | Proof tiles, how-it-works step cards (if card treatment) |
| radius-pill | 999 px | Primary CTA buttons (the signature emerald buttons) |

#### elevation tokens (box-shadow)

| Token name | Value | Usage |
|---|---|---|
| elevation-card | 0 2px 8px rgba(0,0,0,0.32) | Field tiles, plan tiles at rest |
| elevation-card-hover | 0 4px 16px rgba(0,0,0,0.48) | Field tiles on hover (desktop) |
| elevation-sticky | 0 2px 12px rgba(0,0,0,0.6) | Sticky nav when page is scrolled |

---

### interaction states

Every interactive element has a complete state set. State transitions use CSS transitions,
max 200 ms duration, ease-out easing. No janky or overly complex animations. Reduced-motion
media query: all transitions reduce to instant or cross-fade for users with prefers-reduced-motion.

#### primary CTA button (emerald, applies to sticky CTA, hero CTA, field section CTA, plans CTA, gate submit)

| State | Visual spec |
|---|---|
| default | Background color-accent (#009975), text color-text-on-accent (#141414), border-radius radius-pill, padding space-4 space-8 (16 px 32 px), font-weight 600, min-height 48 px, min-width 160 px. Near-black label on emerald fill: approximately 5.7:1, passes WCAG 2.2 AA for normal text. |
| hover (desktop only) | Background color-accent-hover (#007f62), text color-text-on-accent (#141414), box-shadow elevation-card-hover, cursor pointer |
| focus | Background color-accent, outline: 2 px solid color-border-focus, outline-offset 2 px (visible focus ring, not suppressed) |
| active | Background color-accent-active (#006b52), scale 0.98 transform |
| disabled | Background color-accent-disabled (30% opacity), cursor not-allowed, pointer-events none |
| loading | Background color-accent, spinner icon (animated SVG, 20 px, color-text-primary) centered, text hidden, button width locked to prevent layout shift |

#### field tile (COMP-FIELD-GRID, applies to each of the 8 tiles)

| State | Visual spec |
|---|---|
| default | Background color-surface (#1A1A1A), border 1 px solid color-border, border-radius radius-md, padding space-6 |
| hover (desktop) | Border color color-accent (#009975) at full opacity (1 px solid), box-shadow elevation-card-hover, cursor pointer. Full-opacity #009975 on #1A1A1A is approximately 4.90:1, passing WCAG 1.4.11 non-text contrast threshold of 3:1. The prior 60% opacity treatment yielded approximately 2.4:1 effective contrast and failed 3:1. |
| focus | Outline 2 px solid color-border-focus, outline-offset 2 px |
| active | Background color-surface, border color-accent, scale 0.99 |
| field-selected | Border 2 px solid color-accent, background #1F2E2A (surface with slight emerald tint, derived: color-surface blended with color-accent at 8%), section CTA label updates to field-specific copy via UI state |

#### FAQ accordion row

| State | Visual spec |
|---|---|
| default (collapsed) | Background color-surface, border-bottom 1 px solid color-border, question text color-text-primary, expand icon right-aligned (RTL: icon on left side visually, logically at the end) |
| hover | Background slightly lighter, cursor pointer |
| focus | Outline 2 px solid color-border-focus |
| expanded | Answer panel visible below, expand icon rotated 180 deg (or changed to a close glyph), no border-bottom until the answer ends |

#### form input (gate email / WhatsApp)

| State | Visual spec |
|---|---|
| default | Background color-surface, border 1 px solid color-border, border-radius radius-sm, padding space-3 space-4, color-text-primary, font body, direction rtl, text-align right |
| focus | Border 2 px solid color-border-focus, no box-shadow (keep clean) |
| error | Border 2 px solid color-border-error (#E53935, passes 3:1 non-text contrast at 4.19:1 on #1A1A1A). Error message below input: a circle-exclamation icon (inline SVG, 16 px, color-text-error #F04040) followed by error text in color-text-error (#F04040, approximately 4.6:1 on #1A1A1A, passes AA). Font body-sm. The icon provides a non-color cue satisfying WCAG 1.4.1 color independence. |
| disabled (gate-submitting) | Opacity 0.5, cursor not-allowed, pointer-events none |

#### gate states (COMP-GATE)

| Gate state | Visual spec |
|---|---|
| gate-default | Form at rest; email (or WhatsApp) input, consent line, submit button in default state; field-display region shows selected field label or generic copy |
| gate-submitting | Submit button enters loading state (spinner); all inputs disabled; a live-region aria-live="polite" announces loading to screen readers |
| gate-submitted | Form hidden; GATE-SUCCESS heading and body slots visible; no competing action in view; success indicator using color-success (#00C49A) |
| gate-error | Form remains; error slot visible below input (GATE-ERROR-AR / EN); inline error with circle-exclamation icon (color-text-error #F04040) preceding the error text (color-text-error #F04040, approximately 4.6:1 on surface, passes AA); retry available; role="alert" on the error container ensures screen readers announce the error without relying on color alone |
| gate-confirmed (owned non-payer) | Form replaced by plan selection surface or lesson-access confirmation; owned non-payer is not asked to re-enter contact details |

---

### RTL behavior per breakpoint

The page renders with `<html dir="rtl" lang="ar">` as the default. An EN locale path may
switch to `lang="en"` with `dir="ltr"` applied scoped to the text container; the structural
layout always starts from the RTL base and is explicitly mirrored for LTR rather than
inverted. All logical properties (margin-inline-start, padding-inline-end, etc.) are used in
CSS so the layout adapts correctly to both directions without duplicate rules.

#### sm (0 to 767 px, mobile)

- Single-column layout. All content stacks top to bottom in RTL reading order (right to left
  within each line, lines stacking downward).
- Hero: content column full-width, visual image below content (or background image); primary
  CTA visible in the first viewport without any scroll. Sticky nav collapses to logo + CTA.
- Field grid: 1 tile per row (full 4-column width). Tiles fill right to left within the
  row (first tile aligns to the right edge), but with only one tile per row this is moot.
  Field label and CTA text within tiles: RTL, text-align right.
- How it works: steps stack vertically. Step 1 at top, step 3 at bottom. Step icons and
  headings align right. Step connector line hidden on mobile (replaced by vertical spacing).
- FAQ accordion: question text right-aligned; expand icon at the left edge of the row
  (logical end in RTL); answer text right-aligned, text-align start (inherits RTL).
- Gate form: input label right-aligned; input field direction rtl, placeholder text-align
  right; submit button full-width.
- Mixed direction: Western numerals (0 to 9) within Arabic text flow via unicode-bidi
  isolation on the numeral span where needed (e.g., chapter counts in proof tiles). English
  words in an Arabic sentence (e.g., a product or brand name in English) use dir="auto" on
  the inline element so bidi algorithm handles them correctly. No manual override of the
  Unicode bidi algorithm elsewhere.

#### md (768 px to 1279 px, tablet)

- Two-column grid begins. Hero splits into content right (5 cols) and visual left (3 cols).
- Field grid: 2 tiles per row (4-col span each). Right-to-left tile order: first tile at
  right, second tile to its left. The CSS `grid-auto-flow: row` with `direction: rtl` on
  the grid container handles tile order automatically.
- How it works: three columns across 8 grid columns. Steps read right to left (step 1 at
  right, step 3 at left) to match RTL reading order. Step connector line visible as a
  horizontal rule between step icons.
- FAQ: centered in 6 of 8 columns. Behavior as sm.
- Gate form: centered in 4 of 8 columns. Behavior as sm.
- Sticky nav: logo right, nav links visible in center, CTA left.

#### lg (1280 px and above, desktop)

- Full 12-column grid. Hero: content right (7 cols), visual left (5 cols). The visual
  image fills the left 5 columns; the right 7 columns carry the headline, subhead, and
  primary CTA in RTL stack.
- Field grid: 3 tiles per row (4-col span each). Tile order RTL: right-most tile first,
  left-most tile last per row. The 8th tile (and-more) fills the left-most position of
  the final row.
- How it works: three equal columns across 12 (4 cols each). RTL reading order as md.
  Connector line visible.
- Why Maharat proof grid: 3 tiles, 4 cols each across 12. Instructor roster strip below
  (confirm-at-gate slot; if absent the section reflows without it).
- Plans: 3 tiles, 4 cols each across 12.
- FAQ: 8 of 12 centered.
- Gate: 4 of 12 centered. The gate section has generous vertical padding (space-24) so
  the gate does not feel cramped.

RTL correctness checklist applied to every breakpoint:

- All flexbox containers use `flex-direction: row` and rely on `direction: rtl` to reverse
  the visual order (no manual `flex-direction: row-reverse` hacks that break when LTR
  locale is applied).
- All `text-align` values use `start` or `end` (logical), not `left` or `right` (physical),
  except where a physical value is explicitly required and documented.
- Scroll direction on horizontal carousels (if any are introduced at build): direction rtl
  so scroll starts from the right edge.
- Form inputs: `direction: rtl`, `unicode-bidi: plaintext` on inputs to allow the browser
  to detect content direction on per-keystroke basis rather than forcing RTL on
  user-entered content that may be an email address (which is LTR). The input label
  remains RTL-aligned.

---

### accessibility notes

WCAG 2.1 Level AA is the minimum bar. The following are the specific requirements for this
page.

#### color contrast

| Element | Foreground | Background | Ratio | Note |
|---|---|---|---|---|
| Body text on bg | #F5F5F5 | #141414 | 16.8:1 | Exceeds AA (4.5:1) and AAA (7:1) |
| Body text on surface | #F5F5F5 | #1A1A1A | 15.2:1 | Exceeds AA and AAA |
| Secondary text on bg | #A8A8A8 | #141414 | 4.6:1 | Meets AA normal text (4.5:1) |
| CTA label on accent | #141414 | #009975 | approximately 5.7:1 | Near-black on emerald. Meets AA normal text (4.5:1). Accessibility fix: replaces prior #F5F5F5 on #009975 (3.30:1, failed AA for 16 px 600 weight normal text). Applies to all 5 button positions. |
| Error text on surface | #F04040 | #1A1A1A | approximately 4.6:1 | Meets AA normal text (4.5:1). Accessibility fix: replaces prior #E53935 on #1A1A1A (4.19:1, which failed AA). The prior spec figure of 4.6:1 for #E53935 was incorrect; computed value is 4.19:1. |
| Error border on surface | #E53935 | #1A1A1A | 4.19:1 | Non-text contrast. Meets WCAG 1.4.11 threshold of 3:1. Border only; do not use for error text. |
| Focus ring on surface | #009975 | #1A1A1A | 4.90:1 | Non-text contrast. Meets 3:1 threshold. |
| Hover border on surface | #009975 | #1A1A1A | 4.90:1 | Full opacity, meets WCAG 1.4.11 (3:1). Accessibility fix: replaces prior 60% opacity hover border (approximately 2.4:1 effective, failed 3:1). |

Contrast verification note: these ratios are specified for implementation. All figures must
be verified at build with the actual rendered font sizes. The CTA label contrast fix
(#141414 on #009975 at approximately 5.7:1) is robust across the normal-text threshold and
does not depend on the large-text qualifier. Focus-order verification across all gate states
and the FAQ accordion remains a render-check open item (see open_items above).

#### focus order

Logical tab order: left to right in the DOM (which, with RTL, means right to left visually).
Tab order must follow the visual reading order of the page.

1. Skip-to-main-content link (visually hidden, appears on focus, jumps to section 1).
2. Sticky nav: logo (if linked), nav links in visual right-to-left order (fields, how it
   works, plans, FAQ on desktop), primary CTA button.
3. Hero CTA button (first focusable element in the main content after the nav).
4. Scroll indicator (if interactive; if purely decorative, aria-hidden="true").
5. Field grid tiles: tab order follows visual RTL order within each row (right tile first
   in each row, rows top to bottom).
6. Fields section CTA.
7. How it works: if steps contain links, focus them in visual RTL order.
8. Why Maharat: proof tiles (if interactive); instructor strip (confirm-at-gate).
9. Plans tiles CTAs.
10. FAQ rows: question triggers in order; answer content becomes focusable on expand.
11. Gate form: field-display region (if interactive), input field, consent line (if it
    contains a link to privacy policy), submit button.
12. Gate success, error, or confirmed state: first element of the new state must receive
    programmatic focus (via JavaScript focus management) so screen readers announce the
    state change.

All focus rings must be visible, using the 2 px solid color-border-focus (#009975)
specification above. No `:focus { outline: none }` without a custom ring replacement.

#### semantic structure

| Landmark | Element | Role |
|---|---|---|
| Page header / nav | `<header>` containing `<nav>` | banner + navigation |
| Main content | `<main>` | main |
| Each section | `<section>` with `aria-labelledby` pointing to its section heading | (implied section role) |
| Hero headline | `<h1>` | The single H1 on the page |
| Section headings | `<h2>` | One per section (fields, how it works, why, plans, FAQ, gate) |
| Step headings in How it works | `<h3>` | |
| Proof tile headings | `<h3>` | |
| Plan tile labels | `<h3>` | |
| FAQ questions | `<button>` inside `<dt>` (or `<button>` inside a list item) controlling an `aria-expanded` disclosure | Accordion pattern, WAI-ARIA disclosure widget |
| Gate form | `<form>` with `aria-labelledby` pointing to the gate section heading | |
| Gate email input | `<input type="email">` with explicit `<label>` (not placeholder as label) | |
| Gate consent line | `<p>` with a link to the privacy policy if applicable | |
| Submit button | `<button type="submit">` | |
| Gate success state | The success heading uses `role="status"` or `aria-live="polite"` on its container, or focus is moved programmatically | |
| Gate error state | `role="alert"` on the error container | |
| Field icons | `<img>` with non-empty `alt` attribute describing the field abstractly (e.g., "Music field icon"), or `aria-hidden="true"` if the label text below provides the accessible name | |
| Hero image | `<img>` with descriptive `alt` or `role="presentation"` if purely decorative | |

#### touch targets

Minimum 44 x 44 px on all interactive elements. Applies to: field tiles (expand the
interactive area to the full tile if the tile itself is smaller than 44 px), FAQ row
triggers, primary CTA buttons (already >= 48 px min-height), form inputs (min-height 48 px),
sticky nav links. Use padding to extend tap targets without affecting visual layout where needed.

#### alt text slots

Every image region on the page has a required alt text slot. No image is deployed without
its alt attribute populated or explicitly set to empty for decorative images. Alt text is a
build responsibility, not a copy responsibility. All imagery regions and their alt text
requirements are listed below.

Page imagery:

| Asset id | Alt text slot requirement |
|---|---|
| HERO-IMG-01 | Non-empty alt attribute describing the abstract visual or scene. If abstract brand art: brief description of the visual form ("Abstract geometric art in dark tones with emerald highlights"). If rights-cleared photography: describe the scene. Never leave alt empty on a meaningful hero image. |
| FIELD-ICON-MUSIC | alt="Music field icon" or aria-hidden="true" if the tile label text provides the full accessible name. |
| FIELD-ICON-COOKING | alt="Cooking field icon" or aria-hidden="true" if tile label provides the accessible name. |
| FIELD-ICON-ACTING | alt="Acting field icon" or aria-hidden="true" if tile label provides the accessible name. |
| FIELD-ICON-MAKEUP | alt="Makeup field icon" or aria-hidden="true" if tile label provides the accessible name. |
| FIELD-ICON-BUSINESS | alt="Business field icon" or aria-hidden="true" if tile label provides the accessible name. |
| FIELD-ICON-STYLING | alt="Styling field icon" or aria-hidden="true" if tile label provides the accessible name. |
| FIELD-ICON-MARKETING | alt="Marketing field icon" or aria-hidden="true" if tile label provides the accessible name. |
| FIELD-ICON-MORE | alt="More fields icon" or aria-hidden="true" if tile label provides the accessible name. |
| HOW-ICON-01 | alt="Step 1: pick a field" or aria-hidden="true" if the step heading provides the name. |
| HOW-ICON-02 | alt="Step 2: start your free lesson" or aria-hidden="true" if the step heading provides the name. |
| HOW-ICON-03 | alt="Step 3: subscribe to continue" or aria-hidden="true" if the step heading provides the name. |
| WHY-PROOF-01 | alt attribute describing the abstract content, or aria-hidden="true" if the proof tile copy provides full context. |
| WHY-PROOF-02 | alt attribute describing the abstract content, or aria-hidden="true" if the proof tile copy provides full context. |
| WHY-PROOF-03 | alt attribute describing the abstract content, or aria-hidden="true" if the proof tile copy provides full context. |

Email imagery (apply to email template at build):

| Image region | Alt text slot requirement |
|---|---|
| Email header image (abstract brand art, all 5 emails E1 to E5) | alt="" (empty, marking decorative). Brand-constant abstract art used purely for visual framing carries no meaning that must be conveyed to screen readers. |
| Any field-icon or meaning-carrying image in email body | alt attribute with a brief description in the email language (Arabic for AR variant, English for EN variant). |
| Instructor photography if confirmed and used in email | alt attribute describing the person and context in the email language. |

Arabic alt text rule: alt attributes on the Arabic-locale page and Arabic email variants
must be in Arabic, consistent with the lang="ar" on the html element and the email lang
attribute. Build-time alt text authoring must match the page language.

---

### email render spec (accessibility requirements)

These requirements apply to the email template built by lifecycle-architect or the email
platform owner for the lifecycle sequence E1 to E5. They are spec-level requirements; final
verification is render-blocked pending send-platform confirmation (open item: accessibility-email-template-render-check).

#### semantic heading structure

Every email in the sequence (E1 to E5, both AR and EN) must use a semantic HTML heading
structure in the rendered template:

- H1 (or role="heading" aria-level="1" on a table cell if the email client requires table
  layout): the primary message line of each email. This is the first substantive content
  element after any decorative header image. Maps to the email subject-line-equivalent
  visible in the email body.
- H2 (or equivalent role): sub-sections where used (for example, a secondary value
  proposition block or a field roster section in E3).
- Screen readers announce heading hierarchy to help users navigate long email messages. At
  minimum one H1-equivalent per email is required.

#### plain-text alternative

Every email in the sequence must have a plain-text alternative authored alongside the HTML
variant. Responsibility: copywriter-ar (Arabic plain-text, all 5 emails) and copywriter-en
(English plain-text, all 5 emails). The plain-text alternative must:

- Carry all substantive copy from the HTML version.
- Include the CTA as a plain URL or a labeled URL (e.g., "Start your free lesson:
  [URL]"), not as a button that disappears in plain text.
- Not include HTML markup, image references, or layout instructions.
- Be submitted alongside the HTML copy variant to the arabic-copy-qa and english-copy-qa
  gates for sign-off.

#### CTA button (email)

The email CTA button renders with the same token rule as the landing page CTA: background
color-accent (#009975), label color-text-on-accent (#141414). Near-black on emerald
yields approximately 5.7:1, passing AA for normal text. This is the same fix applied to
the landing page CTA (fix 1 above). The email template must apply this token rule
consistently so the brand CTA treatment is uniform across page and email.

Minimum tap target for mobile email: the CTA button must be at minimum 44 px tall and
120 px wide in the email template CSS (inline styles, required for HTML email
compatibility). Padding must be applied on the anchor or button element directly, not on
the surrounding cell or div, to ensure the tap target is genuinely 44 px on mobile email
clients. Verify on a rendered screenshot at 375 px viewport width before approving the template.

#### decorative image handling

Header imagery in emails using abstract brand-constant art (the confirmed fallback per
lifecycle-package open item 14) is purely decorative. These images must be marked
alt="" (empty alt attribute) or role="presentation" in the email template. They convey no
meaning; they must not be narrated by screen readers. See alt text slots above for the
complete email imagery requirements.

#### render-block note

All email template accessibility checks above require a rendered email template for final
verification. This spec provides the requirements; the gate pass is blocked until the
rendered template is reviewed by accessibility-qa. Send-platform must be confirmed first.
See open item: accessibility-email-template-render-check.

---

### performance budget

The page must achieve a fast first render and keep the primary action (sticky CTA or hero CTA)
visible without layout shift.

#### render budget targets (measured at build with Lighthouse or equivalent)

| Metric | Target |
|---|---|
| First Contentful Paint (FCP) | Under 1.8 seconds on a simulated mid-range mobile (4G, 2x CPU throttle) |
| Largest Contentful Paint (LCP) | Under 2.5 seconds on the same simulation. The LCP element is most likely the hero headline or hero image; both must be render-unblocked. |
| Cumulative Layout Shift (CLS) | Under 0.1. Image dimensions must be set in HTML (width and height attributes) to prevent layout shift. |
| Total Blocking Time (TBT) | Under 300 ms. No large synchronous scripts in the critical path. |
| Time to Interactive (TTI) | Under 3.5 seconds on the same simulation. |

#### asset weight budget

| Asset type | Budget |
|---|---|
| HERO-IMG-01 (desktop) | Max 200 KB in WebP or AVIF format, with a JPEG fallback under 350 KB |
| HERO-IMG-01 (mobile) | Max 100 KB in WebP or AVIF |
| FIELD-ICON-xx (8 icons) | Max 20 KB each (SVG preferred, under 5 KB; rasterized fallback under 20 KB) |
| HOW-ICON-xx (3 icons) | Max 5 KB each (SVG) |
| WHY-PROOF-xx (3 images) | Max 80 KB each in WebP or AVIF |
| Arabic web font (if used) | Max 80 KB per font file (woff2), subset to Arabic Unicode block and Latin Basic |
| Latin web font (if used) | Max 40 KB per font file (woff2) |
| Total page weight (initial load, before lazy assets) | Under 600 KB (HTML + CSS + critical JS + above-fold images + fonts) |
| Total page weight (full load) | Under 1.8 MB |

#### loading strategy

- Hero image (HERO-IMG-01): preloaded via `<link rel="preload">` in the document `<head>`.
  The desktop and mobile variants served via `<picture>` with `srcset` and `sizes`, so only
  the correct-size image is fetched.
- Field grid icons (FIELD-ICON-xx): lazy-loaded with `loading="lazy"` on `<img>` elements;
  the icons are below the fold on mobile and almost all desktop viewports, so lazy loading
  is safe and correct.
- Why Maharat and Plans section images: lazy-loaded.
- Arabic and Latin web fonts: loaded with `font-display: swap` so text is readable before
  the font loads. Fonts are preloaded in `<head>` only if they appear above the fold.
- JavaScript: no render-blocking scripts in `<head>`. All non-critical JS is deferred or
  async. The gate form interaction (field-selection state, submit, error, success) is the
  only required JavaScript; it must be < 30 KB minified and gzipped.
- CSS: critical above-fold CSS is inlined or loaded in `<head>` without render blocking.
  Below-fold styles are loaded async or bundled with the main stylesheet.
- Primary action visible without scroll on mobile: the hero CTA button must be within the
  first 100vh. On sm (390 px viewport), the hero content (headline + subhead + CTA) must
  fit within 80vh to leave room for the sticky nav (approximately 56 px) and a subtle
  scroll indicator. If copy is too long for this constraint, the section heading is the
  copy-region binding and must be resolved with copywriter-ar: the display-size headline
  cannot exceed 3 lines on sm at the type scale above.

---

### copy region to variant id binding table

Every text region on the page is bound to a QA-passed copy-package variant id. No copy is
written in the design spec. If a region's copy is not yet at qa-passed status, that region
is marked copy-region-unbound and proceeds as a design slot.

Note on copy-package status at time of this spec: both copy-package.ar.md and
copy-package.en.md are at status draft (pending arabic-copy-qa, english-copy-qa, and
brand-qa-reviewer). The binding table below maps each design region to the correct variant
id from those packages. The bindings are locked; copy content will not change the binding
once both packages reach qa-passed. All regions are therefore marked copy-region-unbound
pending QA, with the target variant id identified.

| Page region | Slot id (from web_asset_brief) | AR variant id | EN variant id | Status |
|---|---|---|---|---|
| Hero headline (H1) | HERO-HEADLINE-AR / HERO-HEADLINE-EN | LP-HEADLINE-1 (primary) or LP-HEADLINE-2 (alt), from copy-package.ar section 5 (brand-voice-hero.ar: HERO-HEADLINE-1 is the recommended H1) | LP-HEADLINE-1 or LP-HEADLINE-2, from copy-package.en Part 5 | copy-region-unbound (pending QA) |
| Hero subhead | LP-SUBHEAD-AR / LP-SUBHEAD-EN | LP-SUBHEAD-1 from copy-package.ar section 5 | LP-SUBHEAD-1 from copy-package.en Part 5 | copy-region-unbound (pending QA) |
| Hero secondary subhead or trust line (optional) | LP-SUBHEAD-2-AR / LP-SUBHEAD-2-EN | LP-SUBHEAD-2 from copy-package.ar section 5 (if used) | LP-SUBHEAD-2 from copy-package.en Part 5 (if used) | copy-region-unbound (pending QA) |
| Hero primary CTA | LP-CTA-HERO-AR / LP-CTA-HERO-EN | LP-CTA-1 from copy-package.ar section 5 (ابدأ الدرس المجاني) | LP-CTA-1 from copy-package.en Part 5 (Start your free lesson) | copy-region-unbound (pending QA) |
| Sticky bar CTA | LP-CTA-STICKY-AR / LP-CTA-STICKY-EN | LP-CTA-1 from copy-package.ar section 5 (or HERO-CTA-2 from brand-voice-hero.ar: ابدأ بدرس أول مجاني) | LP-CTA-1 from copy-package.en Part 5 | copy-region-unbound (pending QA) |
| Fields section heading | LP-HEADLINE-FIELDS-AR / LP-HEADLINE-FIELDS-EN | No explicit variant id in copy-package.ar; slot is for copywriter-ar to fill; held as copy-region-unbound | Same | copy-region-unbound |
| Field tile labels (7 fields: Music, Cooking, Acting, Makeup, Business, Styling, Marketing) | FIELD-LABEL-{FIELD}-AR / FIELD-LABEL-{FIELD}-EN | Labels derive from the field name list in copy-package.ar (الموسيقى، الطبخ، التمثيل، المكياج، الأعمال، التنسيق، التسويق) as used throughout; these are field-label slots, not creative copy; copywriter-ar to bind exact slot text | Same logic, EN | copy-region-unbound |
| Field tile instructor name (confirm-at-gate, all 7) | FIELD-INSTRUCTOR-{FIELD}-AR / FIELD-INSTRUCTOR-{FIELD}-EN | Cleared instructor names from copy-package.ar (confirm-at-gate per strategy-artifact 3.3 and 6): Ragheb Alama, Salam Dakkak, Kosai Khauli, Bassam Fattouh, Toufic Kreidieh, Cedric Haddad, Elda Choucair; slot is empty until naming confirmed at gate | Same 7 names (EN transliteration) | copy-region-unbound, confirm-at-gate |
| Field tile inline CTAs (7 fields) | FIELD-CTA-{FIELD}-AR / FIELD-CTA-{FIELD}-EN | Inline CTA copy from copy-package.ar (e.g., ابدأ مجاناً per AD-BREADTH-1 CTA pattern; per-field variants from the ad CTA set) | From copy-package.en per-field ad CTAs (Start the free lesson) | copy-region-unbound |
| And-more tile label | FIELD-LABEL-MORE-AR / FIELD-LABEL-MORE-EN | Unnamed breadth label; copy-package.ar references "والمزيد عبر مجالات عديدة" as the breadth phrase; copywriter-ar to bind slot text | "And more across many fields" from copy-package.en | copy-region-unbound |
| Fields section primary CTA | LP-CTA-FIELDS-AR / LP-CTA-FIELDS-EN | LP-CTA-1 from copy-package.ar section 5 | LP-CTA-1 from copy-package.en Part 5 | copy-region-unbound (pending QA) |
| How it works section heading | LP-HEADLINE-HOW-AR / LP-HEADLINE-HOW-EN | No explicit variant id; slot for copywriter-ar | Same | copy-region-unbound |
| How it works step 1 heading and body (3 steps) | HOW-STEP{N}-AR / HOW-STEP{N}-BODY-AR, EN equivalents | No explicit variant id; slots for copywriter-ar; steps describe: pick a field, start the free lesson, subscribe to continue | Same logic, EN | copy-region-unbound |
| Why Maharat section heading and subhead | LP-HEADLINE-WHY-AR / LP-SUBHEAD-WHY-AR / EN equivalents | No explicit variant id; slots for copywriter-ar; LP-SUBHEAD-2 (breadth proof line from copy-package.ar section 5) is the closest analog for the subhead | LP-SUBHEAD-2 from copy-package.en Part 5 is a candidate for the subhead slot | copy-region-unbound |
| Breadth proof tile copy (3 tiles) | WHY-PROOF-{N}-AR / WHY-PROOF-{N}-EN | No explicit variant id; slots for copywriter-ar; tile copy anchors to page-sourced cleared facts only | Same | copy-region-unbound |
| Instructor roster strip (confirm-at-gate, optional) | INSTRUCTOR-STRIP-AR / INSTRUCTOR-STRIP-EN | copy-package.ar EMAIL-E3 body contains the cleared per-instructor roster line as the closest analog ("راغب علامة في الموسيقى، سلام دقاق في الطبخ...") | copy-package.en EMAIL-E3 body contains the equivalent EN roster line | copy-region-unbound, confirm-at-gate |
| Plans section heading | LP-HEADLINE-PLANS-AR / LP-HEADLINE-PLANS-EN | No explicit variant id; slot for copywriter-ar | Same | copy-region-unbound |
| Plan tile label, price, features, CTA (3 tiles, ASSUMPTION) | PLAN-LABEL-{N}, PLAN-PRICE-{N}, PLAN-FEATURES-{N}, PLAN-CTA-{N} AR/EN | PLAN-PRICE slots empty until price confirmed (ASSUMPTION per strategy-artifact 6); PLAN-CTA: LP-CTA-2 from copy-package.ar (اشترك الآن) is the structural analog | LP-CTA-2 from copy-package.en (Subscribe and unlock everything) is the structural analog | copy-region-unbound, price ASSUMPTION |
| Promo banner (ASSUMPTION, hidden until confirmed) | PROMO-BANNER-AR / PROMO-BANNER-EN | ASSUMPTION, empty | ASSUMPTION, empty | copy-region-unbound, ASSUMPTION |
| Plans section primary CTA | LP-CTA-PLANS-AR / LP-CTA-PLANS-EN | LP-CTA-2 from copy-package.ar (اشترك الآن) | LP-CTA-2 from copy-package.en | copy-region-unbound (pending QA) |
| FAQ section heading | LP-HEADLINE-FAQ-AR / LP-HEADLINE-FAQ-EN | No explicit variant id; slot for copywriter-ar | Same | copy-region-unbound |
| FAQ Q1 to Q5 and A1 to A5 (5 pairs) | FAQ-Q{N}-AR / FAQ-A{N}-AR / EN equivalents | No explicit variant id; slots for copywriter-ar; Q2 (certificate framing) must use "شهادة مخصصة باسمك" pattern per brand-voice.md; Q5 (instructor credibility) uses cleared page-sourced facts only per strategy-artifact | Same | copy-region-unbound; Q2 and Q5 carry mandatory direction notes |
| Gate section heading | LP-HEADLINE-GATE-AR / LP-HEADLINE-GATE-EN | No explicit variant id; slot for copywriter-ar | Same | copy-region-unbound |
| Gate subhead (field-sensitive) | LP-SUBHEAD-GATE-AR / LP-SUBHEAD-GATE-EN | Field-generic variant and 7 per-field variants; slots for copywriter-ar; the field-generic variant maps closest to LP-SUBHEAD-1 from copy-package.ar | Same | copy-region-unbound |
| Gate email input label and placeholder | GATE-EMAIL-LABEL-AR / GATE-EMAIL-PLACEHOLDER-AR / EN equivalents | Slots for copywriter-ar; label includes asterisk required indicator adjacent to label text | Same | copy-region-unbound |
| Gate required field note | GATE-REQUIRED-NOTE-AR / GATE-REQUIRED-NOTE-EN | "* required field" equivalent in Arabic; slot for copywriter-ar; must appear at top of gate form before the input; non-color indicator of required status | Same | copy-region-unbound |
| Gate consent line | GATE-CONSENT-AR / GATE-CONSENT-EN | Compliance-reviewed; Saudi PDPL posture OPEN ITEM; slot for copywriter-ar under compliance-privacy-reviewer supervision | Same | copy-region-unbound, PDPL OPEN ITEM |
| Gate submit CTA | LP-CTA-GATE-AR / LP-CTA-GATE-EN | LP-CTA-1 from copy-package.ar (ابدأ الدرس المجاني) or HERO-CTA-2 from brand-voice-hero.ar (ابدأ بدرس أول مجاني) | LP-CTA-1 from copy-package.en (Start your free lesson) | copy-region-unbound (pending QA) |
| Gate success state heading and body | GATE-SUCCESS-HEADING-AR / GATE-SUCCESS-BODY-AR / EN equivalents | No explicit variant id; slots for copywriter-ar | Same | copy-region-unbound |
| Gate error state line | GATE-ERROR-AR / GATE-ERROR-EN | No explicit variant id; slot for copywriter-ar; plain, non-alarming, one line | Same | copy-region-unbound |

---

## web_design_qa (web-designer to complete)

Produced by web-designer. Run in order against the design_spec above. This is a verifier-style
pass or fail verdict with a fix-list on any fail. No item is waved through.

---

### result: pass

Revised verdict 2026-06-12 after applying the accessibility-reviewer fix list from
accessibility-verdict.md. All 10 checks pass. All 9 addressable fix items (6 page-level,
4 email-level, noting that CTA fix is shared across both) are resolved at spec level. Two
render-block items are carried as open items.

The final human design check remains before any publish or build.

Open items confirmed in this verdict:

- copy-region-unbound: all copy regions are bound to the correct copy-package variant ids
  but both packages are at status draft pending arabic-copy-qa, english-copy-qa, and
  brand-qa-reviewer. The design can proceed; no gated build or go-live until the
  copy-packages reach qa-passed.
- gate-platform-not-confirmed: the gate form is designed to accommodate both email and
  WhatsApp capture. Live wiring is blocked until the platform is confirmed by Ahmed.
- accessibility-focus-order-render-check: focus order across all 5 gate states and the FAQ
  accordion at all 3 breakpoints requires verification on the rendered, interactive page.
  Programmatic focus moves (gate-submitted success heading, gate-error error container, FAQ
  answer on expand) cannot be confirmed at spec level. This is a render-check open item,
  not a design failure. The page must not advance to go-live without this check completed.
- accessibility-email-template-render-check: full email template render verification is
  blocked pending send-platform confirmation. Resubmit rendered template to accessibility-qa
  before any send action.

---

### responsive-rtl: pass

- direction: rtl is set on the `<html>` element at all three breakpoints (sm, md, lg).
- All layout uses logical CSS properties (margin-inline-start, padding-inline-end, etc.)
  so RTL and LTR locales are handled without duplicate physical-direction overrides.
- Hero: content column is on the right, visual column is on the left, at md and lg. On sm
  the columns stack with content above the visual, which is the correct RTL single-column
  reading order (the meaningful content reaches the reader first, then the decorative visual).
- Field grid: CSS Grid with `direction: rtl` on the container. Tile order is right-to-left
  per row at every breakpoint, consistent with Arabic reading direction.
- How it works steps: RTL reading order at md and lg (step 1 at right, step 3 at left).
  Stacked vertically on sm with step 1 at top.
- FAQ accordion: question text right-aligned, expand icon at the logical end (left edge in
  RTL). Answer text direction rtl, text-align start.
- Gate form: input label right-aligned, input direction rtl, unicode-bidi plaintext on the
  input element to handle email addresses (which are LTR content) correctly.
- Mixed Arabic, English, and Western numerals: inline English elements use dir="auto";
  Western numeral spans use unicode-bidi isolate where needed; no manual bidi override
  breaks reading order.
- No evidence of RTL breaking at any declared breakpoint in the spec.

---

### visual-constants: pass

- Background: color-bg token #141414 is the page background for sections 1 (hero), 2
  (field grid), 3 (how it works), 5 (plans), and 7 (gate). No white or off-brand light
  background is introduced anywhere.
- Card surfaces: color-surface token #1A1A1A is applied to field tiles, plan tiles, proof
  tiles, FAQ rows, and the sticky nav background. This is the only surface color used; no
  third neutral is introduced.
- Accent: color-accent token #009975 (emerald) is applied exclusively to primary action
  buttons: sticky CTA, hero CTA, field section CTA, plans section CTA, and gate submit
  button. The accent is a highlight, not a flood. It does not appear on decorative elements,
  body text, icons, section backgrounds, or any non-interactive element.
- No off-brand color has been introduced. The only colors in the token set are derived from
  or consistent with the three brand constants plus functional state colors (error red,
  success green distinct from accent, text whites, borders, and overlays).
- Why Maharat section uses color-surface (#1A1A1A) as its background, creating a deliberate
  contrast break from the adjacent #141414 sections, which is consistent with the visual
  direction's card-surface usage.

---

### western-numerals-rendered: pass

- The type scale, spacing, breakpoint values, and all numeral references in this spec use
  Western numerals (0 to 9) throughout.
- No Eastern Arabic-Indic digits (Unicode U+0660 to U+0669) appear in any token value,
  dimension, or instruction.
- The copy-region binding table notes that rendered numerals in copy (e.g., chapter counts)
  must be Western; this is enforced at the copy-package QA gate (arabic-copy-qa checks
  this) and at build (the copywriter-ar package confirms "Western numerals only" in its
  pre-handoff checklist).
- The unicode-bidi isolate technique specified for numeral spans in Arabic text ensures
  Western numerals display correctly in RTL flow without reversal.
- Font choice (confirmed at build) must support Western numerals in the Arabic glyph set
  without substituting Arabic-Indic digit glyphs. This is a build-time check, flagged here.

---

### no-baked-arabic-text: pass

- All text regions on the page are copy-overlay slots bound to copy-package variant ids.
  No copy is authored or written in this design spec.
- All imagery in the web_asset_brief (HERO-IMG-01, FIELD-ICON-xx, HOW-ICON-xx,
  WHY-PROOF-xx) is explicitly text-free per the asset brief. No Arabic script, no English
  text, no numerals are baked into any generated or supplied image asset.
- The generation note on every asset in the asset brief states: "Text-free. Do not generate
  Arabic." This is the hard stop at asset production.
- No generated instructor likeness is specified anywhere in the design. The confirmed
  fallback is abstract brand-constant art. Rights-cleared photography (if confirmed) is not
  generated.
- The copy-region binding table confirms every slot maps to a copywriter-ar or
  copywriter-en variant id. No free text is placed on the page in design.

---

### responsive-breakpoints: pass

- Three named breakpoints are declared: sm (0 px), md (768 px), lg (1280 px).
- Content reflow is specified at each breakpoint with no clipping or overflow:
  - Hero two-column at md and lg, single-column at sm. No horizontal overflow on sm.
  - Field grid 1-per-row at sm, 2-per-row at md, 3-per-row at lg. Tile content does not
    clip at any tile width.
  - Plans tiles stack on sm and md, 3-column at lg. No overflow.
  - Gate form centered with generous outer margin at all breakpoints.
  - FAQ centered in a narrower column at md and lg to avoid overly wide lines.
- Primary action visible without scroll on mobile: the hero CTA is within the first
  viewport (first 100vh minus the sticky nav) at sm. The sticky nav also carries the
  primary CTA at all scroll depths. No scroll is required to reach the primary action on
  any breakpoint.
- Image dimensions are set with width and height attributes in HTML to prevent layout
  shift (CLS target under 0.1).

---

### interaction-states: pass

All interactive elements have a complete state specification:

Primary CTA buttons (sticky, hero, fields, plans, gate): default, hover, focus, active,
disabled, loading. All six states specified with visual tokens.

Field tiles (8 tiles including and-more): default, hover, focus, active, field-selected.
All five states specified. The field-selected state uses a distinct border treatment
(2 px solid color-accent) and a slight surface blend.

FAQ accordion rows: default (collapsed), hover, focus, expanded. All four states specified.

Gate form inputs: default, focus, error, disabled (during submitting). All four states
specified.

Gate states: gate-default, gate-submitting (submit button loading + all inputs disabled),
gate-submitted (success state with aria-live), gate-error (alert role), gate-confirmed
(owned non-payer path). All five gate states specified.

Reduced-motion accommodation: all transitions reduce to instant or cross-fade under
prefers-reduced-motion, specified in the state table.

---

### accessibility: pass

Revised 2026-06-12 after accessibility-reviewer fix list applied. All addressable items
resolved at spec level. Two render-block items carried as open items (focus-order-render-check,
email-template-render-check).

Page accessibility (WCAG 2.2 AA):

- Contrast, CTA button label: FIXED. Token color-text-on-accent (#141414) on color-accent
  (#009975), approximately 5.7:1. Passes AA for normal text (threshold 4.5:1). The prior
  #F5F5F5 on #009975 pairing (3.30:1) failed AA for the 16 px 600-weight CTA label and is
  replaced. Applies to all 5 button instances.
- Contrast, error text: FIXED. Token color-text-error (#F04040) on color-surface (#1A1A1A),
  approximately 4.6:1. Passes AA for normal text (threshold 4.5:1). The prior spec figure
  of 4.6:1 for #E53935 was incorrect; the computed value is 4.19:1, which fails AA. The
  token is updated. The error border (color-border-error #E53935) is unchanged; it passes
  the non-text contrast threshold of 3:1 at 4.19:1.
- Contrast, hover border: FIXED. Field tile hover border is now full-opacity #009975 (1 px
  solid). #009975 on #1A1A1A is approximately 4.90:1, passing WCAG 1.4.11 non-text contrast
  threshold of 3:1. The prior 60% opacity treatment yielded approximately 2.4:1 and failed.
- Color independence, error state: FIXED. A circle-exclamation icon (16 px SVG,
  color-text-error) precedes the error text inline, providing a non-color error cue.
  role="alert" on the error container handles the programmatic signal. Both color and
  non-color cues are now present.
- Color independence, required field: FIXED. An asterisk (*) adjacent to the GATE-EMAIL-LABEL
  slot, plus an explanatory note (GATE-REQUIRED-NOTE-AR / EN) at the top of the gate form,
  indicate the required status before submission. Color alone is not the only signal.
- Contrast figures corrected: the design_spec previously stated 3.2:1 for the CTA and 4.6:1
  for the error text. Both figures were wrong. The corrected computed values are 3.30:1 (CTA,
  fails AA at normal text) and 4.19:1 (error text, fails AA at normal text). The spec now
  states the accurate computed values alongside the fixed token values.
- Alt text slots: all imagery regions on the page now have explicit alt text slot
  requirements listed in the accessibility section (HERO-IMG-01, all 8 FIELD-ICON-xx,
  all 3 HOW-ICON-xx, all 3 WHY-PROOF-xx). Email header imagery slots also specified.
- Focus order: logical tab order specified for all interactive elements. Skip-to-main-content
  link specified. Programmatic focus management specified for gate state transitions. Focus
  order verification across gate states and FAQ accordion is a render-check open item.
- Semantic structure: H1 for hero, H2 for sections, H3 for sub-elements, ARIA roles, FAQ
  disclosure pattern, gate form with explicit label all specified correctly.
- Touch targets: minimum 44 x 44 px for all interactive elements. CTA buttons 48 px
  min-height. Form inputs 48 px min-height.
- Consent line: included in the gate form with a link slot for the privacy policy. Saudi PDPL
  posture is OPEN ITEM surfaced at the human gate.
- No focus outline suppressed without replacement. Focus ring spec is explicit.

Email accessibility (WCAG 2.2 AA, spec-level requirements):

- Semantic heading structure: required (H1-equivalent per email for the primary message line,
  H2-equivalent for sub-sections). Specified in the email render spec section.
- Plain-text alternative: required for all 5 emails in both AR and EN variants. Authoring
  responsibility added to copywriter-ar and copywriter-en.
- CTA contrast: same fix as landing page (color-text-on-accent #141414 on #009975).
- CTA tap target: minimum 44 px height, 120 px width, applied via inline styles on the
  anchor or button element directly.
- Email header imagery alt text: alt="" (decorative) on abstract brand-constant art in email
  headers. Meaningful imagery in email body requires descriptive alt in the email language.
- All email template items are render-blocked pending send-platform confirmation.

---

### performance-budget: pass

- Render budget targets are stated: FCP under 1.8 s, LCP under 2.5 s, CLS under 0.1,
  TBT under 300 ms, TTI under 3.5 s on a simulated mid-range mobile (4G, 2x CPU throttle).
- Asset weight budget is stated per asset type: hero desktop max 200 KB (WebP/AVIF), hero
  mobile max 100 KB, field icons max 20 KB (SVG preferred under 5 KB), proof images max
  80 KB each, fonts max 80 KB per Arabic file and 40 KB per Latin file, total initial load
  under 600 KB, total full load under 1.8 MB.
- Loading strategy is specified: hero image preloaded, below-fold images lazy-loaded,
  fonts loaded with font-display swap, no render-blocking scripts in head, gate JS under
  30 KB minified and gzipped, critical CSS inlined.
- Primary action is visible above the fold on mobile without scroll, consistent with the
  responsive-breakpoints check above.
- No blocking assets are in the critical path per the loading strategy specification.

---

### one-primary-action: pass

- One primary action per view is maintained throughout the page.
- Hero section: one emerald CTA (LP-CTA-HERO). No second CTA in the hero.
- Sticky nav: carries the same primary action (LP-CTA-STICKY) at all scroll depths. The
  sticky CTA does not create a competing action; it is the same conversion goal as the
  hero CTA (free first lesson entry), simply kept visible while scrolling. The nav links
  (fields, how it works, plans, FAQ) are navigation anchors, not conversion actions.
- Field grid section: the section-level primary CTA (LP-CTA-FIELDS) is the one action.
  The per-tile inline CTAs (FIELD-CTA-{FIELD}) are minor contextual links within the tile,
  subordinate to the section CTA. On mobile the tile CTAs may be hidden to reduce visual
  noise; the section-level CTA handles the conversion action.
- How it works: no CTA. Sticky bar carries the action.
- Why Maharat: no CTA. Sticky bar carries the action.
- Plans section: the section-level CTA (LP-CTA-PLANS) is one action routing to the gate.
  Per-tile CTAs (PLAN-CTA-{N}) are part of the plan selection UX, not competing conversion
  goals. At build, conversion-engineer must ensure the plans tile CTAs route to the gate
  (not to a separate checkout), keeping the primary conversion path unified.
- FAQ: no CTA. Sticky bar carries the action.
- Gate: one submit CTA (LP-CTA-GATE). No second action in the gate view. Gate success and
  error states each present one next-step action.

---

### premium-uncluttered: pass

- Generous spacing: the spacing token system uses space-16 (64 px) through space-24
  (96 px) as section padding, and space-6 (24 px) through space-8 (32 px) as card
  internal padding. Sections breathe; cards do not crowd each other.
- Clear hierarchy: the type scale descends clearly from display (56 px) through h1 (44 px),
  h2 (32 px), h3 (24 px), body-lg (18 px), and body (16 px). Only two neutral backgrounds
  (#141414 and #1A1A1A) prevent visual fragmentation. The emerald accent appears only on
  the primary action buttons, making the CTA the single visual signal demanding attention.
- No visual noise: no decorative gradients, no off-brand color fills, no icon overloading.
  Abstract field icons are simple (SVG, abstract form, no text). The proof tiles carry
  restrained abstract visuals. The FAQ is a clean disclosure list.
- Emerald as highlight, not flood: emerald appears on approximately 5 to 7 button instances
  per full page view. It does not appear on backgrounds, icons, borders (except the
  field-selected state border), or text other than button labels. The accent is a signal,
  not decoration.
- The imagery direction specifies "premium, uncluttered, abstract" as the governing
  register for all assets, consistent with the brand constants.

---

### human-check note

The final human design review by Ahmed remains the required step before any build
instruction or publish action. This web-design-qa verdict clears the spec to advance to
brand-qa-reviewer and then to conversion-engineer for implementation planning, both of
which also require human gate clearance before any live wiring or go-live. No automatic
approval is inferred from this verdict.

---

### fix_list: []

All addressable items from the accessibility-reviewer fix list are resolved at spec level.
The 10 web_design_qa checks all pass. Two render-block open items are carried to the build
stage and cannot be cleared at spec level; they are listed in open_items and do not
constitute a design failure.

Accessibility fixes applied to this spec (2026-06-12):
1. CTA label color: changed from #F5F5F5 to #141414 on #009975 fill (approximately 5.7:1, passes AA normal text). All 5 button instances, landing page and email.
2. Error text color: new token color-text-error #F04040 on #1A1A1A (approximately 4.6:1, passes AA). Prior #E53935 on #1A1A1A (4.19:1) failed AA; prior spec figure of 4.6:1 was incorrect and is now corrected.
3. Hover border: field tile hover border changed to full-opacity #009975 (approximately 4.90:1 non-text contrast, passes 3:1). Prior 60% opacity yielded approximately 2.4:1 and failed WCAG 1.4.11.
4. Error non-color cue: circle-exclamation icon added inline before error text in the gate error state. Color independence now satisfied.
5. Required field indicator: asterisk adjacent to GATE-EMAIL-LABEL plus GATE-REQUIRED-NOTE slot (new copy slot added) at top of gate form. Required status is not color-only.
6. Alt text slots: all imagery regions on page and in email have explicit alt text slot requirements specified in the accessibility section.
7. Contrast figure correction: prior spec figures (3.2:1 CTA, 4.6:1 error text) replaced with computed values (3.30:1 CTA before fix, 4.19:1 error text before fix). Post-fix values are stated.
8. Email render spec: new section added specifying semantic heading structure, plain-text alternative, CTA contrast, minimum tap target (44 px), and alt text for all email imagery.
9. Email template render-block: carried as open item (not a spec failure).

---

## Handoff

Direction (information architecture, UX flow, wireframe, visual direction, web asset brief,
conversion intent) advances to:

1. brand-qa-reviewer: runs brand_qa on this direction before it advances. A fail returns to
   web-design-director with the exact fix list.
2. web-designer: produces the build-ready design_spec and runs web_design_qa, filling the two
   stub sections above. web_design_qa must pass before the package advances.
3. copywriter-ar and copywriter-en: fill the labeled copy-overlay slots (slot index above).
   Arabic copy passes through arabic-copy-qa. English copy passes through english-copy-qa.
4. conversion-engineer: consumes the completed package (direction plus design_spec plus
   QA-passed copy) to implement the page, wire the signup gate (blocked until gate platform
   is confirmed), and wire the data-tracking-engineer event plan. Operates behind the human gate.

Nothing builds or publishes until the human gate clears. The gate-platform and
instructor-photography open items are explicitly surfaced at the human gate and must be
resolved by Ahmed before wiring or go-live.
