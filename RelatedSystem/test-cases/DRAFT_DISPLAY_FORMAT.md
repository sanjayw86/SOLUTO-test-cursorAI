# How to write & display SIGMA / Horizon drafts (readable format)

Use this layout for **draft** test cases so they are easy to read, review, and paste into chat.

**Finalised Horizon OpenSearch cases:** [TC_019](./TC_019.md) (enrollment + `/carrierinterface/v1/sigma/memo`), [TC_020](./TC_020.md) (call flow + same). Automation IDs **C00653**, **C00654**; Grade **D**.

**Finalised SMS cases (ex-drafts):** [TC_021](./TC_021.md) — **C10000**, Grade **D**; [TC_022](./TC_022.md) — **SMS_TEMP_001**, Grade **D**. Further review: [PENDING_REVIEW.md](./PENDING_REVIEW.md). Old draft filenames **point** to TC_021 / TC_022.

**Finalised ARCH cases:** [TC_023](./TC_023.md) — **C00129**, Grade **D** (調べる entry). [TC_024](./TC_024.md) — **C00131**, Grade **D** (Mypage → Contact Hub). *(Draft files removed after finalisation — edit `TC_023` / `TC_024` only.)*

**Draft files retained (SMS only):** [DRAFT_SMS_Manual_Delivery_Titan_ISS.md](./DRAFT_SMS_Manual_Delivery_Titan_ISS.md) → [TC_021](./TC_021.md); [DRAFT_SMS_Duplicate_Alert_AutoStop.md](./DRAFT_SMS_Duplicate_Alert_AutoStop.md) → [TC_022](./TC_022.md).

## 1. Opening banner (one line)

`Draft N — <Short scenario title> + <OpenSearch type> (full text)`

## 2. Document metadata (blank line after banner)

- **Manual Test Cases:** …  
- **Source:** …  
- **Viewpoint:** …  
- **Template:** Preconditions, Test Steps, Test Data, Postconditions  
- **Status:** DRAFT — …

## 3. Headings (use `##` in `.md` for preview)

- `## Draft test case` — one-line purpose  
- `## Identifiers` — Test Case ID, Title, Priority  
- `## Preconditions` — one bullet or line per item  
- `## Test Steps` — optional `### Phase 1` / `### Phase 2`  
  - Header row: `Step` + TAB + `Action` + TAB + `Expected Result`  
  - One row per step, tab-separated  
- `## Expected result (overall)` — single paragraph  
- `## Test Data` — sub-bullets (MDN, ISS, Japanese text blocks, Titan, URLs, Discover URL)  
- `## Note` — timing, Source values, troubleshooting, FO  
- `## Postconditions` — evidence + cleanup  

## 4. Spacing

- Blank line **before** each `##` section.  
- Blank line **after** multi-line blocks (e.g. after Preconditions list).  

## 5. When the AI displays a draft in chat

Use the same section order and labels as in the file; avoid dense walls of text.
