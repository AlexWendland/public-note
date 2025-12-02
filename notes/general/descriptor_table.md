---
aliases:
  - descriptor table
checked: false
created: 2025-03-22
draft: false
last_edited: 2025-03-22
title: Descriptor table
tags:
  - OS
type: definition
---
>[!tldr] Descriptor table
>In [segmentation](memory_segmentation.md) the [virtual addresses](virtual_memory.md) contain a selector and an offset. The selector relates to some segment descriptor, such as code, data, heap, ect. The *descriptor table* maps this selector to the segment address in [physical memory](physical_memory.md).

