---
aliases:
  - segment
  - memory segments
checked: false
created: 2025-03-22
draft: false
last_edited: 2025-03-22
name: Memory segment
tags:
  - OS
type: definition
---
>[!tldr] Memory segment
>A _memory segment_ is a variable-sized block of memory used in [segmentation](memory_segmentation.md), an alternative to [paging](paging_system.md) for memory management. Instead of dividing memory into fixed-size [pages](memory_page.md), segmentation divides memory into logically distinct sections, such as code, data, and stack segments. Each [segment](memory_segment.md) has a base address and a limit, defining its size and boundaries. The [operating system](operating_system_(os).md) and the [Memory Management Unit (MMU)](memory_management_unit_(mmu).md) manage segment access using a [segment table](descriptor_table.md), which maps segment numbers to [physical memory](physical_memory.md). Unlike [paging](paging_system.md), segmentation allows programs to organize memory based on logical structures rather than fixed-size blocks.
