# Manual Test Cases Skill

This skill teaches Cursor how to generate structured manual test cases from features, user stories, or requirements.

## Folder location
This skill lives in the **manual-test-cases** folder under your Cursor skills directory (e.g. `~/.cursor/skills/manual-test-cases/` or `<project>/.cursor/skills/manual-test-cases/`). Use relative paths so it works for all team members.

## Files in this folder

| File | Purpose |
|------|---------|
| **SKILL.md** | Main skill instructions; Cursor uses this when you ask for manual test cases |
| **manual-test-cases-config.yaml** | Template, storage path, ID conventions; read by the agent |
| **reference.md** | Test types, priorities, step-writing tips |
| **examples-login.md** | Valid and invalid login test case examples |
| **HOW-TO-USE-AND-CUSTOMIZE.md** | How to use the skill and customize templates/IDs |
| **STEP-BY-STEP-GUIDE.md** | Detailed flow for using and creating the skill |
| **README.md** | This file |

## Quick use
In any Cursor chat, say for example:
- *"Generate manual test cases for the password reset flow."*
- *"Create test scenarios for checkout. Include negative cases."*

No extra setup; Cursor loads skills from `~/.cursor/skills/` automatically.
