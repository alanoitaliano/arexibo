# rt_clock-flip_01_portrait - checklist

Family `clock-flip` · 1080x1920 portrait · 60 s cycle · 6 cells · generated for Xibo 4.5.0

**EXPECTED** = derived from options, definitions or 4.5.0 code (source in brackets) · **OBSERVE** = not determinable in advance: record what you see.

## Layout

- [ ] **L1 · EXPECTED** Importing the zip completes without errors and creates the layout 'rt_clock-flip_01_portrait' _(LayoutFactory::createFromZip)_
- [ ] **L2 · EXPECTED** Size 1080x1920 px, orientation portrait; if the resolution does not exist in the CMS it is created ('1080 x 1920') _(LayoutFactory::createFromZip (getByDimensions → create))_
- [ ] **L3 · OBSERVE** Record the layout status after import (valid / draft / with warnings); if draft, publish it _(not determinable)_
- [ ] **L4 · EXPECTED** The Layout Editor shows 12 regions (per cell: caption + widget) _(layout.json)_
- [ ] **L5 · EXPECTED** Assigned to a portrait display (1080x1920): the layout fills the screen with no bars or cropping; if the display is physically rotated, set the rotation on the player _(layout.json (width/height))_
- [ ] **L6 · EXPECTED** The layout lasts 60 s (longest widget duration) and then restarts _(layout.json (duration))_
- [ ] **L7 · OBSERVE** Record whether, when the cycle restarts, countdowns, marquees and animations restart from scratch with no leftovers _(not determinable)_
- [ ] **L8 · EXPECTED** No errors in the player log over at least 2 full cycles _(general criterion)_

## Cell 1 · clock-flip | TwelveHourClock showSeconds=0

Options: `clockFace=TwelveHourClock, showSeconds=0`

- [ ] **1.1 · EXPECTED** The widget occupies the intended area (512x560 px) below the caption, without overlapping adjacent cells or letting content spill outside its borders _(layout.json (region geometry) + acceptance criterion)_
- [ ] **1.2 · EXPECTED** 12h clock (hours 1-12) showing system time _(clock-flip.xml)_
- [ ] **1.3 · OBSERVE** Record whether an AM/PM indicator appears _(clock-flip.xml (ampmColor option))_
- [ ] **1.4 · EXPECTED** Hours and minutes only, no seconds _(clock-flip.xml)_
- Cell result: ☐ PASS  ☐ FAIL  ☐ N/A — Notes: ______

## Cell 2 · clock-flip | TwelveHourClock showSeconds=1

Options: `clockFace=TwelveHourClock, showSeconds=1`

- [ ] **2.1 · EXPECTED** The widget occupies the intended area (512x560 px) below the caption, without overlapping adjacent cells or letting content spill outside its borders _(layout.json (region geometry) + acceptance criterion)_
- [ ] **2.2 · EXPECTED** 12h clock (hours 1-12) showing system time _(clock-flip.xml)_
- [ ] **2.3 · OBSERVE** Record whether an AM/PM indicator appears _(clock-flip.xml (ampmColor option))_
- [ ] **2.4 · EXPECTED** Seconds are shown _(clock-flip.xml)_
- Cell result: ☐ PASS  ☐ FAIL  ☐ N/A — Notes: ______

## Cell 3 · clock-flip | TwentyFourHourClock showSeconds=0

Options: `clockFace=TwentyFourHourClock, showSeconds=0`

- [ ] **3.1 · EXPECTED** The widget occupies the intended area (512x560 px) below the caption, without overlapping adjacent cells or letting content spill outside its borders _(layout.json (region geometry) + acceptance criterion)_
- [ ] **3.2 · EXPECTED** 24h clock (hours 00-23) showing system time _(clock-flip.xml)_
- [ ] **3.3 · EXPECTED** Hours and minutes only, no seconds _(clock-flip.xml)_
- Cell result: ☐ PASS  ☐ FAIL  ☐ N/A — Notes: ______

## Cell 4 · clock-flip | TwentyFourHourClock showSeconds=1

Options: `clockFace=TwentyFourHourClock, showSeconds=1`

- [ ] **4.1 · EXPECTED** The widget occupies the intended area (512x560 px) below the caption, without overlapping adjacent cells or letting content spill outside its borders _(layout.json (region geometry) + acceptance criterion)_
- [ ] **4.2 · EXPECTED** 24h clock (hours 00-23) showing system time _(clock-flip.xml)_
- [ ] **4.3 · EXPECTED** Seconds are shown _(clock-flip.xml)_
- Cell result: ☐ PASS  ☐ FAIL  ☐ N/A — Notes: ______

## Cell 5 · clock-flip | HourlyCounter

Options: `clockFace=HourlyCounter`

- [ ] **5.1 · EXPECTED** The widget occupies the intended area (512x560 px) below the caption, without overlapping adjacent cells or letting content spill outside its borders _(layout.json (region geometry) + acceptance criterion)_
- [ ] **5.2 · OBSERVE** Counter 'HourlyCounter' (not a clock): record the initial value and counting direction; for counters 'offset' is the start date/time (Y-m-d H:i:s), not set here _(clock-flip.xml (offset help))_
- Cell result: ☐ PASS  ☐ FAIL  ☐ N/A — Notes: ______

## Cell 6 · clock-flip | MinuteCounter

Options: `clockFace=MinuteCounter`

- [ ] **6.1 · EXPECTED** The widget occupies the intended area (512x560 px) below the caption, without overlapping adjacent cells or letting content spill outside its borders _(layout.json (region geometry) + acceptance criterion)_
- [ ] **6.2 · OBSERVE** Counter 'MinuteCounter' (not a clock): record the initial value and counting direction; for counters 'offset' is the start date/time (Y-m-d H:i:s), not set here _(clock-flip.xml (offset help))_
- Cell result: ☐ PASS  ☐ FAIL  ☐ N/A — Notes: ______
