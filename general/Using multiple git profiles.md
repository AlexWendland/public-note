---
aliases: []
checked: false
created: 2023-03-19
last_edited: 2023-11-11
draft: false
tags:
  - programming
  - git
  - issue
type: guide
---
# Using multiple git profiles

## Issue
I am using a laptop where I have my personal repositories and some work ones. I would like to commit to these using different profiles and secure them using different [[Secure Shell (SSH) key|SSH keys]].

## Assumptions
I will assume you are:
- using a [[Linux|linux]] system.
- Have generated different [[Secure Shell (SSH) key|SSH keys]] for each profile:
`~/.ssh/personal-key`
`~/.ssh/work-key`
- Your repositories are on [[GitHub]], though you can change the link from [[GitHub]] (`github.com`) to another repository host.

## Solution

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
