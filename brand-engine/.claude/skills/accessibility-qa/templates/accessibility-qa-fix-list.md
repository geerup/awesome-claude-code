# Accessibility QA fix list template

The result this gate returns. Pass advances the asset to brand-qa-reviewer (alongside
compliance-privacy-check where data is collected), then the human gate. Fail returns the list
below to the author (conversion-engineer for pages, lifecycle-architect for emails, designer for
the visual), who regenerates against every item and resubmits to this same gate. This gate never
edits the asset. All example items are illustrative only.

## Result header

```
asset:      <the page or email under review>     # e.g. nonpayer-landing-v1
gate:       accessibility-qa
result:     pass | fail
checked:    contrast-aa, rtl-reading-order, text-alternatives, semantic-structure, control-and-link-labels, target-size, keyboard-and-focus, color-independence, motion-safe
```

## On pass

```
result: pass
note:   advances to brand-qa-reviewer (and compliance-privacy-check if data is collected), then the human gate
```

## On fail: one item per failing check

```
{ check: <check id>, element: "<offending element, named exactly>", fix: "<required change>" }
```

## Illustrative fix items (replace with the real findings)

Name the real offending element. In these illustrations the banned glyph and Eastern numerals
are named in brackets, so this template file itself stays clean.

```
{ check: "contrast-aa",            element: "plan benefit paragraph, #009975 on #1A1A1A",   fix: "set the paragraph to #FFFFFF, keep emerald for the heading and the CTA" }
{ check: "rtl-reading-order",      element: "hero block reads left-to-right on the Arabic page", fix: "mirror the layout and set right-to-left reading order" }
{ check: "text-alternatives",      element: "instructor photo has no alt-text slot",          fix: "add an alt-text slot for copywriter-ar to fill, mark purely decorative images decorative" }
{ check: "semantic-structure",     element: "email body is a single image, no text version",  fix: "rebuild with semantic text and a plain-text alternative" }
{ check: "control-and-link-labels", element: "CTA labeled [click here]",                       fix: "label the control with its action, for example ابدأ الآن" }
{ check: "target-size",            element: "two links 6px apart in the footer",              fix: "increase target size and spacing for reliable tapping" }
{ check: "keyboard-and-focus",     element: "signup field reachable only by mouse",           fix: "make it keyboard-focusable with a visible focus state" }
{ check: "color-independence",     element: "required field marked by red border only",       fix: "add a text or icon cue in addition to color" }
{ check: "motion-safe",            element: "hero video autoplays with no pause",             fix: "add a pause control and respect reduced-motion" }
```

## Checklist for the verifier

- Every failing check has its own item, with the element named exactly.
- The fix names the required change in usage, it never weakens the brand palette.
- A spec-only review blocks on the render-dependent checks (measured contrast, focus order).
- Result is binary: pass only when all checks pass, otherwise fail.
- No em dash, no tatweel, Western numerals only, in this file itself.
