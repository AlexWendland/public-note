---
aliases:
  - system calls
  - system call
checked: false
created: 2024-08-26
last_edited: 2024-08-26
draft: false
tags:
  - computer-science
type: definition
---
>[!tldr] System call
>An application running in [[Proccess modes|user mode]] makes a *system call* to the [[Operating system (OS)|OS]] when it needs to access hardware. The [[Operating system (OS)|OS]] then runs the associated call in [[Proccess modes|kernel mode]] to effect the hardware. This is normally costly for the application as it has to give over control to the kernel.
>
>![[system_call_flow_chart.png]] 
> 
> Some example *system calls* are:
> - Open (file),
> - Send (socket), or
> - mmap (memory).


