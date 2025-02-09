---
aliases: 
checked: false
course: "[[CS6200 Graduate introduction to Operating Systems]]"
created: 2025-02-09
last_edited: 2025-02-09
publish: true
tags:
  - OMSCS
type: lecture
week: 5
---
# Week 5 - Thread design Considerations

## Additional reading

- [Beyond Multiprocessing ... Multithreading the SunOS Kernel](https://s3.amazonaws.com/content.udacity-data.com/courses/ud923/references/ud923-eykholt-paper.pdf)
- [Implementing Lightweight threads](https://s3.amazonaws.com/content.udacity-data.com/courses/ud923/references/ud923-stein-shah-paper.pdf)

## Thread level

We will be revisiting the thread level from [[Week 3 - Threading and concurrency#Thread level]].

![[thread_level_summary.png]]

Key summary:
- Kernel level threads get scheduled on the CPU.
- User level threads get mapped to kernel level threads - this is decided by the user threading library.
	- These are functionally just an abstraction to assist application development.

## Thread data structures

