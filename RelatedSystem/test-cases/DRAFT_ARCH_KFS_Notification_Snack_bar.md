# DRAFT — Manual Test Cases: ARCH — Chat (KFS) — Notification (Snack bar)

**Status:** Draft  
**Viewpoint:** Notification - Snack bar  
**Purpose:** Verify snack-bar notification display behavior for KFS message reception.

---

## Test case (draft): KFS snack-bar notification

**Automation ID:** C00632  
**Grade:** D  
**Test Case ID:** ARCH-CHAT-KFS-NOTIFICATION-SNACKBAR-001  
**Test Case Title:** Verify KFS snack-bar notification display behavior  
**Priority:** High

**Preconditions:**

- App launched and user can navigate target pages.
- KFS queue context active.
- In-app notification settings per scope.

**Test Steps:**

| Step | Action | Expected Result |
|------|--------|-----------------|
| 1 | Keep app on target page for snack-bar verification. | App ready for in-app notification observation. |
| 2 | Send message from ARCH in KFS context. | Message is delivered. |
| 3 | Verify snack bar display on allowed page(s). | Snack bar appears where expected. |
| 4 | Verify non-display on excluded pages (if defined by requirement). | Snack bar not shown on excluded pages. |

---

## Expected result (overall)

Snack-bar display behavior matches KFS notification design.

---

## Traceability (draft)

| Test Case ID | Category | Viewpoint | Purpose of test |
|--------------|----------|-----------|-----------------|
| ARCH-CHAT-KFS-NOTIFICATION-SNACKBAR-001 | ARCH, Chat (KFS) | Notification - Snack bar | Verify snack-bar behavior for KFS chat messages |
