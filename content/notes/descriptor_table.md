---
aliases:
  - descriptor table
created: 2025-03-22
date_checked: 2026-02-05
draft: false
last_edited: 2025-03-22
tags:
  - OS
title: Descriptor table
type: definition
---
>[!note] Descriptor table
>In [segmentation](memory_segmentation.md) the [virtual addresses](virtual_memory.md) contain a selector and an offset. The selector relates to some segment descriptor, such as code, data, heap, etc. The *descriptor table* maps this selector to the segment address in [physical memory](physical_memory.md).

