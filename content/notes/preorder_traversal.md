---
aliases:
checked: false
created: '2026-02-13'
draft: false
last_edited: '2026-02-13'
tags:
title: Preorder traversal
type: definition
---

> [!definition] Preorder traversal
> Given a rooted [tree](/content/notes/tree_%28graph%29.md) where for every vertex we have a given ordering on the children.
> The preorder traversal visits nodes by: (1) processing the current node, then (2) recursively visiting all children in their given order from left to right.
>
> The "pre" in preorder means the parent node is processed **before** its descendants.

> [!example] A simple example
> Consider the following tree:
> ![Simple tree](../../static/images/graphviz/tree_algorithms_example.gv.svg)
> Suppose we traverse nodes left to right.
> Then the preorder traversal is: 2, 1, 7, 4, 0, 5, 3, 6.

> [!note] Relation to depth first search
> Preorder traversal is one way to implement a [depth first search](/content/notes/dfs_tree_%28algorithm%29.md) on a tree. DFS is a general traversal strategy that explores as far as possible along each branch before backtracking. Preorder specifically processes nodes before visiting their descendants.
