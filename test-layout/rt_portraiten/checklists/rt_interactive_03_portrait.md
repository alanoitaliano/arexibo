# rt_interactive_03_portrait - checklist

Family `interactive` · 1080x1920 portrait · 60 s cycle · 2 cells · generated for Xibo 4.5.0

**EXPECTED** = derived from options, definitions or 4.5.0 code (source in brackets) · **OBSERVE** = not determinable in advance: record what you see.

## Layout

- [ ] **L1 · EXPECTED** Importing the zip completes without errors and creates the layout 'rt_interactive_03_portrait' _(LayoutFactory::createFromZip)_
- [ ] **L2 · EXPECTED** Size 1080x1920 px, orientation portrait; if the resolution does not exist in the CMS it is created ('1080 x 1920') _(LayoutFactory::createFromZip (getByDimensions → create))_
- [ ] **L3 · OBSERVE** Record the layout status after import (valid / draft / with warnings); if draft, publish it _(not determinable)_
- [ ] **L4 · EXPECTED** The Layout Editor shows 4 regions (per cell: caption + widget) _(layout.json)_
- [ ] **L5 · EXPECTED** Assigned to a portrait display (1080x1920): the layout fills the screen with no bars or cropping; if the display is physically rotated, set the rotation on the player _(layout.json (width/height))_
- [ ] **L6 · EXPECTED** The layout lasts 60 s (longest widget duration) and then restarts _(layout.json (duration))_
- [ ] **L7 · OBSERVE** Record whether, when the cycle restarts, countdowns, marquees and animations restart from scratch with no leftovers _(not determinable)_
- [ ] **L8 · EXPECTED** No errors in the player log over at least 2 full cycles _(general criterion)_

## Cell 1 · interactive-link | link fitToArea

Options: `text=Fit to area, fitToArea=1`

- [ ] **1.1 · EXPECTED** The widget occupies the intended area (512x560 px) below the caption, without overlapping adjacent cells or letting content spill outside its borders _(layout.json (region geometry) + acceptance criterion)_
- [ ] **1.2 · EXPECTED** Shows «Fit to area» _(option value)_
- [ ] **1.3 · EXPECTED** Touching it triggers no action (no action configured on the widget) _(layout.json (empty actions))_
- [ ] **1.4 · EXPECTED** The text is resized to fill the area (size not fixed) _(4.5.0 definition (fitToArea))_
- Cell result: ☐ PASS  ☐ FAIL  ☐ N/A — Notes: ______

## Cell 2 · interactive-link | link wrap, flex-end

Options: `text=Long wrapped link text to test wrapping, textWrap=1, horizontalAlign=flex-end, verticalAlign=flex-end`

- [ ] **2.1 · EXPECTED** The widget occupies the intended area (512x560 px) below the caption, without overlapping adjacent cells or letting content spill outside its borders _(layout.json (region geometry) + acceptance criterion)_
- [ ] **2.2 · EXPECTED** Shows «Long wrapped link text to test wrapping» _(option value)_
- [ ] **2.3 · EXPECTED** Touching it triggers no action (no action configured on the widget) _(layout.json (empty actions))_
- [ ] **2.4 · EXPECTED** The text wraps within the width _(4.5.0 definition (textWrap))_
- [ ] **2.5 · EXPECTED** Text positioned right (horizontal) and bottom (vertical) _(option value)_
- Cell result: ☐ PASS  ☐ FAIL  ☐ N/A — Notes: ______
