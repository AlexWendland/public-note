---
aliases:
checked: false
created: 2025-03-22
draft: false
last_edited: 2025-03-22
tags:
  - OS
type: definition
---
>[!tldr] Multi-level page tables
> To reduce the memory overhead of a single large [[Page table|page table]], modern systems use a *hierarchical paging structure* called a _multi-level page table_. Instead of a single, flat table mapping all virtual pages to physical frames, the **multi-level approach** breaks this into a series of smaller **nested page tables**.
>
>At the top level, an **outer page table** contains pointers to **lower-level page tables**, continuing down the hierarchy until reaching the **final level** (the "inner page table"), which directly maps virtual pages to physical frames.
>
>![multi_level_page_tables](../../images/excalidraw/multi_level_page_tables.excalidraw.svg)
>
>This approach optimizes memory usage by allocating **only the page tables that are needed**—a technique known as **"on-demand allocation"** or **"sparse paging"**. If a virtual memory region is never accessed, its corresponding page tables are never created, saving memory.
>
>Adding more levels increases granularity, reducing wasted space, but comes at the cost of **more memory lookups per access**, potentially increasing **[[Translation Lookaside Buffer (TLB)|TLB]] misses** and reducing performance.

