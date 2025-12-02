---
aliases:
  - segmentation
checked: false
created: 2025-03-22
draft: false
last_edited: 2025-03-22
title: Memory segmentation
tags:
  - OS
type: definition
---
>[!tldr] Memory segmentation
>_Segmentation_ is a memory management technique that divides memory into logically distinct [memory segments](memory_segment.md), such as code, data, and stack segments, each with a variable size. Instead of using fixed-size blocks like [paging](paging_system.md), segmentation allows programs to allocate memory dynamically based on their needs. The [operating system](operating_system_(os).md) manages memory through a [descriptor table](descriptor_table.md), which stores the base address and limit of each segment. Segmentation can reduce [internal fragmentation](internal_fragmentation.md) but may lead to [external fragmentation](external_fragmentation.md) without additional management techniques.
