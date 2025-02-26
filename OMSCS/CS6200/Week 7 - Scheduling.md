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

