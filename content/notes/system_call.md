---
aliases:
  - system calls
  - system call
created: 2024-08-26
date_checked:
draft: false
last_edited: 2024-08-26
tags:
  - computer-science
title: System call
type: definition
---
>[!tldr] System call
>An application running in [user mode](proccess_modes.md) makes a *system call* to the [OS](operating_system_(os).md) when it needs to access hardware. The [OS](operating_system_(os).md) then runs the associated call in [kernel mode](proccess_modes.md) to effect the hardware. This is normally costly for the application as it has to give over control to the kernel.
>
>![System Call Flow Chart](../../static/images/system_call_flow_chart.png)
>
> Some example *system calls* are:
> - Open (file),
> - Send (socket), or
> - mmap (memory).


