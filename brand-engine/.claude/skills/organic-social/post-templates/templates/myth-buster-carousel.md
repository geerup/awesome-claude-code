# Template: Myth-buster carousel

A carousel that names common myths in a topic and replaces each with the truth. Builds
authority and saves. Campaign-agnostic scaffold. Structure only. Captions by copywriter-ar (AR
primary) and copywriter-en. Nothing publishes.

- Format: carousel, 4:5 or 1:1. A cover, 3 to 5 myth-and-truth slides, a closer.
- Bilingual: AR primary, EN parallel. Arabic is an overlay slot, never baked in.
- Visual constants: #141414, #1A1A1A, emerald #009975. The myth reads muted, the truth reads
  in emerald, so the eye lands on the correction.

## Slides

### Slide 1, cover
- Copy slot (AR): [topic] myths that are costing you [the cost], MSA.
- Copy slot (EN): [topic] myths that are costing you [the cost].

### Slides 2 to N, myth and truth (one per slide)
- Top, the myth: [the common false belief, in quotes], read muted.
- Bottom, the truth: [the correction, one or two confident lines], read in emerald.
- Copy slot (AR) and (EN) for each. Keep each slide to one myth.

### Slide N+1, closer and CTA
- Pattern: now you know how [topic] actually works.
- Copy slot (AR): [closer line, MSA]. [CTA, for example watch on Maharat, or a [KEYWORD]
  lead-gen if the brief sets one].
- Copy slot (EN): [closer line]. [CTA].

## Slots to resolve from the brief

- [topic], the specific myths and truths, the cost, the CTA and any [KEYWORD].
- Truths must be accurate and non-deceptive. No invented claim, no accreditation implication.

## Routing and gates

- Copy to copywriter-ar and copywriter-en. Visuals to creative-director and the designer.
- Gate stack: skill eval, arabic-copy-qa, english-copy-qa, design-qa, brand-qa-reviewer, then
  the human gate to publish. Add compliance-privacy-check if a lead-gen CTA is used.
