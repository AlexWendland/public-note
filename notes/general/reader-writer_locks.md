---
aliases:
checked: false
created: 2025-04-08
draft: false
last_edited: 2025-04-08
name: Reader-writer locks
tags:
  - OS
type: definition
---
>[!tldr] Reader-writer locks
A reader-writer lock is a [synchronization](synchronization.md) construct that allows multiple threads to read shared data concurrently, while ensuring exclusive access for a thread that needs to write. It supports two types of locking:
>
>- **Read lock**: Multiple threads can acquire the read lock simultaneously, as long as no thread holds the write lock.
>- **Write lock**: Only one thread can hold the write lock at a time, and no other thread (reader or writer) may hold the lock concurrently.
>
>Reader-writer locks typically expose two distinct interfaces — one for acquiring and releasing the read lock, and one for the write lock — with internal coordination to ensure mutual exclusion between readers and writers when necessary.

