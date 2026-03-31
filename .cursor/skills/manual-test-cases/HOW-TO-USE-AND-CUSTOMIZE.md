# How to Use & Customize the Manual Test Cases Skill

## How to Use It

### 1. In any project

- Open Cursor and start a chat (no need to open the skill files).
- Cursor loads skills from `~/.cursor/skills/` automatically — no extra setup.

### 2. Ask in natural language

**Examples:**

- *"Generate manual test cases for the password reset flow."*
- *"Create test scenarios for the checkout process."*
- *"Write manual test cases for user registration."*

### 3. Optional refinements

Add one of these to your message:

- *"Include negative cases"* — invalid inputs, errors, boundaries
- *"Keep it to smoke tests only"* — critical path, fewer cases
- *"Include edge cases"* — limits, empty values, special characters
- *"Add UI test cases"* — labels, navigation, layout

**Example combined:**  
*"Generate manual test cases for the password reset flow. Include negative cases."*

---

## Customizing the Skill

Skill files are in the **manual-test-cases** skill folder (the same folder that contains this file). Use relative paths for portability.

| Goal | What to edit | Where |
|------|----------------|-------|
| **Change output format** (fields, table layout) | "Output Structure" section + example | `SKILL.md` |
| **Your ID scheme** (e.g. PROJ-MODULE-001) | Template and quality rules | `SKILL.md` |
| **Naming rules** (titles, modules) | Coverage/quality rules or new subsection | `SKILL.md` |
| **Link to test tool** (Jira, TestRail, etc.) | Add a short "Export" or "Tool" section | `SKILL.md` |
| **More sample test cases** | Add full examples in the same format | `examples.md` (create and link from SKILL.md) |

### Templates

- Open **SKILL.md**.
- Find **"Output Structure"** (the block with Test Case ID, Title, Steps table, etc.).
- Edit field names, add/remove columns (e.g. Component, Requirement ID), or change the steps table to match your team’s format.
- Update the **example** test cases in the same file so they use the new structure.

### Conventions (IDs and naming)

- In **SKILL.md**, search for "Test Case ID" and "MODULE-001".
- Replace with your scheme, e.g. `PROJ-MODULE-001` or `TC-LOGIN-01`.
- Optionally add a short "Conventions" list: ID format, priority names, module names.

### More examples

- Create **examples.md** in the same folder as **SKILL.md**.
- Paste 2–3 full test cases in your desired format.
- In **SKILL.md**, under "Additional Resources", add:  
  *"For more examples, see [examples.md](examples.md)."*

### Tool-specific format (Excel, Jira, TestRail)

If you want columns or fields for a specific tool:

1. In **SKILL.md**, change the "Output Structure" so the fields match that tool (e.g. Summary, Steps, Expected Result, Priority).
2. Optionally add a line like: *"Format test cases for import into [Tool name]: use these column names: …"*

If you share your preferred format (e.g. Excel column names or a sample), the skill text can be adjusted to match it.
