---
aliases:
  - internal fragmentation
created: 2025-03-22
date_checked:
draft: false
last_edited: 2025-03-22
tags:
  - OS
title: Internal fragmentation
type: definition
---
>[!tldr] Internal fragmentation
>_Internal fragmentation_ occurs when allocated memory blocks are larger than the data they store, leaving unused space inside the allocated block. This happens because memory is allocated in fixed-size units (e.g., [pages](memory_page.md) in [paging system](paging_system.md) or predefined allocation sizes in [heap](heap_(os).md) memory). The unused portion inside an allocated block is wasted, leading to inefficiency. For example a process is allocated a 4 KB [memory page](memory_page.md) but only uses 3 KB, wasting 1 KB inside the page.

