# Brand Context (active profile: me)

Canonical source of truth for the personal brand. The 29 brand skills auto-read a mirror of
this file at `.agents/brand-context.md`; keep the two in sync (the `/brand-context` command
writes both). Every other skill reads this first before doing anything, so it does not
re-ask for what is captured here.

This is a personal brand, so it carries a **Person** section on top of the standard
brand-context schema. Fields marked `TODO` are filled by running `/brand-context` (and
`/ingest` to mine your existing content, then `personal-brand`, `brand-strategy`,
`brand-voice`, `brand-identity`). Do not invent values: an unfilled field stops and asks.

---

## Person
- Name: Ahmed El Sanhoury
- Current role / title: TODO
- Zone of authority (what you know deeply x have lived x believe differently): TODO
- The one thing to be known for (one sentence): TODO
- Career arc (the through-line of your story): TODO

## Brand
- Name (personal brand name, usually your name): Ahmed El Sanhoury
- Category (the space you operate in): TODO
- Description (one line: what you do and for whom): TODO
- Stage (establishing / growing / established / pivoting): TODO
- Primary website / home base: TODO

## Audience
- Primary audience (who you want to reach: employers, clients, collaborators, community): TODO
- Key problem (what they are struggling with that you address): TODO
- Their language (words they use, not jargon you use): TODO

## Positioning
- Differentiation (what you offer that peers do not): TODO
- Peers / others in this space (3 to 4): TODO
- Market position (premium / value / niche / mass / category-of-one): TODO

## Brand personality
- Personality words (3 to 5): TODO
- Tone (formal vs casual, serious vs playful): TODO
- Voices you admire (and why): TODO

## Values and mission
- Core values (3 to 5): TODO
- Mission (what you are trying to change or build): TODO

## Point of view (personal brand)
- 3 to 4 core beliefs you hold that most in your field do not say out loud: TODO

## Goals
- Primary 12-month goal (career / clients / audience / venture): TODO
- Emphases active for this engine: career & employability; personal business / services;
  creator / audience growth; founder / startup brand. (All four are in scope per setup.)
- Key metrics (how you will know it is working): TODO

## Language and house style
- Primary language: English.
- Secondary language: Arabic, optional, only when a brief sets it in scope (the Arabic QA
  gates and copywriter then activate).
- House style: plain, confident, specific. No hype. No em dashes (a kept default, easy to
  relax per profile). When Arabic is in scope: Western numerals, no tatweel, RTL-safe.

## Visual constants
- Set by `brand-identity` / `brand-voice`. Until then, these are TODO, not the Maharat
  emerald. Do not reuse Maharat's `#009975` / `#141414` as if they were yours.
- Primary color: TODO   Secondary: TODO   Background: TODO   Type: TODO

## Founder / venture link (if a venture brand exists)
- Venture brand name: TODO (none yet)
- Relationship to the personal brand (set with the `brand-architecture` skill): TODO

## Subjects registry
- The marketable entities for this profile live in `context/subjects/` (you = `me.md`, plus
  service verticals, the venture, and research targets). Mined with `/mine-subject`.
