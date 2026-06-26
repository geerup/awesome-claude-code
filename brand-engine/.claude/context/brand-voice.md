# brand-voice.md: how this brand sounds and looks (active profile = me)

Loaded by every agent before it produces anything customer-facing. This is the voice
`english-copy-qa` and `brand-qa-reviewer` check against. It is a source of truth, not a
campaign input. Campaign variables (offer, price, target) never live here.

The defining content of this file is produced by the `brand-voice` and `brand-identity`
skills from your `brand-context` (run `/brand-context` then those skills). Until then the
voice qualities below are sensible defaults and the visual constants are `TODO`, not Maharat's.

---

## The one-line identity
TODO (one line: who you are and the one thing you want to be known for). Set by
`personal-brand` + `brand-positioning`. The voice should sound like that line.

## Language posture
- Primary language: **English**. English is primary and authoritative here.
- Secondary language: Arabic, optional, only when a brief sets it in scope. When Arabic is in
  scope, `copywriter-ar` and the Arabic gates (`arabic-copy-qa`, `AS-arabic-nlp`) activate and
  the Arabic mechanical rules below apply. When Arabic is not in scope, they do not run.

## Voice qualities (defaults until brand-voice skill refines them)
- Plain and confident. Short sentences. Concrete nouns. Active voice.
- Specific over generic. Earn every claim with a concrete proof.
- Empowering, not deficit-framed. Speak to what the reader can do and become.
- Respect the reader's intelligence. No hype words, no filler, no condescension.

### Empowering vs deficit-framed, worked
- Deficit: "Stop wasting your potential. You are falling behind."
- Empowering: "You already have the drive. Here is the path that turns it into a skill."

## Hard mechanical rules (gate checks, not preferences)
- No em dashes anywhere, in any language. Use a comma, a colon, or a period. (A kept default
  from the original engine; harmless and consistent. Relax per profile if you ever want to.)
- These apply **only when Arabic is in scope**:
  - No tatweel or kashida (Unicode U+0640).
  - Western numerals only (0 to 9), never Eastern Arabic-Indic digits (U+0660 to U+0669).
  - RTL must render correctly; mixed AR and EN or numerals must not break direction.

## Visual constants
- Set by `brand-identity`. Until then these are `TODO`. Do NOT reuse Maharat's emerald
  `#009975` / near-black `#141414` / card `#1A1A1A` as if they were yours; those live in the
  archived `context/profiles/maharat/brand-voice.md`.
- Primary color: TODO   Secondary: TODO   Background: TODO   Accent: TODO
- Typography: TODO   Logo / wordmark: TODO
- Design principle: TODO (e.g. premium, uncluttered, generous space). Set with brand-identity.

## Content guardrails (you can be embarrassed or exposed if these slip)
- Do not overstate your credentials, titles, results, or affiliations. Public claims about you
  are verified in `context/subjects/me.md` first.
- Do not name a client, employer, or collaborator publicly without consent.
- No confidential or under-NDA material in public output.
- Never imply a credential, certification, or accreditation you do not hold.

## Audience to keep in mind while writing
TODO (set from `target-audience`). Write for the specific person you want to reach, in their
language, not yours.

## Where the deep voice lives
- Foundation: `context/profiles/me/brand-context.md` (and `.agents/brand-context.md`).
- Full verbal identity: produced by the `brand-voice` skill (tone dimensions, vocabulary,
  do/don't, channel adaptations) and folded back into this file.
- Your mined voice (hooks, phrases, cadence from your own writing): `context/subjects/me.md`
  (`voice.md`), produced by `/ingest`.
