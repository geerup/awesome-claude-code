#!/usr/bin/env python3
"""populate_email_covers.py: write the verified, language-matched class covers into the email specs.

This is the single maintained record of the per-class CloudFront class covers (the corrected
headers) and the per-class metadata (page links, titles, alt text). It writes two things into each
7-step spec.json (and the 4-email Bassam makeup emails.spec.json):

1. hero_image: the language-matched header. LEFTGRADIENT is the English page, RIGHTGRADIENT is the
   Arabic page. A neutral cover (one image for both pages) is set on src; a language-split cover is
   set on src_en (LEFTGRADIENT / EN-PAGE) and src_ar (RIGHTGRADIENT / AR-PAGE). The renderer's
   _resolve_hero picks src_<lang> then src.

2. class_cards (top-level): three OTHER classes (never the email's own instructor), each with a
   language-matched cover (src_ar / src_en) and a language-matched page link (link_ar / link_en),
   text-free, with descriptive alt. The renderer's ClassCardGrid renders these as the bottom row.

Every cover here was verified servable server-side with the firecrawl scrape tool on 2026-06-18
(formats ["markdown"], proxy "basic"): a "cannot process image/*" error or an image binary body
(Exif/JFIF/RIFF-WEBP/PNG) means servable; a 403/404 or AccessDenied XML body means not. The salam
intended cover dakak-cover.png is dead (403, the og:image type): the active header is the verified
SD_PLANS_BOTTOMGRADIENT.jpg, an INTERIM banner (the plans-page image, not a dedicated class cover),
flagged as needing a real Salam class cover produced. CloudFront is the verified design proof, not
an approved email host: every cover still stages to the Ortto CDN before any send (gate zero).

House style, by code point: no em dash, no en dash, no tatweel, Western numerals only. This source
carries no literal forbidden character.

Usage:
    python3 .claude/scripts/populate_email_covers.py            # write all specs
    python3 .claude/scripts/populate_email_covers.py --check    # report, write nothing
"""

import argparse
import json
import sys
from pathlib import Path

CF = "https://dt92b02v6m7lx.cloudfront.net/"

# The canonical per-class cover record. status is the firecrawl verdict (verified | BLOCKED).
# For a neutral cover, "src" is set and src_ar/src_en are omitted. For a language-split cover,
# src_en (EN page = LEFTGRADIENT / EN-PAGE) and src_ar (AR page = RIGHTGRADIENT / AR-PAGE) are set.
CLASSES = {
    "bassam-fattouh": {
        "title_ar": "بسام فتّوح، يعلّم المكياج",
        "title_en": "Bassam Fattouh, Teaches Makeup",
        "category": "design-style",
        "page_slug": "bassam-fattouh-teaches-makeup",
        "cover": {"src": CF + "BF_CLASSCOVER_LEFTRIGHTGRADIENT.JPG"},
        "status": "verified",
    },
    "bassam-fattouh-bridal": {
        "title_ar": "بسام فتّوح، يعلّم مكياج العروس",
        "title_en": "Bassam Fattouh, Teaches Bridal Makeup",
        "category": "design-style",
        "page_slug": "bassam-fattouh-teaches-bridal-makeup",
        "cover": {"src_en": CF + "BFBRIDAL_CLASSCOVER_DESKTOP_01_LEFTGRADIENT.webp",
                  "src_ar": CF + "BFBRIDAL_CLASSCOVER_DESKTOP_01_RIGHTGRADIENT.webp"},
        "status": "verified",
    },
    "cedric-haddad": {
        "title_ar": "سيدريك حدّاد، يعلّم تنسيق الملابس",
        "title_en": "Cedric Haddad, Teaches Personal Styling",
        "category": "design-style",
        "page_slug": "cedric-haddad-teaches-personal-styling",
        "cover": {"src_en": CF + "CH_CLASSCOVER_DESKTOP_01_LEFTGRADIENT.webp",
                  "src_ar": CF + "CH_CLASSCOVER_DESKTOP_01_RIGHTGRADIENT.webp"},
        "status": "verified",
    },
    "elda-choucair": {
        "title_ar": "إلدا شقير، تعلّم التسويق",
        "title_en": "Elda Choucair, Teaches Marketing",
        "category": "business",
        "page_slug": "elda-choucair-teaches-marketing",
        "cover": {"src_en": CF + "EC_CLASSCOVER_DESKTOP_01_EN-PAGE.webp",
                  "src_ar": CF + "EC_CLASSCOVER_DESKTOP_01_AR-PAGE.webp"},
        "status": "verified",
    },
    "ragheb-alama": {
        "title_ar": "راغب علامة، يعلّم الموسيقى والأداء",
        "title_en": "Ragheb Alama, Teaches Music and Performance",
        "category": "music",
        "page_slug": "ragheb-alama-teaches-music-and-performance",
        "cover": {"src": CF + "RA_CLASSCOVER_DESKTOP_01_NOGRADIENT.webp"},
        "status": "verified",
    },
    "rahma-riad": {
        "title_ar": "رحمة رياض، تعلّم بناء مسيرة في العصر الرقمي",
        "title_en": "Rahma Riad, Teaches Building a Career in the Digital Age",
        "category": "business",
        "page_slug": "rahma-riad-teaches-building-a-career-in-the-digital-age",
        "cover": {"src_en": CF + "RR_CLASSCOVER_DESKTOP_01_LEFTGRADIENT.webp",
                  "src_ar": CF + "RR_CLASSCOVER_DESKTOP_01_RIGHTGRADIENT.webp"},
        "status": "verified",
    },
    "toufic-kredieh": {
        "title_ar": "توفيق كريدية، يعلّم بناء وتنمية مشروعك",
        "title_en": "Toufic Kreidieh, Teaches Building and Growing Your Business",
        "category": "business",
        "page_slug": "toufic-kreidieh-teaches-building-and-growing-your-business",
        "cover": {"src_en": CF + "TK_CLASSCOVER_DESKTOP_01_LEFTGRADIENT.webp",
                  "src_ar": CF + "TK_CLASSCOVER_DESKTOP_01_RIGHTGRADIENT.webp"},
        "status": "verified",
    },
    "kosai-khauli": {
        "title_ar": "قصي خولي، يعلّم التمثيل",
        "title_en": "Kosai Khauli, Teaches Acting",
        "category": "acting",
        "page_slug": "kosai-khauli-teaches-acting",
        "cover": {"src": CF + "02_240222_BEGINNINGS.00_03_55_10.Still001-02.webp"},
        "status": "verified",
    },
    "salam-dakkak": {
        "title_ar": "سلام دقاق، تعلّم الطبخ المشرقي المنزلي",
        "title_en": "Salam Dakkak, Teaches Levantine Home Cooking",
        "category": "cooking",
        "page_slug": "salam-dakkak-teaches-levantine-cooking",
        # dakak-cover.png is DEAD (403, the og:image type). The header is the verified-servable
        # SD_PLANS_BOTTOMGRADIENT.jpg, treated like the other CloudFront covers (stage to Ortto
        # before send), with an interim-banner flag: it is the plans-page image, not a dedicated
        # class cover, until a real Salam class cover is produced.
        "cover": {"src": CF + "SD_PLANS_BOTTOMGRADIENT.jpg"},
        "status": "verified",
        "interim": True,
        "flag": ("INTERIM banner. SD_PLANS_BOTTOMGRADIENT.jpg is the plans-page image (not a "
                 "dedicated class cover), used as Salam's header until a real Salam class cover is "
                 "produced. The intended cover dakak-cover.png is DEAD (403, the og:image type). "
                 "The Drive portrait 11032024_SalamBG_141414 is the alternative cover source once "
                 "hosted. Flag for Ahmed."),
    },
}


def page_link(slug, lang):
    c = CLASSES[slug]
    return "https://www.maharat.com/" + lang + "/class/" + c["category"] + "/" + c["page_slug"]


def hero_for(slug):
    """The language-matched hero_image block for a class spec (header), src_ar / src_en / src."""
    c = CLASSES[slug]
    h = dict(c["cover"])  # src and/or src_ar/src_en
    h["alt_ar"] = c["title_ar"] + "، ماستركلاس على مهارات"
    h["alt_en"] = c["title_en"] + ", a Masterclass on Maharat"
    h["link_ar"] = page_link(slug, "ar")
    h["link_en"] = page_link(slug, "en")
    note = ("Language-matched class cover (LEFTGRADIENT/EN-PAGE on EN, RIGHTGRADIENT/AR-PAGE on AR; "
            "a neutral cover serves both). Verified servable server-side on CloudFront 2026-06-18. "
            "CloudFront is the design proof, NOT an approved email host: stage to the Ortto CDN "
            "(or prove with an inbox send-test) and swap before any send.")
    if c["status"] == "BLOCKED":
        note = ("FALLBACK header. " + c.get("flag", "") + " " + note)
        h["status"] = "BLOCKED"
    elif c.get("interim"):
        # Verified-servable, but an interim banner rather than a dedicated class cover. Treated
        # like the other CloudFront covers (stage to Ortto before send), with the interim flag.
        note = (c.get("flag", "") + " " + note)
        h["status"] = "verified"
    else:
        h["status"] = "verified"
    h["host"] = note
    if c["status"] == "BLOCKED":
        h["send_ready"] = "BLOCKED: source a real class cover for salam, then stage to Ortto CDN"
    elif c.get("interim"):
        h["send_ready"] = ("stage to Ortto before send (CloudFront verified; SD_PLANS is an interim "
                           "banner, not a dedicated class cover, until a real Salam class cover is "
                           "produced; dakak-cover.png is dead)")
    else:
        h["send_ready"] = ("BLOCKED: stage header to Ortto CDN (CloudFront verified, not an approved "
                           "email host)")
    return h


def card_for(slug):
    """A single language-matched class card (cover + page link + alt) for the bottom row."""
    c = CLASSES[slug]
    card = {}
    cov = c["cover"]
    if "src" in cov:
        card["src"] = cov["src"]
    if "src_ar" in cov:
        card["src_ar"] = cov["src_ar"]
    if "src_en" in cov:
        card["src_en"] = cov["src_en"]
    card["link_ar"] = page_link(slug, "ar")
    card["link_en"] = page_link(slug, "en")
    card["alt_ar"] = "صف " + c["title_ar"] + " على مهارات"
    card["alt_en"] = c["title_en"] + " on Maharat"
    return card


# The three OTHER classes shown in each spec's bottom row. Never the spec's own instructor; for the
# two Bassam classes, the other Bassam class is also excluded so the row is three distinct people.
OTHER_CLASSES = {
    "bassam-fattouh": ["cedric-haddad", "elda-choucair", "ragheb-alama"],
    "bassam-fattouh-bridal": ["cedric-haddad", "rahma-riad", "kosai-khauli"],
    "cedric-haddad": ["bassam-fattouh", "elda-choucair", "ragheb-alama"],
    "elda-choucair": ["toufic-kredieh", "rahma-riad", "ragheb-alama"],
    "ragheb-alama": ["kosai-khauli", "bassam-fattouh", "elda-choucair"],
    "rahma-riad": ["elda-choucair", "toufic-kredieh", "kosai-khauli"],
    "toufic-kredieh": ["elda-choucair", "rahma-riad", "ragheb-alama"],
    "kosai-khauli": ["ragheb-alama", "bassam-fattouh", "elda-choucair"],
    "salam-dakkak": ["bassam-fattouh", "ragheb-alama", "kosai-khauli"],
}

# spec file path -> the class slug it belongs to.
SPECS = {
    ".claude/outputs/2026-06-bassam-fattouh-makeup/email-7step/bassam-fattouh/spec.json": "bassam-fattouh",
    ".claude/outputs/2026-06-bassam-fattouh-makeup/email-html/emails.spec.json": "bassam-fattouh",
    ".claude/outputs/2026-06-bassam-fattouh-bridal-makeup/email-7step/bassam-fattouh-bridal/spec.json": "bassam-fattouh-bridal",
    ".claude/outputs/2026-06-cedric-haddad-styling/email-7step/cedric-haddad/spec.json": "cedric-haddad",
    ".claude/outputs/2026-06-elda-choucair-marketing/email-7step/elda-choucair/spec.json": "elda-choucair",
    ".claude/outputs/2026-06-ragheb-alama-music/email-7step/ragheb-alama/spec.json": "ragheb-alama",
    ".claude/outputs/2026-06-rahma-riad-digital-career/email-7step/rahma-riad/spec.json": "rahma-riad",
    ".claude/outputs/2026-06-toufic-kredieh-business/email-7step/toufic-kredieh/spec.json": "toufic-kredieh",
    ".claude/outputs/2026-06-kosai-khauli-acting/email-7step/kosai-khauli/spec.json": "kosai-khauli",
    ".claude/outputs/2026-06-salam-dakkak-cooking/email-7step/salam-dakkak/spec.json": "salam-dakkak",
}

CARDS_NOTE = ("Three OTHER Maharat classes (not this email's instructor), language-matched covers "
              "(AR cover on AR emails, EN cover on EN emails), each linking to its class page. "
              "Covers verified servable on CloudFront 2026-06-18; stage to the Ortto CDN before send.")


def build_spec_patch(slug):
    hero = hero_for(slug)
    cards = [card_for(s) for s in OTHER_CLASSES[slug]]
    return hero, cards


def main():
    ap = argparse.ArgumentParser(description="Populate verified language-matched covers into specs.")
    ap.add_argument("--check", action="store_true", help="report only, write nothing")
    args = ap.parse_args()

    root = Path(__file__).resolve().parents[2]  # repo root (contains .claude/)
    changed = 0
    for rel, slug in SPECS.items():
        path = root / rel
        if not path.exists():
            print("MISSING: " + rel)
            continue
        spec = json.loads(path.read_text(encoding="utf-8"))
        hero, cards = build_spec_patch(slug)
        spec["hero_image"] = hero
        spec["class_cards"] = cards
        spec["class_cards_title_ar"] = "شاهد أيضًا على مهارات"
        spec["class_cards_title_en"] = "More classes on Maharat"
        spec["class_cards_note"] = CARDS_NOTE
        # Refresh the deliverability note so the rendered doc-comment reflects the corrected,
        # language-matched class cover (replacing any stale autopilot-header note).
        spec["hero_deliverability_note"] = hero["host"]
        # Reconcile open_items: drop the stale "ClassCardGrid OMITTED" and autopilot-header lines,
        # then prepend the corrected header and the now-wired class-card row.
        stale = ("classcardgrid omitted", "1_7.png", "2_7.png", "3_6.png", "autopilot",
                 "كريدية.png", "single-language header")
        kept = [o for o in spec.get("open_items", [])
                if not any(s in o.lower() for s in stale)]
        head_line = ("Header corrected to the real, language-matched class cover (EN page "
                     "LEFTGRADIENT/EN-PAGE, AR page RIGHTGRADIENT/AR-PAGE; a neutral cover serves "
                     "both). " + hero["host"])
        cards_line = ("The 'our other classes' ClassCardGrid is now wired: three OTHER classes "
                      "(" + ", ".join(OTHER_CLASSES[slug]) + "), language-matched covers, each "
                      "linking to its class page. Covers verified on CloudFront; stage to Ortto "
                      "before send.")
        spec["open_items"] = [head_line, cards_line] + kept
        txt = json.dumps(spec, ensure_ascii=False, indent=2) + "\n"
        head = hero.get("src") or hero.get("src_en")
        print(("CHECK " if args.check else "WRITE ") + slug + " <- " + rel)
        print("   hero src_en=" + str(hero.get("src_en") or hero.get("src")))
        print("   hero src_ar=" + str(hero.get("src_ar") or hero.get("src")))
        print("   cards=" + ", ".join(OTHER_CLASSES[slug]) + " | status=" + hero["status"])
        if not args.check:
            path.write_text(txt, encoding="utf-8")
        changed += 1
    print(("ok (check): " if args.check else "ok: wrote ") + str(changed) + " spec(s).")
    return 0


if __name__ == "__main__":
    sys.exit(main())
