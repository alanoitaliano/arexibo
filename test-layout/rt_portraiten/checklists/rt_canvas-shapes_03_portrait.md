# rt_canvas-shapes_03_portrait - checklist

Family `canvas-shapes` · 1080x1920 portrait · 60 s cycle · 6 cells · generated for Xibo 4.5.0

**EXPECTED** = derived from options, definitions or 4.5.0 code (source in brackets) · **OBSERVE** = not determinable in advance: record what you see.

## Layout

- [ ] **L1 · EXPECTED** Importing the zip completes without errors and creates the layout 'rt_canvas-shapes_03_portrait' _(LayoutFactory::createFromZip)_
- [ ] **L2 · EXPECTED** Size 1080x1920 px, orientation portrait; if the resolution does not exist in the CMS it is created ('1080 x 1920') _(LayoutFactory::createFromZip (getByDimensions → create))_
- [ ] **L3 · OBSERVE** Record the layout status after import (valid / draft / with warnings); if draft, publish it _(not determinable)_
- [ ] **L4 · EXPECTED** The Layout Editor shows 1 canvas region with 18 elements (per cell: box, caption, element under test) _(layout.json)_
- [ ] **L5 · EXPECTED** Assigned to a portrait display (1080x1920): the layout fills the screen with no bars or cropping; if the display is physically rotated, set the rotation on the player _(layout.json (width/height))_
- [ ] **L6 · EXPECTED** The layout lasts 60 s (longest widget duration) and then restarts _(layout.json (duration))_
- [ ] **L7 · OBSERVE** Record whether, when the cycle restarts, countdowns, marquees and animations restart from scratch with no leftovers _(not determinable)_
- [ ] **L8 · EXPECTED** No errors in the player log over at least 2 full cycles _(general criterion)_

## Cell 1 · element:hexagon | hexagon fit=1

Options: `fit=1`

- [ ] **1.1 · EXPECTED** The element stays inside its own box (488x548 px) below the caption, without spilling outside the area _(layout.json (element geometry) + acceptance criterion)_
- [ ] **1.2 · EXPECTED** Shape 'hexagon': fill #1775F6, outline 8px #0d3c8a _(option value)_
- [ ] **1.3 · EXPECTED** The shape is scaled to fit the element area _(global-elements.xml (fit help))_
- Cell result: ☐ PASS  ☐ FAIL  ☐ N/A — Notes: ______

## Cell 2 · element:circle | circle no outline

Options: `outline=0`

- [ ] **2.1 · EXPECTED** The element stays inside its own box (488x548 px) below the caption, without spilling outside the area _(layout.json (element geometry) + acceptance criterion)_
- [ ] **2.2 · EXPECTED** Shape 'circle': fill #1775F6, no outline _(option value)_
- [ ] **2.3 · OBSERVE** fit=0: record how the shape is positioned/sized in the 488x548 px (non-square) area _(not determinable)_
- Cell result: ☐ PASS  ☐ FAIL  ☐ N/A — Notes: ______

## Cell 3 · element:triangle | triangle gradient

Options: `useGradient=1, gradient={"type":"linear","color1":"#d32f2f","color2":"#1976d2","ang…`

- [ ] **3.1 · EXPECTED** The element stays inside its own box (488x548 px) below the caption, without spilling outside the area _(layout.json (element geometry) + acceptance criterion)_
- [ ] **3.2 · EXPECTED** Shape 'triangle': fill #1775F6, outline 8px #0d3c8a _(option value)_
- [ ] **3.3 · EXPECTED** Fill with linear gradient from #d32f2f to #1976d2, angle 45° _(option value)_
- [ ] **3.4 · OBSERVE** fit=0: record how the shape is positioned/sized in the 488x548 px (non-square) area _(not determinable)_
- Cell result: ☐ PASS  ☐ FAIL  ☐ N/A — Notes: ______

## Cell 4 · element:hexagon | hexagon outline 20px

Options: `outlineColor=#2e7d32, outlineWidth=20`

- [ ] **4.1 · EXPECTED** The element stays inside its own box (488x548 px) below the caption, without spilling outside the area _(layout.json (element geometry) + acceptance criterion)_
- [ ] **4.2 · EXPECTED** Shape 'hexagon': fill #1775F6, outline 20px #2e7d32 _(option value)_
- [ ] **4.3 · OBSERVE** fit=0: record how the shape is positioned/sized in the 488x548 px (non-square) area _(not determinable)_
- Cell result: ☐ PASS  ☐ FAIL  ☐ N/A — Notes: ______

## Cell 5 · element:ellipse | ellipse default

Options: `(predefinite)`

- [ ] **5.1 · EXPECTED** The element stays inside its own box (488x548 px) below the caption, without spilling outside the area _(layout.json (element geometry) + acceptance criterion)_
- [ ] **5.2 · EXPECTED** Shape 'ellipse': fill #1775F6, outline 4px #0d3c8a _(option value)_
- Cell result: ☐ PASS  ☐ FAIL  ☐ N/A — Notes: ______

## Cell 6 · element:ellipse | ellipse no outline

Options: `backgroundColor=#ef6c00, outline=0`

- [ ] **6.1 · EXPECTED** The element stays inside its own box (488x548 px) below the caption, without spilling outside the area _(layout.json (element geometry) + acceptance criterion)_
- [ ] **6.2 · EXPECTED** Shape 'ellipse': fill #ef6c00, no outline _(option value)_
- Cell result: ☐ PASS  ☐ FAIL  ☐ N/A — Notes: ______
