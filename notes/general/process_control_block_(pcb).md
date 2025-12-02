---
aliases:
  - PCB
checked: false
created: 2024-08-26
draft: false
last_edited: 2024-08-26
tags:
  - OS
  - computer-science
title: Process control block (PCB)
type: definition
---
>[!tldr] Process control block (PCB)
>A *Process control block* is a data structure that holds the state for a [process](process.md). This includes but is not limited to:
>- [Process Identification (PID)](process_identification_(pid).md),
>	- Of both the process and its parent if that exists.
>- Process state
>- [Program counter](program_counter_(pc).md)
>- [CPU register](cpu_register.md)
>- Memory management information,
>- Scheduling information,
>- Accounting information,
>	- SPU usage, elapsed time, user/system time.
>- I/O status
>- Process privileges, and
>- Process metadata.

