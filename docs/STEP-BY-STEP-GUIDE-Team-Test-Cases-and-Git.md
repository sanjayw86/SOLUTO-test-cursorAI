# Step-by-Step Guide: Project Setup, Test Cases & Git for the Team

This guide walks you from creating a project through writing manual test cases, storing them, and sharing with the team via Git so everyone stays on the same page.

---

## Part 1: Project & Folder Structure (SOLUTO)

### Step 1.1: Open the project

- Open **SOLUTO** in Cursor: **File → Open Folder** → select the `SOLUTO` folder.
- **Project root** = the SOLUTO folder (e.g. `c:\Users\...\SOLUTO`).

---

### Step 1.2: Standard folder structure (everyone uses this)

```
SOLUTO/
├── <Feature_Name>/           ← e.g. RelatedSystem, LoginFlow
│   └── test-cases/
│       ├── README.md         ← Feature index (list of TCs)
│       ├── TC_001.md
│       ├── TC_002.md
│       └── ...
├── docs/                     ← Guides (this file lives here)
└── scripts/
```

**Rule:** One feature = one folder under `SOLUTO/`. Each feature has its own `test-cases/` folder with README + TC_001, TC_002, …

---

### Step 1.3: Project index

- **SOLUTO/README.md** lists all features and links to each feature’s test-cases.
- When you add a new feature, add a row there (see docs/HOW-TO-ADD-A-NEW-FEATURE.md).

---

## Part 2: Features and Where to Write Manual Test Cases

### Step 2.1: One folder per feature

- **One feature** = **one folder** under `SOLUTO/` (e.g. `SOLUTO/RelatedSystem/`).
- **Test cases for that feature** = files in `SOLUTO/<Feature>/test-cases/`: `TC_001.md`, `TC_002.md`, …

### Step 2.2: First test case = TC_001

- The **first** test case in a feature is always **TC_001.md**.
- The next is **TC_002.md**, then **TC_003.md**, and so on (sequence by order you create them).

### Step 2.3: How to write each test case (TC_XXX.md)

Use this structure (same for all team members):

```markdown
# TC_001 — <Short title>

**Test Case ID:** SOLUTO-<MODULE>-001  
**Title:** <One-line title>  
**Priority:** High | Medium | Low  
**Preconditions:** <What must be true before steps>

**Test Steps:**

| Step | Action | Expected Result |
|------|--------|-----------------|
| 1 | <What to do> | <What should happen> |
| 2 | ... | ... |

**Test Data:** <If needed>  
**Postconditions:** <State after test>
```

**Rules:**
- One main action per step.
- Expected result = specific and verifiable.
- Use the same format for every TC.

### Step 2.4: Adding more test cases

- Create **TC_002.md**, **TC_003.md**, … in the same `test-cases/` folder.
- Add a row in that feature’s **test-cases/README.md** for each new TC.

---

## Part 3: Storing Test Cases & Making Them Useful to the Team

### Step 3.1: Where they are stored

- **Location:** `SOLUTO/<Feature>/test-cases/`.
- **Format:** Markdown (`.md`).
- **Structure:** Same for everyone (Feature → test-cases → README + TC_001, TC_002, …).

### Step 3.2: How this helps other members

- Same structure → everyone knows where to find or add TCs.
- README in each feature’s test-cases → quick index.
- Numbered TCs → easy to refer to (“run TC_003”).
- Git → one source of truth.

---

## Part 4: Git – Repository, Commit, Push, Pull

### Step 4.1: Initialize Git (one-time)

1. Open terminal in Cursor (**Ctrl+`**).
2. Go to project root:
   ```bash
   cd c:\Users\sanjay.waghmare\SOLUTO
   ```
3. If Git is not yet initialized:
   ```bash
   git init
   ```
4. Add a **.gitignore** (e.g. `node_modules/`, `.env`, `*.log`, `.cursor/`). Keep `docs/` and feature folders tracked.

### Step 4.2: Create a repository on GitHub / GitLab / Azure Repos

1. Create a **new repository** (e.g. `SOLUTO`).
2. Do **not** initialize with a README if you already have the folder.
3. Copy the **repository URL**.

### Step 4.3: Connect local project to remote

```bash
git remote add origin https://github.com/YourOrg/SOLUTO.git
```

(Use your actual URL. If `origin` exists: `git remote set-url origin <URL>`.)

### Step 4.4: First commit and push

```bash
git add .
git commit -m "Initial: SOLUTO project structure and test cases"
git branch -M main
git push -u origin main
```

### Step 4.5: Daily workflow – you (author)

When you add or change test cases:

```bash
git add .
git commit -m "Add TC_002 for RelatedSystem"
git push
```

### Step 4.6: How other members get your test cases

**First time:** They clone the repo and open the SOLUTO folder in Cursor.

**Later:** They run `git pull` to get your latest changes.

### Step 4.7: Keeping the team on the same page

| Who     | Action       | Command / Habit                    |
|---------|--------------|-------------------------------------|
| You     | Share changes| `git add` → `git commit` → `git push` |
| Others  | Get your work| `git pull`                          |
| Everyone| Same structure | Use `SOLUTO/<Feature>/test-cases/TC_XXX.md` and update README when adding TCs |

---

## Part 5: Quick Reference – Paths and Commands

### Paths (SOLUTO)

| What        | Path example                          |
|-------------|----------------------------------------|
| Project root| `SOLUTO/`                             |
| One feature | `SOLUTO/RelatedSystem/`               |
| Test cases  | `SOLUTO/RelatedSystem/test-cases/`   |
| One TC      | `SOLUTO/RelatedSystem/test-cases/TC_001.md` |

### Git commands (copy-paste)

```bash
# First-time setup (you)
cd c:\Users\sanjay.waghmare\SOLUTO
git init
git remote add origin <YOUR_REPO_URL>
git add .
git commit -m "Initial: project structure and test cases"
git branch -M main
git push -u origin main

# You – after adding/editing TCs
git add .
git commit -m "Add TC_002 for RelatedSystem"
git push

# Other members – get latest
git clone <REPO_URL>   # only first time
git pull               # every time they need your updates
```

---

## Part 6: Checklist

- [ ] SOLUTO folder opened in Cursor.
- [ ] Structure: `SOLUTO/<Feature>/test-cases/` with README + TC_001, …
- [ ] First test case = TC_001; next = TC_002, TC_003, …
- [ ] Git initialized; remote added; first push done.
- [ ] Team has repo URL; they clone and use `git pull`.
- [ ] Everyone uses the same folder structure and TC template.

---

*Keep this guide in `SOLUTO/docs/` so new team members can follow the same steps.*
