---
aliases:
checked: false
created: 2025-04-08
draft: false
last_edited: 2025-04-08
name: Monitors
tags:
  - OS
type: definition
---
>[!tldr] Monitors
>*Monitors* are a high-level [synchronization](synchronization.md) construct that encapsulate:
>- A shared resource,
>- A set of [mutexes](mutex.md) (or equivalent) to enforce mutual exclusion, and
>- One or more [conditional variables](conditional_variables_(mutex).md) used for managing waiting and signaling between threads.
>
>A monitor typically exposes an API consisting of entry procedures (methods), and ensures that:
>
>- Entering threads abide by the prescribed entry conditions,
>- Threads can wait on a condition (e.g. “buffer not empty”), releasing the lock temporarily, and
>- Other threads can signal those waiting threads when the condition becomes true.
>
>The monitor takes care of **locking**, **unlocking**, **waiting**, and **signaling** internally, so the user doesn't have to manually manage these lower-level details.

