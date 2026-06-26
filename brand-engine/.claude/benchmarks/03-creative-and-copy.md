# Benchmark: creative and copywriting

An external benchmark of the Maharat engine's creative and copywriting skills against
authoritative, real-world frameworks. It maps what best-in-class practice asks for, where
our skills already meet or exceed that bar, where the gaps are, and the specific edits worth
making. It is a reference document. It changes no skill file. Every recommendation is a
proposal that goes through the normal review gate.

Scope: stream 3 creative (creative-concepting, image-prompting) and stream 4 copywriting
(ad-copy, email-copy, subject-lines), plus the handoff contract that binds copy to creative.

## Sources reviewed (web)

Creative brief structure
- [Adobe: Creative briefs, how to write, examples, templates](https://business.adobe.com/blog/basics/creative-brief)
- [Shopify: Creative brief components and best practices (2025)](https://www.shopify.com/blog/creative-brief)
- [Asana: Creative briefs, what to include, template (2026)](https://asana.com/resources/how-write-creative-brief-examples-template)

Ad copy frameworks (AIDA, PAS, the 4 Us, 4 Cs)
- [Reads to Leads: From AIDA to PAS, 5 copywriting formulas that work](https://www.readstoleads.com/blog-article/best-copywriting-formulas)
- [Crazy Egg: AIDA vs PAS, which formula to use and why](https://www.crazyegg.com/blog/aida-vs-pas/)
- [Anyword: The 4 Us, a foolproof formula (Useful, Urgent, Unique, Ultra-specific)](https://www.anyword.com/blog/4us-copywriting-formula)
- [Copywriter Collective: The 4 Us checklist for headlines](https://copywritercollective.com/the-4-us-use-this-checklist-for-writing-powerful-headlines/)

Email body copy and CTA
- [CleverTap: Email copywriting best practices, tips, examples](https://clevertap.com/blog/email-copywriting/)
- [HubSpot: How to write a marketing email, 28 tips](https://blog.hubspot.com/blog/tabid/6307/bid/32606/the-9-must-have-components-of-compelling-email-copy.aspx)
- [Moosend: Email CTAs, best practices and examples (2025)](https://moosend.com/blog/email-cta/)

Email subject lines, length, mobile
- [Twilio: Ideal email subject line length in 2025](https://www.twilio.com/en-us/blog/ideal-email-subject-length)
- [Mailchimp: Best practices for email subject lines](https://mailchimp.com/help/best-practices-for-email-subject-lines/)
- [Attentive: What we learned analyzing billions of subject lines](https://www.attentive.com/blog/email-subject-line-best-practices)

AI image prompt structure (composition, lighting, negative prompts)
- [Let's Enhance: How to write AI image prompts like a pro (2026)](https://letsenhance.io/blog/article/ai-text-prompt-guide/)
- [LTX: AI image prompting guide with examples](https://ltx.io/blog/ai-image-prompt-guide)
- [OpenAI cookbook: GPT image generation models prompting guide](https://developers.openai.com/cookbook/examples/multimodal/image-gen-models-prompting-guide)

## Best-in-class elements

What the sources converge on, by area.

Creative brief structure
- A tight, named set of fields: objective, background and context, target audience, the single
  core message, tone and brand guidelines, deliverables and specs, channels, mandatories and
  constraints, and a measurable success metric. Adobe, Shopify, and Asana all carry roughly
  this spine.
- One core message, not many. The brief forces a single-minded proposition the work expresses.
- Objectives written as measurable outcomes (SMART), so the brief ties to a result, not a vibe.
- Concision with room to create. The best briefs are short and unambiguous on the constraints
  while leaving the execution open.
- Visual references and mood boards. Words miss visual nuance, so reference imagery bridges
  strategy and execution.
- A named owner and approver, and early stakeholder alignment, to prevent rework.

Ad copy frameworks
- AIDA (Attention, Interest, Desire, Action): the awareness-to-action spine for cold or
  top-of-funnel placements.
- PAS (Problem, Agitate, Solution): strong for pain-aware audiences, fast and direct.
- The 4 Us (Useful, Urgent, Unique, Ultra-specific): a headline and subject-line quality
  checklist, with Useful ranked first, then Urgent, Unique, Ultra-specific.
- The 4 Cs (Clear, Concise, Compelling, Credible): a final pass on any line.
- One ad, one CTA, one idea. Variants should be real alternatives that isolate one variable,
  not padding.

Email body copy and CTA
- One email, one job, one CTA. A single focused CTA can lift click-through sharply versus a
  multi-CTA email (Campaign Monitor, cited by the sources, reports a large lift).
- Scannable structure: short sentences, line breaks, the CTA on its own line, generous margins,
  no wall of text. Built for skimming.
- Conversational second person that respects the reader; some tests show first-person CTA
  phrasing ("Start my path") can outperform second person.
- Personalization by behavior and lifecycle stage, not just a first name. Relevance over
  flattery.
- Subject and body and CTA drafted together so the body keeps the promise the subject makes.

Subject lines, length, mobile
- Short. Roughly 30 to 40 characters or 6 to 9 words is the common target; the shortest lines
  (2 to 4 words) often top open rate.
- Mobile-first. About 80 percent of opens are on mobile, where iPhone shows roughly 33 to 35
  characters. Front-load the message in the first few words.
- Preheader text as earned extra space, set deliberately, not left to spill body text.
- Clarity over clickbait. Overpromising costs trust and hurts long-term engagement.
- Test several real alternatives and let program data set the house length.

AI image prompt structure
- A logical order: subject first, then medium and style, then composition, then lighting, then
  color, then technical or extra detail. Density over length, roughly 15 to 50 words, every
  word earning its place.
- Explicit composition. State framing and viewpoint (close-up, wide, top-down), angle
  (eye-level, low-angle), and layout (asymmetric, negative space on one side) so the model does
  not default to a centered, generic frame.
- Deliberate lighting. Named lighting (soft diffuse, golden hour, high-contrast) changes the
  whole look and should be chosen, not left to chance.
- Negative prompts to exclude the unwanted (text, watermark, distortion), with the caveat that
  negatives are soft weights, not hard guarantees, so prefer a positive instruction where one
  exists.

## Our coverage

Where our skills already meet the bar, with the file that carries it.

Creative brief and concepting
- `skills/03-creative-production/creative-concepting/SKILL.md` and its template
  `.../creative-concepting/templates/creative-concept-brief.md` carry a real concept-brief
  spine: each concept has an id, the strategy angle it serves, the segment, a visual
  description, a one-line rationale tied to the angle, and a channel routing. This is the
  single-core-message and named-fields discipline the brief sources ask for, expressed per
  concept.
- The 2 to 4 concepts per angle rule (`creative-concepting/SKILL.md`) matches the
  best-practice on giving review a real choice without flooding it. It maps to the "real
  alternatives, not padding" point.
- Channel routing per concept (paid, lifecycle, organic) matches the channels field, and the
  tie to the strategy `channel_plan` enforces it.
- The objective and success metric live upstream in the `strategy-artifact`
  (`runtime/handoff-contract.md`), so concepting consumes a measurable objective rather than
  restating one. The brief spine is split across the strategy-artifact and the concept brief
  by design.

Image prompting
- `skills/03-creative-production/image-prompting/SKILL.md` and
  `.../image-prompting/templates/image-prompt-sheet.md` already name the core prompt elements:
  subject, mood, light, composition, and the brand visual constants. This matches the
  subject-then-style-then-light ordering the prompt sources recommend.
- Negative instruction is built in: "no text, no lettering, no Arabic script, no watermark"
  (`image-prompting/SKILL.md` step 4 and the template `negative:` line). This matches the
  negative-prompt practice and is sharpened for our Arabic constraint.
- Dimensions, safe areas, and per-placement specs (feed and story) are mandatory in the
  template, which matches the deliverables-and-specs field of a brief.
- Empty, named copy-overlay slots (headline, subhead, CTA) bound to copy-package variant ids
  is a clean separation the generic guides do not even cover.

Ad copy
- `skills/04-copywriting/ad-copy/SKILL.md` enforces one headline, a short body, exactly one
  CTA per variant, and at least two variants per segment. This is the one-ad-one-CTA and
  real-alternatives discipline, and the variant rule directly supports A/B isolation.
- The headline step ("short, concrete, empowering, speak to what the reader can build") and
  body step ("active voice, concrete nouns") map to the 4 Cs (Clear, Concise, Compelling) and
  to the Useful and Unique of the 4 Us, in our own voice.
- `fills` maps each variant to a real asset-brief slot, closing the copy-to-creative loop.

Email copy
- `skills/04-copywriting/email-copy/SKILL.md` anchors each email to one job and exactly one
  CTA, with a two-to-four-line scannable body and no competing buttons. This is the
  one-email-one-CTA and scannability best practice, near verbatim.
- "Open with a line that respects the reader, no hype, no shame" matches conversational,
  reader-respecting tone, and the empowering rule keeps it relevant rather than flattering.
- The email is built to drop into the lifecycle flow (stream 7) and pairs with a subject set,
  which matches drafting subject, body, and CTA together.

Subject lines
- `skills/04-copywriting/subject-lines/SKILL.md` holds a length and clarity bar ("roughly 40
  characters or fewer where the angle allows"), three to five real options, exactly one primary
  flagged, no clickbait, and "true to the body." This matches the short-length, test-several,
  clarity-over-clickbait, keep-the-promise practice.

Cross-cutting
- One clear CTA is enforced in both ad-copy and email-copy. The single-CTA finding is one of
  the most robust in the sources, and we already hold it as a hard rule.
- The gate stack (skill eval, then `arabic-copy-qa` or `english-copy-qa`, then
  `brand-qa-reviewer`, with `design-qa` on visuals) is a verification layer most external
  guides only gesture at.

## Gaps and missing elements (prioritized)

P1, worth addressing
- No named copy framework vocabulary. None of ad-copy, email-copy, or subject-lines references
  AIDA, PAS, the 4 Us, or the 4 Cs. The skills describe good outcomes (short, concrete, one
  CTA) but give the writer no shared structure to reach for or to test against. Adding the 4 Us
  as a headline and subject checklist, and naming PAS and AIDA as optional structures matched to
  funnel stage, would raise the floor without constraining the voice. Sources: Anyword and
  Copywriter Collective (4 Us), Reads to Leads and Crazy Egg (AIDA, PAS).
- Subject-line length bar is single-pointed and not mobile-justified. Our bar says "roughly 40
  characters or fewer." The current data centers on 30 to 40 characters with mobile truncation
  near 33 to 35 characters on iPhone, and recommends front-loading the message in the first few
  words. Our skill does not mention mobile truncation or front-loading. Sources: Twilio,
  Attentive, Mailchimp.
- No preheader or inbox-preview text field. The subject-lines skill mentions surviving the
  inbox preview but neither it nor email-copy defines a preheader as a deliberate, separate
  field. Best practice treats the preheader as earned extra space set on purpose. Sources:
  Twilio, Mailchimp.

P2, useful
- Composition and lighting are named but not menued. image-prompting says "name subject, mood,
  light, composition" but offers no vocabulary (framing, viewpoint, angle, asymmetry, negative
  space, named lighting). The prompt sources stress explicit composition to avoid a default
  centered frame. A short controlled vocabulary in the template would lift prompt quality.
  Sources: Let's Enhance, LTX, OpenAI cookbook.
- No prompt length or density guidance. Sources converge on roughly 15 to 50 dense words. Our
  template gives no target, so prompts may drift long and unfocused.
- No CTA-phrasing guidance. The single-CTA rule is firm, but neither ad-copy nor email-copy
  notes the first-person versus second-person finding, or that the CTA should sit on its own
  line. Minor, but cheap to add. Sources: Moosend, HubSpot.
- No explicit mood-board or visual-reference hook in concepting. Brief sources weight reference
  imagery heavily. Our concept brief is text-only direction. A reference-link field (or a note
  that references attach to the concept) would match practice, with the caveat that any
  attached reference still respects the no-baked-Arabic and visual-constant rules.

P3, optional
- Variant rationale for testing. We require 2 or more variants but do not ask the writer to name
  the one variable each variant isolates. Naming it would sharpen the downstream A/B test
  (stream 8) and is consistent with real-alternatives-not-padding.

## Where ours is stronger

These are deliberate, defensible advantages over the generic external playbooks. They should
be preserved in any edit.

- English-first as the design center, not a localization afterthought. Every copy sub-skill
  drafts Arabic first in MSA with Gulf-familiar wording against the Thmanyah tone benchmark
  (`context/brand-voice.md`, each `04-copywriting` sub-skill). The external sources are English
  defaults with localization bolted on. Ours inverts that.
- No Arabic baked into generated images. `03-creative-production/SKILL.md` and
  `image-prompting/SKILL.md` make this a hard rule: generative tools mangle Arabic and add
  tatweel, so Arabic only ever lands as a human-placed overlay, gated by `arabic-copy-qa`. No
  generic prompt guide addresses this, and it is the single most important Arabic-creative
  safeguard.
- Copy-overlay slots as a contract. Named, empty overlay slots (headline, subhead, CTA) bound
  to copy-package variant ids (`image-prompt-sheet.md`, `handoff-contract.md`) cleanly separate
  text-free image generation from human-written copy. This is cleaner than the typical "write
  the words into the prompt" advice and removes a whole class of rendering failure.
- Mechanical brand rules as enforced gate checks, not preferences. No em dash, no tatweel
  (U+0640), Western numerals only (never U+0660 to U+0669), RTL-safe. These are checked by
  `arabic-copy-qa` and `brand-qa-reviewer`, not left to a style note. External guides have no
  equivalent of a hard mechanical gate.
- No-invented-offer discipline. Every copy sub-skill forbids inventing an offer, price, Skill
  Path title, or instructor name, and stops to ask when the brief is silent. The campaign-
  agnostic principle keeps variables in the brief. Generic frameworks happily invent specifics.
- Language QA gates before brand QA. The ordered stack (skill eval, then language QA, then
  brand QA, plus design QA on visuals) is a verification discipline the external sources do not
  carry. A fail is a hard stop with an exact fix list, not a suggestion.
- Empowering, never deficit-framed. The voice rule (speak to what the reader can become, never
  shame) is a worked, gated standard. PAS in particular, which agitates a pain, is constrained
  by it: we can name a problem but not shame the reader, which is a healthier default than the
  generic "agitate harder" advice.

## Recommendations (specific edits, prioritized, tied to sources)

Each is a proposal for a skill author to apply through the normal gate. No file is edited here.

1. P1. Add a named-framework reference to the copy sub-skills. In `04-copywriting/ad-copy`,
   `email-copy`, and `subject-lines`, add a short "structures you can reach for" note: the 4 Us
   (Useful first, then Urgent, Unique, Ultra-specific) as the headline and subject checklist;
   PAS for pain-aware, bottom-funnel placements (problem named without shaming the reader, to
   honor the empowering rule); AIDA for cold, top-funnel placements; the 4 Cs (Clear, Concise,
   Compelling, Credible) as a final pass. Keep these as optional tools, not mandates, so the
   voice stays primary. Sources: Anyword and Copywriter Collective (4 Us), Reads to Leads and
   Crazy Egg (AIDA, PAS).

2. P1. Make the subject-line length bar mobile-justified and add front-loading. In
   `subject-lines/SKILL.md` step 3 and the template checklist, restate the bar as roughly 30 to
   40 characters with the key word in the first 30 characters, and add a one-line reason: most
   opens are on mobile, where roughly 33 to 35 characters show. Add a checklist item: "front-
   load the message, the angle lands in the first few words." Sources: Twilio, Attentive,
   Mailchimp.

3. P1. Add a preheader field to the email and subject deliverables. In `email-copy` (template)
   or `subject-lines` (template), add an optional `preheader:` field with a short bar (roughly
   40 to 90 characters, true to the body, no spilled body text), so the inbox preview is set on
   purpose rather than by accident. Keep all mechanical rules (no em dash, Western numerals).
   Sources: Twilio, Mailchimp.

4. P2. Add a short composition and lighting vocabulary to the image prompt template. In
   `image-prompt-sheet.md`, expand the `prompt_en` guidance with a controlled menu: framing
   (close-up, medium, wide), viewpoint and angle (eye-level, low-angle, top-down), layout
   (asymmetric, negative space on one side, rule of thirds), and named lighting (soft diffuse,
   golden hour, high-contrast). Add a density target: roughly 15 to 50 words, every word
   earning its place. This keeps prompts from defaulting to a flat centered frame. Sources:
   Let's Enhance, LTX, OpenAI cookbook.

5. P2. Add CTA-phrasing and placement notes to ad-copy and email-copy. Keep the one-CTA hard
   rule, and add: put the CTA on its own line, and consider first-person phrasing where it fits
   the Arabic voice. Frame it as guidance, not a rule, since Arabic phrasing differs from the
   English test data. Sources: Moosend, HubSpot.

6. P2. Add a visual-reference hook to the concept brief. In
   `creative-concept-brief.md`, add an optional `references:` line (links or notes), with a
   caveat that any reference still respects the no-baked-Arabic rule and the visual constants
   (#141414, #1A1A1A, #009975). Words miss visual nuance, and references close that gap.
   Sources: Adobe, Shopify, Asana.

7. P3. Ask each ad or email variant to name the one variable it isolates. Add an optional
   `tests:` line to the ad-copy and email-copy templates (for example "tests: headline angle"
   or "tests: CTA verb"), so the downstream A/B plan (stream 8) inherits a clean hypothesis.
   Sources: Reads to Leads, Crazy Egg (variants as real alternatives).
