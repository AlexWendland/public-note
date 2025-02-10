---
aliases: 
checked: false
course: "[[CS6200 Graduate introduction to Operating Systems]]"
created: 2025-02-09
last_edited: 2025-02-09
publish: true
tags:
  - OMSCS
type: lecture
week: 5
---
# Week 5 - Thread design Considerations

## Additional reading

- [Beyond Multiprocessing ... Multithreading the SunOS Kernel](https://s3.amazonaws.com/content.udacity-data.com/courses/ud923/references/ud923-eykholt-paper.pdf)
- [Implementing Lightweight threads](https://s3.amazonaws.com/content.udacity-data.com/courses/ud923/references/ud923-stein-shah-paper.pdf)

## Thread level

We will be revisiting the thread level from [[Week 3 - Threading and concurrency#Thread level]].

![[thread_level_summary.png]]

Key summary:
- Kernel level threads get scheduled on the CPU.
- User level threads get mapped to kernel level threads - this is decided by the user threading library.
	- These are functionally just an abstraction to assist application development.

## Thread data structures

![[thread_data_structures.excalidraw]]

In previous lecturers we spoke about a [[Process control block (PCB)]] as a single entity. However, when adding threads into the equation it is more convent to break this down into the bit.
- The hard state that is shared by all threads - like the memory mapping, 
- the soft state that is shared by some threads like how to handle signals and system calls, and
- the thread specific state like its current stack and registers.

As we discussed previously the threading library (which can be different for each process) controls the mapping between the user threads and the kernel threads. The kernel threads are the 'real' threads from the perspective of the CPU - these get scheduled onto the CPU. The user threads are not known by the CPU, it is the responsibility of the threading library to map these onto the kernel threads to be executed. This can be done in multiple relationships that have upsides and downsides.
- Many user threads to one kernel threads. This was mainly used by old programming languages, whilst allowing for some parallelism if one threads is mapped onto the kernel thread and uses an I/O operation it blocks all user threads.
- 1:1, common in modern programming languages like pthreads in c. Allows for the most parallelism but decreases portability as it demands a lot of resources from the system it is running on and increases the amount of overhead as it needs a kernel operation to switch user level threads.
- Many to many, balance between both - allows for parallelism whilst also making optimizations to not need so many context switches. Used in programming languages like go. 

The process control block go broken down into small components to increase:
- Scalability,
- Reduce overheads,
- Increase performance, and
- Make the system more flexible.

In a single [[Process control block (PCB)|PCB]] we have:
- Large continuous data structure - decreasing scalability.
- This is private for each entity such as thread - which increases overheads.
- This needs to be saved and restored on each context swich - decreasing performance.
- Would need to update the whole data structure for any change - making the structure less flexible.

With the broken down state we:
- Have smaller data structures - increasing scalability.
- They are easier to share and reference - decreasing overheads.
- Context switches can update only what has changed - increasing performance.
- Updates can be carried out on one component - making it more flexible.

## SunOS 5.0

This OS implements Light Weight Process as laid out in [[Week 5 - Beyond Multiprocessing ... Multithreading and the SunOS Kernel]]. 

