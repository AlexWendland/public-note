---
aliases: null
chatgpt: false
created: 2023-09-29
last_edited: 2023-09-29
publish: true
tags:
  - programming
type: algorithm
---
## Finding paths in a [[Directed graph|directed graph]] via [[Depth-first search (DFS)|DFS]]

To do this we are going to use a [[Depth-first search (DFS)|DFS]] algorithm like [[]] but we are going to track pre/postorder numbers.

```pseudocode
DFS(G)
  input: G = (V,E) in adjacency list representation
  output: Vertices labelled by connected components
    clock = 1
    for all v in V, set visited(v) = False
    for all v in V
      if not visited(v) then
        explore(v)
  return post (defined in Explore)
```

```pseudocode
Explore(z)
  input: vertex z
    pre(z) = clock, clock ++
    visited(z) = True
    for all (z, w) in E
      if not visited(w)
        Explore(w)
	post(z) = clock, clock++
```

### Example

Suppose we have the following graph and let $B$ be the root node. Suppose we explore edges alphabetically and lets run the algorithm above on it.

![[dfs_example.png]]

As we are using [[Depth-first search (DFS)|DFS]] we explore far first and then slowly come back. Which gives us the following [[DFS tree (algorithm)|DFS tree]] with the pre/post numbers.

![[pre_post_calculation_example.png]]

| Letter | Pre | Post |
| ------ | --- | ---- |
| A      | 2   | 11   |
| B      | 1   | 16   |
| C      | 12  | 15   |
| D      | 3   | 10   |
| E      | 4   | 7    |
| F      | 13  | 15   |
| G      | 5   | 6    |
| H      | 8   | 9    |
