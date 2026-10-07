# rt_canvas-text_02_portrait - checklist

Family `canvas-text` · 1080x1920 portrait · 60 s cycle · 6 cells · generated for Xibo 4.5.0

**EXPECTED** = derived from options, definitions or 4.5.0 code (source in brackets) · **OBSERVE** = not determinable in advance: record what you see.

## Layout

- [ ] **L1 · EXPECTED** Importing the zip completes without errors and creates the layout 'rt_canvas-text_02_portrait' _(LayoutFactory::createFromZip)_
- [ ] **L2 · EXPECTED** Size 1080x1920 px, orientation portrait; if the resolution does not exist in the CMS it is created ('1080 x 1920') _(LayoutFactory::createFromZip (getByDimensions → create))_
- [ ] **L3 · OBSERVE** Record the layout status after import (valid / draft / with warnings); if draft, publish it _(not determinable)_
- [ ] **L4 · EXPECTED** The Layout Editor shows 1 canvas region with 18 elements (per cell: box, caption, element under test) _(layout.json)_
- [ ] **L5 · EXPECTED** Assigned to a portrait display (1080x1920): the layout fills the screen with no bars or cropping; if the display is physically rotated, set the rotation on the player _(layout.json (width/height))_
- [ ] **L6 · EXPECTED** The layout lasts 60 s (longest widget duration) and then restarts _(layout.json (duration))_
- [ ] **L7 · OBSERVE** Record whether, when the cycle restarts, countdowns, marquees and animations restart from scratch with no leftovers _(not determinable)_
- [ ] **L8 · EXPECTED** No errors in the player log over at least 2 full cycles _(general criterion)_

## Cell 1 · element:text | vertical flex-end

Options: `verticalAlign=flex-end`

- [ ] **1.1 · EXPECTED** The element stays inside its own box (488x548 px) below the caption, without spilling outside the area _(layout.json (element geometry) + acceptance criterion)_
- [ ] **1.2 · EXPECTED** Text: «Canvas text àèìòù €» _(option value)_
- [ ] **1.3 · EXPECTED** Text positioned bottom (vertical) _(global-elements.xml (hbs))_
- Cell result: ☐ PASS  ☐ FAIL  ☐ N/A — Notes: ______

## Cell 2 · element:text | textShadow on

Options: `textShadow=1, textShadowColor=#888888, shadowX=4, shadowY=4, shadowBlur=6`

- [ ] **2.1 · EXPECTED** The element stays inside its own box (488x548 px) below the caption, without spilling outside the area _(layout.json (element geometry) + acceptance criterion)_
- [ ] **2.2 · EXPECTED** Text: «Canvas text àèìòù €» _(option value)_
- [ ] **2.3 · EXPECTED** Text shadow colour #888888, offset (4,4), blur 6 _(option value)_
- Cell result: ☐ PASS  ☐ FAIL  ☐ N/A — Notes: ______

## Cell 3 · element:text | gradient text

Options: `useGradient=1, gradient={"type":"linear","color1":"#d32f2f","color2":"#1976d2","ang…, fontSize=56, bold=1`

- [ ] **3.1 · EXPECTED** The element stays inside its own box (488x548 px) below the caption, without spilling outside the area _(layout.json (element geometry) + acceptance criterion)_
- [ ] **3.2 · EXPECTED** Text: «Canvas text àèìòù €» _(option value)_
- [ ] **3.3 · EXPECTED** Size 56px _(option value)_
- [ ] **3.4 · EXPECTED** Text is bold _(option value)_
- [ ] **3.5 · EXPECTED** Text with linear gradient from #d32f2f to #1976d2, angle 45° _(option value)_
- Cell result: ☐ PASS  ☐ FAIL  ☐ N/A — Notes: ______

## Cell 4 · element:text | fitToArea (long text)

Options: `fitToArea=1`

- [ ] **4.1 · EXPECTED** The element stays inside its own box (488x548 px) below the caption, without spilling outside the area _(layout.json (element geometry) + acceptance criterion)_
- [ ] **4.2 · EXPECTED** Text: «Long canvas text that must wrap or shrink depending on the …» _(option value)_
- [ ] **4.3 · EXPECTED** The text is resized to fill the element area (size is not the fixed one) _(global-elements.xml (fitToArea help))_
- Cell result: ☐ PASS  ☐ FAIL  ☐ N/A — Notes: ______

## Cell 5 · element:text | textWrap=1 (long text)

Options: `fontSize=28`

- [ ] **5.1 · EXPECTED** The element stays inside its own box (488x548 px) below the caption, without spilling outside the area _(layout.json (element geometry) + acceptance criterion)_
- [ ] **5.2 · EXPECTED** Text: «Long canvas text that must wrap or shrink depending on the …» _(option value)_
- [ ] **5.3 · EXPECTED** Size 28px _(option value)_
- Cell result: ☐ PASS  ☐ FAIL  ☐ N/A — Notes: ______

## Cell 6 · element:text | textWrap=0 (long text)

Options: `fontSize=28, textWrap=0`

- [ ] **6.1 · EXPECTED** The element stays inside its own box (488x548 px) below the caption, without spilling outside the area _(layout.json (element geometry) + acceptance criterion)_
- [ ] **6.2 · EXPECTED** Text: «Long canvas text that must wrap or shrink depending on the …» _(option value)_
- [ ] **6.3 · EXPECTED** Size 28px _(option value)_
- [ ] **6.4 · EXPECTED** The text stays on a single line, without wrapping _(global-elements.xml (textWrap help))_
- Cell result: ☐ PASS  ☐ FAIL  ☐ N/A — Notes: ______
