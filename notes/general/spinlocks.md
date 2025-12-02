---
aliases:
  - spinlocks
checked: false
created: 2025-04-08
draft: false
last_edited: 2025-04-08
title: Spinlocks
tags:
  - OS
type: definition
---
>[!tldr] Spinlocks
>Spinlocks are a [synchronization](synchronization.md) construct that are similar to [mutexes](mutex.md). When a processes tries to acquire the lock whilst another process has it - it will wait at the unlock operation. However, in comparison to a [mutex](mutex.md) the spinlock will not relinquish the [CPU](central_processing_unit_(cpu).md) instead choosing to keep checking if the lock has become free.

