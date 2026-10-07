# rt_embedded_01_portrait - checklist

Family `embedded` · 1080x1920 portrait · 60 s cycle · 6 cells · generated for Xibo 4.5.0

**EXPECTED** = derived from options, definitions or 4.5.0 code (source in brackets) · **OBSERVE** = not determinable in advance: record what you see.

## Layout

- [ ] **L1 · EXPECTED** Importing the zip completes without errors and creates the layout 'rt_embedded_01_portrait' _(LayoutFactory::createFromZip)_
- [ ] **L2 · EXPECTED** Size 1080x1920 px, orientation portrait; if the resolution does not exist in the CMS it is created ('1080 x 1920') _(LayoutFactory::createFromZip (getByDimensions → create))_
- [ ] **L3 · OBSERVE** Record the layout status after import (valid / draft / with warnings); if draft, publish it _(not determinable)_
- [ ] **L4 · EXPECTED** The Layout Editor shows 12 regions (per cell: caption + widget) _(layout.json)_
- [ ] **L5 · EXPECTED** Assigned to a portrait display (1080x1920): the layout fills the screen with no bars or cropping; if the display is physically rotated, set the rotation on the player _(layout.json (width/height))_
- [ ] **L6 · EXPECTED** The layout lasts 60 s (longest widget duration) and then restarts _(layout.json (duration))_
- [ ] **L7 · OBSERVE** Record whether, when the cycle restarts, countdowns, marquees and animations restart from scratch with no leftovers _(not determinable)_
- [ ] **L8 · EXPECTED** No errors in the player log over at least 2 full cycles _(general criterion)_

## Cell 1 · embedded | grid, scaleContent=0

Options: `embedHtml=<div style="width:100%;height:100%;box-sizing:border-box;bo…, embedStyle=html,body{margin:0;width:100%;height:100%}, scaleContent=0`

- [ ] **1.1 · EXPECTED** The widget occupies the intended area (512x560 px) below the caption, without overlapping adjacent cells or letting content spill outside its borders _(layout.json (region geometry) + acceptance criterion)_
- [ ] **1.2 · OBSERVE** scaleContent=0: record whether the content is scaled together with the region (compare with the variant having the opposite value) _(embedded.xml (scaleContent help))_
- [ ] **1.3 · EXPECTED** Box with a 6px border (#263238), 50px grid, two black centre lines, pink→blue gradient background and the text 'embedded 100% x 100%'; fills the whole widget area _(embedHtml/embedStyle)_
- Cell result: ☐ PASS  ☐ FAIL  ☐ N/A — Notes: ______

## Cell 2 · embedded | grid, scaleContent=1

Options: `embedHtml=<div style="width:100%;height:100%;box-sizing:border-box;bo…, embedStyle=html,body{margin:0;width:100%;height:100%}, scaleContent=1`

- [ ] **2.1 · EXPECTED** The widget occupies the intended area (512x560 px) below the caption, without overlapping adjacent cells or letting content spill outside its borders _(layout.json (region geometry) + acceptance criterion)_
- [ ] **2.2 · OBSERVE** scaleContent=1: record whether the content is scaled together with the region (compare with the variant having the opposite value) _(embedded.xml (scaleContent help))_
- [ ] **2.3 · EXPECTED** Box with a 6px border (#263238), 50px grid, two black centre lines, pink→blue gradient background and the text 'embedded 100% x 100%'; fills the whole widget area _(embedHtml/embedStyle)_
- Cell result: ☐ PASS  ☐ FAIL  ☐ N/A — Notes: ______

## Cell 3 · embedded | grid, no embedStyle (height collapse check)

Options: `embedHtml=<div style="width:100%;height:100%;box-sizing:border-box;bo…`

- [ ] **3.1 · EXPECTED** The widget occupies the intended area (512x560 px) below the caption, without overlapping adjacent cells or letting content spill outside its borders _(layout.json (region geometry) + acceptance criterion)_
- [ ] **3.2 · EXPECTED** The box is visible (div with width/height 100%) _(embedHtml)_
- [ ] **3.3 · OBSERVE** Without CSS on html/body the percentage height may collapse: record whether the box fills the area height _(standard CSS)_
- Cell result: ☐ PASS  ☐ FAIL  ☐ N/A — Notes: ______

## Cell 4 · embedded | transparency=1, translucent box

Options: `transparency=1, embedStyle=html,body{margin:0;width:100%;height:100%}, embedHtml=<div style="margin:40px;height:60%;background:rgba(21,101,1…`

- [ ] **4.1 · EXPECTED** The widget occupies the intended area (512x560 px) below the caption, without overlapping adjacent cells or letting content spill outside its borders _(layout.json (region geometry) + acceptance criterion)_
- [ ] **4.2 · EXPECTED** Widget background is transparent (requires content with a transparent background) _(embedded.xml (transparency help))_
- [ ] **4.3 · EXPECTED** Translucent blue box with the text 'transparency=1', 40px from the edges; around and through the box the layout background (#dfe3e8) shows, not a white one _(embedHtml/embedStyle)_
- Cell result: ☐ PASS  ☐ FAIL  ☐ N/A — Notes: ______

## Cell 5 · embedded | canvas animation via embedJavaScript

Options: `embedHtml=<canvas id="c" width="400" height="300" style="width:100%;h…, embedStyle=html,body{margin:0;width:100%;height:100%}, embedJavaScript=(function init(){var c=document.getElementById('c');if(!c){…, scaleContent=1`

- [ ] **5.1 · EXPECTED** The widget occupies the intended area (512x560 px) below the caption, without overlapping adjacent cells or letting content spill outside its borders _(layout.json (region geometry) + acceptance criterion)_
- [ ] **5.2 · OBSERVE** scaleContent=1: record whether the content is scaled together with the region (compare with the variant having the opposite value) _(embedded.xml (scaleContent help))_
- [ ] **5.3 · EXPECTED** Dark canvas (#102027) with an orbiting yellow dot and the text 'embedJavaScript t=…' with a continuously increasing value _(embedJavaScript)_
- Cell result: ☐ PASS  ☐ FAIL  ☐ N/A — Notes: ______

## Cell 6 · embedded | embedScript (head) visible in body

Options: `embedScript=<script>window.__rtHead="embedScript OK";</script>, embedHtml=<div id="o" style="font:32px monospace;padding:12px"></div>, embedJavaScript=(function t(){var o=document.getElementById('o');if(!o){set…`

- [ ] **6.1 · EXPECTED** The widget occupies the intended area (512x560 px) below the caption, without overlapping adjacent cells or letting content spill outside its borders _(layout.json (region geometry) + acceptance criterion)_
- [ ] **6.2 · EXPECTED** The text shows 'embedScript OK'; if it shows 'embedScript NOT executed' the script placed in the head did not run (FAIL) _(embedScript/embedJavaScript)_
- Cell result: ☐ PASS  ☐ FAIL  ☐ N/A — Notes: ______
