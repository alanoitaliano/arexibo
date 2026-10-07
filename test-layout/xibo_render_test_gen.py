#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Generate Xibo CMS 4.5 layout import ZIPs for widget rendering tests.

Each output ZIP has the same structure as a Xibo layout export
(layout.json + mapping.json + library/*) and imports as one layout.
Every layout is a grid of cells; each cell = caption + one widget variant.

Examples:
  xibo_render_test_gen.py --orientation portrait
  xibo_render_test_gen.py --orientation both --out ./rt
  xibo_render_test_gen.py --orientation landscape --only "clock-*,text"
  xibo_render_test_gen.py --list
  xibo_render_test_gen.py --validate-defs ./xibo-cms-4.5.0/modules
"""
from __future__ import annotations

import argparse
import csv
import fnmatch
import html
import json
import re
import struct
import sys
import time
import xml.etree.ElementTree as ET
import zipfile
import zlib
from dataclasses import dataclass, field
from datetime import datetime
from pathlib import Path
from typing import Callable

REF_VERSION = "4.5.0"          # module definitions the options were checked against
OWNER_ID, OWNER_NAME = 1, "admin"
FOLDER_ID, FOLDER_NAME = 1, "/"
LAYOUT_SCHEMA = 4
FAR_FUTURE = 2147483647
DEFAULT_DURATION = 60
BG_COLOR = "#dfe3e8"
MARGIN, GUTTER, CAPTION_H, PAD = 20, 16, 56, 12
DEFAULT_GRID = {"portrait": (2, 3), "landscape": (3, 2)}   # (cols, rows)

# widget schema versions and cdata options (cdata <=> property type code/richText)
SCHEMA = {
    "text": 1, "image": 1, "spacer": 1, "embedded": 1, "global": 1,
    "clock-digital": 2, "clock-analogue": 2, "clock-flip": 2,
    "countdown-clock": 2, "countdown-custom": 2, "countdown-days": 2,
    "countdown-table": 2, "countdown-text": 2,
    "worldclock-analogue": 2, "worldclock-digital-custom": 2,
    "worldclock-digital-date": 2, "worldclock-digital-text": 2,
    "interactive-button": 2, "interactive-link": 2,
}
CDATA_OPTIONS = {
    "text": {"text", "javaScript", "styleSheet"},
    "clock-digital": {"format"},
    "countdown-custom": {"mainTemplate", "styleSheet"},
    "worldclock-digital-custom": {"template_html", "template_style"},
    "embedded": {"embedHtml", "embedStyle", "embedJavaScript", "embedScript"},
}
NON_DEF_OPTIONS = {"enableStat", "name", "uri"}   # not in module property definitions


# ----------------------------------------------------------------- assets
@dataclass(frozen=True)
class Asset:
    name: str
    w: int
    h: int
    idx: int


ASSETS = {a.name: a for a in (
    Asset("rt_wide_2x1.png", 800, 400, 1),
    Asset("rt_tall_1x2.png", 400, 800, 2),
    Asset("rt_square_1x1.png", 512, 512, 3),
)}


def _pixel(x: int, y: int, w: int, h: int):
    m = max(24, min(w, h) // 8)
    if y < m and x < m:
        return (214, 40, 40)            # TL red
    if y < m and x >= w - m:
        return (46, 160, 67)            # TR green
    if y >= h - m and x < m:
        return (30, 80, 220)            # BL blue
    if y >= h - m and x >= w - m:
        return (245, 200, 20)           # BR yellow
    if x < 8 or y < 8 or x >= w - 8 or y >= h - 8:
        return (0, 0, 0) if ((x // 16 + y // 16) % 2 == 0) else (255, 255, 255)
    if abs(x - w // 2) < 2 or abs(y - h // 2) < 2:
        return (0, 0, 0)
    d = ((x - w / 2) ** 2 + (y - h / 2) ** 2) ** 0.5
    if abs(d - min(w, h) * 0.3) < 3:
        return (0, 0, 0)
    if x % 100 == 0 or y % 100 == 0:
        return (255, 255, 255)
    return (int(40 + 200 * x / w), int(40 + 200 * y / h), 190)


def make_png(w: int, h: int) -> bytes:
    """Test-pattern PNG (stdlib only): coloured corners, border, crosshair, grid."""
    def chunk(tag: bytes, data: bytes) -> bytes:
        return (struct.pack(">I", len(data)) + tag + data
                + struct.pack(">I", zlib.crc32(tag + data) & 0xFFFFFFFF))
    raw = bytearray()
    for y in range(h):
        raw.append(0)
        for x in range(w):
            raw.extend(_pixel(x, y, w, h))
    return (b"\x89PNG\r\n\x1a\n"
            + chunk(b"IHDR", struct.pack(">IIBBBBB", w, h, 8, 2, 0, 0, 0))
            + chunk(b"IDAT", zlib.compress(bytes(raw), 9))
            + chunk(b"IEND", b""))


# ----------------------------------------------------------- check model
@dataclass(frozen=True)
class Check:
    kind: str                  # ATTESO (derived from options/definitions) | OSSERVA (record what happens)
    text: str
    src: str                   # where the expectation comes from
    covers: frozenset = frozenset()


def A(text, src, *covers):
    return Check("ATTESO", text, src, frozenset(covers))


def O(text, src, *covers):
    return Check("OSSERVA", text, src, frozenset(covers))


# --------------------------------------------------------------- variants
@dataclass
class Variant:
    label: str
    wtype: str
    opts: dict = field(default_factory=dict)
    media: tuple = ()
    duration: int = DEFAULT_DURATION
    expect: tuple = ()


@dataclass
class CanvasVariant:
    label: str
    element: str
    props: dict = field(default_factory=dict)
    media: str | None = None
    expect: tuple = ()


@dataclass
class Family:
    name: str
    kind: str                      # "grid" | "canvas"
    desc: str
    build: Callable[[], list]


FAMILIES: dict[str, Family] = {}


def family(name: str, kind: str, desc: str):
    def deco(fn):
        FAMILIES[name] = Family(name, kind, desc, fn)
        return fn
    return deco


GRAD = '{"type":"linear","color1":"#222222","color2":"#eee","angle":0}'
GRAD2 = '{"type":"linear","color1":"#d32f2f","color2":"#1976d2","angle":45}'


def _p(txt, size=40, color="#111111", align="left", style=""):
    return (f'<p style="text-align:{align};"><span style="font-size:{size}px;'
            f'color:{color};{style}">{html.escape(txt)}</span></p>')


# ----------------------------------------------------------------- text
@family("text", "grid", "Rich Text: styles, alignment, backgrounds, marquee/paged effects, CSS/JS")
def _text():
    sample = "Rendering test 0123456789 àèìòù €"
    long_ = "Long text to exercise marquee scrolling: " + "lorem ipsum dolor sit amet, " * 6
    multi = (_p("Line one", 44) + _p("Line two àèìòù €", 44, "#c62828")
             + _p("Line three", 44, "#1565c0") + _p("Line four", 44, "#2e7d32"))
    v = [
        Variant("base 40px left", "text", {"text": _p(sample)}),
        Variant("center 56px bold", "text", {"text": _p(sample, 56, align="center", style="font-weight:700;")}),
        Variant("right 28px italic underline", "text",
                {"text": _p(sample, 28, align="right", style="font-style:italic;text-decoration:underline;")}),
        Variant("white on #1565c0 (backgroundColor)", "text",
                {"text": _p(sample, 44, "#ffffff", "center"), "backgroundColor": "#1565c0"}),
        Variant("semi-transparent bg rgba", "text",
                {"text": _p(sample, 44, "#000000", "center"), "backgroundColor": "rgba(255,193,7,0.6)"}),
        Variant("multi paragraph", "text", {"text": multi}),
    ]
    for eff, txt, speed in (("marqueeLeft", _p(long_), 3), ("marqueeRight", _p(long_), 3),
                            ("marqueeUp", multi, 2), ("marqueeDown", multi, 2)):
        v.append(Variant(f"effect={eff} speed={speed}", "text", {"text": txt, "effect": eff, "speed": speed}))
    v += [
        Variant("effect=none (explicit)", "text", {"text": multi, "effect": "none"}),
        Variant("effect=fade (paged, 1000 ms)", "text", {"text": multi, "effect": "fade", "speed": 1000}),
        Variant("effect=scrollVert (paged, 1000 ms)", "text", {"text": multi, "effect": "scrollVert", "speed": 1000}),
        Variant("custom styleSheet", "text",
                {"text": _p(sample, 44), "seeAdvancedFields": 1,
                 "styleSheet": "p{text-shadow:3px 3px 6px #888;letter-spacing:4px;}"},
                expect=(A("Il testo ha un'ombra grigia (3px 3px, sfocatura 6px, #888) e spaziatura tra lettere di 4px",
                          "CSS applicato (styleSheet)", "styleSheet"),)),
        Variant("custom javaScript (turns red @0.5s)", "text",
                {"text": _p(sample, 44), "seeAdvancedFields": 1,
                 "javaScript": "setTimeout(function(){var e=document.querySelector('p span');"
                               "if(e){e.style.color='#c62828';}},500);"},
                expect=(A("Dopo circa 0,5 s il testo passa da nero (#111111) a rosso (#c62828)",
                          "JavaScript applicato (javaScript)", "javaScript"),
                        O("Se il testo resta nero registrarlo: il selettore 'p span' potrebbe non trovare l'elemento "
                          "nel DOM del widget", "non determinabile dalle definizioni", "javaScript"))),
    ]
    return v


# ---------------------------------------------------------------- image
@family("image", "grid", "Image: scaleType x alignment with 2:1, 1:2 and 1:1 test images")
def _image():
    v = []
    for st in ("center", "stretch", "fit"):
        for a, va in (("center", "middle"), ("left", "top"), ("right", "bottom")):
            v.append(Variant(f"wide 2:1 | {st} | {a}/{va}", "image",
                             {"scaleType": st, "alignId": a, "valignId": va, "uri": "rt_wide_2x1.png"},
                             media=("rt_wide_2x1.png",)))
    for name, tag in (("rt_tall_1x2.png", "tall 1:2"), ("rt_square_1x1.png", "square 1:1")):
        for st in ("center", "stretch", "fit"):
            v.append(Variant(f"{tag} | {st} | center/middle", "image",
                             {"scaleType": st, "alignId": "center", "valignId": "middle", "uri": name},
                             media=(name,)))
    return v


# -------------------------------------------------------------- clocks
def _fmt(tok, size=48, color="#1c1c1c", extra="", align="center"):
    return (f'<p style="margin:0;text-align:{align};"><span style="font-size:{size}px;'
            f'color:{color};{extra}">[{tok}]</span></p>')


@family("clock-digital", "grid", "Clock - Digital: formats, locales, offsets, sizes")
def _clock_digital():
    v = []
    for tok in ("HH:mm", "HH:mm:ss", "hh:mm:ss A", "DD/MM/YYYY", "LT", "LTS", "L", "LL", "LLL", "LLLL"):
        v.append(Variant(f"format [{tok}]", "clock-digital", {"format": _fmt(tok, 44)}))
    for lang in ("it", "en-gb", "de", "fr", "es"):
        v.append(Variant(f"lang={lang} dddd D MMMM YYYY", "clock-digital",
                         {"format": _fmt("dddd D MMMM YYYY", 36), "lang": lang}))
    v += [
        Variant("offset=+120 min", "clock-digital", {"format": _fmt("HH:mm:ss", 48), "offset": 120}),
        Variant("offset=-300 min", "clock-digital", {"format": _fmt("HH:mm:ss", 48), "offset": -300}),
        Variant("size 24px", "clock-digital", {"format": _fmt("HH:mm:ss", 24)}),
        Variant("size 96px", "clock-digital", {"format": _fmt("HH:mm", 96)}),
        Variant("bold red", "clock-digital", {"format": _fmt("HH:mm:ss", 56, "#c62828", "font-weight:700;")}),
        Variant("two lines time+date", "clock-digital",
                {"format": _fmt("HH:mm", 56, "#1c1c1c", "font-weight:700;")
                           + _fmt("DD/MM/YYYY", 32, "#455a64")}),
    ]
    return v


@family("clock-analogue", "grid", "Clock - Analogue: themes, alignment, offsets")
def _clock_analogue():
    v = []
    for th in ("1", "2"):
        for ah, av in (("center", "middle"), ("left", "top"), ("right", "bottom")):
            v.append(Variant(f"theme={th} | {ah}/{av}", "clock-analogue",
                             {"themeId": th, "alignmentH": ah, "alignmentV": av}))
    v.append(Variant("theme=1 offset=+180", "clock-analogue", {"themeId": "1", "offset": 180}))
    v.append(Variant("theme=2 offset=-300", "clock-analogue", {"themeId": "2", "offset": -300}))
    return v


@family("clock-flip", "grid", "Clock - Flip: faces, seconds, colours")
def _clock_flip():
    v = []
    for face in ("TwelveHourClock", "TwentyFourHourClock"):
        for sec in (0, 1):
            v.append(Variant(f"{face} showSeconds={sec}", "clock-flip",
                             {"clockFace": face, "showSeconds": sec}))
    for face in ("HourlyCounter", "MinuteCounter", "DailyCounter"):
        v.append(Variant(face, "clock-flip", {"clockFace": face}))
    v.append(Variant("24h custom colours", "clock-flip",
                     {"clockFace": "TwentyFourHourClock", "showSeconds": 1, "backgroundColor": "#263238",
                      "flipCardTextColor": "#ffffff", "flipCardBackgroundColor": "#c62828",
                      "dividerColor": "#ffffff", "ampmColor": "#ffeb3b"}))
    v.append(Variant("12h offset=+90", "clock-flip",
                     {"clockFace": "TwelveHourClock", "offset": 90}))
    return v


# ----------------------------------------------------------- countdowns
CD_DATE_FUTURE = "2030-12-31 23:59:59"
CD_DATE_PAST = "2020-01-01 00:00:00"
CD_DUR = 120

CD_COLORS = {
    "countdown-clock": {"innerBackgroundColor": "#4a148c", "outerBackgroundColor": "#7b1fa2",
                        "innerTextColor": "#ffffff", "labelTextColor": "#e1bee7",
                        "warningBackgroundColor1": "goldenrod", "warningBackgroundColor2": "gold",
                        "finishedBackgroundColor1": "#b71c1c", "finishedBackgroundColor2": "#e53935"},
    "countdown-days": {"textColor": "#b71c1c", "textBackgroundColor": "#fff8e1", "borderColor": "#b71c1c",
                       "labelTextColor": "#555555", "warningBackgroundColor": "#ff8f00",
                       "finishedBackgroundColor": "#7f0000"},
    "countdown-table": {"headerTextColor": "#ffffff", "headerBackgroundColor": "#1b5e20",
                        "evenRowTextColor": "#1b5e20", "evenRowBackgroundColor": "#c8e6c9",
                        "oddRowTextColor": "#1b5e20", "oddRowBackgroundColor": "#e8f5e9",
                        "borderColor": "#1b5e20"},
    "countdown-text": {"textColor": "#0d47a1", "dividerTextColor": "#90a4ae",
                       "warningColor": "#ef6c00", "finishedColor": "#b71c1c"},
    "countdown-custom": {},
}
CD_HAS_WARNING = {"countdown-clock", "countdown-custom", "countdown-days", "countdown-text"}
CD_TEMPLATE = ('<div class="cd"><div class="big">[hha]h [mm]m [ss]s</div>'
               '<div class="small">[DD]d | [MM]m | [YY]y</div></div>')
CD_CSS = (".cd{font-family:sans-serif;text-align:center}.cd .big{font-size:48px;font-weight:700;color:#0d47a1}"
          ".cd .small{font-size:24px;color:#607d8b}")


def _countdown(wtype: str) -> list[Variant]:
    base = {}
    if wtype == "countdown-custom":
        base = {"customTemplate": "1", "moduleType": "countdown",
                "mainTemplate": CD_TEMPLATE, "styleSheet": CD_CSS}

    def mk(label, **o):
        return Variant(label, wtype, {**base, **o}, duration=CD_DUR)

    v = [mk("type=1 widget duration", countdownType="1")]
    if wtype in CD_HAS_WARNING:
        v.append(mk("type=2 90s warning after 30s", countdownType="2",
                    countdownDuration=90, countdownWarningDuration=30))
    else:
        v.append(mk("type=2 custom 90s", countdownType="2", countdownDuration=90))
    v += [mk(f"type=3 date {CD_DATE_FUTURE}", countdownType="3", countdownDate=CD_DATE_FUTURE),
          mk("type=3 date in the past (finished)", countdownType="3", countdownDate=CD_DATE_PAST)]
    if wtype in CD_HAS_WARNING:
        v.append(mk("type=3 future date, warning date in past", countdownType="3",
                    countdownDate=CD_DATE_FUTURE, countdownWarningDate=CD_DATE_PAST))
    v.append(mk("type=2 120s left/top + custom colours", countdownType="2", countdownDuration=120,
                alignmentH="left", alignmentV="top", **CD_COLORS[wtype]))
    return v


for _w, _d in (("countdown-clock", "Countdown - Clock"), ("countdown-custom", "Countdown - Custom"),
               ("countdown-days", "Countdown - Days"), ("countdown-table", "Countdown - Table"),
               ("countdown-text", "Countdown - Text")):
    family(_w, "grid", f"{_d}: types 1/2/3, warning, finished, alignment, colours")(
        lambda w=_w: _countdown(w))


# ----------------------------------------------------------- world clocks
CITIES = [("Europe/Rome", "Roma"), ("America/New_York", "New York"),
          ("Asia/Tokyo", "Tokyo"), ("Australia/Sydney", "Sydney")]
WC_DEFAULT_HTML = ('<div class="clock">\n    <div class="inner-clock">\n        [HH:mm:ss]\n    </div>\n'
                   '    <p class="label">[label]</p>\n</div>')
WC_DEFAULT_CSS = (".clock {\n    background: #a6b1f2;\n    color: #161616;\n    width: 190px;\n"
                  "    height: 90px;\n    border-radius: 15px;\n    text-align: center;\n    margin: 5px;\n}\n\n"
                  ".inner-clock {\n    position: relative;\n    top: 20px;\n    font-size: 24px;\n}\n\n"
                  ".label {\n    position: relative;\n    font-size: 18px;\n    top: 26px;\n}")
WC_CUSTOM_HTML = ('<div class="clock"><div class="inner-clock">[HH:mm]</div>'
                  '<div class="d">[ddd DD/MM]</div><p class="label">[label]</p></div>')
WC_CUSTOM_CSS = (".clock{background:#263238;color:#fff;width:190px;height:110px;border-radius:8px;"
                 "text-align:center;margin:5px}.inner-clock{font-size:36px;padding-top:8px}"
                 ".d{font-size:14px;color:#90a4ae}.label{font-size:18px;margin:4px;color:#ffca28}")


def _wc_json(n: int, highlight: int | None = None) -> str:
    return json.dumps([{"clockTimezone": tz, "clockLabel": lb, "clockHighlight": 1 if i == highlight else 0}
                       for i, (tz, lb) in enumerate(CITIES[:n])], separators=(",", ":"))


def _worldclock(wtype: str, colors: dict, extra: list[tuple[str, dict]] = ()) -> list[Variant]:
    base = {}
    if wtype == "worldclock-digital-custom":
        base = {"template_html": WC_DEFAULT_HTML, "template_style": WC_DEFAULT_CSS,
                "widgetDesignWidth": 200, "widgetDesignHeight": 100}
    combos = [("1 clock 1x1", 1, 1, 1, None, {}),
              ("2 clocks 2x1", 2, 2, 1, None, {}),
              ("4 clocks 2x2", 4, 2, 2, None, {}),
              ("4 clocks 1x4 (column)", 4, 1, 4, None, {}),
              ("4 clocks 2x2 highlight #2, left/top", 4, 2, 2, 1,
               {"alignmentH": "left", "alignmentV": "top"}),
              ("2 clocks 2x1 custom colours", 2, 2, 1, None, colors)]
    if not colors:
        combos = combos[:-1]
    v = [Variant(lb, wtype, {**base, "worldClocks": _wc_json(n, hl), "numCols": c, "numRows": r, **o})
         for lb, n, c, r, hl, o in combos]
    for lb, o in extra:
        v.append(Variant(lb, wtype, {**base, "worldClocks": _wc_json(2), "numCols": 2, "numRows": 1, **o}))
    return v


@family("worldclock-analogue", "grid", "World Clock - Analogue: grid, highlight, toggles, colours")
def _wc_analogue():
    return _worldclock(
        "worldclock-analogue",
        {"bgColor": "#102027", "faceColor": "#eceff1", "caseColor": "#ffca28", "hourHandColor": "#102027",
         "minuteHandColor": "#102027", "secondsHandColor": "#d50000", "dialColor": "#37474f"},
        [("2 clocks: hands only (all toggles off)",
          {"showSecondsHand": 0, "showSteps": 0, "showDetailed": 0, "showMiniDigitalClock": 0, "showLabel": 0}),
         ("2 clocks: no seconds hand, no mini digital", {"showSecondsHand": 0, "showMiniDigitalClock": 0}),
         ("2 clocks: no steps/detailed, label colours",
          {"showSteps": 0, "showDetailed": 0, "labelTextColor": "#000000", "labelBgColor": "#ffeb3b"})])


@family("worldclock-digital-custom", "grid", "World Clock - Digital Custom: grid, custom HTML/CSS")
def _wc_custom():
    return _worldclock("worldclock-digital-custom", {},
                       [("2 clocks: custom HTML/CSS template",
                         {"template_html": WC_CUSTOM_HTML, "template_style": WC_CUSTOM_CSS,
                          "widgetDesignWidth": 200, "widgetDesignHeight": 120})])


@family("worldclock-digital-date", "grid", "World Clock - Digital Date: grid, colours")
def _wc_date():
    return _worldclock("worldclock-digital-date",
                       {"labelColor": "#ffca28", "dateTimeColor": "#ffffff", "backgroundColor": "#1a237e"})


@family("worldclock-digital-text", "grid", "World Clock - Digital Text: grid, colours")
def _wc_text():
    return _worldclock("worldclock-digital-text",
                       {"labelColor": "#c62828", "dateTimeColor": "#1b5e20", "backgroundColor": "#fff9c4"})


# ------------------------------------------------------------- embedded
_FULL = "html,body{margin:0;width:100%;height:100%}"
_GRID_DIV = ('<div style="width:100%;height:100%;box-sizing:border-box;border:6px solid #263238;'
             'font:20px monospace;background:'
             'linear-gradient(90deg,transparent 49.6%,#000 49.6%,#000 50.4%,transparent 50.4%),'
             'linear-gradient(0deg,transparent 49.6%,#000 49.6%,#000 50.4%,transparent 50.4%),'
             'repeating-linear-gradient(0deg,rgba(0,0,0,.18) 0 1px,transparent 1px 50px),'
             'repeating-linear-gradient(90deg,rgba(0,0,0,.18) 0 1px,transparent 1px 50px),'
             'linear-gradient(135deg,#ffcdd2,#bbdefb);">embedded 100% x 100%</div>')
_CANVAS_JS = ("(function init(){var c=document.getElementById('c');if(!c){setTimeout(init,100);return;}"
              "var x=c.getContext('2d'),t=0;(function f(){x.fillStyle='#102027';x.fillRect(0,0,400,300);"
              "x.fillStyle='#ffca28';x.beginPath();x.arc(200+120*Math.cos(t),150+80*Math.sin(t),24,0,6.283);"
              "x.fill();x.fillStyle='#fff';x.font='20px monospace';x.fillText('embedJavaScript t='+t.toFixed(1),10,24);"
              "t+=0.05;requestAnimationFrame(f);})();})();")
_HEAD_JS = ("(function t(){var o=document.getElementById('o');if(!o){setTimeout(t,100);return;}"
            "o.textContent=window.__rtHead||'embedScript NOT executed';})();")


@family("embedded", "grid", "Embedded HTML: scaleContent, transparency, CSS, JS, head script")
def _embedded():
    grid_exp = A("Riquadro con bordo di 6px (#263238), griglia a passo 50px, due linee nere centrali, sfondo sfumato "
                 "rosa→azzurro e testo 'embedded 100% x 100%'; occupa tutta l'area del widget",
                 "embedHtml/embedStyle", "embedHtml", "embedStyle")
    return [
        Variant("grid, scaleContent=0", "embedded",
                {"embedHtml": _GRID_DIV, "embedStyle": _FULL, "scaleContent": 0}, expect=(grid_exp,)),
        Variant("grid, scaleContent=1", "embedded",
                {"embedHtml": _GRID_DIV, "embedStyle": _FULL, "scaleContent": 1}, expect=(grid_exp,)),
        Variant("grid, no embedStyle (height collapse check)", "embedded", {"embedHtml": _GRID_DIV},
                expect=(A("Il riquadro è visibile (div con width/height 100%)", "embedHtml", "embedHtml"),
                        O("Senza CSS su html/body la percentuale d'altezza può collassare: registrare se il riquadro "
                          "riempie l'altezza dell'area", "CSS standard", "embedHtml"))),
        Variant("transparency=1, translucent box", "embedded",
                {"transparency": 1, "embedStyle": _FULL,
                 "embedHtml": '<div style="margin:40px;height:60%;background:rgba(21,101,192,.5);'
                              'font:24px monospace;color:#000">transparency=1</div>'},
                expect=(A("Riquadro blu semitrasparente con testo 'transparency=1', a 40px dai bordi; attorno e "
                          "attraverso il riquadro si vede lo sfondo del layout (#dfe3e8), non un fondo bianco",
                          "embedHtml/embedStyle", "embedHtml", "embedStyle"),)),
        Variant("canvas animation via embedJavaScript", "embedded",
                {"embedHtml": '<canvas id="c" width="400" height="300" style="width:100%;height:100%"></canvas>',
                 "embedStyle": _FULL, "embedJavaScript": _CANVAS_JS, "scaleContent": 1},
                expect=(A("Canvas scuro (#102027) con un pallino giallo che orbita e il testo 'embedJavaScript t=…' "
                          "con valore che aumenta di continuo",
                          "embedJavaScript", "embedHtml", "embedStyle", "embedJavaScript"),)),
        Variant("embedScript (head) visible in body", "embedded",
                {"embedScript": '<script>window.__rtHead="embedScript OK";</script>',
                 "embedHtml": '<div id="o" style="font:32px monospace;padding:12px"></div>',
                 "embedJavaScript": _HEAD_JS},
                expect=(A("Il testo mostra 'embedScript OK'; se mostra 'embedScript NOT executed' lo script inserito "
                          "nell'head non è stato eseguito (KO)", "embedScript/embedJavaScript",
                          "embedScript", "embedHtml", "embedJavaScript"),)),
        Variant("embedStyle only (web fonts/emoji/unicode)", "embedded",
                {"embedStyle": ".b{font:36px serif;padding:12px;color:#4a148c}",
                 "embedHtml": '<div class="b">àèìòù € — ✓ ★ ☀ 日本語</div>'},
                expect=(A("Mostra 'àèìòù € — ✓ ★ ☀ 日本語' in serif 36px viola (#4a148c)", "embedHtml/embedStyle",
                          "embedHtml", "embedStyle"),
                        O("Registrare se qualche simbolo (✓ ★ ☀ o i caratteri giapponesi) appare come quadratino o "
                          "glifo mancante: dipende dai font di sistema del player", "non determinabile", "embedHtml"))),
    ]


# ---------------------------------------------------------- interactive
@family("interactive", "grid", "Interactive Button/Link: text styles, gradients, outline, shadow (no actions)")
def _interactive():
    b = "interactive-button"
    link = "interactive-link"
    return [
        Variant("button default", b, {"text": "Button"}),
        Variant("button gradient bg + outline", b,
                {"text": "Gradient", "useBgGradient": 1, "bgGradient": GRAD2, "outline": 1,
                 "outlineColor": "#000000", "outlineWidth": 6}),
        Variant("button radius 60 + shadow", b,
                {"text": "Rounded", "borderRadius": 60, "bgShadow": 1, "shadowX": 6, "shadowY": 6, "shadowBlur": 10}),
        Variant("button square (roundBorder=0)", b, {"text": "Square", "roundBorder": 0, "backgroundColor": "#2e7d32"}),
        Variant("button font 56 bold italic underline", b,
                {"text": "Styled", "fontSize": 56, "bold": 1, "italics": 1, "underline": 1}),
        Variant("button fitToArea", b, {"text": "Fit to area", "fitToArea": 1}),
        Variant("button wrap, left/top", b,
                {"text": "Long wrapped button label to test wrapping", "textWrap": 1,
                 "horizontalAlign": "flex-start", "verticalAlign": "flex-start"}),
        Variant("button transparent bg", b, {"text": "Transparent", "backgroundColor": "rgba(255,255,255,0)",
                                              "fontColor": "#000000", "outline": 1}),
        Variant("link default", link, {"text": "Link"}),
        Variant("link 80px bold underline", link, {"text": "Big link", "fontSize": 80, "bold": 1, "underline": 1}),
        Variant("link red, no shadow", link, {"text": "Red link", "fontColor": "#c62828", "textShadow": 0}),
        Variant("link text gradient", link, {"text": "Gradient link", "useGradient": 1, "gradient": GRAD2,
                                              "fontSize": 64, "bold": 1}),
        Variant("link fitToArea", link, {"text": "Fit to area", "fitToArea": 1}),
        Variant("link wrap, flex-end", link,
                {"text": "Long wrapped link text to test wrapping", "textWrap": 1,
                 "horizontalAlign": "flex-end", "verticalAlign": "flex-end"}),
    ]


@family("misc", "grid", "Misc: spacer and empty-ish widgets")
def _misc():
    return [Variant("spacer (renders nothing)", "spacer",
                    expect=(A("Nessun contenuto visibile: l'area resta vuota (si vede lo sfondo del layout)",
                              "spacer.xml (nessuna proprietà)"),)),
            Variant("text: single space", "text", {"text": "<p> </p>"}),
            Variant("text: empty paragraph + bg", "text", {"text": "<p></p>", "backgroundColor": "#cfd8dc"})]


# --------------------------------------------------------- canvas elements
def _text_props(**o):
    p = {"text": "Text", "fontFamily": "", "fontColor": "#111111", "fitToArea": 0, "useGradient": 0,
         "gradient": GRAD, "fontSize": 40, "lineHeight": 1.2, "bold": 0, "italics": 0, "underline": 0,
         "textWrap": 1, "justify": 0, "showOverflow": 1, "textShadow": 0, "textShadowColor": "",
         "shadowX": 1, "shadowY": 1, "shadowBlur": 2, "horizontalAlign": "center", "verticalAlign": "center"}
    p.update(o)
    return p


def _date_props(adv: bool, **o):
    p = {}
    if adv:
        p.update({"currentDate": 1, "offset": ""})
    p.update({"date": "", "dateFormat": "d/m/Y H:i:s", "lang": ""})
    t = _text_props()
    t.pop("text")
    t.pop("justify")   # only the text element has it
    p.update(t)
    p.update(o)
    return p


def _shape(kind: str, **o):
    if kind == "rectangle":
        p = {"backgroundColor": "#1775F6", "useGradient": 0, "gradient": GRAD, "roundBorder": 0,
             "borderRadius": 20, "outline": 1, "outlineColor": "#0d3c8a", "outlineWidth": 8}
    elif kind == "ellipse":
        p = {"backgroundColor": "#1775F6", "outline": 1, "outlineColor": "#0d3c8a", "outlineWidth": 4}
    elif kind == "line":
        p = {"lineWidth": 5, "lineColor": "#111111", "lineStyle": "solid",
             "tip1Type": "squared", "tip2Type": "squared"}
    else:   # circle, triangle, pentagon, hexagon
        p = {"backgroundColor": "#1775F6", "useGradient": 0, "gradient": GRAD, "fit": 0,
             "outline": 1, "outlineColor": "#0d3c8a", "outlineWidth": 8}
    p.update(o)
    return p


def _img_props(**o):
    p = {"opacity": 100, "objectFit": "contain", "alignId": "center", "valignId": "middle",
         "roundBorder": 0, "borderRadius": 20, "imageShadow": 0, "shadowX": 1, "shadowY": 1, "shadowBlur": 2}
    p.update(o)
    return p


ELEMENT_TITLE = {"text": "Text", "date": "Date", "date_advanced": "Date / Time", "global_library_image": "",
                 "line": "Line", "rectangle": "Rectangle", "circle": "Circle", "ellipse": "Ellipse",
                 "triangle": "Triangle", "pentagon": "Pentagon", "hexagon": "Hexagon"}


@family("canvas-text", "canvas", "Canvas elements: text and date elements (fonts, align, shadow, gradient, fit)")
def _canvas_text():
    s = "Canvas text àèìòù €"
    lt = "Long canvas text that must wrap or shrink depending on the element options. " * 2
    c = lambda lb, **o: CanvasVariant(lb, "text", _text_props(text=o.pop("text", s), **o))
    v = [
        c("base 40px center"),
        c("64px bold", fontSize=64, bold=1),
        c("italics + underline", italics=1, underline=1),
        c("horizontal flex-start", horizontalAlign="flex-start"),
        c("horizontal flex-end", horizontalAlign="flex-end"),
        c("vertical flex-start", verticalAlign="flex-start"),
        c("vertical flex-end", verticalAlign="flex-end"),
        c("textShadow on", textShadow=1, textShadowColor="#888888", shadowX=4, shadowY=4, shadowBlur=6),
        c("gradient text", useGradient=1, gradient=GRAD2, fontSize=56, bold=1),
        c("fitToArea (long text)", text=lt, fitToArea=1),
        c("textWrap=1 (long text)", text=lt, fontSize=28),
        c("textWrap=0 (long text)", text=lt, fontSize=28, textWrap=0),
        c("justify=1 (long text)", text=lt, fontSize=28, justify=1),
        c("lineHeight 2.0", text=lt, fontSize=28, lineHeight=2.0),
        c("showOverflow=0 (long text)", text=lt, fontSize=40, showOverflow=0),
    ]
    FD = "2026-12-25 10:30:00"        # a Friday
    d = lambda lb, adv, ex=(), **o: CanvasVariant(lb, "date_advanced" if adv else "date", _date_props(adv, **o),
                                                  expect=tuple(ex))
    v += [
        d("date_advanced as shipped (dateFormat 'd/m/Y H:i:s')", True,
          [O("Il valore predefinito 'd/m/Y H:i:s' è in sintassi PHP, ma il renderer usa moment.format(): registrare "
             "il testo mostrato (probabile output diverso da una data leggibile)",
             "global-elements.xml (date_advanced: currentDate.format(dateFormat))", "dateFormat", "currentDate")]),
        d("date_advanced 'dddd D MMMM YYYY' lang=it (current date)", True,
          [A("Data di sistema con giorno della settimana e mese in italiano (es. 'domenica 4 ottobre 2026')",
             "moment.js", "dateFormat", "lang")],
          dateFormat="dddd D MMMM YYYY", lang="it", fontSize=32),
        d("date_advanced 'HH:mm' 80px (current time)", True,
          [A("Ora di sistema (24h) nel formato HH:mm, che avanza al cambio di minuto", "moment.js", "dateFormat")],
          dateFormat="HH:mm", fontSize=80),
        d("date_advanced offset=+120 'HH:mm:ss'", True,
          [A("Ora di sistema +120 min (2 h avanti), con secondi che avanzano ogni secondo",
             "global-elements.xml (offset in minuti)", "offset", "dateFormat")],
          offset=120, dateFormat="HH:mm:ss"),
        d("date_advanced fixed date, 'DD/MM/YYYY HH:mm'", True,
          [A("Mostra esattamente '25/12/2026 10:30' e non cambia nel tempo", "currentDate=0, date=" + FD,
             "currentDate", "date", "dateFormat")],
          currentDate=0, date=FD, dateFormat="DD/MM/YYYY HH:mm"),
        d("date_advanced fixed date, 'dddd D MMMM YYYY' lang=it", True,
          [A("Mostra esattamente 'venerdì 25 dicembre 2026'", "moment.js (locale it)",
             "currentDate", "date", "dateFormat", "lang")],
          currentDate=0, date=FD, dateFormat="dddd D MMMM YYYY", lang="it", fontSize=32),
        d("date_advanced fixed date, 'dddd D MMMM YYYY' lang=de", True,
          [A("Mostra esattamente 'Freitag 25 Dezember 2026'", "moment.js (locale de)",
             "currentDate", "date", "dateFormat", "lang")],
          currentDate=0, date=FD, dateFormat="dddd D MMMM YYYY", lang="de", fontSize=32),
        d("date (static) fixed date, 'DD/MM/YYYY HH:mm:ss'", False,
          [A("Mostra esattamente '25/12/2026 10:30:00' e non cambia nel tempo", "global-elements.xml (date)",
             "date", "dateFormat")],
          date=FD, dateFormat="DD/MM/YYYY HH:mm:ss"),
        d("date (static) empty date", False,
          [A("Non mostra nulla: con date vuota il renderer scrive una stringa vuota",
             "global-elements.xml (date: String(dateValue).length === 0 → html(''))", "date", "dateFormat")]),
    ]
    return v


@family("canvas-shapes", "canvas", "Canvas elements: rectangle, circle, ellipse, triangle, pentagon, hexagon, line")
def _canvas_shapes():
    v = [
        CanvasVariant("rectangle default", "rectangle", _shape("rectangle")),
        CanvasVariant("rectangle roundBorder r=60", "rectangle", _shape("rectangle", roundBorder=1, borderRadius=60)),
        CanvasVariant("rectangle no outline", "rectangle", _shape("rectangle", outline=0)),
        CanvasVariant("rectangle outline 24px", "rectangle", _shape("rectangle", outlineWidth=24, outlineColor="#c62828")),
        CanvasVariant("rectangle gradient", "rectangle", _shape("rectangle", useGradient=1, gradient=GRAD2)),
    ]
    for k in ("circle", "triangle", "pentagon", "hexagon"):
        v.append(CanvasVariant(f"{k} default", k, _shape(k)))
        v.append(CanvasVariant(f"{k} fit=1", k, _shape(k, fit=1)))
    v += [
        CanvasVariant("circle no outline", "circle", _shape("circle", outline=0)),
        CanvasVariant("triangle gradient", "triangle", _shape("triangle", useGradient=1, gradient=GRAD2)),
        CanvasVariant("hexagon outline 20px", "hexagon", _shape("hexagon", outlineWidth=20, outlineColor="#2e7d32")),
        CanvasVariant("ellipse default", "ellipse", _shape("ellipse")),
        CanvasVariant("ellipse no outline", "ellipse", _shape("ellipse", outline=0, backgroundColor="#ef6c00")),
    ]
    for st in ("solid", "dotted", "dashed", "double"):
        v.append(CanvasVariant(f"line {st}", "line", _shape("line", lineStyle=st, lineWidth=8)))
    for t1, t2 in (("line-arrow", "solid-arrow"), ("diamond", "circle")):
        v.append(CanvasVariant(f"line tips {t1}/{t2}", "line", _shape("line", lineWidth=8, tip1Type=t1, tip2Type=t2)))
    return v


@family("canvas-images", "canvas", "Canvas elements: library image objectFit, alignment, radius, shadow, opacity")
def _canvas_images():
    v = []
    for name, tag in (("rt_wide_2x1.png", "wide"), ("rt_tall_1x2.png", "tall"), ("rt_square_1x1.png", "square")):
        for fit in ("contain", "fill", "cover"):
            v.append(CanvasVariant(f"{tag} objectFit={fit}", "global_library_image",
                                   _img_props(objectFit=fit), media=name))
    w = "rt_wide_2x1.png"
    v += [
        CanvasVariant("wide contain left/top", "global_library_image", _img_props(alignId="left", valignId="top"), w),
        CanvasVariant("wide contain right/bottom", "global_library_image", _img_props(alignId="right", valignId="bottom"), w),
        CanvasVariant("wide cover left/top", "global_library_image",
                      _img_props(objectFit="cover", alignId="left", valignId="top"), w),
        CanvasVariant("wide roundBorder r=60", "global_library_image", _img_props(roundBorder=1, borderRadius=60), w),
        CanvasVariant("wide imageShadow", "global_library_image",
                      _img_props(imageShadow=1, shadowX=8, shadowY=8, shadowBlur=12), w),
        CanvasVariant("wide opacity 40", "global_library_image", _img_props(opacity=40), w),
    ]
    return v


# -------------------------------------------------------------- builders
class IdGen:
    def __init__(self, start: int):
        self.n = start

    def next(self) -> int:
        self.n += 1
        return self.n


def _norm(v) -> str:
    if isinstance(v, bool):
        return "1" if v else "0"
    return str(v)


def widget_options(wtype: str, label: str, opts: dict) -> list[tuple[str, str, str]]:
    cd = CDATA_OPTIONS.get(wtype, set())
    out = [("attrib", "enableStat", "Inherit"), ("attrib", "name", label[:100])]
    out += [("cdata" if k in cd else "attrib", k, _norm(v)) for k, v in opts.items()]
    return out


def make_widget(ids, playlist_id, wtype, options, duration, media_ids, now):
    wid = ids.next()
    return {
        "widgetId": wid, "playlistId": playlist_id, "ownerId": OWNER_ID, "type": wtype, "duration": duration,
        "displayOrder": 1, "useDuration": 1, "calculatedDuration": duration, "createdDt": now, "modifiedDt": now,
        "fromDt": 0, "toDt": FAR_FUTURE, "schemaVersion": SCHEMA[wtype],
        "transitionIn": None, "transitionOut": None, "transitionDurationIn": None, "transitionDurationOut": None,
        "widgetOptions": [{"widgetId": wid, "type": t, "option": o, "value": v} for t, o, v in options],
        "mediaIds": list(media_ids), "audio": [], "permissions": [], "playlist": "", "actions": [],
        "tempId": None, "tempWidgetId": None, "isValid": False, "isNew": False,
        "folderId": FOLDER_ID, "permissionsFolderId": FOLDER_ID, "isDynamic": 0,
    }


def make_region(ids, layout_id, rtype, name, rect, z, widget, now_str, duration):
    """widget: callable(playlist_id) -> widget dict, or None (drawer)."""
    x, y, w, h = rect
    rid, pid = ids.next(), ids.next()
    opts = []
    if rtype == "frame":
        opts = [{"regionId": rid, "option": "loop", "value": "0"}] + [
            {"regionId": rid, "option": o, "value": None}
            for o in ("transitionDirection", "transitionDuration", "transitionType")]
    widgets = [widget(pid)] if widget else []
    return {
        "regionId": rid, "layoutId": layout_id, "ownerId": OWNER_ID, "type": rtype, "name": name,
        "width": w, "height": h, "top": y, "left": x, "zIndex": z, "syncKey": None, "regionOptions": opts,
        "permissions": [], "duration": duration, "isDrawer": 1 if rtype == "drawer" else 0, "actions": [],
        "tempId": None,
        "regionPlaylist": {
            "playlistId": pid, "ownerId": OWNER_ID, "name": name, "regionId": rid, "isDynamic": 0,
            "filterMediaName": None, "filterMediaNameLogicalOperator": "OR", "filterMediaTags": None,
            "filterExactTags": 0, "filterMediaTagsLogicalOperator": "OR", "filterFolderId": 0,
            "maxNumberOfItems": 0, "createdDt": now_str, "modifiedDt": now_str, "duration": 0,
            "requiresDurationUpdate": 0, "enableStat": None, "tags": [], "widgets": widgets, "permissions": [],
            "tempId": None, "owner": OWNER_NAME, "groupsWithPermissions": None, "groupsWithPermissionsList": [],
            "folderId": FOLDER_ID, "permissionsFolderId": FOLDER_ID, "folderName": FOLDER_NAME,
        },
    }


def grid_cells(W, H, cols, rows):
    cw = (W - 2 * MARGIN - (cols - 1) * GUTTER) // cols
    ch = (H - 2 * MARGIN - (rows - 1) * GUTTER) // rows
    return [(MARGIN + c * (cw + GUTTER), MARGIN + r * (ch + GUTTER), cw, ch)
            for r in range(rows) for c in range(cols)]


def caption_html(label: str) -> str:
    return (f'<p style="margin:0;"><span style="font-size:18px;color:#37474f;font-family:monospace;">'
            f'{html.escape(label)}</span></p>')


def make_element(ids, eid, rect, layer, props, media_id=None, media_name=None):
    left, top, w, h = rect
    el = {"id": eid, "elementName": "", "elementId": f"element_{eid}_{ids.next()}", "type": "global",
          "left": left, "top": top, "width": w, "height": h, "layer": layer, "rotation": 0,
          "properties": [{"id": k, "value": v} for k, v in props.items()],
          "isVisible": True, "effect": "noTransition"}
    if media_id is not None:
        el["mediaId"] = media_id
    el["mediaName"] = media_name if media_name is not None else ELEMENT_TITLE.get(eid, "")
    return el


@dataclass
class LayoutOut:
    name: str
    family: str
    orientation: str
    layout_json: dict
    assets: list[str]
    mapping: list[dict]
    rows: list[dict]
    W: int = 0
    H: int = 0
    kind: str = "grid"
    duration: int = DEFAULT_DURATION
    cells: list = field(default_factory=list)
    layout_checks: list = field(default_factory=list)


def build_layout(fam: Family, chunk: list, index: int, n_in_family: int, orientation: str,
                 W: int, H: int, grid: tuple[int, int], id_base: int, layout_seq: int) -> LayoutOut:
    ids = IdGen(id_base + layout_seq * 1000)
    layout_id, campaign_id = ids.next(), ids.next()
    now = int(time.time())
    now_str = datetime.fromtimestamp(now).strftime("%Y-%m-%d %H:%M:%S")
    name = f"rt_{fam.name}_{index + 1:02d}_{orientation}"
    desc = (f"Render test: {fam.name} #{index + 1}/{n_in_family} ({orientation} {W}x{H}) "
            f"- generated, Xibo {REF_VERSION} definitions")
    cells = grid_cells(W, H, *grid)
    media_ids = {a: id_base + 500 + ASSETS[a].idx for a in ASSETS}
    used_assets: list[str] = []
    rows, regions, cells_out = [], [], []

    def use(asset: str):
        if asset not in used_assets:
            used_assets.append(asset)

    duration = DEFAULT_DURATION
    if fam.kind == "grid":
        duration = max(v.duration for v in chunk)
        for i, (v, (x, y, cw, ch)) in enumerate(zip(chunk, cells)):
            cap_opts = widget_options("text", f"caption: {v.label}",
                                      {"text": caption_html(f"{v.wtype} | {v.label}"),
                                       "backgroundColor": "#ffffff"})
            regions.append(make_region(
                ids, layout_id, "frame", f"cap | {v.label}"[:100], (x, y, cw, ch), 10 + i,
                lambda pid, o=cap_opts, d=v.duration: make_widget(ids, pid, "text", o, d, [], now),
                now_str, v.duration))
            for a in v.media:
                use(a)
            w_opts = widget_options(v.wtype, v.label, v.opts)
            regions.append(make_region(
                ids, layout_id, "frame", v.label[:100], (x, y + CAPTION_H, cw, ch - CAPTION_H), 100 + i,
                lambda pid, o=w_opts, vv=v: make_widget(ids, pid, vv.wtype, o, vv.duration,
                                                       [media_ids[a] for a in vv.media], now),
                now_str, v.duration))
            rows.append({"layout": name, "orientation": orientation, "cell": i + 1, "widget": v.wtype,
                         "label": v.label, "options": json.dumps(v.opts, ensure_ascii=False),
                         "media": ",".join(v.media)})
            cells_out.append({"cell": i + 1, "widget": v.wtype, "label": v.label, "options": _kv(
                {k: _short(str(x), 60) for k, x in v.opts.items()}),
                "checks": variant_checks(v, Geo(cw, ch - CAPTION_H, v.duration))})
    else:
        elements, layer = [], 1
        for i, (v, (x, y, cw, ch)) in enumerate(zip(chunk, cells)):
            bd = _shape("rectangle", backgroundColor="#ffffff", outlineColor="#b0bec5", outlineWidth=2)
            elements.append(make_element(ids, "rectangle", (x, y, cw, ch), layer, bd)); layer += 1
            cap = _text_props(text=f"{v.element} | {v.label}", fontSize=16, fontColor="#37474f",
                              horizontalAlign="flex-start", verticalAlign="flex-start")
            elements.append(make_element(ids, "text", (x + 8, y + 4, cw - 16, CAPTION_H - 8), layer, cap)); layer += 1
            inner = (x + PAD, y + CAPTION_H, cw - 2 * PAD, ch - CAPTION_H - PAD)
            mid = mname = None
            if v.media:
                use(v.media)
                mid, mname = media_ids[v.media], v.media
            elements.append(make_element(ids, v.element, inner, layer, v.props, mid, mname)); layer += 1
            rows.append({"layout": name, "orientation": orientation, "cell": i + 1, "widget": f"element:{v.element}",
                         "label": v.label, "options": json.dumps(v.props, ensure_ascii=False),
                         "media": v.media or ""})
            cells_out.append({"cell": i + 1, "widget": f"element:{v.element}", "label": v.label,
                              "options": _kv({k: _short(str(x), 60) for k, x in v.props.items()
                                              if _canvas_baseline(v.element).get(k) != x and k != "text"}) or "(predefinite)",
                              "checks": variant_checks(v, Geo(inner[2], inner[3]))})
        g_opts = [("attrib", "enableStat", "Off"), ("attrib", "itemsPerPage", "1"), ("attrib", "name", name),
                  ("raw", "elements", json.dumps([{"elements": elements}], separators=(",", ":"), ensure_ascii=False))]
        regions.append(make_region(
            ids, layout_id, "canvas", "", (0, 0, W, H), 1,
            lambda pid: make_widget(ids, pid, "global", g_opts, duration, [media_ids[a] for a in used_assets], now),
            now_str, duration))

    drawer = make_region(ids, layout_id, "drawer", f"{name} - drawer", (0, 0, W, H), 0, None, now_str, 0)
    code = name[:50]
    ld = {
        "layoutId": layout_id, "ownerId": OWNER_ID, "campaignId": campaign_id, "parentId": None,
        "publishedStatusId": 1, "publishedStatus": "Published", "publishedDate": None, "backgroundImageId": None,
        "schemaVersion": LAYOUT_SCHEMA, "layout": name, "description": desc, "backgroundColor": BG_COLOR,
        "createdDt": now_str, "modifiedDt": now_str, "status": 1, "retired": 0, "backgroundzIndex": 0,
        "width": W, "height": H, "orientation": orientation, "displayOrder": None, "duration": duration,
        "statusMessage": None, "enableStat": 1, "autoApplyTransitions": 0, "code": code, "isLocked": None,
        "regions": regions, "tags": [], "drawers": [drawer], "actions": [], "permissions": [], "campaigns": [],
        "owner": OWNER_NAME, "groupsWithPermissions": None, "groupsWithPermissionsList": [],
        "folderName": FOLDER_NAME, "folderId": FOLDER_ID, "permissionsFolderId": FOLDER_ID, "campaignType": "list",
    }
    layout_json = {
        "layout": name, "description": desc,
        "regions": {str(r["regionId"]): r["name"] for r in regions},
        "drawers": {str(drawer["regionId"]): drawer["name"]},
        "layoutDefinitions": ld,
    }
    mapping = [{"file": a, "mediaid": media_ids[a], "name": a, "type": "image", "duration": 10,
                "background": 0, "font": 0, "tags": []} for a in used_assets]
    lo = LayoutOut(name, fam.name, orientation, layout_json, used_assets, mapping, rows,
                   W=W, H=H, kind=fam.kind, duration=duration, cells=cells_out)
    lo.layout_checks = layout_checks(lo)
    return lo


# ------------------------------------------------------------ checks
def check_layout(lo: LayoutOut) -> list[str]:
    err = []
    ld = lo.layout_json["layoutDefinitions"]
    W, H = ld["width"], ld["height"]
    seen: set = set()

    def uniq(kind, val):
        if (kind, val) in seen:
            err.append(f"duplicate {kind} id {val}")
        seen.add((kind, val))

    if len(ld["code"]) > 50:
        err.append("layout code > 50 chars")
    mapped = {m["mediaid"] for m in lo.mapping}
    for r in ld["regions"] + ld["drawers"]:
        uniq("region", r["regionId"])
        pl = r["regionPlaylist"]
        uniq("playlist", pl["playlistId"])
        if pl["regionId"] != r["regionId"]:
            err.append(f"playlist.regionId mismatch in region {r['regionId']}")
        if r["type"] != "drawer":
            if r["left"] < 0 or r["top"] < 0 or r["left"] + r["width"] > W or r["top"] + r["height"] > H:
                err.append(f"region {r['regionId']} out of bounds")
        for w in pl["widgets"]:
            uniq("widget", w["widgetId"])
            if w["playlistId"] != pl["playlistId"]:
                err.append(f"widget {w['widgetId']} playlistId mismatch")
            for o in w["widgetOptions"]:
                if o["widgetId"] != w["widgetId"]:
                    err.append(f"widgetOption widgetId mismatch in {w['widgetId']}")
            for mid in w["mediaIds"]:
                if mid not in mapped:
                    err.append(f"widget {w['widgetId']} references unmapped media {mid}")
            for o in w["widgetOptions"]:
                if o["option"] == "elements":
                    for grp in json.loads(o["value"]):
                        for el in grp["elements"]:
                            if "mediaId" in el and (el["mediaId"] not in mapped or el["mediaId"] not in w["mediaIds"]):
                                err.append(f"element {el['elementId']} media not mapped/assigned")
                            l, t, ew, eh = el["left"], el["top"], el["width"], el["height"]
                            if l < 0 or t < 0 or l + ew > W or t + eh > H:
                                err.append(f"element {el['elementId']} out of bounds")
    if set(lo.layout_json["regions"]) != {str(r["regionId"]) for r in ld["regions"]}:
        err.append("top-level regions map does not match regions")
    json.loads(json.dumps(lo.layout_json))
    return err


# --------------------------------------------------- definition validation
def _load_props(path: Path) -> dict:
    root = ET.parse(path).getroot()
    props = {}
    for p in root.iter("property"):
        if p.get("id"):
            props[p.get("id")] = (p.get("type"), [o.get("name") for o in p.findall("./options/option")])
    return {"root": root, "props": props}


def validate_defs(defs_dir: Path, families: list[Family]) -> list[str]:
    errs: list[str] = []
    cache: dict = {}
    elem_tpl: dict = {}
    tpl_path = defs_dir / "templates" / "global-elements.xml"
    if tpl_path.exists():
        for t in ET.parse(tpl_path).getroot().iter("template"):
            elem_tpl[t.findtext("id")] = {p.get("id"): (p.get("type"), [o.get("name") for o in p.findall("./options/option")])
                                          for p in t.iter("property") if p.get("id")}
    for fam in families:
        for v in fam.build():
            if fam.kind == "grid":
                if v.wtype not in cache:
                    f = defs_dir / f"{v.wtype}.xml"
                    cache[v.wtype] = _load_props(f) if f.exists() else None
                d = cache[v.wtype]
                if d is None:
                    errs.append(f"[{fam.name}] no definition file for {v.wtype}")
                    continue
                sv = d["root"].findtext("schemaVersion")
                if sv and int(sv) != SCHEMA[v.wtype]:
                    errs.append(f"[{fam.name}] schemaVersion {SCHEMA[v.wtype]} != definition {sv}")
                for k, val in v.opts.items():
                    if k in NON_DEF_OPTIONS:
                        continue
                    if k not in d["props"]:
                        errs.append(f"[{fam.name}] '{v.label}': unknown option '{k}'")
                        continue
                    ptype, choices = d["props"][k]
                    if ptype == "dropdown" and choices and _norm(val) not in choices:
                        errs.append(f"[{fam.name}] '{v.label}': {k}={val!r} not in {choices}")
                    if (ptype in ("code", "richText")) != (k in CDATA_OPTIONS.get(v.wtype, set())):
                        errs.append(f"[{fam.name}] '{v.label}': cdata/attrib mismatch for '{k}' ({ptype})")
            else:
                key = "global_image" if v.element == "global_library_image" else v.element
                defs = elem_tpl.get(key)
                if defs is None:
                    errs.append(f"[{fam.name}] no element template '{key}'")
                    continue
                for k, val in v.props.items():
                    if k not in defs:
                        errs.append(f"[{fam.name}] '{v.label}': unknown element property '{k}'")
                        continue
                    ptype, choices = defs[k]
                    if ptype == "dropdown" and choices and _norm(val) not in choices:
                        errs.append(f"[{fam.name}] '{v.label}': {k}={val!r} not in {choices}")
    return errs


# ------------------------------------------------------------- checklists
@dataclass(frozen=True)
class Geo:
    w: int                      # widget/element area in px
    h: int
    duration: int = DEFAULT_DURATION


UI_ONLY = {"seeAdvancedFields", "customTemplate", "moduleType"}
LANGS = {"it": "italiano", "en-gb": "inglese (UK)", "de": "tedesco", "fr": "francese", "es": "spagnolo"}
TOKENS = {
    "HH:mm": "ore 00-23 e minuti (24h)",
    "HH:mm:ss": "ore 00-23, minuti e secondi (i secondi avanzano ogni secondo)",
    "hh:mm:ss A": "ore 01-12, minuti, secondi e AM/PM",
    "DD/MM/YYYY": "data GG/MM/AAAA con anno a 4 cifre",
    "dddd D MMMM YYYY": "nome del giorno, giorno e nome del mese per esteso, anno",
}
LOCALISED = {"LT", "LTS", "L", "LL", "LLL", "LLLL"}
SRC_OPT = "valore opzione"


def _plain(h: str) -> str:
    return " ".join(html.unescape(re.sub(r"<[^>]+>", " ", h)).split())


def _short(t: str, n: int = 60) -> str:
    return t if len(t) <= n else t[:n - 1] + "…"


def _css(h: str, prop: str):
    m = re.search(prop + r"\s*:\s*([^;\"']+)", h)
    return m.group(1).strip() if m else None


def _mmss(s: int) -> str:
    return "%d:%02d" % (s // 60, s % 60)


def _off(m) -> str:
    m = int(m)
    h, mm = divmod(abs(m), 60)
    return "%s%d min (%d h %02d min)" % ("+" if m >= 0 else "-", abs(m), h, mm)


def _present(o: dict, keys) -> dict:
    return {k: o[k] for k in keys if k in o}


def _kv(d: dict) -> str:
    return ", ".join("%s=%s" % (k, v) for k, v in d.items())


def _grad(g: str) -> str:
    try:
        j = json.loads(g)
        return "gradiente lineare da %s a %s, angolo %s°" % (j["color1"], j["color2"], j["angle"])
    except Exception:
        return "gradiente"


# --- text ---------------------------------------------------------------
def _ck_text(o, g):
    t = o["text"]
    c, bits = [], []
    size, col, al = _css(t, "font-size"), _css(t, "color"), _css(t, "text-align")
    plain = _plain(t)
    if plain:
        if size:
            bits.append("corpo " + size)
        if col:
            bits.append("colore " + col)
        if al:
            bits.append("allineato " + al)
        flags = [n for k, n in (("font-weight:700", "grassetto"), ("font-style:italic", "corsivo"),
                                ("text-decoration:underline", "sottolineato")) if k in t]
        bits += flags
        np_ = t.count("<p")
        if np_ > 1:
            bits.append("%d paragrafi su righe separate" % np_)
        c.append(A("Testo visibile: «%s»%s" % (_short(plain), (" - " + ", ".join(bits)) if bits else ""),
                   SRC_OPT, "text"))
    else:
        c.append(A("Nessun testo visibile (contenuto vuoto)", SRC_OPT, "text"))
    if "backgroundColor" in o:
        bg = o["backgroundColor"]
        extra = " (semitrasparente: attraverso si intravede lo sfondo del layout %s)" % BG_COLOR \
            if bg.startswith("rgba") else ""
        c.append(A("Sfondo del widget %s%s" % (bg, extra), SRC_OPT, "backgroundColor"))
    eff, sp = o.get("effect"), o.get("speed")
    marq = {"marqueeLeft": "da destra verso sinistra", "marqueeRight": "da sinistra verso destra",
            "marqueeUp": "dal basso verso l'alto", "marqueeDown": "dall'alto verso il basso"}
    if eff in marq:
        c.append(A("Il contenuto scorre %s in modo continuo (marquee, velocità %s; 1 = normale)" % (marq[eff], sp),
                   "text.xml (help speed)", "effect", "speed"))
        c.append(O("Registrare se lo scorrimento è fluido (senza scatti) e se al riavvio del ciclo riparte senza "
                   "vuoti o salti", "non determinabile", "effect"))
    elif eff == "none":
        c.append(A("Nessun movimento: contenuto statico", SRC_OPT, "effect"))
    elif eff in ("fade", "scrollVert"):
        c.append(O("Effetto '%s' (transizione tra elementi, %s ms): con un solo blocco di contenuto potrebbe non "
                   "produrre animazione visibile; registrare cosa avviene" % (eff, sp),
                   "text.xml (effectSelector, gruppo 'paged')", "effect", "speed"))
    return c


# --- image --------------------------------------------------------------
def _ck_image(o, g):
    a = ASSETS[o["uri"]]
    st, al, va = o["scaleType"], o["alignId"], o["valignId"]
    ar_i, ar_b = a.w / a.h, g.w / g.h
    c = [A("Mostra l'immagine di test %dx%d px (rapporto %.2f:1): angoli rosso (alto sx), verde (alto dx), "
           "blu (basso sx), giallo (basso dx), bordo a scacchi, croce e cerchio centrali" % (a.w, a.h, ar_i),
           "file in library", "uri")]
    if st == "stretch":
        if abs(ar_i - ar_b) / ar_b < 0.05:
            tx = "rapporti immagine (%.2f) e area (%.2f) quasi uguali: la deformazione è minima" % (ar_i, ar_b)
        else:
            tx = "immagine %.2f:1 in area %.2f:1: il cerchio centrale appare deformato in ellisse" % (ar_i, ar_b)
        c.append(A("L'immagine riempie tutta l'area %dx%d px; proporzioni non mantenute (%s)" % (g.w, g.h, tx),
                   "image.xml (anteprima: proportional=0)", "scaleType"))
    elif st == "fit":
        c.append(A("Immagine interamente visibile (4 angoli colorati presenti) con proporzioni mantenute (il cerchio "
                   "resta un cerchio); margini vuoti sul lato libero", "image.xml (anteprima: proportional=1, fit=1)",
                   "scaleType"))
    else:
        c.append(A("Proporzioni mantenute (il cerchio resta un cerchio)",
                   "image.xml (anteprima: proportional=1, fit=0)", "scaleType"))
        c.append(O("Registrare: l'immagine nativa %dx%d px nell'area %dx%d px risulta ridotta, a dimensione nativa o "
                   "ritagliata? (quali angoli colorati sono visibili)" % (a.w, a.h, g.w, g.h),
                   "non determinabile dalle definizioni", "scaleType"))
    if st == "center":
        c.append(A("Allineamento orizzontale '%s', verticale '%s' (visibile solo se l'immagine non riempie l'area)"
                   % (al, va), "image.xml (alignId/valignId visibili con scaleType=center)", "alignId", "valignId"))
    else:
        c.append(O("alignId=%s / valignId=%s sono nascosti nella UI con scaleType=%s: registrare se influiscono sulla "
                   "posizione" % (al, va, st), "image.xml (visibility)", "alignId", "valignId"))
    return c


# --- clocks -------------------------------------------------------------
def _ck_clock_digital(o, g):
    f = o["format"]
    toks = re.findall(r"\[([^\]]+)\]", f)
    c = []
    for t in toks:
        if t in LOCALISED:
            c.append(O("Token [%s] (formato localizzato moment): il risultato dipende dal locale effettivo (lang='%s'); "
                       "registrare il testo mostrato" % (t, o.get("lang") or "vuoto"), "moment.js", "format"))
        else:
            c.append(A("[%s] → %s; valori uguali a data/ora di sistema del player" % (t, TOKENS.get(t, t)),
                       SRC_OPT, "format"))
    sz, col = _css(f, "font-size"), _css(f, "color")
    st = [n for k, n in (("font-weight:700", "grassetto"),) if k in f]
    c.append(A("%d riga/e di testo, corpo %s, colore %s%s" % (len(toks), sz, col, (", " + ", ".join(st)) if st else ""),
               SRC_OPT, "format"))
    if "lang" in o:
        c.append(A("Nomi di giorno/mese in %s" % LANGS.get(o["lang"], o["lang"]), "moment.js (locale)", "lang"))
    if "offset" in o:
        c.append(A("Orario = ora di sistema %s" % _off(o["offset"]), "clock-digital.xml (help offset)", "offset"))
    return c


def _ck_clock_analogue(o, g):
    c = [A("Orologio analogico: le lancette indicano l'ora di sistema del player e avanzano", SRC_OPT)]
    if "themeId" in o:
        c.append(A("Tema %s" % {"1": "Light (chiaro)", "2": "Dark (scuro)"}[str(o["themeId"])],
                   "clock-analogue.xml", "themeId"))
    if "alignmentH" in o:
        c.append(A("Quadrante allineato %s / %s nell'area (si nota solo se l'area è più grande del quadrante)"
                   % (o["alignmentH"], o["alignmentV"]), "clock-analogue.xml", "alignmentH", "alignmentV"))
    if "offset" in o:
        c.append(A("Ora indicata = ora di sistema %s" % _off(o["offset"]), "clock-analogue.xml (help offset)", "offset"))
    return c


def _ck_clock_flip(o, g):
    cf = o["clockFace"]
    c = []
    if cf == "TwelveHourClock":
        c.append(A("Orologio 12h (ore 1-12) con ora di sistema", "clock-flip.xml", "clockFace"))
        c.append(O("Registrare se compare l'indicatore AM/PM", "clock-flip.xml (opzione ampmColor)", "clockFace"))
    elif cf == "TwentyFourHourClock":
        c.append(A("Orologio 24h (ore 00-23) con ora di sistema", "clock-flip.xml", "clockFace"))
    else:
        c.append(O("Contatore '%s' (non un orologio): registrare valore iniziale e verso del conteggio; per i "
                   "contatori 'offset' è la data/ora di partenza (Y-m-d H:i:s), qui non impostata" % cf,
                   "clock-flip.xml (help offset)", "clockFace"))
    if "showSeconds" in o:
        c.append(A("Mostra anche i secondi" if o["showSeconds"] else "Solo ore e minuti, senza secondi",
                   "clock-flip.xml", "showSeconds"))
    cols = _present(o, ("backgroundColor", "flipCardTextColor", "flipCardBackgroundColor", "dividerColor", "ampmColor"))
    if cols:
        c.append(A("Colori applicati: " + _kv(cols), SRC_OPT, *cols))
    if "offset" in o and cf in ("TwelveHourClock", "TwentyFourHourClock"):
        c.append(A("Orario = ora di sistema %s" % _off(o["offset"]), "clock-flip.xml (help offset)", "offset"))
    return c


# --- countdowns ---------------------------------------------------------
def _ck_countdown(wtype):
    def f(o, g):
        c = []
        t = str(o["countdownType"])
        dur = g.duration
        if t == "1":
            c.append(A("Parte da circa %s (%d s = durata del widget) e scende di 1 s al secondo" % (_mmss(dur), dur),
                       "xibo-countdown-render.js (type 1: durata widget)", "countdownType"))
        elif t == "2":
            d = int(o["countdownDuration"])
            c.append(A("Parte da circa %s (%d s) e scende di 1 s al secondo" % (_mmss(d), d),
                       "xibo-countdown-render.js (type 2: countdownDuration)", "countdownType", "countdownDuration"))
            if d < dur:
                c.append(A("Dopo %d s (prima della fine del ciclo, %d s) raggiunge 0: tutti i valori a 0 (ore/minuti/"
                           "secondi '00') e stile 'finished', che resta fino alla fine" % (d, dur),
                           "xibo-countdown-render.js (total <= 0 → finished)", "countdownDuration"))
        else:
            dt = o["countdownDate"]
            past = datetime.strptime(dt, "%Y-%m-%d %H:%M:%S") < datetime.now()
            if past:
                c.append(A("Data nel passato: stato 'finished' fin dall'inizio, tutti i valori a 0 (ore/minuti/secondi "
                           "'00') e stile 'finished' del widget", "xibo-countdown-render.js (total <= 0)",
                           "countdownType", "countdownDate"))
            else:
                c.append(A("Il tempo residuo corrisponde a quello tra adesso e %s (calcolare i valori attesi con "
                           "--expected-now) e scende di 1 s al secondo" % dt, "xibo-countdown-render.js (type 3)",
                           "countdownType", "countdownDate"))
            d_it = datetime.strptime(dt, "%Y-%m-%d %H:%M:%S").strftime("%d/%m/%Y %H:%M:%S")
            c.append(O("Aprire il widget nell'editor del CMS: il campo 'Countdown Date' deve mostrare la data %s (nel "
                       "formato impostato nel CMS), non un campo vuoto o una data errata: conferma che il formato di "
                       "salvataggio è stato letto correttamente" % d_it, "da verificare dopo l'import", "countdownDate"))
        if "countdownWarningDuration" in o:
            w = int(o["countdownWarningDuration"])
            rem = int(o["countdownDuration"])
            c.append(A("Secondo il codice, dopo circa %d s dall'avvio (restano ~%d s) il widget passa allo stile "
                       "'warning'" % (w, rem - w), "xibo-countdown-render.js: warningDate = avvio + N",
                       "countdownWarningDuration"))
            c.append(O("CONFLITTO tra fonti: il testo di help del campo dice che il warning parte 'dalla fine' (cioè "
                       "quando restano %d s, dopo ~%d s dall'avvio). Registrare dopo quanti secondi compare davvero "
                       "lo stile 'warning': ~%d s = vale il codice, ~%d s = vale l'help" % (w, rem - w, w, rem - w),
                       "countdown-*.xml (helpText) vs xibo-countdown-render.js", "countdownWarningDuration"))
        if "countdownWarningDate" in o:
            c.append(A("Data di warning nel passato: stile 'warning' fin dall'inizio",
                       "xibo-countdown-render.js (warningDate.diff(now) <= 0)", "countdownWarningDate"))
        if wtype == "countdown-custom":
            c.append(A("Mostra 'Hh Mm Ss' con [hha] = ore totali e [mm], [ss] a 2 cifre, e sotto 'DDd | MMm | YYy' "
                       "con giorni totali, mesi e anni, coerenti col tempo residuo; riga grande blu #0d47a1 48px "
                       "grassetto, riga piccola grigia 24px", "template custom (mainTemplate/styleSheet)",
                       "mainTemplate", "styleSheet"))
        else:
            c.append(O("Registrare quali campi sono mostrati (anni/mesi/giorni/ore/minuti/secondi) e se i valori sono "
                       "coerenti col tempo residuo", "non determinabile dalle definizioni"))
        if "alignmentH" in o:
            c.append(A("Contenuto allineato %s / %s nell'area" % (o["alignmentH"], o["alignmentV"]),
                       "definizione 4.5.0", "alignmentH", "alignmentV"))
        cols = _present(o, [k for k in CD_COLORS.get(wtype, {})])
        norm = {k: v for k, v in cols.items() if not re.search("warning|finished", k, re.I)}
        stat = {k: v for k, v in cols.items() if k not in norm}
        if norm:
            c.append(A("Colori dello stato normale applicati: " + _kv(norm), SRC_OPT, *norm))
        if stat:
            c.append(O("Colori degli stati warning/finished (%s) non visibili in questa variante (stati non "
                       "raggiunti): verificarli nelle varianti warning/finished" % _kv(stat),
                       "non verificabile qui", *stat))
        return c
    return f


# --- world clocks -------------------------------------------------------
def _ck_worldclock(wtype):
    toggles = {"showSecondsHand": "Nessuna lancetta dei secondi", "showSteps": "Nessuna tacca sul quadrante",
               "showDetailed": "Aspetto piatto, senza ombre/effetti 3D",
               "showMiniDigitalClock": "Senza mini orologio digitale interno", "showLabel": "Senza etichetta del fuso"}
    colour_keys = {"worldclock-analogue": ("bgColor", "faceColor", "caseColor", "hourHandColor", "minuteHandColor",
                                           "secondsHandColor", "dialColor", "labelTextColor", "labelBgColor"),
                   "worldclock-digital-date": ("labelColor", "dateTimeColor", "backgroundColor"),
                   "worldclock-digital-text": ("labelColor", "dateTimeColor", "backgroundColor"),
                   "worldclock-digital-custom": ()}

    def f(o, g):
        wc = json.loads(o["worldClocks"])
        n = len(wc)
        c = [A("%d orologi: %s" % (n, ", ".join("%s (%s)" % (x["clockLabel"], x["clockTimezone"]) for x in wc)),
               SRC_OPT, "worldClocks"),
             A("Disposti su %s colonna/e × %s riga/e" % (o["numCols"], o["numRows"]),
               "worldclock-*.xml (numCols/numRows)", "numCols", "numRows"),
             A("Ogni orologio mostra l'ora del proprio fuso (confrontare con --expected-now) e avanza",
               "xibo-worldclock-render.js (moment.tz)", "worldClocks")]
        for x in wc:
            if x.get("clockHighlight"):
                if wtype == "worldclock-digital-text":
                    c.append(A("'%s' evidenziato: ora in grassetto" % x["clockLabel"],
                               "worldclock-digital-text.xml (.highlighted .hourText)", "worldClocks"))
                else:
                    c.append(O("'%s' ha clockHighlight=1: registrare come viene evidenziato" % x["clockLabel"],
                               "xibo-worldclock-render.js (clockHighlight)", "worldClocks"))
        if "alignmentH" in o:
            c.append(A("Griglia allineata %s / %s nell'area" % (o["alignmentH"], o["alignmentV"]),
                       "definizione 4.5.0", "alignmentH", "alignmentV"))
        for k, txt in toggles.items():
            if k in o and not o[k] and wtype == "worldclock-analogue":
                c.append(A(txt, "worldclock-analogue.xml (%s=0)" % k, k))
        cols = _present(o, colour_keys[wtype])
        if cols:
            c.append(A("Colori applicati: " + _kv(cols), SRC_OPT, *cols))
        if wtype == "worldclock-digital-custom":
            custom = o["template_html"] == WC_CUSTOM_HTML
            if custom:
                c.append(A("Riquadri scuri (#263238) 190x110 con ora 'HH:mm' 36px, 'ddd DD/MM' piccolo grigio e "
                           "etichetta gialla (#ffca28)", "template custom", "template_html", "template_style"))
            else:
                c.append(A("Template predefinito: riquadri #a6b1f2 190x90, raggio 15px, con ora HH:mm:ss e etichetta",
                           "worldclock-digital-custom.xml (default)", "template_html", "template_style"))
            c.append(O("widgetDesignWidth/Height = %sx%s: registrare se la griglia %sx%s è scalata correttamente "
                       "nell'area %dx%d px" % (o["widgetDesignWidth"], o["widgetDesignHeight"], o["numCols"],
                                               o["numRows"], g.w, g.h),
                       "non determinabile", "widgetDesignWidth", "widgetDesignHeight"))
        return c
    return f


# --- embedded / interactive --------------------------------------------
def _ck_embedded(o, g):
    c = []
    if "scaleContent" in o:
        c.append(O("scaleContent=%s: registrare se il contenuto è scalato insieme alla regione (confrontare con la "
                   "variante con valore opposto)" % o["scaleContent"], "embedded.xml (help scaleContent)",
                   "scaleContent"))
    if o.get("transparency"):
        c.append(A("Sfondo del widget trasparente (richiede contenuto con sfondo trasparente)",
                   "embedded.xml (help transparency)", "transparency"))
    return c


def _ck_interactive(wtype):
    def f(o, g):
        c = [A("Mostra «%s»" % _short(o["text"]), SRC_OPT, "text")]
        c.append(A("Il tocco non esegue alcuna azione (nessuna action configurata sul widget)", "layout.json (actions vuote)"))
        flags = _present(o, ("fontSize", "bold", "italics", "underline"))
        if flags:
            c.append(A("Stile testo: corpo %spx%s%s%s" % (o.get("fontSize", "?"), ", grassetto" if o.get("bold") else "",
                       ", corsivo" if o.get("italics") else "", ", sottolineato" if o.get("underline") else ""),
                       SRC_OPT, *flags))
        cols = _present(o, ("backgroundColor", "fontColor"))
        if cols:
            c.append(A("Colori: " + _kv(cols), SRC_OPT, *cols))
        if o.get("useBgGradient"):
            c.append(A("Sfondo con " + _grad(o["bgGradient"]), SRC_OPT, "useBgGradient", "bgGradient"))
        if o.get("useGradient"):
            c.append(A("Testo con " + _grad(o["gradient"]), SRC_OPT, "useGradient", "gradient"))
        if o.get("outline"):
            c.append(A("Contorno %spx colore %s" % (o.get("outlineWidth", 8), o.get("outlineColor", "#0f59bd")),
                       SRC_OPT, "outline", *_present(o, ("outlineColor", "outlineWidth"))))
        if "roundBorder" in o or "borderRadius" in o:
            r = o.get("borderRadius", 6)
            c.append(A("Angoli arrotondati con raggio %spx" % r if o.get("roundBorder", 1) else "Angoli vivi (quadrati)",
                       SRC_OPT, *_present(o, ("roundBorder", "borderRadius"))))
        if o.get("bgShadow"):
            c.append(A("Ombra del riquadro (%s,%s) sfocatura %s" % (o.get("shadowX"), o.get("shadowY"), o.get("shadowBlur")),
                       SRC_OPT, "bgShadow", *_present(o, ("shadowX", "shadowY", "shadowBlur", "bgShadowColor"))))
        if "textShadow" in o:
            c.append(A("Testo senza ombra" if not o["textShadow"] else "Testo con ombra", SRC_OPT, "textShadow"))
        if o.get("fitToArea"):
            c.append(A("Il testo è ridimensionato per riempire l'area (corpo non fisso)", "definizione 4.5.0 (fitToArea)",
                       "fitToArea"))
        if "textWrap" in o:
            c.append(A("Il testo va a capo entro la larghezza" if o["textWrap"] else "Testo su una sola riga",
                       "definizione 4.5.0 (textWrap)", "textWrap"))
        if "horizontalAlign" in o:
            h = {"flex-start": "a sinistra", "center": "al centro", "flex-end": "a destra"}
            v = {"flex-start": "in alto", "center": "al centro", "flex-end": "in basso"}
            c.append(A("Testo posizionato %s (orizzontale) e %s (verticale)" % (h[o["horizontalAlign"]],
                       v[o["verticalAlign"]]), SRC_OPT, "horizontalAlign", "verticalAlign"))
        return c
    return f


CHECKERS = {
    "text": _ck_text, "image": _ck_image, "clock-digital": _ck_clock_digital, "clock-analogue": _ck_clock_analogue,
    "clock-flip": _ck_clock_flip, "embedded": _ck_embedded,
    "interactive-button": _ck_interactive("interactive-button"), "interactive-link": _ck_interactive("interactive-link"),
    "spacer": lambda o, g: [],
}
for _w in ("countdown-clock", "countdown-custom", "countdown-days", "countdown-table", "countdown-text"):
    CHECKERS[_w] = _ck_countdown(_w)
for _w in ("worldclock-analogue", "worldclock-digital-custom", "worldclock-digital-date", "worldclock-digital-text"):
    CHECKERS[_w] = _ck_worldclock(_w)


# --- canvas elements ----------------------------------------------------
def _canvas_baseline(el: str) -> dict:
    return {"text": _text_props, "date": lambda: _date_props(False), "date_advanced": lambda: _date_props(True),
            "global_library_image": _img_props}.get(el, lambda: _shape(el))()


def _ck_canvas(v: CanvasVariant, g: Geo) -> list[Check]:
    el, p = v.element, v.props
    base = _canvas_baseline(el)
    diff = {k: x for k, x in p.items() if base.get(k) != x and k != "text"}
    c, done = [], set()

    def add(chk, *keys):
        c.append(chk)
        done.update(keys)

    H = {"flex-start": "a sinistra", "center": "al centro", "flex-end": "a destra"}
    V = {"flex-start": "in alto", "center": "al centro", "flex-end": "in basso"}
    if el == "text":
        c.append(A("Testo: «%s»" % _short(p["text"]), SRC_OPT, "text"))
    if el in ("text", "date", "date_advanced"):
        if "fontSize" in diff:
            add(A("Corpo %spx" % diff["fontSize"], SRC_OPT, "fontSize"), "fontSize")
        for k, n in (("bold", "grassetto"), ("italics", "corsivo"), ("underline", "sottolineato")):
            if k in diff:
                add(A("Testo %s" % n, SRC_OPT, k), k)
        if "fontColor" in diff:
            add(A("Colore testo %s" % diff["fontColor"], SRC_OPT, "fontColor"), "fontColor")
        if "horizontalAlign" in diff:
            add(A("Testo allineato %s (orizzontale)" % H[diff["horizontalAlign"]], "global-elements.xml (hbs)",
                  "horizontalAlign"), "horizontalAlign")
        if "verticalAlign" in diff:
            add(A("Testo posizionato %s (verticale)" % V[diff["verticalAlign"]], "global-elements.xml (hbs)",
                  "verticalAlign"), "verticalAlign")
        if diff.get("textShadow"):
            add(A("Ombra del testo colore %s, offset (%s,%s), sfocatura %s" % (p["textShadowColor"], p["shadowX"],
                  p["shadowY"], p["shadowBlur"]), SRC_OPT, "textShadow", "textShadowColor", "shadowX", "shadowY",
                  "shadowBlur"), "textShadow", "textShadowColor", "shadowX", "shadowY", "shadowBlur")
        if diff.get("useGradient"):
            add(A("Testo con " + _grad(p["gradient"]), SRC_OPT, "useGradient", "gradient"), "useGradient", "gradient")
        if diff.get("fitToArea"):
            add(A("Il testo è ridimensionato per riempire l'area dell'elemento (il corpo non è quello fisso)",
                  "global-elements.xml (help fitToArea)", "fitToArea"), "fitToArea")
        if "textWrap" in diff:
            add(A("Il testo va a capo entro la larghezza dell'elemento" if diff["textWrap"] else
                  "Il testo resta su una sola riga, senza andare a capo", "global-elements.xml (help textWrap)",
                  "textWrap"), "textWrap")
        if diff.get("justify"):
            add(A("Testo giustificato (allineato a entrambi i margini, ultima riga esclusa)", "CSS standard", "justify"),
                "justify")
        if "lineHeight" in diff:
            add(A("Interlinea %s" % diff["lineHeight"], SRC_OPT, "lineHeight"), "lineHeight")
        if "showOverflow" in diff:
            add(A("Il testo eccedente l'elemento è nascosto (non esce dai bordi)" if not diff["showOverflow"] else
                  "Il testo eccedente può uscire dall'elemento", "global-elements.xml (hbs: overflow)", "showOverflow"),
                "showOverflow")
    elif el == "global_library_image":
        a = ASSETS[v.media]
        ar_i, ar_b = a.w / a.h, g.w / g.h
        fit = p["objectFit"]
        c.append(A("Mostra l'immagine di test %dx%d px (angoli rosso/verde/blu/giallo, cerchio centrale)" % (a.w, a.h),
                   "file in library"))
        if fit == "contain":
            add(A("Immagine interamente visibile (4 angoli colorati) con proporzioni mantenute; bande vuote sul lato "
                  "libero (immagine %.2f:1, area %.2f:1)" % (ar_i, ar_b), "CSS object-fit: contain", "objectFit"), "objectFit")
        elif fit == "fill":
            add(A("Riempie tutta l'area; proporzioni non mantenute (immagine %.2f:1, area %.2f:1)" % (ar_i, ar_b),
                  "CSS object-fit: fill", "objectFit"), "objectFit")
        else:
            tx = "rapporti quasi uguali: nessun ritaglio visibile" if abs(ar_i - ar_b) / ar_b < 0.05 else \
                "immagine %.2f:1 in area %.2f:1: i bordi eccedenti sono ritagliati (alcuni angoli colorati tagliati)" \
                % (ar_i, ar_b)
            add(A("Riempie tutta l'area mantenendo le proporzioni (%s)" % tx, "CSS object-fit: cover", "objectFit"),
                "objectFit")
        if "alignId" in diff or "valignId" in diff:
            add(A("Immagine allineata %s / %s nell'area" % (p["alignId"], p["valignId"]),
                  "global-elements.xml (help alignId/valignId)", "alignId", "valignId"), "alignId", "valignId")
        if diff.get("roundBorder"):
            add(A("Angoli arrotondati con raggio %spx" % p["borderRadius"], SRC_OPT, "roundBorder", "borderRadius"),
                "roundBorder", "borderRadius")
        if diff.get("imageShadow"):
            add(A("Ombra dell'immagine offset (%s,%s) sfocatura %s" % (p["shadowX"], p["shadowY"], p["shadowBlur"]),
                  SRC_OPT, "imageShadow", "shadowX", "shadowY", "shadowBlur"),
                "imageShadow", "shadowX", "shadowY", "shadowBlur")
        if "opacity" in diff:
            add(A("Opacità %s%%: attraverso l'immagine si intravede lo sfondo bianco del riquadro" % diff["opacity"],
                  "global-elements.xml (help opacity)", "opacity"), "opacity")
    elif el == "line":
        st = {"solid": "continua", "dotted": "punteggiata", "dashed": "tratteggiata", "double": "doppia"}
        tip = {"squared": "quadrata", "diamond": "a rombo", "line-arrow": "a freccia (linee)",
               "solid-arrow": "a freccia piena", "circle": "a cerchio"}
        c.append(A("Linea %s, spessore %spx, colore %s; estremità: %s / %s" % (st[p["lineStyle"]], p["lineWidth"],
                   p["lineColor"], tip[p["tip1Type"]], tip[p["tip2Type"]]), SRC_OPT,
                   "lineStyle", "lineWidth", "lineColor", "tip1Type", "tip2Type"))
        done.update(diff)
    else:   # shapes
        c.append(A("Forma '%s': riempimento %s%s" % (el, p["backgroundColor"],
                   ", contorno %spx %s" % (p["outlineWidth"], p["outlineColor"]) if p.get("outline") else
                   ", senza contorno"), SRC_OPT, "backgroundColor", "outline", "outlineColor", "outlineWidth"))
        if el == "rectangle" and p.get("roundBorder"):
            add(A("Angoli arrotondati con raggio %spx" % p["borderRadius"], SRC_OPT, "roundBorder", "borderRadius"),
                "roundBorder", "borderRadius")
        if p.get("useGradient"):
            add(A("Riempimento con " + _grad(p["gradient"]), SRC_OPT, "useGradient", "gradient"), "useGradient", "gradient")
        if p.get("fit"):
            add(A("La forma è scalata per adattarsi all'area dell'elemento", "global-elements.xml (help fit)", "fit"), "fit")
        elif "fit" in p:
            c.append(O("fit=0: registrare come la forma si posiziona/dimensiona nell'area %dx%d px (non quadrata)"
                       % (g.w, g.h), "non determinabile", "fit"))
        done.update(diff)
    return c + list(v.expect)


def variant_checks(v, g: Geo) -> list[Check]:
    base = [A("Il widget occupa l'area prevista (%dx%d px) sotto la didascalia, senza sovrapporsi alle celle adiacenti "
              "né far uscire contenuto dai propri bordi" % (g.w, g.h), "layout.json (geometria regioni) + criterio "
              "di accettazione")]
    if isinstance(v, CanvasVariant):
        return [A("L'elemento sta nel proprio riquadro (%dx%d px) sotto la didascalia, senza uscire dall'area"
                  % (g.w, g.h), "layout.json (geometria elementi) + criterio di accettazione")] + _ck_canvas(v, g)
    return base + CHECKERS[v.wtype](v.opts, g) + list(v.expect)


def check_coverage(fams) -> list[str]:
    errs = []
    for fam in fams:
        for v in fam.build():
            g = Geo(500, 500, v.duration if isinstance(v, Variant) else DEFAULT_DURATION)
            cov = set().union(*[c.covers for c in variant_checks(v, g)]) if variant_checks(v, g) else set()
            if isinstance(v, Variant):
                keys = set(v.opts) - NON_DEF_OPTIONS - UI_ONLY
            else:
                base = _canvas_baseline(v.element)
                keys = {k for k, x in v.props.items() if base.get(k) != x and k != "text"}
            miss = keys - cov
            if miss:
                errs.append("[%s] '%s': opzioni senza controllo: %s" % (fam.name, v.label, sorted(miss)))
    return errs


# ---------------------------------------------------------- output files
def layout_checks(lo: "LayoutOut") -> list[Check]:
    W, H, n = lo.W, lo.H, len(lo.cells)
    c = [A("L'import dello zip termina senza errori e crea il layout '%s'" % lo.name, "LayoutFactory::createFromZip"),
         A("Dimensioni %dx%d px, orientamento %s; se la risoluzione non esiste nel CMS viene creata ('%d x %d')"
           % (W, H, lo.orientation, W, H), "LayoutFactory::createFromZip (getByDimensions → create)"),
         O("Registrare lo stato del layout dopo l'import (valido / in bozza / con avvisi); se in bozza, pubblicarlo",
           "non determinabile"),
         A(("Nel Layout Editor sono presenti %d regioni (per ogni cella: didascalia + widget)" % (2 * n))
           if lo.kind == "grid" else
           ("Nel Layout Editor è presente 1 regione canvas con %d elementi (per ogni cella: riquadro, didascalia, "
            "elemento in prova)" % (3 * n)), "layout.json")]
    if lo.assets:
        c.append(A("In Libreria compaiono le immagini %s con tag 'imported' (se già presenti con lo stesso nome vengono "
                   "riutilizzate)" % ", ".join(lo.assets), "LayoutFactory::createFromZip (assignTag 'imported')"))
    c += [A("Assegnato a un display con orientamento %s (%dx%d): il layout riempie lo schermo senza bande né ritagli; "
            "con display fisicamente ruotato impostare la rotazione sul player" % (lo.orientation, W, H),
            "layout.json (width/height)"),
          A("Il layout dura %d s (durata massima dei widget) e poi ricomincia" % lo.duration, "layout.json (duration)"),
          O("Registrare se, al riavvio del ciclo, countdown, marquee e animazioni ripartono da capo senza residui",
            "non determinabile"),
          A("Nessun errore nel log del player durante almeno 2 cicli completi", "criterio generale")]
    return c


def cell_title(r: dict) -> str:
    return "%s | %s" % (r["widget"], r["label"])


def render_md(lo: "LayoutOut") -> str:
    out = ["# %s - checklist" % lo.name, "",
           "Famiglia `%s` · %dx%d %s · ciclo %d s · %d celle · generato per Xibo %s" %
           (lo.family, lo.W, lo.H, lo.orientation, lo.duration, len(lo.cells), REF_VERSION), "",
           "**ATTESO** = derivato da opzioni, definizioni o codice 4.5.0 (indicato tra parentesi) · **OSSERVA** = non "
           "determinabile a priori: registrare cosa si vede.", "", "## Layout", ""]
    for i, ch in enumerate(lo.layout_checks, 1):
        out.append("- [ ] **L%d · %s** %s _(%s)_" % (i, ch.kind, ch.text, ch.src))
    for cell in lo.cells:
        out += ["", "## Cella %d · %s" % (cell["cell"], cell_title(cell)), "",
                "Opzioni: `%s`" % _short(cell["options"], 240), ""]
        for j, ch in enumerate(cell["checks"], 1):
            out.append("- [ ] **%d.%d · %s** %s _(%s)_" % (cell["cell"], j, ch.kind, ch.text, ch.src))
        out.append("- Esito cella: ☐ OK  ☐ KO  ☐ N/A — Note: ______")
    return "\n".join(out) + "\n"


CSV_FIELDS = ["layout", "cella", "widget", "variante", "id", "tipo", "controllo", "fonte", "esito", "note"]


def checklist_rows(lo: "LayoutOut") -> list[dict]:
    rows = []
    for i, ch in enumerate(lo.layout_checks, 1):
        rows.append({"layout": lo.name, "cella": "-", "widget": "layout", "variante": "-", "id": "L%d" % i,
                     "tipo": ch.kind, "controllo": ch.text, "fonte": ch.src, "esito": "", "note": ""})
    for cell in lo.cells:
        for j, ch in enumerate(cell["checks"], 1):
            rows.append({"layout": lo.name, "cella": cell["cell"], "widget": cell["widget"], "variante": cell["label"],
                         "id": "%d.%d" % (cell["cell"], j), "tipo": ch.kind, "controllo": ch.text, "fonte": ch.src,
                         "esito": "", "note": ""})
    return rows


PREP_MD = """# Preparazione dei test di rendering

## 1. Registrare l'ambiente (una volta per sessione)
- [ ] Versione CMS: ______ (le opzioni sono verificate sulle definizioni Xibo %(ref)s)
- [ ] Player e versione: ______  · display: risoluzione ______ , rotazione ______
- [ ] Fuso orario e locale del player/display: ______ (influisce su orologi, date e formati localizzati)
- [ ] Data e ora del test: ______ · orologio di riferimento usato: ______
- [ ] Cartella del CMS dove importare i layout: ______

## 2. Importazione
- [ ] Importare prima UN solo layout (es. `rt_clock-digital_01_*`) e verificarne l'esito, poi gli altri
- [ ] Verificare che gli ID interni agli zip (partono da %(idb)d) siano stati riassegnati dal CMS
- [ ] Verificare in Libreria le immagini di test (`rt_*.png`) e che non siano duplicate

## 3. Valori attesi che dipendono dall'istante del test
Eseguire sul computer di test, nello stesso momento della verifica:

    python3 xibo_render_test_gen.py --expected-now

Stampa gli orari attuali nei fusi usati dalle varianti world clock e i valori attesi dei countdown con data
(`rt_countdown-*`). Per le celle con offset, il riferimento è l'ora di sistema del player.

## 4. Come compilare
- Per ogni layout: aprire `checklists/<layout>.md` oppure compilare `checklist.csv` (separatore `;`, UTF-8):
  colonna `esito` = OK / KO / N/A, `note` per i dettagli.
- Controlli **ATTESO**: OK se il risultato coincide; altrimenti KO con una descrizione di ciò che si vede.
- Controlli **OSSERVA**: nessun giudizio a priori; scrivere in `note` cosa succede (serve a chiarire il comportamento).
- In caso di KO: allegare uno screenshot e indicare layout, cella e id del controllo.
"""


def expected_now() -> None:
    from math import floor
    now = datetime.now().astimezone()
    print("Adesso: %s (%s)" % (now.strftime("%Y-%m-%d %H:%M:%S"), now.tzname()))
    try:
        from zoneinfo import ZoneInfo
        print("\nOrari attesi per i fusi delle varianti world clock:")
        for tz, label in CITIES:
            t = datetime.now(ZoneInfo(tz))
            print("  %-10s %-20s %s (UTC%s)" % (label, tz, t.strftime("%H:%M:%S %a %d/%m"), t.strftime("%z")))
    except Exception as e:      # tz database missing
        print("\nFusi non calcolabili (%s): installare tzdata (pip install tzdata)" % e)
    print("\nCountdown con data (valori iniziali attesi, calcolati come moment.js):")
    for dt in (CD_DATE_FUTURE, CD_DATE_PAST):
        tgt = datetime.strptime(dt, "%Y-%m-%d %H:%M:%S")
        secs = (tgt - datetime.now()).total_seconds()
        if secs <= 0:
            print("  %s → già scaduto: tutti i valori a 0, stile 'finished'" % dt)
            continue
        days = secs / 86400
        months = days * 4800 / 146097
        print("  %s → ore totali [hha]=%d, [mm]=%02d, [ss]=%02d, giorni [DD]=%d, mesi [MM]=%d, anni [YY]=%d"
              % (dt, floor(secs / 3600), floor(secs % 3600 / 60), floor(secs % 60), floor(days), floor(months),
                 floor(months / 12)))
    print("\nI valori scendono di 1 s al secondo: confrontarli entro 1-2 s dall'avvio del widget.")


# ------------------------------------------------------------------ main
def write_zip(path: Path, lo: LayoutOut, png_cache: dict):
    with zipfile.ZipFile(path, "w", zipfile.ZIP_DEFLATED) as z:
        z.writestr("layout.json", json.dumps(lo.layout_json, ensure_ascii=False))
        z.writestr("mapping.json", json.dumps(lo.mapping, ensure_ascii=False))
        for a in lo.assets:
            if a not in png_cache:
                png_cache[a] = make_png(ASSETS[a].w, ASSETS[a].h)
            z.writestr(f"library/{a}", png_cache[a])


def select_families(only: str | None) -> list[Family]:
    if not only:
        return list(FAMILIES.values())
    pats = [p.strip() for p in only.split(",") if p.strip()]
    sel = [f for f in FAMILIES.values() if any(fnmatch.fnmatch(f.name, p) for p in pats)]
    if not sel:
        sys.exit(f"no family matches {only!r}; use --list")
    return sel


def parse_pair(s: str, what: str) -> tuple[int, int]:
    try:
        a, b = s.lower().split("x")
        a, b = int(a), int(b)
        if a <= 0 or b <= 0:
            raise ValueError
        return a, b
    except ValueError:
        sys.exit(f"invalid {what} {s!r}, expected NxM")


def main(argv=None) -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--orientation", choices=["portrait", "landscape", "both"], default="portrait")
    ap.add_argument("--resolution", default="1920x1080",
                    help="LONGxSHORT side, swapped for portrait (default 1920x1080)")
    ap.add_argument("--grid", help="cells per layout as COLSxROWS, applied to every orientation "
                                   "(default 2x3 portrait, 3x2 landscape)")
    ap.add_argument("--only", help="comma-separated family names/globs, e.g. 'clock-*,text'")
    ap.add_argument("--out", default="./xibo_render_tests", help="output directory")
    ap.add_argument("--id-base", type=int, default=900000, help="base for generated ids (zip-internal)")
    ap.add_argument("--list", action="store_true", help="list families and variant counts, then exit")
    ap.add_argument("--no-checklist", action="store_true", help="do not write checklists")
    ap.add_argument("--expected-now", action="store_true",
                    help="print time-dependent expected values (world clocks, dated countdowns) and exit")
    ap.add_argument("--validate-checks", action="store_true",
                    help="check that every option of every variant is covered by a checklist item, then exit")
    ap.add_argument("--validate-defs", metavar="DIR",
                    help=f"check options against the Xibo modules/ dir (tag {REF_VERSION}) and exit")
    a = ap.parse_args(argv)

    if a.expected_now:
        expected_now()
        return 0
    fams = select_families(a.only)
    if a.validate_checks or not a.no_checklist:
        miss = check_coverage(fams)
        if miss:
            print("\n".join(miss), file=sys.stderr)
            return 2
        if a.validate_checks:
            print("OK: every option of every variant has a checklist item")
            return 0
    if a.list:
        print(f"{'family':28}{'kind':8}{'variants':>9}  description")
        for f in fams:
            print(f"{f.name:28}{f.kind:8}{len(f.build()):>9}  {f.desc}")
        return 0
    if a.validate_defs:
        errs = validate_defs(Path(a.validate_defs), fams)
        print("\n".join(errs) if errs else f"OK: all options valid against {a.validate_defs}")
        return 2 if errs else 0

    long_, short = parse_pair(a.resolution, "--resolution")
    long_, short = max(long_, short), min(long_, short)
    orients = ["portrait", "landscape"] if a.orientation == "both" else [a.orientation]
    out = Path(a.out)
    png_cache: dict = {}
    seq, bad = 0, 0
    for o in orients:
        W, H = (short, long_) if o == "portrait" else (long_, short)
        grid = parse_pair(a.grid, "--grid") if a.grid else DEFAULT_GRID[o]
        cap = grid[0] * grid[1]
        odir = out / o
        odir.mkdir(parents=True, exist_ok=True)
        matrix, nlay, nreg, ck_rows = [], 0, 0, []
        cdir = odir / "checklists"
        if not a.no_checklist:
            cdir.mkdir(parents=True, exist_ok=True)
        for fam in fams:
            vs = fam.build()
            chunks = [vs[i:i + cap] for i in range(0, len(vs), cap)]
            for i, ch in enumerate(chunks):
                seq += 1
                lo = build_layout(fam, ch, i, len(chunks), o, W, H, grid, a.id_base, seq)
                errs = check_layout(lo)
                if errs:
                    bad += 1
                    print(f"CHECK FAILED {lo.name}:\n  " + "\n  ".join(errs), file=sys.stderr)
                    continue
                write_zip(odir / f"{lo.name}.zip", lo, png_cache)
                if not a.no_checklist:
                    (cdir / f"{lo.name}.md").write_text(render_md(lo), encoding="utf-8")
                    ck_rows += checklist_rows(lo)
                matrix += lo.rows
                nlay += 1
                nreg += len(lo.layout_json["layoutDefinitions"]["regions"])
        with open(odir / "matrix.csv", "w", newline="", encoding="utf-8") as fh:
            w = csv.DictWriter(fh, fieldnames=["layout", "orientation", "cell", "widget", "label", "options", "media"])
            w.writeheader()
            w.writerows(matrix)
        extra = ""
        if not a.no_checklist:
            with open(odir / "checklist.csv", "w", newline="", encoding="utf-8-sig") as fh:
                w = csv.DictWriter(fh, fieldnames=CSV_FIELDS, delimiter=";")
                w.writeheader()
                w.writerows(ck_rows)
            extra = f"  checks={len(ck_rows)}"
        print(f"{o:9} {W}x{H}  grid {grid[0]}x{grid[1]}  layouts={nlay}  regions={nreg}  variants={len(matrix)}{extra}  -> {odir}")
    if not a.no_checklist:
        (out / "00_preparazione.md").write_text(PREP_MD % {"ref": REF_VERSION, "idb": a.id_base}, encoding="utf-8")
    return 1 if bad else 0


if __name__ == "__main__":
    sys.exit(main())
