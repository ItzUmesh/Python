# Git Commands Used to Connect This Repo to GitHub

This document explains every Git command that was run to turn your local `Python` folder into a repository linked to [https://github.com/ItzUmesh/Python](https://github.com/ItzUmesh/Python), plus how to use them going forward.

---

## What to do for future days' work

Whenever you finish a day (or any chunk of work) and want to save it to GitHub, do these **four steps** from PowerShell:

```powershell
cd "C:\Users\ns0ume01\source\repos\Python"
git add -A
git commit -m "Day 2: describe what you did"
git push
```

**Step by step:**

1. **`cd "C:\Users\ns0ume01\source\repos\Python"`** — Go to your Python project folder (skip if you're already there).
2. **`git add -A`** — Stage all new and changed files (new folders like `Day2`, new `.py` files, edits to existing files).
3. **`git commit -m "..."`** — Save a snapshot. Replace the message with something like:
   - `"Day 2: variables and types"`
   - `"Day 3: loops and lists"`
   - `"Day 4: functions"`
   - `"Fix typo in Day 2"`
4. **`git push`** — Upload your commits to GitHub. Your repo will show the latest files at https://github.com/ItzUmesh/Python.

You don't need to run `git init` or `git remote add` again. Just repeat these four steps whenever you want to save and back up your work.

---

## How to add additional files (e.g. in Day1)

When you create new files inside a folder like `Day1` (or any folder), you can add them in two ways:

**Option 1 — Add only that folder**

```powershell
cd "C:\Users\ns0ume01\source\repos\Python"
git add Day1/
git status
git commit -m "Day 1: add new files"
git push
```

- **`git add Day1/`** — Stages only new and changed files inside the `Day1` folder. Use any folder name (e.g. `Day2/`, `Day3/`).

**Option 2 — Add everything in the repo**

```powershell
cd "C:\Users\ns0ume01\source\repos\Python"
git add -A
git status
git commit -m "Day 1: add new files"
git push
```

- **`git add -A`** — Stages all new and changed files everywhere (Day1, Day2, root, etc.). Easiest if you want to back up the whole project.

Then **`git commit -m "..."`** and **`git push`** work the same either way. No extra setup is needed for files inside Day1 or any other directory.

---

## 1. Initialize a New Git Repository

```powershell
cd "C:\Users\ns0ume01\source\repos\Python"
git init
```

**What it does:**

- `cd "C:\Users\ns0ume01\source\repos\Python"` — Changes your current directory to your Python project folder. All following Git commands run in this folder.
- `git init` — Creates a hidden `.git` folder inside the project. That folder stores all version history (commits, branches, remotes). Until you run `git init`, the folder is just a normal folder; after that, it becomes a Git repository.

**When to use:** Only once per project, when you want to start tracking that folder with Git.

---

## 2. Add the GitHub Remote

```powershell
git remote add origin https://github.com/ItzUmesh/Python.git
```

**What it does:**

- `git remote add origin <url>` — Registers a “remote” named `origin` that points to your GitHub repo URL. Git uses this name when you run `push` or `pull`. The word `origin` is a convention (you could use another name, but `origin` is standard for the main remote).

**When to use:** Once per repo, when you first connect this local repo to a GitHub (or other) remote. To see your remotes later: `git remote -v`.

---

## 3. Create a `.gitignore` File

A `.gitignore` file was created (not a Git command, but important). It lists files and folders that Git should **not** track or commit.

**Why it matters:** Without it, Git would try to commit things like:

- Python cache (`__pycache__`, `.pyc`)
- Visual Studio files (`.vs/`)
- The `Python_remote/` clone folder (which has its own `.git` and would cause errors if added)

So we added a `.gitignore` so only your real project files get committed.

---

## 4. Stage All Files for Commit

```powershell
git add -A
git status
```

**What it does:**

- `git add -A` — Stages **all** changes in the repo: new files, modified files, and deleted files. “Staging” means “mark these changes to be included in the next commit.” Nothing is committed yet.
- `git status` — Shows what is staged, what is modified but not staged, and what branch you’re on. Useful before every commit.

**Alternatives:**

- `git add .` — Stages all changes in the current directory and below (often similar to `-A`).
- `git add path/to/file` — Stages only that file.

**When to use:** Run `git add` (and often `git status`) whenever you want to prepare a new commit.

---

## 5. Create the First Commit

```powershell
git commit -m "Initial commit: Python learning repo"
```

**What it does:**

- `git commit` — Creates a snapshot (a “commit”) of everything that is currently staged. Each commit has a unique ID and a message.
- `-m "Initial commit: Python learning repo"` — Sets the commit message. Good messages describe what changed or why (e.g. “Add Day 2 exercises”, “Fix typo in intro”).

**When to use:** After every logical chunk of work, after running `git add`. Commits are the history Git keeps.

---

## 6. Rename the Branch to `main`

```powershell
git branch -M main
```

**What it does:**

- `git branch -M main` — Renames the current branch to `main`. Git often creates the first branch as `master`; GitHub’s default is `main`. Using `-M` forces the rename even if `main` already exists (it overwrites).

**When to use:** Once per repo if you want your default branch to be named `main` to match GitHub.

---

## 7. Push to GitHub and Set Upstream

```powershell
git push -u origin main
```

**What it does:**

- `git push` — Sends your local commits to a remote repository.
- `origin` — The remote we added earlier (your GitHub repo).
- `main` — The branch name to push. So “push the `main` branch to `origin`.”
- `-u origin main` — Sets the “upstream” of your local `main` branch to `origin/main`. After this, you can just run `git push` (and `git pull`) without typing the branch name each time.

**When to use:** Whenever you want to upload your latest commits to GitHub. After the first time with `-u`, usually just `git push` is enough.

---

## Summary: Commands in Order (One-Time Setup)

| Step | Command | Purpose |
|------|---------|--------|
| 1 | `cd "C:\Users\ns0ume01\source\repos\Python"` | Go to project folder |
| 2 | `git init` | Turn folder into a Git repo |
| 3 | `git remote add origin https://github.com/ItzUmesh/Python.git` | Link to GitHub |
| 4 | *(Create `.gitignore`)* | Ignore cache, IDE, and clone folder |
| 5 | `git add -A` | Stage all files |
| 6 | `git commit -m "Initial commit: Python learning repo"` | Create first commit |
| 7 | `git branch -M main` | Name default branch `main` |
| 8 | `git push -u origin main` | Upload to GitHub and set upstream |

---

## Daily Workflow: Saving Your Work to GitHub

Whenever you add or change files and want to save them to GitHub, run:

```powershell
cd "C:\Users\ns0ume01\source\repos\Python"
git add -A
git status
git commit -m "Short description of what you did"
git push
```

- **`git add -A`** — Stage all changes.
- **`git status`** — Optional but recommended: check what will be committed.
- **`git commit -m "..."`** — Create a commit with a clear message.
- **`git push`** — Send commits to GitHub (no `-u` needed after the first time).

---

## Quick Reference

| Command | Meaning |
|---------|--------|
| `git status` | See what’s changed and what’s staged |
| `git add -A` | Stage everything |
| `git commit -m "message"` | Save a snapshot with a message |
| `git push` | Upload commits to GitHub |
| `git pull` | Download and merge latest changes from GitHub |
| `git remote -v` | List remotes (e.g. `origin`) |
| `git log --oneline` | Show recent commits briefly |

If you run into authentication when pushing, use your GitHub **Personal Access Token** (not your account password) when Git asks for credentials.
