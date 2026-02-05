---
aliases:
  - external fragmentation
created: 2025-03-22
date_checked: 2026-02-05
draft: false
last_edited: 2026-02-05
tags:
  - OS
title: External fragmentation
type: definition
---
>[!definition] External fragmentation
>_External fragmentation_ occurs when free memory is split into small, non-contiguous blocks, making it impossible to allocate a large contiguous block despite having enough total free space. This happens in systems that use variable-sized allocations (e.g., [segmentation](memory_segmentation.md) or [heap](heap_(os).md) memory management). For example, if a program repeatedly allocates and frees different-sized memory chunks, gaps form between allocated blocks, preventing large allocations.
>![external_fragmentation](../../static/images/excalidraw/external_fragmentation.excalidraw.svg)

