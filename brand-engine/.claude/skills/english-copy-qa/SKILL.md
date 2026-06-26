---
name: english-copy-qa
description: The English copy quality gate. Use to check any English customer-facing copy before brand QA, triggers on "english QA," "check the english," "is this english on brand," "review the english copy." Verifies plain confident empowering tone (never deficit-framed), no em dashes, Western numerals, one clear CTA where applicable, no accreditation implication, and no invented offers or titles, returning pass or a structured fix list.
---

# English copy QA (the English gate, before brand QA)

The English-specific quality gate, parallel to `arabic-copy-qa`. Runs only on English copy,
after the skill eval and before `brand-qa-reviewer` in the gate stack (see
`runtime/verification.md`). A verifier, not an author: it never edits the copy, it returns
pass, or fail with an exact fix list. The author regenerates against the list and resubmits
to this same gate.

## Purpose

Catch English-specific defects the skill eval and brand QA are not built to catch in one
pass: deficit framing, hype, the em dash glyph, Eastern numerals, missing or competing CTAs,
language that implies accreditation, and invented offers or titles. It is the reason English
copy reaches brand QA already clean of mechanical and tone faults. The English follows the
same plain, empowering spirit as the Arabic; it is not a translation afterthought.

## When to use

- Any customer-facing asset that contains English copy: ad copy, email copy, subject lines,
  landing page copy, lifecycle flow copy.
- Always after the asset passes its skill eval, always before `brand-qa-reviewer`.

## Inputs

- The English copy under review (the spans, in context).
- `context/brand-voice.md`: the voice, the tone benchmark, the hard mechanical rules.
- The active brief and `context/` for any offer, title, or price the copy references, so a
  reference can be checked against a confirmed source rather than assumed.

## The checks

Run each. Report every failing span, not just the first.

1. empowering-tone: plain, confident, empowering. Speaks to what the reader can become, never
   deficit-framed, no shame, no hype words.
2. no-em-dash: no em dash glyph anywhere. Use a comma, colon, or period instead.
3. western-numerals: digits are 0 to 9 only, never Eastern Arabic numerals in English copy.
4. one-clear-cta: where a CTA applies, exactly one clear primary call to action, not zero and
   not competing CTAs. Marked not-applicable for copy with no action (for example a pure
   headline test).
5. no-accreditation-implication: never says or implies certificates are accredited. Maharat
   issues completion certificates, not accredited ones.
6. no-invented-offers-titles: no Skill Path title, content lineup item, instructor name,
   price, or offer that is not confirmed in the brief or `context/`. If one is needed and not
   confirmed, that is a fail, not a guess.
7. plain-active-voice: short sentences, concrete nouns, active voice. Flags stiff, corporate,
   or over-explained phrasing that breaks the Thmanyah-equivalent tone.

## Steps

1. Read the copy in context against the seven checks.
2. For each failing check, capture the offending span, quoted exactly.
3. Decide the result: pass only when every applicable check passes, otherwise fail.
4. Return the result in the shape below. Never edit the copy.

## Output

- Pass: the copy advances to `brand-qa-reviewer`.
- Fail: a structured fix list, one item per failure:

```
{ check: <the failing check id>, span: "<the offending span, quoted>", fix: "<the required change>" }
```

Example: `{ check: "no-em-dash", span: "fast, intelligent [em dash] and yours", fix: "replace the em dash with a comma or a period" }`. Quote the span verbatim from the copy under review; here the banned glyph is named in brackets so this file stays clean.

See `templates/english-qa-fix-list.md`.

## Hard rules

- Never edit the copy. Verify and route only.
- Binary: pass and advance, or fail and return. No soft warnings that pass through.
- No item is waved through. The author regenerates against the full list and resubmits here.
- Passing this gate is not passing brand QA. `brand-qa-reviewer` still runs last.

## How it connects

- Runs in the gate stack between the skill eval and `brand-qa-reviewer`, per
  `runtime/verification.md`, as the English-language counterpart to `arabic-copy-qa`.
- On pass, the asset advances to brand QA. On fail, it returns to the authoring agent with
  the fix list.
- Wraps the English copy in artifacts across streams 4, 6, and 7; the artifact qa block
  records the copy QA result per `runtime/handoff-contract.md`.
