# rt_clock-digital_02_landscape - checklist

Family `clock-digital` · 1920x1080 landscape · 60 s cycle · 6 cells · generated for Xibo 4.5.0

**EXPECTED** = derived from options, definitions or 4.5.0 code (source in brackets) · **OBSERVE** = not determinable in advance: record what you see.

## Layout

- [ ] **L1 · EXPECTED** Importing the zip completes without errors and creates the layout 'rt_clock-digital_02_landscape' _(LayoutFactory::createFromZip)_
- [ ] **L2 · EXPECTED** Size 1920x1080 px, orientation landscape; if the resolution does not exist in the CMS it is created ('1920 x 1080') _(LayoutFactory::createFromZip (getByDimensions → create))_
- [ ] **L3 · OBSERVE** Record the layout status after import (valid / draft / with warnings); if draft, publish it _(not determinable)_
- [ ] **L4 · EXPECTED** The Layout Editor shows 12 regions (per cell: caption + widget) _(layout.json)_
- [ ] **L5 · EXPECTED** Assigned to a landscape display (1920x1080): the layout fills the screen with no bars or cropping; if the display is physically rotated, set the rotation on the player _(layout.json (width/height))_
- [ ] **L6 · EXPECTED** The layout lasts 60 s (longest widget duration) and then restarts _(layout.json (duration))_
- [ ] **L7 · OBSERVE** Record whether, when the cycle restarts, countdowns, marquees and animations restart from scratch with no leftovers _(not determinable)_
- [ ] **L8 · EXPECTED** No errors in the player log over at least 2 full cycles _(general criterion)_

## Cell 1 · clock-digital | format [L]

Options: `format=<p style="margin:0;text-align:center;"><span style="font-si…`

- [ ] **1.1 · EXPECTED** The widget occupies the intended area (616x456 px) below the caption, without overlapping adjacent cells or letting content spill outside its borders _(layout.json (region geometry) + acceptance criterion)_
- [ ] **1.2 · OBSERVE** Token [L] (moment localised format): the result depends on the effective locale (lang='empty'); record the text shown _(moment.js)_
- [ ] **1.3 · EXPECTED** 1 line(s) of text, size 44px, colour #1c1c1c _(option value)_
- Cell result: ☐ PASS  ☐ FAIL  ☐ N/A — Notes: ______

## Cell 2 · clock-digital | format [LL]

Options: `format=<p style="margin:0;text-align:center;"><span style="font-si…`

- [ ] **2.1 · EXPECTED** The widget occupies the intended area (616x456 px) below the caption, without overlapping adjacent cells or letting content spill outside its borders _(layout.json (region geometry) + acceptance criterion)_
- [ ] **2.2 · OBSERVE** Token [LL] (moment localised format): the result depends on the effective locale (lang='empty'); record the text shown _(moment.js)_
- [ ] **2.3 · EXPECTED** 1 line(s) of text, size 44px, colour #1c1c1c _(option value)_
- Cell result: ☐ PASS  ☐ FAIL  ☐ N/A — Notes: ______

## Cell 3 · clock-digital | format [LLL]

Options: `format=<p style="margin:0;text-align:center;"><span style="font-si…`

- [ ] **3.1 · EXPECTED** The widget occupies the intended area (616x456 px) below the caption, without overlapping adjacent cells or letting content spill outside its borders _(layout.json (region geometry) + acceptance criterion)_
- [ ] **3.2 · OBSERVE** Token [LLL] (moment localised format): the result depends on the effective locale (lang='empty'); record the text shown _(moment.js)_
- [ ] **3.3 · EXPECTED** 1 line(s) of text, size 44px, colour #1c1c1c _(option value)_
- Cell result: ☐ PASS  ☐ FAIL  ☐ N/A — Notes: ______

## Cell 4 · clock-digital | format [LLLL]

Options: `format=<p style="margin:0;text-align:center;"><span style="font-si…`

- [ ] **4.1 · EXPECTED** The widget occupies the intended area (616x456 px) below the caption, without overlapping adjacent cells or letting content spill outside its borders _(layout.json (region geometry) + acceptance criterion)_
- [ ] **4.2 · OBSERVE** Token [LLLL] (moment localised format): the result depends on the effective locale (lang='empty'); record the text shown _(moment.js)_
- [ ] **4.3 · EXPECTED** 1 line(s) of text, size 44px, colour #1c1c1c _(option value)_
- Cell result: ☐ PASS  ☐ FAIL  ☐ N/A — Notes: ______

## Cell 5 · clock-digital | lang=it dddd D MMMM YYYY

Options: `format=<p style="margin:0;text-align:center;"><span style="font-si…, lang=it`

- [ ] **5.1 · EXPECTED** The widget occupies the intended area (616x456 px) below the caption, without overlapping adjacent cells or letting content spill outside its borders _(layout.json (region geometry) + acceptance criterion)_
- [ ] **5.2 · EXPECTED** [dddd D MMMM YYYY] → full weekday name, day, full month name, year; values equal to the player's system date/time _(option value)_
- [ ] **5.3 · EXPECTED** 1 line(s) of text, size 36px, colour #1c1c1c _(option value)_
- [ ] **5.4 · EXPECTED** Weekday/month names in Italian _(moment.js (locale))_
- Cell result: ☐ PASS  ☐ FAIL  ☐ N/A — Notes: ______

## Cell 6 · clock-digital | lang=en-gb dddd D MMMM YYYY

Options: `format=<p style="margin:0;text-align:center;"><span style="font-si…, lang=en-gb`

- [ ] **6.1 · EXPECTED** The widget occupies the intended area (616x456 px) below the caption, without overlapping adjacent cells or letting content spill outside its borders _(layout.json (region geometry) + acceptance criterion)_
- [ ] **6.2 · EXPECTED** [dddd D MMMM YYYY] → full weekday name, day, full month name, year; values equal to the player's system date/time _(option value)_
- [ ] **6.3 · EXPECTED** 1 line(s) of text, size 36px, colour #1c1c1c _(option value)_
- [ ] **6.4 · EXPECTED** Weekday/month names in English (UK) _(moment.js (locale))_
- Cell result: ☐ PASS  ☐ FAIL  ☐ N/A — Notes: ______
