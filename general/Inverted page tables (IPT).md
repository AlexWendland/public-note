---
aliases:
  - IPT
checked: false
created: 2025-03-23
last_edited: 2025-03-23
publish: true
tags:
  - OS
type: definition
---
>[!tldr] Inverted page tables
>Traditional [[page tables]] are indexed by [[Virtual memory|virtual addresses]], but on 64-bit architectures, the virtual address space can be many petabytes, while physical memory is usually much smaller (gigabytes or terabytes). This results in large [[Page table|page tables]], consuming significant memory.
>
>An *inverted page table (IPT)* solves this by indexing entries by physical page frame rather than by virtual address. Each entry stores the [[Process Identification (PID)|PID]] and [[Virtual page number (VPN)]] to uniquely identify which process and virtual address map to that physical frame.
> 
> This causes slow lookups, as searching by virtual address requires a linear search, which is inefficient. Many systems use a [[Hash table|hash table]] to speed up lookups. The [[Translation Lookaside Buffer (TLB)]] caches recent translations, avoiding frequent IPT lookups.

