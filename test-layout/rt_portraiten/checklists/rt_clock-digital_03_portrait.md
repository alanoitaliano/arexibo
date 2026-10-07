# rt_clock-digital_03_portrait - checklist

Family `clock-digital` · 1080x1920 portrait · 60 s cycle · 6 cells · generated for Xibo 4.5.0

**EXPECTED** = derived from options, definitions or 4.5.0 code (source in brackets) · **OBSERVE** = not determinable in advance: record what you see.

## Layout

- [ ] **L1 · EXPECTED** Importing the zip completes without errors and creates the layout 'rt_clock-digital_03_portrait' _(LayoutFactory::createFromZip)_
- [ ] **L2 · EXPECTED** Size 1080x1920 px, orientation portrait; if the resolution does not exist in the CMS it is created ('1080 x 1920') _(LayoutFactory::createFromZip (getByDimensions → create))_
- [ ] **L3 · OBSERVE** Record the layout status after import (valid / draft / with warnings); if draft, publish it _(not determinable)_
- [ ] **L4 · EXPECTED** The Layout Editor shows 12 regions (per cell: caption + widget) _(layout.json)_
- [ ] **L5 · EXPECTED** Assigned to a portrait display (1080x1920): the layout fills the screen with no bars or cropping; if the display is physically rotated, set the rotation on the player _(layout.json (width/height))_
- [ ] **L6 · EXPECTED** The layout lasts 60 s (longest widget duration) and then restarts _(layout.json (duration))_
- [ ] **L7 · OBSERVE** Record whether, when the cycle restarts, countdowns, marquees and animations restart from scratch with no leftovers _(not determinable)_
- [ ] **L8 · EXPECTED** No errors in the player log over at least 2 full cycles _(general criterion)_

## Cell 1 · clock-digital | lang=de dddd D MMMM YYYY

Options: `format=<p style="margin:0;text-align:center;"><span style="font-si…, lang=de`

- [ ] **1.1 · EXPECTED** The widget occupies the intended area (512x560 px) below the caption, without overlapping adjacent cells or letting content spill outside its borders _(layout.json (region geometry) + acceptance criterion)_
- [ ] **1.2 · EXPECTED** [dddd D MMMM YYYY] → full weekday name, day, full month name, year; values equal to the player's system date/time _(option value)_
- [ ] **1.3 · EXPECTED** 1 line(s) of text, size 36px, colour #1c1c1c _(option value)_
- [ ] **1.4 · EXPECTED** Weekday/month names in German _(moment.js (locale))_
- Cell result: ☐ PASS  ☐ FAIL  ☐ N/A — Notes: ______

## Cell 2 · clock-digital | lang=fr dddd D MMMM YYYY

Options: `format=<p style="margin:0;text-align:center;"><span style="font-si…, lang=fr`

- [ ] **2.1 · EXPECTED** The widget occupies the intended area (512x560 px) below the caption, without overlapping adjacent cells or letting content spill outside its borders _(layout.json (region geometry) + acceptance criterion)_
- [ ] **2.2 · EXPECTED** [dddd D MMMM YYYY] → full weekday name, day, full month name, year; values equal to the player's system date/time _(option value)_
- [ ] **2.3 · EXPECTED** 1 line(s) of text, size 36px, colour #1c1c1c _(option value)_
- [ ] **2.4 · EXPECTED** Weekday/month names in French _(moment.js (locale))_
- Cell result: ☐ PASS  ☐ FAIL  ☐ N/A — Notes: ______

## Cell 3 · clock-digital | lang=es dddd D MMMM YYYY

Options: `format=<p style="margin:0;text-align:center;"><span style="font-si…, lang=es`

- [ ] **3.1 · EXPECTED** The widget occupies the intended area (512x560 px) below the caption, without overlapping adjacent cells or letting content spill outside its borders _(layout.json (region geometry) + acceptance criterion)_
- [ ] **3.2 · EXPECTED** [dddd D MMMM YYYY] → full weekday name, day, full month name, year; values equal to the player's system date/time _(option value)_
- [ ] **3.3 · EXPECTED** 1 line(s) of text, size 36px, colour #1c1c1c _(option value)_
- [ ] **3.4 · EXPECTED** Weekday/month names in Spanish _(moment.js (locale))_
- Cell result: ☐ PASS  ☐ FAIL  ☐ N/A — Notes: ______

## Cell 4 · clock-digital | offset=+120 min

Options: `format=<p style="margin:0;text-align:center;"><span style="font-si…, offset=120`

- [ ] **4.1 · EXPECTED** The widget occupies the intended area (512x560 px) below the caption, without overlapping adjacent cells or letting content spill outside its borders _(layout.json (region geometry) + acceptance criterion)_
- [ ] **4.2 · EXPECTED** [HH:mm:ss] → hours 00-23, minutes and seconds (seconds advance every second); values equal to the player's system date/time _(option value)_
- [ ] **4.3 · EXPECTED** 1 line(s) of text, size 48px, colour #1c1c1c _(option value)_
- [ ] **4.4 · EXPECTED** Time = system time +120 min (2 h 00 min) _(clock-digital.xml (offset help))_
- Cell result: ☐ PASS  ☐ FAIL  ☐ N/A — Notes: ______

## Cell 5 · clock-digital | offset=-300 min

Options: `format=<p style="margin:0;text-align:center;"><span style="font-si…, offset=-300`

- [ ] **5.1 · EXPECTED** The widget occupies the intended area (512x560 px) below the caption, without overlapping adjacent cells or letting content spill outside its borders _(layout.json (region geometry) + acceptance criterion)_
- [ ] **5.2 · EXPECTED** [HH:mm:ss] → hours 00-23, minutes and seconds (seconds advance every second); values equal to the player's system date/time _(option value)_
- [ ] **5.3 · EXPECTED** 1 line(s) of text, size 48px, colour #1c1c1c _(option value)_
- [ ] **5.4 · EXPECTED** Time = system time -300 min (5 h 00 min) _(clock-digital.xml (offset help))_
- Cell result: ☐ PASS  ☐ FAIL  ☐ N/A — Notes: ______

## Cell 6 · clock-digital | size 24px

Options: `format=<p style="margin:0;text-align:center;"><span style="font-si…`

- [ ] **6.1 · EXPECTED** The widget occupies the intended area (512x560 px) below the caption, without overlapping adjacent cells or letting content spill outside its borders _(layout.json (region geometry) + acceptance criterion)_
- [ ] **6.2 · EXPECTED** [HH:mm:ss] → hours 00-23, minutes and seconds (seconds advance every second); values equal to the player's system date/time _(option value)_
- [ ] **6.3 · EXPECTED** 1 line(s) of text, size 24px, colour #1c1c1c _(option value)_
- Cell result: ☐ PASS  ☐ FAIL  ☐ N/A — Notes: ______
