---
name: me
description: How to market Ahmed El Sanhoury (the person this engine is for). Use for any asset built around you: bio, LinkedIn, portfolio, career stories, talks, outreach. Loads with context/subjects/me.md (facts and the binding claims table), this pack's voice.md and templates. Seeded as a stub; run /ingest and /mine-subject me to fill it from your own material. Never publish a claim about yourself that is not a verified row in me.md.
---

# Marketing Ahmed El Sanhoury (the `me` product skill)

Read first: `context/subjects/_CATALOG.md` (status), `context/subjects/me.md` (facts, the
claims table is binding), `voice.md` (register and hooks), the active brief (objective,
channel, audience).

## What the product is

You. A personal brand spanning four emphases: career and employability, personal business and
services, creator and audience growth, and a founder/venture brand built alongside. The
concrete offer in any given asset comes from the brief, never invented here.

## Segments and angles (fill from your positioning)

Define 3 segments your material supports, each with its angle and the verified proof behind it.
Until `/ingest` and `personal-brand` fill these, they are TODO, not to be guessed.

1. [audience 1, e.g. hiring managers / employers]. Angle: TODO. Proof: claims rows TODO.
2. [audience 2, e.g. potential clients]. Angle: TODO. Proof: claims rows TODO.
3. [audience 3, e.g. your growing audience]. Angle: TODO. Proof: claims rows TODO.

## What copy may promise vs not

Copy speaks to what you have done and can do, earned by a verified claim. It never overstates a
title, inflates a result, claims a credential you do not hold, or names a client or employer
without consent. Empowering framing, specific over generic.

## Career stories

Story material lives in `context/subjects/me.md` (career chapters, signature projects). The
`career-narrative` skill turns it into engaging retellings (origin arc, STAR case studies,
LinkedIn/talk/portfolio cuts). Every story stays inside the verified claims.

## Gate stack

Pack eval first (machine checks then llm checks), then `english-copy-qa` (default;
`arabic-copy-qa` if Arabic is in scope), then `brand-qa-reviewer`, then the human gate (you).
