# rt_text_03_landscape - checklist

Family `text` · 1920x1080 landscape · 60 s cycle · 3 cells · generated for Xibo 4.5.0

**EXPECTED** = derived from options, definitions or 4.5.0 code (source in brackets) · **OBSERVE** = not determinable in advance: record what you see.

## Layout

- [ ] **L1 · EXPECTED** Importing the zip completes without errors and creates the layout 'rt_text_03_landscape' _(LayoutFactory::createFromZip)_
- [ ] **L2 · EXPECTED** Size 1920x1080 px, orientation landscape; if the resolution does not exist in the CMS it is created ('1920 x 1080') _(LayoutFactory::createFromZip (getByDimensions → create))_
- [ ] **L3 · OBSERVE** Record the layout status after import (valid / draft / with warnings); if draft, publish it _(not determinable)_
- [ ] **L4 · EXPECTED** The Layout Editor shows 6 regions (per cell: caption + widget) _(layout.json)_
- [ ] **L5 · EXPECTED** Assigned to a landscape display (1920x1080): the layout fills the screen with no bars or cropping; if the display is physically rotated, set the rotation on the player _(layout.json (width/height))_
- [ ] **L6 · EXPECTED** The layout lasts 60 s (longest widget duration) and then restarts _(layout.json (duration))_
- [ ] **L7 · OBSERVE** Record whether, when the cycle restarts, countdowns, marquees and animations restart from scratch with no leftovers _(not determinable)_
- [ ] **L8 · EXPECTED** No errors in the player log over at least 2 full cycles _(general criterion)_

## Cell 1 · text | effect=scrollVert (paged, 1000 ms)

Options: `text=<p style="text-align:left;"><span style="font-size:44px;col…, effect=scrollVert, speed=1000`

- [ ] **1.1 · EXPECTED** The widget occupies the intended area (616x456 px) below the caption, without overlapping adjacent cells or letting content spill outside its borders _(layout.json (region geometry) + acceptance criterion)_
- [ ] **1.2 · EXPECTED** Visible text: «Line one Line two àèìòù € Line three Line four» - size 44px, colour #111111, aligned left, 4 paragraphs on separate lines _(option value)_
- [ ] **1.3 · OBSERVE** Effect 'scrollVert' (transition between items, 1000 ms): with a single block of content it may produce no visible animation; record what happens _(text.xml (effectSelector, 'paged' group))_
- Cell result: ☐ PASS  ☐ FAIL  ☐ N/A — Notes: ______

## Cell 2 · text | custom styleSheet

Options: `text=<p style="text-align:left;"><span style="font-size:44px;col…, seeAdvancedFields=1, styleSheet=p{text-shadow:3px 3px 6px #888;letter-spacing:4px;}`

- [ ] **2.1 · EXPECTED** The widget occupies the intended area (616x456 px) below the caption, without overlapping adjacent cells or letting content spill outside its borders _(layout.json (region geometry) + acceptance criterion)_
- [ ] **2.2 · EXPECTED** Visible text: «Rendering test 0123456789 àèìòù €» - size 44px, colour #111111, aligned left _(option value)_
- [ ] **2.3 · EXPECTED** The text has a grey shadow (3px 3px, blur 6px, #888) and 4px letter spacing _(applied CSS (styleSheet))_
- Cell result: ☐ PASS  ☐ FAIL  ☐ N/A — Notes: ______

## Cell 3 · text | custom javaScript (turns red @0.5s)

Options: `text=<p style="text-align:left;"><span style="font-size:44px;col…, seeAdvancedFields=1, javaScript=setTimeout(function(){var e=document.querySelector('p span'…`

- [ ] **3.1 · EXPECTED** The widget occupies the intended area (616x456 px) below the caption, without overlapping adjacent cells or letting content spill outside its borders _(layout.json (region geometry) + acceptance criterion)_
- [ ] **3.2 · EXPECTED** Visible text: «Rendering test 0123456789 àèìòù €» - size 44px, colour #111111, aligned left _(option value)_
- [ ] **3.3 · EXPECTED** After about 0.5 s the text turns from black (#111111) to red (#c62828) _(applied JavaScript (javaScript))_
- [ ] **3.4 · OBSERVE** If the text stays black, record it: the selector 'p span' may not find the element in the widget DOM _(not determinable from definitions)_
- Cell result: ☐ PASS  ☐ FAIL  ☐ N/A — Notes: ______
