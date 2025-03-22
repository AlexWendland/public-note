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

Page sizes are determined by the [[Operating system (OS)|operating system]] but commonly are (4kB, 8kB, 2MB, 4MB, 1GB).

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

