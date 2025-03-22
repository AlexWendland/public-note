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

## Goals

The operation system supports the abstraction of [[Virtual memory|virtual memory]] for processes so it need to:
- Map [[Virtual memory|virtual memory]] onto [[Physical memory|physical memory]].
- Manage what should be in [[Physical memory|physical memory]].
- Validate memory access of processes.

When we speak about memory there are two main abstractions [[Operating system (OS)|OS]] can use for memory:
- [[Paging system]]: This uses [[Memory page|memory pages]] which fixes the size of the smallest unit that can be moved between memory locations. This is the currently the most popular way to manage memory. 
- [[Memory segmentation]]: This uses [[Memory segment|memory segments]] which have variable sizes.



![[Page tables.excalidraw]]


