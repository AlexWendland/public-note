---
aliases:
  - trap instruction
checked: false
created: 2024-08-26
draft: false
last_edited: 2024-08-26
tags:
  - computer-science
  - OS
type: definition
---
>[!tldr] Trap instruction
>A trap instruction is sent to when an application in [[Proccess modes|user mode]] tries to access hardware without using a [[System call|system call]]. This is passed to the [[Operating system (OS)|OS]] to judge if the call was illegitimate or harmful. Whilst this is happening the process is stopped from doing anything else.

