# Rendering test preparation

## 1. Record the environment (once per session)
- [ ] CMS version: ______ (options are verified against the Xibo 4.5.0 definitions)
- [ ] Player and version: ______  · display: resolution ______ , rotation ______
- [ ] Timezone and locale of the player/display: ______ (affects clocks, dates and localised formats)
- [ ] Test date and time: ______ · reference clock used: ______
- [ ] CMS folder the layouts are imported into: ______

## 2. Import
- [ ] Import ONE layout first (e.g. `rt_clock-digital_01_*`) and check the outcome, then the others
- [ ] Check that the IDs inside the zips (starting at 900000) were reassigned by the CMS
- [ ] Check the test images (`rt_*.png`) in the Library and that they are not duplicated

## 3. Expected values that depend on the moment of the test
Run on the test machine, at the same moment as the check:

    python3 xibo_render_test_gen.py --expected-now

It prints the current times in the timezones used by the world clock variants and the expected values of the dated
countdowns (`rt_countdown-*`). For cells with an offset, the reference is the player's system time.

## 4. How to fill in
- For each layout: open `checklists/<layout>.md` or fill in `checklist.csv` (`;` separator, UTF-8):
  `result` column = PASS / FAIL / N/A, `notes` for details.
- **EXPECTED** checks: PASS if the result matches; otherwise FAIL with a description of what you see.
- **OBSERVE** checks: no prior judgement; write in `notes` what happens (it clarifies the behaviour).
- On FAIL: attach a screenshot and note the layout, cell and check id.
