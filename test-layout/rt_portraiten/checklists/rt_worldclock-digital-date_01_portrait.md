# rt_worldclock-digital-date_01_portrait - checklist

Family `worldclock-digital-date` · 1080x1920 portrait · 60 s cycle · 6 cells · generated for Xibo 4.5.0

**EXPECTED** = derived from options, definitions or 4.5.0 code (source in brackets) · **OBSERVE** = not determinable in advance: record what you see.

## Layout

- [ ] **L1 · EXPECTED** Importing the zip completes without errors and creates the layout 'rt_worldclock-digital-date_01_portrait' _(LayoutFactory::createFromZip)_
- [ ] **L2 · EXPECTED** Size 1080x1920 px, orientation portrait; if the resolution does not exist in the CMS it is created ('1080 x 1920') _(LayoutFactory::createFromZip (getByDimensions → create))_
- [ ] **L3 · OBSERVE** Record the layout status after import (valid / draft / with warnings); if draft, publish it _(not determinable)_
- [ ] **L4 · EXPECTED** The Layout Editor shows 12 regions (per cell: caption + widget) _(layout.json)_
- [ ] **L5 · EXPECTED** Assigned to a portrait display (1080x1920): the layout fills the screen with no bars or cropping; if the display is physically rotated, set the rotation on the player _(layout.json (width/height))_
- [ ] **L6 · EXPECTED** The layout lasts 60 s (longest widget duration) and then restarts _(layout.json (duration))_
- [ ] **L7 · OBSERVE** Record whether, when the cycle restarts, countdowns, marquees and animations restart from scratch with no leftovers _(not determinable)_
- [ ] **L8 · EXPECTED** No errors in the player log over at least 2 full cycles _(general criterion)_

## Cell 1 · worldclock-digital-date | 1 clock 1x1

Options: `worldClocks=[{"clockTimezone":"Europe/Rome","clockLabel":"Rome","clockH…, numCols=1, numRows=1`

- [ ] **1.1 · EXPECTED** The widget occupies the intended area (512x560 px) below the caption, without overlapping adjacent cells or letting content spill outside its borders _(layout.json (region geometry) + acceptance criterion)_
- [ ] **1.2 · EXPECTED** 1 clock(s): Rome (Europe/Rome) _(option value)_
- [ ] **1.3 · EXPECTED** Arranged in 1 column(s) × 1 row(s) _(worldclock-*.xml (numCols/numRows))_
- [ ] **1.4 · EXPECTED** Each clock shows the time of its own timezone (compare with --expected-now) and advances _(xibo-worldclock-render.js (moment.tz))_
- Cell result: ☐ PASS  ☐ FAIL  ☐ N/A — Notes: ______

## Cell 2 · worldclock-digital-date | 2 clocks 2x1

Options: `worldClocks=[{"clockTimezone":"Europe/Rome","clockLabel":"Rome","clockH…, numCols=2, numRows=1`

- [ ] **2.1 · EXPECTED** The widget occupies the intended area (512x560 px) below the caption, without overlapping adjacent cells or letting content spill outside its borders _(layout.json (region geometry) + acceptance criterion)_
- [ ] **2.2 · EXPECTED** 2 clock(s): Rome (Europe/Rome), New York (America/New_York) _(option value)_
- [ ] **2.3 · EXPECTED** Arranged in 2 column(s) × 1 row(s) _(worldclock-*.xml (numCols/numRows))_
- [ ] **2.4 · EXPECTED** Each clock shows the time of its own timezone (compare with --expected-now) and advances _(xibo-worldclock-render.js (moment.tz))_
- Cell result: ☐ PASS  ☐ FAIL  ☐ N/A — Notes: ______

## Cell 3 · worldclock-digital-date | 4 clocks 2x2

Options: `worldClocks=[{"clockTimezone":"Europe/Rome","clockLabel":"Rome","clockH…, numCols=2, numRows=2`

- [ ] **3.1 · EXPECTED** The widget occupies the intended area (512x560 px) below the caption, without overlapping adjacent cells or letting content spill outside its borders _(layout.json (region geometry) + acceptance criterion)_
- [ ] **3.2 · EXPECTED** 4 clock(s): Rome (Europe/Rome), New York (America/New_York), Tokyo (Asia/Tokyo), Sydney (Australia/Sydney) _(option value)_
- [ ] **3.3 · EXPECTED** Arranged in 2 column(s) × 2 row(s) _(worldclock-*.xml (numCols/numRows))_
- [ ] **3.4 · EXPECTED** Each clock shows the time of its own timezone (compare with --expected-now) and advances _(xibo-worldclock-render.js (moment.tz))_
- Cell result: ☐ PASS  ☐ FAIL  ☐ N/A — Notes: ______

## Cell 4 · worldclock-digital-date | 4 clocks 1x4 (column)

Options: `worldClocks=[{"clockTimezone":"Europe/Rome","clockLabel":"Rome","clockH…, numCols=1, numRows=4`

- [ ] **4.1 · EXPECTED** The widget occupies the intended area (512x560 px) below the caption, without overlapping adjacent cells or letting content spill outside its borders _(layout.json (region geometry) + acceptance criterion)_
- [ ] **4.2 · EXPECTED** 4 clock(s): Rome (Europe/Rome), New York (America/New_York), Tokyo (Asia/Tokyo), Sydney (Australia/Sydney) _(option value)_
- [ ] **4.3 · EXPECTED** Arranged in 1 column(s) × 4 row(s) _(worldclock-*.xml (numCols/numRows))_
- [ ] **4.4 · EXPECTED** Each clock shows the time of its own timezone (compare with --expected-now) and advances _(xibo-worldclock-render.js (moment.tz))_
- Cell result: ☐ PASS  ☐ FAIL  ☐ N/A — Notes: ______

## Cell 5 · worldclock-digital-date | 4 clocks 2x2 highlight #2, left/top

Options: `worldClocks=[{"clockTimezone":"Europe/Rome","clockLabel":"Rome","clockH…, numCols=2, numRows=2, alignmentH=left, alignmentV=top`

- [ ] **5.1 · EXPECTED** The widget occupies the intended area (512x560 px) below the caption, without overlapping adjacent cells or letting content spill outside its borders _(layout.json (region geometry) + acceptance criterion)_
- [ ] **5.2 · EXPECTED** 4 clock(s): Rome (Europe/Rome), New York (America/New_York), Tokyo (Asia/Tokyo), Sydney (Australia/Sydney) _(option value)_
- [ ] **5.3 · EXPECTED** Arranged in 2 column(s) × 2 row(s) _(worldclock-*.xml (numCols/numRows))_
- [ ] **5.4 · EXPECTED** Each clock shows the time of its own timezone (compare with --expected-now) and advances _(xibo-worldclock-render.js (moment.tz))_
- [ ] **5.5 · OBSERVE** 'New York' has clockHighlight=1: record how it is highlighted _(xibo-worldclock-render.js (clockHighlight))_
- [ ] **5.6 · EXPECTED** Grid aligned left / top in the area _(4.5.0 definition)_
- Cell result: ☐ PASS  ☐ FAIL  ☐ N/A — Notes: ______

## Cell 6 · worldclock-digital-date | 2 clocks 2x1 custom colours

Options: `worldClocks=[{"clockTimezone":"Europe/Rome","clockLabel":"Rome","clockH…, numCols=2, numRows=1, labelColor=#ffca28, dateTimeColor=#ffffff, backgroundColor=#1a237e`

- [ ] **6.1 · EXPECTED** The widget occupies the intended area (512x560 px) below the caption, without overlapping adjacent cells or letting content spill outside its borders _(layout.json (region geometry) + acceptance criterion)_
- [ ] **6.2 · EXPECTED** 2 clock(s): Rome (Europe/Rome), New York (America/New_York) _(option value)_
- [ ] **6.3 · EXPECTED** Arranged in 2 column(s) × 1 row(s) _(worldclock-*.xml (numCols/numRows))_
- [ ] **6.4 · EXPECTED** Each clock shows the time of its own timezone (compare with --expected-now) and advances _(xibo-worldclock-render.js (moment.tz))_
- [ ] **6.5 · EXPECTED** Colours applied: labelColor=#ffca28, dateTimeColor=#ffffff, backgroundColor=#1a237e _(option value)_
- Cell result: ☐ PASS  ☐ FAIL  ☐ N/A — Notes: ______
