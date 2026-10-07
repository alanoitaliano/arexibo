# rt_worldclock-analogue_02_portrait - checklist

Family `worldclock-analogue` · 1080x1920 portrait · 60 s cycle · 3 cells · generated for Xibo 4.5.0

**EXPECTED** = derived from options, definitions or 4.5.0 code (source in brackets) · **OBSERVE** = not determinable in advance: record what you see.

## Layout

- [ ] **L1 · EXPECTED** Importing the zip completes without errors and creates the layout 'rt_worldclock-analogue_02_portrait' _(LayoutFactory::createFromZip)_
- [ ] **L2 · EXPECTED** Size 1080x1920 px, orientation portrait; if the resolution does not exist in the CMS it is created ('1080 x 1920') _(LayoutFactory::createFromZip (getByDimensions → create))_
- [ ] **L3 · OBSERVE** Record the layout status after import (valid / draft / with warnings); if draft, publish it _(not determinable)_
- [ ] **L4 · EXPECTED** The Layout Editor shows 6 regions (per cell: caption + widget) _(layout.json)_
- [ ] **L5 · EXPECTED** Assigned to a portrait display (1080x1920): the layout fills the screen with no bars or cropping; if the display is physically rotated, set the rotation on the player _(layout.json (width/height))_
- [ ] **L6 · EXPECTED** The layout lasts 60 s (longest widget duration) and then restarts _(layout.json (duration))_
- [ ] **L7 · OBSERVE** Record whether, when the cycle restarts, countdowns, marquees and animations restart from scratch with no leftovers _(not determinable)_
- [ ] **L8 · EXPECTED** No errors in the player log over at least 2 full cycles _(general criterion)_

## Cell 1 · worldclock-analogue | 2 clocks: hands only (all toggles off)

Options: `worldClocks=[{"clockTimezone":"Europe/Rome","clockLabel":"Rome","clockH…, numCols=2, numRows=1, showSecondsHand=0, showSteps=0, showDetailed=0, showMiniDigitalClock=0, showLabel=0`

- [ ] **1.1 · EXPECTED** The widget occupies the intended area (512x560 px) below the caption, without overlapping adjacent cells or letting content spill outside its borders _(layout.json (region geometry) + acceptance criterion)_
- [ ] **1.2 · EXPECTED** 2 clock(s): Rome (Europe/Rome), New York (America/New_York) _(option value)_
- [ ] **1.3 · EXPECTED** Arranged in 2 column(s) × 1 row(s) _(worldclock-*.xml (numCols/numRows))_
- [ ] **1.4 · EXPECTED** Each clock shows the time of its own timezone (compare with --expected-now) and advances _(xibo-worldclock-render.js (moment.tz))_
- [ ] **1.5 · EXPECTED** No seconds hand _(worldclock-analogue.xml (showSecondsHand=0))_
- [ ] **1.6 · EXPECTED** No ticks on the dial _(worldclock-analogue.xml (showSteps=0))_
- [ ] **1.7 · EXPECTED** Flat look, no shadows/3D effects _(worldclock-analogue.xml (showDetailed=0))_
- [ ] **1.8 · EXPECTED** No inner mini digital clock _(worldclock-analogue.xml (showMiniDigitalClock=0))_
- [ ] **1.9 · EXPECTED** No timezone label _(worldclock-analogue.xml (showLabel=0))_
- Cell result: ☐ PASS  ☐ FAIL  ☐ N/A — Notes: ______

## Cell 2 · worldclock-analogue | 2 clocks: no seconds hand, no mini digital

Options: `worldClocks=[{"clockTimezone":"Europe/Rome","clockLabel":"Rome","clockH…, numCols=2, numRows=1, showSecondsHand=0, showMiniDigitalClock=0`

- [ ] **2.1 · EXPECTED** The widget occupies the intended area (512x560 px) below the caption, without overlapping adjacent cells or letting content spill outside its borders _(layout.json (region geometry) + acceptance criterion)_
- [ ] **2.2 · EXPECTED** 2 clock(s): Rome (Europe/Rome), New York (America/New_York) _(option value)_
- [ ] **2.3 · EXPECTED** Arranged in 2 column(s) × 1 row(s) _(worldclock-*.xml (numCols/numRows))_
- [ ] **2.4 · EXPECTED** Each clock shows the time of its own timezone (compare with --expected-now) and advances _(xibo-worldclock-render.js (moment.tz))_
- [ ] **2.5 · EXPECTED** No seconds hand _(worldclock-analogue.xml (showSecondsHand=0))_
- [ ] **2.6 · EXPECTED** No inner mini digital clock _(worldclock-analogue.xml (showMiniDigitalClock=0))_
- Cell result: ☐ PASS  ☐ FAIL  ☐ N/A — Notes: ______

## Cell 3 · worldclock-analogue | 2 clocks: no steps/detailed, label colours

Options: `worldClocks=[{"clockTimezone":"Europe/Rome","clockLabel":"Rome","clockH…, numCols=2, numRows=1, showSteps=0, showDetailed=0, labelTextColor=#000000, labelBgColor=#ffeb3b`

- [ ] **3.1 · EXPECTED** The widget occupies the intended area (512x560 px) below the caption, without overlapping adjacent cells or letting content spill outside its borders _(layout.json (region geometry) + acceptance criterion)_
- [ ] **3.2 · EXPECTED** 2 clock(s): Rome (Europe/Rome), New York (America/New_York) _(option value)_
- [ ] **3.3 · EXPECTED** Arranged in 2 column(s) × 1 row(s) _(worldclock-*.xml (numCols/numRows))_
- [ ] **3.4 · EXPECTED** Each clock shows the time of its own timezone (compare with --expected-now) and advances _(xibo-worldclock-render.js (moment.tz))_
- [ ] **3.5 · EXPECTED** No ticks on the dial _(worldclock-analogue.xml (showSteps=0))_
- [ ] **3.6 · EXPECTED** Flat look, no shadows/3D effects _(worldclock-analogue.xml (showDetailed=0))_
- [ ] **3.7 · EXPECTED** Colours applied: labelTextColor=#000000, labelBgColor=#ffeb3b _(option value)_
- Cell result: ☐ PASS  ☐ FAIL  ☐ N/A — Notes: ______
