---
aliases:
created: 2025-03-23
date_checked: 2026-02-05
draft: false
last_edited: 2026-02-05
tags:
  - OS
title: Checkpointing
type: definition
---
>[!note] Checkpointing
>Checkpointing is an operation performed by the [operating system](operating_system_(os).md) where it copies a current [process](process.md) state and saves a write protected copy of it. The operating system can then resume the process from that state in the future. This is useful for:
>- Debugging: You can jump between checkpoints to find out where bugs happen.
>- Migration: You can move the processes state onto another machine and resume it from there.
>- Disaster recovery: You can save old versions of the program if something goes wrong and restart from a past checkpoint.

