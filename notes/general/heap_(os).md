---
aliases:
  - heap
checked: false
created: 2023-08-26
draft: false
last_edited: 2023-11-11
tags:
  - programming
  - OS
title: Heap (OS)
type: definition
---
> [!tldr] Heap
> The *heap* of a processes is dynamic memory which is allocated at run time. It will be used to store variables which my vary dramatically in size depending on what the application is run on - for example reading data into memory. This memory will stay allocated until it is explicit de-allocated. Therefore the heap can come with considerable overheads and require techniques like [garbage collection](garbage_collection_(programming).md) or custom allocations to handle.
