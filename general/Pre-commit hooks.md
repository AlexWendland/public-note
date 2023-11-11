---
aliases: []
chatgpt: false
created: 2023-04-24
last_edited: 2023-04-24
publish: true
tags: programming, git
type: tool
---
# Pre-commit hooks

[Pre-commit hooks](https://pre-commit.com/) are a great way to run checks against your code before it is committed to the repository. This saves time and money by not having to run checks in the CI/CD pipeline, and also puts control of your commits back in your hands.

## Setting up pre-commit hooks

You can install the pre-commit package using pip.

```bash
pip install pre-commit
```

After installing the pre-commit package, you can run the following command in this repository to install the hooks.

```bash
pre-commit install
```

This will run the checks every time you try to commit your changes. If the pre-commit hooks change, you will need to run this command again to update them.

## Using pre-commit hooks

When you commit your changes using git commit, the pre-commit hooks will run. The output of the hooks will be displayed, and they will either pass or fail. If any of the hooks fail, the exact file that caused the failure will be reported.

If a hook fails, it will either automatically fix the problem or provide an explanation of the issue and prompt you to fix it. After fixing the issues, you **must** add the changes and commit them again.

If you need to push changes and cannot figure out why they have failed, you can force a commit by using the --no-verify flag:

```bash
git commit --no-verify -m "Commit message"
```

## Configuring pre-commit hooks

You can see which hooks are running in the `.pre-commit-config.yaml` file at the base of the repository. To add additional hooks, you can search for them online. If you decide to change the hooks, make sure to inform others and let them decide whether they want to apply the changes. Others will need to run `pre-commit install` again after any changes are made. For further guidance on configuring pre-commit hooks, see the [pre-commit hooks documentation](https://pre-commit.com/#plugins).

## .pre-commit-config.yaml example

``` yaml
repos:
  - repo: https://github.com/pre-commit/pre-commit-hooks
    rev: v4.4.0
    hooks:
      # This will check that yaml files are valid and correctly formatted
      - id: check-yaml
      # This will check if large files have been added to the repository.
      - id: check-added-large-files
  - repo: https://github.com/psf/black
    rev: 23.3.0
    hooks:
      - id: black
  - repo: https://github.com/pycqa/isort
    rev: 5.11.2
    hooks:
     - id: isort
       name: isort (python)
```
