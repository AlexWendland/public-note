---
aliases:
created: 2023-10-12
date_checked:
draft: false
last_edited: 2026-02-05
tags:
  - programming
title: Chain Hashing
type: data structure
---
>[!definition] Chain Hashing
>This is a form of [Hash table](hash_table.md) ($A$, $h: K \rightarrow A$) who's entries in the [associative array](associative_array.md) are [linked lists](linked_lists.md). Given an element $k \in K$ to add it to this hash table you calculate $h(k)$ then append it to the associated [linked list](linked_lists.md). Then to check if an element $e \in K$ is in your hash table calculate $h(e)$ and then search the associated linked list.
