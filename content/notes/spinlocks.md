---
aliases:
  - spinlocks
created: 2025-04-08
date_checked: 2026-01-29
draft: false
last_edited: 2025-04-08
tags:
  - OS
title: Spinlocks
type: definition
---
>[!note] Spinlocks
>Spinlocks are a [synchronization](synchronization.md) construct that is similar to [mutexes](mutex.md). When a process tries to acquire the lock whilst another process has it, it will wait at the unlock operation. However, in comparison to a [mutex](mutex.md), the spinlock will not relinquish the [CPU](central_processing_unit_(cpu).md) and instead continues to actively poll for the lock to become available.
