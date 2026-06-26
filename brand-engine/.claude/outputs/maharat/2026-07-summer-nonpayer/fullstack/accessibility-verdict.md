# Accessibility QA Verdict: Summer of Skills

```
campaign_id:  2026-07-summer-nonpayer
gate:         accessibility-qa
checked_by:   accessibility-reviewer
date:         2026-06-12
assets:
  - web-design-package.md + conversion-package.md (Summer of Skills landing page, stream 6)
  - lifecycle-package.md + copy-package.ar.md + copy-package.en.md (emails E1..E5, stream 7)
prior_gates:
  - skill_eval:    pass (conversion-package envelope; lifecycle-package envelope)
  - web_design_qa: pass (web-design-package 2026-06-12, all 10 checks pass)
  - design_qa:     in flight (design-specs.md present; running alongside this gate per verification.md)
wcag_standard: WCAG 2.2 AA
```

---

## Revision history

```
v1  2026-06-12  Initial verdict: page FAIL (6 items), email FAIL (5 items).
                Fix list issued to conversion-engineer (page) and lifecycle-architect (email).
v2  2026-06-12  Re-verification after web-designer applied all addressable fixes to
                web-design-package.md (design_spec revised, web_design_qa: pass, fix_list empty).
                Result: page PASS, email PASS. Two render-block items carried as open items.
```

---

## RE-VERIFICATION SUMMARY (v2)

```
page_result:   PASS
email_result:  PASS

render_block_open_items: 2 (carried forward, not failures)
  1. focus-order-render-check: focus order across all 5 gate states and FAQ accordion
     at all 3 breakpoints. Requires the rendered, interactive page. Must complete
     before go-live. Not a spec failure.
  2. email-template-render-check: full email template render (semantic headings,
     plain-text alternative, alt text, CTA contrast at rendered size, tap target,
     RTL at 375 px). Blocked until send-platform is confirmed. Must complete before
     any send action. Not a spec failure.

contrast_ratios_recomputed (WCAG relative luminance formula, sRGB):
  CTA button label: #141414 on #009975
    L(#141414) = 0.00702
    L(#009975) = 0.24051
    ratio = (0.24051 + 0.05) / (0.00702 + 0.05) = 0.29051 / 0.05702 = 5.10:1
    threshold (normal text, 16 px 600 weight): 4.5:1
    result: PASS (margin 0.60:1 above threshold)

  error text: #F04040 on #1A1A1A
    L(#F04040) = 0.22573
    L(#1A1A1A) = 0.01034
    ratio = (0.22573 + 0.05) / (0.01034 + 0.05) = 0.27573 / 0.06034 = 4.57:1
    threshold (normal text, 14 px 400 weight): 4.5:1
    result: PASS (margin 0.07:1 above threshold; thin margin; verify at rendered size)

  hover border (non-text): #009975 at full opacity on #1A1A1A
    L(#009975) = 0.24051  L(#1A1A1A) = 0.01034
    ratio = (0.24051 + 0.05) / (0.01034 + 0.05) = 0.29051 / 0.06034 = 4.81:1
    threshold (non-text contrast, WCAG 1.4.11): 3:1
    result: PASS

note_on_spec_stated_ratios:
  The design_spec states approximately 5.7:1 for the CTA fix and approximately 4.90:1
  for the hover border. The recomputed values (5.10:1 CTA, 4.81:1 hover) are slightly
  lower than the spec approximations. Both still pass their respective thresholds by a
  clear margin. The error text spec figure of 4.6:1 is consistent with the recomputed
  4.57:1 (rounding difference only). All three pass.
```

---

## Part 1: Landing Page (RE-VERIFICATION)

```
asset:    Summer of Skills landing page (web-design-package.md design_spec + conversion-package.md)
gate:     accessibility-qa
result:   PASS
checked:  contrast-aa, rtl-reading-order, text-alternatives, semantic-structure,
          control-and-link-labels, target-size, keyboard-and-focus, color-independence,
          motion-safe, spec-only-render-block
```

### Check-by-check re-verification against the prior fix list

**Fix 1: contrast-aa, CTA button label**

Prior state: #F5F5F5 on #009975, 3.30:1, failed AA (4.5:1) for 16 px 600-weight normal text.

Fix applied per web-design-package.md:
- Token color-text-on-accent updated to #141414.
- Applied to all 5 button positions: sticky CTA, hero CTA, field section CTA, plans CTA,
  gate submit button.
- design_spec interaction states table, web_design_qa accessibility section, and the color
  tokens table all confirm #141414 on #009975.

Recomputed ratio: 5.10:1 (see summary above).
Threshold: 4.5:1 for normal text.
Result: PASS. The fix is consistently applied across all 5 button instances in the spec.

Note: the spec states approximately 5.7:1. The recomputed value is 5.10:1. Both pass.
The discrepancy is in the approximation; the WCAG pass is unaffected. At the rendered build
the ratio must be verified; the margin above threshold (0.60:1) is sufficient to be robust
to minor font-render variation.

**Fix 2: contrast-aa, error text**

Prior state: #E53935 on #1A1A1A, 4.19:1, failed AA (4.5:1) for 14 px 400-weight normal text.

Fix applied per web-design-package.md:
- New token color-text-error introduced at #F04040.
- Applied to error message text below the gate input in the error state.
- Token color-border-error remains #E53935 (border only, passes 3:1 non-text at 4.19:1,
  which was always correct).
- design_spec interaction states table (form input, error state row) and the color tokens
  table both confirm color-text-error #F04040.

Recomputed ratio: 4.57:1.
Threshold: 4.5:1 for normal text.
Result: PASS. Margin is narrow (0.07:1). This is flagged for build verification: confirm the
error text renders at exactly 14 px (0.875 rem) weight 400. If the rendered size is smaller
(sub-14 px) or the font substitution increases effective weight, verify this pairing again
on the actual render. The spec value and threshold are both correct; the narrow margin is
noted, not a failure at spec level.

**Fix 3: contrast-aa, hover border**

Prior state: #009975 at 60% opacity on #1A1A1A, approximately 2.4:1 effective, failed
non-text contrast (WCAG 1.4.11, threshold 3:1).

Fix applied per web-design-package.md:
- Field tile hover border changed to full-opacity 1 px solid #009975.
- design_spec interaction states table (field tile, hover row) confirms: "Border color
  color-accent (#009975) at full opacity (1 px solid)."
- Accessibility notes table confirms: "Hover border on surface #009975 / #1A1A1A / 4.90:1
  / Full opacity, meets WCAG 1.4.11 (3:1)."

Recomputed ratio: 4.81:1.
Threshold: 3:1 non-text contrast (WCAG 1.4.11).
Result: PASS.

**Fix 4: color-independence, error icon**

Prior state: COMP-GATE-ERROR conveyed error by color (red border, red text) only. The
role="alert" handled the programmatic signal but there was no non-color visual cue.

Fix applied per web-design-package.md:
- A circle-exclamation icon (inline SVG, 16 px, color-text-error #F04040) is now specified
  inline before the error text in the gate error state.
- design_spec interaction states table (form input, error state row) confirms: "a
  circle-exclamation icon (inline SVG, 16 px, color-text-error #F04040) followed by error
  text in color-text-error."
- gate states table (gate-error row) confirms: "inline error with circle-exclamation icon
  (color-text-error #F04040) preceding the error text."
- role="alert" on the error container is confirmed.

Both color and non-color cues present. WCAG 1.4.1 color independence satisfied.
Result: PASS.

**Fix 5: color-independence, required field**

Prior state: the required email input had no pre-submission indicator beyond the error
border firing after a failed submit attempt. Color alone (error red on submit) was the
only signal.

Fix applied per web-design-package.md:
- An asterisk (*) adjacent to GATE-EMAIL-LABEL is now specified.
- A new copy slot GATE-REQUIRED-NOTE-AR / GATE-REQUIRED-NOTE-EN is introduced at the top
  of the gate form, to be populated by copywriter-ar / copywriter-en with the "* required
  field" explanatory note.
- design_spec wireframe (section 7, email input region) confirms: "[REQUIRED INDICATOR:
  an asterisk (*) immediately adjacent to the label text, plus a note at the top of the
  form reading '* required field' ... The required status is conveyed by both the asterisk
  symbol and the explanatory label text, not by color alone.]"
- The copy-overlay slot index confirms GATE-REQUIRED-NOTE-AR and GATE-REQUIRED-NOTE-EN
  as new slots with the correct direction.
- web_design_qa accessibility section confirms: "Color independence, required field: FIXED."

Required status is conveyed before submission by non-color means (asterisk symbol plus
explanatory text). WCAG 1.4.1 satisfied.
Result: PASS.

**Alt-text slots (page imagery)**

Prior state: passed at spec level in v1; no change required.

Re-verification: the accessibility notes section of web-design-package.md lists explicit
alt-text slot requirements for all 14 image regions on the page: HERO-IMG-01, 8
FIELD-ICON-xx slots, 3 HOW-ICON-xx slots, and 3 WHY-PROOF-xx slots. Requirements are
correct (non-empty descriptive alt for meaningful images, alt="" for decorative, or
aria-hidden where the adjacent label text provides the accessible name). Email imagery
alt-text slots also specified in the email render spec section (alt="" on abstract header
art, descriptive alt for any meaning-carrying body images).
Result: PASS.

**Checks confirmed passing from v1 (no regression detected)**

- rtl-reading-order: dir="rtl" on html element, logical CSS properties throughout, RTL
  tile order, RTL FAQ, RTL form inputs with unicode-bidi plaintext. No LTR leakage. No
  Eastern Arabic-Indic digits. No em dashes. No tatweel. Web_design_qa responsive-rtl: pass.
  No change to this area in the revised spec. No regression.

- semantic-structure: H1 hero headline, H2 section headings, H3 step/proof/plan headings,
  nav, main, section with aria-labelledby, FAQ disclosure pattern, gate form with explicit
  label, gate success with role="status" or aria-live, gate error with role="alert". All
  unchanged and confirmed in the revised spec. No regression.

- control-and-link-labels: all CTAs carry descriptive copy slots. No bare click-here or
  اضغط هنا. Nav links descriptive. No change in the revised spec. No regression.

- target-size: minimum 44 x 44 px on all interactive elements, CTA buttons 48 px min-height,
  form inputs 48 px min-height, FAQ row triggers 44 x 44 px. Confirmed in the revised spec.
  No regression.

- keyboard-and-focus: skip-to-main-content link specified, full focus order documented,
  2 px solid #009975 focus ring on all interactive elements (4.81:1 on #1A1A1A, passes 3:1),
  no outline:none without replacement. Focus order render-block carried as open item. No
  regression at spec level.

- motion-safe: all transitions max 200 ms ease-out, prefers-reduced-motion query specified
  (reduces to instant or cross-fade), no autoplay, no flash. Confirmed unchanged. No
  regression.

- color-independence (non-error states): no state or meaning conveyed by color alone outside
  the error state (which is now fixed). No regression.

**Render-block open items (carried, not failures)**

```
{
  check:   "spec-only-render-block",
  element: "focus order verification across all 5 gate states (gate-default, gate-submitting,
            gate-submitted, gate-error, gate-confirmed) and the FAQ accordion at all 3
            breakpoints. Specifically: (a) programmatic focus move to the success heading on
            gate-submitted, (b) programmatic focus move to error container on gate-error,
            (c) FAQ accordion answer content becoming keyboard-focusable on expand.",
  status:  "open item, not a failure. Spec correctly specifies the intent. Cannot verify
            programmatic focus moves at spec level. Carry to rendered build verification
            before go-live. The page must not advance to go-live without this check.",
  carried_from: "v1 verdict"
}

{
  check:   "spec-only-render-block",
  element: "measured CTA contrast at rendered font size. Recomputed ratio is 5.10:1 on the
            fixed #141414 on #009975 pairing. This comfortably passes 4.5:1 normal text and
            the 3:1 large-text threshold. No render-level uncertainty remains on the CTA
            contrast itself. This item is substantially resolved; carry only to confirm the
            token is applied in the build.",
  status:  "substantially resolved at spec level. Low residual risk. Confirm at build."
}
```

---

## Part 2: Emails E1..E5 (RE-VERIFICATION)

```
asset:    Lifecycle email sequence E1..E5 (lifecycle-package.md + copy-package.ar.md
          variants EMAIL-E1..EMAIL-E5 + copy-package.en.md variants EMAIL-E1..EMAIL-E5)
gate:     accessibility-qa
result:   PASS
checked:  contrast-aa, rtl-reading-order, text-alternatives, semantic-structure,
          control-and-link-labels, target-size, keyboard-and-focus, color-independence,
          motion-safe, spec-only-render-block
```

### Check-by-check re-verification against the prior email fix list

**Email Fix 1: semantic-structure**

Prior state: no confirmed semantic HTML heading structure, no plain-text alternative, no
decorative image handling specified in the email template.

Fix applied per web-design-package.md (email render spec section, added in this revision):
- H1 (or role="heading" aria-level="1") required for the primary message line of each email
  (E1 to E5, both AR and EN).
- H2-equivalent required for sub-sections where used.
- Plain-text alternative required for all 5 emails in both AR and EN. Authoring
  responsibility assigned: copywriter-ar (AR plain-text) and copywriter-en (EN plain-text).
  Requirements for plain-text: all substantive copy, CTA as labeled URL, no HTML markup.
  Submitted to arabic-copy-qa and english-copy-qa gates alongside the HTML variants.
- Abstract brand-constant header imagery specified as alt="" (decorative) in the email
  render spec and alt-text slots table.

web_design_qa accessibility section confirms: "Email accessibility (WCAG 2.2 AA, spec-level):
Semantic heading structure: required ... Plain-text alternative: required ... Email header
imagery alt text: alt='' (decorative) on abstract brand-constant art."

Result: PASS at spec level. Render-block carried as open item (final verification requires
the rendered email template).

**Email Fix 2: text-alternatives**

Prior state: no alt-text slots specified for email header or body imagery.

Fix applied per web-design-package.md:
- Email imagery alt-text slots table added in the accessibility notes section.
- Email header image (abstract brand art, all 5 emails): alt="" (decorative, explicitly
  specified).
- Any field-icon or meaning-carrying image in email body: descriptive alt in the email
  language (Arabic for AR variant, English for EN).
- Instructor photography if confirmed: descriptive alt in the email language.

Result: PASS at spec level.

**Email Fix 3: contrast-aa, email CTA button**

Prior state: if the email template used #F5F5F5 on #009975, the same 3.30:1 fail applied.

Fix applied per web-design-package.md (email render spec, CTA button section):
- Email CTA button specified: background color-accent (#009975), label color-text-on-accent
  (#141414). "Near-black on emerald yields approximately 5.7:1, passing AA for normal text."
- The fix is explicitly required to be consistent with the landing page CTA treatment.

Recomputed ratio: 5.10:1 (same pairing as the landing page CTA; see summary above).
Threshold: 4.5:1 for normal text.
Result: PASS at spec level. Final verification at rendered template.

**Email Fix 4: target-size, email CTA tap target**

Prior state: no minimum button dimensions specified for the email template.

Fix applied per web-design-package.md (email render spec, CTA button section):
- Minimum 44 px height, 120 px width specified.
- Padding must be applied on the anchor or button element directly (not surrounding cell
  or div) to ensure the tap target is genuinely 44 px on mobile email clients.
- Verification at 375 px viewport width on a rendered email screenshot required before
  approving the template.

Result: PASS at spec level. Render-block carried as open item.

**Checks confirmed passing from v1 (no regression)**

- rtl-reading-order: email copy in copy-package.ar.md is MSA, Western numerals throughout.
  No Eastern Arabic-Indic digits. No LTR leakage in copy. RTL structure at build is a
  template responsibility; the copy is direction-clean. No change in this revision. No
  regression.

- control-and-link-labels: all 5 AR email CTAs and all 5 EN email CTAs carry descriptive
  labels. No bare اضغط هنا or "click here." No change in this revision. No regression.

- motion-safe: no motion, autoplay, animation, or video in any email. No flash risk. No
  change. No regression.

- color-independence: email body copy carries meaning through text, not color alone. No
  change. No regression.

**Render-block open item (carried, not a failure)**

```
{
  check:   "spec-only-render-block",
  element: "email template render: all email checks (semantic heading structure, plain-text
            alternative, alt text, CTA contrast at rendered size, CTA tap target at 375 px,
            RTL rendering of the AR email template) require a rendered email template for
            final verification.",
  status:  "open item, not a failure. Send-platform unconfirmed (lifecycle-package open
            item 2). Once platform is confirmed and template is built, resubmit the rendered
            template to accessibility-qa before any send action. Copy-level checks (RTL,
            control labels, Western numerals, no em dash, no tatweel) pass at the
            copy-package level.",
  carried_from: "v1 verdict"
}
```

---

## Gate status summary (v2)

```
page_result:   PASS
email_result:  PASS

addressable_items_resolved: 9 of 9
  page-level: 5 of 5 (CTA contrast, error text contrast, hover border contrast,
              error icon, required field indicator)
  email-level: 4 of 4 (semantic heading structure, text alternatives, CTA contrast,
               tap target) -- email CTA contrast is the same fix as the page CTA,
               counted once per asset

render_block_items_carried: 2 (not failures, must clear before go-live / send)
  1. focus-order-render-check (page): requires rendered interactive page
  2. email-template-render-check: requires rendered email template after
     send-platform confirmation

contrast_ratios_final:
  CTA button (#141414 on #009975):       5.10:1  (threshold 4.5:1 normal text, PASS)
  error text (#F04040 on #1A1A1A):       4.57:1  (threshold 4.5:1 normal text, PASS; margin narrow)
  hover border (#009975 on #1A1A1A):     4.81:1  (threshold 3:1 non-text, PASS)
  error border (#E53935 on #1A1A1A):     4.19:1  (threshold 3:1 non-text, PASS; border only)
  focus ring (#009975 on #1A1A1A):       4.81:1  (threshold 3:1 non-text, PASS)
  body text (#F5F5F5 on #141414):       16.8:1   (threshold 4.5:1 normal text, PASS)
  secondary text (#A8A8A8 on #141414):   4.6:1   (threshold 4.5:1 normal text, PASS)

build_flags:
  - Error text margin is narrow (4.57:1, threshold 4.5:1, margin 0.07:1). Verify the
    rendered font size is exactly 14 px (0.875 rem) weight 400 at build. If the font
    substitution changes effective rendered size, re-check this ratio.
  - CTA contrast spec approximation (5.7:1) is higher than recomputed (5.10:1). Both pass.
    The recomputed value is the operative figure.

routing_on_pass:
  - Both assets advance to brand-qa-reviewer as the next gate, per verification.md gate
    stack (accessibility runs before brand-qa-reviewer on streams 6 and 7).
  - The two render-block open items are surfaced at the human gate and must be resolved
    before go-live (page) and before any send action (email).
  - All other blocking open items (gate-platform-not-confirmed, Saudi PDPL, copy regions
    unbound, instructor naming, price confirmation) remain as surfaced in the
    conversion-package and web-design-package envelopes and are not cleared by this gate.

note_on_gate_stack:
  This gate ran alongside design-qa (design-specs.md present, in flight) and ahead of
  brand-qa-reviewer, per verification.md. On pass, both assets continue through the
  gate stack to brand-qa-reviewer. The human gate is separate and downstream of all
  quality gates. Passing this gate is not approval to send or publish.

note_on_brand_palette:
  All fixes adjust usage only. No brand hex values (#141414, #1A1A1A, #009975) were
  changed. The CTA fix changes the label color from #F5F5F5 to #141414 (not a brand
  constant). The error text fix replaces a functional state color (#E53935) with
  #F04040 (also not a brand constant). The hover border fix removes opacity from the
  existing brand accent. Brand palette is intact.
```

---

## Checks confirmed passing (page, all unchanged from v1 except where noted)

- rtl-reading-order: PASS (confirmed passing at v1; no change in revised spec; no regression)
- text-alternatives: PASS (alt-text slots now fully documented in the revised spec for all
  14 page image regions and all email image regions; confirmed at spec level)
- semantic-structure: PASS (H1, H2, H3, landmark elements, FAQ disclosure pattern, gate
  form with explicit label, gate states with correct ARIA roles; confirmed in revised spec)
- control-and-link-labels: PASS (all CTAs descriptive; no bare click-here; confirmed)
- target-size: PASS (44 px minimum on all targets; CTA and inputs 48 px; confirmed)
- keyboard-and-focus: PASS at spec level (focus ring 4.81:1 non-text on #1A1A1A, passes
  3:1; focus order specified; render-block for verification carried as open item)
- motion-safe: PASS (max 200 ms transitions; prefers-reduced-motion query; no autoplay;
  no flash)
- color-independence: PASS (error state now has icon cue; required field now has asterisk
  and explanatory note; no other color-only state or meaning)

---

Verdict issued (v2): 2026-06-12
Gate: accessibility-qa
Issued by: accessibility-reviewer
Standard: WCAG 2.2 AA
Re-verification of: prior verdict v1 2026-06-12
All addressable fix items: resolved
Render-block open items: 2 (carried, not failures)
