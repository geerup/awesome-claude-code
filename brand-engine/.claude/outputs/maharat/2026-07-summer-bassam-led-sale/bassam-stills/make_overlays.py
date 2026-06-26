#!/usr/bin/env python3
"""
Maharat branded landscape-banner overlay renderer.

Bakes the brand treatment (near-black bottom scrim, white Maharat wordmark,
emerald eyebrow, white headline, optional instructor name+skill line) over each
normalized still. Arabic is shaped natively via Pillow+raqm (RTL, letter
joining, bidi); English is LTR.

Brand constants (CLAUDE.md / context/brand-voice.md):
  near-black #141414, card #1A1A1A, emerald #009975. No em dashes. Western numerals.

NOTE ON SCOPE: these are standalone branded landscape banners for web/promo use,
NOT email headers. Baked copy is appropriate here. (If a banner is ever repurposed
as an email header, the engine's text-free rule and Ortto-CDN hosting would apply.)

Usage:
  python3 make_overlays.py            # render every frame, both languages
  python3 make_overlays.py 04 ar      # render one frame + language (test)
"""
import json, os, sys
from PIL import Image, ImageDraw, ImageFont, ImageOps

BASE = os.path.dirname(os.path.abspath(__file__))
REPO = "/home/user/claude/.claude/context/brand-assets"
FONTS = {
    "ar_head":    f"{REPO}/fonts/lyon-arabic-display/LyonArabicDisplay-Black.otf",
    "ar_body":    f"{REPO}/fonts/29lt-azer/29LTAzer-Regular.otf",
    "ar_eyebrow": f"{REPO}/fonts/29lt-azer/29LTAzer-Black.otf",
    "en_head":    f"{REPO}/fonts/acumin-pro/AcuminPro-Bold.ttf",
    "en_body":    f"{REPO}/fonts/acumin-pro/AcuminPro-Regular.ttf",
    "en_eyebrow": f"{REPO}/fonts/acumin-pro/AcuminPro-Bold.ttf",
}
LOGO = f"{REPO}/logo/maharat-white.png"

NEAR_BLACK = (20, 20, 20)     # #141414
EMERALD    = (0, 153, 117)    # #009975
WHITE      = (255, 255, 255)
LIGHT      = (229, 229, 229)  # #E5E5E5

OUT_W, OUT_H = 1200, 630       # 1.91:1 web/promo landscape banner
S = OUT_W / 1200.0             # scale factor for type sizes


def fit_cover(im, w, h):
    im = ImageOps.exif_transpose(im).convert("RGB")
    sw, sh = im.size
    scale = max(w / sw, h / sh)
    nw, nh = int(round(sw * scale)), int(round(sh * scale))
    im = im.resize((nw, nh), Image.LANCZOS)
    left, top = (nw - w) // 2, (nh - h) // 2
    return im.crop((left, top, left + w, top + h))


def _ramp(h, frac, max_a, power, from_bottom):
    col = Image.new("L", (1, h), 0)
    px = col.load()
    if from_bottom:
        start = int(h * frac)
        for y in range(h):
            px[0, y] = 0 if y <= start else int(max_a * (((y - start) / (h - start)) ** power))
    else:
        end = int(h * frac)
        for y in range(h):
            px[0, y] = 0 if y >= end else int(max_a * ((1 - y / end) ** power))
    return col


def draw_scrim(base, max_a=235, top_frac=0.40):
    w, h = base.size
    flat = Image.new("RGB", (w, h), NEAR_BLACK)
    base.paste(flat, (0, 0), _ramp(h, top_frac, max_a, 1.5, True).resize((w, h)))  # bottom
    base.paste(flat, (0, 0), _ramp(h, 0.22, 130, 1.4, False).resize((w, h)))       # top (logo)
    return base


def font(key, size):
    return ImageFont.truetype(FONTS[key], max(1, int(size)))


def _txt_kwargs(rtl):
    return {"direction": "rtl", "features": ["kern", "liga", "calt"]} if rtl else {}


def wrap(draw, text, fnt, max_w, rtl):
    words, lines, cur = text.split(), [], ""
    for wd in words:
        trial = (cur + " " + wd).strip()
        wlen = draw.textlength(trial, font=fnt, **({"direction": "rtl"} if rtl else {}))
        if wlen <= max_w or not cur:
            cur = trial
        else:
            lines.append(cur); cur = wd
    if cur:
        lines.append(cur)
    return lines


def lh(fnt, mult=1.0):
    a, d = fnt.getmetrics()
    return int((a + d) * mult)


def place_logo(base, rtl, pad):
    if not os.path.exists(LOGO):
        print("WARN: logo not found", LOGO); return
    logo = Image.open(LOGO).convert("RGBA")
    th = int(34 * S)
    r = th / logo.height
    logo = logo.resize((int(logo.width * r), th), Image.LANCZOS)
    y = int(40 * S)
    x = (base.width - pad - logo.width) if rtl else pad
    base.alpha_composite(logo, (x, y)) if base.mode == "RGBA" else base.paste(logo, (x, y), logo)


def render(frame, lang):
    rtl = (lang == "ar")
    fam = "ar" if rtl else "en"
    src = os.path.join(BASE, frame["src"])
    base = fit_cover(Image.open(src), OUT_W, OUT_H)
    sc = frame.get("scrim") or {}
    draw_scrim(base, sc.get("max_a", 235), sc.get("top_frac", 0.40))
    place_logo(base, rtl, int(64 * S))
    draw = ImageDraw.Draw(base)

    pad = int(64 * S)
    x = (OUT_W - pad) if rtl else pad
    anchor = ("r" if rtl else "l") + "a"

    eyebrow  = (frame.get(f"eyebrow_{lang}") or "").strip()
    headline = (frame.get(f"headline_{lang}") or "").strip()
    name     = (frame.get(f"name_{lang}") or "").strip()

    f_eye  = font(f"{fam}_eyebrow", 25 * S)
    f_head = font(f"{fam}_head", (56 if rtl else 52) * S)
    f_name = font(f"{fam}_body", 29 * S)

    head_lines = wrap(draw, headline, f_head, int(OUT_W * 0.80), rtl)

    # build block top->bottom with per-element advance
    seq = []
    if eyebrow:
        seq.append((eyebrow, f_eye, EMERALD, lh(f_eye, 1.0) + int(14 * S)))
    for ln in head_lines:
        seq.append((ln, f_head, WHITE, lh(f_head, 1.06)))
    if name:
        seq.append((name, f_name, LIGHT, lh(f_name, 1.0) + int(10 * S)))
        # add a little gap before the name line
        # (applied by bumping the last headline advance)
    total = sum(adv for _, _, _, adv in seq)
    if name:
        total += int(8 * S)

    y = OUT_H - pad - total
    for i, (txt, fnt, fill, adv) in enumerate(seq):
        if name and i == len(seq) - 1:
            y += int(8 * S)  # breathing room above name
        draw.text((x, y), txt, font=fnt, fill=fill, anchor=anchor, **_txt_kwargs(rtl))
        y += adv

    out_dir = os.path.join(BASE, "branded")
    os.makedirs(out_dir, exist_ok=True)
    out = os.path.join(out_dir, f"{frame['id']}.{lang}.jpg")
    base.convert("RGB").save(out, quality=88, optimize=True)
    return out


def load():
    with open(os.path.join(BASE, "overlay-copy.json"), encoding="utf-8") as f:
        return json.load(f)["frames"]


def main():
    frames = load()
    if len(sys.argv) >= 3:
        fid, lang = sys.argv[1], sys.argv[2]
        fr = next(f for f in frames if f["id"] == fid)
        print(render(fr, lang)); return
    for fr in frames:
        for lang in ("ar", "en"):
            print(render(fr, lang))


if __name__ == "__main__":
    main()
