---
name: content-distribution
description: Repurpose one article into email, organic-social, and other formats, and route each to its owner. Use when a published or planned article needs a distribution and repurposing plan, triggers on "content distribution," "repurpose the article," "distribute the content," "turn the article into," "atomize the content," "content into social and email." Produces the content-package distribution_plan and routes to organic-social and lifecycle owners.
---

# Content distribution (sub-skill of content-marketing)

Takes one article and plans how it becomes many formats: an email, organic-social posts, and
other derivatives, then routes each to the owner who produces it. The content-marketer plans
the repurposing, the destination owners and copywriters produce the final pieces. Assembled
into the `content-package` by the content-marketing hub.

## Purpose

Get full value from each article by atomizing it into the formats the audience meets across
owned channels, without duplicating effort or losing the angle. One source, many touchpoints.
One machine, any campaign.

## When to use

- An article is planned or published and needs a repurposing and distribution plan.
- One source piece should feed email, organic social, and other owned formats.

## Inputs

- The article_brief or the published article: target query, outline, CTA.
- The `strategy-artifact`: angle and segments, so each format keeps the message.
- `context/04-tools-and-access.md`: which owned channels exist (only approved tools).
- `context/brand-voice.md`: voice and the hard mechanical rules.

## Steps

1. Pull the article's core angle and CTA, the spine every derivative keeps.
2. List the derivative formats: email, organic-social posts, and others the channels support.
3. For each format, note the angle it carries, the CTA, and the owner who produces it:
   email to lifecycle-architect and copywriter-ar or copywriter-en, social to organic-social.
4. Sequence the distribution: what goes out, where, and in what order around the article.
5. Keep copy production with the owners. This skill routes and briefs, it does not write the
   final email or caption copy.
6. Flag any format that would need an unconfirmed offer, price, or Skill Path title, and stop
   and ask rather than inventing one.

## Output

The `content-package` distribution_plan:

```
source         the article_brief id or published URL
derivatives[]  each: format (email | organic-social | other), angle_carried, cta,
               owner, language (ar | en), routing_notes
sequence       the order and timing of the derivatives around the article
notes          channels unavailable, values blocked on the brief
```

See `templates/content-distribution-plan.md`.

## Hard rules

- One source angle carried across every derivative. English-first, English in parallel.
- This skill routes and briefs, it does not write final email or caption copy. That copy is
  authored by the destination owners and copywriters and runs its own gate stack.
- No em dashes. No tatweel. Western numerals only.
- Never invent an offer, price, Skill Path title, or instructor name. If a derivative needs one
  and the brief is silent, stop and ask. Never imply certificate accreditation.
- Do not adopt a distribution tool without approval, per CLAUDE.md principle 3.

## How it connects

Feeds the content-marketing hub's distribution_plan, and routes derivatives to organic-social
(for the `organic-package`) and to lifecycle-architect and the copywriters (for the
`copy-package` and `lifecycle-package`). Each authored derivative runs the gate stack at its
own owner, per `runtime/verification.md`.
