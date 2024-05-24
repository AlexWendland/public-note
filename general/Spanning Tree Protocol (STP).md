---
aliases:
  - STP
checked: false
created: 2024-05-23
last_edited: 2024-05-23
publish: true
tags:
  - programming
type: algorithm
---
# Spanning Tree Protocol (STP)

The spanning tree protocol was introduced to get rid of cycles in [[Network|networks]] that used [[Bridge|bridges]] and [[Hub|hubs]]. It does this by forming a [[Spanning subgraph|spanning]] [[Tree (graph)|tree]] in the network so that the [[Layer 2 Data Link|layer 2]] devices use to send messages through.

This is a [[Distributed algorithm|distributed algorithm]] and is computed locally on each device in the network for their neighbours. Each device will have a unique ID and the tree will be formed by picking the root of the tree to be the device with the lowest ID. Then each device working out its nearest neighbour to the root of the tree. 

This is done iteratively by each device telling its neighbours 4 bits of information:
1. The ID of itself,
2. The node it believes is the root, 
3. The shortest distance between itself and that node, and 
4. If this host thinks that node is the next node in the shortest path to the root.

Once it receives a configuration message, it then recalculates what it thinks is the new root and its shortest distance to that root. It then tells all its neighbours about its new status.

To calculate the spanning tree it keeps track of which node is its next nearest neighbour to the root. It splits ties of equal distance paths by taking the path that ends in the root with the lowest ID.

To calculate the set of active connections a node keeps track of which node is the next node in the shortest path to the root and the nodes that think it is the next node in the shortest path to the root. These nodes are the nodes that are considered active links.

When broadcasting and flooding all switches still send messages to all links but a [[Switch|switch]] only forwards or floods a message it receives on an active connection.

When switches implement