---
name: arabic-copy-qa
description: The Arabic copy quality gate. Use to check any Arabic customer-facing copy before brand QA, triggers on "arabic QA," "check the arabic," "is this arabic on brand," "review the arabic copy." Verifies MSA with Gulf-familiar wording, Thmanyah tone, no tatweel or kashida, Western numerals, no em dashes, empowering not deficit-framed, and RTL-safe, returning pass or a structured fix list.
---

# Arabic copy QA (the Arabic gate, before brand QA)

The Arabic-specific quality gate. Runs only on Arabic copy, and runs after the skill eval and
before `brand-qa-reviewer` in the gate stack (see `runtime/verification.md`). A verifier, not
an author: it never edits the copy, it returns pass, or fail with an exact fix list. The
author regenerates against the list and resubmits to this same gate.

## Purpose

Catch Arabic-specific defects the skill eval and brand QA are not built to catch: dialect
drift, stiff or off-tone phrasing, tatweel, Eastern numerals, broken RTL. It is the reason
Arabic copy reaches brand QA already clean of mechanical and tone faults.

## When to use

- Any customer-facing asset that contains Arabic copy: ad copy, email copy, subject lines,
  landing page copy, lifecycle flow copy.
- Always after the asset passes its skill eval, always before `brand-qa-reviewer`.

## Inputs

- The Arabic copy under review (the spans, in context).
- `context/brand-voice.md`: the voice, the tone benchmark, the hard mechanical rules.

## The checks

Run each. Stop reporting nothing; report every failing span.

1. msa-gulf-familiar: Modern Standard Arabic with Gulf-familiar wording. Not heavy dialect,
   not stiff formal Arabic.
2. thmanyah-tone: clear, modern, intelligent, never stiff. Respects the reader.
3. no-tatweel: no tatweel or kashida (U+0640) anywhere.
4. western-numerals: digits are 0 to 9 only, never Eastern Arabic numerals.
5. no-em-dash: no em dash (U+2014) anywhere. Comma, colon, or period instead.
6. empowering-framing: speaks to what the reader can build, never deficit-framed, no shame,
   no hype.
7. rtl-safe: renders right-to-left correctly; mixed Arabic, English, or numerals do not break
   direction.

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

Example: `{ check: "no-em-dash", span: "سريع وذكي [شرطة طويلة] وملكك", fix: "استبدل الشرطة الطويلة بفاصلة أو نقطة" }`. Quote the span verbatim from the copy under review; here the banned glyph is named in brackets so this file stays clean.

See `templates/arabic-qa-fix-list.md`.

## Hard rules

- Never edit the copy. Verify and route only.
- Binary: pass and advance, or fail and return. No soft warnings that pass through.
- No item is waved through. The author regenerates against the full list and resubmits here.
- Passing this gate is not passing brand QA. `brand-qa-reviewer` still runs last.

## How it connects

- Runs in the gate stack between the skill eval and `brand-qa-reviewer`, per
  `runtime/verification.md`.
- On pass, the asset advances to brand QA. On fail, it returns to the authoring agent
  (copywriter-ar, conversion-engineer, or lifecycle-architect) with the fix list.
- Wraps the Arabic copy in artifacts across streams 4, 6, and 7; the artifact qa block records
  arabic_qa as pass or fail per `runtime/handoff-contract.md`.
