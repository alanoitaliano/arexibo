# rt_text_01_landscape - checklist

Family `text` · 1920x1080 landscape · 60 s cycle · 6 cells · generated for Xibo 4.5.0

**EXPECTED** = derived from options, definitions or 4.5.0 code (source in brackets) · **OBSERVE** = not determinable in advance: record what you see.

## Layout

- [ ] **L1 · EXPECTED** Importing the zip completes without errors and creates the layout 'rt_text_01_landscape' _(LayoutFactory::createFromZip)_
- [ ] **L2 · EXPECTED** Size 1920x1080 px, orientation landscape; if the resolution does not exist in the CMS it is created ('1920 x 1080') _(LayoutFactory::createFromZip (getByDimensions → create))_
- [ ] **L3 · OBSERVE** Record the layout status after import (valid / draft / with warnings); if draft, publish it _(not determinable)_
- [ ] **L4 · EXPECTED** The Layout Editor shows 12 regions (per cell: caption + widget) _(layout.json)_
- [ ] **L5 · EXPECTED** Assigned to a landscape display (1920x1080): the layout fills the screen with no bars or cropping; if the display is physically rotated, set the rotation on the player _(layout.json (width/height))_
- [ ] **L6 · EXPECTED** The layout lasts 60 s (longest widget duration) and then restarts _(layout.json (duration))_
- [ ] **L7 · OBSERVE** Record whether, when the cycle restarts, countdowns, marquees and animations restart from scratch with no leftovers _(not determinable)_
- [ ] **L8 · EXPECTED** No errors in the player log over at least 2 full cycles _(general criterion)_

## Cell 1 · text | base 40px left

Options: `text=<p style="text-align:left;"><span style="font-size:40px;col…`

- [ ] **1.1 · EXPECTED** The widget occupies the intended area (616x456 px) below the caption, without overlapping adjacent cells or letting content spill outside its borders _(layout.json (region geometry) + acceptance criterion)_
- [ ] **1.2 · EXPECTED** Visible text: «Rendering test 0123456789 àèìòù €» - size 40px, colour #111111, aligned left _(option value)_
- Cell result: ☐ PASS  ☐ FAIL  ☐ N/A — Notes: ______

## Cell 2 · text | center 56px bold

Options: `text=<p style="text-align:center;"><span style="font-size:56px;c…`

- [ ] **2.1 · EXPECTED** The widget occupies the intended area (616x456 px) below the caption, without overlapping adjacent cells or letting content spill outside its borders _(layout.json (region geometry) + acceptance criterion)_
- [ ] **2.2 · EXPECTED** Visible text: «Rendering test 0123456789 àèìòù €» - size 56px, colour #111111, aligned center, bold _(option value)_
- Cell result: ☐ PASS  ☐ FAIL  ☐ N/A — Notes: ______

## Cell 3 · text | right 28px italic underline

Options: `text=<p style="text-align:right;"><span style="font-size:28px;co…`

- [ ] **3.1 · EXPECTED** The widget occupies the intended area (616x456 px) below the caption, without overlapping adjacent cells or letting content spill outside its borders _(layout.json (region geometry) + acceptance criterion)_
- [ ] **3.2 · EXPECTED** Visible text: «Rendering test 0123456789 àèìòù €» - size 28px, colour #111111, aligned right, italic, underlined _(option value)_
- Cell result: ☐ PASS  ☐ FAIL  ☐ N/A — Notes: ______

## Cell 4 · text | white on #1565c0 (backgroundColor)

Options: `text=<p style="text-align:center;"><span style="font-size:44px;c…, backgroundColor=#1565c0`

- [ ] **4.1 · EXPECTED** The widget occupies the intended area (616x456 px) below the caption, without overlapping adjacent cells or letting content spill outside its borders _(layout.json (region geometry) + acceptance criterion)_
- [ ] **4.2 · EXPECTED** Visible text: «Rendering test 0123456789 àèìòù €» - size 44px, colour #ffffff, aligned center _(option value)_
- [ ] **4.3 · EXPECTED** Widget background #1565c0 _(option value)_
- Cell result: ☐ PASS  ☐ FAIL  ☐ N/A — Notes: ______

## Cell 5 · text | semi-transparent bg rgba

Options: `text=<p style="text-align:center;"><span style="font-size:44px;c…, backgroundColor=rgba(255,193,7,0.6)`

- [ ] **5.1 · EXPECTED** The widget occupies the intended area (616x456 px) below the caption, without overlapping adjacent cells or letting content spill outside its borders _(layout.json (region geometry) + acceptance criterion)_
- [ ] **5.2 · EXPECTED** Visible text: «Rendering test 0123456789 àèìòù €» - size 44px, colour #000000, aligned center _(option value)_
- [ ] **5.3 · EXPECTED** Widget background rgba(255,193,7,0.6) (translucent: the layout background #dfe3e8 shows through) _(option value)_
- Cell result: ☐ PASS  ☐ FAIL  ☐ N/A — Notes: ______

## Cell 6 · text | multi paragraph

Options: `text=<p style="text-align:left;"><span style="font-size:44px;col…`

- [ ] **6.1 · EXPECTED** The widget occupies the intended area (616x456 px) below the caption, without overlapping adjacent cells or letting content spill outside its borders _(layout.json (region geometry) + acceptance criterion)_
- [ ] **6.2 · EXPECTED** Visible text: «Line one Line two àèìòù € Line three Line four» - size 44px, colour #111111, aligned left, 4 paragraphs on separate lines _(option value)_
- Cell result: ☐ PASS  ☐ FAIL  ☐ N/A — Notes: ______
