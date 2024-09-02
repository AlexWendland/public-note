---
aliases: 
checked: false
course: "[[CS6200 Graduate introduction to Operating Systems]]"
created: 2024-08-26
last_edited: 2024-08-26
publish: true
tags:
  - OMSCS
type: lecture
week: 3
---
# Week 3 - Threading and concurrency

["An Introduction to Programming with Threads"](https://s3.amazonaws.com/content.udacity-data.com/courses/ud923/references/ud923-birrell-paper.pdf) by Birrell

![[Thread]]

## Visual metaphor

Threads are like workers in a toy shop:
- is an active entity
	- Executing unit of toy order
- Works simultaneously with others
	- many workers completing toy orders
- requires coordination
	- sharing tools, parts, workstations

In comparison to a thread:
- is an active entity
	- executing unit of a [[Process|process]]
- works simultaneously with others
	- many threads executing
- requires coordination
	- sharing of [[Input output (IO)|IO]] devices, [[Central processing unit (CPU)|CPU]], and [[Virtual memory|virtual memory]].

## Difference between a process and a thread

Each [[Process|process]] has its own [[Address space (OS)|address space]] and [[Process control block (PCB)|PCB]] whereas each [[Thread|thread]] in a [[Process|process]] shares the same [[Address space (OS)|address space]], code and data but has its own [[CPU register|CPU registers]], [[Program counter (PC)|program counter]], and [[Stack (OS)|stack]]. A [[Thread|thread]] does not have its own [[Process control block (PCB)|PCB]] but its state is tracked in the [[Process|process]] [[Process control block (PCB)|PCB]].

![[process_vs_thread.png]]

## Benefits of multithreading

Threads allow us to parallelise a process over multiple cores without incurring the code complexity of [[Inter-process communication (IPC)]] or the overhead of multiple [[Process control block (PCB)|PCB]] instances. You can specialise threads for a particular task that needs the same items from the [[Cache|cache]] this allows you to run the task off a hot cache all the time.

Multi-threading on a single core also can be efficient. As one of the largest costs in [[Context switch (CPU)|context switching]] is to remap the [[Address space (OS)|address space]] the time it takes to [[Context switch (CPU)|context switch]] between [[Thread|threads]] is lower than that for [[Process|processes]]. Therefore if you have [[Input output (IO)|I/O]] bound tasks using multi-threading can improve performance.

## Downsides of mulitithreading

Now threads have access to the same [[Virtual memory|virtual memory]] they can perform operations on the same bit of memory which can lead to unintended outcomes. For example two threads incrementing a number leading to the number only being incremented by one.

## Concurrency control mechanisms

### Mutual exclusion

You can limit certain actions to only be carried out by one thread at a time. This is called mutex.

### Threads waiting

Similar to [[Process|processes]] threads can enter a wait state for [[Input output (IO)|I/O]] operations or other conditions. This is controlled by condition variables.

### Threads getting woken up

Threads can also wake each other up.

## Thread creation

Threads interfaces are different between providers. In this course we follow on specific implementation.

Threads have a data-structure that tracks their current state. Containing data like:
- Tread ID,
- Process it belongs to,
- [[CPU register]],
- [[Stack (OS)|stack]],
- attributes.

A [[Thread|thread]] can start another [[Thread|thread]] using the Fork command (not the same as UNIX fork). This takes a program to run and the arguments and starts a new thread.

A [[Thread|thread]] can be terminated using the `join` command which makes the thread calling it wait till the joined thread finishes and then gets any returned value.

>[!note] Different threads execute operations in a non-deterministic manner
> If two threads are safely writing to a list the order of those writes are non-deterministic as it is up to the kernel to schedule them.



