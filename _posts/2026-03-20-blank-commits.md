---
title: "How To Git Commit With Blank Messages"
permalink: blank-commits
---

## How?

One liner:
```
git commit -a --allow-empty-message -m \"\"
```

Or add an alias to `~/.gitconfig`

```
[alias]
	nccommit = commit -a --allow-empty-message -m \"\"
```

Then you can:

```
git nccommit
```

## Why?

- In the interest of preventing cognitive overload, it's better to leave a commit message blank unless there is something utterly useful to write.

## But What About Accountability

- Leave meaningful messages for major changes (may be while merging to a more important branch). If someone is going to hold you accountable for not meaningfully describing a typo fix, you probably need to find other people to work with.

## But What About Auto-generating Changelogs With Conventional Commits?

Quoting [lobste.rs/~thiht](https://lobste.rs/~thiht):

> Honestly I never bother reading changelogs generated from conventional commits, they're trash. Changelogs must be written by humans, for humans. A commit is too small a unit to make a useful changelog, it lacks high level vision.

## References

- [https://stackoverflow.com/questions/6218199/git-commit-with-no-commit-message](https://stackoverflow.com/questions/6218199/git-commit-with-no-commit-message)
