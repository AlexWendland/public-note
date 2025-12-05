---
aliases:
checked: false
created: 2025-03-23
draft: false
last_edited: 2025-03-23
tags:
  - OS
title: Demand paging
type: definition
---
>[!tldr] Demand paging
> As [virtual memory](virtual_memory.md) is far larger than [physical memory](physical_memory.md) to maximize resource usage the [operating system](operating_system_(os).md) will swap out memory in [RAM](random_access_memory_(ram).md) to some secondary storage like the disk. In doing so it updates the [page table entry](page_table_entry.md) to reflect this. If the memory is then accessed again it needs to pull it back off the secondary storage. It does this in the following way:
> 1. Memory is referenced.
> 2. The [MMU](memory_management_unit_(mmu).md) raises a trap to hand control to the [operating system](operating_system_(os).md).
> 3. The page is recovered from the secondary storage.
> 4. The page is copied into a free [memory frame](memory_frame.md) in [RAM](random_access_memory_(ram).md).
> 5. The [page table entry](page_table_entry.md) is updated to reflect this change.
> 6. Control is handed back to the [process](process.md).
>
> ![Demand Paging](../../static/images/demand_paging.png)

