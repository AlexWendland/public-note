---
aliases:
created: 2025-03-23
date_checked: 2026-02-05
draft: false
last_edited: 2026-02-05
tags:
  - OS
title: Buddy Allocator
type: definition
---
>[!note] Buddy Allocator
>The *buddy allocator* is a [memory allocator](memory_allocator.md) used in the [linux](linux.md) kernel to efficiently manage contiguous blocks of memory. It works by dividing memory into blocks of sizes that are powers of 2.
>
>**How it works**
>
>1. **Allocation:**
>   - Memory is initially available as large power-of-2 blocks.
>   - When a request is made, the allocator finds the smallest block that fits the request.
>   - If the block is too large, it recursively splits it into two equal "buddies" until the requested size is reached.
>2. **Deallocation & merging ("Buddy system")**
>   - When memory is freed, the allocator checks whether its **buddy (the adjacent block of the same size)** is also free.
>   - If both buddies are free, they are **merged** back into a larger block.
>   - This process continues up the hierarchy, helping to reduce fragmentation.
>
>**Advantages & trade-offs**
>
>- **Fast allocation & deallocation**: Simple bitwise operations track buddy pairs.
>- **Merging reduces fragmentation**: Helps prevent [external fragmentation](external_fragmentation.md).
>- **[Internal fragmentation](internal_fragmentation.md)**: Requests that don't match a power-of-2 size may waste memory.
>
>![Buddy Allocator](../../static/images/buddy_allocator.png)

