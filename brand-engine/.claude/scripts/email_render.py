#!/usr/bin/env python3
"""
email_render.py: render QA-passed Maharat email copy into the SLOTTED component HTML.

Upgraded to the Maharat email standard (live-components, the "Elda reference" build):
context/email-design-system.md (tokens, the 12+1 core component library plus the 3 multi-instructor
digest modules, brand fonts, themes) and runtime/email-module-map.md (the data-ortto-module /
data-slot / data-role / data-lang / data-copy-id / data-link-slot contract and the gate routing).

Campaign-agnostic. Reads a JSON email spec (the render-ready form of QA-passed copy, with stable
data-copy-id values per slot) and writes one self-contained, slotted .html per email, plus an
index.html preview sheet. Stdlib only. Mirrors the house-style sweep by code point: no em dash,
no en dash, no tatweel, Western numerals only, so this source file carries no literal forbidden
character.

What "slotted" means here, versus the old flat render:
- Every line of copy is a LIVE HTML text slot (data-slot="copy") bound to a data-copy-id from the
  spec, tagged data-lang. Copy is never baked into an image.
- Every image is text-free (data-slot="element") with descriptive alt. The hero is the
  campaign/email hero_image (the manifest's verified header), language-matched: hero_image.src_ar
  (the AR-page / RIGHTGRADIENT cover) on AR emails, hero_image.src_en (the EN-page / LEFTGRADIENT
  cover) on EN emails, falling back to a language-neutral hero_image.src. Class covers live on
  CloudFront and are the verified design proof; they still stage to the Ortto CDN before send.
- Brand fonts (Lyon Arabic Display + 29LT Azer for AR, Acumin Pro for EN) are delivered via the
  Ortto-hosted custom-fonts CSS links in the head, the ar2 reference pattern. No binary is
  embedded or committed.
- One primary CTA per email: an MSO VML roundrect for Outlook plus a non-mso pill, near-black
  #141414 label on emerald #009975 (about 5:1, clears WCAG AA).
- Sender identity and an unsubscribe link in every email. The footer social icons are the getbee
  set; the unsubscribe href is the platform merge tag.

The 7-step "account-created to activation" components, per email-design-system.md:
- SectionHeading (eyebrow + headline), BodyCopy, ListBlock ("what you will learn" / steps,
  emerald bullets), ClassCardGrid (three OTHER PORTRAIT instructor cards: a text-free on-brand
  #141414 portrait with the name + "Teaches <subject>" as a live HTML overlay, ONLY status-cleared,
  rights-cleared, else omitted), FeatureImage (a single text-free image), PromoLine (a code chip +
  urgency line, ONLY when the spec carries a real code, never invented), and the single primary
  Button.

Per-email module selection is driven by the spec: each email may carry a "modules" list naming the
ordered body blocks to emit between the SectionHeading and the CTA (for example
["body", "list", "feature", "promo"]). When "modules" is absent, the renderer infers a sensible
default from the keys the email provides (body, then list if list_items, then feature if
feature_image, then promo if promo). The header (logo, hero, eyebrow, headline), the single CTA,
and the footer are always emitted. The "our other classes" ClassCardGrid renders as a bottom row
after the CTA, only when the spec supplies three status-cleared, rights-cleared portrait cards
(top-level "class_cards" or per-email "class_cards"). Each card carries a text-free portrait
(portrait_src, or a rare language-split portrait_src_ar / portrait_src_en), the instructor name
(name_ar / name_en), the subject phrase (subject_ar / subject_en, the page-cleared "Teaches X" /
"يعلّم X"), a language-matched class-page link (link_ar / link_en), and a descriptive alt. The name
and subject are LIVE HTML over the dark lower third, never baked into the portrait. The three are
OTHER classes, never the email's own.

The multi-instructor digest modules (LessonCardGrid, IssueIndex, MemberWin) extend this for
multi-instructor and catalog emails (a Skill Path, a themed roundup, an occasion sale, a
recommendation), per context/multi-instructor-angles.md. LessonCardGrid is the in-body offer grid:
each card casts one instructor as one lesson toward the email's umbrella outcome (an outcome
headline, a "with <Name>, <credential>" line, and a quiet secondary link, never a second pill).
IssueIndex is an optional numbered table of contents; MemberWin is one real, consented testimonial
that leads into the primary CTA. Each renders only when the spec supplies its data (lesson_cards,
issue_index, member_win), so a spec without these keys is unaffected. Every per-card credential
must trace to a page-cleared fact and every named instructor must be catalog-status-confirmed, or
the author drops that card before render.

The spec never carries a price, plan, or any value not in the brief. The renderer invents nothing.
Nothing here sends: the output is approval-ready, slotted HTML that stops at the gate stack and the
human gate. The committed slotted HTML is the source of truth; the MJML library under
skills/05-build-launch/email-html-build/mjml/ compiles to match it.

Usage:
    python3 .claude/scripts/email_render.py <spec.json> [--out <dir>]
    python3 .claude/scripts/email_render.py <spec.json> --check   # sweep only, write nothing
"""

import argparse
import html
import json
import re
import sys
from pathlib import Path

# The email asset pipeline map (the GitHub-to-Ortto source-to-serve record). The serve URL is
# resolved from here: an image src becomes its ortto_serve_url when the map marks that source
# 'served', otherwise the src is left as the CloudFront cover (the verified design proof for
# preview). Today every row is pending, so this is behavior-preserving; the live src flips to Ortto
# per image as each row is served, with no renderer change. See
# context/profiles/maharat/instructors/_EMAIL-ASSET-PIPELINE.md and scripts/email_asset_pipeline.py.
_PIPELINE_MAP_PATH = (Path(__file__).resolve().parents[1]
                      / "context" / "instructors" / "email-asset-pipeline.json")
_SERVE_BY_SOURCE = None  # lazy {source_url: ortto_serve_url} for rows whose status is 'served'


def _serve_table():
    """Lazy-load {source_url: ortto_serve_url} for every map row marked status 'served'.

    Campaign-agnostic and optional: a missing or unreadable map yields an empty table (the
    CloudFront src is used as the preview fallback). Only rows that are actually served populate it.
    """
    global _SERVE_BY_SOURCE
    if _SERVE_BY_SOURCE is not None:
        return _SERVE_BY_SOURCE
    table = {}
    try:
        data = json.loads(_PIPELINE_MAP_PATH.read_text(encoding="utf-8"))
        for row in data.get("images", []):
            url = row.get("ortto_serve_url", "pending")
            if row.get("status") == "served" and url and url != "pending":
                src = row.get("source", "")
                if src:
                    table[src] = url
    except (OSError, ValueError):
        table = {}
    _SERVE_BY_SOURCE = table
    return table


def _serve_src(src):
    """Resolve an image src to its Ortto serve URL when the map marks that source 'served'.

    Falls back to the given src (the CloudFront cover) unchanged when the source is not in the map
    or not yet served. This keeps preview rendering on the verified CloudFront proof until Ortto
    serves the bytes, then flips to the Ortto URL with no other change.
    """
    if not src:
        return src
    return _serve_table().get(src, src)

# Forbidden set, same as scripts/pack_check.py and scripts/house_style_sweep.py: em dash, en dash,
# tatweel, and the Arabic-Indic and extended Arabic-Indic numerals. Built by code point so this
# source file carries no literal forbidden character.
FORBIDDEN = re.compile(
    "[" + chr(0x2014) + chr(0x2013) + chr(0x0640)
    + chr(0x0660) + "-" + chr(0x0669)
    + chr(0x06F0) + "-" + chr(0x06F9) + "]"
)

# Brand visual constants (context/brand-voice.md, context/email-design-system.md). Constitution
# only. The pending gold #C4963C and panel #1c1c1c are NOT used in customer-facing email.
BG = "#141414"       # paper
CARD = "#1A1A1A"     # panel
ACCENT = "#009975"   # emerald (one per email)
INK = "#FFFFFF"      # headline on dark
BODY = "#E6E6E6"     # body on dark
MUTE = "#B9B9B9"      # fine print (lightened to clear WCAG AA on #141414)
FAINT = "#B3B3B3"    # footer legal (lightened to clear WCAG AA on #141414)
RULE = "#262626"     # hairline divider
CTA_TEXT = INK       # white CTA label on emerald (owner-directed; see note: below WCAG AA on #009975)

# Brand fonts via the Ortto-hosted custom-fonts CSS. Stacks per email-design-system.md.
FONT_AR = "'Lyon Arabic Display','29LT Azer',Tahoma,Arial,sans-serif"
FONT_EN = "'Acumin Pro',Arial,sans-serif"
CSS_LYON = "https://accounts-api-us.ortto.app/-/settings/custom-fonts.css?family=Lyon+Arabic+Display&k=bWFoYXJhdA"
CSS_ACUMIN = "https://accounts-api-us.ortto.app/-/settings/custom-fonts.css?family=Acumin+Pro&k=bWFoYXJhdA"

LOGO = "https://m.autopilotapp.com/maharat/logo/l_80b9b5a2-f18b-4bc7-a859-2cf899449f05.png"
SOCIAL = [
    ("facebook", "https://www.facebook.com/people/Maharat/100090569760903/",
     "https://app-rsrc.getbee.io/public/resources/social-networks-icon-sets/t-outline-circle-white/facebook@2x.png"),
    ("instagram", "https://www.instagram.com/maharatarabia/",
     "https://app-rsrc.getbee.io/public/resources/social-networks-icon-sets/t-outline-circle-white/instagram@2x.png"),
    ("twitter", "https://twitter.com/maharatarabia/",
     "https://app-rsrc.getbee.io/public/resources/social-networks-icon-sets/t-outline-circle-white/twitter@2x.png"),
    ("linkedin", "https://www.linkedin.com/company/maharatarabia/",
     "https://app-rsrc.getbee.io/public/resources/social-networks-icon-sets/t-outline-circle-white/linkedin@2x.png"),
]
SOCIAL_ALT = {
    "ar": {"facebook": "فيسبوك", "instagram": "إنستغرام", "twitter": "إكس", "linkedin": "لينكدإن"},
    "en": {"facebook": "Facebook", "instagram": "Instagram", "twitter": "X", "linkedin": "LinkedIn"},
}
STRINGS = {
    "ar": {"view": "اعرض في المتصفح", "unsub": "إلغاء الاشتراك",
           "sender": "مهارات للتعليم، ص.ب 77983، أبوظبي، الإمارات العربية المتحدة"},
    "en": {"view": "View in browser", "unsub": "Unsubscribe",
           "sender": "Maharat for Education, P.O Box 77983, Abu Dhabi, United Arab Emirates"},
}

esc = html.escape


def cid(e, role, camp):
    """Stable data-copy-id for a slot: <base>-<id>-<role>-<lang>, or campaign-stable for shared roles.

    The base is campaign-agnostic: the email's copy_id_base, else the spec's copy_id_base, else a
    slug derived from the campaign_id. Eyebrow and the footer sender line are campaign-stable
    (<base>-<role>-<lang>); everything else is per-email (<base>-<id>-<role>-<lang>).
    """
    shared = {"eyebrow", "footer-sender"}
    base = e.get("copy_id_base") or camp.get("copy_id_base") or _slug_base(camp)
    if role in shared:
        return f"{base}-{role}-{e['lang']}"
    return f"{base}-{e['id']}-{role}-{e['lang']}"


def _slug_base(camp):
    """A stable copy-id base from the campaign_id, campaign-agnostic. 'email-<slug>'."""
    raw = str(camp.get("copy_id_slug") or camp.get("campaign_id") or "campaign")
    slug = re.sub(r"[^a-z0-9]+", "-", raw.lower()).strip("-")
    return "email-" + slug


def _para(text):
    """Split a body line on a blank-line marker into <br><br>-joined live text, escaped."""
    if isinstance(text, str):
        text = [text]
    return "<br><br>".join(esc(t) for t in text)


def _doc_comment(e, camp, lang, rtl):
    """Campaign-agnostic provenance comment, driven by spec fields. No hard-coded instructor."""
    title = camp.get("campaign_title", camp.get("campaign_id", ""))
    src = camp.get("generated_from", "the QA-passed copy spec")
    status = camp.get("status", "draft, not approved, nothing sends")
    catalog = camp.get("catalog_status_note",
                       "blocked on catalog status (the roster is unconfirmed in _CATALOG.md)")
    hero_note = camp.get("hero_deliverability_note", "")
    c = []
    c.append('<!--')
    c.append('  ' + esc(title) + ', ' + e["id"].upper() + ' (' + esc(e.get("name", "")) + '), '
             + lang.upper() + ' (' + ("RTL" if rtl else "LTR") + '). INTERNAL DRAFT.')
    c.append('  Status: ' + esc(status) + '. ' + esc(catalog) + '.')
    c.append('  Slotted live-component build per context/email-design-system.md + runtime/email-module-map.md.')
    c.append('  Every word is a live copy slot bound to a data-copy-id from ' + esc(src) + ' (NOT rewritten).')
    if hero_note:
        c.append('  Header: ' + esc(hero_note))
    c.append('  Generated by scripts/email_render.py from the spec.json (the source of truth). Nothing sends.')
    c.append('-->')
    return c


def _heading(text, lang, font, align, size, pad):
    """A secondary in-body heading (a ListBlock title, a ClassCardGrid title). Live copy slot."""
    return ('<tr><td data-ortto-module="heading" data-slot="copy" data-role="headline" data-lang="' + lang
            + '" class="px ' + ("ar" if lang == "ar" else "en")
            + '" style="padding:' + pad + ';color:' + INK + ';font-size:' + str(size)
            + 'px;font-weight:700;line-height:1.4;text-align:' + align + ';font-family:' + font + ';">'
            + '<h2 style="margin:0;font-size:' + str(size) + 'px;font-weight:700;line-height:1.4;color:' + INK
            + ';font-family:' + font + ';">' + esc(text) + '</h2></td></tr>')


def _block_body(e, camp, lang, font, align):
    """BodyCopy (copy slot)."""
    return ('<tr><td data-ortto-module="paragraph" data-slot="copy" data-role="body" data-lang="' + lang
            + '" data-copy-id="' + cid(e, "body", camp) + '" class="px ' + ("ar" if lang == "ar" else "en")
            + '" style="padding:0 40px 14px;color:' + BODY + ';font-size:15px;line-height:1.85;text-align:'
            + align + ';">' + _para(e["body"]) + '</td></tr>')


def _block_list(e, camp, lang, font, align):
    """ListBlock (copy slot): emerald-bullet 'what you will learn' or steps. Optional title."""
    items = e.get("list_items") or []
    if not items:
        return ""
    out = []
    title = e.get("list_title")
    if title:
        out.append(_heading(title, lang, font, align, 20, "6px 40px 10px"))
    rows = ('<ul role="list" style="margin:0;padding:0;list-style:none;">'
            + "".join('<li style="padding:5px 0;"><span class="bul" aria-hidden="true">&bull;</span>&nbsp;&nbsp;'
                      + esc(li) + '</li>' for li in items)
            + '</ul>')
    out.append('<tr><td data-ortto-module="text" data-slot="copy" data-role="list" data-lang="' + lang
               + '" data-copy-id="' + cid(e, "list", camp) + '" class="px ' + ("ar" if lang == "ar" else "en")
               + '" style="padding:0 40px 8px;color:' + BODY + ';font-size:15px;line-height:1.7;text-align:'
               + align + ';">' + rows + '</td></tr>')
    return "".join(out)


def _block_feature(e, camp, lang):
    """FeatureImage (element): a single 600 wide, text-free, rights-cleared image, radius 16."""
    fi = e.get("feature_image")
    if not fi or not fi.get("src"):
        return ""
    link = fi.get("link", "")
    img = ('<img src="' + esc(_serve_src(fi["src"])) + '" width="552" alt="' + esc(fi.get("alt", ""))
           + '" style="display:block;width:100%;max-width:552px;height:auto;border-radius:16px;margin:0 auto;">')
    inner = ('<a href="' + esc(link) + '">' + img + '</a>') if link else img
    return ('<tr><td data-ortto-module="image" data-slot="element" align="center" class="px" '
            'style="padding:6px 24px 14px;">' + inner + '</td></tr>')


def _block_promo(e, camp, lang, align):
    """PromoLine (copy slot): a code chip plus a short urgency line. ONLY when a real code exists.

    Never invents a code or a deadline. The chip uses constitution colors only (panel border,
    emerald text); the pending gold #C4963C stays out. The spec carries promo.code and promo.line,
    both real brief inputs or the block is omitted.
    """
    promo = e.get("promo")
    if not promo or not promo.get("code"):
        return ""
    code = promo["code"]
    line = promo.get("line", "")
    chip = ('<div style="display:inline-block;background:' + ACCENT + ';border-radius:10px;'
            'padding:9px 16px;color:' + BG + ';font-size:16px;font-weight:700;letter-spacing:3px;">'
            + esc(code) + '</div>')
    line_html = ('<div style="padding:8px 0 0;color:' + MUTE + ';font-size:13px;">' + esc(line) + '</div>') if line else ""
    return ('<tr><td data-ortto-module="text" data-slot="copy" data-role="body" data-lang="' + lang
            + '" data-copy-id="' + cid(e, "promo", camp) + '" align="center" class="' + ("ar" if lang == "ar" else "en")
            + '" style="padding:8px 40px 10px;text-align:center;">' + chip + line_html + '</td></tr>')


# Portrait card geometry. The card is a text-free on-brand #141414 instructor portrait (the website
# grid image, *_HOMEPORTRAIT_BOTTOMGRADIENT* / *BG_141414-BOTTOM-GRADIENT*) shown as a standard image,
# with the name and the "Teaches <subject>" line as LIVE HTML text in a caption BENEATH it, plus an
# emerald accent rule. A plain <img> plus live text survives Ortto's BeeFree editor (a background-image
# overlay does not) and renders everywhere. Width is the 600 wrap split three-up minus gutters. The
# three source portraits do not share one native ratio, so the card is a FIXED 4:5 box and the image
# fills it with object-fit:cover (cropping the dark bottom gradient, not the face) so the three cards
# always align. Outlook (no object-fit) gets the same box via the width/height attributes.
_CARD_W = 176   # rendered card width in the 3-up desktop row
_CARD_H = 220   # fixed card height (4:5 portrait box; keeps the three cards balanced)


def _portrait_card_cell(c, lang, font):
    """One portrait instructor card: a text-free portrait IMAGE with the name and "Teaches <subject>"
    as a live HTML caption BENEATH it. A plain <img> plus live text (no background image, no VML)
    survives Ortto's BeeFree editor and renders everywhere. The whole cell links to the class page
    (the card is NOT a CTA). The portrait is the website grid image, language-neutral and text-free
    (portrait_src_<lang> wins for a rare language-split portrait, else the neutral portrait_src, else
    the legacy src_<lang>/src). The NAME and the "Teaches <subject>" line are live copy slots.
    """
    psrc = (c.get("portrait_src_" + lang) or c.get("portrait_src")
            or c.get("src_" + lang) or c.get("src") or "")
    psrc = _serve_src(psrc)
    clink = c.get("link_" + lang) or c.get("link", "https://www.maharat.com")
    calt = c.get("alt_" + lang) or c.get("alt", "")
    name = c.get("name_" + lang) or c.get("name", "")
    subject = c.get("subject_" + lang) or c.get("subject", "")
    cls = "ar" if lang == "ar" else "en"
    # The portrait as a standard linked image (BeeFree-safe: no background-image, no VML).
    img = ('<a href="' + esc(clink) + '" data-slot="element" '
           'style="display:block;text-decoration:none;">'
           '<img src="' + esc(psrc) + '" width="' + str(_CARD_W) + '" height="' + str(_CARD_H) + '" '
           'alt="' + esc(calt) + '" '
           'style="display:block;width:100%;max-width:' + str(_CARD_W) + 'px;height:' + str(_CARD_H) + 'px;'
           'object-fit:cover;object-position:center top;border-radius:12px;border:0;"></a>')
    # The caption beneath: emerald accent rule, the name, then "Teaches <subject>". Live copy slots.
    rule = ('<div style="width:26px;height:3px;background:' + ACCENT + ';font-size:0;line-height:0;'
            'margin:0 auto 7px;">&nbsp;</div>')
    name_html = ('<div data-slot="copy" data-role="card-name" data-lang="' + lang + '" class="' + cls
                 + '" style="color:' + INK + ';font-size:15px;font-weight:700;line-height:1.3;'
                 'font-family:' + font + ';">' + esc(name) + '</div>') if name else ""
    subj_html = ('<div data-slot="copy" data-role="card-subject" data-lang="' + lang + '" class="' + cls
                 + '" style="color:' + BODY + ';font-size:12px;line-height:1.4;padding-top:3px;'
                 'font-family:' + font + ';">' + esc(subject) + '</div>') if subject else ""
    caption = ('<a href="' + esc(clink) + '" style="display:block;text-decoration:none;'
               'padding:12px 2px 0;text-align:center;">' + rule + name_html + subj_html + '</a>')
    return ('<td class="card" width="33%" align="center" valign="top" data-ortto-module="image" '
            'data-slot="element" data-alt="' + esc(calt) + '" style="padding:6px;">'
            + img + caption + '</td>')


def _block_classcards(e, camp, lang):
    """ClassCardGrid (elements): three linked, status-cleared PORTRAIT instructor cards.

    Each card reproduces the maharat.com instructor grid card: a text-free on-brand #141414 portrait
    of the instructor with an emerald accent rule, the instructor NAME, and "Teaches <subject>" /
    "يعلّم <subject>" as LIVE HTML text in the lower third (overlaid, never baked into the image).
    Language-matched: the AR card shows the Arabic name + Arabic subject and links to the /ar class
    page, the EN card the English name + subject and the /en page. The three are OTHER classes, never
    the email's own instructor. Each card is a single link to its class page (not a CTA).

    Rendered ONLY when three cards are supplied (per-email class_cards or the campaign default).
    Otherwise omitted (the omission is flagged in the README per the build rules).
    """
    cards = e.get("class_cards")
    if cards is None:
        cards = camp.get("class_cards") or []
    if len(cards) < 3:
        return ""
    title = camp.get("class_cards_title_ar", "شاهد أيضًا على مهارات") if lang == "ar" \
        else camp.get("class_cards_title_en", "More classes on Maharat")
    align = "right" if lang == "ar" else "left"
    font = FONT_AR if lang == "ar" else FONT_EN
    cells = [_portrait_card_cell(c, lang, font) for c in cards[:3]]
    out = []
    out.append('<tr><td data-ortto-module="divider" data-slot="structural" style="padding:6px 40px;">'
               '<div style="border-top:1px solid ' + RULE + ';font-size:0;line-height:0;">&nbsp;</div></td></tr>')
    out.append(_heading(title, lang, font, align, 20, "20px 40px 14px"))
    out.append('<tr><td class="px" style="padding:0 28px 14px;"><table role="presentation" width="100%" '
               'cellpadding="0" cellspacing="0"><tr>' + "".join(cells) + '</tr></table></td></tr>')
    return "".join(out)


# --- The multi-instructor digest modules (the extension set, per email-design-system.md 14 to 16).
# LessonCardGrid, IssueIndex, and MemberWin extend the core for multi-instructor and catalog emails
# (a Skill Path launch, a themed roundup, an occasion sale, a recommendation). The angle method is
# context/multi-instructor-angles.md. Each renders only when the spec supplies its data, so a spec
# without these keys is unaffected. Every copy slot binds a data-copy-id; every portrait is a
# text-free element; the per-card link is a quiet secondary text link, never a second pill, so the
# email keeps one primary CTA.


def _eyebrow_row(text, lang, font, align):
    """A small emerald section eyebrow (a digest section label like 'Lessons for you'). A live copy
    slot styled like the SectionHeading eyebrow. Section labels carry no data-copy-id, the same as
    the ClassCardGrid title."""
    cls = "ar" if lang == "ar" else "en"
    return ('<tr><td data-ortto-module="text" data-slot="copy" data-role="eyebrow" data-lang="' + lang
            + '" class="px ' + cls + '" style="padding:18px 40px 8px;color:' + BODY
            + ';font-size:13px;font-weight:700;letter-spacing:2px;text-align:' + align
            + ';font-family:' + font + ';">' + esc(text) + '</td></tr>')


def _lesson_card_cell(c, idx, e, camp, lang, font):
    """One LessonCardGrid card: a text-free instructor portrait (element) with an outcome headline,
    a "with <Name>, <credential>" line, and a quiet secondary link beneath it (copy slots). The card
    casts one instructor as one lesson toward the email's umbrella outcome. Only status-cleared,
    rights-cleared instructors; an unconfirmed instructor's card is dropped by the author, not here.
    The per-card link is a quiet text link, never a second pill, so the email keeps one primary CTA.
    """
    psrc = _serve_src(c.get("portrait_src_" + lang) or c.get("portrait_src")
                      or c.get("src_" + lang) or c.get("src") or "")
    clink = c.get("link_" + lang) or c.get("link", "https://www.maharat.com")
    calt = c.get("alt_" + lang) or c.get("alt", "")
    headline = c.get("headline_" + lang) or c.get("headline", "")
    credential = c.get("credential_" + lang) or c.get("credential", "")
    cta_label = c.get("cta_" + lang) or c.get("cta", "")
    align = "right" if lang == "ar" else "left"
    cls = "ar" if lang == "ar" else "en"
    img = ('<a href="' + esc(clink) + '" data-slot="element" style="display:block;text-decoration:none;">'
           '<img src="' + esc(psrc) + '" width="' + str(_CARD_W) + '" alt="' + esc(calt) + '" '
           'style="display:block;width:100%;max-width:' + str(_CARD_W) + 'px;height:auto;'
           'border-radius:12px;border:0;"></a>')
    rule = ('<div style="width:26px;height:3px;background:' + ACCENT + ';font-size:0;line-height:0;'
            'margin:8px 0 7px;">&nbsp;</div>')
    head_html = ('<div data-slot="copy" data-role="card-headline" data-lang="' + lang + '" data-copy-id="'
                 + cid(e, "lesson" + str(idx) + "-headline", camp) + '" class="' + cls
                 + '" style="color:' + INK + ';font-size:15px;font-weight:700;line-height:1.35;'
                 'font-family:' + font + ';">' + esc(headline) + '</div>') if headline else ""
    cred_html = ('<div data-slot="copy" data-role="card-credential" data-lang="' + lang + '" data-copy-id="'
                 + cid(e, "lesson" + str(idx) + "-credential", camp) + '" class="' + cls
                 + '" style="color:' + BODY + ';font-size:12px;line-height:1.5;padding-top:5px;'
                 'font-family:' + font + ';">' + esc(credential) + '</div>') if credential else ""
    cta_html = ('<div data-slot="copy" data-role="card-cta" data-lang="' + lang + '" data-copy-id="'
                + cid(e, "lesson" + str(idx) + "-cta", camp) + '" class="' + cls
                + '" style="padding-top:8px;"><a href="' + esc(clink) + '" style="color:' + ACCENT
                + ';font-size:13px;font-weight:700;text-decoration:none;">' + esc(cta_label)
                + '</a></div>') if cta_label else ""
    caption = ('<div style="padding:10px 2px 0;text-align:' + align + ';">'
               + rule + head_html + cred_html + cta_html + '</div>')
    return ('<td class="card" width="33%" align="center" valign="top" data-ortto-module="image" '
            'data-slot="element" data-alt="' + esc(calt) + '" style="padding:6px;">' + img + caption + '</td>')


def _block_lessoncards(e, camp, lang):
    """LessonCardGrid (the multi-instructor offer grid): up to three cards, each casting one
    instructor as one lesson toward the email's umbrella outcome (outcome headline, then "with
    <Name>, <credential>", then a quiet secondary link). The angle method is
    context/multi-instructor-angles.md. Rendered only when the spec supplies lesson_cards (per-email
    or campaign default). Status-cleared, rights-cleared instructors only; an unconfirmed
    instructor's card is dropped by the author before render.
    """
    cards = e.get("lesson_cards")
    if cards is None:
        cards = camp.get("lesson_cards") or []
    if not cards:
        return ""
    title = (e.get("lessons_title_" + lang) or camp.get("lessons_title_" + lang)
             or ("دروس لك" if lang == "ar" else "Lessons for you"))
    align = "right" if lang == "ar" else "left"
    font = FONT_AR if lang == "ar" else FONT_EN
    cells = [_lesson_card_cell(c, i + 1, e, camp, lang, font) for i, c in enumerate(cards[:3])]
    out = [_eyebrow_row(title, lang, font, align)]
    out.append('<tr><td class="px" style="padding:0 28px 14px;"><table role="presentation" width="100%" '
               'cellpadding="0" cellspacing="0"><tr>' + "".join(cells) + '</tr></table></td></tr>')
    return "".join(out)


def _block_issueindex(e, camp, lang):
    """IssueIndex ("In this issue"): an optional numbered table of contents at the top of a digest.
    A copy slot (data-role="index"), Western numerals, each entry an in-email or in-page link.
    Rendered only when the spec supplies issue_index.
    """
    entries = e.get("issue_index") or []
    if not entries:
        return ""
    title = (e.get("issue_index_title_" + lang)
             or ("في هذا العدد" if lang == "ar" else "In this issue"))
    align = "right" if lang == "ar" else "left"
    font = FONT_AR if lang == "ar" else FONT_EN
    cls = "ar" if lang == "ar" else "en"
    rows = []
    for i, it in enumerate(entries):
        label = it.get("label_" + lang) or it.get("label", "")
        link = it.get("link", "")
        num = str(i + 1).zfill(2)
        inner = esc(num) + "&nbsp;&nbsp;" + esc(label)
        if link:
            inner = '<a href="' + esc(link) + '" style="color:' + BODY + ';text-decoration:none;">' + inner + '</a>'
        rows.append('<div style="padding:4px 0;">' + inner + '</div>')
    out = [_eyebrow_row(title, lang, font, align)]
    out.append('<tr><td data-ortto-module="text" data-slot="copy" data-role="index" data-lang="' + lang
               + '" data-copy-id="' + cid(e, "issueindex", camp) + '" class="px ' + cls
               + '" style="padding:0 40px 10px;color:' + BODY + ';font-size:15px;line-height:1.7;text-align:'
               + align + ';">' + "".join(rows) + '</td></tr>')
    return "".join(out)


def _block_memberwin(e, camp, lang):
    """MemberWin: one real, consented member testimonial, an attribution, and a short reflective
    bridge line that leads into the primary CTA. Copy slots. The testimonial must be real and
    consented, never invented; authenticity is checked at brand QA and compliance. Rendered only
    when the spec supplies member_win with a quote.
    """
    mw = e.get("member_win")
    if not mw or not (mw.get("quote_" + lang) or mw.get("quote")):
        return ""
    quote = mw.get("quote_" + lang) or mw.get("quote", "")
    attribution = mw.get("attribution_" + lang) or mw.get("attribution", "")
    bridge = mw.get("bridge_" + lang) or mw.get("bridge", "")
    title = (e.get("member_win_title_" + lang)
             or ("قصص المشتركين" if lang == "ar" else "Member wins"))
    align = "right" if lang == "ar" else "left"
    font = FONT_AR if lang == "ar" else FONT_EN
    cls = "ar" if lang == "ar" else "en"
    out = [_eyebrow_row(title, lang, font, align)]
    out.append('<tr><td data-ortto-module="text" data-slot="copy" data-role="quote" data-lang="' + lang
               + '" data-copy-id="' + cid(e, "memberwin-quote", camp) + '" class="px ' + cls
               + '" style="padding:0 40px 8px;color:' + INK + ';font-size:18px;line-height:1.6;text-align:'
               + align + ';font-family:' + font + ';">' + _para(quote) + '</td></tr>')
    if attribution:
        out.append('<tr><td data-ortto-module="paragraph" data-slot="copy" data-role="body" data-lang="' + lang
                   + '" data-copy-id="' + cid(e, "memberwin-attribution", camp) + '" class="px ' + cls
                   + '" style="padding:0 40px 8px;color:' + MUTE + ';font-size:13px;text-align:'
                   + align + ';">' + esc(attribution) + '</td></tr>')
    if bridge:
        out.append('<tr><td data-ortto-module="paragraph" data-slot="copy" data-role="body" data-lang="' + lang
                   + '" data-copy-id="' + cid(e, "memberwin-bridge", camp) + '" class="px ' + cls
                   + '" style="padding:0 40px 12px;color:' + BODY + ';font-size:15px;line-height:1.85;text-align:'
                   + align + ';">' + _para(bridge) + '</td></tr>')
    return "".join(out)


# The body-block dispatch table, by module key. The header, CTA, and footer are always emitted.
BLOCK = {
    "body": lambda e, camp, lang, font, align: _block_body(e, camp, lang, font, align),
    "list": lambda e, camp, lang, font, align: _block_list(e, camp, lang, font, align),
    "feature": lambda e, camp, lang, font, align: _block_feature(e, camp, lang),
    "promo": lambda e, camp, lang, font, align: _block_promo(e, camp, lang, align),
    "lessoncards": lambda e, camp, lang, font, align: _block_lessoncards(e, camp, lang),
    "issueindex": lambda e, camp, lang, font, align: _block_issueindex(e, camp, lang),
    "memberwin": lambda e, camp, lang, font, align: _block_memberwin(e, camp, lang),
    "classcards": lambda e, camp, lang, font, align: _block_classcards(e, camp, lang),
}


def _module_order(e):
    """The ordered body blocks for an email: explicit spec 'modules', else inferred from keys.

    The digest modules (issueindex, lessoncards, memberwin) join the inference only when their keys
    are present, so a spec without them renders exactly as before. A digest usually sets an explicit
    'modules' list; the inferred order is a sensible default (index, then body, then the lesson
    grid, then the member win).
    """
    mods = e.get("modules")
    if mods:
        return [m for m in mods if m in BLOCK]
    order = []
    if e.get("issue_index"):
        order.append("issueindex")
    order.append("body")
    if e.get("list_items"):
        order.append("list")
    if e.get("feature_image"):
        order.append("feature")
    if e.get("lesson_cards"):
        order.append("lessoncards")
    if e.get("promo") and e["promo"].get("code"):
        order.append("promo")
    if e.get("member_win"):
        order.append("memberwin")
    return order


def render_email(e, camp):
    lang = e["lang"]
    rtl = lang == "ar"
    diratt = "rtl" if rtl else "ltr"
    align = "right" if rtl else "left"
    font = FONT_AR if rtl else FONT_EN
    cls = "ar" if rtl else "en"
    s = STRINGS[lang]
    eyebrow = camp.get("brand_eyebrow_ar", "مهارات") if rtl else camp.get("brand_eyebrow", "MAHARAT")

    hero = _resolve_hero(e, camp, lang)
    cta = e["cta"]
    cta_url = cta.get("url", "#")
    # MSO VML roundrect width: rough by label length, kept compact.
    vml_w = max(150, min(280, 70 + len(cta["label"]) * (16 if not rtl else 13)))

    d = []
    d.extend(_doc_comment(e, camp, lang, rtl))
    d.append('<!DOCTYPE html>')
    d.append('<html lang="' + lang + '" dir="' + diratt + '" xmlns="http://www.w3.org/1999/xhtml" '
             'xmlns:v="urn:schemas-microsoft-com:vml" xmlns:o="urn:schemas-microsoft-com:office:office">')
    d.append('<head>')
    d.append('<meta charset="utf-8">')
    d.append('<meta name="viewport" content="width=device-width, initial-scale=1">')
    d.append('<meta name="color-scheme" content="dark"><meta name="supported-color-schemes" content="dark">')
    d.append('<title>' + esc(e["subject"]) + '</title>')
    if rtl:
        d.append('<link href="' + CSS_LYON + '" rel="stylesheet">')
    d.append('<link href="' + CSS_ACUMIN + '" rel="stylesheet">')
    d.append('<style>')
    d.append('body{margin:0;padding:0;background:' + BG + ';}')
    d.append('img{border:0;line-height:100%;outline:none;text-decoration:none;-ms-interpolation-mode:bicubic;}')
    d.append('a{text-decoration:none;}')
    d.append('.wrap{width:600px;max-width:600px;}')
    d.append('.' + cls + '{font-family:' + font + ';}')
    d.append('.bul{color:' + ACCENT + ';font-weight:700;}')
    d.append('@media only screen and (max-width:600px){.wrap{width:100% !important;}'
             '.px{padding-left:24px !important;padding-right:24px !important;}'
             '.card{display:block !important;width:100% !important;}'
             '.card table{max-width:100% !important;height:300px !important;}'
             '.card td{height:300px !important;}.h1{font-size:24px !important;}}')
    d.append('</style>')
    d.append('</head>')
    d.append('<body style="margin:0;padding:0;background:' + BG + ';">')

    # Preheader, hidden copy slot
    d.append('<div data-ortto-module="paragraph" data-slot="copy" data-role="preheader" data-lang="' + lang
             + '" data-copy-id="' + cid(e, "preheader", camp) + '" style="display:none;max-height:0;overflow:hidden;opacity:0;">'
             + esc(e.get("preheader", "")) + '</div>')

    d.append('<table role="presentation" width="100%" cellpadding="0" cellspacing="0" style="background:' + BG + ';">')
    d.append('<tr><td align="center" style="padding:0 12px;">')
    d.append('<table role="presentation" class="wrap ' + cls + '" width="600" cellpadding="0" cellspacing="0" '
             'style="width:600px;max-width:600px;background:' + BG + ';direction:' + diratt + ';font-family:' + font + ';">')

    # LogoBar (element). Maharat sends carry no view-in-browser link, so none is emitted.
    d.append('<tr><td data-ortto-module="image" data-slot="element" align="center" style="padding:24px 0 20px;">'
             '<a href="https://www.maharat.com" aria-label="' + esc("الصفحة الرئيسية لمهارات" if rtl else "Maharat homepage")
             + '"><img src="' + LOGO + '" width="120" alt="' + esc("مهارات" if rtl else "Maharat")
             + '" style="display:block;width:120px;height:auto;"></a></td></tr>')

    # Hero (element, text-free)
    if hero:
        d.append('<tr><td data-ortto-module="image" data-slot="element" style="padding:0;">'
                 '<a href="' + esc(hero["link"]) + '"><img src="' + esc(hero["src"]) + '" width="600" alt="'
                 + esc(hero["alt"]) + '" style="display:block;width:100%;max-width:600px;height:auto;border-radius:16px;">'
                 '</a></td></tr>')

    # SectionHeading: eyebrow + headline (copy slots). The eyebrow is optional: a campaign that
    # sets brand_eyebrow (and brand_eyebrow_ar) to an empty string renders no eyebrow row.
    if eyebrow:
        d.append('<tr><td data-ortto-module="text" data-slot="copy" data-role="eyebrow" data-lang="' + lang
                 + '" data-copy-id="' + cid(e, "eyebrow", camp) + '" class="px ' + cls
                 + '" style="padding:30px 40px 0;color:' + BODY + ';font-size:13px;font-weight:700;letter-spacing:2px;text-align:'
                 + align + ';">' + esc(eyebrow) + '</td></tr>')
    head_pad_top = "10px" if eyebrow else "30px"
    d.append('<tr><td data-ortto-module="heading" data-slot="copy" data-role="headline" data-lang="' + lang
             + '" data-copy-id="' + cid(e, "headline", camp) + '" class="px h1 ' + cls
             + '" style="padding:' + head_pad_top + ' 40px 12px;color:' + INK + ';font-size:28px;font-weight:700;line-height:1.45;text-align:'
             + align + ';font-family:' + font + ';">'
             + '<h1 style="margin:0;font-size:28px;font-weight:700;line-height:1.45;color:' + INK + ';font-family:' + font + ';">'
             + esc(e["headline"]) + '</h1></td></tr>')

    # Greeting (optional copy slot)
    if e.get("greeting"):
        d.append('<tr><td data-ortto-module="paragraph" data-slot="copy" data-role="body" data-lang="' + lang
                 + '" data-copy-id="' + cid(e, "greeting", camp) + '" class="px ' + cls
                 + '" style="padding:0 40px 6px;color:' + MUTE + ';font-size:15px;line-height:1.7;text-align:'
                 + align + ';">' + esc(e["greeting"]) + '</td></tr>')

    # Per-email body modules (driven by the spec, between SectionHeading and the CTA)
    order = _module_order(e)
    for m in order:
        d.append(BLOCK[m](e, camp, lang, font, align))

    # Primary CTA: MSO VML roundrect + non-mso pill, white label on emerald (owner-directed; below WCAG AA)
    d.append('<tr><td align="center" style="padding:10px 40px 30px;">')
    d.append('<!--[if mso]><v:roundrect xmlns:v="urn:schemas-microsoft-com:vml" href="' + esc(cta_url)
             + '" style="height:50px;v-text-anchor:middle;width:' + str(vml_w) + 'px;" arcsize="56%" fillcolor="' + ACCENT
             + '" stroke="false"><center style="color:' + CTA_TEXT + ';font-family:sans-serif;font-size:16px;font-weight:bold;">'
             + esc(cta["label"]) + '</center></v:roundrect><![endif]-->')
    d.append('<!--[if !mso]><!-- -->')
    d.append('<table role="presentation" cellpadding="0" cellspacing="0"><tr>')
    d.append('<td data-ortto-module="button" data-slot="copy" data-role="cta" data-lang="' + lang
             + '" data-copy-id="' + cid(e, "cta", camp) + '" data-link-slot="' + esc(cta_url)
             + '" bgcolor="' + ACCENT + '" style="border-radius:28px;">'
             '<a href="' + esc(cta_url) + '" data-ap3-idx="1" class="' + cls
             + '" style="display:inline-block;padding:15px 44px;color:' + CTA_TEXT + ';font-size:16px;font-weight:700;font-family:'
             + font + ';">' + esc(cta["label"]) + '</a></td>')
    d.append('</tr></table>')
    d.append('<!--<![endif]-->')
    d.append('</td></tr>')

    # The "our other classes" bottom row (ClassCardGrid): three OTHER status-cleared,
    # rights-cleared, text-free, language-matched covers, after the CTA. Rendered only when three
    # cards are supplied (per-email class_cards or the campaign default), else omitted. Skipped here
    # if the spec already placed "classcards" in its module order (no double render).
    if "classcards" not in order:
        cards = _block_classcards(e, camp, lang)
        if cards:
            d.append(cards)

    # Footer: social icons + www + sender identity + unsubscribe
    icons = "".join(
        '<a href="' + esc(href) + '" data-ap3-idx="' + str(i + 2) + '" style="display:inline-block;padding:0 7px;">'
        '<img src="' + esc(src) + '" width="30" alt="' + esc(SOCIAL_ALT[lang][name])
        + '" style="width:30px;height:30px;"></a>'
        for i, (name, href, src) in enumerate(SOCIAL))
    d.append('<tr><td data-ortto-module="social" data-slot="element" align="center" '
             'style="padding:28px 40px 10px;border-top:1px solid ' + RULE + ';">' + icons + '</td></tr>')
    d.append('<tr><td data-slot="structural" align="center" style="padding:10px 40px 2px;">'
             '<a href="https://www.maharat.com" style="color:' + MUTE + ';font-size:13px;">www.maharat.com</a></td></tr>')
    d.append('<tr><td data-ortto-module="text" data-slot="copy" data-role="body" data-lang="' + lang
             + '" data-copy-id="' + cid(e, "footer-sender", camp) + '" align="center" class="' + cls
             + '" style="padding:2px 40px;color:' + FAINT + ';font-size:12px;line-height:1.7;">' + esc(s["sender"]) + '</td></tr>')
    d.append('<tr><td data-slot="structural" align="center" style="padding:6px 40px 28px;">'
             '<a href="{{ urls.unsubscribe }}" style="color:' + FAINT + ';font-size:12px;text-decoration:underline;">'
             + esc(s["unsub"]) + '</a></td></tr>')

    d.append('</table></td></tr></table>')
    d.append('</body>')
    d.append('</html>')
    return "\n".join(x for x in d if x)


def _resolve_hero(e, camp, lang):
    """Per-email hero wins; else the campaign default. Per-language src, alt, and link.

    The header src is language-matched: src_<lang> (src_ar / src_en) wins, falling back to the
    language-neutral src. This lets an AR email carry the AR-page (RIGHTGRADIENT) class cover and
    an EN email the EN-page (LEFTGRADIENT) cover, while a language-neutral cover (one image for
    both pages) is set once on src. LEFTGRADIENT is the English page, RIGHTGRADIENT is the Arabic
    page (the gradient falls toward the reading-start edge).
    """
    for hi in (e.get("hero_image"), camp.get("hero_image")):
        if not hi:
            continue
        src = hi.get("src_" + lang) or hi.get("src")
        if src:
            link = hi.get("link_" + lang) or hi.get("link", "https://www.maharat.com")
            # Serve resolution: the Ortto serve URL when the map marks this source served, else the
            # CloudFront cover unchanged (the preview design proof). All pending today, so no change.
            return {"src": _serve_src(src), "alt": hi.get("alt_" + lang) or hi.get("alt", ""),
                    "link": link}
    return None


def render_index(spec):
    title = esc(spec.get("campaign_title", spec.get("campaign_id", "")))
    status = esc(spec.get("status", "draft, nothing sends"))
    opens = spec.get("open_items", [])
    open_html = "".join('<li>' + esc(o) + '</li>' for o in opens)

    items = []
    for e in spec["emails"]:
        fid = e["id"] + "." + e["lang"]
        fname = fid + ".html"
        alts = e.get("subject_alts", [])
        alt_html = ('<div class="alts">' + " &middot; ".join(esc(a) for a in alts) + '</div>') if alts else ""
        items.append(
            '<div class="item">'
            '<div class="meta"><span class="tag">' + esc(e["id"].upper()) + ' ' + esc(e["lang"].upper()) + '</span>'
            '<span class="name">' + esc(e.get("name", "")) + '</span></div>'
            '<div class="subj">' + esc(e["subject"]) + '</div>' + alt_html
            + '<div class="pre">' + esc(e.get("preheader", "")) + '</div>'
            '<a class="open" href="' + fname + '">' + fname + '</a>'
            '<iframe loading="lazy" src="' + fname + '" title="' + esc(fid) + '"></iframe>'
            '</div>'
        )

    css = (
        "body{margin:0;background:" + BG + ";color:" + INK + ";font-family:'Acumin Pro',Arial,sans-serif;}"
        ".head{padding:32px 32px 8px;max-width:1200px;margin:0 auto;}"
        ".head h1{margin:0 0 6px;font-size:22px;}"
        ".bar{display:inline-block;padding:6px 12px;border:1px solid " + ACCENT + ";color:" + ACCENT
        + ";border-radius:999px;font-size:12px;font-weight:700;}"
        ".note{max-width:1200px;margin:10px auto 0;padding:0 32px;color:" + BODY + ";font-size:13px;}"
        ".open-items{max-width:1200px;margin:12px auto 0;padding:0 32px;color:" + MUTE + ";font-size:13px;}"
        ".open-items li{margin:2px 0;}"
        ".grid{display:grid;grid-template-columns:repeat(auto-fill,minmax(360px,1fr));gap:20px;"
        "max-width:1200px;margin:0 auto;padding:24px 32px 48px;}"
        ".item{background:" + CARD + ";border:1px solid " + RULE + ";border-radius:14px;padding:16px;}"
        ".meta{display:flex;gap:10px;align-items:center;margin-bottom:8px;}"
        ".tag{background:" + ACCENT + ";color:" + BG + ";font-weight:700;font-size:11px;padding:3px 8px;border-radius:6px;}"
        ".name{color:" + MUTE + ";font-size:12px;}"
        ".subj{font-size:15px;font-weight:600;margin-bottom:4px;}"
        ".alts{color:" + MUTE + ";font-size:12px;margin-bottom:6px;}"
        ".pre{color:" + BODY + ";font-size:12px;margin-bottom:10px;}"
        ".open{color:" + ACCENT + ";font-size:12px;text-decoration:none;}"
        "iframe{width:100%;height:760px;border:1px solid " + RULE + ";border-radius:10px;margin-top:10px;background:" + BG + ";}"
    )
    note = esc(spec.get("index_note",
              "Slotted live-component builds (the Elda reference standard). Every word is a live copy "
              "slot bound to a data-copy-id; every image is text-free. Brand fonts via the Ortto "
              "custom-fonts CSS. Draft, not approved, nothing sends. Not yet through the gate stack "
              "or the human gate."))
    return (
        '<!DOCTYPE html><html lang="en" dir="ltr"><head><meta charset="utf-8">'
        '<meta name="viewport" content="width=device-width,initial-scale=1">'
        '<link href="' + CSS_ACUMIN + '" rel="stylesheet">'
        '<title>' + title + ' . email preview</title><style>' + css + '</style></head><body>'
        '<div class="head"><h1>' + title + '</h1><span class="bar">' + status + '</span></div>'
        '<div class="note">' + note + '</div>'
        + ('<ul class="open-items">' + open_html + '</ul>' if open_html else '')
        + '<div class="grid">' + "".join(items) + '</div></body></html>'
    )


def sweep(name, text):
    hits = FORBIDDEN.findall(text)
    if hits:
        uniq = " ".join(sorted({hex(ord(c)) for c in hits}))
        print("  FAIL: " + name + " has forbidden characters: " + uniq
              + " (em/en dash, tatweel, or Eastern numerals)")
    return len(hits)


def main():
    ap = argparse.ArgumentParser(description="Render a Maharat email spec to slotted brand HTML.")
    ap.add_argument("spec", help="path to the email spec JSON")
    ap.add_argument("--out", help="output directory (default: spec's directory)")
    ap.add_argument("--check", action="store_true", help="sweep house style only, write nothing")
    args = ap.parse_args()

    spec_path = Path(args.spec)
    spec = json.loads(spec_path.read_text(encoding="utf-8"))
    out = Path(args.out) if args.out else spec_path.parent
    out.mkdir(parents=True, exist_ok=True)

    print("email_render (slotted): " + spec.get("campaign_id", spec_path.stem))
    bad = 0
    rendered = []
    heroes = 0
    for e in spec["emails"]:
        h = render_email(e, spec)
        if _resolve_hero(e, spec, e["lang"]):
            heroes += 1
        bad += sweep(e["id"] + "." + e["lang"] + ".html", h)
        rendered.append((out / (e["id"] + "." + e["lang"] + ".html"), h))
    index = render_index(spec)
    bad += sweep("index.html", index)

    if bad:
        print("FAIL: " + str(bad) + " forbidden character(s). Nothing written.")
        return 1

    if args.check:
        print("ok: house-style sweep clean for " + str(len(rendered)) + " slotted email(s) (check only)")
        return 0

    for path, h in rendered:
        path.write_text(h, encoding="utf-8")
    (out / "index.html").write_text(index, encoding="utf-8")
    print("ok: wrote " + str(len(rendered)) + " slotted email(s) + index.html to " + str(out)
          + " (" + str(heroes) + " with a hero image)")
    print("PASS: house-style clean; each email is slotted (live copy slots bound to data-copy-id),")
    print("      one primary CTA (MSO VML + pill), sender identity, and unsubscribe.")
    print("Gates next: email-html-build eval, arabic/english-copy-qa by slot, email-asset-qa, "
          "accessibility-qa, compliance-privacy-check, brand-qa-reviewer, human gate. Nothing sends.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
