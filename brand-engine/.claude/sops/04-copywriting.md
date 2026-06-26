# SOP 04: Copywriting

Stream 4. Owners: copywriter-ar (Arabic, the default) and copywriter-en (English, when the
brief calls for it). Mode: reasoning. Writes the customer-facing words: copy variants per
segment and subject lines, and fills the empty copy-overlay slots in the asset briefs. Arabic
is primary; English follows the same plain, empowering tone, never a translation afterthought.

No em dashes, no tatweel, Western numerals, English-first, empowering framing, no
accreditation claims.

---

## Trigger

A campaign with a QA-passed `strategy-artifact` (stream 2), and, where the campaign has
visual assets, a QA-passed `creative-package` (stream 3) whose asset briefs have empty
copy-overlay slots to fill.

## Inputs

- The `strategy-artifact` (stream 2): segments, angle, offer framing, success metric.
- The `creative-package` (stream 3), if visuals exist: asset briefs with empty overlay slots.
- The brief: offer (product, plan, price, promotion), language, channels.
- `context/brand-voice.md` for tone, worked empowering examples, and the mechanical rules.

## Steps

1. Write per segment. For each segment in the strategy-artifact, write copy variants. Each
   variant has an id, the segment it serves, a headline, body, exactly one CTA, and a language
   tag (ar or en). Lead with what the reader can build, never with what they lack.
2. Keep the offer exact. Any price, plan, or promotion comes verbatim from the brief. If a
   price is an ASSUMPTION, write around value and leave the price as a flagged placeholder. Do
   not invent a discount, a offer title, or an subject name.
3. Write subject lines. For email assets, write subject lines per segment and flag the primary
   one. Western numerals, no em dashes, empowering, RTL-safe.
4. Fill the overlay slots. Map each variant to the asset-brief copy slots it fills, by slot
   name (headline, subhead, cta). The text fits the safe areas the designer reserved.
5. Default to Arabic, add English when the brief asks. copywriter-ar owns the Arabic, which is
   primary. copywriter-en writes the English to the same tone where the brief calls for it.
6. Assemble the copy-package and run the gates. Carry forward open items from upstream.

## Output

A `copy-package` (see `runtime/handoff-contract.md`):
- variants[]: each with id, segment, headline, body, one CTA, language (ar or en).
- subject_lines[]: for email assets, with the chosen primary flagged.
- fills: which asset_brief copy slots each variant fills.

This artifact hands off to streams 5, 6, and 7.

## Quality bar

- Every variant traces to a segment and the angle from the strategy-artifact.
- Exactly one CTA per variant. Subject lines have one flagged primary.
- The offer in the copy traces exactly to the brief. No invented price, promotion, title, or
  subject name. No accreditation implication.
- Empowering, never deficit-framed. No em dashes, no tatweel, Western numerals, RTL-safe.
- Gates, in order (see `verification.md`): skill eval, then arabic-copy-qa for Arabic copy or
  english-copy-qa for English copy, then brand-qa. A failure at any gate is a hard stop back
  to the author with exact fixes; it does not advance.

## Example output (shape, not real copy, no invented values)

```
copy-package:
  variants:
    - id: variant-ar-lapsed-01
      segment: lapsed-engaged
      language: ar
      headline: "[empowering headline tied to the angle]"
      body: "[short, concrete, confident; offer detail only from the brief]"
      cta: "[one clear CTA]"
    - id: variant-en-lapsed-01
      segment: lapsed-engaged
      language: en
      headline: "[same spirit, plain and empowering]"
      body: "[one CTA, no em dash, Western numerals]"
      cta: "[one clear CTA]"
  subject_lines:
    - id: subj-ar-01   language: ar   primary: true   text: "[subject]"
    - id: subj-ar-02   language: ar   primary: false  text: "[subject]"
  fills:
    - variant: variant-ar-lapsed-01  asset_brief: "[brief id]"  slots: { headline, cta }
  open_items: [price ASSUMPTION pending before any send]
```

## Review owner

copywriter-ar owns the Arabic copy-package; copywriter-en owns the English variants. The copy
advances only after skill eval, the matching language QA, and brand-qa all pass. No invented
offer detail, title, or an unverified claim enters any variant.

No em dashes, no invented values. A missing variable is a stop-and-ask, not a guess.
