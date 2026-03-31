# Skill Template

Use this structure when creating or updating a skill from instructions.

## Required sections

1. **YAML frontmatter**
   - `name`: lowercase, hyphens, gerund form ○○ing-○○ (max 64 chars)
   - `description`: third person, specific, trigger terms (max 1024 chars)

2. **Overview**
   - What the skill does and when to use it

3. **Purpose / Context** (optional but recommended)
   - Purpose, background, out-of-scope, success criteria

4. **Input**
   - Required: instructions, template_path (or equivalent)
   - Optional: skill_path, related_files, constraints

5. **Output**
   - Deliverables (SKILL.md, reference.md, etc.)
   - How to confirm completion

6. **Steps or process**
   - Numbered steps or sub-sections with Purpose, Action, Decision, Check, On failure

7. **Reference**
   - Links to template, examples, best practices (one level deep from SKILL.md)

## File layout

```
skill-name/
├── SKILL.md           # Required
├── reference.md       # Optional
├── examples.md        # Optional
├── example.md         # Optional
└── assets/            # Optional
    └── skill-template.md
```

## Naming

- Skill name: **○○ing-○○** (e.g. authoring-skills, writing-requirements)
- Directory: same as `name` in frontmatter
