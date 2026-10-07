# rt_countdown-custom_01_portrait - checklist

Family `countdown-custom` · 1080x1920 portrait · 120 s cycle · 6 cells · generated for Xibo 4.5.0

**EXPECTED** = derived from options, definitions or 4.5.0 code (source in brackets) · **OBSERVE** = not determinable in advance: record what you see.

## Layout

- [ ] **L1 · EXPECTED** Importing the zip completes without errors and creates the layout 'rt_countdown-custom_01_portrait' _(LayoutFactory::createFromZip)_
- [ ] **L2 · EXPECTED** Size 1080x1920 px, orientation portrait; if the resolution does not exist in the CMS it is created ('1080 x 1920') _(LayoutFactory::createFromZip (getByDimensions → create))_
- [ ] **L3 · OBSERVE** Record the layout status after import (valid / draft / with warnings); if draft, publish it _(not determinable)_
- [ ] **L4 · EXPECTED** The Layout Editor shows 12 regions (per cell: caption + widget) _(layout.json)_
- [ ] **L5 · EXPECTED** Assigned to a portrait display (1080x1920): the layout fills the screen with no bars or cropping; if the display is physically rotated, set the rotation on the player _(layout.json (width/height))_
- [ ] **L6 · EXPECTED** The layout lasts 120 s (longest widget duration) and then restarts _(layout.json (duration))_
- [ ] **L7 · OBSERVE** Record whether, when the cycle restarts, countdowns, marquees and animations restart from scratch with no leftovers _(not determinable)_
- [ ] **L8 · EXPECTED** No errors in the player log over at least 2 full cycles _(general criterion)_

## Cell 1 · countdown-custom | type=1 widget duration

Options: `customTemplate=1, moduleType=countdown, mainTemplate=<div class="cd"><div class="big">[hha]h [mm]m [ss]s</div><d…, styleSheet=.cd{font-family:sans-serif;text-align:center}.cd .big{font-…, countdownType=1`

- [ ] **1.1 · EXPECTED** The widget occupies the intended area (512x560 px) below the caption, without overlapping adjacent cells or letting content spill outside its borders _(layout.json (region geometry) + acceptance criterion)_
- [ ] **1.2 · EXPECTED** Starts at about 2:00 (120 s = widget duration) and decreases by 1 s per second _(xibo-countdown-render.js (type 1: widget duration))_
- [ ] **1.3 · EXPECTED** Shows 'Hh Mm Ss' with [hha] = total hours and [mm], [ss] as 2 digits, and below 'DDd | MMm | YYy' with total days, months and years, consistent with the remaining time; large bold blue #0d47a1 48px line, small grey 24px line _(custom template (mainTemplate/styleSheet))_
- Cell result: ☐ PASS  ☐ FAIL  ☐ N/A — Notes: ______

## Cell 2 · countdown-custom | type=2 90s warning after 30s

Options: `customTemplate=1, moduleType=countdown, mainTemplate=<div class="cd"><div class="big">[hha]h [mm]m [ss]s</div><d…, styleSheet=.cd{font-family:sans-serif;text-align:center}.cd .big{font-…, countdownType=2, countdownDuration=90, countdownWar…`

- [ ] **2.1 · EXPECTED** The widget occupies the intended area (512x560 px) below the caption, without overlapping adjacent cells or letting content spill outside its borders _(layout.json (region geometry) + acceptance criterion)_
- [ ] **2.2 · EXPECTED** Starts at about 1:30 (90 s) and decreases by 1 s per second _(xibo-countdown-render.js (type 2: countdownDuration))_
- [ ] **2.3 · EXPECTED** After 90 s (before the end of the 120 s cycle) it reaches 0: all values 0 (hours/minutes/seconds '00') and the 'finished' style, which stays until the end _(xibo-countdown-render.js (total <= 0 → finished))_
- [ ] **2.4 · EXPECTED** Per the code, after about 30 s from the start (~60 s left) the widget switches to the 'warning' style _(xibo-countdown-render.js: warningDate = start + N)_
- [ ] **2.5 · OBSERVE** SOURCE CONFLICT: the field's help text says the warning starts 'from the end' (i.e. when 30 s are left, after ~60 s from the start). Record after how many seconds the 'warning' style really appears: ~30 s = the code is right, ~60 s = the help text is right _(countdown-*.xml (helpText) vs xibo-countdown-render.js)_
- [ ] **2.6 · EXPECTED** Shows 'Hh Mm Ss' with [hha] = total hours and [mm], [ss] as 2 digits, and below 'DDd | MMm | YYy' with total days, months and years, consistent with the remaining time; large bold blue #0d47a1 48px line, small grey 24px line _(custom template (mainTemplate/styleSheet))_
- Cell result: ☐ PASS  ☐ FAIL  ☐ N/A — Notes: ______

## Cell 3 · countdown-custom | type=3 date 2030-12-31 23:59:59

Options: `customTemplate=1, moduleType=countdown, mainTemplate=<div class="cd"><div class="big">[hha]h [mm]m [ss]s</div><d…, styleSheet=.cd{font-family:sans-serif;text-align:center}.cd .big{font-…, countdownType=3, countdownDate=2030-12-31 23:59:59`

- [ ] **3.1 · EXPECTED** The widget occupies the intended area (512x560 px) below the caption, without overlapping adjacent cells or letting content spill outside its borders _(layout.json (region geometry) + acceptance criterion)_
- [ ] **3.2 · EXPECTED** Remaining time equals the time between now and 2030-12-31 23:59:59 (compute the expected values with --expected-now) and decreases by 1 s per second _(xibo-countdown-render.js (type 3))_
- [ ] **3.3 · OBSERVE** Open the widget in the CMS editor: the 'Countdown Date' field must show the date 31/12/2030 23:59:59 (in the format set in the CMS), not an empty field or a wrong date: confirms the saved date format was read correctly _(to verify after import)_
- [ ] **3.4 · EXPECTED** Shows 'Hh Mm Ss' with [hha] = total hours and [mm], [ss] as 2 digits, and below 'DDd | MMm | YYy' with total days, months and years, consistent with the remaining time; large bold blue #0d47a1 48px line, small grey 24px line _(custom template (mainTemplate/styleSheet))_
- Cell result: ☐ PASS  ☐ FAIL  ☐ N/A — Notes: ______

## Cell 4 · countdown-custom | type=3 date in the past (finished)

Options: `customTemplate=1, moduleType=countdown, mainTemplate=<div class="cd"><div class="big">[hha]h [mm]m [ss]s</div><d…, styleSheet=.cd{font-family:sans-serif;text-align:center}.cd .big{font-…, countdownType=3, countdownDate=2020-01-01 00:00:00`

- [ ] **4.1 · EXPECTED** The widget occupies the intended area (512x560 px) below the caption, without overlapping adjacent cells or letting content spill outside its borders _(layout.json (region geometry) + acceptance criterion)_
- [ ] **4.2 · EXPECTED** Date in the past: 'finished' state from the start, all values 0 (hours/minutes/seconds '00') and the widget's 'finished' style _(xibo-countdown-render.js (total <= 0))_
- [ ] **4.3 · OBSERVE** Open the widget in the CMS editor: the 'Countdown Date' field must show the date 01/01/2020 00:00:00 (in the format set in the CMS), not an empty field or a wrong date: confirms the saved date format was read correctly _(to verify after import)_
- [ ] **4.4 · EXPECTED** Shows 'Hh Mm Ss' with [hha] = total hours and [mm], [ss] as 2 digits, and below 'DDd | MMm | YYy' with total days, months and years, consistent with the remaining time; large bold blue #0d47a1 48px line, small grey 24px line _(custom template (mainTemplate/styleSheet))_
- Cell result: ☐ PASS  ☐ FAIL  ☐ N/A — Notes: ______

## Cell 5 · countdown-custom | type=3 future date, warning date in past

Options: `customTemplate=1, moduleType=countdown, mainTemplate=<div class="cd"><div class="big">[hha]h [mm]m [ss]s</div><d…, styleSheet=.cd{font-family:sans-serif;text-align:center}.cd .big{font-…, countdownType=3, countdownDate=2030-12-31 23:59:59,…`

- [ ] **5.1 · EXPECTED** The widget occupies the intended area (512x560 px) below the caption, without overlapping adjacent cells or letting content spill outside its borders _(layout.json (region geometry) + acceptance criterion)_
- [ ] **5.2 · EXPECTED** Remaining time equals the time between now and 2030-12-31 23:59:59 (compute the expected values with --expected-now) and decreases by 1 s per second _(xibo-countdown-render.js (type 3))_
- [ ] **5.3 · OBSERVE** Open the widget in the CMS editor: the 'Countdown Date' field must show the date 31/12/2030 23:59:59 (in the format set in the CMS), not an empty field or a wrong date: confirms the saved date format was read correctly _(to verify after import)_
- [ ] **5.4 · EXPECTED** Warning date in the past: 'warning' style from the start _(xibo-countdown-render.js (warningDate.diff(now) <= 0))_
- [ ] **5.5 · EXPECTED** Shows 'Hh Mm Ss' with [hha] = total hours and [mm], [ss] as 2 digits, and below 'DDd | MMm | YYy' with total days, months and years, consistent with the remaining time; large bold blue #0d47a1 48px line, small grey 24px line _(custom template (mainTemplate/styleSheet))_
- Cell result: ☐ PASS  ☐ FAIL  ☐ N/A — Notes: ______

## Cell 6 · countdown-custom | type=2 120s left/top + custom colours

Options: `customTemplate=1, moduleType=countdown, mainTemplate=<div class="cd"><div class="big">[hha]h [mm]m [ss]s</div><d…, styleSheet=.cd{font-family:sans-serif;text-align:center}.cd .big{font-…, countdownType=2, countdownDuration=120, alignmentH=…`

- [ ] **6.1 · EXPECTED** The widget occupies the intended area (512x560 px) below the caption, without overlapping adjacent cells or letting content spill outside its borders _(layout.json (region geometry) + acceptance criterion)_
- [ ] **6.2 · EXPECTED** Starts at about 2:00 (120 s) and decreases by 1 s per second _(xibo-countdown-render.js (type 2: countdownDuration))_
- [ ] **6.3 · EXPECTED** Shows 'Hh Mm Ss' with [hha] = total hours and [mm], [ss] as 2 digits, and below 'DDd | MMm | YYy' with total days, months and years, consistent with the remaining time; large bold blue #0d47a1 48px line, small grey 24px line _(custom template (mainTemplate/styleSheet))_
- [ ] **6.4 · EXPECTED** Content aligned left / top in the area _(4.5.0 definition)_
- Cell result: ☐ PASS  ☐ FAIL  ☐ N/A — Notes: ______
