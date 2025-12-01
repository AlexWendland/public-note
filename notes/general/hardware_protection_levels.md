---
aliases:
checked: false
created: 2025-04-12
draft: false
last_edited: 2025-04-12
name: Hardware protection levels
tags:
  - OS
type: definition
---
>[!tldr] Hardware protection levels
>Within the [CPU](central_processing_unit_(cpu).md) there are different privilege levels which software can reside in. This normally uses the 'ring model' in which there are 4 levels:
>- Ring 0:
>	- Highest level of privilege which allows it to use all hardware operations.
>	- Used by the kernel, or core [OS](operating_system_(os).md) components.
>- Ring 1 & 2:
>	- Intermediate privilege levels.
>	- Rarely used in modern operating systems.
>	- Intended to be used by drivers or services that existed between the user and the kernel.
>- Ring 3:
>	- Lowest privilege level.
>	- Used by user-mode applications.
>	- Cannot directly access hardware.
>
> When using a bare-metal [hypervisor](virtual_machine_monitor_(vmm).md) this introduces another set of distinctions. Root or non-root applications (so in total there are 8 levels).
> - Root mode:
> 	- Used by the hypervisor.
> 	- Can control virtual machines and intercept privileged instructions.
> - Non-root mode:
> 	- Used by guest operating systems running inside virtual machines.
> 	- Applications running here may believe they have full control of the resources but these instructions are intercepted by the [hypervisor](virtual_machine_monitor_(vmm).md).

