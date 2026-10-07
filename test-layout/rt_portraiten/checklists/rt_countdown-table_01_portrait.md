# rt_countdown-table_01_portrait - checklist

Family `countdown-table` · 1080x1920 portrait · 120 s cycle · 5 cells · generated for Xibo 4.5.0

**EXPECTED** = derived from options, definitions or 4.5.0 code (source in brackets) · **OBSERVE** = not determinable in advance: record what you see.

## Layout

- [ ] **L1 · EXPECTED** Importing the zip completes without errors and creates the layout 'rt_countdown-table_01_portrait' _(LayoutFactory::createFromZip)_
- [ ] **L2 · EXPECTED** Size 1080x1920 px, orientation portrait; if the resolution does not exist in the CMS it is created ('1080 x 1920') _(LayoutFactory::createFromZip (getByDimensions → create))_
- [ ] **L3 · OBSERVE** Record the layout status after import (valid / draft / with warnings); if draft, publish it _(not determinable)_
- [ ] **L4 · EXPECTED** The Layout Editor shows 10 regions (per cell: caption + widget) _(layout.json)_
- [ ] **L5 · EXPECTED** Assigned to a portrait display (1080x1920): the layout fills the screen with no bars or cropping; if the display is physically rotated, set the rotation on the player _(layout.json (width/height))_
- [ ] **L6 · EXPECTED** The layout lasts 120 s (longest widget duration) and then restarts _(layout.json (duration))_
- [ ] **L7 · OBSERVE** Record whether, when the cycle restarts, countdowns, marquees and animations restart from scratch with no leftovers _(not determinable)_
- [ ] **L8 · EXPECTED** No errors in the player log over at least 2 full cycles _(general criterion)_

## Cell 1 · countdown-table | type=1 widget duration

Options: `countdownType=1`

- [ ] **1.1 · EXPECTED** The widget occupies the intended area (512x560 px) below the caption, without overlapping adjacent cells or letting content spill outside its borders _(layout.json (region geometry) + acceptance criterion)_
- [ ] **1.2 · EXPECTED** Starts at about 2:00 (120 s = widget duration) and decreases by 1 s per second _(xibo-countdown-render.js (type 1: widget duration))_
- [ ] **1.3 · OBSERVE** Record which fields are shown (years/months/days/hours/minutes/seconds) and whether the values are consistent with the remaining time _(not determinable from definitions)_
- Cell result: ☐ PASS  ☐ FAIL  ☐ N/A — Notes: ______

## Cell 2 · countdown-table | type=2 custom 90s

Options: `countdownType=2, countdownDuration=90`

- [ ] **2.1 · EXPECTED** The widget occupies the intended area (512x560 px) below the caption, without overlapping adjacent cells or letting content spill outside its borders _(layout.json (region geometry) + acceptance criterion)_
- [ ] **2.2 · EXPECTED** Starts at about 1:30 (90 s) and decreases by 1 s per second _(xibo-countdown-render.js (type 2: countdownDuration))_
- [ ] **2.3 · EXPECTED** After 90 s (before the end of the 120 s cycle) it reaches 0: all values 0 (hours/minutes/seconds '00') and the 'finished' style, which stays until the end _(xibo-countdown-render.js (total <= 0 → finished))_
- [ ] **2.4 · OBSERVE** Record which fields are shown (years/months/days/hours/minutes/seconds) and whether the values are consistent with the remaining time _(not determinable from definitions)_
- Cell result: ☐ PASS  ☐ FAIL  ☐ N/A — Notes: ______

## Cell 3 · countdown-table | type=3 date 2030-12-31 23:59:59

Options: `countdownType=3, countdownDate=2030-12-31 23:59:59`

- [ ] **3.1 · EXPECTED** The widget occupies the intended area (512x560 px) below the caption, without overlapping adjacent cells or letting content spill outside its borders _(layout.json (region geometry) + acceptance criterion)_
- [ ] **3.2 · EXPECTED** Remaining time equals the time between now and 2030-12-31 23:59:59 (compute the expected values with --expected-now) and decreases by 1 s per second _(xibo-countdown-render.js (type 3))_
- [ ] **3.3 · OBSERVE** Open the widget in the CMS editor: the 'Countdown Date' field must show the date 31/12/2030 23:59:59 (in the format set in the CMS), not an empty field or a wrong date: confirms the saved date format was read correctly _(to verify after import)_
- [ ] **3.4 · OBSERVE** Record which fields are shown (years/months/days/hours/minutes/seconds) and whether the values are consistent with the remaining time _(not determinable from definitions)_
- Cell result: ☐ PASS  ☐ FAIL  ☐ N/A — Notes: ______

## Cell 4 · countdown-table | type=3 date in the past (finished)

Options: `countdownType=3, countdownDate=2020-01-01 00:00:00`

- [ ] **4.1 · EXPECTED** The widget occupies the intended area (512x560 px) below the caption, without overlapping adjacent cells or letting content spill outside its borders _(layout.json (region geometry) + acceptance criterion)_
- [ ] **4.2 · EXPECTED** Date in the past: 'finished' state from the start, all values 0 (hours/minutes/seconds '00') and the widget's 'finished' style _(xibo-countdown-render.js (total <= 0))_
- [ ] **4.3 · OBSERVE** Open the widget in the CMS editor: the 'Countdown Date' field must show the date 01/01/2020 00:00:00 (in the format set in the CMS), not an empty field or a wrong date: confirms the saved date format was read correctly _(to verify after import)_
- [ ] **4.4 · OBSERVE** Record which fields are shown (years/months/days/hours/minutes/seconds) and whether the values are consistent with the remaining time _(not determinable from definitions)_
- Cell result: ☐ PASS  ☐ FAIL  ☐ N/A — Notes: ______

## Cell 5 · countdown-table | type=2 120s left/top + custom colours

Options: `countdownType=2, countdownDuration=120, alignmentH=left, alignmentV=top, headerTextColor=#ffffff, headerBackgroundColor=#1b5e20, evenRowTextColor=#1b5e20, evenRowBackgroundColor=#c8e6c9, oddRowTextColor=#1b5e20, oddRowBackgroundColor=#e8f5…`

- [ ] **5.1 · EXPECTED** The widget occupies the intended area (512x560 px) below the caption, without overlapping adjacent cells or letting content spill outside its borders _(layout.json (region geometry) + acceptance criterion)_
- [ ] **5.2 · EXPECTED** Starts at about 2:00 (120 s) and decreases by 1 s per second _(xibo-countdown-render.js (type 2: countdownDuration))_
- [ ] **5.3 · OBSERVE** Record which fields are shown (years/months/days/hours/minutes/seconds) and whether the values are consistent with the remaining time _(not determinable from definitions)_
- [ ] **5.4 · EXPECTED** Content aligned left / top in the area _(4.5.0 definition)_
- [ ] **5.5 · EXPECTED** Normal-state colours applied: headerTextColor=#ffffff, headerBackgroundColor=#1b5e20, evenRowTextColor=#1b5e20, evenRowBackgroundColor=#c8e6c9, oddRowTextColor=#1b5e20, oddRowBackgroundColor=#e8f5e9, borderColor=#1b5e20 _(option value)_
- Cell result: ☐ PASS  ☐ FAIL  ☐ N/A — Notes: ______
