# Brand foundation: the upstream layer (29 skills)

These skills were folded in to expand the engine, not replace anything. The engine already had
QA gates that *check* brand voice and design; it lacked skills that *define* brand strategy,
identity, positioning, voice, story, and messaging. These fill that gap and run as Stream 0
(see `runtime/stream-ownership.md`).

They are standard Agent-Skills (`SKILL.md` + YAML), invoked by name or by their trigger
phrases. Every one of them reads `.agents/brand-context.md` first (the active profile's
brand-context, canonical at `context/profiles/me/brand-context.md`). Run `/brand-context` once
to seed it before the rest.

## The layers

### Foundation
- `brand-context` — captures and stores brand DNA; written to `.agents/brand-context.md`. Run first.

### Strategy and positioning
- `brand-strategy` — full brand strategy report.
- `brand-positioning` — competitive position, positioning statement, proof points.
- `brand-architecture` — how your personal brand and any venture/sub-brands relate (founder use).
- `competitor-branding` — how competitors brand themselves; gaps to own.
- `target-audience` — ICP, personas, audience language.
- `brand-measurement` — brand KPIs and tracking (feeds streams 8 and 9).

### Identity and visual
- `brand-identity` — visual identity brief (logo direction, palette, type, imagery). Feeds streams 3 and 6.
- `brand-story` — origin and founder narrative (long, short, one-liner).
- `brand-packaging` — packaging design brief (product use).
- `brand-naming` — generate or evaluate names (venture / product use).

### Voice and messaging
- `brand-voice` — verbal identity; folds into `context/brand-voice.md` and feeds `brand-qa-reviewer`.
- `brand-messaging` — messaging hierarchy, value prop, key messages. Feeds stream 4.
- `brand-manifesto` — belief-driven declaration.

### Launch and transform
- `brand-launch` — public debut plan.
- `rebranding` — strategic transformation of an existing brand.
- `brand-audit` — brand health across 6 dimensions.
- `brand-guidelines` — the standards document (visual + verbal).

### Personal and B2B
- `personal-brand` — the spine for this engine: positioning, point of view, platform, content
  pillars, bios, 90-day launch. Run early.
- `b2b-brand-marketing` — B2B positioning, buying committee, thought leadership, LinkedIn.
- `brand-partnerships` — co-branding and alliances.

### Channels (sit beside the engine's own channel hubs; inform, never replace)
- `d2c-marketing`, `email-marketing`, `whatsapp-marketing`, `meta-ads`, `google-ads`,
  `influencer-marketing`, `ugc-strategy`. The brand `aso` playbook is preserved inside the
  engine's `aso` skill at `aso/references/brand-aso-playbook.md` (the engine's decomposed `aso`
  hub stays the channel owner).

## Dependency map (read brand-context first)

```
brand-context  ->  everything below reads it first
  strategy:   brand-strategy <-> brand-positioning <-> brand-messaging
  identity:   brand-identity <-> brand-voice <-> brand-guidelines
  transform:  brand-audit -> rebranding -> brand-launch
  audience:   target-audience -> brand-messaging, brand-voice, brand-positioning
  compete:    competitor-branding -> brand-positioning, brand-strategy
  personal:   personal-brand <-> b2b-brand-marketing <-> brand-manifesto
  venture:    brand-architecture <-> brand-naming <-> brand-strategy
  measure:    brand-measurement <-> brand-audit <-> brand-strategy
  channels:   d2c-marketing <-> meta-ads <-> google-ads <-> email-marketing; ugc <-> influencer
```

## Relationship to the engine's existing skills

- These define; the engine's gates (`brand-voice-qa`, `english-copy-qa`, `design-qa`,
  `web-design-qa`, `brand-qa-reviewer`) check against what they define.
- These are upstream; the engine's 9 funnel hubs (`01-brief-intake` ... `09-reporting-learning`)
  execute campaigns using the foundation as input.
- Only one name overlapped the engine (`aso`); the brand playbook was merged in, not dropped.
