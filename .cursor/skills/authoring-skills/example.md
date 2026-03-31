# Example: Using the authoring-skills process

## Request

"Create a skill that generates manual test cases from a feature description."

## What the agent does

1. **Review instructions and template**  
   Uses `assets/skill-template.md` and the user’s instructions.

2. **New vs update**  
   No `skill_path` → treat as new skill.

3. **Structure**  
   - `name`: e.g. `generating-manual-test-cases` (gerund form)  
   - `description`: third person, e.g. "Generates manual test cases from feature descriptions. Use when the user asks for test cases, test scenarios, or test plans."  
   - Sections: Overview, Input, Output, Process, Reference.

4. **Create SKILL.md**  
   Writes SKILL.md with the template structure and links to reference.md or examples if needed.

5. **Verify**  
   Checks name format, description length, line count, terminology, and link depth.

## Result

A new skill in `~/.cursor/skills/generating-manual-test-cases/` (or project path) with SKILL.md and any reference or example files.
