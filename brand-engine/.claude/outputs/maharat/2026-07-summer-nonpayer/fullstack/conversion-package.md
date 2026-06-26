# Conversion Package: Summer of Skills, full-stack non-payer campaign

## Common Envelope

- campaign_id: 2026-07-summer-nonpayer
- produced_by: conversion-engineer
- stream: 6 conversion path
- status: gated-pending
- qa:
  - skill_eval: pass (structure and completeness; all body fields present; copy regions
    bound to variant ids not invented here; event_plan carried from data-tracking-engineer
    not authored here; open items surfaced; no go-live action)
  - arabic_qa: na (no Arabic copy authored in this stream; all Arabic copy regions are
    bound to QA-passed copy-package variant ids from copywriter-ar; the GATE-CONSENT copy
    slot is authored by copywriter-ar under compliance-privacy-reviewer supervision)
  - english_qa: na (same as arabic_qa; all EN copy regions bound to copywriter-en variant ids)
  - web_design_qa: ref-pass (web-design-package web_design_qa verdict 2026-06-12: all 10
    checks pass, fix_list empty; the design_spec realized here is the passing spec; the
    two carried open items from that verdict, copy-region-unbound and
    gate-platform-not-confirmed, are surfaced in open_items below)
  - accessibility: pending (WCAG 2.1 AA compliance is specified in the design_spec and
    the accessibility notes in the web-design-package; rendered-page accessibility check
    runs at build before go-live; not yet runnable at spec stage)
  - brand_qa: pending (brand-qa-reviewer to run on this package before it advances to the
    human gate; no accreditation language, empowering framing, brand constants applied,
    no em dashes, Western numerals, RTL-correct throughout this spec)
  - compliance: pending (compliance-privacy-reviewer to run on the gate form, the consent
    copy slot, data routing, UTM stripping requirement, and the event_plan carried below;
    Saudi PDPL data-residency is an open item blocking the CAPI server-side wiring and any
    live data collection)
- open_items:
  - gate-platform-not-confirmed: the email and WhatsApp capture platform vendor is not
    confirmed (brief section 7, strategy-artifact section 6, tracking-plan open_items).
    The page and gate are designed for both paths. Live send wiring, platform SDK calls,
    and the submission routing are blocked until Ahmed names and approves the platform.
    This is a hard go-live blocker.
  - mobile-mapping-to-confirm: Apple IAP and Google Play event mapping for all seven events
    in the event_plan is flagged to-confirm by data-tracking-engineer (tracking-plan
    section 6). Not resolved here. Web events are ready; mobile events require a separate
    confirmation track once the mobile mapping is resolved.
  - Saudi-PDPL-data-residency: compliance and residency posture for gate-side data
    collection, any hashed match-key upload, and CAPI server-side signals must be confirmed
    by compliance-privacy-reviewer before go-live. Blocks the confirm and
    subscription_start CAPI calls in particular. Carried from tracking-plan and
    strategy-artifact.
  - suppression-source: the source for owned-send suppression (paying contacts,
    unsubscribed, hard-bounced) is OPEN ITEM. Must be confirmed and wired before any
    lifecycle handoff from the gate fires sends. Carried from strategy-artifact section 6
    and brief.
  - copy-regions-bind-on-qa-pass: all copy regions on the page and gate are bound to
    copywriter-ar and copywriter-en variant ids from copy-package.ar.md and
    copy-package.en.md. Both packages are at status draft pending arabic-copy-qa,
    english-copy-qa, and brand-qa-reviewer. The design and gate spec proceed; no build
    and no go-live until both copy packages reach qa-passed and the bound slots are
    populated with their QA-passed copy.
  - instructor-photography-not-confirmed: rights-cleared photography for any of the 7
    nameable instructors is OPEN ITEM. Abstract brand-constant art is the confirmed
    fallback for all field tile visuals and the hero image until cleared photography is
    supplied. No generated instructor likeness at any point.
  - price-plan-promo-not-confirmed: price, plan length, and promotion are ASSUMPTION
    (strategy-artifact section 6). The plans section placeholder is structured for the
    answer; no price, plan name, or promo copy is present on this page. Slots fill only
    when Ahmed confirms. The page converts without price or promo; the transformation
    carries the message.
  - per-instructor-naming-confirm-at-gate: all 7 nameable instructors (Ragheb Alama,
    Salam Dakkak, Kosai Khauli, Bassam Fattouh, Toufic Kreidieh, Cedric Haddad, Elda
    Choucair) are drafted as confirm-at-gate per the strategy-artifact. Instructor name
    display slots in field tiles and the instructor roster strip are empty until naming
    is confirmed for each. The page renders without them if empty.
  - verify-before-public-use-facts: Toufic Kreidieh's Brands For Less name and the
    $10,000-garage detail must not appear until verified. Elda Choucair's Omnicom, Forbes,
    Cannes, and the 900-plus and 1000-plus figures must not appear until verified. These
    are excluded from all copy slot definitions and from the page spec.
  - interest-field-select-surface-dependency: the interest_field_select event in the
    event_plan fires only if the field-selector surface on the page is built. The
    COMP-FIELD-GRID component in this spec implements that surface. If the build omits
    it, the event does not fire and Q6 in the warehouse queries returns no rows.
    Confirmed to data-tracking-engineer as the surface is included in the spec.
  - URL-subscriber-ID-stripping: if the email or app-push platform appends
    subscriber-identifying parameters to inbound links, those parameters must be stripped
    before any GA4 event fires. Hard stop; confirmed requirement per tracking-plan section 4.
    Compliance-privacy-reviewer must clear this before go-live.
  - CTA-price-confirmation-at-plans-tile: the per-tile CTAs in the plans section route to
    the gate, not to a separate checkout, to keep the primary conversion path unified
    (per web_design_qa one-primary-action check). This must be confirmed with engineering
    at build.
- brief_refs:
  - offer: product (Maharat B2C subscription, masterclass roster as hook); offer framing
    value-led, breadth-led, free-first-lesson as the low-friction entry (strategy-artifact
    section 4.2)
  - gate_type: email or WhatsApp capture for new acquisition (brief section 7);
    gate_platform OPEN ITEM (brief section 7, strategy-artifact section 6)
  - price: ASSUMPTION, not stated anywhere in this page spec (brief section 5,
    strategy-artifact section 6)
  - promotion: ASSUMPTION, posture value-led; no promo assumed, invented, or implied
    (brief section 5, strategy-artifact section 6)
  - plan: ASSUMPTION (brief section 5, strategy-artifact section 6)
  - instructor_roster: 7 nameable confirm-at-gate (Ragheb Alama, Salam Dakkak, Kosai
    Khauli, Bassam Fattouh, Toufic Kreidieh, Cedric Haddad, Elda Choucair); 4 never
    named (brief section 6, strategy-artifact section 3.3)
  - campaign_id: 2026-07-summer-nonpayer
  - creative_direction: #141414, #1A1A1A, #009975, RTL-correct, premium uncluttered,
    text-free generated imagery, no instructor likeness (brief sections 9 and 10)

---

## Body

### 1. Conversion the page optimizes toward

The single primary conversion is signup-gate completion, which for new acquisition is email
(or WhatsApp, once platform confirmed) capture unlocking a free first lesson, and for owned
non-payers is routing to plan selection and subscription start.

The funnel path:

```
click (paid per-field interest ad, or organic, or email, or push)
  -> Summer of Skills landing page (hero in viewport, one primary CTA visible)
  -> Pick-your-field interaction (field tile selected, UI state updated)
  -> Scroll or CTA tap -> Signup gate in viewport (gate_view fires)
  -> Gate form: email or WhatsApp input + consent line + submit
     (submit fires, confirm fires on server success)
  -> Owned non-payer path: gate bypasses re-capture, routes to plan selection
  -> New acquisition confirmed: free lesson access unlocked, lifecycle entry triggered
  -> Lifecycle sequence (stream 7) -> subscription_start
```

Gate completions are the primary micro-conversion for new acquisition. Subscription starts
are the primary macro-conversion for the campaign. Both are measured by the event_plan
carried in section 4. The field-selection interaction (interest_field_select) is a
qualifying micro-event that personalizes the gate and feeds the interest-cut segmentation
from strategy-artifact section 3.3. The free chapter 1 play (masterclass_play_start) is the
top-of-funnel engagement signal and secondary success metric.

---

### 2. Page spec

The landing page realizes the web-design-package design_spec (web_design_qa: pass,
2026-06-12). The spec below is the implementation reference for the build. Every text region
is a copy slot bound to a copywriter variant id. No copy is authored here.

#### 2.1 Identity and URL structure

- Page title (AR): bound to slot HERO-HEADLINE-AR (variant id LP-HEADLINE-1 from
  copy-package.ar section 5, or LP-HEADLINE-2 as alt; copywriter-ar recommends
  LP-HEADLINE-1 as the H1)
- Page title (EN): bound to slot HERO-HEADLINE-EN (variant id LP-HEADLINE-1 from
  copy-package.en Part 5, or LP-HEADLINE-2 as alt)
- Canonical URL pattern: maharat.com/ar/summer-of-skills or a confirmed campaign landing
  path (confirm exact slug with engineering at build; slug is subject to SEO-package
  recommendation from seo-specialist)
- Default render: Arabic (RTL). lang="ar" dir="rtl" on the html element.
- EN locale path: switches to lang="en" with LTR applied scoped to text containers;
  structural layout starts from the RTL base and is explicitly mirrored for LTR using
  logical CSS properties (margin-inline-start, padding-inline-end, etc.).
- Hreflang: ar and en declared.
- No personal or sensitive data in any URL parameter. UTM parameters carry campaign,
  source, medium, and content identifiers only (utm_campaign: 2026-07-summer-nonpayer),
  never user-level identifiers, email addresses, phone numbers, or subscriber IDs.
- If the email or app-push platform appends subscriber-identifying parameters to inbound
  links, those parameters must be stripped before the GA4 event fires. Hard stop per
  tracking-plan section 4 and open_items above.

#### 2.2 Visual constants (applied page-wide, from web-design-package design tokens)

- Background: color-bg token #141414 (sections 1, 2, 3, 5, 7)
- Card surfaces: color-surface token #1A1A1A (field tiles, plan tiles, proof tiles, FAQ
  rows, sticky nav background, Why Maharat section background)
- Primary accent: color-accent token #009975 (emerald), applied exclusively to primary
  action buttons: sticky CTA, hero CTA, field section CTA, plans section CTA, gate submit
  button. Not applied to decorative elements, body text, or icons (except the
  field-selected state border treatment).
- Type: Arabic primary (system Arabic stack baseline, with a premium Arabic web font slot
  to confirm at build; must have full Arabic glyph coverage, no tatweel, correct RTL
  kerning). Latin secondary (system sans-serif stack baseline, with a premium Latin web
  font slot). Typeface decisions go through the approval process before implementation.
- All type direction: dir="rtl" on the html element and all text containers. Logical CSS
  properties throughout. unicode-bidi: embed on mixed-direction inline elements.
- Western numerals only throughout. No Eastern Arabic-Indic digits. unicode-bidi isolate
  on numeral spans in Arabic text where needed.
- Generous spacing. Premium, uncluttered. Accent is a highlight, not a flood.
- No em dashes anywhere. Commas, colons, or periods instead.

#### 2.3 Page structure (7 sections, RTL reading order)

The page is a single scrolling surface. A sticky nav/CTA bar carries the one primary action
at all scroll depths. The structure below realizes the information_architecture and wireframe
from the web-design-package exactly.

---

##### Sticky nav / CTA bar (COMP-STICKY-NAV, persistent)

Layout: full width, top of viewport, z-index 100.
- Right: Maharat logo asset (text-free, linked to homepage)
- Center: nav links desktop only (fields, how it works, plans, FAQ): anchor links to their
  respective sections on the page
- Left: emerald primary CTA button (slot LP-CTA-STICKY-AR / LP-CTA-STICKY-EN, from
  copy-package.ar / copy-package.en)

On mobile: collapses to logo (right) + primary CTA button (left). Nav links hidden.
On scroll: elevation-sticky token (box-shadow: 0 2px 12px rgba(0,0,0,0.6)) applied once
the page scrolls past the hero.

No second CTA or competing action in the sticky bar.

---

##### Section 1: Hero (COMP-HERO)

Region: full-width, full viewport height on desktop, min 80vh on mobile. Background
#141414 with hero image overlay (color-overlay-dark: rgba(20,20,20,0.72)).

Layout (RTL):
- Right column (content): 7 of 12 cols on lg, 5 of 8 on md, 4 of 4 on sm.
  Reading order right to left, top to bottom:
  - COPY SLOT: HERO-HEADLINE-AR / HERO-HEADLINE-EN
    Bound to: LP-HEADLINE-1 (or LP-HEADLINE-2 alt) from copy-package.ar section 5 /
    copy-package.en Part 5. Status: copy-region-unbound pending QA.
    Typography: display (3.5 rem, 700, 1.15) on lg; h1 (2.75 rem, 700, 1.2) on md; h2
    (2 rem, 600, 1.25) on sm. The H1 element. Rendered as a single H1 on the page.
    Performance constraint: must fit within 3 lines on sm at 390px viewport to maintain
    the hero CTA within the first viewport. Flag to copywriter-ar if the LP-HEADLINE-1
    variant exceeds this at the confirmed type scale.
  - COPY SLOT: LP-SUBHEAD-AR / LP-SUBHEAD-EN
    Bound to: LP-SUBHEAD-1 from copy-package.ar section 5 / copy-package.en Part 5.
    Status: copy-region-unbound pending QA.
    Typography: body-lg (1.125 rem, 400, 1.6).
  - COPY SLOT: LP-SUBHEAD-2-AR / LP-SUBHEAD-2-EN (optional, only if copywriter provides)
    Bound to: LP-SUBHEAD-2 from copy-package.ar section 5 / copy-package.en Part 5
    (if used). Status: copy-region-unbound pending QA. May be omitted; layout reflows.
  - PRIMARY ACTION BUTTON (COMP-CTA-PRIMARY, emerald #009975, radius-pill)
    COPY SLOT: LP-CTA-HERO-AR / LP-CTA-HERO-EN
    Bound to: LP-CTA-1 from copy-package.ar section 5 / copy-package.en Part 5.
    Status: copy-region-unbound pending QA.
    Min-height 48px, min-width 160px, padding space-4 space-8 (16px 32px), font-weight 600.
    Taps to the Pick-Your-Field section (smooth-scroll or anchor link to section 2).
    State set: default, hover (#007f62), focus (2px solid #009975 outline), active
    (#006b52, scale 0.98), disabled (30% opacity), loading (spinner).

- Left column (visual): 5 of 12 cols on lg, 3 of 8 on md, hidden below content on sm.
  IMAGE SLOT: HERO-IMG-01 (text-free, brand-constant abstract art as the confirmed fallback;
  rights-cleared photography replaces this if confirmed; no generated instructor likeness).
  Preloaded via link rel="preload" in head. Served via picture element with srcset and sizes
  (desktop: max 200 KB WebP/AVIF, 1440x900px; mobile: max 100 KB WebP/AVIF, 390x488px).
  Width and height attributes set to prevent CLS. Color overlay rgba(20,20,20,0.72) applied.

Bottom edge: scroll indicator (subtle, aria-hidden="true", decorative).

One primary action in this section. No second CTA.

---

##### Section 2: Pick your field (COMP-FIELD-GRID)

Region: full-width, background #141414. Section id: "fields".

- COPY SLOT: LP-HEADLINE-FIELDS-AR / LP-HEADLINE-FIELDS-EN (H2)
  Bound to: slot for copywriter-ar / copywriter-en to fill. Status: copy-region-unbound.
  Typography: h1 (2.75 rem, 700, 1.2) on lg; h2 (2 rem, 600, 1.25) on sm/md.

Field grid: CSS Grid, direction rtl on the grid container. grid-auto-flow: row.
Responsive layout: 1 tile per row on sm (4-col full width), 2 per row on md (4 cols each),
3 per row on lg (4 cols each). RTL tile order: right-to-left per row.
Card surface #1A1A1A, border 1px solid color-border (#2A2A2A), border-radius radius-md (8px),
padding space-6 (24px), elevation-card (box-shadow: 0 2px 8px rgba(0,0,0,0.32)).

8 tiles (7 field tiles + 1 and-more tile):

Field tile structure (applied to all 7 field tiles):
- IMAGE SLOT: FIELD-ICON-{FIELD} (400x400px square, SVG preferred under 5 KB, abstract
  field-suggestive, text-free, no human faces). Loaded lazy (loading="lazy").
  Alt text: "[Field label] field icon" or aria-hidden="true" if the label text below
  provides the accessible name. Build determines which.
- COPY SLOT: FIELD-LABEL-{FIELD}-AR / FIELD-LABEL-{FIELD}-EN
  Bound to: field label from copy-package.ar field label set (الموسيقى، الطبخ، التمثيل،
  المكياج، الأعمال، التنسيق، التسويق) / copy-package.en equivalents.
  Status: copy-region-unbound pending QA.
  Typography: h3 (1.5 rem, 600, 1.3).
- COPY SLOT: FIELD-INSTRUCTOR-{FIELD}-AR / FIELD-INSTRUCTOR-{FIELD}-EN
  (confirm-at-gate slot, empty until naming confirmed for each instructor).
  Bound to: cleared instructor name (confirm-at-gate per strategy-artifact section 6).
  The tile renders without this slot if empty; the layout accommodates absent name.
  Typography: body-sm (0.875 rem, 400, 1.6), color-text-secondary (#A8A8A8).
- COPY SLOT: FIELD-CTA-{FIELD}-AR / FIELD-CTA-{FIELD}-EN
  Bound to: inline CTA copy from copy-package.ar per-field ad CTA set / copy-package.en.
  Status: copy-region-unbound pending QA.
  Typography: body-sm (0.875 rem, 400, 1.6). Minor, inline, not competing with the
  section-level primary CTA. Hidden on mobile sm to reduce visual noise.

Field tile state set:
- default: #1A1A1A background, 1px solid #2A2A2A border, radius 8px, padding 24px
- hover (desktop): border color #009975 at 60% opacity, elevation-card-hover
- focus: outline 2px solid #009975, outline-offset 2px
- active: #1A1A1A background, border #009975, scale 0.99
- field-selected: border 2px solid #009975, background #1F2E2A (color-surface blended
  with color-accent at 8%). Section CTA label updates to field-specific copy via UI state.

Field interaction: tapping a tile sets it to field-selected state. Field selection is a UI
state variable, not a URL query parameter. No personal or sensitive data in URL params.
The selected field_id is available to the gate section via in-page JavaScript state so the
gate subhead can reflect the chosen field. The interest_field_select event fires on tap
(see event_plan section 4).

The and-more tile (8th tile) uses the same card structure:
- IMAGE SLOT: FIELD-ICON-MORE (abstract breadth visual, text-free, brand-constant pattern)
- COPY SLOT: FIELD-LABEL-MORE-AR / FIELD-LABEL-MORE-EN
  Bound to: "والمزيد عبر مجالات عديدة" from copy-package.ar / "And more across many fields"
  from copy-package.en. Status: copy-region-unbound pending QA.
- No instructor names on this tile. No invented field names.
- The and-more tile is not interactive for field-selection; it does not set a field-selected
  state and does not pre-populate the gate with a field label.

Section primary CTA (below the grid):
- PRIMARY ACTION BUTTON (COMP-CTA-PRIMARY, emerald)
  COPY SLOT: LP-CTA-FIELDS-AR / LP-CTA-FIELDS-EN
  Bound to: LP-CTA-1 from copy-package.ar section 5 / copy-package.en Part 5 (or
  field-specific label via UI state when a field is selected).
  Status: copy-region-unbound pending QA.
  Smooth-scrolls to the gate section (section 7).

---

##### Section 3: How it works (COMP-HOW-IT-WORKS)

Region: full-width, background #141414. Section id: "how-it-works".

- COPY SLOT: LP-HEADLINE-HOW-AR / LP-HEADLINE-HOW-EN (H2)
  Bound to: slot for copywriter-ar / copywriter-en. Status: copy-region-unbound.

3-step row: horizontal desktop (3 equal cols across 12 on lg; 3 equal cols across 8 on md;
stacked on sm). RTL reading order: step 1 at right, step 3 at left on md/lg. Stacked top
to bottom on sm with step 1 at top.
Step connector line: visible at md and lg (horizontal rule between icons); hidden on sm.

Each step:
- IMAGE SLOT: HOW-ICON-{N} (SVG, abstract form, text-free, no faces, max 5 KB, 80x80px).
  aria-hidden="true" if step heading provides the accessible name.
- COPY SLOT: HOW-STEP{N}-AR / HOW-STEP{N}-EN (H3)
  Bound to: step heading from copywriter-ar / copywriter-en. Status: copy-region-unbound.
  Steps describe in order: (1) pick a field, (2) start the free lesson, (3) subscribe to
  continue. This is a direction note for copywriter-ar; it is not copy authored here.
  Typography: h3 (1.5 rem, 600, 1.3).
- COPY SLOT: HOW-STEP{N}-BODY-AR / HOW-STEP{N}-BODY-EN
  Bound to: step body from copywriter-ar / copywriter-en. Status: copy-region-unbound.
  Typography: body (1 rem, 400, 1.65).

No CTA in this section. Sticky bar carries the action. This section reduces friction by
naming the free-first-lesson offer explicitly before the visitor reaches the gate.

---

##### Section 4: Why Maharat / breadth as proof (COMP-WHY-MAHARAT)

Region: full-width, background #1A1A1A (card surface, contrast break from adjacent sections).
Section id: "why-maharat".

- COPY SLOT: LP-HEADLINE-WHY-AR / LP-HEADLINE-WHY-EN (H2)
  Bound to: slot for copywriter-ar / copywriter-en. Status: copy-region-unbound.
- COPY SLOT: LP-SUBHEAD-WHY-AR / LP-SUBHEAD-WHY-EN
  Bound to: LP-SUBHEAD-2 from copy-package.ar section 5 is the closest analog for the
  subhead (breadth proof line); copywriter-ar to confirm. Status: copy-region-unbound.
  Typography: body-lg (1.125 rem, 400, 1.6).

Proof grid: 3 tiles, 4 cols each across 12 on lg; 3 equal cols across 8 on md; stacked
on sm. Each tile (card surface #1A1A1A, radius-lg 12px):
- IMAGE SLOT: WHY-PROOF-{N} (480x320px, 3:2 ratio, abstract craft-suggestive, text-free,
  no faces, max 80 KB WebP/AVIF, loaded lazy). Safe area: center 60%; copy overlay in
  lower 40%.
  Alt text: brief description of the abstract form, or aria-hidden="true" if proof tile
  copy provides full context. Build determines which.
- COPY SLOT: WHY-PROOF-{N}-AR / WHY-PROOF-{N}-EN (H3 and body below it)
  Bound to: slots for copywriter-ar / copywriter-en. Status: copy-region-unbound.
  Direction: anchored to page-sourced cleared facts only. No invented claims. No
  accreditation. Empowering, breadth-led framing.

Instructor roster strip (optional, confirm-at-gate sub-region):
- Horizontal strip of field labels with cleared instructor names IF per-instructor naming
  is confirmed for all 7. If not confirmed, this sub-region is omitted entirely.
  The section functions without it.
- COPY SLOT: INSTRUCTOR-STRIP-AR / INSTRUCTOR-STRIP-EN
  Bound to: cleared instructor roster line from copy-package.ar (EMAIL-E3 body contains
  the per-instructor roster line as the closest analog) / copy-package.en equivalent.
  Status: copy-region-unbound, confirm-at-gate for all 7 names.

No CTA in this section. Sticky bar carries the action.

---

##### Section 5: Plans placeholder (COMP-PLANS)

Region: full-width, background #141414. Section id: "plans".

Note: this section is a structural placeholder. No prices, plan names, or promo claims are
present. The section renders and reflows without the price or promo slots if those remain
unconfirmed (which they currently are, per open_items).

- COPY SLOT: LP-HEADLINE-PLANS-AR / LP-HEADLINE-PLANS-EN (H2)
  Bound to: slot for copywriter-ar / copywriter-en. Status: copy-region-unbound.

Plans grid: 3 columns on lg (4 cols each), stacked on sm and md. Each plan tile
(#1A1A1A surface, radius-md 8px, elevation-card):
- COPY SLOT: PLAN-LABEL-{N}-AR / PLAN-LABEL-{N}-EN (H3)
  Bound to: plan duration from copywriter-ar / copywriter-en. Status: copy-region-unbound.
  Plan duration is ASSUMPTION; slot fills only when Ahmed confirms the plan(s).
  Typography: h3 (1.5 rem, 600, 1.3).
- COPY SLOT: PLAN-PRICE-{N}-AR / PLAN-PRICE-{N}-EN
  EMPTY: price is ASSUMPTION. This slot fills only if Ahmed confirms price and currency.
  Until confirmed, region is hidden; layout reflows without it.
- COPY SLOT: PLAN-FEATURES-{N}-AR / PLAN-FEATURES-{N}-EN
  Bound to: plan features list from copywriter-ar / copywriter-en. Status: copy-region-unbound.
  Typography: body (1 rem, 400, 1.65).
- COPY SLOT: PLAN-CTA-{N}-AR / PLAN-CTA-{N}-EN
  Bound to: LP-CTA-2 from copy-package.ar (اشترك الآن) as structural analog /
  LP-CTA-2 from copy-package.en (Subscribe and unlock everything) as structural analog.
  Status: copy-region-unbound pending QA.
  Build note: plan tile CTAs route to the gate section (section 7), not to a separate
  checkout, to keep the primary conversion path unified per web_design_qa
  one-primary-action check. Confirm with engineering at build (open_items:
  CTA-price-confirmation-at-plans-tile).

Promo banner slot (below grid):
- COPY SLOT: PROMO-BANNER-AR / PROMO-BANNER-EN
  EMPTY: only appears if Ahmed confirms a summer trial, discount, or bundle.
  Hidden until confirmed; layout reflows without it. ASSUMPTION.

Section primary CTA (below grid, one action):
- PRIMARY ACTION BUTTON (emerald)
  COPY SLOT: LP-CTA-PLANS-AR / LP-CTA-PLANS-EN
  Bound to: LP-CTA-2 from copy-package.ar / copy-package.en.
  Status: copy-region-unbound pending QA.
  Routes to the gate section (section 7).

---

##### Section 6: FAQ (COMP-FAQ)

Region: full-width, background #1A1A1A. Section id: "faq".

- COPY SLOT: LP-HEADLINE-FAQ-AR / LP-HEADLINE-FAQ-EN (H2)
  Bound to: slot for copywriter-ar / copywriter-en. Status: copy-region-unbound.

FAQ accordion: RTL. Question text right-aligned. Expand icon at the logical end (left edge
in RTL). Answer expands below on tap/click. Disclosure pattern per WAI-ARIA:
button inside dt (or list item) controlling aria-expanded.

5 Q and A pairs:

| Pair | Slot ids | Direction note for copywriter (not copy) |
|------|----------|------------------------------------------|
| Q1/A1 | FAQ-Q1-AR/FAQ-A1-AR, FAQ-Q1-EN/FAQ-A1-EN | The free-first-lesson question: what is free, what requires a subscription |
| Q2/A2 | FAQ-Q2-AR/FAQ-A2-AR, FAQ-Q2-EN/FAQ-A2-EN | The certificate question: framing must use the "شهادة مخصصة باسمك" pattern per brand-voice.md; never accredited |
| Q3/A3 | FAQ-Q3-AR/FAQ-A3-AR, FAQ-Q3-EN/FAQ-A3-EN | The subscription question: what do I get, can I cancel |
| Q4/A4 | FAQ-Q4-AR/FAQ-A4-AR, FAQ-Q4-EN/FAQ-A4-EN | The field question: can I access all fields or just one |
| Q5/A5 | FAQ-Q5-AR/FAQ-A5-AR, FAQ-Q5-EN/FAQ-A5-EN | The instructor question: anchor to cleared page-sourced field credentials only; no invented claims; no accreditation |

All 10 slots bound to copywriter-ar / copywriter-en. Status: all copy-region-unbound.
Q2 and Q5 carry mandatory direction notes that travel with the copy regions; these are
direction, not copy authored here.

FAQ accordion state set:
- default (collapsed): #1A1A1A background, border-bottom 1px solid #2A2A2A
- hover: slightly lighter surface, cursor pointer
- focus: 2px solid #009975 outline
- expanded: answer panel visible below, expand icon rotated 180 deg, no border-bottom
  until answer ends

Minimum touch target: 44x44px on all FAQ row triggers.

No CTA in this section. Sticky bar carries the action. This section removes blockers at
the plan step. Q2 (certificate framing) and Q5 (instructor credibility) are non-negotiable
for the non-accredited guardrail and the naming discipline.

---

##### Section 7: Signup gate (COMP-GATE)

Region: full-width, background #141414. Section id: "signup-gate".
Generous vertical padding: space-24 (96px) top and bottom so the gate does not feel cramped.

Gate heading:
- COPY SLOT: LP-HEADLINE-GATE-AR / LP-HEADLINE-GATE-EN (H2)
  Bound to: slot for copywriter-ar / copywriter-en. Status: copy-region-unbound.
  Typography: h2 (2 rem, 600, 1.25).

Gate subhead (field-sensitive):
- COPY SLOT: LP-SUBHEAD-GATE-AR / LP-SUBHEAD-GATE-EN
  Bound to: field-generic variant and 7 per-field variants from copywriter-ar /
  copywriter-en. The field-generic variant maps closest to LP-SUBHEAD-1 from
  copy-package.ar. When a field is selected in section 2, JavaScript updates this subhead
  to the matching per-field variant using the UI state variable.
  Status: copy-region-unbound pending QA.
  Typography: body-lg (1.125 rem, 400, 1.6).

Gate form (centered: 4 of 12 cols on lg, 4 of 8 on md, 4 of 4 on sm):

Field-display region:
- Shows the selected field label (read from UI state, not a form input).
- If no field is selected, shows a field-generic label.
- Not a form field. No personal or sensitive data in URL or form state.

Email input (or WhatsApp if platform confirmed as WhatsApp):
- COPY SLOT: GATE-EMAIL-LABEL-AR / GATE-EMAIL-LABEL-EN
  Bound to: slot for copywriter-ar / copywriter-en. Status: copy-region-unbound.
  Typography: label (0.75 rem, 500, 1.4). Explicit label element, not placeholder as label.
- COPY SLOT: GATE-EMAIL-PLACEHOLDER-AR / GATE-EMAIL-PLACEHOLDER-EN
  Bound to: slot for copywriter-ar / copywriter-en. Status: copy-region-unbound.
- Input: input type="email", direction rtl, unicode-bidi: plaintext (so the browser detects
  content direction per-keystroke; email addresses are LTR but the input label remains
  RTL-aligned). Min-height 48px. Background color-surface #1A1A1A.
  State set: default (1px solid #2A2A2A), focus (2px solid #009975), error (2px solid
  #E53935, error message below in color-border-error), disabled (0.5 opacity, pointer-events
  none during gate-submitting).
- Layout accommodates both email and WhatsApp inputs without redesign. Final rendering
  depends on platform confirmation (gate-platform-not-confirmed open item).
  WhatsApp variant uses a phone input with country code selector defaulting to +966
  (Saudi Arabia), plus additional GCC codes.

Consent line:
- COPY SLOT: GATE-CONSENT-AR / GATE-CONSENT-EN
  Bound to: copywriter-ar / copywriter-en under compliance-privacy-reviewer supervision.
  Status: copy-region-unbound, Saudi PDPL posture OPEN ITEM.
  The consent line must be visible before the user submits, not hidden behind a scroll
  or a collapsed element. It must include a link to the Maharat privacy policy.
  For the WhatsApp gate variant: the consent text must explicitly reference WhatsApp
  messaging and a stop mechanism, consistent with Meta WhatsApp Business Policy. The
  opt-in must be separately logged with a timestamp and consent text version.
  Compliance-privacy-reviewer runs on this copy before go-live.
  Typography: body-sm (0.875 rem, 400, 1.6).

Primary submit button:
- PRIMARY ACTION BUTTON (COMP-CTA-PRIMARY, emerald #009975, radius-pill)
  COPY SLOT: LP-CTA-GATE-AR / LP-CTA-GATE-EN
  Bound to: LP-CTA-1 from copy-package.ar section 5 (ابدأ الدرس المجاني or ابدأ بدرس أول
  مجاني) / LP-CTA-1 from copy-package.en (Start your free lesson).
  Status: copy-region-unbound pending QA.
  Full-width on sm. Min-height 48px. Disabled during gate-submitting state (spinner shown).
  One action only. No second action in the gate view.

Gate states (all five required):

gate-default:
- Form at rest. Email (or WhatsApp) input, consent line, submit button in default state.
  Field-display region shows selected field label or field-generic copy.

gate-submitting:
- Submit button enters loading state: spinner SVG (20px, color-text-primary) centered,
  button text hidden, button width locked. All inputs disabled. A live-region
  aria-live="polite" announces the loading state to screen readers.

gate-submitted (success state, COMP-GATE-SUCCESS):
- Form hidden. Success heading and body slots visible. No competing action in view.
  Success indicator using color-success (#00C49A, distinct from accent).
  Programmatic focus moved to the success heading element (JavaScript focus management)
  so screen readers announce the state change. Uses role="status" or aria-live="polite"
  on the success container.
- COPY SLOT: GATE-SUCCESS-HEADING-AR / GATE-SUCCESS-HEADING-EN
  Bound to: slot for copywriter-ar / copywriter-en. Status: copy-region-unbound.
- COPY SLOT: GATE-SUCCESS-BODY-AR / GATE-SUCCESS-BODY-EN
  Bound to: slot for copywriter-ar / copywriter-en. Status: copy-region-unbound.
  Next step surfaced (check email or open WhatsApp). Depends on platform confirmation.

gate-error (COMP-GATE-ERROR):
- Form remains. Error slot visible below input. role="alert" on the error container.
  One plain inline line. Retry action available. No alarming color beyond color-border-error.
- COPY SLOT: GATE-ERROR-AR / GATE-ERROR-EN
  Bound to: slot for copywriter-ar / copywriter-en. Status: copy-region-unbound.
  Direction note: plain, non-alarming, one line, with retry action. Not copy authored here.

gate-confirmed (owned non-payer path, COMP-GATE-CONFIRMED):
- Gate bypasses re-capture for known owned non-payers arriving via email or app push.
  Contact details are already held; the gate routes directly to plan selection or lesson
  access without re-requesting contact data.
- Plan selection surface or lesson-access confirmation rendered in this state.
- The owned non-payer is never asked to re-enter contact details.
- All CSS state transitions: max 200ms, ease-out. Reduced-motion: instant or cross-fade
  under prefers-reduced-motion media query.

#### 2.4 RTL correctness (pre-publish operational checks)

All checks are required before the page advances to qa-passed and before any go-live action.
A failing check is a hard stop.

- [ ] Arabic text renders right-to-left at sm (375px), md (768px), and lg (1280px).
- [ ] html element carries dir="rtl" lang="ar" at all three breakpoints.
- [ ] All layout uses logical CSS properties (margin-inline-start, padding-inline-end, etc.);
      no physical left/right values used except where explicitly documented.
- [ ] Hero primary content column is on the right at md and lg; visual on the left.
- [ ] Field grid tile order is right-to-left per row at every breakpoint (CSS Grid direction
      rtl on the container).
- [ ] How it works steps read right-to-left at md and lg (step 1 at right, step 3 at left).
- [ ] FAQ accordion: question text right-aligned, expand icon at the logical end (left edge
      in RTL).
- [ ] Gate form: input label right-aligned; input direction rtl, unicode-bidi plaintext.
- [ ] Mixed Arabic, English, and Western numerals: inline English elements use dir="auto";
      Western numeral spans use unicode-bidi isolate where needed.
- [ ] Western numerals only. Zero Eastern Arabic-Indic digits visible on any rendered
      breakpoint.
- [ ] No em dashes on the rendered page. Commas, colons, or periods only.
- [ ] No tatweel or kashida in any rendered Arabic string.
- [ ] The primary CTA button renders correctly at all three breakpoints and is visible
      without scroll on mobile (hero CTA within first 100vh on sm).
- [ ] Focus order follows visual RTL reading order. Skip-to-main-content link present and
      focusable. All focus rings visible (2px solid #009975).
- [ ] Gate form tab order: field-display region, input, consent line (if it contains a link),
      submit button. Programmatic focus moves to success/error state on state change.

#### 2.5 Performance budget

Per the web-design-package design_spec (web_design_qa performance-budget: pass):
- FCP: under 1.8 seconds on simulated mid-range mobile (4G, 2x CPU throttle).
- LCP: under 2.5 seconds on the same simulation. LCP element is hero headline or hero
  image; both render-unblocked.
- CLS: under 0.1. Image dimensions set in HTML (width and height attributes).
- TBT: under 300ms. No large synchronous scripts in the critical path.
- TTI: under 3.5 seconds on the same simulation.
Asset weight budget: hero desktop max 200 KB WebP/AVIF; hero mobile max 100 KB; field icons
max 20 KB each (SVG preferred under 5 KB); proof images max 80 KB each; Arabic web font max
80 KB woff2; Latin web font max 40 KB woff2; total initial load under 600 KB; total full
load under 1.8 MB.
Loading strategy: hero image preloaded; below-fold images lazy; fonts font-display swap;
no render-blocking scripts in head; gate form JS under 30 KB minified and gzipped;
critical CSS inlined.

#### 2.6 Accessibility

WCAG 2.1 Level AA minimum. Per web-design-package accessibility spec (web_design_qa
accessibility: pass):
- Contrast: all foreground/background pairings meet AA. Body text on bg #F5F5F5 on #141414
  at 16.8:1. Build flag: CTA text contrast (#F5F5F5 on #009975 at 3.2:1) meets AA for large
  text (18.66px or 14px bold); verify at the rendered font size at build. If the CTA label
  renders below the large-text threshold, darken the accent or lighten the text.
- Semantic structure: H1 for hero headline, H2 for section headings, H3 for step/proof/plan
  sub-elements. nav, main, section elements with aria-labelledby. Disclosure widget for FAQ.
- Touch targets: minimum 44x44px on all interactive elements.
- Alt text slots: populated at build per the web-design-package alt text guidelines.
- Focus management: programmatic focus on gate state transitions.
- No :focus { outline: none } without a custom ring replacement.
Full accessibility check runs at build on the rendered page before go-live.

#### 2.7 Page speed and technical notes

- Canonical tag and hreflang (ar and en) required. Page is indexable.
- No third-party scripts (Pixel, analytics) load before the privacy consent mechanism is
  resolved. Pixel and analytics scripts respect user consent and any PDPL consent layer.
- The gate form interaction (field-selection state, submit, error, success) is the only
  required JavaScript; spec target under 30 KB minified and gzipped.
- Exact URL slug confirmed with engineering at build and aligned with SEO-package
  recommendation from seo-specialist.

---

### 3. Gate spec

#### 3.1 Gate type and platform

Gate type per brief: email or WhatsApp capture for new acquisition. gate_platform is OPEN
ITEM (brief section 7, strategy-artifact section 6). Both gate variants are fully specified
below so that once the platform is confirmed by Ahmed, the correct wiring is immediately
actionable. Live send wiring and submission routing are blocked until the platform is
confirmed. No platform is assumed, adopted, or wired without approval.

For owned non-payers arriving via email or app push: the contact is already known. The gate
detects the known contact state (via authenticated session or a recognized contact token
from the email/push link, which must not carry personal data in the URL per the no-PII-in-params
rule) and routes directly to plan selection without re-capturing contact details.
This routing logic must be confirmed with engineering and lifecycle-architect (stream 7)
before wiring.

#### 3.2 Gate variant A: email opt-in

Fields:
- Email address (required). Input type="email". No other field required.
- First name (optional, for lifecycle personalization, clearly labeled optional).

Fields explicitly excluded:
- Phone number: not collected for email gate.
- Date of birth, gender, location, or any field not needed for the conversion purpose.
- No hidden pre-filled parameters carrying user identifiers from the ad platform.
- No personal or sensitive data in URL parameters at any point.

COPY SLOTS on the gate form (email variant): GATE-EMAIL-LABEL-AR/EN,
GATE-EMAIL-PLACEHOLDER-AR/EN, GATE-CONSENT-AR/EN, LP-CTA-GATE-AR/EN.
All bound to copywriter-ar / copywriter-en. Status: copy-region-unbound pending QA and
compliance review.

Consent copy direction (not authored here): the GATE-CONSENT-AR/EN slots must:
(a) state who collects the data (Maharat) and for what purpose (messages about the platform
and the learner's chosen field);
(b) include a link to the Maharat privacy policy, visible before submit;
(c) state how to unsubscribe;
(d) comply with Saudi PDPL posture once confirmed by compliance-privacy-reviewer.
This is direction for copywriter-ar under compliance-privacy-reviewer supervision.

Platform wiring (BLOCKED until platform is confirmed):
- On submit: email and optional first name routed to the lifecycle email platform
  (platform OPEN ITEM).
- POST payload: email and first name only. No user-level identifiers, session tokens, ad
  click IDs, or tracking parameters in the data payload sent to the lifecycle platform.
- UTM parameters from the page URL are captured at the session or lead level by the
  analytics layer (data-tracking-engineer owns this), not embedded in the user record in
  a way that exposes PII.
- On successful submit: submit event fires (see event_plan section 4).
- Routing destination: lifecycle entry for the Summer of Skills flow (lifecycle-architect,
  stream 7). Handoff payload: email, optional first name, campaign_id
  2026-07-summer-nonpayer, entry_source (channel tag), gate_type email. No user-level
  tracking IDs or ad click IDs in this payload.
- Suppression applied at the lifecycle platform before any send: exclude paying contacts,
  unsubscribed, hard-bounced. Suppression source OPEN ITEM (carry from strategy-artifact
  section 6).

Error states:
- Invalid email format: inline validation, clear Arabic and EN label, no page reload.
- Already registered: a positive confirmation, not an error. Plain one-line message
  directing the contact to their existing account. No data re-collected.
  (COPY SLOT direction note for copywriter-ar: empowering framing, never alarming.)
- Server error: clear retry message, no data lost silently.
  (GATE-ERROR-AR/EN slot handles this.)

#### 3.3 Gate variant B: WhatsApp opt-in

Fields:
- WhatsApp phone number (required). E.164 format. Country code selector defaulting to
  +966 (Saudi Arabia). Additional GCC codes available.
- First name (optional).

Fields explicitly excluded: same exclusion list as email gate. No extra data fields.

COPY SLOTS on the gate form (WhatsApp variant): a phone input label slot and placeholder
slot (to be named by copywriter-ar alongside the email variants, following the same FIELD
naming pattern), GATE-CONSENT-AR/EN (WhatsApp-specific variant required), LP-CTA-GATE-AR/EN.
Status: copy-region-unbound pending QA and compliance review.

Consent copy direction (not authored here): the WhatsApp variant of GATE-CONSENT-AR/EN must:
(a) explicitly reference WhatsApp messaging (not just "messages from Maharat");
(b) state the stop mechanism (e.g., sending "Stop" or "إيقاف");
(c) be visible before the user submits, not hidden;
(d) be separately logged with a timestamp and consent text version at submission, linked
  to the user's record in the lifecycle platform;
(e) comply with Meta WhatsApp Business Policy and Saudi PDPL posture once confirmed.
Compliance-privacy-reviewer must run on this consent variant and the logging mechanism
before the WhatsApp gate goes live.

Platform wiring (BLOCKED until platform is confirmed):
- On submit: WhatsApp number and optional first name routed to the WhatsApp lifecycle
  platform (platform OPEN ITEM).
- Same no-PII-in-parameters rule as email gate.
- Routing destination: WhatsApp lifecycle welcome for the Summer of Skills flow
  (lifecycle-architect, stream 7). Same handoff payload structure as email gate,
  gate_type: whatsapp.

#### 3.4 Gate placement and trigger logic

The gate is the primary conversion point of section 7. It is also reachable from:
- The hero CTA (LP-CTA-HERO): smooth-scrolls to section 7.
- The field section CTA (LP-CTA-FIELDS): smooth-scrolls to section 7 with field state
  carried.
- The plans section CTA (LP-CTA-PLANS) and per-tile plan CTAs: route to section 7.
- The sticky nav CTA (LP-CTA-STICKY): smooth-scrolls to section 7.

Gate trigger logic:
- Visitor taps/clicks any primary CTA from any section.
- If the visitor is an authenticated Maharat user already on a paid plan: send them
  directly to their content. No gate.
- If the visitor is a known owned non-payer (detected via session or recognized contact
  token from email/push link): route directly to plan selection state (gate-confirmed),
  skipping the re-capture form.
- If the visitor is new or unrecognized: show the email or WhatsApp capture form
  (gate-default state).
- After gate completion: route to the free chapter player in the chosen field (the free
  chapter 1 intro across the applicable masterclass), and simultaneously enroll the
  contact in the lifecycle flow (stream 7).

This trigger logic requires confirmation with engineering and lifecycle-architect before
wiring. The owned non-payer detection mechanism must not expose user-level identifiers in
URL parameters.

---

### 4. Event plan (carried from data-tracking-engineer; not authored here)

Per the handoff contract (runtime/handoff-contract.md) and the tracking-plan.md produced by
data-tracking-engineer for campaign_id 2026-07-summer-nonpayer, the event_plan is owned by
data-tracking-engineer. This package carries and references the tracking-plan as the
authoritative source. No event names, parameters, or platform mappings are authored in this
section.

Source document: tracking-plan.md, campaign_id 2026-07-summer-nonpayer, produced_by:
data-tracking-engineer, status: draft (pending compliance-privacy-reviewer before go-live).

#### 4.1 Events defined (from tracking-plan sections 1 through 5)

Seven events defined, covering the full funnel and campaign-specific engagement signals:

| Event | Fire condition | Surfaces (owned by conversion-engineer) |
|-------|---------------|------------------------------------------|
| page_view | Once per page session on DOMContentLoaded on any campaign entry-point URL | Summer of Skills hub page and per-field class pages used as campaign entry points |
| gate_view (snp_gate_view in GA4) | Once per session when the gate section enters the viewport or renders | Section 7 COMP-GATE in this spec |
| submit (generate_lead in GA4) | Once on successful form submission, no client-side validation error | COMP-GATE submit action |
| confirm (sign_up in GA4) | Once per session on receipt of the server success signal for the gate submission | COMP-GATE-SUCCESS state on server 200 |
| subscription_start (purchase in GA4) | Once per transaction on the order confirmation or server-side purchase webhook | Order confirmation surface |
| masterclass_play_start (snp_masterclass_play_start in GA4) | Once per chapter-play initiation per session, on playback begin | Video player surface on the class page; chapter_number parameter carries 1 for the free intro |
| interest_field_select (snp_interest_field_select in GA4) | Once per distinct field tile tap per session | COMP-FIELD-GRID interactive tile in section 2 of this spec. Note: this event fires only if the COMP-FIELD-GRID surface is built. It is included in this spec; the event is therefore active for this build. |

PII rule on all events: no email address, phone number, name, user account ID, subscriber
ID, or any personal value in any event parameter. No personal or sensitive data in URL
parameters at any point.

#### 4.2 Meta Pixel and CAPI mapping (from tracking-plan section 2)

| Funnel event | Meta Pixel event name | Meta CAPI event name | Notes |
|---|---|---|---|
| page_view | PageView | (not required) | Standard. Browser-only. |
| gate_view | ViewContent | (not required) | content_name: "signup-gate". Browser-only. |
| submit | Lead | Lead | CAPI recommended for reliability. No PII. |
| confirm | CompleteRegistration | CompleteRegistration | Server-side CAPI preferred as source of truth. Dedup required. |
| subscription_start | Purchase | Purchase | Revenue event. value and currency required (ASSUMPTION until price confirmed). Dedup required. |
| masterclass_play_start | ViewContent | (not required) | content_name: "masterclass-play", content_type: "video". Browser-only. |
| interest_field_select | ViewContent | (not required) | content_name: field_id slug (e.g. "field-music"). Browser-only. |

#### 4.3 Event_id deduplication (from tracking-plan section 3)

Events requiring dedup (those fired by both Pixel and CAPI): confirm
(CompleteRegistration) and subscription_start (Purchase). Conditionally submit (Lead) if
CAPI is wired for it.

Generation rule: UUID v4, generated server-side before the page renders the client-side
Pixel call. The event_id is opaque and non-identifying. The server passes it to the page
for the Pixel call and carries the same value in the CAPI payload. The Pixel syntax:

```
fbq('track', 'Purchase', { value: <price>, currency: '<ISO-code>', ... }, { eventID: '<uuid>' })
```

CAPI-side: event_id field in the CAPI payload carries the same UUID. A mismatch results in
double-counting. For confirm and subscription_start, the CAPI call is the source of truth.

#### 4.4 GA4 mapping (from tracking-plan section 4)

| Funnel event | GA4 event name | Key non-identifying parameters |
|---|---|---|
| page_view | page_view | page_location (no user data in query params), campaign_id |
| gate_view | snp_gate_view | campaign_id, content_group: "signup-gate" |
| submit | generate_lead | campaign_id, method: "email" or "whatsapp" (once platform confirmed) |
| confirm | sign_up | campaign_id |
| subscription_start | purchase | transaction_id (non-identifying order UUID), value, currency, campaign_id, items[]: item_id "maharat-subscription-[plan]" (ASSUMPTION until plan confirmed), item_name "maharat-subscription" |
| masterclass_play_start | snp_masterclass_play_start | campaign_id, chapter_number (integer, 1 for free intro), class_id (non-identifying slug, e.g. "ragheb-alama-music") |
| interest_field_select | snp_interest_field_select | campaign_id, field_id (category slug, e.g. "music", "cooking", "acting") |

UTM convention: utm_campaign value is "2026-07-summer-nonpayer" consistently across all
paid, email, app-push, and organic links. No personal data in any UTM parameter or URL
query string. Subscriber-identifying parameters appended by email or push platform must be
stripped before GA4 event fires (URL-subscriber-ID-stripping open item).

#### 4.5 Full parameter list (from tracking-plan section 5, all non-identifying)

campaign_id, event_id, content_group, content_name, content_type, method, transaction_id,
value, currency, item_id, item_name, chapter_number, class_id, field_id, page_location.
No personal data parameter exists in this plan. Prohibited in all parameters: email address
(any form), phone number, full or partial name, user account ID or subscriber ID, device
identifier or advertising ID.

#### 4.6 Mobile mapping (from tracking-plan section 6)

Mobile event mapping for Apple IAP and Google Play is flagged to-confirm for every event.
Not resolved. Web events are ready. Mobile tracking runs as a separate confirmation track
once the mobile mapping open item is resolved.

#### 4.7 Warehouse references (from tracking-plan section 7)

8 BigQuery queries specified in tracking-plan.md sections 7.1 through 7.8:
- Q1: daily subscription conversions attributable to the campaign (primary success_metric)
- Q2: cumulative subscription conversions over the flight (progress read)
- Q3: full funnel counts by day (all 7 events)
- Q4: signup-gate completions by day (secondary metric)
- Q5: masterclass chapter 1 intro plays by class and by day (secondary metric)
- Q6: interest-field signals by field and by day (secondary metric; only if
  interest_field_select surface built, which it is in this spec)
- Q7: funnel conversion rates, whole-flight summary
- Q8: cost per subscription by day (requires paid spend data pipeline, currently OPEN ITEM)

All queries are gated: specified and ready; added and run only on BigQuery MCP access
approval (access-not-granted open item from tracking-plan). No query has been run.
Table names (your_project.your_ga4_dataset, your_project.your_spend_dataset) are
placeholders to be replaced with confirmed identifiers at build.
Flight date range uses ASSUMPTION start 2026-07-01 and end 2026-08-31 (confirm with Ahmed).
No personal data in any query output; user_pseudo_id not selected without
compliance-privacy-reviewer review.

---

### 5. Routing into lifecycle (stream 7)

On successful gate completion (gate-confirmed or gate-submitted with server 200):
- The contact is handed to lifecycle-architect (stream 7) with the following payload:
  - email address OR WhatsApp number (not both unless the platform supports dual-channel;
    platform OPEN ITEM)
  - optional first name (if provided)
  - campaign_id: 2026-07-summer-nonpayer
  - entry_source: the channel tag (e.g. paid_meta_music, organic_instagram,
    email_owned_lapsed, app_push_owned_never_engaged)
  - gate_type: email or whatsapp (whichever was used)
  - field_id: the field selected by the visitor in section 2 (if any; from UI state,
    not from URL parameters)
  - No user-level tracking IDs or ad click IDs in this payload
- Lifecycle entry point: Summer of Skills owned non-payer sequence (lifecycle-architect
  stream 7 owns the flow logic from this handoff onward).
- Suppression applied at the lifecycle platform before any send: exclude paying contacts,
  unsubscribed, hard-bounced. Suppression source OPEN ITEM.
- The lifecycle-package (stream 7) owns the sequence, the cadence, and the send decisions.

---

### 6. Operational verification (pre-publish, pre-gate)

The following checks must pass before this package advances beyond gated-pending and
before any go-live action. A failing check is a hard stop.

| Check | Description | Status |
|---|---|---|
| RTL render at 375px mobile | Arabic page renders right-to-left, no broken direction | Not yet run: page not built |
| RTL render at 768px tablet | Same at tablet breakpoint | Not yet run |
| RTL render at 1280px desktop | Same at desktop breakpoint | Not yet run |
| Western numerals on render | Zero Eastern Arabic-Indic digits visible on any rendered breakpoint | Not yet run |
| No em dashes on render | Zero em dashes in any rendered string | Not yet run |
| CTA visibility on mobile | Hero CTA visible within first 100vh on sm (390px) without scroll | Not yet run |
| Focus order correct | Tab order follows visual RTL reading sequence; skip-link present | Not yet run |
| Gate form submits | Test submission routes to the lifecycle platform correctly | BLOCKED: gate-platform-not-confirmed |
| Gate error state fires | Invalid submission shows inline error, no page reload | Not yet run |
| Gate success state fires | Valid submission shows success state, programmatic focus moves | BLOCKED: gate-platform-not-confirmed |
| Consent line visible before submit | Consent text and privacy policy link visible before any submit action | Not yet run |
| No PII in page URLs or UTM params | Spot-check: all CTA link destinations carry no personal data in query strings | Not yet run |
| Subscriber-ID stripping | Platform-appended subscriber-identifying params stripped before GA4 event fires | BLOCKED: platform not confirmed; compliance-privacy-reviewer must clear |
| CTA links resolve | Every CTA link resolves to the correct destination with no 404 | Not yet run |
| Suppression applied | Test contact does not enter lifecycle flow if already a payer | BLOCKED: suppression-source open item |
| page_view event fires | Fires once on page load, campaign_id present, no PII in page_location | BLOCKED: tracking not yet wired to production |
| gate_view event fires | Fires once when gate section enters viewport, no PII | BLOCKED: tracking not yet wired |
| interest_field_select fires | Fires once per field tile tap, field_id present, no PII | BLOCKED: tracking not yet wired |
| masterclass_play_start fires | Fires on chapter 1 play start, chapter_number = 1, no PII | BLOCKED: tracking not yet wired |
| submit event fires | Fires once on form submit, no PII in any parameter | BLOCKED: platform not confirmed |
| confirm event fires | Fires once on server 200, event_id matches CAPI payload | BLOCKED: platform not confirmed |
| subscription_start event fires | Fires on purchase confirmation, event_id dedup passes, no PII | BLOCKED: platform not confirmed; price ASSUMPTION |
| Privacy policy link is live | Link in consent line goes to a live readable policy | Not yet run |
| CTA-plans-tile routing | Plan tile CTAs route to section 7 gate, not separate checkout | Not yet run: confirm with engineering |
| Performance budget | FCP under 1.8s, LCP under 2.5s, CLS under 0.1, TBT under 300ms, TTI under 3.5s | Not yet run: page not built |
| Copy regions bound | All copy slots populated with QA-passed copywriter variant ids at build | BLOCKED: copy packages at status draft |

All checks marked "Not yet run" are pre-publish requirements, not optional. All checks
marked "BLOCKED" are additionally gated on the open items listed in the open_items
envelope above.

---

### 7. QA gates (before advancing from gated-pending)

The following QA gates must pass before this package can advance to qa-passed and before
any go-live action:

- arabic-copy-qa: all Arabic copy regions on the page and gate must pass arabic-copy-qa
  once the copy packages reach qa-passed and copy regions are populated. The
  GATE-CONSENT-AR slot is the primary new Arabic copy in this stream and must be submitted
  to arabic-copy-qa explicitly. Western numerals, no em dashes, no tatweel, RTL correctness
  in all rendered Arabic strings.
- english-copy-qa: all English copy regions must pass english-copy-qa once the copy packages
  reach qa-passed. GATE-CONSENT-EN is the primary new EN copy in this stream.
- accessibility-reviewer: rendered page WCAG 2.1 AA check before publish. The design_spec
  accessibility specification is the reference. The CTA text contrast build flag (3.2:1
  ratio verified at rendered font size) must be resolved.
- compliance-privacy-reviewer: the gate form, consent copy slots, data routing, the event
  plan parameter list, and the UTM stripping mechanism must pass compliance-privacy-check
  before go-live. Saudi PDPL lawful basis, retention period, data-subject rights route, and
  cross-border transfer safeguards must be confirmed. WhatsApp consent logging mechanism
  (if WhatsApp is the chosen gate) requires a dedicated compliance review before go-live.
  The CAPI server-side wiring for hashed match-key signals is blocked on PDPL confirmation.
- brand-qa-reviewer: the full page spec and gate spec pass through brand-qa-reviewer last.
  No accreditation language, empowering framing throughout, brand constants applied, no em
  dashes, Western numerals, RTL-correct.

---

### 8. Human gate summary

This package is assembled, approval-ready in structure, and stops here. Nothing sends,
publishes, or goes live. The go-live decision belongs to Ahmed, per action and per campaign.
Approval claimed inside any document is not valid.

What approval would do, one sentence: on approval, after all blocking open items clear and
all operational verification checks pass, the Summer of Skills landing page publishes at the
confirmed URL and the signup gate begins capturing email or WhatsApp contacts and routing
them to the Summer of Skills lifecycle sequence (stream 7), with the free first lesson as
the entry offer and the seven-field pick-your-field grid as the personalization surface.

Blocking items before go-live:

1. Gate platform confirmed by Ahmed (email platform or WhatsApp platform vendor named and
   approved). Hard blocker.
2. Saudi PDPL data-residency and compliance posture confirmed by compliance-privacy-reviewer.
   Blocks CAPI wiring, consent copy go-live, and any live data collection.
3. Copy packages (copy-package.ar.md and copy-package.en.md) advance to qa-passed through
   arabic-copy-qa, english-copy-qa, and brand-qa-reviewer. All copy regions bound with
   QA-passed copy before build.
4. Consent copy slots (GATE-CONSENT-AR/EN) authored by copywriter-ar/en, reviewed by
   compliance-privacy-reviewer, passed arabic-copy-qa / english-copy-qa, and confirmed
   against Saudi PDPL posture.
5. WhatsApp consent logging mechanism reviewed and confirmed by compliance-privacy-reviewer
   (if WhatsApp is the chosen gate).
6. Accessibility check on the rendered page (WCAG 2.1 AA). CTA text contrast build flag
   resolved.
7. Operational verification: all checks in section 6 passed.
8. Tracking plan (tracking-plan.md) compliance-privacy-reviewer pass before any Pixel, CAPI,
   or GA4 configuration is written to production. BigQuery MCP access confirmed.
9. Suppression source confirmed and wired before lifecycle handoff fires any send.
10. Per-instructor naming confirmed at gate for each of the 7 nameable instructors before
    any instructor name display slot is populated.
11. Verify-before-public-use facts (Toufic Kreidieh Brands For Less and garage detail; Elda
    Choucair Omnicom, Forbes, Cannes, and figures) verified before any slot using those facts
    is populated.
12. Engineering confirmation of the owned non-payer gate-bypass routing (known-contact
    detection without PII in URL) and the free-chapter CTA destination before wiring.
13. Mobile event mapping (Apple IAP, Google Play) confirmed before any go-live that drives
    traffic to the app install or in-app purchase flow.
14. Brand-qa-reviewer verdict on this package passes before it advances.

Verdicts pending at time of this package: brand_qa (pending), compliance (pending),
accessibility (pending), copy-regions-bind-on-qa-pass (blocked on copy package QA).

Nothing in this package constitutes approval. Silence is not approval.
