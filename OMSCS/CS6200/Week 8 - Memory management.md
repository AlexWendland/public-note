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

![[Page tables]]

Note here in [[Paging system|paging]] that the physical address consists of a [[Virtual page number|virtual page number]] with an offset.

>[!warning] [[Byte|Bytes]]
>The minimum addressable unit of memory is a [[Byte|byte]] not a bit. So the offset within a [[Memory page|page]] is given in [[Byte|bytes]].

![[Page tables.excalidraw]]

[[Physical memory]] is only allocated to [[Virtual memory|virtual memory]] when it is first referenced. This is identified by the operating system when a [[Physical memory|physical memories]] location is not in a [[Page tables|page table]] 

