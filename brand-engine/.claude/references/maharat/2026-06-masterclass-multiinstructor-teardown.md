# Multi-instructor email findings: a MasterClass teardown

How to produce multi-instructor offer emails, and how to build an angle that talks about several
instructors in one send. Drawn from a primary-source teardown of about 180 live MasterClass
marketing emails across 7 batches, parsed 2026-06-19, and turned into a reusable, campaign-agnostic
capability in this engine. (The first pass was 39 emails from batch 1; the full corpus confirmed
the findings at scale and surfaced the additions in section 9.)

The corpus is now committed in the repo at
[`references/masterclass-emails/`](https://github.com/hostmaster-maharat/claude/tree/claude/laughing-dijkstra-0cx0tv/.claude/references/masterclass-emails)
(178 marketing emails in per-batch folders; 6 transactional receipt, refund, and invoice files were
held out as personal data, see that folder's README). The analysis is reproducible: run
[`scripts/email_corpus_analyze.py`](https://github.com/hostmaster-maharat/claude/blob/claude/laughing-dijkstra-0cx0tv/.claude/scripts/email_corpus_analyze.py)
to regenerate the catalog and tally at
[`references/masterclass-emails/INDEX.md`](https://github.com/hostmaster-maharat/claude/blob/claude/laughing-dijkstra-0cx0tv/.claude/references/masterclass-emails/INDEX.md)
(178 emails, 48 with a multi-instructor signal, 46 with an offer subject).

This is a findings map with the work that shipped linked inline. The rules it serves live in
[`CLAUDE.md`](https://github.com/hostmaster-maharat/claude/blob/claude/laughing-dijkstra-0cx0tv/.claude/CLAUDE.md)
and the anchor docs it points to. The canonical method is
[`context/multi-instructor-angles.md`](https://github.com/hostmaster-maharat/claude/blob/claude/laughing-dijkstra-0cx0tv/.claude/context/multi-instructor-angles.md).
Reference only: MasterClass is a different brand with different rules. Borrow the structure and the
angle craft, never the copy mechanics (several of their habits are hard stops here, see section 7).
No em dashes, Western numerals only; the source emails use em dashes and accreditation language
this file does not reproduce.

## 1. The headline finding

MasterClass runs two email engines side by side:

- Single-instructor class emails (about 70% of the batch): one class, one teacher, one sharp
  angle. For example `NEW: Turn office tension into your next promotion`, `A neuroscientist's
  secret to relationships that last`, `Why your instincts won't help you in a fight`.
- Multi-instructor catalog emails (about 25%): several instructors in one send, unified by a
  single reader outcome. For example `Stop leaving money on the table`, `The smarter way to manage
  your health`, `Stop hiding your greatest asset` (Pride), `Struggling to persuade people`, `We
  picked these for you`, the Mother's Day and Father's Day sale family.

Every multi-instructor email is the same architecture, reskinned: learn one template and you can
produce all of them. The engine had no equivalent of that template, it was built single-instructor
end to end. The most useful detail: the single-instructor emails use the identical three-card grid,
but the three cards are three lessons from one class, not three instructors. Same module, different
fill, which is why this was cheap to add to
[`scripts/email_render.py`](https://github.com/hostmaster-maharat/claude/blob/claude/laughing-dijkstra-0cx0tv/.claude/scripts/email_render.py).

## 2. The four multi-instructor archetypes

| Archetype | Example in the batch | What unifies the instructors | Shape |
|---|---|---|---|
| Themed roundup / digest | `The smarter way to manage your health`, `Stop leaving money on the table` | A reader outcome theme (manage your health, stop underearning) | Hero theme line, then 3 instructor "lesson" cards, then New / Coming Soon, then a Member Win |
| Occasion / moment | `Ends tonight: Get 50% off for Mother's Day`, `Stop hiding your greatest asset` (Pride) | A calendar or identity moment reframed to the reader | Same as digest, with an occasion hero and an "In this issue" index |
| Curated "picked for you" | `We picked these for you`, `Handpicked for you` | Personalization ("it's nice to feel seen, isn't it?") | 3 recommended classes across unrelated topics, then a membership CTA |
| Catalog sale | `Get 50% off select MasterClass products` | The offer itself (the discount) | Membership value bullets, then N product value-stacks, then one offer CTA |

The full method for each lives in
[`context/multi-instructor-angles.md`](https://github.com/hostmaster-maharat/claude/blob/claude/laughing-dijkstra-0cx0tv/.claude/context/multi-instructor-angles.md).

## 3. How they build one angle across many instructors

This is the method, and it is consistent across every multi-instructor email:

1. The umbrella is a reader outcome, never "here are 3 teachers." The hero states one thing the
   reader wants. The health email opens on "your body sends signals every day, most people do not
   know how to read them." The negotiation email opens on "ever walked out of a conversation
   wishing you had pushed harder for what you deserve."
2. Each instructor is cast as one lesson toward that outcome. The card headline is the outcome, the
   subline is the proof: "Prepare like a negotiator to claim your full value, with Chris Voss" or
   "Reclaim your time by doing less, with Cal Newport." The pattern is rigid: outcome-first verb
   headline, then "with [Name], [one credential line]", then a per-card link.
3. The grouping logic is always one of five: skill or topic cluster, occasion, identity or values
   moment, algorithmic recommendation, or catalog offer.
4. The lead-and-supporting-cast move: one email can give one instructor a full INSTRUCTOR SPOTLIGHT
   (a deeper "what you will do" block) while the others stay as compact cards.

These map to the strategy and copy work in
[`offer-and-angle`](https://github.com/hostmaster-maharat/claude/blob/claude/laughing-dijkstra-0cx0tv/.claude/skills/02-strategy-planning/offer-and-angle/SKILL.md)
and
[`email-copy`](https://github.com/hostmaster-maharat/claude/blob/claude/laughing-dijkstra-0cx0tv/.claude/skills/04-copywriting/email-copy/SKILL.md).

## 4. The reusable body skeleton (digest and occasion)

Observed in `The smarter way to manage your health`, `Stop leaving money on the table`, and `Ends
tonight: Get 50% off for Mother's Day`. The eyebrow labels are theirs.

1. Hero: the unifying outcome line, plus the primary CTA.
2. "In this issue": a numbered index (01 to 06) of the sections that follow, magazine style.
3. "Lessons for you": 3 instructor cards, each = outcome headline, "with [Name], [credential]",
   per-card link.
4. "Just for you": one more recommended class, single card.
5. "New and noteworthy": a new launch teaser.
6. "Coming soon": an upcoming class teaser.
7. "Member wins": one real testimonial, a reflective bridge line, the CTA.
8. Footer.

Structural devices worth keeping: a rule-of-three preheader that previews the three lessons; the
numbered "in this issue" index; the member testimonial that leads into the CTA; one primary CTA
with the per-card links as quiet secondaries. These became the three new build modules in
[`context/email-design-system.md`](https://github.com/hostmaster-maharat/claude/blob/claude/laughing-dijkstra-0cx0tv/.claude/context/email-design-system.md)
(LessonCardGrid, IssueIndex, MemberWin).

## 5. The promotional urgency ladder (a sequence the engine lacked)

The sale emails are one sequence with escalating urgency. The subjects, house-cleaned (originals
used em dashes), map a reusable promo arc:

| Step | Subject pattern in the batch | Role |
|---|---|---|
| 1 | "Father's Day sale starts now, get 50% off" | announce |
| 2 | "Get 50% off this Mother's Day" / "Get 50% off select products" | the offer, mid-window |
| 3 | "50% off select products ends tomorrow" | penultimate urgency |
| 4 | "Ends Tonight: Get 50% off select products" | final hours |
| 5 | "Extended: Get 50% off, ends tonight" | extension |
| 6 | "4 days left: 50% off for Father's Day" | countdown variant |

This became Pattern 6 PROMOTION in
[`sequence-standards.md`](https://github.com/hostmaster-maharat/claude/blob/claude/laughing-dijkstra-0cx0tv/.claude/skills/07-lifecycle-messaging/templates/sequence-standards.md)
and the
[`promo-sequence`](https://github.com/hostmaster-maharat/claude/blob/claude/laughing-dijkstra-0cx0tv/.claude/skills/07-lifecycle-messaging/promo-sequence/SKILL.md)
sub-skill.

## 6. Single-instructor anatomy (for contrast)

`NEW: Turn office tension into your next promotion` shows the single-instructor shape the engine
already builds: hero with a pain, then authority, then outcome, then three lesson cards drawn from
the one class, then the class CTA. Same three-card grid as the multi-instructor emails, filled with
lessons rather than instructors. The single-instructor angle types: "NEW" launch, "Coming soon"
teaser, "Launched last week" recency, a question or pain hook, an authority hook ("ask the person
who built it"), and a contrarian hook ("your instincts won't help you").

## 7. What not to borrow (these collide with the constitution)

| In the references | Maharat rule it breaks | Adaptation |
|---|---|---|
| Em dashes throughout | No em dashes, any language or file | Comma, colon, or period |
| "career-accelerating certificate courses", "AI-native business school" | Never imply accreditation | Outcome language only, no credentialing claim |
| Heavy specific credentials ("world's youngest self-made billionaire", "former FBI negotiator") | Claims discipline, catalog status | Keep "with [Name], [credential]", but every credential traces to a page-cleared fact and every named instructor is catalog-status-confirmed in [`_CATALOG.md`](https://github.com/hostmaster-maharat/claude/blob/claude/laughing-dijkstra-0cx0tv/.claude/context/instructors/_CATALOG.md) |
| "200+ classes", "200+ iconic instructors" | No invented values | Use the real catalog count from context, or omit |
| Multiple competing CTAs | One primary CTA per email | One primary join or offer CTA, per-card links are quiet secondaries |

One habit worth considering: MasterClass discloses "this email was in part generated by AI and then
fact-checked by humans."

## 8. The gap, and what this adds

The engine was single-instructor end to end. What shipped on this branch closes the gap:

- The angle method: [`context/multi-instructor-angles.md`](https://github.com/hostmaster-maharat/claude/blob/claude/laughing-dijkstra-0cx0tv/.claude/context/multi-instructor-angles.md), wired into [`offer-and-angle`](https://github.com/hostmaster-maharat/claude/blob/claude/laughing-dijkstra-0cx0tv/.claude/skills/02-strategy-planning/offer-and-angle/SKILL.md) and [`email-copy`](https://github.com/hostmaster-maharat/claude/blob/claude/laughing-dijkstra-0cx0tv/.claude/skills/04-copywriting/email-copy/SKILL.md).
- The PROMOTION lifecycle pattern: Pattern 6 in [`sequence-standards.md`](https://github.com/hostmaster-maharat/claude/blob/claude/laughing-dijkstra-0cx0tv/.claude/skills/07-lifecycle-messaging/templates/sequence-standards.md) plus the [`promo-sequence`](https://github.com/hostmaster-maharat/claude/tree/claude/laughing-dijkstra-0cx0tv/.claude/skills/07-lifecycle-messaging/promo-sequence) sub-skill.
- Three build modules (LessonCardGrid, IssueIndex, MemberWin) in [`email-design-system.md`](https://github.com/hostmaster-maharat/claude/blob/claude/laughing-dijkstra-0cx0tv/.claude/context/email-design-system.md), the slot contract [`email-module-map.md`](https://github.com/hostmaster-maharat/claude/blob/claude/laughing-dijkstra-0cx0tv/.claude/runtime/email-module-map.md), and the renderer [`email_render.py`](https://github.com/hostmaster-maharat/claude/blob/claude/laughing-dijkstra-0cx0tv/.claude/scripts/email_render.py).
- The natural Maharat vehicle already exists: Skill Paths (bundles across instructors) and any cross-catalog or occasion promotion. The guardrail "do not invent Skill Path titles or the content lineup" applies directly.

Operational consequence, recorded in [`verification.md`](https://github.com/hostmaster-maharat/claude/blob/claude/laughing-dijkstra-0cx0tv/.claude/runtime/verification.md): a multi-instructor email multiplies the instructor gate. Every named instructor must be catalog-status-confirmed and every credential page-cleared, or that card is dropped. This is stricter than a single-instructor send.

## 9. Full-corpus re-analysis (all 7 batches, about 180 emails)

The full corpus confirmed the architecture at scale and surfaced new patterns batch 1 alone did
not show. Verdict: the shipped capability holds, the additions below extend it, nothing is walked
back.

Confirmed at scale: the themed-digest skeleton, the rigid `with [Name], [credential]` card formula,
the LessonCardGrid / IssueIndex / MemberWin modules, and the promo urgency ladder all recur dozens
of times.

New, now folded into the engine:
- The dominant multi-instructor format is a subject-led "3 [ways or lessons] to [outcome]" digest.
  The subject is the umbrella outcome plus the card count. Added to
  [`context/multi-instructor-angles.md`](https://github.com/hostmaster-maharat/claude/blob/claude/laughing-dijkstra-0cx0tv/.claude/context/multi-instructor-angles.md)
  and the [subject-lines](https://github.com/hostmaster-maharat/claude/blob/claude/laughing-dijkstra-0cx0tv/.claude/skills/04-copywriting/subject-lines/templates/subject-lines.md) template.
- Co-taught class (two instructors, one class), distinct from the N-class digest: one Hero plus one
  BodyCopy naming both, never a grid. Added to the angle method.
- Single-instructor launch templates: the first-person personal-voice letter, the
  "Meet your new instructor" announcement, and the "Start your session" activation nudge. Added to
  [`newsletter-patterns.md`](https://github.com/hostmaster-maharat/claude/blob/claude/laughing-dijkstra-0cx0tv/.claude/skills/04-copywriting/email-copy/templates/newsletter-patterns.md)
  and the `/email-mockup` archetypes.
- Gifting and referral: give-a-membership aimed at existing members (a new audience), often tied to
  an occasion. Added as a grouping logic and a PROMOTION variant.
- A richer occasion calendar and urgency vocabulary, mapped to Maharat-relevant moments. Added to
  the PROMOTION pattern.

New, deliberately NOT built (compliance-gated):
- Contest, sweepstakes, and prize draws ("win a session with an instructor"). Real and common in
  the corpus, but for Maharat they need Saudi PDPL, contest and sweepstakes law, eligibility, and
  entry-data handling cleared by `compliance-privacy-reviewer` first. Documented as not-buildable
  in the angle method; no contest email is produced until cleared.

The capability is now also operable as one prompt: the
[`/email-mockup`](https://github.com/hostmaster-maharat/claude/blob/claude/laughing-dijkstra-0cx0tv/.claude/commands/email-mockup.md)
command builds an HTML mockup for any archetype from the primitives, blocks, templates, Ortto
section ids, and rules, with a worked example at
[`examples/multi-instructor-digest/`](https://github.com/hostmaster-maharat/claude/tree/claude/laughing-dijkstra-0cx0tv/.claude/skills/05-build-launch/email-html-build/examples/multi-instructor-digest).

---

## Update, 2026-06-19: what shipped

The findings above are now a reusable capability on branch `claude/laughing-dijkstra-0cx0tv`,
campaign-agnostic, inventing no offer, title, or instructor. 23 files, additive, house-style clean,
nothing sends. Verified: the renderer produces a clean AR and EN digest (one primary CTA, quiet
per-card secondaries, RTL and LTR correct, Western numerals, unique copy-ids), existing specs
render unchanged, and the house-style sweep passes across every changed file.

Reference and method
- [`references/2026-06-masterclass-multiinstructor-teardown.md`](https://github.com/hostmaster-maharat/claude/blob/claude/laughing-dijkstra-0cx0tv/.claude/references/2026-06-masterclass-multiinstructor-teardown.md): this doc.
- [`context/multi-instructor-angles.md`](https://github.com/hostmaster-maharat/claude/blob/claude/laughing-dijkstra-0cx0tv/.claude/context/multi-instructor-angles.md): the canonical angle method (5 grouping logics, the umbrella-outcome rule, the LessonCard formula, the lead-and-supporting-cast spotlight, brand adaptations, the CTA reconciliation).

Lifecycle, the PROMOTION pattern
- [`skills/07-lifecycle-messaging/templates/sequence-standards.md`](https://github.com/hostmaster-maharat/claude/blob/claude/laughing-dijkstra-0cx0tv/.claude/skills/07-lifecycle-messaging/templates/sequence-standards.md): Pattern 6 PROMOTION and the selector row.
- [`skills/07-lifecycle-messaging/promo-sequence/`](https://github.com/hostmaster-maharat/claude/tree/claude/laughing-dijkstra-0cx0tv/.claude/skills/07-lifecycle-messaging/promo-sequence): the sub-skill ([SKILL](https://github.com/hostmaster-maharat/claude/blob/claude/laughing-dijkstra-0cx0tv/.claude/skills/07-lifecycle-messaging/promo-sequence/SKILL.md), [template](https://github.com/hostmaster-maharat/claude/blob/claude/laughing-dijkstra-0cx0tv/.claude/skills/07-lifecycle-messaging/promo-sequence/templates/promo-sequence.md), [evals](https://github.com/hostmaster-maharat/claude/blob/claude/laughing-dijkstra-0cx0tv/.claude/skills/07-lifecycle-messaging/promo-sequence/evals/evals.json)).
- [`skills/07-lifecycle-messaging/SKILL.md`](https://github.com/hostmaster-maharat/claude/blob/claude/laughing-dijkstra-0cx0tv/.claude/skills/07-lifecycle-messaging/SKILL.md) and the [lifecycle-architect](https://github.com/hostmaster-maharat/claude/blob/claude/laughing-dijkstra-0cx0tv/.claude/agents/lifecycle-architect.md) agent: the new pattern wired into the selector and the agent's reads.

Strategy and copy
- [`skills/02-strategy-planning/offer-and-angle/SKILL.md`](https://github.com/hostmaster-maharat/claude/blob/claude/laughing-dijkstra-0cx0tv/.claude/skills/02-strategy-planning/offer-and-angle/SKILL.md) and its [template](https://github.com/hostmaster-maharat/claude/blob/claude/laughing-dijkstra-0cx0tv/.claude/skills/02-strategy-planning/offer-and-angle/templates/angle-and-offer-framing.md): the multi-instructor angle as a campaign angle.
- [`skills/04-copywriting/email-copy/SKILL.md`](https://github.com/hostmaster-maharat/claude/blob/claude/laughing-dijkstra-0cx0tv/.claude/skills/04-copywriting/email-copy/SKILL.md) and [`newsletter-patterns.md`](https://github.com/hostmaster-maharat/claude/blob/claude/laughing-dijkstra-0cx0tv/.claude/skills/04-copywriting/email-copy/templates/newsletter-patterns.md): the digest copy shape and the one-primary-CTA reconciliation; the old second-hand study now points at this primary-source work.

Build modules (renderer-native, MJML mirrored)
- [`context/email-design-system.md`](https://github.com/hostmaster-maharat/claude/blob/claude/laughing-dijkstra-0cx0tv/.claude/context/email-design-system.md), [`runtime/email-module-map.md`](https://github.com/hostmaster-maharat/claude/blob/claude/laughing-dijkstra-0cx0tv/.claude/runtime/email-module-map.md), [`email-html-structure.md`](https://github.com/hostmaster-maharat/claude/blob/claude/laughing-dijkstra-0cx0tv/.claude/skills/05-build-launch/email-html-build/templates/email-html-structure.md): the three digest modules added to the library and the slot contract.
- [`scripts/email_render.py`](https://github.com/hostmaster-maharat/claude/blob/claude/laughing-dijkstra-0cx0tv/.claude/scripts/email_render.py): three additive module renderers; existing specs render unchanged.
- [`14-lessoncardgrid.mjml`](https://github.com/hostmaster-maharat/claude/blob/claude/laughing-dijkstra-0cx0tv/.claude/skills/05-build-launch/email-html-build/mjml/components/14-lessoncardgrid.mjml), [`15-issueindex.mjml`](https://github.com/hostmaster-maharat/claude/blob/claude/laughing-dijkstra-0cx0tv/.claude/skills/05-build-launch/email-html-build/mjml/components/15-issueindex.mjml), [`16-memberwin.mjml`](https://github.com/hostmaster-maharat/claude/blob/claude/laughing-dijkstra-0cx0tv/.claude/skills/05-build-launch/email-html-build/mjml/components/16-memberwin.mjml): MJML fragments mirroring the renderer.

Guardrail
- [`runtime/verification.md`](https://github.com/hostmaster-maharat/claude/blob/claude/laughing-dijkstra-0cx0tv/.claude/runtime/verification.md): the multiplied instructor gate for multi-instructor emails.

The mockup command and the full-corpus additions (2026-06-19, batches 2 to 7)
- [`commands/email-mockup.md`](https://github.com/hostmaster-maharat/claude/blob/claude/laughing-dijkstra-0cx0tv/.claude/commands/email-mockup.md): the `/email-mockup` prompt that builds an HTML mockup from the primitives, blocks, templates, Ortto section ids, and rules, for any archetype.
- [`examples/multi-instructor-digest/`](https://github.com/hostmaster-maharat/claude/tree/claude/laughing-dijkstra-0cx0tv/.claude/skills/05-build-launch/email-html-build/examples/multi-instructor-digest): a rendered, swept worked example (the "3 ways to X" digest).
- [`context/multi-instructor-angles.md`](https://github.com/hostmaster-maharat/claude/blob/claude/laughing-dijkstra-0cx0tv/.claude/context/multi-instructor-angles.md): the "3 X to Y" subject formula, the co-taught vs digest distinction, the gifting logic, and the compliance-gated contest note.
- [`newsletter-patterns.md`](https://github.com/hostmaster-maharat/claude/blob/claude/laughing-dijkstra-0cx0tv/.claude/skills/04-copywriting/email-copy/templates/newsletter-patterns.md) and [`subject-lines.md`](https://github.com/hostmaster-maharat/claude/blob/claude/laughing-dijkstra-0cx0tv/.claude/skills/04-copywriting/subject-lines/templates/subject-lines.md): the single-instructor launch templates and the subject patterns by archetype.
- [`sequence-standards.md`](https://github.com/hostmaster-maharat/claude/blob/claude/laughing-dijkstra-0cx0tv/.claude/skills/07-lifecycle-messaging/templates/sequence-standards.md): the occasion calendar, the urgency vocabulary, and the gifting variant in PROMOTION.

Links point to the `claude/laughing-dijkstra-0cx0tv` branch, where every path resolves now; `main`
was left untouched (it is behind this branch, and advancing it is a separate, approved step).
Nothing here sends: output stops at the gate stack and the human gate.
