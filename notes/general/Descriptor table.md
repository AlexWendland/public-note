---
aliases:
  - descriptor table
checked: false
created: 2025-03-22
draft: false
last_edited: 2025-03-22
tags:
  - OS
type: definition
---
>[!tldr] Descriptor table
>In [[Memory segmentation|segmentation]] the [[Virtual memory|virtual addresses]] contain a selector and an offset. The selector relates to some segment descriptor, such as code, data, heap, ect. The *descriptor table* maps this selector to the segment address in [[Physical memory|physical memory]].

