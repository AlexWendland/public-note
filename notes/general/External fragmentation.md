---
aliases:
  - external fragmentation
checked: false
created: 2025-03-22
last_edited: 2025-03-22
draft: false
tags:
  - OS
type: definition
---
>[!tldr] External fragmentation
>_External fragmentation_ occurs when free memory is split into small, non-contiguous blocks, making it impossible to allocate a large contiguous block despite having enough total free space. This happens in systems that use variable-sized allocations (e.g., [[Memory segmentation|segmentation]] or [[Heap (OS)|heap]] memory management). For example if a program repeatedly allocates and frees different-sized memory chunks, gaps form between allocated blocks, preventing large allocations.
>![external_fragmenation](../../images/excalidraw/external_fragmenation.excalidraw.svg)

