# DRAFT — Manual Test Cases: ARCH — Chat (KFS) suite

**Status:** Draft  
**Reference alignment:** Structure and wording style follow ARCH test cases `TC_023` through `TC_029` (Source/Viewpoint, Preconditions, Environments, phased steps, Expected result, Test Data, Note, Postconditions, Traceability).  
**Scope:** KFS scenarios using skill **[故] Chat (KFS)**.

---

## Common environment references

| Layer | Purpose | URLs / notes |
|--------|---------|----------------|
| **ARCH** | Operator UI | **SQA1:** `https://acyan-sqa1.uap.jpnmob-acyan.npr.aws.asurion.net/techarch/` **SQA3:** `https://acyan-sqa3.uap.jpnmob-acyan.npr.aws.asurion.net/techarch` **SQA4:** `https://acyan-sqa4.uap.jpnmob-acyan.npr.aws.asurion.net/techarch/` **SQA5:** `https://acyan-sqa5.uap.jpnmob-acyan.npr.aws.asurion.net/techarch/` **UAT1:** `https://acyan-uat.uap.jpnmob-acyan.npr.aws.asurion.net/techarch` **UAT2:** `https://acyan-uat2.uap.jpnmob-acyan.npr.aws.asurion.net/techarch` |
| **Amazon Connect** | Routing profile / agent status | **SQA:** `https://uap-acyan-sqa1-jpmob-telephony.my.connect.aws/home` **UAT:** `https://uap-acyan-uat-jpmob-telephony.my.connect.aws/home` |
| **App** | Tsukasapo / Kosapo | Build must match ARCH + Connect line |

---

## Draft 1 — Chat send and receive (KFS)

**Automation ID:** C00239  
**Grade:** D  
**Test Case ID:** ARCH-CHAT-KFS-SENDRECV-001  
**Test Case Title:** Verify KFS chat send/receive and closure with inquiry fields  
**Priority:** High  
**Viewpoint:** Chat send and receive

**Preconditions:**

- **User profile:** Kosapo Android
- `serviceEnabled: true`
- `kfsServiceEnabled: true`
- `enrolledModelCode: "(Android model)"`
- `appleSubscriptionEnabled: false`
- `brand: AU`
- **Skill selection (ARCH):** **[故] Chat (KFS)**
- **Browser:** Chrome for ARCH.

**Test Steps:**

### Phase A — App entry and chat open

| Step | Action | Expected Result |
|------|--------|-----------------|
| 1 | Click **破損・盗難・紛失 お手続き** tile on **My page**. | KFS entry screen opens. |
| 2 | Click **チャットでご相談 (Start chat)**. | Chat opens. |

### Phase B — ARCH and routing readiness

| Step | Action | Expected Result |
|------|--------|-----------------|
| 3 | Open **ARCH** (same line as app), sign in as Operator. | ARCH opens and operator can operate the queue. |
| 4 | Open **Amazon Connect** dashboard page. | Connect dashboard opens. |
| 5 | Search your username in **User management**. | User is found. |
| 6 | Change routing profile to **KFS**. | KFS routing profile is set. |
| 7 | Click **OK** button (or Save equivalent) to confirm. | Profile update is persisted. |
| 8 | Set status to **応答可能 (Responsible)**. | Agent is available to receive chat. |

### Phase C — Send/receive and close

| Step | Action | Expected Result |
|------|--------|-----------------|
| 9 | Send a message from mobile side. | Message appears on ARCH and is deliverable both ways. |
| 10 | Click **完了する** at top-right on ARCH. | Wrap-up flow starts. |
| 11 | Select **問合せ区分1**, **問合せ区分2**, **終了理由**, **NPS自己評価**. | Mandatory closure fields are selected. |
| 12 | Click **OK** button. | Conversation closes successfully. |

**Expected result (overall):**
- KFS chat works end-to-end (mobile <-> ARCH) and closes with required fields.

**Traceability (draft):**
- `ARCH-CHAT-KFS-SENDRECV-001` | ARCH, Chat (KFS) | Chat send and receive

---

## Draft 2 — Correspondence completed (KFS)

**Automation ID:** C00628  
**Grade:** D  
**Test Case ID:** ARCH-CHAT-KFS-CORRESPONDENCE-001  
**Test Case Title:** Verify KFS correspondence can be completed successfully  
**Priority:** High  
**Viewpoint:** Correspondence completed

**Preconditions:**

- KFS route and operator setup same as Draft 1.
- Active chat session exists in KFS queue.
- Operator has rights to complete correspondence.

**Test Steps:**

| Step | Action | Expected Result |
|------|--------|-----------------|
| 1 | Accept/open the KFS chat on ARCH. | Session opens without error. |
| 2 | Exchange at least one message with user. | Two-way chat works. |
| 3 | Click **完了する**. | Wrap-up starts. |
| 4 | Fill required completion fields (問合せ区分1/2, 終了理由, NPS自己評価). | Required fields valid. |
| 5 | Click **OK** to complete. | Correspondence is completed and closed. |

**Expected result (overall):**
- KFS conversation can be completed cleanly with mandatory fields.

**Traceability (draft):**
- `ARCH-CHAT-KFS-CORRESPONDENCE-001` | ARCH, Chat (KFS) | Correspondence completed

---

## Draft 3 — Automatic reply - au (KFS)

**Automation ID:** C00629  
**Grade:** D  
**Test Case ID:** ARCH-CHAT-KFS-AUTOREPLY-AU-001  
**Test Case Title:** Verify KFS automatic reply (au) outside business hours  
**Priority:** High  
**Viewpoint:** Automatic reply - au

**Preconditions:**

- au target user prepared for KFS chat route.
- Test executed outside applicable business hours.
- KFS skill/routing selected.

**Test Steps:**

| Step | Action | Expected Result |
|------|--------|-----------------|
| 1 | Open KFS chat entry path on app and start chat. | Chat starts in KFS context. |
| 2 | Send a message outside business hours. | Automatic reply for **au** is displayed. |
| 3 | Confirm the flow remains in KFS queue context on ARCH. | Session routing is KFS. |
| 4 | Close chat after verification. | Conversation ends normally. |

**Expected result (overall):**
- au overtime auto-reply is displayed and KFS route stays correct.

**Traceability (draft):**
- `ARCH-CHAT-KFS-AUTOREPLY-AU-001` | ARCH, Chat (KFS) | Automatic reply - au

---

## Draft 4 — Automatic reply - uq (KFS)

**Automation ID:** C00630  
**Grade:** D  
**Test Case ID:** ARCH-CHAT-KFS-AUTOREPLY-UQ-001  
**Test Case Title:** Verify KFS automatic reply (UQ) outside business hours  
**Priority:** High  
**Viewpoint:** Automatic reply - uq

**Preconditions:**

- UQ target user prepared for KFS chat route.
- Test executed outside applicable business hours.
- KFS skill/routing selected.

**Test Steps:**

| Step | Action | Expected Result |
|------|--------|-----------------|
| 1 | Open KFS chat entry path on app and start chat. | Chat starts in KFS context. |
| 2 | Send a message outside business hours. | Automatic reply for **UQ** is displayed. |
| 3 | Confirm the flow remains in KFS queue context on ARCH. | Session routing is KFS. |
| 4 | Close chat after verification. | Conversation ends normally. |

**Expected result (overall):**
- UQ overtime auto-reply is displayed and KFS route stays correct.

**Traceability (draft):**
- `ARCH-CHAT-KFS-AUTOREPLY-UQ-001` | ARCH, Chat (KFS) | Automatic reply - uq

---

## Draft 5 — Notification - Push notification (KFS)

**Automation ID:** C00631  
**Grade:** D  
**Test Case ID:** ARCH-CHAT-KFS-NOTIFICATION-PUSH-001  
**Test Case Title:** Verify KFS push notification when ARCH sends message  
**Priority:** High  
**Viewpoint:** Notification - Push notification

**Preconditions:**

- App not launched on device.
- Notification setting combination as required by test scope.
- KFS skill selected in ARCH and routing profile is KFS.

**Test Steps:**

| Step | Action | Expected Result |
|------|--------|-----------------|
| 1 | Keep app closed on device. | App not active. |
| 2 | Open ARCH and ensure queue context is KFS. | Operator is ready on KFS. |
| 3 | Send message from ARCH to user session. | Message send succeeds. |
| 4 | Observe device without launching app. | Push notification is received. |

**Expected result (overall):**
- KFS-originated message generates OS push notification under expected conditions.

**Traceability (draft):**
- `ARCH-CHAT-KFS-NOTIFICATION-PUSH-001` | ARCH, Chat (KFS) | Notification - Push notification

---

## Draft 6 — Notification - Snack bar (KFS)

**Automation ID:** C00632  
**Grade:** D  
**Test Case ID:** ARCH-CHAT-KFS-NOTIFICATION-SNACKBAR-001  
**Test Case Title:** Verify KFS snack-bar notification display behavior  
**Priority:** High  
**Viewpoint:** Notification - Snack bar

**Preconditions:**

- App launched and user can navigate target pages.
- KFS queue context active.
- In-app notification settings per test scope.

**Test Steps:**

| Step | Action | Expected Result |
|------|--------|-----------------|
| 1 | Keep app on target page for snack-bar verification. | App ready for in-app notification observation. |
| 2 | Send message from ARCH in KFS context. | Message is delivered. |
| 3 | Verify snack bar display on allowed page(s). | Snack bar appears where expected. |
| 4 | Verify non-display on excluded pages (if defined by requirement). | Snack bar not shown on excluded pages. |

**Expected result (overall):**
- Snack bar display behavior matches KFS notification design.

**Traceability (draft):**
- `ARCH-CHAT-KFS-NOTIFICATION-SNACKBAR-001` | ARCH, Chat (KFS) | Notification - Snack bar

---

## Notes

- These are detailed drafts for KFS track; finalize into `TC_030.md` onward when you confirm each scenario.
- Keep this consolidated file only during drafting; remove once individual TC files are finalized (unless you request to retain).
