---
aliases:
  - page tables
  - page
  - page table
checked: false
created: 2024-08-26
draft: false
last_edited: 2024-08-26
tags:
  - OS
  - computer-science
type: definition
---
>[!tldr] Page table
>A *page table* maps addresses in the [[Virtual memory|virtual address space]] of a [[Process|process]] which is indexed by the [[Virtual page number (VPN)|virtual page number]] and an offset within that page. The [[Virtual page number (VPN)|virtual page number]] is mapped to a [[Physical Frame Number (PFN)|physical frame number]] which combined with the offset can identify a location in [[Physical memory|physical memory]].
>The simplest way to do this is with flat page tables. This is a page table contains one entry for each [[Virtual page number (VPN)|virtual page number]] which is the index in the page table. The [[Page table entry|page table entry]] then consists of the [[Physical Frame Number (PFN)|physical frame number]] a long with some management [[Bit|bits]] which inform the [[Operating system (OS)|operating system]] if the memory mapping is valid, what permissions the [[Process|process]] has for this memory.
>To then do the mapping it sums the offset from the [[Virtual memory|virtual address]] with the [[Physical Frame Number (PFN)|physical frame number]] in the page table to get the [[Physical memory|physical address]].
>Other page table types exist such as [[Multi-level page tables]] or [[Inverted page tables (IPT)]].

