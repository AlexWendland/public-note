---
aliases:
  - frame
  - memory frames
created: 2025-03-22
date_checked:
draft: false
last_edited: 2025-03-22
tags: []
title: Memory frame
type: definition
---
>[!tldr] Memory frame
>A _frame_ is a fixed-size block of [physical memory](physical_memory.md) used in a [paging system](paging_system.md). When a process requests memory, its [virtual address space](virtual_memory.md) is divided into [pages](memory_page.md) of the same size, and the [operating system](operating_system_(os).md) maps these pages to available _frames_ in [physical memory](physical_memory.md). The [MMU](memory_management_unit_(mmu).md) handles this mapping using a [page table](page_table.md). Since frames and pages are of equal size, paging avoids external fragmentation, though it may introduce internal [fragmentation](fragmentation.md) if a page does not fully utilize a frame.
