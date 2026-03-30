# DRAFT — Manual Test Cases: ARCH — Chat (KFS) — Notification (Push notification)

**Status:** Draft  
**Viewpoint:** Notification - Push notification  
**Purpose:** Verify OS push notification is received when ARCH sends message in KFS context.

---

## Test case (draft): KFS push notification

**Automation ID:** C00631  
**Grade:** D  
**Test Case ID:** ARCH-CHAT-KFS-NOTIFICATION-PUSH-001  
**Test Case Title:** Verify KFS push notification when ARCH sends message  
**Priority:** High

**Preconditions:**

- App not launched on device.
- Notification setting combination per scope.
- KFS skill selected in ARCH and routing profile is KFS.

**Test Steps:**

| Step | Action | Expected Result |
|------|--------|-----------------|
| 1 | Keep app closed on device. | App not active. |
| 2 | Open ARCH and ensure queue context is KFS. | Operator is ready on KFS. |
| 3 | Send message from ARCH to user session. | Message send succeeds. |
| 4 | Observe device without launching app. | Push notification is received. |

---

## Expected result (overall)

KFS-originated message generates OS push notification under expected conditions.

---

## Traceability (draft)

| Test Case ID | Category | Viewpoint | Purpose of test |
|--------------|----------|-----------|-----------------|
| ARCH-CHAT-KFS-NOTIFICATION-PUSH-001 | ARCH, Chat (KFS) | Notification - Push notification | Verify push notification for KFS chat messages |
