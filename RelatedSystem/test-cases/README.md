# RelatedSystem – Test Cases

**Project:** SOLUTO  
**Feature:** RelatedSystem

---

## Test cases

| # | Test case | File |
|---|-----------|------|
| 1 | Welcome SMS and Reminder 1/2 SMS (Orange API, brand AU) | [TC_001](./TC_001.md) |
| 2 | Reminder1 SMS after Welcome SMS (Admin UI: Remind1 ON, 1 day) | [TC_002](./TC_002.md) |
| 3 | Reminder2 SMS after Welcome SMS (Admin UI: Remind2 ON, 1 day) | [TC_003](./TC_003.md) |
| 4 | Welcome SMS and Reminder 1/2 SMS (Orange API, brand UQ) | [TC_004](./TC_004.md) |
| 5 | Reminder1 SMS after Welcome SMS (Admin UI: Remind1 ON, 1 day) – UQ | [TC_005](./TC_005.md) |
| 6 | Reminder2 SMS after Welcome SMS (Admin UI: Remind2 ON, 1 day) – UQ | [TC_006](./TC_006.md) |
| 7 | Welcome SMS after CSV enrollment (CSV registration, brand AU) | [TC_007](./TC_007.md) |
| 8 | Reminder1 SMS after CSV enrollment (CSV registration, Remind1 ON, brand AU) | [TC_008](./TC_008.md) |
| 9 | Reminder2 SMS after CSV enrollment (CSV registration, Remind2 ON, brand AU) | [TC_009](./TC_009.md) |
| 10 | Welcome SMS not sent after CSV enrollment (CSV registration, service enabled: false, brand AU) | [TC_010](./TC_010.md) |
| 11 | Reminder1 SMS not sent after CSV enrollment (CSV registration, service enabled: false, brand AU) | [TC_011](./TC_011.md) |
| 12 | Reminder2 SMS not sent after CSV enrollment (CSV registration, service enabled: false, brand AU) | [TC_012](./TC_012.md) |
| 13 | Call Reservation SMS sent when reservation is made (Un-provisioned MDN, brand AU) | [TC_013](./TC_013.md) |
| 14 | Call Reminder SMS sent before actual call reservation time (Un-provisioned MDN, brand AU) | [TC_014](./TC_014.md) |
| 15 | Call Cancellation SMS sent when reservation is cancelled (Un-provisioned MDN, brand AU) | [TC_015](./TC_015.md) |
| 16 | Call Reservation SMS not sent when reservation is made (Provisioned MDN, brand AU) | [TC_016](./TC_016.md) |
| 17 | Enrollment SMS (Welcome, Reminder1, Reminder2) in ISS and SIGMA MEMO / ATOM API logs in OpenSearch (CSV or Orange API, AU) | [TC_017](./TC_017.md) |
| 18 | Call Reservation, Reminder, and Cancellation SMS in ISS and SIGMA MEMO / ATOM API logs in OpenSearch (Un-provisioned MDN, AU) | [TC_018](./TC_018.md) |
| 19 | Enrollment SMS (Welcome, Reminder1, Reminder2) in ISS and Horizon SIGMA MEMO logs in OpenSearch (CSV or Orange API, AU) | [TC_019](./TC_019.md) |
| 20 | Call Reservation, Reminder, and Cancellation SMS in ISS and Horizon SIGMA MEMO logs in OpenSearch (Un-provisioned MDN, AU) | [TC_020](./TC_020.md) |
| 21 | Manual delivery mode — Titan GET/PUT, `iss_dispatch_history`, duplicate check, approve to ISS | [TC_021](./TC_021.md) |
| 22 | Duplicate SMS — auto-stop, `deliveryEnabled` false, Teams / email / OpenSearch, recovery | [TC_022](./TC_022.md) |
| 23 | ARCH Soluto chat send/receive — Operator, Connect routing profile, URL, inquiry close (Tsukasapo) | [TC_023](./TC_023.md) |
| 24 | ARCH Soluto chat — Contact Hub from Mypage (same as TC_023 except steps 10–11) | [TC_024](./TC_024.md) |
| 25 | ARCH Soluto chat — Correspondence completed, Contact footer entry, IRIS case history | [TC_025](./TC_025.md) |
| 26 | ARCH Soluto chat — Automatic reply (au) outside business hours | [TC_026](./TC_026.md) |
| 27 | ARCH Soluto chat — Automatic reply (UQ) outside business hours | [TC_027](./TC_027.md) |
| 28 | ARCH chat — Notification (Push notification) | [TC_028](./TC_028.md) |
| 29 | ARCH chat — Notification (Snack bar) | [TC_029](./TC_029.md) |
| 30 | ARCH KFS chat — send/receive, Connect KFS routing, inquiry close (Kosapo path) | [TC_030](./TC_030.md) |
| 31 | ARCH KFS chat — Correspondence completed, Contact hub → Lost and stolen, IRIS case history | [TC_031](./TC_031.md) |
| 32 | ARCH KFS chat — Automatic reply (au) outside business hours | [TC_032](./TC_032.md) |
| 33 | ARCH KFS chat — Automatic reply (UQ) outside business hours | [TC_033](./TC_033.md) |
| 34 | ARCH KFS chat — Notification (Push notification) | [TC_034](./TC_034.md) |
| 35 | ARCH KFS chat — Notification (Snack bar) | [TC_035](./TC_035.md) |
| 37 | ARCH chat — App/ARCH two-way message visibility (Soluto + KFS) | [TC_037](./TC_037.md) |

---

**Pending your review (Sanjay):** [PENDING_REVIEW.md](./PENDING_REVIEW.md) — **Automation ID** / **Grade** set (**TC_021:** C10000, D; **TC_022:** SMS_TEMP_001, D); remaining checklist items as needed. **TC_023:** C00129, D; **TC_024:** C00131, D; **TC_025:** C00163, D; **TC_026:** C00322, D; **TC_027:** C00323, D; **TC_028:** C00077, D; **TC_029:** C00101, D; **TC_030:** C00239, D; **TC_031:** C00628, D; **TC_032:** C00629, D; **TC_033:** C00630, D; **TC_034:** C00631, D; **TC_035:** C00632, D (ARCH). **TC_037**: pending Automation ID/Grade.

**Adding more test cases:** Create `TC_038.md`, … in this folder and add a row above for each. For each new test case, provide **Automation ID** (e.g. C00549) and **Grade** (e.g. D) so they can be included in the document.

**Drafts:** Edit formal `TC_NNN.md` after promotion. **KFS push** (**TC_034**) and **KFS snack bar** (**TC_035**): no companion `DRAFT_ARCH_KFS_Notification_*` files unless Sanjay asks for one. **Pointers (entry points):** [DRAFT_SMS_Manual_Delivery_Titan_ISS.md](./DRAFT_SMS_Manual_Delivery_Titan_ISS.md), [DRAFT_SMS_Duplicate_Alert_AutoStop.md](./DRAFT_SMS_Duplicate_Alert_AutoStop.md) → **TC_021** / **TC_022**; [DRAFT_ARCH_KFS_Automatic_reply_au.md](./DRAFT_ARCH_KFS_Automatic_reply_au.md), [DRAFT_ARCH_KFS_Automatic_reply_UQ.md](./DRAFT_ARCH_KFS_Automatic_reply_UQ.md) → **TC_032** / **TC_033**. **KFS draft still in progress:** [DRAFT_ARCH_KFS_Test_Cases.md](./DRAFT_ARCH_KFS_Test_Cases.md) (consolidated reference). **KFS snack bar** is finalised as **TC_035** — no companion draft unless Sanjay asks. Update this README when that list changes.
