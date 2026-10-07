# rt_image_02_portrait - checklist

Family `image` · 1080x1920 portrait · 60 s cycle · 6 cells · generated for Xibo 4.5.0

**EXPECTED** = derived from options, definitions or 4.5.0 code (source in brackets) · **OBSERVE** = not determinable in advance: record what you see.

## Layout

- [ ] **L1 · EXPECTED** Importing the zip completes without errors and creates the layout 'rt_image_02_portrait' _(LayoutFactory::createFromZip)_
- [ ] **L2 · EXPECTED** Size 1080x1920 px, orientation portrait; if the resolution does not exist in the CMS it is created ('1080 x 1920') _(LayoutFactory::createFromZip (getByDimensions → create))_
- [ ] **L3 · OBSERVE** Record the layout status after import (valid / draft / with warnings); if draft, publish it _(not determinable)_
- [ ] **L4 · EXPECTED** The Layout Editor shows 12 regions (per cell: caption + widget) _(layout.json)_
- [ ] **L5 · EXPECTED** The images rt_wide_2x1.png, rt_tall_1x2.png appear in the Library with tag 'imported' (if already present with the same name they are reused) _(LayoutFactory::createFromZip (assignTag 'imported'))_
- [ ] **L6 · EXPECTED** Assigned to a portrait display (1080x1920): the layout fills the screen with no bars or cropping; if the display is physically rotated, set the rotation on the player _(layout.json (width/height))_
- [ ] **L7 · EXPECTED** The layout lasts 60 s (longest widget duration) and then restarts _(layout.json (duration))_
- [ ] **L8 · OBSERVE** Record whether, when the cycle restarts, countdowns, marquees and animations restart from scratch with no leftovers _(not determinable)_
- [ ] **L9 · EXPECTED** No errors in the player log over at least 2 full cycles _(general criterion)_

## Cell 1 · image | wide 2:1 | fit | center/middle

Options: `scaleType=fit, alignId=center, valignId=middle, uri=rt_wide_2x1.png`

- [ ] **1.1 · EXPECTED** The widget occupies the intended area (512x560 px) below the caption, without overlapping adjacent cells or letting content spill outside its borders _(layout.json (region geometry) + acceptance criterion)_
- [ ] **1.2 · EXPECTED** Shows the 800x400 px test image (ratio 2.00:1): red corner (top left), green (top right), blue (bottom left), yellow (bottom right), checkered border, central cross and circle _(library file)_
- [ ] **1.3 · EXPECTED** Whole image visible (all 4 coloured corners present) with aspect ratio preserved (the circle stays a circle); empty margins on the free side _(image.xml (preview: proportional=1, fit=1))_
- [ ] **1.4 · OBSERVE** alignId=center / valignId=middle are hidden in the UI when scaleType=fit: record whether they affect the position _(image.xml (visibility))_
- Cell result: ☐ PASS  ☐ FAIL  ☐ N/A — Notes: ______

## Cell 2 · image | wide 2:1 | fit | left/top

Options: `scaleType=fit, alignId=left, valignId=top, uri=rt_wide_2x1.png`

- [ ] **2.1 · EXPECTED** The widget occupies the intended area (512x560 px) below the caption, without overlapping adjacent cells or letting content spill outside its borders _(layout.json (region geometry) + acceptance criterion)_
- [ ] **2.2 · EXPECTED** Shows the 800x400 px test image (ratio 2.00:1): red corner (top left), green (top right), blue (bottom left), yellow (bottom right), checkered border, central cross and circle _(library file)_
- [ ] **2.3 · EXPECTED** Whole image visible (all 4 coloured corners present) with aspect ratio preserved (the circle stays a circle); empty margins on the free side _(image.xml (preview: proportional=1, fit=1))_
- [ ] **2.4 · OBSERVE** alignId=left / valignId=top are hidden in the UI when scaleType=fit: record whether they affect the position _(image.xml (visibility))_
- Cell result: ☐ PASS  ☐ FAIL  ☐ N/A — Notes: ______

## Cell 3 · image | wide 2:1 | fit | right/bottom

Options: `scaleType=fit, alignId=right, valignId=bottom, uri=rt_wide_2x1.png`

- [ ] **3.1 · EXPECTED** The widget occupies the intended area (512x560 px) below the caption, without overlapping adjacent cells or letting content spill outside its borders _(layout.json (region geometry) + acceptance criterion)_
- [ ] **3.2 · EXPECTED** Shows the 800x400 px test image (ratio 2.00:1): red corner (top left), green (top right), blue (bottom left), yellow (bottom right), checkered border, central cross and circle _(library file)_
- [ ] **3.3 · EXPECTED** Whole image visible (all 4 coloured corners present) with aspect ratio preserved (the circle stays a circle); empty margins on the free side _(image.xml (preview: proportional=1, fit=1))_
- [ ] **3.4 · OBSERVE** alignId=right / valignId=bottom are hidden in the UI when scaleType=fit: record whether they affect the position _(image.xml (visibility))_
- Cell result: ☐ PASS  ☐ FAIL  ☐ N/A — Notes: ______

## Cell 4 · image | tall 1:2 | center | center/middle

Options: `scaleType=center, alignId=center, valignId=middle, uri=rt_tall_1x2.png`

- [ ] **4.1 · EXPECTED** The widget occupies the intended area (512x560 px) below the caption, without overlapping adjacent cells or letting content spill outside its borders _(layout.json (region geometry) + acceptance criterion)_
- [ ] **4.2 · EXPECTED** Shows the 400x800 px test image (ratio 0.50:1): red corner (top left), green (top right), blue (bottom left), yellow (bottom right), checkered border, central cross and circle _(library file)_
- [ ] **4.3 · EXPECTED** Aspect ratio preserved (the circle stays a circle) _(image.xml (preview: proportional=1, fit=0))_
- [ ] **4.4 · OBSERVE** Record whether the native 400x800 px image in the 512x560 px area is scaled down, shown at native size or cropped (which coloured corners are visible) _(not determinable from definitions)_
- [ ] **4.5 · EXPECTED** Horizontal alignment 'center', vertical 'middle' (only noticeable if the image does not fill the area) _(image.xml (alignId/valignId visible when scaleType=center))_
- Cell result: ☐ PASS  ☐ FAIL  ☐ N/A — Notes: ______

## Cell 5 · image | tall 1:2 | stretch | center/middle

Options: `scaleType=stretch, alignId=center, valignId=middle, uri=rt_tall_1x2.png`

- [ ] **5.1 · EXPECTED** The widget occupies the intended area (512x560 px) below the caption, without overlapping adjacent cells or letting content spill outside its borders _(layout.json (region geometry) + acceptance criterion)_
- [ ] **5.2 · EXPECTED** Shows the 400x800 px test image (ratio 0.50:1): red corner (top left), green (top right), blue (bottom left), yellow (bottom right), checkered border, central cross and circle _(library file)_
- [ ] **5.3 · EXPECTED** The image fills the whole 512x560 px area; aspect ratio not preserved (0.50:1 image in a 0.91:1 area: the central circle looks like an ellipse) _(image.xml (preview: proportional=0))_
- [ ] **5.4 · OBSERVE** alignId=center / valignId=middle are hidden in the UI when scaleType=stretch: record whether they affect the position _(image.xml (visibility))_
- Cell result: ☐ PASS  ☐ FAIL  ☐ N/A — Notes: ______

## Cell 6 · image | tall 1:2 | fit | center/middle

Options: `scaleType=fit, alignId=center, valignId=middle, uri=rt_tall_1x2.png`

- [ ] **6.1 · EXPECTED** The widget occupies the intended area (512x560 px) below the caption, without overlapping adjacent cells or letting content spill outside its borders _(layout.json (region geometry) + acceptance criterion)_
- [ ] **6.2 · EXPECTED** Shows the 400x800 px test image (ratio 0.50:1): red corner (top left), green (top right), blue (bottom left), yellow (bottom right), checkered border, central cross and circle _(library file)_
- [ ] **6.3 · EXPECTED** Whole image visible (all 4 coloured corners present) with aspect ratio preserved (the circle stays a circle); empty margins on the free side _(image.xml (preview: proportional=1, fit=1))_
- [ ] **6.4 · OBSERVE** alignId=center / valignId=middle are hidden in the UI when scaleType=fit: record whether they affect the position _(image.xml (visibility))_
- Cell result: ☐ PASS  ☐ FAIL  ☐ N/A — Notes: ______
