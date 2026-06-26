# organic-social-style.md: how Maharat organic social is written and structured

Extracted and normalized from the team's organic copy document (the "Organic Copy Doc", the
production doc for previous and planned Maharat organic posts). This file captures the reusable
voice-in-practice, the formatting legend, the bilingual convention, and the post-format
taxonomy. It is a companion to `brand-voice.md`, not a replacement. Where the source document
conflicts with a hard rule in `CLAUDE.md` or `brand-voice.md`, the engine rule wins. Every such
conflict is listed in the reconciliation section at the end so nothing is imported blindly.

Source: Organic Copy Doc (Maharat). Provenance only; this file is the normalized version the
engine uses.

---

## What this adds over brand-voice.md

`brand-voice.md` sets the voice and the hard rules. This file adds the practical, repeatable
structure of how that voice shows up in organic social: the formats, the slide and story
scaffolds, the engagement mechanics, and the CTA patterns the team actually uses.

## The formatting legend (production shorthand)

The source doc uses a consistent shorthand for who reads what and where it appears. Keep it when
writing or routing organic creative, so design and copy stay aligned.

| Term | Meaning |
|---|---|
| Regular text | The sound bite or on-screen script, the words the viewer reads or hears |
| Italic note | A note or description from the team, not customer-facing, never rendered |
| Super | Text laid on top of footage or a visual (a caption over video) |
| Title Card | Full-screen text on a matte background (no footage behind it) |
| Frame Copy | Copy for in-frame videos or statics (text inside the composed frame) |

In this engine, customer-facing words inside any visual are still overlay slots filled by
`copywriter-ar` (AR) or `copywriter-en` (EN). Arabic is never baked into a generated image. See
the creative rule in `brand-voice.md`.

## Bilingual convention

- Most posts are bilingual, English and Arabic, with Arabic carrying equal weight. Arabic is
  primary per the Arabic-first rule, English follows the same spirit.
- Two layouts appear in the source: "Bilingual" (EN and AR together on one slide or story) and
  "AR/EN separate" (parallel AR and EN versions). Pick per format and platform; note the choice
  in the template.
- Direct, attributed instructor quotes may be kept verbatim even when colloquial, because they
  are real quotes. All other copy is Modern Standard Arabic with Gulf-familiar wording.

## Voice in practice (patterns observed, all on-brand)

- Open on a sharp question or a relatable tension, then resolve it. Example pattern: a hook
  question, a moment of chaos or confusion, then clarity.
- Name the real problem plainly, then offer the structured path out. Empowering, not
  deficit-framed: the reader is capable, they need clarity and a system.
- Short lines. One idea per line. Concrete nouns. Active voice.
- Outcomes are specific and confident: "a stronger voice, clearer expression," "a polished
  everyday look," "meals you can make any day of the week."
- Close with one clear action.

## Engagement mechanics (story-native)

The source leans on interactive story stickers to drive participation. When a post uses one,
leave the on-screen space for it and never bake the options into the art.

- Poll: a question plus 2 to 4 short options. Leave space under the question for the sticker;
  do not render the poll title or options as baked text.
- Emoji slider: a single question with a slider. Leave space, no baked title.
- Countdown: a launch or drop countdown. Leave space for the countdown sticker in 9:16.
- Quiz: a question with a right answer, for teaching moments.

## CTA patterns (the comment-to-DM and DM-to-link mechanics)

The source uses comment and DM keyword mechanics to turn reach into leads. The keyword is
highlighted in a pill shape or underline. Keep the action singular and clear.

- Lead magnet: "Comment [KEYWORD] to get the full guide." The keyword triggers a DM with the
  asset link.
- Early access or launch: "DM us [KEYWORD] to get an exclusive launch link." or "Reply
  [KEYWORD] for early access."
- The keyword is a placeholder per campaign (for example GUIDE, START, READY, BRAND). It is a
  campaign input, never invented here.

Compliance note: any link the DM delivers, and any gate it lands on, must carry no personal or
sensitive data in the URL, and the data-collection point must disclose its collection per the
privacy rules. Comment-to-DM automation is a tool and platform decision, gated, not assumed.

## Post-format taxonomy (templates live in the skills)

These are the recurring formats. Each has a reusable template in its related skill folder.

| Format | Where the template lives |
|---|---|
| Story engagement sequence (hook, tension, poll, pain point) | skills/organic-social/post-templates/ |
| Countdown or launch story (countdown, poll, CTA lead-gen) | skills/organic-social/post-templates/ |
| Value carousel (hook, pain, what is inside, visual, CTA) | skills/organic-social/post-templates/ |
| Myth-buster carousel (cover, myth and truth, closer CTA) | skills/organic-social/post-templates/ |
| Skills roundup carousel (cover, one skill per slide, CTA) | skills/organic-social/post-templates/ |
| Quote inspiration carousel (cover, one quote per slide) | skills/organic-social/post-templates/ |
| Class trailer structure (authority, credibility, scroller, end card) | skills/03-creative-production/creative-concepting/templates/ |
| Teaser hype video (counter, stat frames, reveal, CTA) | skills/03-creative-production/creative-concepting/templates/ |
| Social CTA and caption patterns | skills/04-copywriting/ad-copy/templates/ |

---

## Reconciliation with engine hard rules (the source conflicts, resolved)

The source document predates this engine's rule set and conflicts with it in five places. In
every case the engine rule wins. These are recorded so the conflicts are visible, not silently
carried forward.

1. Numerals. The source uses Eastern Arabic numerals (for example the year written in
   Arabic-Indic digits, percentages, and "skill 1" markers). The engine requires Western
   numerals 0 to 9 in all copy. Convert on import. Templates here use Western numerals.
2. Em dashes. The source uses em dashes in slide headers and copy. The engine bans em dashes in
   any language or file. Use a comma, a colon, or a period. Templates here carry none.
3. Visual palette. The source stories use bright theme backgrounds (orange, red, pink, yellow)
   and magenta text highlights. These conflict with the brand visual constants (near-black
   #141414, card surfaces #1A1A1A, emerald accent #009975). The brand constants remain
   authoritative. The bright per-campaign backgrounds are NOT adopted. If a future campaign
   wants a seasonal palette, that is an explicit decision for Ahmed, not a default. Flagged as
   an open item, not resolved here.
4. Baked offers. The source bakes specific offers into posts (for example an end-of-year
   percentage discount). Offers and prices are per-campaign brief inputs and are never
   hard-coded. Templates use placeholders ([OFFER], [DISCOUNT], [KEYWORD]).
5. Named instructors and titles. The source names instructors and uses class titles in posts.
   Templates stay campaign-agnostic and use placeholders ([INSTRUCTOR], [CLASS TITLE]). Naming
   any instructor in a live post still requires the standing confirmation rule: only when
   confirmed public via a published Maharat course page. Never invent a Skill Path title or the
   content lineup.

All other patterns from the source (the formats, the hooks, the engagement mechanics, the CTA
structure, the bilingual layout, the outcome-led voice) are on-brand and adopted.
