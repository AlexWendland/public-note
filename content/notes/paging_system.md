---
aliases:
  - paging system
  - paging
created: 2025-03-22
date_checked:
draft: false
last_edited: 2025-03-22
tags:
  - OS
title: Paging system
type: definition
---
>[!tldr] Paging system
>_Paging_ is a memory management scheme that divides both [physical memory](physical_memory.md) and [virtual memory](virtual_memory.md) into fixed-size blocks called [memory pages](memory_page.md) ([virtual memory](virtual_memory.md)) and [memory frames](memory_frame.md) ([physical memory](physical_memory.md)). The [operating system](operating_system_(os).md) maintains a [page table](page_table.md) to map virtual pages to physical frames, allowing non-contiguous memory allocation and reducing [fragmentation](fragmentation.md). Paging enables efficient memory use and simplifies process isolation, but it requires hardware support in the form of a [Memory Management Unit (MMU)](memory_management_unit_(mmu).md) to handle address translation.

