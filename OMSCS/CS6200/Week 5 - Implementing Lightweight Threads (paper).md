---
aliases: 
checked: false
course: "[[CS6200 Graduate introduction to Operating Systems]]"
created: 2025-02-09
last_edited: 2025-02-09
publish: true
tags:
  - OMSCS
type: paper
week: 5
---
# Week 5 - Implementing Lightweight Threads (paper)

Ref: [Implementing Lightweight threads](https://s3.amazonaws.com/content.udacity-data.com/courses/ud923/references/ud923-stein-shah-paper.pdf)

## Notes

This paper describes an implementation of light weight threads in the SunOS architecture. This is laid out in [[Week 5 - Beyond Multiprocessing ... Multithreading and the SunOS Kernel]].

- If one thread calls exit on the process then all threads will exit.
- Threads have there own signal mask.
- Signals to the process are sent to one of the threads which have that signal unmasked.
	- If all threads have it masked it is left pending on the process until a thread unmasks it.
- Signals can be sent to a particular thread.
- All threads within a process share signal handlers.
- 