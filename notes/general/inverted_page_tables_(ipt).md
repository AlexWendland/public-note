---
aliases:
  - IPT
checked: false
created: 2025-03-23
draft: false
last_edited: 2025-03-23
name: Inverted page tables (IPT)
tags:
  - OS
type: definition
---
>[!tldr] Inverted page tables
>Traditional [page tables](page_tables.md) are indexed by [virtual addresses](virtual_memory.md), but on 64-bit architectures, the virtual address space can be many petabytes, while physical memory is usually much smaller (gigabytes or terabytes). This results in large [page tables](page_table.md), consuming significant memory.
>
>An *inverted page table (IPT)* solves this by indexing entries by physical page frame rather than by virtual address. Each entry stores the [PID](process_identification_(pid).md) and [Virtual page number (VPN)](virtual_page_number_(vpn).md) to uniquely identify which process and virtual address map to that physical frame.
>
> This causes slow lookups, as searching by virtual address requires a linear search, which is inefficient. Many systems use a [hash table](hash_table.md) to speed up lookups. The [Translation Lookaside Buffer (TLB)](translation_lookaside_buffer_(tlb).md) caches recent translations, avoiding frequent IPT lookups.

