---
aliases:
  - linked list
  - linked lists
  - double linked list
  - double linked lists
checked: false
created: 2023-10-12
draft: false
last_edited: 2023-11-11
title: Linked lists
tags:
  - programming
type: data structure
---
>[!tldr] Linked list
>A linked list stores a collect of elements of the same data type. The data structure consists of a set of sequential nodes. Each node has the following information
>1. The element we are storing at this position, and
>2. A pointer to the next node.
>If it is a *double linked list* it also has a 3rd element:
>3. A pointer to the previous node.
>
>The next pointer at the last node and the previous pointer at the first node are null.
>
>Linked lists have [spacial complexity](spacial_complexity.md) of $O(n)$ but the also have overhead of $O(n)$ to store the additional points.
>
>This has the following operations:
>- Access: $O(n)$ by index
>- Search: $O(n)$ you have to go through the whole list
>- Insert, delete, update:
>	- $O(1)$ at the beginning
>	- $O(n)$ at an index

# Trade offs

Linked lists are good data structures when you don't know the size of the information that the beginning. To add or delete elements only requires updating a couple of points whereas in an [array](array_(data_structure).md) it may involve copying a lot of data. This also allows for storing different bits of the list in different memory locations - this can have some efficiency losses if you do it too much.

However looking up elements by index is very slow in comparison to an [array](array_(data_structure).md) whereas it has the same speed as going through the whole data structure.
