---
aliases:
  - frame
  - memory frames
checked: false
created: 2025-03-22
last_edited: 2025-03-22
publish: false
tags: 
type: definition
---
>[!tldr] Memory frame
>A _frame_ is a fixed-size block of [[Physical memory|physical memory]] used in a [[Paging system|paging system]]. When a process requests memory, its [[Virtual memory|virtual address space]] is divided into [[Memory page|pages]] of the same size, and the [[Operating system (OS)|operating system]] maps these pages to available _frames_ in [[Physical memory|physical memory]]. The [[Memory Management Unit (MMU)|MMU]] handles this mapping using a [[Page tables|page table]]. Since frames and pages are of equal size, paging avoids external fragmentation, though it may introduce internal [[Fragmentation|fragmentation]] if a page does not fully utilize a frame.
