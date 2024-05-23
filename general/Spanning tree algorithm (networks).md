---
aliases: 
checked: false
created: 2024-05-23
last_edited: 2024-05-23
publish: true
tags:
  - programming
type: algorithm
---
# Spanning tree algorithm (networks)

The spanning tree algorithm was introduced to get rid of cycles in [[Network|networks]] that used [[Bridge|bridges]] and [[Hub|hubs]]. It does this by forming a [[Spanning subgraph|spanning]] [[Tree (graph)|tree]] in the network so that the [[Layer 2 Data Link|layer 2]] devices use to send messages through.

This is a [[Distributed algorithm|distributed algorithm]] and is computed locally on each device in the network for their neighbours. Each device will have a unique ID and the tree will be formed by picking the root of the tree to be the device with the lowest ID. Then each device working out its nearest neighbour to the root of the tree. 

This is done iteratively by each device telling its neighbours 3 bits of information:
1. The ID of itself,
2. The node it believes is the root, and
3. The shortest distance between itself and that node.

If it doesn't know of any nodes with lower ID than itself it uses itself as the root with distance 0.

It splits ties of equal distance paths by taking the path that ends in the root with the lowest ID.

It will stop sending configuration messages one
## Pseudocode

```pseudocode
Name(variables):
	Input:
	Output:
1. 
```

## Run time



## Correctness
