---
name: manual-test-cases
description: Generate structured manual test cases from features, user stories, or requirements. Use when the user asks for manual test cases, test scenarios, test plans, QA test cases, or validation steps for a feature or requirement. Always use this skill and reference SKILL.md and manual-test-cases-config.yaml from the skill folder.
---

# Manual Test Case Generation

## Portability

Use **relative paths or skill-folder-relative references** only. Do not use hard-coded local paths (e.g. `C:\Users\...` or `/Users/...`) so the skill works for all team members and environments.

## Independence from Authoring

This skill **operates independently**. It is used only for generating manual test cases from features, user stories, or requirements. Do **not** invoke the authoring-skills (meta-skill) when generating manual test cases—authoring-skills is for creating or updating other skills, not for test case generation.

## Mandatory Reference

**When generating manual test cases, always:**

1. **Use this file** as the source of instructions: **SKILL.md** (in this skill folder).

2. **Use the YAML config** for structure, template fields, and storage: **manual-test-cases-config.yaml** (in this skill folder).

3. **Read both files** from the manual-test-cases skill folder before generating test cases. Apply the template fields and conventions from the YAML. Save or suggest saving generated test cases to the path in the YAML (`storage.default_output_path`) or to a path the user specifies.

## When to Apply

Use this skill when the user wants:
- Manual test cases for a feature, user story, or requirement
- Test scenarios or test plan for QA
- Step-by-step validation or verification steps
- Coverage for positive, negative, or edge cases

## Instructions

### 1. Load Reference Files

- Read **SKILL.md** and **manual-test-cases-config.yaml** from the manual-test-cases skill folder (same folder as this file; use relative paths for portability).
- Use the YAML `template.fields` and `conventions` for IDs and structure.

### 2. Gather Input

Before generating, clarify if not obvious:
- **Scope**: Feature name, user story, or requirement text
- **Type**: Functional, UI, regression, smoke, or mixed
- **Depth**: Brief (smoke) vs detailed (full functional)

### 3. Output Structure

Generate each test case using the template from the YAML. Standard structure:

```markdown
**Test Case ID:** [Module]-[Number] (e.g., AUTH-001)
**Test Case Title:** [Short, action-oriented title]
**Priority:** High | Medium | Low
**Preconditions:** [Required state, data, or setup]
**Test Steps:**
| Step | Action | Expected Result |
|------|--------|-----------------|
| 1 | [Action] | [Expected outcome] |
| 2 | [Action] | [Expected outcome] |
**Test Data:** [If applicable]
**Postconditions:** [State after test, cleanup if needed]
```

### 4. Storage

- **Default**: Offer to save output to the path in the YAML (`storage.default_output_path`, e.g. `./test-cases`) with filename from `storage.default_filename` (e.g. `manual-test-cases.md` or `.yaml`).
- **User path**: If the user specifies a folder or file path, save (or provide content for) the generated test cases there.
- Store **SKILL.md** and **manual-test-cases-config.yaml** only in the skill folder; do not copy them to the output location unless the user asks.

### 5. Coverage Guidelines

- **Positive cases**: Happy path, valid inputs, expected flows
- **Negative cases**: Invalid inputs, error handling, boundary values
- **Edge cases**: Limits, empty/null, special characters, permissions
- **UI/UX**: Labels, navigation, accessibility where relevant

Include at least one positive and one negative scenario per distinct behavior.

### 6. Quality Rules

- Steps are atomic and repeatable; avoid "verify the system works"
- Expected results are specific and verifiable
- Preconditions list only what is required for this test
- Use consistent IDs (e.g., AUTH-001, AUTH-002) per YAML conventions

### 7. Optional Additions

- **Traceability**: Reference requirement or story ID in the test case
- **Risk**: Mark high-risk areas with High priority
- **Environment**: Note if a specific env or role is required

---

## Example: Login – Valid and Invalid Scenarios

**Input:** "Login with email and password"

### Valid scenario (positive)

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

### Invalid scenario (negative)

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

---

## Additional Resources

- For more templates and test types, see [reference.md](reference.md).
- For configuration and storage path, see [manual-test-cases-config.yaml](manual-test-cases-config.yaml).
- For login examples (valid and invalid), see [examples-login.md](examples-login.md).
