---
aliases:
  - spinlocks
checked: false
created: 2025-04-08
last_edited: 2025-04-08
publish: true
tags:
  - OS
type: definition
---
>[!tldr] Spinlocks
>Spinlocks are a [[Synchronization|synchronization]] construct that are similar to [[Mutex|mutexes]]. When a processes tries to acquire the lock whilst another process has it - it will wait at the unlock operation. However, in comparison to a [[Mutex|mutex]] the spinlock will not relinquish the [[Central processing unit (CPU)|CPU]] instead choosing to keep checking if the lock has become free.

