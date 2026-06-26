#!/usr/bin/env python3
"""Rewrite each Maharat email build spec's class_cards to the PORTRAIT instructor-card structure.

Reads the canonical portrait-card data (scripts/_portrait_cards_data.py) and, for every build spec,
replaces each existing "our other classes" card with the portrait card for the SAME instructor (the
team's three OTHER-instructor choices and order are preserved, only the structure changes: a
text-free portrait + name + "Teaches <subject>" overlay + language-matched link). The instructor is
detected from the existing card's link/alt slug, so no choice is invented. Also refreshes the
class_cards_note and the ClassCardGrid open_items line to describe the portrait cards. Idempotent.

House style: writes no em dash, en dash, tatweel, or Eastern numerals.

Usage:
  python3 .claude/scripts/update_portrait_cards.py            # rewrite all known specs
  python3 .claude/scripts/update_portrait_cards.py --check    # report, write nothing
"""
import json
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from _portrait_cards_data import CARDS, card_for  # noqa: E402

ROOT = Path(__file__).resolve().parents[1]
SPECS = [
    "outputs/2026-06-bassam-fattouh-makeup/email-7step/bassam-fattouh/spec.json",
    "outputs/2026-06-bassam-fattouh-makeup/email-html/emails.spec.json",
    "outputs/2026-06-bassam-fattouh-bridal-makeup/email-7step/bassam-fattouh-bridal/spec.json",
    "outputs/2026-06-ragheb-alama-music/email-7step/ragheb-alama/spec.json",
    "outputs/2026-06-kosai-khauli-acting/email-7step/kosai-khauli/spec.json",
    "outputs/2026-06-rahma-riad-digital-career/email-7step/rahma-riad/spec.json",
    "outputs/2026-06-toufic-kredieh-business/email-7step/toufic-kredieh/spec.json",
    "outputs/2026-06-cedric-haddad-styling/email-7step/cedric-haddad/spec.json",
    "outputs/2026-06-elda-choucair-marketing/email-7step/elda-choucair/spec.json",
    "outputs/2026-06-salam-dakkak-cooking/email-7step/salam-dakkak/spec.json",
]

NOTE = ("Three OTHER Maharat classes (not this email's instructor) as PORTRAIT instructor cards: a "
        "text-free on-brand near-black portrait (the same image the maharat.com instructor grid "
        "uses), an emerald accent rule, the instructor name, and the page-cleared Teaches subject "
        "phrase as a LIVE HTML overlay in the lower third (never baked into the image), each linking "
        "to its language-matched class page. Portraits verified servable on CloudFront 2026-06-18; "
        "they stage to the Ortto CDN before any send, the same as the hero.")

OPEN_RE = re.compile(r"The 'our other classes' ClassCardGrid")


def slug_from_card(c):
    """Detect the class slug from an existing card's link (or alt as a fallback)."""
    for key in ("link_ar", "link_en", "link"):
        link = c.get(key, "")
        m = re.search(r"/class/[a-z-]+/([a-z0-9-]+)", link)
        if m and m.group(1) in CARDS:
            return m.group(1)
    return None


def convert(cards):
    out, missing = [], []
    for c in cards:
        # Already portrait-shaped and resolvable: re-derive from its slug for a clean, canonical row.
        slug = slug_from_card(c)
        if not slug:
            missing.append(c)
            out.append(c)
            continue
        out.append(card_for(slug))
    return out, missing


def main(argv):
    check = "--check" in argv
    changed = 0
    for rel in SPECS:
        p = ROOT / rel
        if not p.exists():
            print("  SKIP (missing): " + rel)
            continue
        spec = json.loads(p.read_text(encoding="utf-8"))
        cards = spec.get("class_cards")
        if not cards:
            print("  SKIP (no top-level class_cards): " + rel)
            continue
        new_cards, missing = convert(cards)
        if missing:
            print("  WARN: " + rel + " has " + str(len(missing))
                  + " card(s) with an unrecognized class slug; left as-is.")
        spec["class_cards"] = new_cards
        spec["class_cards_note"] = NOTE
        # Refresh the ClassCardGrid open_items line if present.
        ois = spec.get("open_items", [])
        for i, o in enumerate(ois):
            if OPEN_RE.search(o):
                names = ", ".join(slug_from_card(c) or "?" for c in new_cards)
                ois[i] = ("The 'our other classes' ClassCardGrid is now PORTRAIT instructor cards: "
                          "three OTHER classes (" + names + "), each a text-free on-brand portrait "
                          "with the instructor name and the Teaches subject phrase as a live HTML "
                          "overlay, language-matched, linking to its class page. Portraits are the "
                          "maharat.com grid images, verified servable on CloudFront; stage to Ortto "
                          "before send.")
        names = " / ".join((slug_from_card(c) or "?") for c in new_cards)
        print(("  ok " if not check else "  would update ") + rel + "  ->  " + names)
        if not check:
            p.write_text(json.dumps(spec, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
        changed += 1
    print(("CHECK: " if check else "DONE: ") + str(changed) + " spec(s) "
          + ("to update." if check else "updated to portrait cards."))
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
