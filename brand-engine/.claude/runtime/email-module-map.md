# email-module-map.md: the slot contract for built emails

This is the binding contract between QA-passed copy, reviewed assets, and the built email
HTML. It exists so a built email is three things at once: a brand-correct render, an
Ortto-editable asset, and a gate-traceable artifact where every word and every image points
back to the QA that cleared it. The visual standard lives in `context/profiles/maharat/email-design-system.md`.
This file defines how the parts are tagged and routed.

No em dashes. Western numerals only. English-first. RTL is the default direction.

## The one rule everything else serves

Emails are built from live modules, never as one flat image. Every line of copy is live HTML
text in a copy slot. Every image is text-free. This is what makes an email QA-able by the
copy and asset gates, accessible, RTL-correct, and editable in the platform. An image-only
send (copy baked into a picture) is a hard fail, it cannot pass the gates and does not ship.

## The slot attributes

Every module-bearing cell carries a small, fixed set of data attributes. They are the seams
the platform and the gates read.

| Attribute | Values | Meaning |
|---|---|---|
| `data-ortto-module` | `paragraph` `heading` `text` `image` `button` `social` `divider` | the Ortto module type the cell maps to |
| `data-slot` | `copy` `element` `structural` | what kind of content the cell holds, and which gate owns it |
| `data-role` | `preheader` `eyebrow` `headline` `body` `list` `cta` `eventdetails` `billing` `card-name` `card-subject` `card-headline` `card-credential` `card-cta` `index` `quote` | the role the content plays |
| `data-lang` | `ar` `en` | the language of a copy slot, the routing key for copy QA |
| `data-copy-id` | a `copy-package` variant id | the QA-passed copy this slot renders, never free copy |
| `data-link-slot` | a URL | the destination for a `cta` or linked element, no personal data in the URL |

## What each `data-slot` means, and who gates it

- `copy`: live customer-facing text (preheader, eyebrow, headline, body, list, cta label).
  Binds to a QA-passed `copy-package` variant by `data-copy-id` and carries `data-lang`. It
  is never written into the template by hand. It routes to its language copy gate:
  `data-lang="ar"` goes to `arabic-copy-qa`, `data-lang="en"` goes to `english-copy-qa`.
- `element`: an image or visual (logo, hero, feature image, class card, social icon). It
  routes to `email-asset-qa` (the asset and visual gate, owned by `email-asset-reviewer`).
  Every `element` carries real `alt` text and is text-free.
- `structural`: chrome with no customer-facing copy of its own (view-in-browser link,
  dividers, the www line, the unsubscribe link, layout tables). No copy gate, but it still
  passes the house-style sweep and `compliance-privacy-check` (unsubscribe present, links clean).

## The module library, mapped

The visual definition of each module is in `context/profiles/maharat/email-design-system.md`. Here is how the
16 modules carry slots (the 12+1 core plus the 3 multi-instructor digest modules). A built email
composes only from this set.

| Module | `data-ortto-module` | `data-slot` | typical `data-role` | gate |
|---|---|---|---|---|
| LogoBar | image | element | (none) | email-asset-qa |
| Hero | image | element | (none, text-free) | email-asset-qa |
| SectionHeading | heading | copy | eyebrow + headline | language copy QA |
| BodyCopy | paragraph | copy | body | language copy QA |
| Button | button | copy | cta (+ `data-link-slot`) | language copy QA |
| PromoLine | text | copy | body (code chip is structural) | language copy QA |
| Divider | divider | structural | (none) | house style only |
| ListBlock | text | copy | list | language copy QA |
| ClassCardGrid | image | element | (none, 3 linked covers) | email-asset-qa |
| FeatureImage | image | element | (none, text-free) | email-asset-qa |
| EventDetails | text | copy | eventdetails | language copy QA |
| BillingNotice | paragraph | copy | billing | language copy QA |
| Footer | social + structural | element + structural | (none) | email-asset-qa (icons) + house style |
| LessonCardGrid | image + text | element + copy | card-headline + card-credential + card-cta | email-asset-qa (portraits) + language copy QA (headline, credential, link label) |
| IssueIndex | text | copy | index | language copy QA |
| MemberWin | text | copy | quote + body | language copy QA |

The last three are the multi-instructor digest modules (`context/profiles/maharat/email-design-system.md`, the
extension set). LessonCardGrid is the only mixed module whose cells split between `element` (the
text-free portrait, to `email-asset-qa`) and `copy` (the outcome headline, the credential line,
and the secondary link label, to language copy QA). Because it names instructors, every card is
also blocked until that instructor's catalog status is confirmed and its credential is
page-cleared (see "Claims and catalog status" below); an unconfirmed instructor's card is dropped.

Text-on-image, where a headline sits over a hero, is built as a live copy slot positioned
over a text-free `element` background (a background image with a VML fallback for Outlook),
never as text baked into the picture.

## How a built email maps to the gate stack

The build is one asset with many slots. The gates run per `runtime/verification.md`, routed by
slot:

1. Skill eval: the `email-html-build` eval (structure, every copy slot bound to a `data-copy-id`,
   one primary `cta`, slot attributes well formed, house-style sweep clean).
2. Language copy QA, per copy slot by `data-lang`: Arabic slots to `arabic-copy-qa`, English
   slots to `english-copy-qa`. A bilingual email passes both for its respective slots. A copy
   slot whose `data-copy-id` is not QA-passed blocks the build.
3. Asset and visual QA: every `element` slot to `email-asset-qa`.
4. Accessibility QA (`accessibility-qa`): the email render.
5. Compliance and privacy (`compliance-privacy-check`): the send, suppression, links, unsubscribe.
6. Brand QA (`brand-qa-reviewer`): last, the whole assembled email.
7. Human gate: nothing sends without Ahmed, per action and per campaign.

## Assets and hosting

Email images come from the approved Ortto CDN (`m.autopilotapp.com`, `ic.autopilotapp.com`),
where Maharat's real, rights-cleared creative lives, or are uploaded there at build. Raw Google
Drive links and hotlink-protected CloudFront objects are not email-safe (a direct fetch can
return 403), so an asset is staged to the CDN, never hot-linked from Drive. Sourcing and rights
are checked by `email-asset-qa`.

## Claims and catalog status

An email that names or pictures an instructor is blocked until the instructor's catalog status
is confirmed (`context/profiles/maharat/instructor-packs`), and it carries only page-cleared facts plus
voice.md verified-safe beliefs. Held-back claims stay out until cleared.
