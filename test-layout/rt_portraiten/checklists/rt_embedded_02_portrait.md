# rt_embedded_02_portrait - checklist

Family `embedded` · 1080x1920 portrait · 60 s cycle · 1 cells · generated for Xibo 4.5.0

**EXPECTED** = derived from options, definitions or 4.5.0 code (source in brackets) · **OBSERVE** = not determinable in advance: record what you see.

## Layout

- [ ] **L1 · EXPECTED** Importing the zip completes without errors and creates the layout 'rt_embedded_02_portrait' _(LayoutFactory::createFromZip)_
- [ ] **L2 · EXPECTED** Size 1080x1920 px, orientation portrait; if the resolution does not exist in the CMS it is created ('1080 x 1920') _(LayoutFactory::createFromZip (getByDimensions → create))_
- [ ] **L3 · OBSERVE** Record the layout status after import (valid / draft / with warnings); if draft, publish it _(not determinable)_
- [ ] **L4 · EXPECTED** The Layout Editor shows 2 regions (per cell: caption + widget) _(layout.json)_
- [ ] **L5 · EXPECTED** Assigned to a portrait display (1080x1920): the layout fills the screen with no bars or cropping; if the display is physically rotated, set the rotation on the player _(layout.json (width/height))_
- [ ] **L6 · EXPECTED** The layout lasts 60 s (longest widget duration) and then restarts _(layout.json (duration))_
- [ ] **L7 · OBSERVE** Record whether, when the cycle restarts, countdowns, marquees and animations restart from scratch with no leftovers _(not determinable)_
- [ ] **L8 · EXPECTED** No errors in the player log over at least 2 full cycles _(general criterion)_

## Cell 1 · embedded | embedStyle only (web fonts/emoji/unicode)

Options: `embedStyle=.b{font:36px serif;padding:12px;color:#4a148c}, embedHtml=<div class="b">àèìòù € — ✓ ★ ☀ 日本語</div>`

- [ ] **1.1 · EXPECTED** The widget occupies the intended area (512x560 px) below the caption, without overlapping adjacent cells or letting content spill outside its borders _(layout.json (region geometry) + acceptance criterion)_
- [ ] **1.2 · EXPECTED** Shows 'àèìòù € — ✓ ★ ☀ 日本語' in 36px serif purple (#4a148c) _(embedHtml/embedStyle)_
- [ ] **1.3 · OBSERVE** Record whether any symbol (✓ ★ ☀ or the Japanese characters) appears as a box or missing glyph: depends on the player's system fonts _(not determinable)_
- Cell result: ☐ PASS  ☐ FAIL  ☐ N/A — Notes: ______
