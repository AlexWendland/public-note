---
aliases:
  - trap instruction
created: 2024-08-26
date_checked: 2026-02-05
draft: false
last_edited: 2024-08-26
tags:
  - computer-science
  - OS
title: Trap instruction
type: definition
---
>[!note] Trap instruction
>A trap instruction is sent to when an application in [user mode](process_modes.md) tries to access hardware without using a [system call](system_call.md). This is passed to the [OS](operating_system_(os).md) to judge if the call was illegitimate or harmful. While this is happening, the process is stopped from doing anything else.

