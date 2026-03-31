# Login – Manual Test Case Examples

## Valid scenario (positive)

**Test Case ID:** AUTH-001  
**Test Case Title:** Successful login with valid credentials  
**Priority:** High  
**Preconditions:** User is on login page; valid account exists.  
**Test Steps:**

| Step | Action | Expected Result |
|------|--------|-----------------|
| 1 | Enter valid email in Email field | Email is accepted; no error message |
| 2 | Enter valid password in Password field | Password is masked (e.g. bullets) |
| 3 | Click Sign In | User is redirected to dashboard/home; session is created |
| 4 | Verify user name or profile visible | Logged-in state is displayed |

**Test Data:** email: test@example.com, password: ValidPass1!  
**Postconditions:** User is logged in; logout option is available.

---

## Invalid scenario (negative)

**Test Case ID:** AUTH-002  
**Test Case Title:** Login fails with invalid password  
**Priority:** High  
**Preconditions:** User is on login page; valid email is known.  
**Test Steps:**

| Step | Action | Expected Result |
|------|--------|-----------------|
| 1 | Enter valid email in Email field | Email is accepted |
| 2 | Enter incorrect password in Password field | Password is accepted in field (masked) |
| 3 | Click Sign In | Error message displayed (e.g. "Invalid email or password"); user remains on login page |
| 4 | Verify session not created | No session cookie or token; user must retry |

**Test Data:** email: test@example.com, password: WrongPass123  
**Postconditions:** User remains on login page; can re-enter credentials; no partial login state.
