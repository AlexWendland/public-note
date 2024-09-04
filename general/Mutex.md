---
aliases:
  - mutex
  - critical section
checked: false
created: 2024-09-04
last_edited: 2024-09-04
publish: true
tags:
  - OS
type: definition
---
>[!tldr] Mutex
> A *mutex* is a lock on some shared operation between [[Thread|threads]]. For example accessing shared memory. To do the operation you must obtain the mutex (if some other [[Thread|thread]] has the mutex you enter a wait state). The mutex is just a [[Data structure|data structure]] consisting of atleast:
> - Status of the mutex,
> - Current mutex owner, and
> - List of threads waiting on the mutex.
> 
> Birrells original [[Application Programming Interface (API)|API]] used a [[Context manager|context manager]] syntax but common [[Application Programming Interface (API)|apis]] use an lock and unlock command. The code in the [[Context manager|context manager]] or between the lock and unlock commands is called the critical [[section]].

