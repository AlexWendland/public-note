---
aliases:
  - mutex
  - critical section
  - mutexes
checked: false
created: 2024-09-04
draft: false
last_edited: 2024-09-04
name: Mutex
tags:
  - OS
type: definition
---
>[!tldr] Mutex
> A *mutex* is a lock on some shared operation between [threads](thread.md). For example accessing shared memory. To do the operation you must obtain the mutex (if some other [thread](thread.md) has the mutex you enter a wait state). The mutex is just a [data structure](data_structure.md) consisting of atleast:
> - Status of the mutex,
> - Current mutex owner, and
> - List of threads waiting on the mutex.
>
> Birrells original [API](application_programming_interface_(api).md) used a [context manager](context_manager.md) syntax but common [apis](application_programming_interface_(api).md) use an lock and unlock command. The code in the [context manager](context_manager.md) or between the lock and unlock commands is called the *critical section*.

