---
aliases: 
checked: false
course: "[[CS6200 Graduate introduction to Operating Systems]]"
created: 2025-03-09
last_edited: 2025-03-09
publish: true
tags:
  - OMSCS
type: lecture
week: 8
---
# Week 8 - Memory management

## Overview

The operation system supports the abstraction of [[Virtual memory|virtual memory]] for processes so it need to:
- Map [[Virtual memory|virtual memory]] onto [[Physical memory|physical memory]].
- Manage what should be in [[Physical memory|physical memory]].
- Validate memory access of processes.

When we speak about memory there are two main abstractions [[Operating system (OS)|OS]] can use for memory:
- [[Paging system]]: This uses [[Memory page|memory pages]] which fixes the size of the smallest unit that can be moved between memory locations. This is the currently the most popular way to manage memory. 
- [[Memory segmentation]]: This uses [[Memory segment|memory segments]] which have variable sizes.

To support these memory mapping there are 3 bits of hardware that take a [[Virtual memory|virtual address]] to a place on [[Random Access Memory (RAM)|RAM]].
- [[Memory Management Unit (MMU)]]: A component on the [[Central processing unit (CPU)|CPU]] that performs the mapping from [[Virtual memory|virtual memory]] to [[Physical memory|physical memory]]. This is also responsible for raising faults for illegal access or accesses that require different permissions.
- [[Translation Lookaside Buffer (TLB)]]: A cache within the [[Memory Management Unit (MMU)|MMU]] to speed up address mappings.
- [[Memory controller]]: A component that maps different sticks of [[Random Access Memory (RAM)|RAM]] into one contiguous physical address space to be used by the [[Memory Management Unit (MMU)|MMU]].

![[memory_hardware.excalidraw]]

## Page tables

![[Page table]]

Note here in [[Paging system|paging]] that the physical address consists of a [[Virtual page number (VPN)|virtual page number]] with an offset.

>[!warning] Offset index
>The minimum addressable unit of memory is a [[Byte|byte]] not a [[Bit|bit]]. So the offset within a [[Memory page|page]] is given in [[Byte|bytes]].

[[Physical memory]] is only allocated to [[Virtual memory|virtual memory]] when it is first referenced. This is identified by the operating system when a [[Physical memory|physical memories]] location is not in a [[Page table|page table]]. When this happens the [[Operating system (OS)|operating system]] takes control and either allocates the memory or swaps something out of [[Random Access Memory (RAM)|RAM]] to provide space for the new memory. This is called 'allocation on first touch'. When a [[Memory page|page]] is removed from [[Random Access Memory (RAM)|RAM]] this is called 'reclaimed'.

![[Page table entry]]


The [[Memory Management Unit (MMU)|MMU]] uses the flags within the [[Page table entry|page table entry]] to determine if the [[Process|processes]] operation on that memory is valid. If not it raises a fault which triggers the kernels page fault handler.

## Page table size

There are two major factors that influence the page table size:
- The [[CPU register|register]] size. I.e. if you are on a 32-[[Bit|bit]] architecture or a 64-[[Bit|bit]] architecture.
- The size of the [[Memory page|pages]]. I.e. What size chunks are you cutting your [[Random Access Memory (RAM)|RAM]] into.

The register size is important as it limits the size of the [[Virtual memory|virtual address]]. The size of the page is important as it determines how large the offset needs to be.

Page sizes are determined by the [[Operating system (OS)|operating system]] but commonly are 4kB, 2MB (large), and 1GB (huge).

![[Page tables.excalidraw]]

>[!example] 32-bit architecture with 4kB page size
>As a [[Byte|byte]] is the smallest addressable size, lets use this as our unit for the below calculations.
>As we have a 32-bit architecture the [[Virtual memory|virtual addresses]] have size 32 [[Bit|bits]].
>As the page size is 2kB = $2^2 * 2^{10} = 2^{12}$B we will need 12 bits for the offset.
>Therefore we are left with 20 bits of the [[Virtual memory|virtual address]] for the [[Virtual page number (VPN)]]. This means there are $2^{20}$ [[Memory page|pages]].
>With this we can now work out the size of the page table. For this architecture, 32-[[Bit|bit]] addresses are 4 [[Byte|bytes]] large which is the size of the [[Page table entry|page table entry]]. We have $2^{20}$ page entries so we get $4 * 2^{20}$B = 4 MB of size.


>[!example] 64-bit architecture with 4kB page size
>If we do the same calculation with a 64-bit architecture we get 64-12 = 62 bits for the number of page table entries. Therefore we get a page table size of $2^{64} * 4$B = 64PB per process! Way too large to hold in memory or disk for most computers!

## Multi-level page tables

![[Multi-level page tables]]

>[!example] Single vs double size comparison
>Suppose we have the same processes running only a 12-[[Bit|bit]] architecture. Though we run it on two different machines where: 
>- the first uses flat page tables, with [[Virtual memory|virtual addresses]] having a 6 bit [[Virtual page number (VPN)|VPN]] and a 6-bit offset, and
>- the second uses 2-level page tables, with the [[Virtual memory|virtual addresses]] having a 2 bit first index and 4 bit second index with a 6-bit offset.
>
>Suppose both of these processes use the first 2kB and last 1kB of memory. How large are the page tables and how many entries do they use?
>
>Notice as they both have 6 bit off sets the page size is $2^6 = 64$B. Therefore the first 2kB = $2^{11}$ B takes the first $2^{11}/2^{6}=2^5 = 32$ entries and the last 1kB takes the last $2^4 = 16$ entries.
>In the flat table the page table has 64 entries in which 48 are used. In the second example the fist table has 4 entries with only 3 of these being used, the second layer has 16 entries and in all 3 tables all of these are used.
>You can see in the second example we had in total 52 page table entries with only 1 not used but in the first we had 64 entries with 16 not being used.

## Inverted page tables

![[Inverted page tables (IPT)]]

## Segmentation

![[Memory segmentation|segmentation]]

![[Descriptor table|descriptor table]]

Normally [[Memory segmentation|segmentation]] is used in conjunction with [[Paging system|paging]]. First use segmentation to cut down the [[Virtual memory|virtual memory]] then using [[Paging system|paging]] to get pages within that segment. 

## Page size

What is the correct page size? This depends on your application, normally page sizes come in 3 different buckets 'regular' about 4kB, 'large' about 2MB and 'huge' about 1GB.

Larger page sizes means smaller [[Page table|page tables]] as the offset does more of the work - however this can lead to [[Internal fragmentation|internal fragmentation]]. Therefore applications that are likely to need large contiguous blocks of memory such as databases are better off with larger or huge table sizes but applications that to store lots of small objects are better off with smaller page tables.

## Memory allocation

![[Memory allocator]]

The main challenge [[Memory allocator|memory allocators]] suffer from is [[External fragmentation|external fragmentation]].

![[External fragmentation]]

The linux kernel has two types of allocators.

![[Buddy Allocator]]

However, the objects the [[Linux|linux]] kernel normally stores are not powers of 2. Causing a lot of [[Internal fragmentation|internal fragmentation]] so another [[Memory allocator|memory allocator]] is also used.

![[Slab allocator]]

## Demand paging

![[Demand paging]]

### When should pages be swapped out?

- When we are nearing full use of the memory.
- When the CPU utilization is low.

### What pages should be swapped out?

- Pages that aren't going to be used in the future.
	- Hard to tell in practice so we use heuristics.
- History-based predictions such as [[ Least-recently used (LRU)|LRU]]
	- Access bit in the [[Page table entry|page table entry]] can be used for this.
- Pages that don't need to be written out.
	- Dirty bit in the [[Page table entry|page table entry]] can be used for this.
- Avoid swapping non-swappable pages, such as some kernel state. Applications can 'pin' their pages to guarantee they stay in memory.

## Copy on write

![[Copy on write (COW)]]

