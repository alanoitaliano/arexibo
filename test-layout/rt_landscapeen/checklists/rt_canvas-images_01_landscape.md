# rt_canvas-images_01_landscape - checklist

Family `canvas-images` · 1920x1080 landscape · 60 s cycle · 6 cells · generated for Xibo 4.5.0

**EXPECTED** = derived from options, definitions or 4.5.0 code (source in brackets) · **OBSERVE** = not determinable in advance: record what you see.

## Layout

- [ ] **L1 · EXPECTED** Importing the zip completes without errors and creates the layout 'rt_canvas-images_01_landscape' _(LayoutFactory::createFromZip)_
- [ ] **L2 · EXPECTED** Size 1920x1080 px, orientation landscape; if the resolution does not exist in the CMS it is created ('1920 x 1080') _(LayoutFactory::createFromZip (getByDimensions → create))_
- [ ] **L3 · OBSERVE** Record the layout status after import (valid / draft / with warnings); if draft, publish it _(not determinable)_
- [ ] **L4 · EXPECTED** The Layout Editor shows 1 canvas region with 18 elements (per cell: box, caption, element under test) _(layout.json)_
- [ ] **L5 · EXPECTED** The images rt_wide_2x1.png, rt_tall_1x2.png appear in the Library with tag 'imported' (if already present with the same name they are reused) _(LayoutFactory::createFromZip (assignTag 'imported'))_
- [ ] **L6 · EXPECTED** Assigned to a landscape display (1920x1080): the layout fills the screen with no bars or cropping; if the display is physically rotated, set the rotation on the player _(layout.json (width/height))_
- [ ] **L7 · EXPECTED** The layout lasts 60 s (longest widget duration) and then restarts _(layout.json (duration))_
- [ ] **L8 · OBSERVE** Record whether, when the cycle restarts, countdowns, marquees and animations restart from scratch with no leftovers _(not determinable)_
- [ ] **L9 · EXPECTED** No errors in the player log over at least 2 full cycles _(general criterion)_

## Cell 1 · element:global_library_image | wide objectFit=contain

Options: `(predefinite)`

- [ ] **1.1 · EXPECTED** The element stays inside its own box (592x444 px) below the caption, without spilling outside the area _(layout.json (element geometry) + acceptance criterion)_
- [ ] **1.2 · EXPECTED** Shows the 800x400 px test image (red/green/blue/yellow corners, central circle) _(library file)_
- [ ] **1.3 · EXPECTED** Whole image visible (4 coloured corners) with aspect ratio preserved; empty bands on the free side (image 2.00:1, area 1.33:1) _(CSS object-fit: contain)_
- Cell result: ☐ PASS  ☐ FAIL  ☐ N/A — Notes: ______

## Cell 2 · element:global_library_image | wide objectFit=fill

Options: `objectFit=fill`

- [ ] **2.1 · EXPECTED** The element stays inside its own box (592x444 px) below the caption, without spilling outside the area _(layout.json (element geometry) + acceptance criterion)_
- [ ] **2.2 · EXPECTED** Shows the 800x400 px test image (red/green/blue/yellow corners, central circle) _(library file)_
- [ ] **2.3 · EXPECTED** Fills the whole area; aspect ratio not preserved (image 2.00:1, area 1.33:1) _(CSS object-fit: fill)_
- Cell result: ☐ PASS  ☐ FAIL  ☐ N/A — Notes: ______

## Cell 3 · element:global_library_image | wide objectFit=cover

Options: `objectFit=cover`

- [ ] **3.1 · EXPECTED** The element stays inside its own box (592x444 px) below the caption, without spilling outside the area _(layout.json (element geometry) + acceptance criterion)_
- [ ] **3.2 · EXPECTED** Shows the 800x400 px test image (red/green/blue/yellow corners, central circle) _(library file)_
- [ ] **3.3 · EXPECTED** Fills the whole area keeping the aspect ratio (2.00:1 image in a 1.33:1 area: the excess edges are cropped (some coloured corners cut off)) _(CSS object-fit: cover)_
- Cell result: ☐ PASS  ☐ FAIL  ☐ N/A — Notes: ______

## Cell 4 · element:global_library_image | tall objectFit=contain

Options: `(predefinite)`

- [ ] **4.1 · EXPECTED** The element stays inside its own box (592x444 px) below the caption, without spilling outside the area _(layout.json (element geometry) + acceptance criterion)_
- [ ] **4.2 · EXPECTED** Shows the 400x800 px test image (red/green/blue/yellow corners, central circle) _(library file)_
- [ ] **4.3 · EXPECTED** Whole image visible (4 coloured corners) with aspect ratio preserved; empty bands on the free side (image 0.50:1, area 1.33:1) _(CSS object-fit: contain)_
- Cell result: ☐ PASS  ☐ FAIL  ☐ N/A — Notes: ______

## Cell 5 · element:global_library_image | tall objectFit=fill

Options: `objectFit=fill`

- [ ] **5.1 · EXPECTED** The element stays inside its own box (592x444 px) below the caption, without spilling outside the area _(layout.json (element geometry) + acceptance criterion)_
- [ ] **5.2 · EXPECTED** Shows the 400x800 px test image (red/green/blue/yellow corners, central circle) _(library file)_
- [ ] **5.3 · EXPECTED** Fills the whole area; aspect ratio not preserved (image 0.50:1, area 1.33:1) _(CSS object-fit: fill)_
- Cell result: ☐ PASS  ☐ FAIL  ☐ N/A — Notes: ______

## Cell 6 · element:global_library_image | tall objectFit=cover

Options: `objectFit=cover`

- [ ] **6.1 · EXPECTED** The element stays inside its own box (592x444 px) below the caption, without spilling outside the area _(layout.json (element geometry) + acceptance criterion)_
- [ ] **6.2 · EXPECTED** Shows the 400x800 px test image (red/green/blue/yellow corners, central circle) _(library file)_
- [ ] **6.3 · EXPECTED** Fills the whole area keeping the aspect ratio (0.50:1 image in a 1.33:1 area: the excess edges are cropped (some coloured corners cut off)) _(CSS object-fit: cover)_
- Cell result: ☐ PASS  ☐ FAIL  ☐ N/A — Notes: ______
