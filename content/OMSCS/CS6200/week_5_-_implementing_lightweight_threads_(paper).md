---
aliases:
course_code: CS6200
course_name: Graduate introduction to Operating Systems
created: 2025-02-09
date_checked: 2026-02-05
draft: false
last_edited: 2025-02-09
tags:
  - OMSCS
title: Week 5 - Implementing Lightweight Threads (paper)
type: paper
week: 5
---

Ref: [Implementing Lightweight threads](https://s3.amazonaws.com/content.udacity-data.com/courses/ud923/references/ud923-stein-shah-paper.pdf)

# Notes

This paper describes an implementation of light weight threads in the SunOS architecture. This is laid out in [Week 5 - Beyond Multiprocessing ... Multithreading and the SunOS Kernel](week_5_-_beyond_multiprocessing_..._multithreading_and_the_sunos_kernel.md).

- If one thread calls exit on the process then all threads will exit.
- Threads have their own signal mask.
- Signals to the process are sent to one of the threads which have that signal unmasked.
	- If all threads have it masked it is left pending on the process until a thread unmasks it.
- Signals can be sent to a particular thread.
- All threads within a process share signal handlers.