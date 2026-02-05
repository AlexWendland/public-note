---
aliases:
course_code: CS6200
course_name: Graduate introduction to Operating Systems
created: 2025-02-26
date_checked: 2026-02-05
draft: false
last_edited: 2026-02-05
tags:
  - OMSCS
title: Week 7 - Scheduling
type: lecture
week: 7
---
# Additional reading

- [Chip Multithreading Systems Need a New Operating System Scheduler](https://s3.amazonaws.com/content.udacity-data.com/courses/ud923/references/ud923-fedorova-paper.pdf)

# CPU scheduling

In the following section we use the term 'task' to refer to either a Process or a Thread from the point of view of the scheduler, these are the same.

The CPU scheduler picks tasks in the ready queue to run on available CPU's. It runs in the following circumstances:
- There is a free CPU.
- A task becomes ready after completing I/O operations or being created.

The scheduling algorithm is tied to the data structure of the runqueue - the queue that holds the ready tasks.

# Run-to-completion scheduling

This model will run tasks until complete. To discuss this we make simplifications:
- There is a fixed group of tasks.
- We know the execution time of these tasks.
- We will not interrupt tasks once they are running.
- We have a single CPU.

To evaluate different algorithms we will compare different metrics:
- Throughput.
- Average job completion time.
- Average job wait time.
- CPU utilization.

Let's assume we are in a situation with 3 tasks $T1$, $T2$, and $T3$ which take 1, 10 and 1 seconds to complete respectively.

## First come first served (FCFS)

Implements a [FIFO](../../notes/first_in_first_out_(fifo)_queue.md) queue and does tasks in order.

Throughput: 3/12s = 0.25 tasks/s

Average completion time: (1 + 11 + 12) / 3 = 8 secs

Average wait time: (0 + 1 + 11) / 3 = 4 seconds

## Shortest job first (SJF)

Schedule tasks in the order of their execution times.

For this we can make the run queue either an ordered queue with $O(n)$ insertion time but $O(1)$ retrieval time or a ordered tree with $O(log(n))$ insertion time and $O(log(n))$ retrieval time (with re-balancing).

Throughput: 3/12s = 0.25 tasks/s

Average completion time: (1 + 2 + 12) / 3 = 5 secs

Average wait time: (0 + 1 + 2) / 3 = 1 second

# Preemptive scheduling

In this model we now allow the CPU to switch which task it is now working on. We also assume tasks do not arrive at the same time.

| Task | Execution time | Arrival time |
| ---- | ------------- | ------------ |
| $T1$ | 1 sec         | 2            |
| $T2$ | 10 sec        | 0            |
| $T3$ | 1 sec         | 2            |

> [!note] Execution time
> In the real world we don't know the execution time, however we can try to guess it using:
> - How long it ran the last time?
> - How long did it run for the last $n$ runs?

# Preemptive priority scheduling

In this model we not only allow for interruptions but also a priority between tasks. In this model you want to run the highest priority tasks first.

| Task | Execution time | Arrival time | Priority |
| ---- | ------------- | ------------ | -------- |
| $T1$ | 1 sec         | 2            | $P1$     |
| $T2$ | 10 sec        | 0            | $P2$     |
| $T3$ | 1 sec         | 2            | $P3$     |

Where $P1 < P2 < P3$.

We use a data structure to embed the priority of the tasks. This can be achieved by either separate priority queues which get drained in order. Otherwise you can have a tree structure in which the priority is embedded in its subtrees.

## Starvation

If we have a very low priority task, this can never get run if enough higher priority tasks are constantly generated. This can be an issue if it needs to eventually be run.

To avoid this we use *priority aging* we make the priority not just evaluated on its actual priority but on how long it has been in the run queue.

## Priority inversion

If lower priority tasks use mutexes that higher priority tasks requires we can generate a situation in which lots of lower priority tasks all complete before the low priority task holding the mutex unlocks it. This will mean the high priority task will essentially be locked back to the priority of the task that holds the mutex.

To avoid this when a task is holding a mutex, its priority is the max of the priorities of all the tasks that need that mutex. This ensures it will not block higher priority tasks.

