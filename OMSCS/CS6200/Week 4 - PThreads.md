---
aliases: 
checked: false
course: "[[CS6200 Graduate introduction to Operating Systems]]"
created: 2024-09-04
last_edited: 2024-09-04
publish: true
tags:
  - OMSCS
type: lecture
week: 4
---
# Week 4 - PThreads

![[Portable operating system interface (POSIX)|POSIX]]

![[POSIX threads (PThreads)|PThreads]]

## Thread interface

The core [[Data structure|data structure]] in the [[POSIX threads (PThreads)|PThreads]] library is `pthread_t` which represents a thread. This can be created through:
```
int pthread_create(
	pthread_t *thread,
	const pthread_attr_t *attr,
	void * (*start_routine)(void *),
	void *arg
)
```