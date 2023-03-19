---
aliases: []
type: str
publish: false
created: 2023-03-19
last_edited: 2023-03-19
tags: programming, git
---
# Using multiple git profiles

## Issue
I am using a laptop where I have my personal repositories but also some work ones. I would like to commit to these using different profiles and secure them using different [[Secure Shell (SSH) key|SSH keys]]. 

## Assumptions
For this I will assume you are using a [[Linux|linux]] system.

## Solution
Make sure you have generated different [[Secure Shell (SSH) key|SSH keys]] for each profile. I will assume these are in:
- \~/.ssh/personal-key
- \~/.ssh/work-key
