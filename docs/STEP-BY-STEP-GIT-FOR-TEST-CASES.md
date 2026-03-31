# Step-by-Step Guide: Storing Test Cases in Git (For Team Use)

**Purpose:** Store the SOLUTO project (test cases, docs, scripts) in Git so other team members can access and use everything in one place.

---

## Prerequisites

- Git installed on your machine.
- A GitHub (or similar) account.
- Your project folder (e.g. `SOLUTO`) with all files ready.

---

## Step 1: Open Your Project Folder in the Terminal

1. Open **Command Prompt** (Win + R → type `cmd` → Enter).
2. Go to your project folder:
   ```bash
   cd c:\Users\sanjay.waghmare\SOLUTO
   ```
3. Confirm you see the prompt: `c:\Users\sanjay.waghmare\SOLUTO>`

**What we did:** Made sure we were inside the correct project directory before any Git commands.

---

## Step 2: Check If Git Is Already Set Up

1. In the same Command Prompt, run:
   ```bash
   git status
   ```
2. **If you see:** `fatal: not a git repository (or any of the parent directories): .git`  
   **Meaning:** This folder is not yet a Git repository. Go to Step 3.
3. **If you see:** Something like "On branch master" or "No commits yet"  
   **Meaning:** Git is already initialized. You can skip Step 3 and move to adding/committing or connecting to a remote.

**What we did:** Checked whether the project was already a Git repo so we knew whether to run `git init` or not.

---

## Step 3: Turn the Folder Into a Git Repository

1. In the same folder, run:
   ```bash
   git init
   ```
2. You should see: `Initialized empty Git repository in C:/Users/sanjay.waghmare/SOLUTO/.git/`

**What we did:** Created a new Git repository inside your project folder. Git can now track files and history in this folder.

---

## Step 4: Add All Project Files to Git (Staging)

1. Run:
   ```bash
   git add .
   ```
2. The `.` means "current folder and everything inside it."
3. You may see warnings about LF/CRLF (line endings). These are normal on Windows; the files are still added.

**What we did:** Told Git to include all your files (README, docs, scripts, test cases TC_001–TC_006, etc.) in the next save (commit).

---

## Step 5: Save the Snapshot (First Commit)

1. Run:
   ```bash
   git commit -m "Add SOLUTO project with docs, scripts, and RelatedSystem test cases"
   ```
2. Replace the message in quotes with a short description of what you're saving if you prefer.
3. You should see something like: `[master (root-commit) 9844684] ...` and `11 files changed, 786 insertions(+)` plus a list of created files.

**What we did:** Saved the first snapshot of your project in Git. Everything you added in Step 4 is now stored in the local Git history.

---

## Step 6: Create a Remote Repository (So Others Can Access It)

1. Log in to **GitHub** (or your organization's Git host).
2. Click **New** (or "New repository").
3. Set the repository name (e.g. `SOLUTO-test-cursorAI`).
4. Leave "Add a README" **unchecked** (you already have one).
5. Click **Create repository**.
6. Copy the repository URL (e.g. `https://github.com/sanjayw86/SOLUTO-test-cursorAI.git`).

**What we did:** Created an empty repository on GitHub that will hold your project so others can clone and use it.

---

## Step 7: Connect Your Local Project to the Remote

1. In Command Prompt, in your project folder, run (use your actual URL):
   ```bash
   git remote add origin https://github.com/sanjayw86/SOLUTO-test-cursorAI.git
   ```
2. No output usually means it worked.  
   If you see "remote origin already exists," the remote is already set; you can skip or update it as needed.

**What we did:** Linked your local Git repo to the GitHub repo. The name `origin` is the standard name for this remote.

---

## Step 8: Check Your Branch Name (master or main)

1. Run:
   ```bash
   git branch
   ```
2. You will see either `* master` or `* main`. The `*` is your current branch.

**What we did:** Confirmed which branch name to use in the next step (e.g. `master` or `main`).

---

## Step 9: Push Your Code to GitHub

1. If your branch is **master**:
   ```bash
   git push -u origin master
   ```
2. If your branch is **main**:
   ```bash
   git push -u origin main
   ```
3. If a sign-in window appears:
   - Choose **"Sign in with your browser"** and complete login in the browser.
4. If GitHub asks to **Authorize Git Credential Manager**, click **Authorize git-ecosystem**.
5. If GitHub asks to **Confirm access**, enter your password or 2FA code and click **Verify**.
6. When it succeeds, you'll see something like:  
   `Writing objects: 100% (17/17), 7.18 KiB` and  
   `* [new branch] master -> master` and  
   `branch 'master' set up to track 'origin/master'.`

**What we did:** Uploaded your committed project (all files and structure) to GitHub. Other team members can now open the repo and use the test cases and project structure.

---

## Step 10: Verify on GitHub

1. Open the repository URL in a browser, e.g.:  
   **https://github.com/sanjayw86/SOLUTO-test-cursorAI**
2. You should see: README, `docs/`, `scripts/`, `RelatedSystem/test-cases/` (README.md, TC_001.md … TC_006.md).

**What we did:** Confirmed that the project and test cases are stored correctly and visible to others.

---

## Summary: What We Did End-to-End

| Step | Action | Result |
|------|--------|--------|
| 1 | Opened project folder in terminal | Ready to run Git commands |
| 2 | Ran `git status` | Confirmed folder was not a Git repo |
| 3 | Ran `git init` | Created a new Git repository |
| 4 | Ran `git add .` | Staged all project files |
| 5 | Ran `git commit -m "..."` | Saved first snapshot locally |
| 6 | Created a new repo on GitHub | Had a URL for the remote |
| 7 | Ran `git remote add origin <URL>` | Linked local repo to GitHub |
| 8 | Ran `git branch` | Saw branch name (master) |
| 9 | Ran `git push -u origin master` | Pushed project to GitHub |
| 10 | Opened repo in browser | Verified files and structure |

---

## For Later: When You Change Something

1. `git add .`
2. `git commit -m "Short description of change"`
3. `git push`

---

## How Others Get the Project

They run:

```bash
git clone https://github.com/sanjayw86/SOLUTO-test-cursorAI.git
```

Then they have the full project (docs, scripts, test cases) on their machine.

---

*Document based on the steps followed to store the SOLUTO test cases and project in Git for team use.*
