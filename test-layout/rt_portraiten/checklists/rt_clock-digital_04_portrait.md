# rt_clock-digital_04_portrait - checklist

Family `clock-digital` · 1080x1920 portrait · 60 s cycle · 3 cells · generated for Xibo 4.5.0

**EXPECTED** = derived from options, definitions or 4.5.0 code (source in brackets) · **OBSERVE** = not determinable in advance: record what you see.

## Layout

- [ ] **L1 · EXPECTED** Importing the zip completes without errors and creates the layout 'rt_clock-digital_04_portrait' _(LayoutFactory::createFromZip)_
- [ ] **L2 · EXPECTED** Size 1080x1920 px, orientation portrait; if the resolution does not exist in the CMS it is created ('1080 x 1920') _(LayoutFactory::createFromZip (getByDimensions → create))_
- [ ] **L3 · OBSERVE** Record the layout status after import (valid / draft / with warnings); if draft, publish it _(not determinable)_
- [ ] **L4 · EXPECTED** The Layout Editor shows 6 regions (per cell: caption + widget) _(layout.json)_
- [ ] **L5 · EXPECTED** Assigned to a portrait display (1080x1920): the layout fills the screen with no bars or cropping; if the display is physically rotated, set the rotation on the player _(layout.json (width/height))_
- [ ] **L6 · EXPECTED** The layout lasts 60 s (longest widget duration) and then restarts _(layout.json (duration))_
- [ ] **L7 · OBSERVE** Record whether, when the cycle restarts, countdowns, marquees and animations restart from scratch with no leftovers _(not determinable)_
- [ ] **L8 · EXPECTED** No errors in the player log over at least 2 full cycles _(general criterion)_

## Cell 1 · clock-digital | size 96px

Options: `format=<p style="margin:0;text-align:center;"><span style="font-si…`

- [ ] **1.1 · EXPECTED** The widget occupies the intended area (512x560 px) below the caption, without overlapping adjacent cells or letting content spill outside its borders _(layout.json (region geometry) + acceptance criterion)_
- [ ] **1.2 · EXPECTED** [HH:mm] → hours 00-23 and minutes (24h); values equal to the player's system date/time _(option value)_
- [ ] **1.3 · EXPECTED** 1 line(s) of text, size 96px, colour #1c1c1c _(option value)_
- Cell result: ☐ PASS  ☐ FAIL  ☐ N/A — Notes: ______

## Cell 2 · clock-digital | bold red

Options: `format=<p style="margin:0;text-align:center;"><span style="font-si…`

- [ ] **2.1 · EXPECTED** The widget occupies the intended area (512x560 px) below the caption, without overlapping adjacent cells or letting content spill outside its borders _(layout.json (region geometry) + acceptance criterion)_
- [ ] **2.2 · EXPECTED** [HH:mm:ss] → hours 00-23, minutes and seconds (seconds advance every second); values equal to the player's system date/time _(option value)_
- [ ] **2.3 · EXPECTED** 1 line(s) of text, size 56px, colour #c62828, bold _(option value)_
- Cell result: ☐ PASS  ☐ FAIL  ☐ N/A — Notes: ______

## Cell 3 · clock-digital | two lines time+date

Options: `format=<p style="margin:0;text-align:center;"><span style="font-si…`

- [ ] **3.1 · EXPECTED** The widget occupies the intended area (512x560 px) below the caption, without overlapping adjacent cells or letting content spill outside its borders _(layout.json (region geometry) + acceptance criterion)_
- [ ] **3.2 · EXPECTED** [HH:mm] → hours 00-23 and minutes (24h); values equal to the player's system date/time _(option value)_
- [ ] **3.3 · EXPECTED** [DD/MM/YYYY] → date DD/MM/YYYY with 4-digit year; values equal to the player's system date/time _(option value)_
- [ ] **3.4 · EXPECTED** 2 line(s) of text, size 56px, colour #1c1c1c, bold _(option value)_
- Cell result: ☐ PASS  ☐ FAIL  ☐ N/A — Notes: ______
