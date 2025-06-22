---
aliases:
  - Kernel mode
  - User mode
  - kernel mode
  - user mode
checked: false
created: 2024-08-26
last_edited: 2024-08-26
draft: false
tags:
  - computer-science
  - OS
type: definition
---
>[!tldr] Process modes
>Processes normally has at least 2 modes. 
> - Kernel mode: Which has privileged access to hardware resources.
> - User mode: Must access resources through the [[Operating system (OS)|OS]] via [[System call|system calls]].
>
> The mode is determined by a bit set in the [[Central processing unit (CPU)|CPU]]. If an application running in user mode tries to access hardware this sends a [[Trap instruction|trap instruction]] to the [[Operating system (OS)|OS]] for the operating system to inspect that call. This will freeze the application whilst this is being investigated. 
