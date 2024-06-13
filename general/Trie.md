---
aliases:
  - trie
  - prefix tree
checked: false
created: 2024-06-13
last_edited: 2024-06-13
publish: true
tags:
  - programming
type: data structure
---
>[!tldr] Trie
>A *trie* or *prefix tree* is used for associating words in a given alphabet $A$ to some values in $X$. 
>- This is given by a rooted [[Tree (graph)|tree]] $(T = (V, E), r)$.
>- An edge letter map $a: E \rightarrow A$, where no to edges sharing a node at the same distance from the root have the same letter.
>- A node key map $k: V \rightarrow X \cup \{ - \}$ where $-$ is a null value.
>Then every word $w = w_1 w_2 \ldots w_{n-1} w_n$ in $A$ has a path $p 

