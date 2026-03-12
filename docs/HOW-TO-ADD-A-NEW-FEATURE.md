# How to Add a New Feature (Step-by-Step)

Use this so **everyone** adds features the same way.

---

## Standard structure

```
SOLUTO/
├── RelatedSystem/
│   └── test-cases/
│       ├── README.md
│       ├── TC_001.md
│       └── ...
├── <NewFeature>/
│   └── test-cases/
│       ├── README.md
│       ├── TC_001.md    ← First test case = TC_001
│       └── ...
├── docs/
└── scripts/
```

**Rule:** One feature = one folder under `SOLUTO/`. Each feature has its own `test-cases/` with README + TC_001, TC_002, … (sequence by order you create them).

---

## Step-by-step: Add a new feature

1. **Create folder** `SOLUTO/<FeatureName>/` (e.g. `SOLUTO/LoginFlow/`).
2. **Create folder** `SOLUTO/<FeatureName>/test-cases/`.
3. **Add** `test-cases/README.md` — copy from RelatedSystem, change feature name and table (start with one row for TC_001).
4. **Add** `test-cases/TC_001.md` — first test case for this feature gets number **001**. Use same template (Title, Priority, Preconditions, Steps table, Test Data, Postconditions).
5. **More test cases:** Create `TC_002.md`, `TC_003.md`, …; add a row in README for each. Sequence = order you create (002, 003, …).
6. **(Optional)** Add the new feature to `SOLUTO/README.md`.

---

## Sequence numbers

| When | File | Sequence |
|------|------|----------|
| First test case in a feature | TC_001.md | 001 |
| Second | TC_002.md | 002 |
| Third | TC_003.md | 003 |
| … | … | … |

Same for every feature: first TC = 001, next = 002, and so on.
