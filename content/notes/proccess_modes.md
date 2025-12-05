---
aliases:
  - Kernel mode
  - User mode
  - kernel mode
  - user mode
checked: false
created: 2024-08-26
draft: false
last_edited: 2024-08-26
tags:
  - computer-science
  - OS
title: Proccess modes
type: definition
---
>[!tldr] Process modes
>Processes normally has at least 2 modes.
> - Kernel mode: Which has privileged access to hardware resources.
> - User mode: Must access resources through the [OS](operating_system_(os).md) via [system calls](system_call.md).
>
> The mode is determined by a bit set in the [CPU](central_processing_unit_(cpu).md). If an application running in user mode tries to access hardware this sends a [trap instruction](trap_instruction.md) to the [OS](operating_system_(os).md) for the operating system to inspect that call. This will freeze the application whilst this is being investigated.
