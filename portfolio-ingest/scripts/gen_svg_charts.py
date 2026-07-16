#!/usr/bin/env python3
"""Deterministic SVG chart generator for the rebuild pages.

Injects charts between <!-- SVGCHART:id --> ... <!-- /SVGCHART:id --> markers
in rebuild/stats.html and rebuild/index.html. Re-runnable: regenerates the
content between markers every run.

Form + color per the dataviz skill (emphasis form: one accent + grays).
Palette check (validate_palette.js, surface #EFE9DC, light):
  - #D2401E accent: CVD 23.4 / normal 36.0 vs ink - PASS; used for the story series
  - #2A251D / #948871 are deliberate de-emphasis grays (not categorical slots);
    the mute contrast WARN (2.88:1) is relieved by direct labels on every mark
    and a <details> data table per chart, as the validator prescribes.
Data verbatim from uploads/canonical-analytics-extract.md +
Social Media Reporting 2025.xlsx rows in full-folder-scan-extract.json.
"""
import re

ACCENT = '#D2401E'
INK = '#17140F'
INK2 = '#2A251D'
MID = '#6A604F'
MUTE = '#948871'
RULE = 'rgba(23,20,15,.14)'
RULE_SOFT = 'rgba(23,20,15,.08)'

# ---------------- data (verbatim) ----------------
MONTHLY = [  # (label, total)
    ('Jan 24', 2384748), ('Feb 24', 2409817), ('Mar 24', 2434279),
    ('Apr 24', 2470492), ('May 24', 2495456), ('Jun 24', 2518614),
    ('Jul 24', 2544690), ('Aug 24', 2570927), ('Sep 24', 2601221),
    ('Oct 24', 2627656), ('Nov 24', 2653477), ('Dec 24', 2709827),
    ('Jan 25', 2738003), ('Feb 25', 2765694), ('Mar 25', 2797709),
    ('Apr 25', 2813262),
]
MONTHLY_ANNO = {  # index -> (short label, tip extra)
    3: ('24.04 LTS · +36,339', 'Ubuntu 24.04 LTS launch month'),
    11: ('record · +56,350', 'Record net-growth month; 20 Years tail'),
    15: ('peak · 2.81M', 'Peak audience'),
}
ER = [('2022', 1.3), ('2023', 1.9), ('2024', 5.18)]
LI_ENG = [('2022', 203327, False), ('2023', 290445, False), ('2024', 974046, True), ('Q1 25', 271164, None)]  # True=accent, None=dim/context
LI_ADDS = [('2022', 46753, False), ('2023', 139519, False), ('2024', 201377, True), ('Q1 25', 66234, None)]
X_IMP = [('2022', 13739418), ('2023', 11113915), ('2024', 5522990)]
X_ADDS = [('2022', 53328, False), ('2023', 89393, False), ('2024', 81624, False)]

def fmt(n):
    n = float(n)
    if n >= 1_000_000: return f'{n/1_000_000:.2f}M'
    if n >= 10_000: return f'{n/1000:.0f}K'
    if n >= 1_000: return f'{n:,.0f}'
    return f'{n:g}'

def fmt_pct(n):
    return f'{float(n):g}%'

def fmt_full(n):
    return f'{n:g}' if isinstance(n, float) and n < 100 else f'{n:,}'

MONO = f'font-family:Geist Mono,ui-monospace,monospace'

def svg_open(w, h, cls='svgchart'):
    return (f'<svg class="{cls}" viewBox="0 0 {w} {h}" role="img" '
            f'style="width:100%;height:auto;display:block" '
            f'xmlns="http://www.w3.org/2000/svg">')

def gridlines(x0, x1, ys, labels):
    out = []
    for y, lab in zip(ys, labels):
        out.append(f'<line x1="{x0}" y1="{y:.1f}" x2="{x1}" y2="{y:.1f}" stroke="{RULE_SOFT}" stroke-width="1"/>')
        out.append(f'<text x="{x0-8}" y="{y+3.5:.1f}" text-anchor="end" style="{MONO};font-size:10px" fill="{MUTE}">{lab}</text>')
    return ''.join(out)

def details_table(id_, title, rows, unit=''):
    trs = ''.join(f'<tr><td>{a}</td><td style="text-align:right">{b}</td></tr>' for a, b in rows)
    return (f'<details class="chart-data"><summary>Data table</summary>'
            f'<table aria-label="{title}"><thead><tr><th>Period</th><th style="text-align:right">{unit or "Value"}</th></tr></thead>'
            f'<tbody>{trs}</tbody></table></details>')

def line_chart(id_, series, w=760, h=290, y0=None, y1=None, anno=None, yfmt=fmt,
               ml=62, mr=18, mt=18, mb=34, area=True, gridn=4, unit=''):
    anno = anno or {}
    vals = [v for _, v in series]
    lo = y0 if y0 is not None else min(vals)
    hi = y1 if y1 is not None else max(vals)
    span = hi - lo or 1
    px = lambda i: ml + i * (w - ml - mr) / (len(series) - 1)
    py = lambda v: mt + (h - mt - mb) * (1 - (v - lo) / span)
    pts = [(px(i), py(v)) for i, (_, v) in enumerate(series)]
    path = 'M' + 'L'.join(f'{x:.1f},{y:.1f}' for x, y in pts)
    gys = [mt + i * (h - mt - mb) / gridn for i in range(gridn + 1)]
    glabels = [yfmt(hi - i * span / gridn) for i in range(gridn + 1)]
    s = [svg_open(w, h)]
    s.append(gridlines(ml, w - mr, gys, glabels))
    s.append(f'<line x1="{ml}" y1="{h-mb}" x2="{w-mr}" y2="{h-mb}" stroke="{INK}" stroke-width="1"/>')
    if area:
        s.append(f'<path d="{path}L{pts[-1][0]:.1f},{h-mb}L{pts[0][0]:.1f},{h-mb}Z" fill="{ACCENT}" fill-opacity="0.09"/>')
    s.append(f'<path d="{path}" fill="none" stroke="{ACCENT}" stroke-width="2" stroke-linejoin="round" stroke-linecap="round"/>')
    # x labels: first, annotated, last (selective) for dense series; all if short
    label_ix = set([0, len(series) - 1]) | set(anno.keys()) if len(series) > 6 else set(range(len(series)))
    for i, ((lab, v), (x, y)) in enumerate(zip(series, pts)):
        if i in label_ix:
            s.append(f'<text x="{x:.1f}" y="{h-mb+16}" text-anchor="middle" style="{MONO};font-size:9.5px" fill="{MUTE}">{lab}</text>')
        if i in anno:
            short, _tip = anno[i]
            s.append(f'<circle cx="{x:.1f}" cy="{y:.1f}" r="4.5" fill="{ACCENT}" stroke="#EFE9DC" stroke-width="2"/>')
            ty = y - 12 if i != 0 else y - 12
            anchor = 'end' if i == len(series) - 1 else 'middle'
            tx = x - 2 if anchor == 'end' else x
            s.append(f'<text x="{tx:.1f}" y="{ty:.1f}" text-anchor="{anchor}" style="{MONO};font-size:10px;font-weight:600" fill="{INK2}">{short}</text>')
        # hover hit target (bigger than mark) + native tooltip fallback
        s.append(f'<g class="hit" data-tip="{lab}: {fmt_full(v)}{unit}"><circle cx="{x:.1f}" cy="{y:.1f}" r="12" fill="transparent"/></g>')
    s.append('</svg>')
    tbl = details_table(id_, id_, [(lab, fmt_full(v) + unit) for lab, v in series], unit='Value')
    return ''.join(s) + tbl

def col_chart(id_, series, w=760, h=270, yfmt=fmt, ml=62, mr=18, mt=26, mb=30, unit=''):
    """series: (label, value, emphasis) emphasis: True accent / False ink2 / None dim-context"""
    vals = [v for _, v, _ in series]
    hi = max(vals) * 1.06
    n = len(series)
    slot = (w - ml - mr) / n
    bw = min(slot * 0.56, 92)
    py = lambda v: mt + (h - mt - mb) * (1 - v / hi)
    gys = [mt + i * (h - mt - mb) / 4 for i in range(5)]
    glabels = [yfmt(hi - i * hi / 4) for i in range(5)]
    s = [svg_open(w, h)]
    s.append(gridlines(ml, w - mr, gys, glabels))
    s.append(f'<line x1="{ml}" y1="{h-mb}" x2="{w-mr}" y2="{h-mb}" stroke="{INK}" stroke-width="1"/>')
    for i, (lab, v, emph) in enumerate(series):
        x = ml + slot * i + (slot - bw) / 2
        top = py(v)
        color = ACCENT if emph else (MUTE if emph is None else INK2)
        r = 4
        bh = (h - mb) - top
        if bh < r: r = max(bh, 0)
        s.append(f'<path d="M{x:.1f},{h-mb}V{top+r:.1f}Q{x:.1f},{top:.1f} {x+r:.1f},{top:.1f}H{x+bw-r:.1f}Q{x+bw:.1f},{top:.1f} {x+bw:.1f},{top+r:.1f}V{h-mb}Z" fill="{color}"/>')
        lab_fill = ACCENT if emph else MID
        s.append(f'<text x="{x+bw/2:.1f}" y="{top-7:.1f}" text-anchor="middle" style="{MONO};font-size:10.5px;font-weight:600" fill="{lab_fill}">{fmt_full(v)}</text>')
        s.append(f'<text x="{x+bw/2:.1f}" y="{h-mb+16}" text-anchor="middle" style="{MONO};font-size:10px" fill="{MUTE}">{lab}</text>')
        s.append(f'<g class="hit" data-tip="{lab}: {fmt_full(v)}{unit}"><rect x="{x-4:.1f}" y="{mt}" width="{bw+8:.1f}" height="{h-mt-mb}" fill="transparent"/></g>')
    s.append('</svg>')
    tbl = details_table(id_, id_, [(lab, fmt_full(v) + unit) for lab, v, _ in series])
    return ''.join(s) + tbl

# ---------------- chart assembly ----------------
def block(title, src, inner, note=''):
    n = f'<p class="axis-note">{note}</p>' if note else ''
    return (f'\n<div class="chart-block">\n<p class="chart-title">{title}</p>\n'
            f'<p class="chart-src">{src}</p>\n{inner}\n{n}\n</div>\n')

charts = {}

charts['s1'] = block(
    'Total audience, month by month · Jan 2024 - Apr 2025 peak',
    'Source: Social Media Reporting 2025.xlsx, audience growth trackers',
    line_chart('s1', MONTHLY, y0=2_300_000, y1=2_860_000, anno=MONTHLY_ANNO),
    'Y-axis starts at 2.30M to show monthly movement. Sixteen consecutive data points of net growth, and the spikes are event-led: April 2024 is the Ubuntu 24.04 LTS launch month, December 2024 is the record month on the 20 Years campaign tail, April 2025 is the 2.81M peak.')

charts['s2'] = block(
    'Organic engagement rate, full-year · the quality curve',
    'Source: Sprout Social; 2023 figure from the Vancouver Sprint 2024 deck (1.3% +47% = 1.9%)',
    line_chart('s2', ER, w=560, h=230, y0=0, y1=6, gridn=3, unit='%', area=True, yfmt=fmt_pct),
    'Rate nearly tripled 2023 to 2024 while post volume fell - the efficiency story in one line.')

charts['s3'] = block(
    'LinkedIn engagements by year',
    'Source: Sprout Social profile performance, May 2022 - Mar 2025',
    col_chart('s3', LI_ENG),
    '2023 to 2024: +235%. Q1 2025 (muted, three months only) delivered more than full-year 2022.')

charts['s4'] = block(
    'Net new LinkedIn followers by year',
    'Source: Sprout Social profile performance',
    col_chart('s4', LI_ADDS),
    'Every year added more than the year before. 2023 alone: +90% YoY (Vancouver Sprint deck).')

charts['s5'] = block(
    'X, the managed decline · reach fell with the platform, audience held',
    'Source: Sprout Social profile performance (two panels, one axis each - never a dual axis)',
    '<div style="display:grid;grid-template-columns:repeat(auto-fit,minmax(280px,1fr));gap:28px">'
    + '<div><p class="chart-title" style="margin-bottom:8px">Impressions</p>'
    + line_chart('s5a', X_IMP, w=380, h=210, y0=0, y1=15_000_000, gridn=3)
    + '</div><div><p class="chart-title" style="margin-bottom:8px">Net new followers</p>'
    + col_chart('s5b', X_ADDS, w=380, h=210)
    + '</div></div>',
    'Posts were cut 40% (1,007 to 607) as reach declined platform-wide - yet the account still added 81,624 followers in 2024. Reallocation, not neglect.')

charts['s6'] = block(
    'The audience curve under this case',
    'Source: Social Media Reporting 2025.xlsx · full chart on the Numbers page',
    line_chart('s6', MONTHLY, w=680, h=200, y0=2_300_000, y1=2_860_000, gridn=2,
               anno={3: ('LTS', 'launch'), 11: ('record', 'best month'), 15: ('2.81M', 'peak')}),
    '')

TIP_JS = '''<script>
(function(){
  var tip = document.createElement('div');
  tip.style.cssText = 'position:fixed;pointer-events:none;z-index:99;background:#17140F;color:#EFE9DC;font:11px/1.5 "Geist Mono",monospace;padding:5px 9px;border-radius:3px;opacity:0;transition:opacity .12s';
  document.body.appendChild(tip);
  document.addEventListener('mouseover', function(e){
    var g = e.target.closest && e.target.closest('.hit');
    if (g && g.dataset.tip) { tip.textContent = g.dataset.tip; tip.style.opacity = 1; }
    else tip.style.opacity = 0;
  });
  document.addEventListener('mousemove', function(e){
    if (tip.style.opacity == 1) { tip.style.left = (e.clientX + 14) + 'px'; tip.style.top = (e.clientY - 30) + 'px'; }
  });
})();
</script>'''

TABLE_CSS = '''<style>
.chart-data{margin-top:8px}
.chart-data summary{font-family:'Geist Mono',ui-monospace,monospace;font-size:10px;letter-spacing:.08em;text-transform:uppercase;color:#948871;cursor:pointer}
.chart-data table{border-collapse:collapse;font-size:12px;margin-top:8px;font-family:'Geist Mono',ui-monospace,monospace}
.chart-data th,.chart-data td{padding:4px 14px 4px 0;border-bottom:1px solid rgba(23,20,15,.08);text-align:left;color:#2A251D}
.chart-data th{font-size:10px;text-transform:uppercase;letter-spacing:.08em;color:#948871}
</style>'''

def inject(path, ids):
    s = open(path, encoding='utf-8').read()
    for cid in ids:
        m = re.search(f'<!-- SVGCHART:{cid} -->.*?<!-- /SVGCHART:{cid} -->', s, re.S)
        assert m, f'{path}: marker {cid} missing'
        s = s.replace(m.group(0), f'<!-- SVGCHART:{cid} -->{charts[cid]}<!-- /SVGCHART:{cid} -->')
    # ensure helper JS + table CSS present once
    if 'chart-data summary' not in s:
        s = s.replace('</head>', TABLE_CSS + '\n</head>')
    if 'position:fixed;pointer-events:none;z-index:99' not in s:
        s = s.replace('</body>', TIP_JS + '\n</body>')
    open(path, 'w', encoding='utf-8').write(s)
    print(f'{path}: injected {ids}')

if __name__ == '__main__':
    inject('rebuild/stats.html', ['s1', 's2', 's3', 's4', 's5'])
    inject('rebuild/index.html', ['s6'])
