---
aliases: 
checked: false
created: 2025-03-23
last_edited: 2025-03-23
publish: true
tags:
  - OS
type: definition
---
>[!tldr] Checkpointing
>Checkpointing is an operation performed by the [[Operating system (OS)|operating system]] where it copies a current [[Process|processes]] state and saves a write protected copy of it. The operating system can then resume the process from that state in the future. This is useful for:
>- Debugging: You can jump between checkpoints to find out where bugs happen.
>- Migration: You can move the processes state onto another machine and resume it from there.
>- Disaster recovery: You can save old versions of the program if something goes wrong and restart from a past checkpoint.

