# rt_worldclock-digital-custom_01_landscape - checklist

Family `worldclock-digital-custom` · 1920x1080 landscape · 60 s cycle · 6 cells · generated for Xibo 4.5.0

**EXPECTED** = derived from options, definitions or 4.5.0 code (source in brackets) · **OBSERVE** = not determinable in advance: record what you see.

## Layout

- [ ] **L1 · EXPECTED** Importing the zip completes without errors and creates the layout 'rt_worldclock-digital-custom_01_landscape' _(LayoutFactory::createFromZip)_
- [ ] **L2 · EXPECTED** Size 1920x1080 px, orientation landscape; if the resolution does not exist in the CMS it is created ('1920 x 1080') _(LayoutFactory::createFromZip (getByDimensions → create))_
- [ ] **L3 · OBSERVE** Record the layout status after import (valid / draft / with warnings); if draft, publish it _(not determinable)_
- [ ] **L4 · EXPECTED** The Layout Editor shows 12 regions (per cell: caption + widget) _(layout.json)_
- [ ] **L5 · EXPECTED** Assigned to a landscape display (1920x1080): the layout fills the screen with no bars or cropping; if the display is physically rotated, set the rotation on the player _(layout.json (width/height))_
- [ ] **L6 · EXPECTED** The layout lasts 60 s (longest widget duration) and then restarts _(layout.json (duration))_
- [ ] **L7 · OBSERVE** Record whether, when the cycle restarts, countdowns, marquees and animations restart from scratch with no leftovers _(not determinable)_
- [ ] **L8 · EXPECTED** No errors in the player log over at least 2 full cycles _(general criterion)_

## Cell 1 · worldclock-digital-custom | 1 clock 1x1

Options: `template_html=<div class="clock">
    <div class="inner-clock">
        […, template_style=.clock {
    background: #a6b1f2;
    color: #161616;
    w…, widgetDesignWidth=200, widgetDesignHeight=100, worldClocks=[{"clockTimezone":"Europe/R…`

- [ ] **1.1 · EXPECTED** The widget occupies the intended area (616x456 px) below the caption, without overlapping adjacent cells or letting content spill outside its borders _(layout.json (region geometry) + acceptance criterion)_
- [ ] **1.2 · EXPECTED** 1 clock(s): Rome (Europe/Rome) _(option value)_
- [ ] **1.3 · EXPECTED** Arranged in 1 column(s) × 1 row(s) _(worldclock-*.xml (numCols/numRows))_
- [ ] **1.4 · EXPECTED** Each clock shows the time of its own timezone (compare with --expected-now) and advances _(xibo-worldclock-render.js (moment.tz))_
- [ ] **1.5 · EXPECTED** Default template: #a6b1f2 boxes 190x90, 15px radius, with HH:mm:ss time and label _(worldclock-digital-custom.xml (default))_
- [ ] **1.6 · OBSERVE** widgetDesignWidth/Height = 200x100: record whether the 1x1 grid is scaled correctly in the 616x456 px area _(not determinable)_
- Cell result: ☐ PASS  ☐ FAIL  ☐ N/A — Notes: ______

## Cell 2 · worldclock-digital-custom | 2 clocks 2x1

Options: `template_html=<div class="clock">
    <div class="inner-clock">
        […, template_style=.clock {
    background: #a6b1f2;
    color: #161616;
    w…, widgetDesignWidth=200, widgetDesignHeight=100, worldClocks=[{"clockTimezone":"Europe/R…`

- [ ] **2.1 · EXPECTED** The widget occupies the intended area (616x456 px) below the caption, without overlapping adjacent cells or letting content spill outside its borders _(layout.json (region geometry) + acceptance criterion)_
- [ ] **2.2 · EXPECTED** 2 clock(s): Rome (Europe/Rome), New York (America/New_York) _(option value)_
- [ ] **2.3 · EXPECTED** Arranged in 2 column(s) × 1 row(s) _(worldclock-*.xml (numCols/numRows))_
- [ ] **2.4 · EXPECTED** Each clock shows the time of its own timezone (compare with --expected-now) and advances _(xibo-worldclock-render.js (moment.tz))_
- [ ] **2.5 · EXPECTED** Default template: #a6b1f2 boxes 190x90, 15px radius, with HH:mm:ss time and label _(worldclock-digital-custom.xml (default))_
- [ ] **2.6 · OBSERVE** widgetDesignWidth/Height = 200x100: record whether the 2x1 grid is scaled correctly in the 616x456 px area _(not determinable)_
- Cell result: ☐ PASS  ☐ FAIL  ☐ N/A — Notes: ______

## Cell 3 · worldclock-digital-custom | 4 clocks 2x2

Options: `template_html=<div class="clock">
    <div class="inner-clock">
        […, template_style=.clock {
    background: #a6b1f2;
    color: #161616;
    w…, widgetDesignWidth=200, widgetDesignHeight=100, worldClocks=[{"clockTimezone":"Europe/R…`

- [ ] **3.1 · EXPECTED** The widget occupies the intended area (616x456 px) below the caption, without overlapping adjacent cells or letting content spill outside its borders _(layout.json (region geometry) + acceptance criterion)_
- [ ] **3.2 · EXPECTED** 4 clock(s): Rome (Europe/Rome), New York (America/New_York), Tokyo (Asia/Tokyo), Sydney (Australia/Sydney) _(option value)_
- [ ] **3.3 · EXPECTED** Arranged in 2 column(s) × 2 row(s) _(worldclock-*.xml (numCols/numRows))_
- [ ] **3.4 · EXPECTED** Each clock shows the time of its own timezone (compare with --expected-now) and advances _(xibo-worldclock-render.js (moment.tz))_
- [ ] **3.5 · EXPECTED** Default template: #a6b1f2 boxes 190x90, 15px radius, with HH:mm:ss time and label _(worldclock-digital-custom.xml (default))_
- [ ] **3.6 · OBSERVE** widgetDesignWidth/Height = 200x100: record whether the 2x2 grid is scaled correctly in the 616x456 px area _(not determinable)_
- Cell result: ☐ PASS  ☐ FAIL  ☐ N/A — Notes: ______

## Cell 4 · worldclock-digital-custom | 4 clocks 1x4 (column)

Options: `template_html=<div class="clock">
    <div class="inner-clock">
        […, template_style=.clock {
    background: #a6b1f2;
    color: #161616;
    w…, widgetDesignWidth=200, widgetDesignHeight=100, worldClocks=[{"clockTimezone":"Europe/R…`

- [ ] **4.1 · EXPECTED** The widget occupies the intended area (616x456 px) below the caption, without overlapping adjacent cells or letting content spill outside its borders _(layout.json (region geometry) + acceptance criterion)_
- [ ] **4.2 · EXPECTED** 4 clock(s): Rome (Europe/Rome), New York (America/New_York), Tokyo (Asia/Tokyo), Sydney (Australia/Sydney) _(option value)_
- [ ] **4.3 · EXPECTED** Arranged in 1 column(s) × 4 row(s) _(worldclock-*.xml (numCols/numRows))_
- [ ] **4.4 · EXPECTED** Each clock shows the time of its own timezone (compare with --expected-now) and advances _(xibo-worldclock-render.js (moment.tz))_
- [ ] **4.5 · EXPECTED** Default template: #a6b1f2 boxes 190x90, 15px radius, with HH:mm:ss time and label _(worldclock-digital-custom.xml (default))_
- [ ] **4.6 · OBSERVE** widgetDesignWidth/Height = 200x100: record whether the 1x4 grid is scaled correctly in the 616x456 px area _(not determinable)_
- Cell result: ☐ PASS  ☐ FAIL  ☐ N/A — Notes: ______

## Cell 5 · worldclock-digital-custom | 4 clocks 2x2 highlight #2, left/top

Options: `template_html=<div class="clock">
    <div class="inner-clock">
        […, template_style=.clock {
    background: #a6b1f2;
    color: #161616;
    w…, widgetDesignWidth=200, widgetDesignHeight=100, worldClocks=[{"clockTimezone":"Europe/R…`

- [ ] **5.1 · EXPECTED** The widget occupies the intended area (616x456 px) below the caption, without overlapping adjacent cells or letting content spill outside its borders _(layout.json (region geometry) + acceptance criterion)_
- [ ] **5.2 · EXPECTED** 4 clock(s): Rome (Europe/Rome), New York (America/New_York), Tokyo (Asia/Tokyo), Sydney (Australia/Sydney) _(option value)_
- [ ] **5.3 · EXPECTED** Arranged in 2 column(s) × 2 row(s) _(worldclock-*.xml (numCols/numRows))_
- [ ] **5.4 · EXPECTED** Each clock shows the time of its own timezone (compare with --expected-now) and advances _(xibo-worldclock-render.js (moment.tz))_
- [ ] **5.5 · OBSERVE** 'New York' has clockHighlight=1: record how it is highlighted _(xibo-worldclock-render.js (clockHighlight))_
- [ ] **5.6 · EXPECTED** Grid aligned left / top in the area _(4.5.0 definition)_
- [ ] **5.7 · EXPECTED** Default template: #a6b1f2 boxes 190x90, 15px radius, with HH:mm:ss time and label _(worldclock-digital-custom.xml (default))_
- [ ] **5.8 · OBSERVE** widgetDesignWidth/Height = 200x100: record whether the 2x2 grid is scaled correctly in the 616x456 px area _(not determinable)_
- Cell result: ☐ PASS  ☐ FAIL  ☐ N/A — Notes: ______

## Cell 6 · worldclock-digital-custom | 2 clocks: custom HTML/CSS template

Options: `template_html=<div class="clock"><div class="inner-clock">[HH:mm]</div><d…, template_style=.clock{background:#263238;color:#fff;width:190px;height:110…, widgetDesignWidth=200, widgetDesignHeight=120, worldClocks=[{"clockTimezone":"Europe/R…`

- [ ] **6.1 · EXPECTED** The widget occupies the intended area (616x456 px) below the caption, without overlapping adjacent cells or letting content spill outside its borders _(layout.json (region geometry) + acceptance criterion)_
- [ ] **6.2 · EXPECTED** 2 clock(s): Rome (Europe/Rome), New York (America/New_York) _(option value)_
- [ ] **6.3 · EXPECTED** Arranged in 2 column(s) × 1 row(s) _(worldclock-*.xml (numCols/numRows))_
- [ ] **6.4 · EXPECTED** Each clock shows the time of its own timezone (compare with --expected-now) and advances _(xibo-worldclock-render.js (moment.tz))_
- [ ] **6.5 · EXPECTED** Dark boxes (#263238) 190x110 with time 'HH:mm' 36px, small grey 'ddd DD/MM' and yellow (#ffca28) label _(custom template)_
- [ ] **6.6 · OBSERVE** widgetDesignWidth/Height = 200x120: record whether the 2x1 grid is scaled correctly in the 616x456 px area _(not determinable)_
- Cell result: ☐ PASS  ☐ FAIL  ☐ N/A — Notes: ______
