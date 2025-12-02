---
aliases:
  - physical memory
  - physical addresses
checked: false
created: 2024-08-26
draft: false
last_edited: 2024-08-26
title: Physical memory
tags:
  - OS
  - hardware
  - computer-science
type: definition
---
>[!tldr] Physical memory
>_Physical memory_ usually refers to the actual [RAM](random_access_memory_(ram).md) installed in a computer. However, the term can also have more specific meanings depending on the context. A *physical address* is a reference to a location in this [RAM](ram.md), but in some cases, it may also refer to an abstraction used by the [operating system](operating_system_(os).md), which treats memory as a contiguous block, even if the physical layout is non-contiguous. The mapping between virtual addresses and physical addresses is handled by the [Memory Management Unit (MMU)](memory_management_unit_(mmu).md) and [memory controller](memory_controller.md), which ensure that memory is accessed correctly and efficiently.

