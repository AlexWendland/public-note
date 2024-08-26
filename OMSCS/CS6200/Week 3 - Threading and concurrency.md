---
aliases: 
checked: false
course: "[[CS6200 Graduate introduction to Operating Systems]]"
created: 2024-08-26
last_edited: 2024-08-26
publish: true
tags:
  - OMSCS
type: lecture
week: 3
---
# Week 3 - Threading and concurrency

["An Introduction to Programming with Threads"](https://s3.amazonaws.com/content.udacity-data.com/courses/ud923/references/ud923-birrell-paper.pdf) by Birrell

## Visual metaphor

Threads are like workers in a toy shop:
- is an active entity
	- Executing unit of toy order
- Works simultaneously with others
	- many workers completing toy orders
- requires coordination
	- sharing tools, parts, workstations

In comparison to a thread:
- is an active entity
	- executing unit of a [[Process|process]]
- works simultaneously with others
	- many threads executing
- requires coordination
	- sharing of [[Input output (IO)|IO]] devices, [[Central processing unit (CPU)|CPU]], and [[Virtual memory|virtual memory]].

