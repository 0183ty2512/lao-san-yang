"""Shared HTML for the course index, lesson reader, and navigation drawer."""
from html import escape
from datetime import date


ICON_PATHS = {
    "contents": '<path d="M8 6h12M8 12h12M8 18h12"/><path d="M3.5 6h.1m-.1 6h.1m-.1 6h.1"/>',
    "type": '<path d="m2 18 5-13 5 13M4 14h6m4 4 3.5-9L21 18m-5.8-3h4.5"/>',
    "sun": '<circle cx="12" cy="12" r="4"/><path d="M12 2v2m0 16v2M2 12h2m16 0h2M5 5l1.5 1.5m11 11L19 19M5 19l1.5-1.5m11-11L19 5"/>',
    "moon": '<path d="M20 15.1A8.5 8.5 0 0 1 8.9 4 8.6 8.6 0 1 0 20 15.1Z"/>',
    "close": '<path d="m6 6 12 12M18 6 6 18"/>',
    "arrow": '<path d="M4 12h15m-6-6 6 6-6 6"/>',
    "back": '<path d="M20 12H5m6-6-6 6 6 6"/>',
    "download": '<path d="M12 3v12m-4-4 4 4 4-4M4 16v4h16v-4"/>',
    "clock": '<circle cx="12" cy="12" r="8.5"/><path d="M12 7v5l3.5 2"/>',
    "search": '<circle cx="10" cy="10" r="6.5"/><path d="m15 15 5 5"/>',
}


def icon(name, class_name=""):
    return (f'<svg class="{class_name}" width="18" height="18" viewBox="0 0 24 24" '
            'aria-hidden="true" fill="none" stroke="currentColor" stroke-width="1.7" '
            f'stroke-linecap="round" stroke-linejoin="round">{ICON_PATHS[name]}</svg>')


BRAND = '''<svg class="brand-mark" width="34" height="34" viewBox="0 0 36 36" aria-hidden="true" fill="none">
<rect width="36" height="36" rx="10" fill="currentColor"/>
<g stroke="white" stroke-width="1.45" stroke-linecap="round">
<path d="M5 17c5-8 10-9 16-4s8 4 11 1M4 22c6-9 13-11 18-6s7 5 10 2M6 26c5-7 11-10 16-6s6 4 8 3"/>
</g></svg>'''


def contours():
    # Nested isobars around two pressure centres, clipped at the panel edges.
    rings = []
    for x, y, tilt, size in [(305, 82, -22, 1), (54, 259, 18, .84)]:
        for level in range(1, 12):
            a = (13 + level * 13) * size
            b = (8 + level * 9) * size
            rings.append(f'<path transform="translate({x} {y}) rotate({tilt})" d="M {-a:.1f} 0 '
                         f'C {-1.12*a:.1f} {-b:.1f} {-.21*a:.1f} {-1.18*b:.1f} {.43*a:.1f} {-b:.1f} '
                         f'S {1.21*a:.1f} {-.35*b:.1f} {a:.1f} {.3*b:.1f} '
                         f'S {.3*a:.1f} {1.06*b:.1f} {-.41*a:.1f} {.83*b:.1f} '
                         f'S {-a:.1f} {.34*b:.1f} {-a:.1f} 0Z"/>')
    return ('<svg class="contours" viewBox="0 0 430 250" fill="none" stroke="currentColor" '
            'stroke-width="1.1" focusable="false" aria-hidden="true">'+''.join(rings)+'</svg>')


def toolbar():
    return f'''<header class="site-header"><div class="bar-inner">
<a class="brand" href="index.html" aria-label="大气研习，返回50日复习首页">{BRAND}<span class="brand-title">大气研习</span></a>
<nav class="toolbar" aria-label="阅读工具">
<button type="button" id="toc-toggle" class="tool-button" aria-haspopup="dialog" aria-controls="toc-dialog" aria-expanded="false">{icon("contents")}<span class="button-label">目录</span></button>
<button type="button" id="font-toggle" class="tool-button" aria-controls="font-panel" aria-expanded="false" aria-label="调节阅读字号">{icon("type")}<span class="button-label">字号</span></button>
<div id="font-panel" hidden role="group" aria-label="阅读字号"><strong>阅读字号</strong><div class="font-controls">
<button type="button" id="font-minus" aria-label="减小字号">−</button><output id="font-value" aria-live="polite">18 px</output>
<button type="button" id="font-plus" aria-label="增大字号">＋</button></div><button type="button" id="font-reset">恢复默认</button></div>
<button type="button" id="theme-toggle" class="tool-button" aria-label="切换明暗主题">{icon("moon","theme-light")}{icon("sun","theme-dark")}<span class="button-label">主题</span></button>
</nav></div></header>'''


def toc_entry(link, label, meta, level, current=False):
    active = ' aria-current="page"' if current else ''
    detail = f'<span class="entry-meta">{escape(meta)}</span>' if meta else ''
    return (f'<a class="toc-entry" data-level="{level}" href="{escape(link)}"{active}>'
            f'<span class="entry-label">{escape(label)}</span>{detail}</a>')


def drawer(manifest, day, sections):
    days = ''.join(toc_entry(f'D{m["day"]:02}.html', f'D{m["day"]:02} · {m["title"]}',
                             m['date'], 2, m['day'] == day) for m in manifest)
    outline = ''.join(toc_entry('#'+entry['id'], entry['label'], entry['meta'], entry['level'])
                      for entry in sections)
    section_button = ('<button id="toc-sections-tab" type="button" data-list="sections" '
                      'role="tab" aria-controls="toc-sections" aria-selected="true">本日内容</button>') if day else ''
    day_pressed = 'false' if day else 'true'
    return f'''<dialog id="toc-dialog" aria-labelledby="toc-title">
<div class="drawer-head"><h2 id="toc-title">快速目录</h2><button type="button" id="toc-close" aria-label="关闭目录">{icon("close")}</button></div>
<div class="drawer-tabs" role="tablist" aria-label="目录范围">{section_button}<button id="toc-days-tab" data-list="days" role="tab" aria-controls="toc-days" aria-selected="{day_pressed}" type="button">50天日程</button></div>
<div class="drawer-search"><input type="search" id="toc-search" aria-label="搜索目录" placeholder="搜索题号、主题或日期" autocomplete="off"></div>
<nav class="drawer-list" aria-label="跳转列表"><div id="toc-sections" role="tabpanel" aria-label="本日内容"{'' if day else ' hidden'}>{outline}</div><div id="toc-days" role="tabpanel" aria-labelledby="toc-days-tab"{' hidden' if day else ''}>{days}</div>
<p id="toc-empty" class="empty-state" hidden>没有匹配项，试试其他题号或关键词。</p></nav></dialog>'''


def page(title, body, manifest, day=None, sections=(), asset_version=''):
    return f'''<!doctype html>
<html lang="zh-CN"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>{escape(title)} · 大气研习</title><script src="theme.js?v={asset_version}"></script><link rel="stylesheet" href="style.css?v={asset_version}">
<noscript><style>.toolbar,.drawer-tabs{{display:none}}</style></noscript></head>
<body class="page-{'day' if day else 'index'}">{toolbar()}<main class="shell">{body}</main>
<footer class="site-footer"><a href="index.html">大气研习 · 50日复习计划</a></footer>{drawer(manifest,day,sections)}</body></html>'''


def lesson_header(item, last_day):
    day = item['day']
    previous = (f'<a href="D{day-1:02}.html">{icon("back")} 上一天</a>' if day > 1 else '')
    following = (f'<a href="D{day+1:02}.html">下一天 {icon("arrow")}</a>' if day < last_day else '')
    return f'''<section class="lesson-hero" id="lesson-start" tabindex="-1">{contours()}
<p class="eyebrow">D{day:02} / {last_day} <span aria-hidden="true">·</span> <time datetime="{item["date"]}">{item["date"].replace("-",".")}</time></p>
<h1>{escape(item['title'])}</h1><div class="hero-meta"><span>{icon("clock")} 4 小时</span><span>动力 40% · 天气 40% · 物理 20%</span></div>
<nav class="lesson-actions" aria-label="日课导航">{previous}{following}<a href="md/D{day:02}.md" download>{icon("download")} 下载 MD</a></nav></section>'''


def index_body(manifest, review):
    cards = []
    for item in manifest:
        number = f'D{item["day"]:02}'
        month_day = date.fromisoformat(item["date"]).strftime('%m.%d')
        cards.append(f'''<a class="card" data-date="{item["date"]}" data-day="{number}" href="{number}.html">
<div class="card-meta"><span class="card-day">{number}</span><time class="card-date" datetime="{item["date"]}">{month_day}</time></div>
<span class="card-title">{escape(item["title"])}</span><span class="card-arrow">{icon("arrow")}</span></a>''')
    return f'''<section class="hero">{contours()}<p class="eyebrow">2026.10.29 — 12.17</p>
<h1>大气科学<span>50日复习计划</span></h1><p class="hero-meta">每天四小时，复习动力气象、天气学与大气物理。</p>
<a href="D01.html" class="hero-action" id="open-today"><span data-action-label>从 D01 开始</span>{icon("arrow")}</a></section>
<section aria-labelledby="catalog-title"><div class="catalog-head"><h2 id="catalog-title">每日课程</h2>
<input id="search" type="search" aria-label="搜索课程" placeholder="搜索天数、日期或知识点"></div>
<div class="grid">{''.join(cards)}</div><p class="empty-state" id="catalog-empty" hidden>没有找到课程，试试其他日期或知识点。</p></section>{review}'''
