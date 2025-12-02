---
aliases: []
checked: false
created: 2023-03-19
draft: false
last_edited: 2023-11-11
tags:
  - programming
  - git
  - issue
title: Using multiple git profiles
type: guide
---
# Issue
I am using a laptop where I have my personal repositories and some work ones. I would like to commit to these using different profiles and secure them using different [SSH keys](secure_shell_(ssh)_key.md).

# Assumptions
I will assume you are:
- using a [linux](linux.md) system.
- Have generated different [SSH keys](secure_shell_(ssh)_key.md) for each profile:
`~/.ssh/personal-key`
`~/.ssh/work-key`
- Your repositories are on [GitHub](github.md), though you can change the link from [GitHub](github.md) (`github.com`) to another repository host.

# Solution

\1. Add hosts to your `~/.ssh/config`  file such as:

```sh
Host work-github
  HostName github.com
  User git
  IdentityFile ~/.ssh/work-key
  IdentitiesOnly yes

Host personal-github
  HostName github.com
  User git
  IdentityFile ~/.ssh/personal-key
  IdentitiesOnly yes
```

For later steps, "work" and "personal" will be referred to as `<account>`.

2a. Change the remote host for an existing repository:

```sh
cd /path/to/your/repo
git remote set-url origin <account>-github:/remote/path/of/repo.git
```

2b. Clone a repository using the new host:

```sh
cd /path/to/the/folder/for/repositories
git clone <account>-github:/remote/path/of/repo.git
```

\3. Set the user details for the repository:

```sh
git config user.name "Your Name"
git config user.email "your@email.here"
```
