---
aliases:
course_code: CS6200
course_name: Graduate introduction to Operating Systems
created: 2025-03-09
date_checked: 2026-02-05
draft: false
last_edited: 2026-02-05
tags:
  - OMSCS
title: Week 8 - Memory management
type: lecture
week: 8
---
# Overview

The operating system supports the abstraction of [virtual memory](../../notes/virtual_memory.md) for processes so it needs to:
- Map [virtual memory](../../notes/virtual_memory.md) onto [physical memory](../../notes/physical_memory.md).
- Manage what should be in [physical memory](../../notes/physical_memory.md).
- Validate memory access of processes.

When we speak about memory there are two main abstractions [OS](../../notes/operating_system_(os).md) can use for memory:
- [Paging system](../../notes/paging_system.md): This uses [memory pages](../../notes/memory_page.md) which fixes the size of the smallest unit that can be moved between memory locations. This is currently the most popular way to manage memory.
- [Memory segmentation](../../notes/memory_segmentation.md): This uses [memory segments](../../notes/memory_segment.md) which have variable sizes.

To support these memory mappings there are 3 hardware components that take a [virtual address](../../notes/virtual_memory.md) to a place on [RAM](../../notes/random_access_memory_(ram).md).
- [Memory Management Unit (MMU)](../../notes/memory_management_unit_(mmu).md): A component on the [CPU](../../notes/central_processing_unit_(cpu).md) that performs the mapping from [virtual memory](../../notes/virtual_memory.md) to [physical memory](../../notes/physical_memory.md). This is also responsible for raising faults for illegal access or accesses that require different permissions.
- [Translation Lookaside Buffer (TLB)](../../notes/translation_lookaside_buffer_(tlb).md): A cache within the [MMU](../../notes/memory_management_unit_(mmu).md) to speed up address mappings.
- [Memory controller](../../notes/memory_controller.md): A component that maps different sticks of [RAM](../../notes/random_access_memory_(ram).md) into one contiguous physical address space to be used by the [MMU](../../notes/memory_management_unit_(mmu).md).

![memory_hardware](../../../static/images/excalidraw/memory_hardware.excalidraw.svg)

# Page tables

[Page table](../../notes/page_table.md)

Note here in [paging](../../notes/paging_system.md) that the virtual address consists of a [virtual page number](../../notes/virtual_page_number_(vpn).md) with an offset.

>[!warning] Offset index
>The minimum addressable unit of memory is a [byte](../../notes/byte.md) not a [bit](../../notes/bit.md). So the offset within a [page](../../notes/memory_page.md) is given in [bytes](../../notes/byte.md).

[Physical memory](../../notes/physical_memory.md) is only allocated to [virtual memory](../../notes/virtual_memory.md) when it is first referenced. This is identified by the operating system when a [physical memory](../../notes/physical_memory.md) location is not in a [page table](../../notes/page_table.md). When this happens the [operating system](../../notes/operating_system_(os).md) takes control and either allocates the memory or swaps something out of [RAM](../../notes/random_access_memory_(ram).md) to provide space for the new memory. This is called 'allocation on first touch'. When a [page](../../notes/memory_page.md) is removed from [RAM](../../notes/random_access_memory_(ram).md) this is called 'reclaimed'.

[Page table entry](../../notes/page_table_entry.md)


The [MMU](../../notes/memory_management_unit_(mmu).md) uses the flags within the [page table entry](../../notes/page_table_entry.md) to determine if the [process](../../notes/process.md)'s operation on that memory is valid. If not it raises a fault which triggers the kernel's page fault handler.

# Page table size

There are two major factors that influence the page table size:
- The [register](../../notes/cpu_register.md) size. I.e. if you are on a 32-[bit](../../notes/bit.md) architecture or a 64-[bit](../../notes/bit.md) architecture.
- The size of the [pages](../../notes/memory_page.md). I.e. What size chunks are you cutting your [RAM](../../notes/random_access_memory_(ram).md) into.

The register size is important as it limits the size of the [virtual address](../../notes/virtual_memory.md). The size of the page is important as it determines how large the offset needs to be.

Page sizes are determined by the [operating system](../../notes/operating_system_(os).md) but commonly are 4kB, 2MB (large), and 1GB (huge).

![Page tables](../../../static/images/excalidraw/Page_tables.excalidraw.svg)

>[!example] 32-bit architecture with 4kB page size
>As a [byte](../../notes/byte.md) is the smallest addressable size, lets use this as our unit for the below calculations.
>As we have a 32-bit architecture the [virtual addresses](../../notes/virtual_memory.md) have size 32 [bits](../../notes/bit.md).
>As the page size is 4kB = $2^2 * 2^{10} = 2^{12}$B we will need 12 bits for the offset.
>Therefore we are left with 20 bits of the [virtual address](../../notes/virtual_memory.md) for the [Virtual page number (VPN)](../../notes/virtual_page_number_(vpn).md). This means there are $2^{20}$ [pages](../../notes/memory_page.md).
>With this we can now work out the size of the page table. For this architecture, 32-[bit](../../notes/bit.md) addresses are 4 [bytes](../../notes/byte.md) large which is the size of the [page table entry](../../notes/page_table_entry.md). We have $2^{20}$ page entries so we get $4 * 2^{20}$B = 4 MB of size.


>[!example] 64-bit architecture with 4kB page size
>If we do the same calculation with a 64-bit architecture we get 64-12 = 62 bits for the number of page table entries. Therefore we get a page table size of $2^{64} * 4$B = 64PB per process! Way too large to hold in memory or disk for most computers!

# Multi-level page tables

[Multi-level page tables](../../notes/multi-level_page_tables.md)

>[!example] Single vs double size comparison
>Suppose we have the same processes running only a 12-[bit](../../notes/bit.md) architecture. Though we run it on two different machines where:
>- the first uses flat page tables, with [virtual addresses](../../notes/virtual_memory.md) having a 6 bit [VPN](../../notes/virtual_page_number_(vpn).md) and a 6-bit offset, and
>- the second uses 2-level page tables, with the [virtual addresses](../../notes/virtual_memory.md) having a 2 bit first index and 4 bit second index with a 6-bit offset.
>
>Suppose both of these processes use the first 2kB and last 1kB of memory. How large are the page tables and how many entries do they use?
>
>Notice as they both have 6 bit off sets the page size is $2^6 = 64$B. Therefore the first 2kB = $2^{11}$ B takes the first $2^{11}/2^{6}=2^5 = 32$ entries and the last 1kB takes the last $2^4 = 16$ entries.
>In the flat table the page table has 64 entries in which 48 are used. In the second example the first table has 4 entries with only 3 of these being used, the second layer has 16 entries and in all 3 tables all of these are used.
>You can see in the second example we had in total 52 page table entries with only 1 not used but in the first we had 64 entries with 16 not being used.

# Inverted page tables

[Inverted page tables (IPT)](../../notes/inverted_page_tables_(ipt).md)

# Segmentation

[segmentation](../../notes/memory_segmentation.md)

[descriptor table](../../notes/descriptor_table.md)

Normally [segmentation](../../notes/memory_segmentation.md) is used in conjunction with [paging](../../notes/paging_system.md). First use segmentation to cut down the [virtual memory](../../notes/virtual_memory.md) then using [paging](../../notes/paging_system.md) to get pages within that segment.

# Page size

What is the correct page size? This depends on your application, normally page sizes come in 3 different buckets 'regular' about 4kB, 'large' about 2MB and 'huge' about 1GB.

Larger page sizes mean smaller [page tables](../../notes/page_table.md) as the offset does more of the work - however this can lead to [internal fragmentation](../../notes/internal_fragmentation.md). Therefore applications that are likely to need large contiguous blocks of memory such as databases are better off with larger or huge table sizes but applications that store lots of small objects are better off with smaller page tables.

# Memory allocation

[Memory allocator](../../notes/memory_allocator.md)

The main challenge [memory allocators](../../notes/memory_allocator.md) suffer from is [external fragmentation](../../notes/external_fragmentation.md).

[External fragmentation](../../notes/external_fragmentation.md)

The linux kernel has two types of allocators.

[Buddy Allocator](../../notes/buddy_allocator.md)

However, the objects the [linux](../../notes/linux.md) kernel normally stores are not powers of 2. Causing a lot of [internal fragmentation](../../notes/internal_fragmentation.md) so another [memory allocator](../../notes/memory_allocator.md) is also used.

[Slab allocator](../../notes/slab_allocator.md)

# Demand paging

[Demand paging](../../notes/demand_paging.md)

## When should pages be swapped out?

- When we are nearing full use of the memory.
- When the CPU utilization is low.

## What pages should be swapped out?

- Pages that aren't going to be used in the future.
	- Hard to tell in practice so we use heuristics.
- History-based predictions such as [LRU](../../notes/least-recently_used_(lru).md)
	- Access bit in the [page table entry](../../notes/page_table_entry.md) can be used for this.
- Pages that don't need to be written out.
	- Dirty bit in the [page table entry](../../notes/page_table_entry.md) can be used for this.
- Avoid swapping non-swappable pages, such as some kernel state. Applications can 'pin' their pages to guarantee they stay in memory.

# Copy on write

[Copy on write (COW)](../../notes/copy_on_write_(cow).md)

# Checkpointing

[Checkpointing](../../notes/checkpointing.md)

