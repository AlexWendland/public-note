---
aliases:
  - memory allocator
  - memory allocators
created: 2025-03-23
date_checked: 2026-02-05
draft: false
last_edited: 2025-03-23
tags:
  - OS
title: Memory allocator
type: definition
---
>[!note] Memory allocator
>The memory allocator gets used when a process needs to map [physical memory](physical_memory.md) onto its [virtual memory](virtual_memory.md). There are two different kinds of allocators:
>- Kernel-level allocators: that is used by the kernel to get memory for the kernel state but also the static process state.
>- User-level allocators: dynamic process state on the [heap](heap_(os).md) obtained by calls to malloc/free.

