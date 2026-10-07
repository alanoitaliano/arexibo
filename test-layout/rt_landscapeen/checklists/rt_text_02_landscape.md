# rt_text_02_landscape - checklist

Family `text` · 1920x1080 landscape · 60 s cycle · 6 cells · generated for Xibo 4.5.0

**EXPECTED** = derived from options, definitions or 4.5.0 code (source in brackets) · **OBSERVE** = not determinable in advance: record what you see.

## Layout

- [ ] **L1 · EXPECTED** Importing the zip completes without errors and creates the layout 'rt_text_02_landscape' _(LayoutFactory::createFromZip)_
- [ ] **L2 · EXPECTED** Size 1920x1080 px, orientation landscape; if the resolution does not exist in the CMS it is created ('1920 x 1080') _(LayoutFactory::createFromZip (getByDimensions → create))_
- [ ] **L3 · OBSERVE** Record the layout status after import (valid / draft / with warnings); if draft, publish it _(not determinable)_
- [ ] **L4 · EXPECTED** The Layout Editor shows 12 regions (per cell: caption + widget) _(layout.json)_
- [ ] **L5 · EXPECTED** Assigned to a landscape display (1920x1080): the layout fills the screen with no bars or cropping; if the display is physically rotated, set the rotation on the player _(layout.json (width/height))_
- [ ] **L6 · EXPECTED** The layout lasts 60 s (longest widget duration) and then restarts _(layout.json (duration))_
- [ ] **L7 · OBSERVE** Record whether, when the cycle restarts, countdowns, marquees and animations restart from scratch with no leftovers _(not determinable)_
- [ ] **L8 · EXPECTED** No errors in the player log over at least 2 full cycles _(general criterion)_

## Cell 1 · text | effect=marqueeLeft speed=3

Options: `text=<p style="text-align:left;"><span style="font-size:40px;col…, effect=marqueeLeft, speed=3`

- [ ] **1.1 · EXPECTED** The widget occupies the intended area (616x456 px) below the caption, without overlapping adjacent cells or letting content spill outside its borders _(layout.json (region geometry) + acceptance criterion)_
- [ ] **1.2 · EXPECTED** Visible text: «Long text to exercise marquee scrolling: lorem ipsum dolor …» - size 40px, colour #111111, aligned left _(option value)_
- [ ] **1.3 · EXPECTED** Content scrolls from right to left continuously (marquee, speed 3; 1 = normal) _(text.xml (speed help))_
- [ ] **1.4 · OBSERVE** Record whether the scrolling is smooth (no stutter) and whether it restarts without gaps or jumps when the cycle restarts _(not determinable)_
- Cell result: ☐ PASS  ☐ FAIL  ☐ N/A — Notes: ______

## Cell 2 · text | effect=marqueeRight speed=3

Options: `text=<p style="text-align:left;"><span style="font-size:40px;col…, effect=marqueeRight, speed=3`

- [ ] **2.1 · EXPECTED** The widget occupies the intended area (616x456 px) below the caption, without overlapping adjacent cells or letting content spill outside its borders _(layout.json (region geometry) + acceptance criterion)_
- [ ] **2.2 · EXPECTED** Visible text: «Long text to exercise marquee scrolling: lorem ipsum dolor …» - size 40px, colour #111111, aligned left _(option value)_
- [ ] **2.3 · EXPECTED** Content scrolls from left to right continuously (marquee, speed 3; 1 = normal) _(text.xml (speed help))_
- [ ] **2.4 · OBSERVE** Record whether the scrolling is smooth (no stutter) and whether it restarts without gaps or jumps when the cycle restarts _(not determinable)_
- Cell result: ☐ PASS  ☐ FAIL  ☐ N/A — Notes: ______

## Cell 3 · text | effect=marqueeUp speed=2

Options: `text=<p style="text-align:left;"><span style="font-size:44px;col…, effect=marqueeUp, speed=2`

- [ ] **3.1 · EXPECTED** The widget occupies the intended area (616x456 px) below the caption, without overlapping adjacent cells or letting content spill outside its borders _(layout.json (region geometry) + acceptance criterion)_
- [ ] **3.2 · EXPECTED** Visible text: «Line one Line two àèìòù € Line three Line four» - size 44px, colour #111111, aligned left, 4 paragraphs on separate lines _(option value)_
- [ ] **3.3 · EXPECTED** Content scrolls from bottom to top continuously (marquee, speed 2; 1 = normal) _(text.xml (speed help))_
- [ ] **3.4 · OBSERVE** Record whether the scrolling is smooth (no stutter) and whether it restarts without gaps or jumps when the cycle restarts _(not determinable)_
- Cell result: ☐ PASS  ☐ FAIL  ☐ N/A — Notes: ______

## Cell 4 · text | effect=marqueeDown speed=2

Options: `text=<p style="text-align:left;"><span style="font-size:44px;col…, effect=marqueeDown, speed=2`

- [ ] **4.1 · EXPECTED** The widget occupies the intended area (616x456 px) below the caption, without overlapping adjacent cells or letting content spill outside its borders _(layout.json (region geometry) + acceptance criterion)_
- [ ] **4.2 · EXPECTED** Visible text: «Line one Line two àèìòù € Line three Line four» - size 44px, colour #111111, aligned left, 4 paragraphs on separate lines _(option value)_
- [ ] **4.3 · EXPECTED** Content scrolls from top to bottom continuously (marquee, speed 2; 1 = normal) _(text.xml (speed help))_
- [ ] **4.4 · OBSERVE** Record whether the scrolling is smooth (no stutter) and whether it restarts without gaps or jumps when the cycle restarts _(not determinable)_
- Cell result: ☐ PASS  ☐ FAIL  ☐ N/A — Notes: ______

## Cell 5 · text | effect=none (explicit)

Options: `text=<p style="text-align:left;"><span style="font-size:44px;col…, effect=none`

- [ ] **5.1 · EXPECTED** The widget occupies the intended area (616x456 px) below the caption, without overlapping adjacent cells or letting content spill outside its borders _(layout.json (region geometry) + acceptance criterion)_
- [ ] **5.2 · EXPECTED** Visible text: «Line one Line two àèìòù € Line three Line four» - size 44px, colour #111111, aligned left, 4 paragraphs on separate lines _(option value)_
- [ ] **5.3 · EXPECTED** No movement: static content _(option value)_
- Cell result: ☐ PASS  ☐ FAIL  ☐ N/A — Notes: ______

## Cell 6 · text | effect=fade (paged, 1000 ms)

Options: `text=<p style="text-align:left;"><span style="font-size:44px;col…, effect=fade, speed=1000`

- [ ] **6.1 · EXPECTED** The widget occupies the intended area (616x456 px) below the caption, without overlapping adjacent cells or letting content spill outside its borders _(layout.json (region geometry) + acceptance criterion)_
- [ ] **6.2 · EXPECTED** Visible text: «Line one Line two àèìòù € Line three Line four» - size 44px, colour #111111, aligned left, 4 paragraphs on separate lines _(option value)_
- [ ] **6.3 · OBSERVE** Effect 'fade' (transition between items, 1000 ms): with a single block of content it may produce no visible animation; record what happens _(text.xml (effectSelector, 'paged' group))_
- Cell result: ☐ PASS  ☐ FAIL  ☐ N/A — Notes: ______
