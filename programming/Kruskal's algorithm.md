---
aliases: 
type: algorithm
publish: true
created: 2023-10-01
last_edited: 2023-10-01
tags:
  - programming
chatgpt: false
---
# Kruskal's algorithm

This is an algorithm to solve the [[Minimum Spanning Tree problem (MST)|MST]] problem. 

## Pseudocode

```pseudocode
Kruskal's(G):
	Input: undirected graph G=(V,E) with weights w(e).
	Output: MST edges X
1. Sort E by weights, smallest to largest
2. Set X to be empty
3. For e = (v,w) in E (ordered)
	1. If X U e does't have a cycle then X = X U e.
4. Output X
```