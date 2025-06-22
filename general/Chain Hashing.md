---
aliases: null
checked: false
created: 2023-10-12
last_edited: 2023-11-11
draft: false
tags:
  - programming
type: data structure
---
>[!tldr] Chain Hashing
>This is a form of [[Hash table]] ($A$, $h: K \rightarrow A$) who's entries in the [[Associative array|associative array]] are [[Linked lists|linked lists]]. Given an element $k \in K$ to add it to this hash table you calculate $h(k)$ then append it to the associated [[Linked lists|linked list]]. Then to check if an element $e \in K$ is in your hash table calculate $h(e)$ and then search the associated linked list.
