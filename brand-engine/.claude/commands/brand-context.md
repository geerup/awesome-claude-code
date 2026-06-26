---
description: Set or refresh the brand foundation. Runs the brand-context skill (and points to the foundation sequence), then keeps the canonical file and the auto-read mirror in sync. Usage - /brand-context
allowed-tools: Read, Write, Edit, Glob, Grep, WebSearch, WebFetch
---

# /brand-context

Seed or refresh the brand foundation that every brand skill and every funnel stream reads.

## What to do

1. Run the `brand-context` skill. Gather only what is missing (do not re-ask what is already
   filled). For a personal brand, also capture the Person section (role, zone of authority, the
   one thing to be known for).
2. Write the result to BOTH:
   - canonical: `context/profiles/me/brand-context.md`
   - auto-read mirror (what the 29 brand skills read first): `.agents/brand-context.md`
   Keep them identical. If they ever diverge, the canonical wins.
3. Reflect the engine-side digest into `context/01-brand-brief.md` and, for voice/visuals,
   `context/brand-voice.md` (these are filled fully by the `brand-voice` and `brand-identity`
   skills).
4. Recommend the foundation sequence next (see `skills/_BRAND-FOUNDATION.md`):
   `/ingest` -> `personal-brand` -> `target-audience` -> `competitor-branding` ->
   `brand-positioning` -> `brand-strategy` -> `brand-voice` -> `brand-messaging` ->
   `brand-identity` (and `brand-architecture` if a venture is in scope).

## Rules
- Do not invent facts about the person or brand. Unknown is an OPEN ITEM, not a guess.
- English-first. No em dashes.

$ARGUMENTS
