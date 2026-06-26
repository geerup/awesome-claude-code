# SOP: App store optimization (ASO)

ASO stream. Owner: aso-specialist. Mode: reasoning for the plan, execution (gated) for any
store change. Grows organic installs on the App Store and Google Play across Arabic and
English: the store listing, the store creatives, and the listing experiments. It assembles
an approval-ready `aso-package` and stops. Publishing a store change is a gated action.

English-first, RTL-correct, no em dashes, no tatweel, Western numerals, no accreditation claims.

---

## Trigger

A brief with app growth or organic installs in scope, or a channel_plan that includes ASO.

## Inputs

- The `strategy-artifact` (stream 2): the angle, segments, offer framing, channel_plan.
- The brief: the app and stores in scope, the markets (GCC, primary Saudi Arabia), the
  languages (Arabic and English), the window. If a store, market, or language is not in the
  brief, stop and ask.
- Store keyword and competitor data from the store consoles and research tools.
- Listing copy is written by `copywriter-ar` (English-first) and the English copywriter,
  referenced by variant id, never written here. Store creatives come from `creative-director`
  and the designer.

## Steps

1. Research store keywords and competitors per store and per language. Map search intent to
   the listing fields. Arabic and English are localized in parallel, not translated as an
   afterthought.
2. Optimize the store listing fields: title, subtitle, description, and the keyword field, per
   store (App Store and Google Play) and per language. Each field draws on the keyword and
   intent map; nothing claims an offer, price, or feature not confirmed in the brief or context.
3. Route the listing copy to `copywriter-ar` and the English copywriter. Reference QA-passed
   variants by id. Run copy QA then brand QA before the field is package-ready.
4. Plan the store creatives: screenshots, the preview video, and the icon, per store spec.
   Visual constants #141414, #1A1A1A, emerald #009975. RTL-correct, Western numerals in any
   rendered text, no Arabic baked into a generated image. The designer runs design-qa.
5. Plan the listing experiments: the store A/B tests (creatives, copy fields), the hypothesis,
   the metric, and the read window. Tie the metric to the strategy success_metric.
6. Set the reviews and ratings response policy: on-brand, empowering replies, no accreditation
   claim, no offer not confirmed, escalation for sensitive or compliance-touching reviews.
7. Assemble the `aso-package` and stop at the human gate. Publishing a store change is a gated
   action; nothing publishes to a live store listing without sign-off.

## Output

An `aso-package` (wrapped in the common envelope, per `runtime/handoff-contract.md`):
- store_listing: title, subtitle, description, keyword field, per store and per language, each
  referencing a QA-passed copy variant by id.
- store_creatives: screenshots, preview video, icon, per store spec, design-qa passed.
- experiments: the store A/B tests, hypotheses, metrics, and read windows.
- reviews_policy: the on-brand response and escalation policy.
- publish_on_approval: one plain sentence of what publishing the store change does.
- open_items: store-access not confirmed, market or language not set, creative not delivered.

## Quality bar

- Listing copy is QA-passed (skill eval, arabic-copy-qa for Arabic, english-copy-qa for
  English, then brand-qa-reviewer, per `runtime/verification.md`). RTL renders correctly.
- Store creatives pass design-qa: visual constants, RTL, Western numerals, no baked Arabic,
  store-spec dimensions and safe areas, premium and uncluttered.
- Every keyword, field, and creative traces to the brief and the keyword map. No invented
  offer, price, Skill Path title, content lineup, or instructor name.
- No accreditation implication in any listing field, creative, or review reply.
- The store-access open item is surfaced; a store publish is blocked until access is confirmed
  and the human gate clears.

## Example output (shape, not real values)

```
store_listing:
  app_store: { ar: {title_ref, subtitle_ref, description_ref, keyword_field_ref},
               en: {...} }
  google_play: { ar: {...}, en: {...} }
experiments:
  - { surface: screenshots, hypothesis, metric (ties to success_metric), read_window }
reviews_policy: on-brand replies, escalation for compliance-touching reviews
publish_on_approval: "Publishes the updated AR and EN listings to the stores in scope."
open_items: store-access-to-confirm, creative-delivery-pending
```

## Review owner

Ahmed, at the human gate. Approval is per store change. The aso-specialist publishes a store
change only after the gate clears, and only what was approved. Silence is not approval.

House rule: facts come from `context/`, variables come from the active brief. When both are
silent on something needed, stop and ask. Do not invent a value.
