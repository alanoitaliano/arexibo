# rt_canvas-text_04_landscape - checklist

Family `canvas-text` · 1920x1080 landscape · 60 s cycle · 6 cells · generated for Xibo 4.5.0

**EXPECTED** = derived from options, definitions or 4.5.0 code (source in brackets) · **OBSERVE** = not determinable in advance: record what you see.

## Layout

- [ ] **L1 · EXPECTED** Importing the zip completes without errors and creates the layout 'rt_canvas-text_04_landscape' _(LayoutFactory::createFromZip)_
- [ ] **L2 · EXPECTED** Size 1920x1080 px, orientation landscape; if the resolution does not exist in the CMS it is created ('1920 x 1080') _(LayoutFactory::createFromZip (getByDimensions → create))_
- [ ] **L3 · OBSERVE** Record the layout status after import (valid / draft / with warnings); if draft, publish it _(not determinable)_
- [ ] **L4 · EXPECTED** The Layout Editor shows 1 canvas region with 18 elements (per cell: box, caption, element under test) _(layout.json)_
- [ ] **L5 · EXPECTED** Assigned to a landscape display (1920x1080): the layout fills the screen with no bars or cropping; if the display is physically rotated, set the rotation on the player _(layout.json (width/height))_
- [ ] **L6 · EXPECTED** The layout lasts 60 s (longest widget duration) and then restarts _(layout.json (duration))_
- [ ] **L7 · OBSERVE** Record whether, when the cycle restarts, countdowns, marquees and animations restart from scratch with no leftovers _(not determinable)_
- [ ] **L8 · EXPECTED** No errors in the player log over at least 2 full cycles _(general criterion)_

## Cell 1 · element:date_advanced | date_advanced offset=+120 'HH:mm:ss'

Options: `offset=120, dateFormat=HH:mm:ss`

- [ ] **1.1 · EXPECTED** The element stays inside its own box (592x444 px) below the caption, without spilling outside the area _(layout.json (element geometry) + acceptance criterion)_
- [ ] **1.2 · EXPECTED** System time +120 min (2 h ahead), with seconds advancing every second _(global-elements.xml (offset in minutes))_
- Cell result: ☐ PASS  ☐ FAIL  ☐ N/A — Notes: ______

## Cell 2 · element:date_advanced | date_advanced fixed date, 'DD/MM/YYYY HH:mm'

Options: `currentDate=0, date=2026-12-25 10:30:00, dateFormat=DD/MM/YYYY HH:mm`

- [ ] **2.1 · EXPECTED** The element stays inside its own box (592x444 px) below the caption, without spilling outside the area _(layout.json (element geometry) + acceptance criterion)_
- [ ] **2.2 · EXPECTED** Shows exactly '25/12/2026 10:30' and never changes _(currentDate=0, date=2026-12-25 10:30:00)_
- Cell result: ☐ PASS  ☐ FAIL  ☐ N/A — Notes: ______

## Cell 3 · element:date_advanced | date_advanced fixed date, 'dddd D MMMM YYYY' lang=it

Options: `currentDate=0, date=2026-12-25 10:30:00, dateFormat=dddd D MMMM YYYY, lang=it, fontSize=32`

- [ ] **3.1 · EXPECTED** The element stays inside its own box (592x444 px) below the caption, without spilling outside the area _(layout.json (element geometry) + acceptance criterion)_
- [ ] **3.2 · EXPECTED** Size 32px _(option value)_
- [ ] **3.3 · EXPECTED** Shows exactly 'venerdì 25 dicembre 2026' _(moment.js (locale it))_
- Cell result: ☐ PASS  ☐ FAIL  ☐ N/A — Notes: ______

## Cell 4 · element:date_advanced | date_advanced fixed date, 'dddd D MMMM YYYY' lang=de

Options: `currentDate=0, date=2026-12-25 10:30:00, dateFormat=dddd D MMMM YYYY, lang=de, fontSize=32`

- [ ] **4.1 · EXPECTED** The element stays inside its own box (592x444 px) below the caption, without spilling outside the area _(layout.json (element geometry) + acceptance criterion)_
- [ ] **4.2 · EXPECTED** Size 32px _(option value)_
- [ ] **4.3 · EXPECTED** Shows exactly 'Freitag 25 Dezember 2026' _(moment.js (locale de))_
- Cell result: ☐ PASS  ☐ FAIL  ☐ N/A — Notes: ______

## Cell 5 · element:date | date (static) fixed date, 'DD/MM/YYYY HH:mm:ss'

Options: `date=2026-12-25 10:30:00, dateFormat=DD/MM/YYYY HH:mm:ss`

- [ ] **5.1 · EXPECTED** The element stays inside its own box (592x444 px) below the caption, without spilling outside the area _(layout.json (element geometry) + acceptance criterion)_
- [ ] **5.2 · EXPECTED** Shows exactly '25/12/2026 10:30:00' and never changes _(global-elements.xml (date))_
- Cell result: ☐ PASS  ☐ FAIL  ☐ N/A — Notes: ______

## Cell 6 · element:date | date (static) empty date

Options: `(predefinite)`

- [ ] **6.1 · EXPECTED** The element stays inside its own box (592x444 px) below the caption, without spilling outside the area _(layout.json (element geometry) + acceptance criterion)_
- [ ] **6.2 · EXPECTED** Shows nothing: with an empty date the renderer writes an empty string _(global-elements.xml (date: String(dateValue).length === 0 → html('')))_
- Cell result: ☐ PASS  ☐ FAIL  ☐ N/A — Notes: ______
