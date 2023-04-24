---
aliases: []
type: tool
publish: true
created: 2023-04-24
last_edited: 2023-04-24
tags: programming, git
chatgpt: false
---
# Pre-commit hooks

[Pre-commit hooks](https://pre-commit.com/) are a method of checking files are up to some provided standard before the are commited to a repository. The configuration file (`.pre-commit-config.yaml`) for that standard can be kept in the repository and updated as the standard changes.

As a user it is quite simple - first [install](https://pre-commit.com/#install) pre-commit hooks (it is a [[Python]] package). Then within the repository you simply run
``` shell
pre-commit install
```
which configures the hooks for this repository. Then when running `git commit` before doing that it runs the checks specified in the repository. If any of them fail it does not commit. Some of the 'hooks' will auto format the files which you can then check.