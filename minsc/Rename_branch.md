# Renaming a GitHub branch from master to main

After renaming the branch on GitHub (from master to main), in your local repo, you can do:

```bash
git branch -m master main
git fetch origin
git branch -u origin/main main
git remote set-head origin -a
```
