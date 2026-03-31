---
name: authoring-skills
description: Creates or updates a skill from the given instructions in a defined format. Use when the user asks to create a skill, update an existing skill's format, or author a new skill from instructions.
---

# Create or Update a Skill from Instructions

## Overview

This skill provides the steps to create or update a skill from given instructions so that the content follows a **defined format**.

### Purpose and context

- **Purpose**: Turn the instructions into a template so that creation and updates stay consistent.
- **Context**: Inconsistent formatting reduces discoverability and reusability of skills.
- **Out of scope**: Cases where the instructions are vague or lack concrete content.
- **Success criteria**:
  - Skill name (`name`) is in gerund form **○○ing-○○** (e.g. authoring-skills, writing-requirements)
  - `description` is in third person, specific, and includes trigger terms
  - SKILL.md body is 500 lines or fewer
  - Structure follows the template
  - Terminology is consistent

### Agent

- Structure content according to the template and best practices.
- If information is missing, organize what can be inferred and avoid over-guessing.
- Add reference files only when needed; link to them from SKILL.md at one level only.

### Input

- **Required**:
  - `instructions`: The content to create or update
  - `template_path`: The template to use (e.g. `assets/skill-template.md`)
- **Optional**:
  - `skill_path`: Directory of an existing skill or path to `SKILL.md`
  - `related_files`: Related files such as references, examples, or scripts
  - `constraints`: Naming or structure rules (skill name in gerund form ○○ing-○○ is recommended)

### Output

- **Deliverables**:
  - Updated `SKILL.md`
  - If needed: `reference.md`, `examples.md`, `scripts/`, etc.
- **Impact**:
  - Clearer description, structure, terminology, and references
- **How to confirm completion**:
  - Read SKILL.md and check that it meets the success criteria

### Steps (summary)

1. Review the instructions and the template
2. Decide whether this is a new skill or an update
3. Build the structure according to the template
4. Create or update SKILL.md and reference files
5. Verify against best practices

---

## Create/Update Process

### 1. Review the instructions and the template

- **Purpose**: Clarify what the skill should look like
- **Action**: Read the instructions and template and note required items
- **Decision**: If instructions are incomplete, fill in only what can be reasonably inferred
- **Check**: Confirm that the template’s required sections are understood
- **On failure**: If critical information is missing, record it as insufficient requirements

### 2. Decide whether this is a new skill or an update

- **Purpose**: Decide how much to reuse existing assets
- **Action**: Check whether `skill_path` exists and what it contains
- **Decision**: If `skill_path` exists, treat as update; otherwise, create new
- **Check**: Ensure the existing skill’s purpose aligns with the instructions
- **On failure**: If the purpose does not match, treat as new creation instead

### 3. Build the structure according to the template

- **Purpose**: Keep the format consistent
- **Action**:
  - Set `name` in gerund form **○○ing-○○** (e.g. authoring-skills, splitting-bilingual-specs)
  - Write `description` according to the rules (third person, trigger terms, max 1024 chars)
  - Place overview, purpose, input, output, and steps as in the template
- **Decision**: If content is long, split into reference files
- **Check**: Confirm all required sections from the template are present
- **On failure**: Add any missing structure

### 4. Create or update SKILL.md and reference files

- **Purpose**: Turn the instructions into concrete deliverables
- **Action**:
  - Write SKILL.md following the template
  - Create `reference.md` and/or `examples.md` if needed
  - Keep references one level deep from SKILL.md
- **Decision**: If references are not needed, keep only SKILL.md
- **Check**: Confirm there are no broken or duplicate links
- **On failure**: Reorganize references and retry

### 5. Verify

- **Purpose**: Confirm the result matches best practices
- **Action**: Go through the checklist
- **Decision**: If a criterion is not met, return to the relevant step
- **Check**:
  - `name` is in gerund form ○○ing-○○
  - `description` is in third person and within 1024 characters
  - SKILL.md body is 500 lines or fewer
  - Terminology is consistent
  - References are linked only one level deep
- **On failure**: Fix and verify again

---

## Reference

- Best practices: [Claude Agent Skills](https://docs.anthropic.com/en/docs/build-with-claude/agent-skills)
- Skill template: [skill-template.md](assets/skill-template.md)
- Usage example: [example.md](example.md)
