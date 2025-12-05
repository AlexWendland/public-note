---
aliases:
  - array
checked: false
created: 2023-10-12
draft: false
last_edited: 2025-12-05
tags:
  - programming
title: Array (data structure)
type: data structure
---
> [!definition] Array
> This data structure consists of a collection of elements of the same memory size, where each one is identified by an index. This comes with a function to map index's to memory location of each element. (This is normally integer index with a contiguous memory block.) These can *static* where you fix the size of the array before hand or *dynamic* where you allow the array size to change.
>
>This has [spacial complexity](spacial_complexity.md) of $O(n)$ to store $n$ elements and $O(1)$ overhead if the indexing function is sufficiently simple.
>
> This has the following operations:
> - Access: $O(1)$
> - Update: $O(1)$
> - Copy: $O(n)$
> If this is a *dynamic array* meaning you can resize it, it will also have
> - Insert
> 	- $O(1)$ if at the end
> 	- $O(n)$ in a given position
> - Delete
> 	- $O(1)$ if at the end
> 	- $O(n)$ in a given position



