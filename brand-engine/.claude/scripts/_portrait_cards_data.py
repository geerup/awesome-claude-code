#!/usr/bin/env python3
"""Canonical portrait-instructor-card data for the Maharat "our other classes" ClassCardGrid.

One entry per class, keyed by the class slug (the last path segment of the class-page URL). Each
entry carries the page-cleared NAME and "Teaches <subject>" / "يعلّم <subject>" phrase (exact, from
context/profiles/maharat/instructor-packs/<slug>/masterclass-pages.md and the live maharat.com library grid,
no invention), the class category, and the text-free on-brand #141414 PORTRAIT card image (the same
*_HOMEPORTRAIT_BOTTOMGRADIENT* / *BG_141414-BOTTOM-GRADIENT* image the website grid uses, each
verified servable server-side on CloudFront 2026-06-18). The portrait is language-neutral: only the
overlaid name + subject + link change by language. House style: no em dash, no tatweel, Western
numerals only.

This is a data module imported by scripts/update_portrait_cards.py. It is not customer-facing copy.
"""

CF = "https://dt92b02v6m7lx.cloudfront.net/"

# slug -> {category, name_ar, name_en, subject_ar, subject_en, portrait}
# subject_* is the verbatim "Teaches <subject>" / "يعلّم|تعلّم <subject>" phrase from the page.
CARDS = {
    "bassam-fattouh-teaches-makeup": {
        "category": "design-style",
        "name_en": "Bassam Fattouh", "name_ar": "بسام فتّوح",
        "subject_en": "Teaches Makeup", "subject_ar": "يعلّم المكياج",
        "portrait": CF + "BF_HOMEPORTRAIT_BOTTOMGRADIENT_Fixed.webp",
    },
    "bassam-fattouh-teaches-bridal-makeup": {
        "category": "design-style",
        "name_en": "Bassam Fattouh", "name_ar": "بسام فتّوح",
        "subject_en": "Teaches Bridal Makeup", "subject_ar": "يعلّم مكياج العروس",
        "portrait": CF + "BFBRIDAL_HOMEPORTRAIT_BOTTOMGRADIENT_RECOLORED.webp",
    },
    "cedric-haddad-teaches-personal-styling": {
        "category": "design-style",
        "name_en": "Cedric Haddad", "name_ar": "سيدريك حدّاد",
        "subject_en": "Teaches Personal Styling", "subject_ar": "يعلّم تنسيق الملابس",
        "portrait": CF + "CH_HOMEPORTRAIT_BOTTOMGRADIENT.webp",
    },
    "elda-choucair-teaches-marketing": {
        "category": "business",
        "name_en": "Elda Choucair", "name_ar": "إلدا شقير",
        "subject_en": "Teaches Marketing", "subject_ar": "تعلّم التسويق",
        "portrait": CF + "EC_HOMEPORTRAIT_BOTTOMGRADIENT.webp",
    },
    "ragheb-alama-teaches-music-and-performance": {
        "category": "music",
        "name_en": "Ragheb Alama", "name_ar": "راغب علامة",
        "subject_en": "Teaches Music and Performance", "subject_ar": "يعلّم الموسيقى والأداء",
        "portrait": CF + "05032024_RaghebBG_141414-BOTTOM-GRADIENT-01.webp",
    },
    "kosai-khauli-teaches-acting": {
        "category": "acting",
        "name_en": "Kosai Khauli", "name_ar": "قصي خولي",
        "subject_en": "Teaches Acting", "subject_ar": "يعلّم التمثيل",
        "portrait": CF + "04032024_KosaiBG_141414-BOTTOM-GRADIENT-01.webp",
    },
    "rahma-riad-teaches-building-a-career-in-the-digital-age": {
        "category": "business",
        "name_en": "Rahma Riad", "name_ar": "رحمة رياض",
        "subject_en": "Teaches Building a Career in the Digital Age",
        "subject_ar": "تعلّم بناء مسيرة في العصر الرقمي",
        "portrait": CF + "RR_HOMEPORTRAIT_BOTTOMGRADIENT.webp",
    },
    "toufic-kreidieh-teaches-building-and-growing-your-business": {
        "category": "business",
        "name_en": "Toufic Kreidieh", "name_ar": "توفيق كريدية",
        "subject_en": "Teaches Building and Growing Your Business",
        "subject_ar": "يعلّم بناء وتنمية مشروعك",
        "portrait": CF + "TK_HOMEPORTRAIT_BOTTOMGRADIENT.webp",
    },
    "salam-dakkak-teaches-levantine-cooking": {
        "category": "cooking",
        "name_en": "Salam Dakkak", "name_ar": "سلام دقاق",
        "subject_en": "Teaches Levantine Home Cooking", "subject_ar": "تعلّم الطبخ المشرقي المنزلي",
        "portrait": CF + "11032024_SalamBG_141414-BOTTOM-GRADIENT-02.webp",
    },
}


def card_for(slug):
    """Build the full portrait-card spec object for a class slug (language-matched fields)."""
    d = CARDS[slug]
    base = "https://www.maharat.com/{lang}/class/" + d["category"] + "/" + slug
    return {
        "portrait_src": d["portrait"],
        "name_ar": d["name_ar"], "name_en": d["name_en"],
        "subject_ar": d["subject_ar"], "subject_en": d["subject_en"],
        "link_ar": base.format(lang="ar"), "link_en": base.format(lang="en"),
        "alt_ar": "صورة " + d["name_ar"] + ", " + d["subject_ar"] + " على مهارات",
        "alt_en": d["name_en"] + ", " + d["subject_en"] + " on Maharat, portrait",
    }
