# rt_clock-analogue_01_portrait - checklist

Family `clock-analogue` · 1080x1920 portrait · 60 s cycle · 6 cells · generated for Xibo 4.5.0

**EXPECTED** = derived from options, definitions or 4.5.0 code (source in brackets) · **OBSERVE** = not determinable in advance: record what you see.

## Layout

- [ ] **L1 · EXPECTED** Importing the zip completes without errors and creates the layout 'rt_clock-analogue_01_portrait' _(LayoutFactory::createFromZip)_
- [ ] **L2 · EXPECTED** Size 1080x1920 px, orientation portrait; if the resolution does not exist in the CMS it is created ('1080 x 1920') _(LayoutFactory::createFromZip (getByDimensions → create))_
- [ ] **L3 · OBSERVE** Record the layout status after import (valid / draft / with warnings); if draft, publish it _(not determinable)_
- [ ] **L4 · EXPECTED** The Layout Editor shows 12 regions (per cell: caption + widget) _(layout.json)_
- [ ] **L5 · EXPECTED** Assigned to a portrait display (1080x1920): the layout fills the screen with no bars or cropping; if the display is physically rotated, set the rotation on the player _(layout.json (width/height))_
- [ ] **L6 · EXPECTED** The layout lasts 60 s (longest widget duration) and then restarts _(layout.json (duration))_
- [ ] **L7 · OBSERVE** Record whether, when the cycle restarts, countdowns, marquees and animations restart from scratch with no leftovers _(not determinable)_
- [ ] **L8 · EXPECTED** No errors in the player log over at least 2 full cycles _(general criterion)_

## Cell 1 · clock-analogue | theme=1 | center/middle

Options: `themeId=1, alignmentH=center, alignmentV=middle`

- [ ] **1.1 · EXPECTED** The widget occupies the intended area (512x560 px) below the caption, without overlapping adjacent cells or letting content spill outside its borders _(layout.json (region geometry) + acceptance criterion)_
- [ ] **1.2 · EXPECTED** Analogue clock: the hands show the player's system time and move _(option value)_
- [ ] **1.3 · EXPECTED** Theme Light _(clock-analogue.xml)_
- [ ] **1.4 · EXPECTED** Clock face aligned center / middle in the area (only noticeable if the area is larger than the face) _(clock-analogue.xml)_
- Cell result: ☐ PASS  ☐ FAIL  ☐ N/A — Notes: ______

## Cell 2 · clock-analogue | theme=1 | left/top

Options: `themeId=1, alignmentH=left, alignmentV=top`

- [ ] **2.1 · EXPECTED** The widget occupies the intended area (512x560 px) below the caption, without overlapping adjacent cells or letting content spill outside its borders _(layout.json (region geometry) + acceptance criterion)_
- [ ] **2.2 · EXPECTED** Analogue clock: the hands show the player's system time and move _(option value)_
- [ ] **2.3 · EXPECTED** Theme Light _(clock-analogue.xml)_
- [ ] **2.4 · EXPECTED** Clock face aligned left / top in the area (only noticeable if the area is larger than the face) _(clock-analogue.xml)_
- Cell result: ☐ PASS  ☐ FAIL  ☐ N/A — Notes: ______

## Cell 3 · clock-analogue | theme=1 | right/bottom

Options: `themeId=1, alignmentH=right, alignmentV=bottom`

- [ ] **3.1 · EXPECTED** The widget occupies the intended area (512x560 px) below the caption, without overlapping adjacent cells or letting content spill outside its borders _(layout.json (region geometry) + acceptance criterion)_
- [ ] **3.2 · EXPECTED** Analogue clock: the hands show the player's system time and move _(option value)_
- [ ] **3.3 · EXPECTED** Theme Light _(clock-analogue.xml)_
- [ ] **3.4 · EXPECTED** Clock face aligned right / bottom in the area (only noticeable if the area is larger than the face) _(clock-analogue.xml)_
- Cell result: ☐ PASS  ☐ FAIL  ☐ N/A — Notes: ______

## Cell 4 · clock-analogue | theme=2 | center/middle

Options: `themeId=2, alignmentH=center, alignmentV=middle`

- [ ] **4.1 · EXPECTED** The widget occupies the intended area (512x560 px) below the caption, without overlapping adjacent cells or letting content spill outside its borders _(layout.json (region geometry) + acceptance criterion)_
- [ ] **4.2 · EXPECTED** Analogue clock: the hands show the player's system time and move _(option value)_
- [ ] **4.3 · EXPECTED** Theme Dark _(clock-analogue.xml)_
- [ ] **4.4 · EXPECTED** Clock face aligned center / middle in the area (only noticeable if the area is larger than the face) _(clock-analogue.xml)_
- Cell result: ☐ PASS  ☐ FAIL  ☐ N/A — Notes: ______

## Cell 5 · clock-analogue | theme=2 | left/top

Options: `themeId=2, alignmentH=left, alignmentV=top`

- [ ] **5.1 · EXPECTED** The widget occupies the intended area (512x560 px) below the caption, without overlapping adjacent cells or letting content spill outside its borders _(layout.json (region geometry) + acceptance criterion)_
- [ ] **5.2 · EXPECTED** Analogue clock: the hands show the player's system time and move _(option value)_
- [ ] **5.3 · EXPECTED** Theme Dark _(clock-analogue.xml)_
- [ ] **5.4 · EXPECTED** Clock face aligned left / top in the area (only noticeable if the area is larger than the face) _(clock-analogue.xml)_
- Cell result: ☐ PASS  ☐ FAIL  ☐ N/A — Notes: ______

## Cell 6 · clock-analogue | theme=2 | right/bottom

Options: `themeId=2, alignmentH=right, alignmentV=bottom`

- [ ] **6.1 · EXPECTED** The widget occupies the intended area (512x560 px) below the caption, without overlapping adjacent cells or letting content spill outside its borders _(layout.json (region geometry) + acceptance criterion)_
- [ ] **6.2 · EXPECTED** Analogue clock: the hands show the player's system time and move _(option value)_
- [ ] **6.3 · EXPECTED** Theme Dark _(clock-analogue.xml)_
- [ ] **6.4 · EXPECTED** Clock face aligned right / bottom in the area (only noticeable if the area is larger than the face) _(clock-analogue.xml)_
- Cell result: ☐ PASS  ☐ FAIL  ☐ N/A — Notes: ______
