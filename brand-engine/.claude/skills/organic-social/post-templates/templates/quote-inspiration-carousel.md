# Template: Quote inspiration carousel

A high-save carousel built from real, attributed quotes, one per slide, around a theme.
Campaign-agnostic scaffold. Structure only. Captions and quote placement by copywriter-ar (AR
primary) and copywriter-en. Nothing publishes.

- Format: carousel, 4:5 or 1:1. A cover, one quote per slide.
- Bilingual: AR primary. A quote is shown in the language it was given; provide a parallel
  translation slot where useful. Arabic is an overlay slot, never baked into a generated image.
- Visual constants: #141414, #1A1A1A, emerald #009975. The quote reads large and calm, the
  attribution small in emerald.

## Slides

### Slide 1, cover
- Copy slot (AR): [the theme, MSA, for example words to start the year right].
- Copy slot (EN): [the theme].

### Slides 2 to N, one quote per slide
- Quote slot: [the real, attributed quote]. Verbatim. A real quote may stay in the speaker's
  own register even if colloquial, because it is a genuine quote, not invented copy.
- Attribution slot: [INSTRUCTOR or speaker]. Only confirmed-public people. Use a placeholder
  until confirmed. Never attribute an invented quote to a real person.
- Optional visual: a real, rights-cleared image of the speaker, never a generated likeness.

### Optional last slide, soft CTA
- Copy slot (AR): [one line tying the theme back to Maharat]. [CTA if the brief sets one].
- Copy slot (EN): [same].

## Slots to resolve from the brief

- The theme, the real quotes and their [INSTRUCTOR] attributions, the optional CTA.
- Quotes are real and sourced. No invented quotes. No accreditation implication. Only
  confirmed-public people are named or shown.

## Routing and gates

- Quotes and captions to copywriter-ar and copywriter-en. Images to creative-director and the
  designer, real rights-cleared assets only.
- Gate stack: skill eval, arabic-copy-qa, english-copy-qa, design-qa, brand-qa-reviewer, then
  the human gate to publish.
