# rt_canvas-text_03_portrait - checklist

Family `canvas-text` · 1080x1920 portrait · 60 s cycle · 6 cells · generated for Xibo 4.5.0

**EXPECTED** = derived from options, definitions or 4.5.0 code (source in brackets) · **OBSERVE** = not determinable in advance: record what you see.

## Layout

- [ ] **L1 · EXPECTED** Importing the zip completes without errors and creates the layout 'rt_canvas-text_03_portrait' _(LayoutFactory::createFromZip)_
- [ ] **L2 · EXPECTED** Size 1080x1920 px, orientation portrait; if the resolution does not exist in the CMS it is created ('1080 x 1920') _(LayoutFactory::createFromZip (getByDimensions → create))_
- [ ] **L3 · OBSERVE** Record the layout status after import (valid / draft / with warnings); if draft, publish it _(not determinable)_
- [ ] **L4 · EXPECTED** The Layout Editor shows 1 canvas region with 18 elements (per cell: box, caption, element under test) _(layout.json)_
- [ ] **L5 · EXPECTED** Assigned to a portrait display (1080x1920): the layout fills the screen with no bars or cropping; if the display is physically rotated, set the rotation on the player _(layout.json (width/height))_
- [ ] **L6 · EXPECTED** The layout lasts 60 s (longest widget duration) and then restarts _(layout.json (duration))_
- [ ] **L7 · OBSERVE** Record whether, when the cycle restarts, countdowns, marquees and animations restart from scratch with no leftovers _(not determinable)_
- [ ] **L8 · EXPECTED** No errors in the player log over at least 2 full cycles _(general criterion)_

## Cell 1 · element:text | justify=1 (long text)

Options: `fontSize=28, justify=1`

- [ ] **1.1 · EXPECTED** The element stays inside its own box (488x548 px) below the caption, without spilling outside the area _(layout.json (element geometry) + acceptance criterion)_
- [ ] **1.2 · EXPECTED** Text: «Long canvas text that must wrap or shrink depending on the …» _(option value)_
- [ ] **1.3 · EXPECTED** Size 28px _(option value)_
- [ ] **1.4 · EXPECTED** Justified text (aligned to both margins, last line excluded) _(standard CSS)_
- Cell result: ☐ PASS  ☐ FAIL  ☐ N/A — Notes: ______

## Cell 2 · element:text | lineHeight 2.0

Options: `fontSize=28, lineHeight=2.0`

- [ ] **2.1 · EXPECTED** The element stays inside its own box (488x548 px) below the caption, without spilling outside the area _(layout.json (element geometry) + acceptance criterion)_
- [ ] **2.2 · EXPECTED** Text: «Long canvas text that must wrap or shrink depending on the …» _(option value)_
- [ ] **2.3 · EXPECTED** Size 28px _(option value)_
- [ ] **2.4 · EXPECTED** Line height 2.0 _(option value)_
- Cell result: ☐ PASS  ☐ FAIL  ☐ N/A — Notes: ______

## Cell 3 · element:text | showOverflow=0 (long text)

Options: `showOverflow=0`

- [ ] **3.1 · EXPECTED** The element stays inside its own box (488x548 px) below the caption, without spilling outside the area _(layout.json (element geometry) + acceptance criterion)_
- [ ] **3.2 · EXPECTED** Text: «Long canvas text that must wrap or shrink depending on the …» _(option value)_
- [ ] **3.3 · EXPECTED** Text exceeding the element is hidden (does not go past the edges) _(global-elements.xml (hbs: overflow))_
- Cell result: ☐ PASS  ☐ FAIL  ☐ N/A — Notes: ______

## Cell 4 · element:date_advanced | date_advanced as shipped (dateFormat 'd/m/Y H:i:s')

Options: `(predefinite)`

- [ ] **4.1 · EXPECTED** The element stays inside its own box (488x548 px) below the caption, without spilling outside the area _(layout.json (element geometry) + acceptance criterion)_
- [ ] **4.2 · OBSERVE** The shipped default 'd/m/Y H:i:s' is PHP syntax, but the renderer uses moment.format(): record the text shown (likely not a readable date) _(global-elements.xml (date_advanced: currentDate.format(dateFormat)))_
- Cell result: ☐ PASS  ☐ FAIL  ☐ N/A — Notes: ______

## Cell 5 · element:date_advanced | date_advanced 'dddd D MMMM YYYY' lang=it (current date)

Options: `dateFormat=dddd D MMMM YYYY, lang=it, fontSize=32`

- [ ] **5.1 · EXPECTED** The element stays inside its own box (488x548 px) below the caption, without spilling outside the area _(layout.json (element geometry) + acceptance criterion)_
- [ ] **5.2 · EXPECTED** Size 32px _(option value)_
- [ ] **5.3 · EXPECTED** System date with weekday and month names in Italian (e.g. 'domenica 4 ottobre 2026') _(moment.js)_
- Cell result: ☐ PASS  ☐ FAIL  ☐ N/A — Notes: ______

## Cell 6 · element:date_advanced | date_advanced 'HH:mm' 80px (current time)

Options: `dateFormat=HH:mm, fontSize=80`

- [ ] **6.1 · EXPECTED** The element stays inside its own box (488x548 px) below the caption, without spilling outside the area _(layout.json (element geometry) + acceptance criterion)_
- [ ] **6.2 · EXPECTED** Size 80px _(option value)_
- [ ] **6.3 · EXPECTED** System time (24h) as HH:mm, advancing when the minute changes _(moment.js)_
- Cell result: ☐ PASS  ☐ FAIL  ☐ N/A — Notes: ______
