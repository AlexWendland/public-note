---
aliases:
course_code: CS6422
course_name: Database Systems Implementations
created: '2026-06-19'
date_checked:
draft: false
last_edited: '2026-06-19'
tags:
  - OMSCS
title: Week 8 - B+tree
type: lecture
week: 8
---

With a database there are two kinds of queries.

- Point queries - 'Get me person named Alex'

- Range queries - 'Get me all the children between 10 and 18 years old'

Hash tables for indexes work great for point queries.
The execute in $\Theta(1)$ time as we just look for the key Alex.
However, they struggle at 'range queries'.
Here, there is nothing we can really do other than iterate through the keys.
The solution to this is to use an ordered index - which in this course we implement as a B+ tree.

# B+ tree

A B+ tree is a balanced tree where each node can have at most some fixed number $F$ of children - called the fan out.
This means the hight of the tree is always $\ceil \log_F(n) \ceil$.
The keys for the values in the nodes must be linearly order.
The tree has two kinds of nodes - internal nodes and leaf nodes.

The internal nodes hold two data structures, $F$ pointers to other internal nodes and $F-1$ 'dividers'.
If you are querying for value $v$ the dividers tell you which next node to follow by checking $d_{i-1} \leq v < d_i$ then go to node $i$.

The leaf nodes hold the actual values.
This means that they contain two data structures, the first holding the key and the second a pointer to the tuple.
The leaf also nodes a reference to the next right (increase) leaf node.



