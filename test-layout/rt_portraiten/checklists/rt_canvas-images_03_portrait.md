# rt_canvas-images_03_portrait - checklist

Family `canvas-images` · 1080x1920 portrait · 60 s cycle · 3 cells · generated for Xibo 4.5.0

**EXPECTED** = derived from options, definitions or 4.5.0 code (source in brackets) · **OBSERVE** = not determinable in advance: record what you see.

## Layout

- [ ] **L1 · EXPECTED** Importing the zip completes without errors and creates the layout 'rt_canvas-images_03_portrait' _(LayoutFactory::createFromZip)_
- [ ] **L2 · EXPECTED** Size 1080x1920 px, orientation portrait; if the resolution does not exist in the CMS it is created ('1080 x 1920') _(LayoutFactory::createFromZip (getByDimensions → create))_
- [ ] **L3 · OBSERVE** Record the layout status after import (valid / draft / with warnings); if draft, publish it _(not determinable)_
- [ ] **L4 · EXPECTED** The Layout Editor shows 1 canvas region with 9 elements (per cell: box, caption, element under test) _(layout.json)_
- [ ] **L5 · EXPECTED** The images rt_wide_2x1.png appear in the Library with tag 'imported' (if already present with the same name they are reused) _(LayoutFactory::createFromZip (assignTag 'imported'))_
- [ ] **L6 · EXPECTED** Assigned to a portrait display (1080x1920): the layout fills the screen with no bars or cropping; if the display is physically rotated, set the rotation on the player _(layout.json (width/height))_
- [ ] **L7 · EXPECTED** The layout lasts 60 s (longest widget duration) and then restarts _(layout.json (duration))_
- [ ] **L8 · OBSERVE** Record whether, when the cycle restarts, countdowns, marquees and animations restart from scratch with no leftovers _(not determinable)_
- [ ] **L9 · EXPECTED** No errors in the player log over at least 2 full cycles _(general criterion)_

## Cell 1 · element:global_library_image | wide roundBorder r=60

Options: `roundBorder=1, borderRadius=60`

- [ ] **1.1 · EXPECTED** The element stays inside its own box (488x548 px) below the caption, without spilling outside the area _(layout.json (element geometry) + acceptance criterion)_
- [ ] **1.2 · EXPECTED** Shows the 800x400 px test image (red/green/blue/yellow corners, central circle) _(library file)_
- [ ] **1.3 · EXPECTED** Whole image visible (4 coloured corners) with aspect ratio preserved; empty bands on the free side (image 2.00:1, area 0.89:1) _(CSS object-fit: contain)_
- [ ] **1.4 · EXPECTED** Rounded corners with 60px radius _(option value)_
- Cell result: ☐ PASS  ☐ FAIL  ☐ N/A — Notes: ______

## Cell 2 · element:global_library_image | wide imageShadow

Options: `imageShadow=1, shadowX=8, shadowY=8, shadowBlur=12`

- [ ] **2.1 · EXPECTED** The element stays inside its own box (488x548 px) below the caption, without spilling outside the area _(layout.json (element geometry) + acceptance criterion)_
- [ ] **2.2 · EXPECTED** Shows the 800x400 px test image (red/green/blue/yellow corners, central circle) _(library file)_
- [ ] **2.3 · EXPECTED** Whole image visible (4 coloured corners) with aspect ratio preserved; empty bands on the free side (image 2.00:1, area 0.89:1) _(CSS object-fit: contain)_
- [ ] **2.4 · EXPECTED** Image shadow offset (8,8) blur 12 _(option value)_
- Cell result: ☐ PASS  ☐ FAIL  ☐ N/A — Notes: ______

## Cell 3 · element:global_library_image | wide opacity 40

Options: `opacity=40`

- [ ] **3.1 · EXPECTED** The element stays inside its own box (488x548 px) below the caption, without spilling outside the area _(layout.json (element geometry) + acceptance criterion)_
- [ ] **3.2 · EXPECTED** Shows the 800x400 px test image (red/green/blue/yellow corners, central circle) _(library file)_
- [ ] **3.3 · EXPECTED** Whole image visible (4 coloured corners) with aspect ratio preserved; empty bands on the free side (image 2.00:1, area 0.89:1) _(CSS object-fit: contain)_
- [ ] **3.4 · EXPECTED** Opacity 40%: the white background of the box shows through the image _(global-elements.xml (opacity help))_
- Cell result: ☐ PASS  ☐ FAIL  ☐ N/A — Notes: ______
