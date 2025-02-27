---
aliases: 
checked: false
course: "[[CS6200 Graduate introduction to Operating Systems]]"
created: 2025-02-26
last_edited: 2025-02-26
publish: true
tags:
  - OMSCS
type: lecture
week: 7
---
# Week 7 - Scheduling

## Additional reading

- [Chip Multithreading Systems Need a New Operating System Scheduler](https://s3.amazonaws.com/content.udacity-data.com/courses/ud923/references/ud923-fedorova-paper.pdf)

## CPU scheduling

In the following lesson we use the term 'task' to refer to either a Process or a Thread from the point of view of the scheduler these are the same.

The CPU scheduler picks tasks in the ready queue to run on available CPU's. It runs in the following circumstances:
- There is a free CPU.
- A task becomes ready after completing an I/O operations or being created.

The scheduling algorithm is tied to the data structure of the runqueue - the queue that holds the ready tasks.

## Run-to-completion scheduling

This model will run tasks until complete. To discus this we make simplifications:
- There is a fixed group of tasks.
- We know the execution time of these tasks.
- We will not interrupt tasks once they are running. 
- We have a single CPU.

To evaluate different algorithms we will compare different metrics:
- Throughput.
- Average job completion time.
- Average job wait time.
- CPU utilization.

Lets assume we are in a situation with 3 tasks $T1$, $T2$, and $T3$ which take 1, 10 and 1 seconds to complete respectively. 

### First come first served (FCFS)

Implements a [[First in first out (FIFO) queue|FIFO]] queue and does tasks in order.

Throughput: 3/12s = 0.25 tasks/s

Average completion time: (1 + 11 + 12) / 3 = 8 secs

Average wait time: (0 + 1 + 11) / 3 = 4 seconds

### Shortest job first (SJF)

Schedule tasks in the order of their execution times. 

For this we can make the run queue either an ordered queue with $O(n)$ insertion time but $O(1)$ retrieval time or a ordered tree with $O(log(n))$ insertion time and $O(log(n))$ retrieval time (with re-balancing). 

Throughput: 3/12s = 0.25 tasks/s

Average completion time: (1 + 2 + 12) / 3 = 5 secs

Average wait time: (0 + 1 + 2) / 3 = 1 seconds

## Preemptive scheduling

In this model we now allow the CPU to switch which task it is now working on. We also assume tasks do not arrive at the same time.

| Task | Exection time | Arrival time |
| ---- | ------------- | ------------ |
| $T1$ | 1 sec         | 2            |
| $T2$ | 10 sec        | 0            |
| $T3$ | 1 sec         | 2            |

