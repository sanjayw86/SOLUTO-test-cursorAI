# Manual Test Cases: Detailed Step-by-Step Flow

This guide has two parts:
- **Part A**: Using the skill to generate manual test cases (day-to-day use)
- **Part B**: Creating an AI skill for manual test cases from scratch (one-time setup)

---

# Part A: Generate Manual Test Cases (Step-by-Step)

## Overview

1. Open Cursor and ensure the skill is available.
2. Provide clear input (feature/requirement).
3. Ask the AI to generate test cases.
4. Review and refine.
5. Export or copy into your test tool.

---

## Step 1: Confirm the Skill Is Available

**What to do:**
- The skill lives in the **manual-test-cases** folder under your Cursor skills directory (e.g. `~/.cursor/skills/manual-test-cases/` or project `.cursor/skills/manual-test-cases/`).
- Cursor loads skills from `~/.cursor/skills/` (or project `.cursor/skills/`) automatically. No extra setup.

**Check (optional):**
- In Cursor, start a new chat and ask: *"Generate manual test cases for a simple login with email and password."*
- If you get structured test cases (with Test Case ID, Steps, Expected Results), the skill is in use.

---

## Step 2: Prepare Your Input

**What the AI needs:**
- **Scope**: What to test (feature, user story, requirement, or screen).
- **Optional**: Type of tests (functional, UI, smoke) and depth (quick vs detailed).

**Examples of good input:**

| You provide | AI can generate |
|-------------|------------------|
| "Login with email and password" | Positive, negative, and edge cases for login |
| "Checkout flow: cart → address → payment → order confirmation" | End-to-end test cases for the flow |
| "User profile: edit name, email, change password" | Test cases per sub-feature |
| "API: Create order (POST /orders) with validation" | Manual test cases (request/response, error codes) |

**Tips:**
- Paste the exact user story or requirement text if you have it.
- Mention constraints: "Only happy path" or "Include negative and boundary cases."

---

## Step 3: Ask the AI (Exact Prompts)

**3a. Basic request**
```
Generate manual test cases for [your feature/requirement].
```
Example: *"Generate manual test cases for forgot password flow: user enters email, receives link, resets password."*

**3b. With test type**
```
Create [functional / UI / smoke] manual test cases for [feature].
```
Example: *"Create smoke manual test cases for the dashboard after login."*

**3c. With coverage**
```
Generate manual test cases for [feature]. Include positive, negative, and edge cases.
```
Example: *"Generate manual test cases for user registration. Include positive, negative, and edge cases."*

**3d. From a user story**
```
Here is the user story: [paste story]. Generate manual test cases for it.
```

**3e. With format preference**
```
Generate manual test cases for [feature] in a table format with Test Case ID, Steps, and Expected Results.
```

Use one of these as a template and replace the bracketed parts with your scope.

---

## Step 4: Review the Generated Test Cases

**Checklist:**

1. **IDs**  
   - Format consistent? (e.g. AUTH-001, AUTH-002)  
   - Match your project’s convention if you have one.

2. **Steps**  
   - One clear action per step.  
   - Expected results specific and verifiable (e.g. "Error message: Invalid email" not "Shows error").

3. **Coverage**  
   - At least one positive and one negative scenario per behavior.  
   - Critical flows (e.g. login, payment) marked High priority.

4. **Preconditions**  
   - Only what’s needed for that test (e.g. "User on login page", "Valid account exists").

**If something is wrong:**
- "Make the expected results more specific."
- "Add negative test cases for invalid email format."
- "Use our ID format: PROJ-MODULE-001."

---

## Step 5: Use the Test Cases

**Options:**
- **Copy**: Select the markdown in the chat and paste into Confluence, Notion, or a doc.
- **Export**: Copy into Excel/Google Sheets (one row per step or per test case, as you prefer).
- **Test management**: Import or type into your tool (e.g. Jira, TestRail, Zephyr) using the same fields (ID, Title, Steps, Expected Result, Priority).

**Flow summary:**

```
Prepare input → Open Cursor chat → Paste requirement/feature
    → Ask "Generate manual test cases for..."
    → Review (IDs, steps, coverage)
    → Refine with follow-up if needed
    → Copy/export into your doc or test tool
```

---

# Part B: Create an AI Skill for Manual Test Cases (Step-by-Step)

Use this when you want to create or customize a skill from scratch (e.g. different template or company format).

---

## Step 1: Decide Location and Name

**Location:**
- **Personal** (all your projects): `~/.cursor/skills/` or `%USERPROFILE%\.cursor\skills\`
- **Project** (one repo only): `<your-project>\.cursor\skills\`

**Name:**  
Use lowercase, hyphens, no spaces. Examples: `manual-test-cases`, `qa-test-templates`.

**Action:**  
Create folder:  
`<skills-dir>/<skill-name>/`  
Example: `<skills-dir>/manual-test-cases/`

---

## Step 2: Create SKILL.md with Frontmatter

**2a. Create the file**  
Path: `<skill-folder>/SKILL.md` (e.g. `manual-test-cases/SKILL.md` inside your skills directory)

**2b. Add YAML frontmatter at the top:**

```yaml
---
name: manual-test-cases
description: Generate structured manual test cases from features, user stories, or requirements. Use when the user asks for manual test cases, test scenarios, test plans, QA test cases, or validation steps for a feature or requirement.
---
```

**Rules:**
- `name`: lowercase, letters, numbers, hyphens only; max 64 characters.
- `description`: What the skill does (WHAT) + when to use it (WHEN). Write in third person. Include trigger phrases like "manual test cases", "test scenarios", "test plan".

---

## Step 3: Add "When to Apply" Section

**Purpose:** Tell the AI when this skill is relevant.

**Example:**

```markdown
# Manual Test Case Generation

## When to Apply

Use this skill when the user wants:
- Manual test cases for a feature, user story, or requirement
- Test scenarios or test plan for QA
- Step-by-step validation or verification steps
- Coverage for positive, negative, or edge cases
```

You can add or remove bullet points to match how your team talks about testing.

---

## Step 4: Define the Output Template

**Purpose:** So every test case has the same structure.

**Example:**

```markdown
## Output Structure

Generate each test case using this template:

**Test Case ID:** [Module]-[Number] (e.g., AUTH-001)
**Test Case Title:** [Short, action-oriented title]
**Priority:** High | Medium | Low
**Preconditions:** [Required state, data, or setup]
**Test Steps:**
| Step | Action | Expected Result |
|------|--------|-----------------|
| 1 | [Action] | [Expected outcome] |
**Test Data:** [If applicable]
**Postconditions:** [State after test]
```

**Customize:**  
Change fields to match your tool (e.g. add "Component", "Assignee", "Requirement ID"). Keep the table for steps so the AI stays consistent.

---

## Step 5: Add Coverage and Quality Rules

**Purpose:** Define what “good” test cases mean (coverage + quality).

**Example:**

```markdown
## Coverage Guidelines

- **Positive cases**: Valid inputs, happy path
- **Negative cases**: Invalid inputs, error handling, boundaries
- **Edge cases**: Limits, empty/null, special characters
- Include at least one positive and one negative per behavior

## Quality Rules

- Steps are atomic and repeatable
- Expected results are specific and verifiable
- Preconditions list only what is required for this test
- Use consistent IDs (e.g., MODULE-001, MODULE-002)
```

Adjust to your process (e.g. "always include a security test case for auth flows").

---

## Step 6: Add at Least One Full Example

**Purpose:** The AI mimics structure and style from examples.

**Example:** One positive and one negative test case, using your template (ID, Title, Priority, Preconditions, Steps, Expected Results, Test Data, Postconditions).  
See the existing `SKILL.md` in `manual-test-cases` for the login example.

**Tip:** Add 1–2 examples that match your real projects (e.g. your module names, your priority labels).

---

## Step 7: Add Optional Reference File

**Purpose:** Keep SKILL.md short; put details in another file.

**Create:**  
`<skill-folder>/reference.md`

**Contents (examples):**
- Test types (functional, UI, smoke, regression)
- Priority definitions (High/Medium/Low)
- Step-writing tips
- How you do traceability (e.g. Requirement ID ↔ Test Case ID)

**In SKILL.md**, add at the end:

```markdown
## Additional Resources

- For more templates and test types, see [reference.md](reference.md).
```

---

## Step 8: Verify the Skill

**Checklist:**

1. **File path**  
   - `SKILL.md` is inside `...\skills\manual-test-cases\` (or your chosen name).

2. **Frontmatter**  
   - `name` and `description` are correct; description has trigger phrases.

3. **Length**  
   - SKILL.md under ~500 lines (use reference.md for long content).

4. **Test**  
   - New Cursor chat → "Generate manual test cases for [a simple feature]."  
   - Confirm output matches your template and looks usable.

---

## End-to-End Flow (Summary)

**Part A – Using the skill:**  
Prepare input → Open Cursor → Ask with a clear prompt → Review → Refine → Copy/export to doc or test tool.

**Part B – Creating the skill:**  
Choose folder and name → Create SKILL.md with frontmatter → Add "When to Apply" → Define output template → Add coverage and quality rules → Add 1–2 examples → Optionally add reference.md → Verify with a sample request.

If you tell me your tool (e.g. Jira, TestRail) or your company’s test case format, the steps can be tailored to that (e.g. exact field names and a ready-to-paste template).
