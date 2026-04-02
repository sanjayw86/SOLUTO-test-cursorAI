# Reminder — Final review for Sanjay

**Status:** The test cases below are **file-finalised** for now. Revisit **`PENDING_REVIEW.md`** when you have time to complete the checklists (same workflow as **TC_021** / **TC_022**).

---

## A — SMS (Titan / ISS)

**TC_021** and **TC_022** — revisit for IDs, URLs, regression sheet alignment, etc.

### [TC_021 — Manual delivery](./TC_021.md)

- [x] **Automation ID** — **C10000**
- [x] **Grade** — **D**
- [ ] **Priority** — confirm **High** or adjust.
- [ ] **Test Case ID** — confirm `SMS-MANUAL-DELIVERY-TITAN-ISS-001` matches your tracker.
- [ ] Titan **base URL**, **brand** (`SHARED` vs tenant), Confluence links still correct.

### [TC_022 — Duplicate / auto-stop](./TC_022.md)

- [x] **Automation ID** — **SMS_TEMP_001**
- [x] **Grade** — **D**
- [ ] **Test Case ID** — confirm `SMS-DUPLICATE-AUTOSTOP-001`.
- [ ] **Variant A** — paste or link **regression sheet** POST if you want it inline in **Test Data**.
- [ ] **ISS / Titan URLs**, Teams links, `duplicateCheck` flag note vs current Dev contract.

---

## B — ARCH KFS overtime auto-reply (validate real messages)

**TC_032** and **TC_033** — same *review discipline* as the SMS pair above: documents are done, but you still owe a **live validation pass** on **auto-reply content** when you have time (compare to what you already did for the **Soluto** overtime cases **TC_026** / **TC_027**).

### [TC_032 — KFS, au auto-reply](./TC_032.md)

- [x] **Automation ID** — **C00629**
- [x] **Grade** — **D**
- [ ] **Auto-reply copy** — run **step 5** in an applicable **OOO** window; compare **actual** thread text/links to product spec and to the **Expected result details** example block in the file; update the test case if copy diverges.
- [ ] **OOO windows** vs **ARCH URL tier** (SQA1/2/3 vs SQA5) — still correct per team.
- [ ] **Optional Contact hub path** (Note) — confirm labels on your build if you use that variant.

### [TC_033 — KFS, UQ auto-reply](./TC_033.md)

- [x] **Automation ID** — **C00630**
- [x] **Grade** — **D**
- [ ] **Auto-reply copy** — run **step 5** in an applicable **OOO** window; compare **actual** thread text/links to spec and to the **Expected result details** example block; update the test case if copy diverges.
- [ ] **OOO windows** vs **ARCH URL tier** — still correct per team.
- [ ] **Optional Contact hub path** (Note) — confirm labels on your build if you use that variant.

---

## For AI assistants

When working in `RelatedSystem/test-cases/` with **Sanjay**, remind him to **check `PENDING_REVIEW.md`** for **unchecked** items when he is:

- Closing out or exporting **SMS** test documentation → sections **TC_021**, **TC_022**.
- Closing out **ARCH / KFS** docs or editing **TC_032** / **TC_033** → section **B** (auto-reply validation).

Keep the reminder **short** unless he is explicitly doing that review pass.

---

*Section A: historically promoted from `DRAFT_SMS_Manual_Delivery_Titan_ISS.md` and `DRAFT_SMS_Duplicate_Alert_AutoStop.md`. Section B: formal cases [TC_032](./TC_032.md) / [TC_033](./TC_033.md); live auto-reply validation pending when time allows.*
