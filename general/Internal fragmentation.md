---
aliases:
  - internal fragmentation
checked: false
created: 2025-03-22
last_edited: 2025-03-22
draft: false
tags:
  - OS
type: definition
---
>[!tldr] Internal fragmentation
>_Internal fragmentation_ occurs when allocated memory blocks are larger than the data they store, leaving unused space inside the allocated block. This happens because memory is allocated in fixed-size units (e.g., [[Memory page|pages]] in [[Paging system|paging system]] or predefined allocation sizes in [[Heap (OS)|heap]] memory). The unused portion inside an allocated block is wasted, leading to inefficiency. For example a process is allocated a 4 KB [[Memory page|memory page]] but only uses 3 KB, wasting 1 KB inside the page.

