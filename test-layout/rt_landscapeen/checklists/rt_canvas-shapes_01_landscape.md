# rt_canvas-shapes_01_landscape - checklist

Family `canvas-shapes` · 1920x1080 landscape · 60 s cycle · 6 cells · generated for Xibo 4.5.0

**EXPECTED** = derived from options, definitions or 4.5.0 code (source in brackets) · **OBSERVE** = not determinable in advance: record what you see.

## Layout

- [ ] **L1 · EXPECTED** Importing the zip completes without errors and creates the layout 'rt_canvas-shapes_01_landscape' _(LayoutFactory::createFromZip)_
- [ ] **L2 · EXPECTED** Size 1920x1080 px, orientation landscape; if the resolution does not exist in the CMS it is created ('1920 x 1080') _(LayoutFactory::createFromZip (getByDimensions → create))_
- [ ] **L3 · OBSERVE** Record the layout status after import (valid / draft / with warnings); if draft, publish it _(not determinable)_
- [ ] **L4 · EXPECTED** The Layout Editor shows 1 canvas region with 18 elements (per cell: box, caption, element under test) _(layout.json)_
- [ ] **L5 · EXPECTED** Assigned to a landscape display (1920x1080): the layout fills the screen with no bars or cropping; if the display is physically rotated, set the rotation on the player _(layout.json (width/height))_
- [ ] **L6 · EXPECTED** The layout lasts 60 s (longest widget duration) and then restarts _(layout.json (duration))_
- [ ] **L7 · OBSERVE** Record whether, when the cycle restarts, countdowns, marquees and animations restart from scratch with no leftovers _(not determinable)_
- [ ] **L8 · EXPECTED** No errors in the player log over at least 2 full cycles _(general criterion)_

## Cell 1 · element:rectangle | rectangle default

Options: `(predefinite)`

- [ ] **1.1 · EXPECTED** The element stays inside its own box (592x444 px) below the caption, without spilling outside the area _(layout.json (element geometry) + acceptance criterion)_
- [ ] **1.2 · EXPECTED** Shape 'rectangle': fill #1775F6, outline 8px #0d3c8a _(option value)_
- Cell result: ☐ PASS  ☐ FAIL  ☐ N/A — Notes: ______

## Cell 2 · element:rectangle | rectangle roundBorder r=60

Options: `roundBorder=1, borderRadius=60`

- [ ] **2.1 · EXPECTED** The element stays inside its own box (592x444 px) below the caption, without spilling outside the area _(layout.json (element geometry) + acceptance criterion)_
- [ ] **2.2 · EXPECTED** Shape 'rectangle': fill #1775F6, outline 8px #0d3c8a _(option value)_
- [ ] **2.3 · EXPECTED** Rounded corners with 60px radius _(option value)_
- Cell result: ☐ PASS  ☐ FAIL  ☐ N/A — Notes: ______

## Cell 3 · element:rectangle | rectangle no outline

Options: `outline=0`

- [ ] **3.1 · EXPECTED** The element stays inside its own box (592x444 px) below the caption, without spilling outside the area _(layout.json (element geometry) + acceptance criterion)_
- [ ] **3.2 · EXPECTED** Shape 'rectangle': fill #1775F6, no outline _(option value)_
- Cell result: ☐ PASS  ☐ FAIL  ☐ N/A — Notes: ______

## Cell 4 · element:rectangle | rectangle outline 24px

Options: `outlineColor=#c62828, outlineWidth=24`

- [ ] **4.1 · EXPECTED** The element stays inside its own box (592x444 px) below the caption, without spilling outside the area _(layout.json (element geometry) + acceptance criterion)_
- [ ] **4.2 · EXPECTED** Shape 'rectangle': fill #1775F6, outline 24px #c62828 _(option value)_
- Cell result: ☐ PASS  ☐ FAIL  ☐ N/A — Notes: ______

## Cell 5 · element:rectangle | rectangle gradient

Options: `useGradient=1, gradient={"type":"linear","color1":"#d32f2f","color2":"#1976d2","ang…`

- [ ] **5.1 · EXPECTED** The element stays inside its own box (592x444 px) below the caption, without spilling outside the area _(layout.json (element geometry) + acceptance criterion)_
- [ ] **5.2 · EXPECTED** Shape 'rectangle': fill #1775F6, outline 8px #0d3c8a _(option value)_
- [ ] **5.3 · EXPECTED** Fill with linear gradient from #d32f2f to #1976d2, angle 45° _(option value)_
- Cell result: ☐ PASS  ☐ FAIL  ☐ N/A — Notes: ______

## Cell 6 · element:circle | circle default

Options: `(predefinite)`

- [ ] **6.1 · EXPECTED** The element stays inside its own box (592x444 px) below the caption, without spilling outside the area _(layout.json (element geometry) + acceptance criterion)_
- [ ] **6.2 · EXPECTED** Shape 'circle': fill #1775F6, outline 8px #0d3c8a _(option value)_
- [ ] **6.3 · OBSERVE** fit=0: record how the shape is positioned/sized in the 592x444 px (non-square) area _(not determinable)_
- Cell result: ☐ PASS  ☐ FAIL  ☐ N/A — Notes: ______
