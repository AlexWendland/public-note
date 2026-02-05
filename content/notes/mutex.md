---
aliases:
  - mutex
  - critical section
  - mutexes
created: 2024-09-04
date_checked: 2026-02-05
draft: false
last_edited: 2026-02-05
tags:
  - OS
title: Mutex
type: definition
---
>[!definition] Mutex
> A *mutex* is a lock on some shared operation between [threads](thread.md). For example accessing shared memory. To do the operation you must obtain the mutex (if some other [thread](thread.md) has the mutex you enter a wait state). The mutex is just a [data structure](data_structure.md) consisting of at least:
> - Status of the mutex,
> - Current mutex owner, and
> - List of threads waiting on the mutex.
>
> Birrells original [API](application_programming_interface_(api).md) used a [context manager](context_manager.md) syntax but common [APIs](application_programming_interface_(api).md) use an lock and unlock command. The code in the [context manager](context_manager.md) or between the lock and unlock commands is called the *critical section*.

