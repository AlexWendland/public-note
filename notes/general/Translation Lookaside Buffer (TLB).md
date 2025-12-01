---
aliases:
  - TLB
checked: false
created: 2025-03-22
draft: false
last_edited: 2025-03-22
tags:
  - hardware
  - OS
type: definition
---
>[!tldr] Translation Lookaside Buffer (TLB)
>The _Translation Lookaside Buffer (TLB)_ is a small, high-speed cache inside the [[Memory Management Unit (MMU)|MMU]] that stores recently used virtual-to-physical address mappings. Since accessing these mappings in memory is slow, the TLB helps speed up address translation by reducing the need to fetch mapping table entries from [[Random Access Memory (RAM)|RAM]]. A TLB hit means the translation is found instantly, while a TLB miss requires fetching the mapping from the table in main memory.

