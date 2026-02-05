---
aliases:
  - semaphores
  - semaphore
created: 2025-03-24
date_checked: 2026-02-05
draft: false
last_edited: 2026-02-05
tags:
  - OS
title: Semaphores
type: definition
---
> [!definition] Semaphores
> **Semaphores** are a [synchronization](synchronization.md) construct used to control access to shared resources. A semaphore is initialized with an integer value (often called the **capacity**). It maintains a counter that represents the number of available "permits." When a [thread](thread.md) attempts to acquire the semaphore:
>
>- If the counter is greater than 0, the thread decrements it and proceeds.
>- If the counter is 0, the thread blocks (waits) until another thread releases the semaphore.
>
> When a thread releases the semaphore, the counter is incremented by 1, potentially waking a waiting thread.
>This mechanism ensures that at most the initial number of threads (the max count) can hold the semaphore concurrently.

