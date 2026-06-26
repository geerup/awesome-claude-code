# Design QA fix list template

The result this gate returns. Pass advances the asset to brand-qa-reviewer, then to the human
design check. Fail returns the list below to the designer agent, who regenerates against every
item and resubmits to this same gate. This gate never edits the asset. All example items are
illustrative only.

## Result header

```
asset:      <the asset or concept id under review>     # e.g. concept-nonpayer-ig-story-v1
gate:       design-qa
result:     pass | fail
checked:    rtl-correct, visual-constants, western-numerals-rendered, no-baked-arabic-text, safe-areas-dimensions, premium-uncluttered
```

## On pass

```
result: pass
note:   advances to brand-qa-reviewer, then the human design check (final manual step)
```

## On fail: one item per failing check

```
{ check: <check id>, span: "<offending element, quoted or described exactly>", fix: "<required change>" }
```

## Illustrative fix items (replace with the real findings)

Quote or describe the real offending element. In these illustrations the banned glyph and
Eastern numerals are named in brackets, so this template file itself stays clean.

```
{ check: "rtl-correct",              span: "Arabic headline left-aligned, reads left-to-right", fix: "Set right-to-left alignment and reading order for the Arabic layout" }
{ check: "visual-constants",         span: "background #222222, accent floods the frame",       fix: "Use near-black #141414, surfaces #1A1A1A, emerald #009975 as a highlight not a flood" }
{ check: "western-numerals-rendered", span: "price shown in [eastern arabic numerals]",          fix: "Use Western numerals: 12 months" }
{ check: "no-baked-arabic-text",     span: "headline baked into the generated image",           fix: "Remove the baked text, leave the copy-overlay slot empty for copywriter-ar" }
{ check: "safe-areas-dimensions",    span: "logo clipped by the 9:16 story crop",               fix: "Declare the safe area and move critical content inside it" }
{ check: "premium-uncluttered",      span: "three competing focal points, crowded layout",       fix: "Establish one clear focal point and add generous space" }
```

## Checklist for the verifier

- Every failing check has its own item, with the element quoted or described exactly.
- The fix names the required change, it does not redesign the whole asset.
- A human design check remains the final manual step after a pass.
- Result is binary: pass only when all checks pass, otherwise fail.
- No em dash, Western numerals only, in this file itself.
