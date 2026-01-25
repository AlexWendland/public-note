---
aliases:
  - hash table
created: 2023-10-12
date_checked:
draft: false
last_edited: 2023-11-11
tags:
  - programming
title: Hash table
type: data structure
---
>[!tldr] Hash table
>This consists of an [associative array](associative_array.md) $A$ and a [hash function](hash_function.md) $f: K \rightarrow A$. Values provided to the hash table get hashed using $f$ which provides a key (usually thought of as a number below a given load value) for $A$. Then the within this entry of $A$ you will store some object that can verify if the value is in this table.
>In an ideal world the [hash function](hash_function.md) $f$ would map each key to a different key of $A$ however this is unlikely to happen in practice. So hash tables need to handle key collision.

