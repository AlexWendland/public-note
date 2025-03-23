---
aliases:
  - memory allocator
  - memory allocators
checked: false
created: 2025-03-23
last_edited: 2025-03-23
publish: true
tags:
  - OS
type: definition
---
>[!tldr] Memory allocator
>The memory allocator gets used when a process needs map some [[Physical memory|physical memory]] onto its [[Virtual memory|virtual memory]]. There are two different kinds of allocators:
>- Kernel-level allocators: That is used by the kernel to get memory for the kernel state but also the static process state.
>- User-level allocators: Dynamic process state on the [[Heap (OS)|heap]] obtained by calls to malloc/free.

