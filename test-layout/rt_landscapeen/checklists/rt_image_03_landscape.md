# rt_image_03_landscape - checklist

Family `image` · 1920x1080 landscape · 60 s cycle · 3 cells · generated for Xibo 4.5.0

**EXPECTED** = derived from options, definitions or 4.5.0 code (source in brackets) · **OBSERVE** = not determinable in advance: record what you see.

## Layout

- [ ] **L1 · EXPECTED** Importing the zip completes without errors and creates the layout 'rt_image_03_landscape' _(LayoutFactory::createFromZip)_
- [ ] **L2 · EXPECTED** Size 1920x1080 px, orientation landscape; if the resolution does not exist in the CMS it is created ('1920 x 1080') _(LayoutFactory::createFromZip (getByDimensions → create))_
- [ ] **L3 · OBSERVE** Record the layout status after import (valid / draft / with warnings); if draft, publish it _(not determinable)_
- [ ] **L4 · EXPECTED** The Layout Editor shows 6 regions (per cell: caption + widget) _(layout.json)_
- [ ] **L5 · EXPECTED** The images rt_square_1x1.png appear in the Library with tag 'imported' (if already present with the same name they are reused) _(LayoutFactory::createFromZip (assignTag 'imported'))_
- [ ] **L6 · EXPECTED** Assigned to a landscape display (1920x1080): the layout fills the screen with no bars or cropping; if the display is physically rotated, set the rotation on the player _(layout.json (width/height))_
- [ ] **L7 · EXPECTED** The layout lasts 60 s (longest widget duration) and then restarts _(layout.json (duration))_
- [ ] **L8 · OBSERVE** Record whether, when the cycle restarts, countdowns, marquees and animations restart from scratch with no leftovers _(not determinable)_
- [ ] **L9 · EXPECTED** No errors in the player log over at least 2 full cycles _(general criterion)_

## Cell 1 · image | square 1:1 | center | center/middle

Options: `scaleType=center, alignId=center, valignId=middle, uri=rt_square_1x1.png`

- [ ] **1.1 · EXPECTED** The widget occupies the intended area (616x456 px) below the caption, without overlapping adjacent cells or letting content spill outside its borders _(layout.json (region geometry) + acceptance criterion)_
- [ ] **1.2 · EXPECTED** Shows the 512x512 px test image (ratio 1.00:1): red corner (top left), green (top right), blue (bottom left), yellow (bottom right), checkered border, central cross and circle _(library file)_
- [ ] **1.3 · EXPECTED** Aspect ratio preserved (the circle stays a circle) _(image.xml (preview: proportional=1, fit=0))_
- [ ] **1.4 · OBSERVE** Record whether the native 512x512 px image in the 616x456 px area is scaled down, shown at native size or cropped (which coloured corners are visible) _(not determinable from definitions)_
- [ ] **1.5 · EXPECTED** Horizontal alignment 'center', vertical 'middle' (only noticeable if the image does not fill the area) _(image.xml (alignId/valignId visible when scaleType=center))_
- Cell result: ☐ PASS  ☐ FAIL  ☐ N/A — Notes: ______

## Cell 2 · image | square 1:1 | stretch | center/middle

Options: `scaleType=stretch, alignId=center, valignId=middle, uri=rt_square_1x1.png`

- [ ] **2.1 · EXPECTED** The widget occupies the intended area (616x456 px) below the caption, without overlapping adjacent cells or letting content spill outside its borders _(layout.json (region geometry) + acceptance criterion)_
- [ ] **2.2 · EXPECTED** Shows the 512x512 px test image (ratio 1.00:1): red corner (top left), green (top right), blue (bottom left), yellow (bottom right), checkered border, central cross and circle _(library file)_
- [ ] **2.3 · EXPECTED** The image fills the whole 616x456 px area; aspect ratio not preserved (1.00:1 image in a 1.35:1 area: the central circle looks like an ellipse) _(image.xml (preview: proportional=0))_
- [ ] **2.4 · OBSERVE** alignId=center / valignId=middle are hidden in the UI when scaleType=stretch: record whether they affect the position _(image.xml (visibility))_
- Cell result: ☐ PASS  ☐ FAIL  ☐ N/A — Notes: ______

## Cell 3 · image | square 1:1 | fit | center/middle

Options: `scaleType=fit, alignId=center, valignId=middle, uri=rt_square_1x1.png`

- [ ] **3.1 · EXPECTED** The widget occupies the intended area (616x456 px) below the caption, without overlapping adjacent cells or letting content spill outside its borders _(layout.json (region geometry) + acceptance criterion)_
- [ ] **3.2 · EXPECTED** Shows the 512x512 px test image (ratio 1.00:1): red corner (top left), green (top right), blue (bottom left), yellow (bottom right), checkered border, central cross and circle _(library file)_
- [ ] **3.3 · EXPECTED** Whole image visible (all 4 coloured corners present) with aspect ratio preserved (the circle stays a circle); empty margins on the free side _(image.xml (preview: proportional=1, fit=1))_
- [ ] **3.4 · OBSERVE** alignId=center / valignId=middle are hidden in the UI when scaleType=fit: record whether they affect the position _(image.xml (visibility))_
- Cell result: ☐ PASS  ☐ FAIL  ☐ N/A — Notes: ______
