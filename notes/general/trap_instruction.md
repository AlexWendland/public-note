---
aliases:
  - trap instruction
checked: false
created: 2024-08-26
draft: false
last_edited: 2024-08-26
name: Trap instruction
tags:
  - computer-science
  - OS
type: definition
---
>[!tldr] Trap instruction
>A trap instruction is sent to when an application in [user mode](proccess_modes.md) tries to access hardware without using a [system call](system_call.md). This is passed to the [OS](operating_system_(os).md) to judge if the call was illegitimate or harmful. Whilst this is happening the process is stopped from doing anything else.

