# Web design QA fix list

The output of `web-design-qa`. A binary verdict on a web or landing-page `design_spec`. Pass
only when every check passes. On fail, one item per failing check. Never edit the spec, verify
and route only.

## Verdict

```
skill        web-design-qa
target       <the design_spec under review>
result       pass | fail
```

## On pass

The spec advances to `brand-qa-reviewer`, then to `conversion-engineer` and the human design
check. No fix list.

## On fail

One item per failing check:

```
{ check: <check id>, span: "<the offending element, quoted or described>", fix: "<the required change>" }
```

Check ids: responsive-rtl, visual-constants, western-numerals-rendered, no-baked-arabic-text,
responsive-breakpoints, interaction-states, accessibility, performance-budget,
one-primary-action, premium-uncluttered, human-check-preserved, result-is-binary.

Example items:

```
{ check: "responsive-rtl", span: "hero reverts to ltr at the md breakpoint", fix: "set direction rtl at every breakpoint, keep Arabic reading order top-right" }
{ check: "interaction-states", span: "primary action has no focus or disabled state", fix: "specify focus, active, disabled, loading, and error states for the primary action" }
{ check: "one-primary-action", span: "two emerald CTAs in the hero", fix: "keep one primary action, demote the second to a secondary style" }
```

## Hard rules

- Binary: pass and advance, or fail and return. No soft warnings.
- No item is waved through. The web-designer fixes against the full list and resubmits here.
- A human design check stays the final manual step on any Arabic surface.
