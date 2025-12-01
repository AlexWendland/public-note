---
aliases:
  - paging system
  - paging
checked: false
created: 2025-03-22
draft: false
last_edited: 2025-03-22
tags:
  - OS
type: definition
---
>[!tldr] Paging system
>_Paging_ is a memory management scheme that divides both [[Physical memory|physical memory]] and [[Virtual memory|virtual memory]] into fixed-size blocks called [[Memory page|memory pages]] ([[Virtual memory|virtual memory]]) and [[Memory frame|memory frames]] ([[Physical memory|physical memory]]). The [[Operating system (OS)|operating system]] maintains a [[Page table|page table]] to map virtual pages to physical frames, allowing non-contiguous memory allocation and reducing [[Fragmentation|fragmentation]]. Paging enables efficient memory use and simplifies process isolation, but it requires hardware support in the form of a [[Memory Management Unit (MMU)]] to handle address translation.

