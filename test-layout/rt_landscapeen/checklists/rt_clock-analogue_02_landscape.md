# rt_clock-analogue_02_landscape - checklist

Family `clock-analogue` · 1920x1080 landscape · 60 s cycle · 2 cells · generated for Xibo 4.5.0

**EXPECTED** = derived from options, definitions or 4.5.0 code (source in brackets) · **OBSERVE** = not determinable in advance: record what you see.

## Layout

- [ ] **L1 · EXPECTED** Importing the zip completes without errors and creates the layout 'rt_clock-analogue_02_landscape' _(LayoutFactory::createFromZip)_
- [ ] **L2 · EXPECTED** Size 1920x1080 px, orientation landscape; if the resolution does not exist in the CMS it is created ('1920 x 1080') _(LayoutFactory::createFromZip (getByDimensions → create))_
- [ ] **L3 · OBSERVE** Record the layout status after import (valid / draft / with warnings); if draft, publish it _(not determinable)_
- [ ] **L4 · EXPECTED** The Layout Editor shows 4 regions (per cell: caption + widget) _(layout.json)_
- [ ] **L5 · EXPECTED** Assigned to a landscape display (1920x1080): the layout fills the screen with no bars or cropping; if the display is physically rotated, set the rotation on the player _(layout.json (width/height))_
- [ ] **L6 · EXPECTED** The layout lasts 60 s (longest widget duration) and then restarts _(layout.json (duration))_
- [ ] **L7 · OBSERVE** Record whether, when the cycle restarts, countdowns, marquees and animations restart from scratch with no leftovers _(not determinable)_
- [ ] **L8 · EXPECTED** No errors in the player log over at least 2 full cycles _(general criterion)_

## Cell 1 · clock-analogue | theme=1 offset=+180

Options: `themeId=1, offset=180`

- [ ] **1.1 · EXPECTED** The widget occupies the intended area (616x456 px) below the caption, without overlapping adjacent cells or letting content spill outside its borders _(layout.json (region geometry) + acceptance criterion)_
- [ ] **1.2 · EXPECTED** Analogue clock: the hands show the player's system time and move _(option value)_
- [ ] **1.3 · EXPECTED** Theme Light _(clock-analogue.xml)_
- [ ] **1.4 · EXPECTED** Time shown = system time +180 min (3 h 00 min) _(clock-analogue.xml (offset help))_
- Cell result: ☐ PASS  ☐ FAIL  ☐ N/A — Notes: ______

## Cell 2 · clock-analogue | theme=2 offset=-300

Options: `themeId=2, offset=-300`

- [ ] **2.1 · EXPECTED** The widget occupies the intended area (616x456 px) below the caption, without overlapping adjacent cells or letting content spill outside its borders _(layout.json (region geometry) + acceptance criterion)_
- [ ] **2.2 · EXPECTED** Analogue clock: the hands show the player's system time and move _(option value)_
- [ ] **2.3 · EXPECTED** Theme Dark _(clock-analogue.xml)_
- [ ] **2.4 · EXPECTED** Time shown = system time -300 min (5 h 00 min) _(clock-analogue.xml (offset help))_
- Cell result: ☐ PASS  ☐ FAIL  ☐ N/A — Notes: ______
