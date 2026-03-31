# Manual Test Cases – Reference

## Test Case Types

| Type | Focus | When to Use |
|------|--------|-------------|
| Functional | Feature behavior, inputs/outputs | Core feature validation |
| UI | Layout, labels, navigation, responsiveness | Screens and flows |
| Negative | Invalid input, errors, boundaries | Robustness |
| Smoke | Critical path only | Quick sanity after deploy |
| Regression | Existing behavior unchanged | After code/config changes |

## Priority Guidelines

- **High**: Critical path, security, data integrity, blocking bugs
- **Medium**: Important flows, common user actions
- **Low**: Rare paths, cosmetic, nice-to-have

## Step Writing Tips

- One action per step; one expected result per step
- Use "Verify that..." or "Confirm that..." for checks
- Avoid vague expectations: use "Error message X is displayed" not "App shows error"

## Common Test Data Notes

- **Valid**: Document example values (e.g., test@example.com)
- **Invalid**: Document what makes it invalid (e.g., empty, wrong format)
- **Boundary**: Min/max length, zero, special characters

## Traceability (Optional)

Link test cases to requirements:

```
Requirement ID: REQ-101
Test Cases: AUTH-001, AUTH-002, AUTH-003
```

Use when the user needs coverage mapping or audit trail.
