---
aliases:
  - heap
created: 2023-08-26
date_checked: 2026-01-28
draft: false
last_edited: 2026-01-28
tags:
  - programming
  - OS
title: Heap (OS)
type: definition
---
> [!definition] Heap
> The *heap* of a process is dynamic memory which is allocated at run time. It will be used to store variables which may vary dramatically in size depending on what the application is run on - for example reading data into memory. This memory will stay allocated until it is explicitly deallocated. Therefore the heap can come with considerable overheads and require techniques like [garbage collection](garbage_collection_(programming).md) or custom allocations to handle.
