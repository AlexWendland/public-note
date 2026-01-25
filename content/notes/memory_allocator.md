---
aliases:
  - memory allocator
  - memory allocators
created: 2025-03-23
date_checked:
draft: false
last_edited: 2025-03-23
tags:
  - OS
title: Memory allocator
type: definition
---
>[!tldr] Memory allocator
>The memory allocator gets used when a process needs map some [physical memory](physical_memory.md) onto its [virtual memory](virtual_memory.md). There are two different kinds of allocators:
>- Kernel-level allocators: That is used by the kernel to get memory for the kernel state but also the static process state.
>- User-level allocators: Dynamic process state on the [heap](heap_(os).md) obtained by calls to malloc/free.

