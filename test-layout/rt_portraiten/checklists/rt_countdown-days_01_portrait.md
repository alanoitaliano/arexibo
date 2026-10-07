# rt_countdown-days_01_portrait - checklist

Family `countdown-days` · 1080x1920 portrait · 120 s cycle · 6 cells · generated for Xibo 4.5.0

**EXPECTED** = derived from options, definitions or 4.5.0 code (source in brackets) · **OBSERVE** = not determinable in advance: record what you see.

## Layout

- [ ] **L1 · EXPECTED** Importing the zip completes without errors and creates the layout 'rt_countdown-days_01_portrait' _(LayoutFactory::createFromZip)_
- [ ] **L2 · EXPECTED** Size 1080x1920 px, orientation portrait; if the resolution does not exist in the CMS it is created ('1080 x 1920') _(LayoutFactory::createFromZip (getByDimensions → create))_
- [ ] **L3 · OBSERVE** Record the layout status after import (valid / draft / with warnings); if draft, publish it _(not determinable)_
- [ ] **L4 · EXPECTED** The Layout Editor shows 12 regions (per cell: caption + widget) _(layout.json)_
- [ ] **L5 · EXPECTED** Assigned to a portrait display (1080x1920): the layout fills the screen with no bars or cropping; if the display is physically rotated, set the rotation on the player _(layout.json (width/height))_
- [ ] **L6 · EXPECTED** The layout lasts 120 s (longest widget duration) and then restarts _(layout.json (duration))_
- [ ] **L7 · OBSERVE** Record whether, when the cycle restarts, countdowns, marquees and animations restart from scratch with no leftovers _(not determinable)_
- [ ] **L8 · EXPECTED** No errors in the player log over at least 2 full cycles _(general criterion)_

## Cell 1 · countdown-days | type=1 widget duration

Options: `countdownType=1`

- [ ] **1.1 · EXPECTED** The widget occupies the intended area (512x560 px) below the caption, without overlapping adjacent cells or letting content spill outside its borders _(layout.json (region geometry) + acceptance criterion)_
- [ ] **1.2 · EXPECTED** Starts at about 2:00 (120 s = widget duration) and decreases by 1 s per second _(xibo-countdown-render.js (type 1: widget duration))_
- [ ] **1.3 · OBSERVE** Record which fields are shown (years/months/days/hours/minutes/seconds) and whether the values are consistent with the remaining time _(not determinable from definitions)_
- Cell result: ☐ PASS  ☐ FAIL  ☐ N/A — Notes: ______

## Cell 2 · countdown-days | type=2 90s warning after 30s

Options: `countdownType=2, countdownDuration=90, countdownWarningDuration=30`

- [ ] **2.1 · EXPECTED** The widget occupies the intended area (512x560 px) below the caption, without overlapping adjacent cells or letting content spill outside its borders _(layout.json (region geometry) + acceptance criterion)_
- [ ] **2.2 · EXPECTED** Starts at about 1:30 (90 s) and decreases by 1 s per second _(xibo-countdown-render.js (type 2: countdownDuration))_
- [ ] **2.3 · EXPECTED** After 90 s (before the end of the 120 s cycle) it reaches 0: all values 0 (hours/minutes/seconds '00') and the 'finished' style, which stays until the end _(xibo-countdown-render.js (total <= 0 → finished))_
- [ ] **2.4 · EXPECTED** Per the code, after about 30 s from the start (~60 s left) the widget switches to the 'warning' style _(xibo-countdown-render.js: warningDate = start + N)_
- [ ] **2.5 · OBSERVE** SOURCE CONFLICT: the field's help text says the warning starts 'from the end' (i.e. when 30 s are left, after ~60 s from the start). Record after how many seconds the 'warning' style really appears: ~30 s = the code is right, ~60 s = the help text is right _(countdown-*.xml (helpText) vs xibo-countdown-render.js)_
- [ ] **2.6 · OBSERVE** Record which fields are shown (years/months/days/hours/minutes/seconds) and whether the values are consistent with the remaining time _(not determinable from definitions)_
- Cell result: ☐ PASS  ☐ FAIL  ☐ N/A — Notes: ______

## Cell 3 · countdown-days | type=3 date 2030-12-31 23:59:59

Options: `countdownType=3, countdownDate=2030-12-31 23:59:59`

- [ ] **3.1 · EXPECTED** The widget occupies the intended area (512x560 px) below the caption, without overlapping adjacent cells or letting content spill outside its borders _(layout.json (region geometry) + acceptance criterion)_
- [ ] **3.2 · EXPECTED** Remaining time equals the time between now and 2030-12-31 23:59:59 (compute the expected values with --expected-now) and decreases by 1 s per second _(xibo-countdown-render.js (type 3))_
- [ ] **3.3 · OBSERVE** Open the widget in the CMS editor: the 'Countdown Date' field must show the date 31/12/2030 23:59:59 (in the format set in the CMS), not an empty field or a wrong date: confirms the saved date format was read correctly _(to verify after import)_
- [ ] **3.4 · OBSERVE** Record which fields are shown (years/months/days/hours/minutes/seconds) and whether the values are consistent with the remaining time _(not determinable from definitions)_
- Cell result: ☐ PASS  ☐ FAIL  ☐ N/A — Notes: ______

## Cell 4 · countdown-days | type=3 date in the past (finished)

Options: `countdownType=3, countdownDate=2020-01-01 00:00:00`

- [ ] **4.1 · EXPECTED** The widget occupies the intended area (512x560 px) below the caption, without overlapping adjacent cells or letting content spill outside its borders _(layout.json (region geometry) + acceptance criterion)_
- [ ] **4.2 · EXPECTED** Date in the past: 'finished' state from the start, all values 0 (hours/minutes/seconds '00') and the widget's 'finished' style _(xibo-countdown-render.js (total <= 0))_
- [ ] **4.3 · OBSERVE** Open the widget in the CMS editor: the 'Countdown Date' field must show the date 01/01/2020 00:00:00 (in the format set in the CMS), not an empty field or a wrong date: confirms the saved date format was read correctly _(to verify after import)_
- [ ] **4.4 · OBSERVE** Record which fields are shown (years/months/days/hours/minutes/seconds) and whether the values are consistent with the remaining time _(not determinable from definitions)_
- Cell result: ☐ PASS  ☐ FAIL  ☐ N/A — Notes: ______

## Cell 5 · countdown-days | type=3 future date, warning date in past

Options: `countdownType=3, countdownDate=2030-12-31 23:59:59, countdownWarningDate=2020-01-01 00:00:00`

- [ ] **5.1 · EXPECTED** The widget occupies the intended area (512x560 px) below the caption, without overlapping adjacent cells or letting content spill outside its borders _(layout.json (region geometry) + acceptance criterion)_
- [ ] **5.2 · EXPECTED** Remaining time equals the time between now and 2030-12-31 23:59:59 (compute the expected values with --expected-now) and decreases by 1 s per second _(xibo-countdown-render.js (type 3))_
- [ ] **5.3 · OBSERVE** Open the widget in the CMS editor: the 'Countdown Date' field must show the date 31/12/2030 23:59:59 (in the format set in the CMS), not an empty field or a wrong date: confirms the saved date format was read correctly _(to verify after import)_
- [ ] **5.4 · EXPECTED** Warning date in the past: 'warning' style from the start _(xibo-countdown-render.js (warningDate.diff(now) <= 0))_
- [ ] **5.5 · OBSERVE** Record which fields are shown (years/months/days/hours/minutes/seconds) and whether the values are consistent with the remaining time _(not determinable from definitions)_
- Cell result: ☐ PASS  ☐ FAIL  ☐ N/A — Notes: ______

## Cell 6 · countdown-days | type=2 120s left/top + custom colours

Options: `countdownType=2, countdownDuration=120, alignmentH=left, alignmentV=top, textColor=#b71c1c, textBackgroundColor=#fff8e1, borderColor=#b71c1c, labelTextColor=#555555, warningBackgroundColor=#ff8f00, finishedBackgroundColor=#7f0000`

- [ ] **6.1 · EXPECTED** The widget occupies the intended area (512x560 px) below the caption, without overlapping adjacent cells or letting content spill outside its borders _(layout.json (region geometry) + acceptance criterion)_
- [ ] **6.2 · EXPECTED** Starts at about 2:00 (120 s) and decreases by 1 s per second _(xibo-countdown-render.js (type 2: countdownDuration))_
- [ ] **6.3 · OBSERVE** Record which fields are shown (years/months/days/hours/minutes/seconds) and whether the values are consistent with the remaining time _(not determinable from definitions)_
- [ ] **6.4 · EXPECTED** Content aligned left / top in the area _(4.5.0 definition)_
- [ ] **6.5 · EXPECTED** Normal-state colours applied: textColor=#b71c1c, textBackgroundColor=#fff8e1, borderColor=#b71c1c, labelTextColor=#555555 _(option value)_
- [ ] **6.6 · OBSERVE** Warning/finished state colours (warningBackgroundColor=#ff8f00, finishedBackgroundColor=#7f0000) are not visible in this variant (states not reached): check them in the warning/finished variants _(not verifiable here)_
- Cell result: ☐ PASS  ☐ FAIL  ☐ N/A — Notes: ______
