# Multi-instructor and catalog email angles

How the engine builds an angle for an email that features two or more instructors, or the catalog
as a whole, rather than a single class. This is the method behind a Skill Path email, a themed
roundup, an occasion sale, or a "picked for you" recommendation. It is the reusable craft; the
specifics (which instructors, which offer, which occasion, which Skill Path) are always brief and
context inputs, never invented here.

Primary evidence: `references/2026-06-masterclass-multiinstructor-teardown.md`. This doc is the
method; that doc is the teardown it was drawn from. Strategy uses this in
`skills/02-strategy-planning/offer-and-angle`; copy uses it in
`skills/04-copywriting/email-copy`; the build modules are LessonCardGrid, IssueIndex, and MemberWin
in `context/email-design-system.md`.

Arabic-first, empowering, never deficit-framed. No em dashes, no tatweel, Western numerals only.
No accreditation implication. Any Arabic line below is illustrative, replace before use; copy is
authored by copywriter-ar or copywriter-en and runs the gate stack.

---

## The one rule: the angle is a reader outcome, not a list of teachers

A multi-instructor email fails the moment it becomes "here are some of our instructors." The angle
is one outcome the reader wants, and each instructor is cast as one path toward it. The reader
should feel the email is about their goal, with the instructors as the proof that the goal is
reachable.

So every multi-instructor email starts the same way: name the outcome, then group instructors who
each move the reader toward it.

---

## Step 1: pick the grouping logic

One of six. The brief or the occasion decides which; do not mix more than one umbrella per email.

1. Skill or topic cluster. Several instructors who each teach a different facet of one capability
   (for example several voices on persuasion, or on building a business). Umbrella = the
   capability the reader gains.
2. Occasion or moment. A calendar moment in the Maharat market (for example Ramadan, Eid,
   back-to-school, National Day, a New Year reset). Umbrella = the moment reframed to what the
   reader can do for themselves or someone they care about. The occasion must be real and in the
   brief or calendar, never invented.
3. Identity or values moment. A theme the audience identifies with, told with care and never as a
   stereotype. Umbrella = "turn who you are into a strength."
4. Curated recommendation. A personalized set across unrelated topics. Umbrella = recognition,
   "chosen for you," and it must rest on real, consented signal, never a faked personal field.
5. Catalog offer. A discount or bundle across the catalog or a Skill Path. Umbrella = the offer
   itself, with the value made plain. Price, discount, and dates come from the brief, never
   invented, and certificates are never implied to be accredited.
6. Gifting or referral. Give-a-membership or refer-a-friend, aimed at existing members or engaged
   contacts (a different audience from non-payers), often tied to an occasion (a holiday, a
   giving moment). Umbrella = "share what you value with someone you care about." The offer and
   dates come from the brief, never invented; suppression and consent for the gift recipient still
   apply.

Not a grouping logic, and not buildable here: a contest, sweepstakes, or prize draw (for example
"win a session with an instructor"). It is a recognized acquisition mechanic in the references, but
for Maharat it is gated: it needs Saudi PDPL, contest and sweepstakes law, eligibility, and
entry-data handling cleared by `compliance-privacy-reviewer` before anything is designed or built.
Until then, document it and stop, do not produce a contest email.

## Step 2: write the umbrella outcome (the hero)

One sentence the reader wants to be true about themselves, in the Maharat voice. It states the
gain, not the deficit. It sets up why several instructors belong in one email: they are all paths
to this one outcome.

- Good shape: name the gain, then promise the email is the path to it.
- Avoid: "meet our instructors", "explore our catalog", any line about the brand rather than the
  reader.

## The subject formula: "3 [ways or lessons] to [outcome]"

The dominant multi-instructor subject in the reference corpus is a number plus the umbrella
outcome: "3 ways to [outcome]", "3 lessons to [outcome]", "3 tips to [outcome]". The number matches
the count of lesson cards, and the subject is the umbrella outcome itself, so the subject and the
hero and the cards all carry one promise. Use it for the skill-cluster and occasion archetypes. The
number is the real card count (usually 3), never inflated. Western numerals. It pairs with a
rule-of-three preheader that previews the three cards.

## Step 3: cast each instructor as one lesson card

Each card uses the same three-part formula. This is the LessonCardGrid module.

```
headline:   an outcome-first, verb-led line (what the reader will be able to do)
credential: "with [Instructor], [one page-cleared credential line]"
link:       a quiet secondary link to that class (label like "Start learning"), never a competing button
```

Co-taught is different from a digest. When two or more instructors teach ONE class together (a
single co-taught course), that is not a LessonCardGrid of separate classes: it is one Hero plus one
BodyCopy that names both instructors and the one class. The LessonCardGrid is for N separate
classes, one instructor each, under the shared umbrella. Do not force a co-taught class into the
grid, and do not split a digest's separate classes into one card.

Rules for the card:
- The headline is the reader's outcome, not the class title and not the instructor's name.
- The credential line names the instructor and one reason to trust them. That one reason must
  trace to a page-cleared fact or a voice.md verified-safe belief for that instructor
  (`skills/instructor-marketing`). No borrowed or inflated credential.
- The instructor must be catalog-status-confirmed before the email can advance. An unconfirmed
  instructor is held back, the card is dropped, not improvised.
- Three cards is the natural set (the grid is 3-up). Fewer is fine; more becomes a long scroll.

## Step 4 (optional): lead and supporting cast

When one instructor leads the email, give that one a deeper INSTRUCTOR SPOTLIGHT block (a short
"what you will be able to do" list), and keep the others as compact cards. This lets one email
headline a single instructor and still feature several, useful for a Skill Path with a marquee
name plus a supporting lineup.

## Step 5: one primary CTA, per-card links stay quiet

The email has exactly one primary action, the join or the offer, rendered as the one emerald pill
and repeated at most once near the foot. Every per-card "start learning" link is a quiet secondary
text link, never a second pill. This keeps the constitution's one-primary-CTA rule intact in a
multi-card layout (see `context/email-design-system.md`, the CTA rule).

---

## The angle archetypes, mapped to grouping logic

| Archetype | Grouping logic | Umbrella outcome (shape, not copy) | Lead module |
|---|---|---|---|
| Themed roundup (the "3 ways to X" digest) | skill or topic cluster | "Get better at [capability], with the people who do it best" | IssueIndex then LessonCardGrid |
| Occasion sale | occasion plus catalog offer | "[Moment] is a reason to invest in yourself" | IssueIndex then LessonCardGrid |
| Identity moment | identity or values | "Turn [who you are] into your strength" | LessonCardGrid plus one Spotlight |
| Picked for you | curated recommendation | "Chosen for you, based on what you have watched" | LessonCardGrid |
| Skill Path launch | skill cluster, brief-named path | "One path, several mentors, one outcome" | Spotlight plus LessonCardGrid |
| Gifting | gifting or referral | "Share what you value with someone you care about" | BodyCopy offer plus optional LessonCardGrid |

The Skill Path titles and lineup are never invented. They come from context and the brief; a
missing one is a stop-and-ask (the guardrail in `CLAUDE.md`).

---

## Brand adaptations (every multi-instructor email)

- Arabic-first, empowering, no deficit framing. The umbrella speaks to a gain.
- No em dashes, no tatweel, Western numerals only.
- No accreditation or certificate-equivalence claim, ever. Outcomes, not credentials-as-proof.
- Every instructor credential traces to a page-cleared fact; every named instructor is
  catalog-status-confirmed, or the card is dropped.
- Catalog counts, prices, discounts, dates, and Skill Path titles are brief and context inputs,
  never invented. "Up to X percent" or "N classes" render only from a real value.
- Personalization ("picked for you") rests on real consented signal only, never a faked field, and
  never personal data in a URL or tracking.
- One primary CTA. Per-card links are quiet secondaries.

## How this connects

- Strategy (`offer-and-angle`) sets the umbrella outcome and the grouping logic as the campaign
  angle when the brief's product is a Skill Path, a bundle, an occasion promotion, or a catalog
  recommendation.
- Copy (`email-copy`) writes the hero umbrella line, the per-card outcome headlines, the credential
  lines (from the instructor packs), the IssueIndex labels, and the MemberWin, as copy-package
  variants bound by id.
- Lifecycle (`promo-sequence` and the other patterns) sequences these emails; a single
  multi-instructor email can also sit inside a non-payer, welcome, or winback flow.
- Build (`email-html-build`, `scripts/email_render.py`) renders the LessonCardGrid, IssueIndex, and
  MemberWin modules, each slot bound to a QA-passed `data-copy-id` and gated.
