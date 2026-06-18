---
aliases:
course_code: CS6422
course_name: Database Systems Implementations
created: '2026-06-16'
date_checked: '2026-06-16'
draft: false
last_edited: 2026-06-18
tags:
  - OMSCS
title: Week 7 - Thread-safe hash tables
type: lecture
week: 7
---

In the previous lecture we discussed a hash table.
However, in production we will have multiple threads consistently accessing this.
Therefore we need it to be thread safe to enable concurrent reads and writes.

# Single mutex

The first most trivial way to enable concurrent access is to add a mutex to access the hash table at all.
This means that all operations involving the hash table are serialized.
However, functionally this will make the use of the hash table unbelievably slow.

# std::shared_mutex

The first improvement we can make on a single mutex is to use C++'s shared mutex.
This is functionally a read-write lock.
This means multiple threads can concurrently read the hash table but it will exclusively lock for writing.

# Fine-grained locking

Instead of having a single lock for the whole hash table we can instead provide a shared_mutex for each entry in the hash table.
To support this we add a vector of shared_mutexes and change all our insert/delete/get methods to first acquire this lock.

As we add more shared_mutexes they come with larger and larger overhead.
Therefore a balance needs to be struck between how fine-grained to make the mutex.

# Testing implementations

When testing out different locking implementations it can be hard to do this on live systems.
This is due to the threads and mutexes being controlled by the OS.

- It can be too fast for quantitative testing.

- Non-deterministic behaviour can cause issues.

Therefore, we use a simplified python implementation to let us know how the locks behave under different protocols and access patterns.
This has the downside of being synchronous but comes with upsides:

- Controlled environment to test in.

- Deterministic behaviour.

This works by us taking discrete time steps and allowing threads to try to lock or unlock a resource.
Then we can compare how long it takes for each set of tasks to complete in these discrete time steps.

