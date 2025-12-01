---
aliases:
  - page tables
  - page
  - page table
checked: false
created: 2024-08-26
draft: false
last_edited: 2024-08-26
name: Page table
tags:
  - OS
  - computer-science
type: definition
---
>[!tldr] Page table
>A *page table* maps addresses in the [virtual address space](virtual_memory.md) of a [process](process.md) which is indexed by the [virtual page number](virtual_page_number_(vpn).md) and an offset within that page. The [virtual page number](virtual_page_number_(vpn).md) is mapped to a [physical frame number](physical_frame_number_(pfn).md) which combined with the offset can identify a location in [physical memory](physical_memory.md).
>The simplest way to do this is with flat page tables. This is a page table contains one entry for each [virtual page number](virtual_page_number_(vpn).md) which is the index in the page table. The [page table entry](page_table_entry.md) then consists of the [physical frame number](physical_frame_number_(pfn).md) a long with some management [bits](bit.md) which inform the [operating system](operating_system_(os).md) if the memory mapping is valid, what permissions the [process](process.md) has for this memory.
>To then do the mapping it sums the offset from the [virtual address](virtual_memory.md) with the [physical frame number](physical_frame_number_(pfn).md) in the page table to get the [physical address](physical_memory.md).
>Other page table types exist such as [Multi-level page tables](multi-level_page_tables.md) or [Inverted page tables (IPT)](inverted_page_tables_(ipt).md).

