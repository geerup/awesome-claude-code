# Template: Class trailer structure (video)

A reusable structure for a class or Masterclass trailer cut, extracted and normalized from the
Maharat organic copy doc. Campaign-agnostic scaffold for creative-director and the designer.
Structure and direction only. On-screen words are overlay slots filled by copywriter-ar (AR
primary) and copywriter-en. Arabic is never baked into a generated image. Nothing publishes.

- Length: about 35 to 45 seconds (confirm per brief).
- Visual constants: #141414, #1A1A1A, emerald #009975. Premium, uncluttered. Real,
  rights-cleared instructor footage and stills only, never a generated likeness.
- Footage timecodes are pulled from the source trailer or hero asset; note the slot, do not
  invent a timecode.

## Structure

### 1. Opening, the hook
- Visual: a strong opening line or moment from the instructor. [footage slot, timecode].
- Super slot (AR/EN): [a short hook line over the footage].

### 2. Title card, authority stack (ordered by priority)
- Full-screen matte title card. List the credibility markers ordered by priority, so if space
  runs short you remove from the bottom up.
- Slots (AR/EN), confirmed facts only: [award or recognition 1], [2], [3], with any logos that
  are cleared for use. No invented award, no accreditation implication.

### 3. Title card, credibility stack
- Full-screen matte title card. The instructor's track record in concrete numbers.
- Slots (AR/EN), confirmed facts only: [years of experience], [role or title], [scale, for
  example teams led], [body of work]. Western numerals. No invented figure.

### 4. Title card, class scroller
- A scrolling list of what the class covers, the topics as hooks (not full lessons).
- Slots (AR/EN): [topic 1], [topic 2], [topic 3], [topic 4], and "and much more".
- Do not invent the lineup. Use confirmed class topics from the brief or the published course
  page. If topics are not confirmed, this card is an open item.

### 5. Closing and end card
- Visual: a closing line from the instructor. [footage slot, timecode].
- End card (AR/EN): [INSTRUCTOR] teaches [CLASS TITLE]. Watch on Maharat.
- [INSTRUCTOR] and [CLASS TITLE] are brief inputs. Name the instructor only when confirmed
  public via a published Maharat course page.

## Slots to resolve from the brief

- [INSTRUCTOR], [CLASS TITLE], the authority and credibility facts, the class topics, the
  footage timecodes, the cleared logos.
- The authority and credibility facts come from the instructor's profile in
  `context/profiles/maharat/instructors/<slug>/profile.md`. Use only facts marked cleared there. If a fact is
  marked "verify before public use", it is not yet usable in a public trailer.
- No price. No invented award, figure, topic, or title. No accreditation implication.

## Routing and gates

- Direction here, visuals executed by the designer. On-screen words to copywriter-ar and
  copywriter-en.
- Gate stack: skill eval, arabic-copy-qa, english-copy-qa, design-qa (RTL, brand constants,
  Western numerals, no baked Arabic), brand-qa-reviewer, then the human gate to publish.
