---
aliases:
  - TLB
created: 2025-03-22
date_checked: 2026-02-05
draft: false
last_edited: 2025-03-22
tags:
  - hardware
  - OS
title: Translation Lookaside Buffer (TLB)
type: definition
---
> [!definition] Translation Lookaside Buffer (TLB)
> The _Translation Lookaside Buffer (TLB)_ is a small, high-speed cache inside the [MMU](memory_management_unit_(mmu).md) that stores recently used virtual-to-physical address mappings. Since accessing these mappings in memory is slow, the TLB helps speed up address translation by reducing the need to fetch mapping table entries from [RAM](random_access_memory_(ram).md). A TLB hit means the translation is found instantly, while a TLB miss requires fetching the mapping from the table in main memory.
