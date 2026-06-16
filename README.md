*the 42 curriculum by mabu-are, aabtah.*


# massage for us

## mabu-are to aabtah
### code...
I need from you to do :
1- if any file will rase error... import and use ouer error costom
2- type any thing you need in README.md to me
3- include any thing you see in .gitignore
4- type alot of commint in your code to let me understand how it work
5- if you wont to update any in my code type the update in description of the fun

### Makefile
but the mlx and any extracted file in a new dir
let the Makefile on me pls i wona desine it <3
### valid_maze.txt
the valid_maze is just an example for us


## aabtah to mabu-are














# reference

# git command you need to know

### Git Reference Guide for Our Team
Here are the essential Git commands we need to collaborate smoothly on our 42 project, ensuring we don't overwrite each other's code and can review things safely.

---

#### 1. Managing Branches (Moving & Creating)

* **How to create a new branch?**
    ```bash
    git branch <branch_name>
    ```
    *Description:* This creates a new standalone branch from your current position. For example, `git branch feature/maze-validation`.

* **How to switch from one branch to another?**
    ```bash
    git checkout <branch_name>
    ```
    *Alternatively (Modern Git):*
    ```bash
    git switch <branch_name>
    ```
    *Description:* This moves you from your current branch to another one. Make sure to commit or stash your changes before switching so you don't carry over uncommitted work.

* **How to create AND switch to a new branch in one command?**
    ```bash
    git checkout -b <branch_name>
    ```
    *Alternatively (Modern Git):*
    ```bash
    git switch -c <branch_name>
    ```
    *Description:* Shortcut to create a new branch and immediately check it out.

---

#### 2. Reviewing Other Branches Safely

* **How to see the code of another branch without losing/deleting your current progress?**
    1. First, make sure your current work is safely committed:
       ```bash
       git add .
       git commit -m "Save current progress before checking other branch"
       ```
    2. Alternatively, if your code is broken and you don't want to commit it yet, **stash** it:
       ```bash
       git stash
       ```
       *(This temporarily hides your uncommitted changes and cleans your working directory).*
    3. Now, switch to the other branch to look at the code:
       ```bash
       git checkout <other_branch_name>
       ```
    4. **How to return back to your original branch?**
       ```bash
       git checkout <your_original_branch>
       ```
    5. If you used `git stash` earlier, bring your working changes back with:
       ```bash
       git stash pop
       ```

---

#### 3. Merging Code

* **How to merge another branch into your current branch?**
    1. Always switch to the branch you want to receive the changes (e.g., `main` or your primary dev branch):
       ```bash
       git checkout main
       ```
    2. Pull the latest updates from remote just in case:
       ```bash
       git pull origin main
       ```
    3. Merge the specific feature branch into your current branch:
       ```bash
       git merge <feature_branch_name>
       ```
    *Note:* If there are merge conflicts, Git will mark them in the files. Open the files, resolve the conflicts, save, then run `git add <file>` and `git commit` to finish the merge.

---

#### 4. Going Back in Time (Undoing Commits)

* **How to undo/go back to a previous commit?**
    
    * **Option A: Soft Reset (Safe - Keeps your code changes)**
        ```bash
        git reset --soft HEAD~1
        ```
        *Description:* This undoes the very last commit, but keeps all your written code modifications in your staging area so you can edit and re-commit them.
        
    * **Option B: Hard Reset (Dangerous - Deletes updates permanently)**
        ```bash
        git reset --hard HEAD~1
        ```
        *Description:* Destroys the last commit AND completely wipes out all code changes associated with it. Use with extreme caution!
        
    * **Option C: Revert (Best for Shared Branches)**
        ```bash
        git revert <commit_hash>
        ```
        *Description:* Instead of rewriting history, this creates a *new* commit that does the exact opposite of the target commit. This is the safest way when working together so it doesn't break the history for the other person.

---

#### 5. Additional Helpful Team Commands

* **Check the status of your working repository:**
    ```bash
    git status
    ```
    *Description:* Shows which files are modified, staged for commit, or untracked. Run this constantly!

* **See the commit history as a clean graph:**
    ```bash
    git log --oneline --graph --all
    ```
    *Description:* Shows a beautiful visual representation of all branches and commit histories so we don't get lost.

* **Check what exactly changed before committing:**
    ```bash
    git diff
    ```
    *Description:* Shows line-by-line what code was added or removed since your last save.
