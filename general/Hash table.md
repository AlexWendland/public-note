---
aliases:
  - hash table
chatgpt: false
created: 2023-10-12
last_edited: 2023-10-12
publish: true
tags:
  - programming
type: data structure
---
>[!tldr] Hash table
>This consists of an [[Associative array|associative array]] $A$ and a [[Hash function|hash function]] $f: K \rightarrow A$. Values provided to the hash table get hashed using $f$ which provides a key (usually thought of as a number below a given load value) for $A$. Then the within this entry of $A$ you will store some object that can verify if the value is in this table.
>In an ideal world the [[Hash function|hash function]] $f$ would map each key to a different key of $A$ however this is unlikely to happen in practice. So hash tables need to handle key collision.

