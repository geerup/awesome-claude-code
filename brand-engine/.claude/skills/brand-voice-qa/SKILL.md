---
name: brand-voice-qa
description: The Maharat brand-voice copy gate. Use to check Arabic copy against the documented Maharat brand voice, triggers on "brand voice QA," "is this the active brand voice," "check the copy against the brand voice." Verifies empowering-not-deficit voice, positioning and mission alignment, the brand lexicon, the instructor and product framing, gendered reader address, and the guardrails, returning pass or a structured fix list. It runs after arabic-copy-qa and complements brand-qa-reviewer.
---

# Brand Voice QA (the Maharat brand-voice gate)

The brand-voice quality gate, used by `brand-voice-reviewer` (and available to any agent reviewing
Arabic copy). It checks copy against the evidence-based Maharat brand voice documented in
`references/2026-06-maharat-ar-copy/02-brand-voice-and-tone-manual.md`, drawn from the live site. A
verifier, not an author: it never edits the copy, it returns pass, or fail with an exact fix list.

## Purpose

Catch voice defects the language gate and the general brand gate are not built to catch: copy that is
mechanically clean but does not sound like Maharat. It checks the specific ways the brand speaks about
itself, its instructors, and its product, and the lexicon and address that make the voice recognizable.

## When to use

- Any Arabic customer-facing asset, after `arabic-copy-qa` (language and mechanics) passes, before or
  alongside `brand-qa-reviewer` (the general brand and guardrail gate).

## Inputs

- The Arabic copy under review, in context.
- `context/brand-voice.md` and `references/2026-06-maharat-ar-copy/` (the manual and the live corpus).

## The checks

Run each. Report every failing span, not just the first.

1. voice-alignment: empowering and never deficit-framed, Thmanyah tone, modern and confident, not
   stiff and not hype. Beauty and skill are confidence and self-expression, never correction.
2. positioning-and-mission: nothing contradicts the positioning and mission (نخبة العرب, منبر للعرب
   من قبل العرب, تثقيف وترفيه وإلهام, التعلّم ملهمًا لا مرهقًا).
3. lexicon: reaches for the brand's signature vocabulary where natural, carries no off-brand, deficit,
   or hype words, and uses modern loanwords only where the domain expects them.
4. instructor-framing: instructor mentions use the "[name] يعلّم/تعلّم [topic]" pattern, anchor
   authority to a concrete proof, name no private clients or brand-line specifics, and name an
   instructor only when confirmed.
5. product-framing: correct taxonomy (صفوف and قوائم مهارات), the certificate framed as a personal
   completion certificate and never accredited, value-led price shown only where the brief provides it,
   and no invented offer, title, or lineup.
6. address-and-register: reader address is gendered to the audience (feminine for beauty and style,
   masculine or plural elsewhere) and the person and number are consistent within the asset.
7. guardrails: no accreditation implication, no roadmap, fundraising, or unannounced plans.

## Steps

1. Read the copy in context against the seven checks.
2. For each failing check, capture the offending span, quoted exactly.
3. Decide the result: pass only when every check passes, otherwise fail.
4. Return the result in the shape below. Never edit the copy.

## Output

- Pass: the copy advances to `brand-qa-reviewer`.
- Fail: a structured fix list, one item per failure:

```
{ check: <the failing check id>, span: "<the offending span, quoted>", fix: "<the required change>" }
```

See `templates/brand-voice-qa-fix-list.md`.

## Hard rules

- Never edit the copy. Verify and route only.
- Binary: pass and advance, or fail and return. No soft warnings that pass through.
- No item is waved through. The author regenerates against the full list and resubmits here.
- Passing this gate is not passing brand QA. `brand-qa-reviewer` still runs last.

## How it connects

- Runs after `arabic-copy-qa` and before or alongside `brand-qa-reviewer`, per
  `runtime/verification.md`. On pass, the copy advances to brand QA. On fail, it returns to
  `brand-copywriter-ar` or `copywriter-ar` with the fix list.
