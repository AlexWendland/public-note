---
aliases: 
checked: false
course: "[[CS6200 Graduate introduction to Operating Systems]]"
created: 2025-03-24
last_edited: 2025-03-24
draft: false
tags:
  - OMSCS
type: lecture
week: 9
---
# Week 9 - Inter-process communication

![[Inter-process communication (IPC)]]

## Message based IPC

Message based [[Inter-process communication (IPC)|IPC]] opens two ports (not necessarily in the networking sense) one in each process. Then the kernel is used to move the messages between the two ports. Examples of this are:
- Pipes: A stream of bytes between the process - no structured messages. This is used when connecting stdin to stdout of a process when you 'pipe' them in a terminal.
- Message queues: A queue of structured messages that the processes can pop one at a time. In [[Linux|linux]] there two APIs for this SystemV and [[Portable operating system interface (POSIX)|POSIX]].
- Network sockets: Uses the same interface as connecting to a network port. Normally the [[Operating system (OS)|operating system]] optimizes this process by skipping some overhead of the network protocols.
Message based [[Inter-process communication (IPC)|IPC]] is simple to use as the kernel handles the [[Synchronization|synchronization]] but come with overhead as the message has to be copied between processes and involves [[Context switch (CPU)|context switches]] to communicate with the kernel.

## Shared Memory IPC

 This form of [[Inter-process communication (IPC)|IPC]] maps a bit of memory into both processes. After it is mapped in neither processes need to go through the kernel to communicate. However that means both processes need [[Synchronization|synchronization]] to ensure they don't over-write one another. They also need to establish a shared protocol on how to communicate.

The main APIs here are: SystemV and [[Portable operating system interface (POSIX)|POSIX]].

### SystemV shared memory

- Uses "segments" of shared memory which are not necessarily contiguous physical memory.
- The memory is shared system wide. This means there are system wide limits on shared memory.
- The [[Operating system (OS)|operating system]] creates a shared memory segment and identifies it by a key.
- Processes need to map that [[Physical memory|physical memory]] into their [[Virtual memory|virtual memory]].
- This segment can be detached (so it no longer has a mapping in [[Virtual memory|virtual memory]]).
- The segment can also be destroyed so it no longer has a system identifier.

In comparison to SysV [[Portable operating system interface (POSIX)|POSIX]] uses a shared file descriptor to access the shared memory.

### Synchronization

As multiple processes can now access the same memory we need to be able to coordinate read and writes.

Pthreads [[Mutex|mutexes]] and [[Conditional variables (Mutex)|conditional variables]] can be used for this but we will need to share their data structures in the shared memory to be accessed by both processes.

This can also be achieved via a message queue by sending read write messages.

Otherwise [[Semaphores|semaphores]] can be used for this which will be covered later.

## Command line utility with IPC

When using SysV you can use the following command line functions to manage IPC resources:
- ipcs: This is used to display information about the utilities. The -m flag displays information on shared memory only.
- ipcrm: This deletes IPC entities. You can specify an exact one using the -m flag with the shmid.

When using the [[Portable operating system interface (POSIX)|POSIX]] API the IPC tools are saved as files and can be accessed via:
- /dev/shm: For shared memory and semaphores.
- /dev/mqueue: For shared queues.

## Design considerations

When using shared memory, you can choose between one large segment of shared memory for two processes or lots of smaller segment for each purpose.

