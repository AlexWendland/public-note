---
aliases:
checked: false
created: '2026-02-13'
draft: false
last_edited: '2026-02-13'
tags:
title: Postorder traversal
type: definition
---

> [!definition] Postorder traversal
> Given a rooted [tree](/content/notes/tree_%28graph%29.md) where for every vertex we have a given ordering on the children.
> The postorder traversal visits nodes by: (1) recursively visiting all children in their given order from left to right, then (2) processing the current node.
>
> The "post" in postorder means the parent node is processed **after** its descendants.

> [!example] A simple example
> Consider the following tree:
> ![Simple tree](../../static/images/graphviz/tree_algorithms_example.gv.svg)
> Suppose we traverse nodes left to right.
> Then the postorder traversal is: 1, 4, 3, 6, 5, 0, 7, 2.

> [!note] Relation to depth first search
> Postorder traversal is one way to implement a [depth first search](/content/notes/dfs_tree_%28algorithm%29.md) on a tree. DFS is a general traversal strategy that explores as far as possible along each branch before backtracking. Postorder specifically processes nodes after visiting their descendants.
