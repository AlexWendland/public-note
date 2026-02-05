---
aliases:
course_code: CS6200
course_name: Graduate introduction to Operating Systems
created: 2025-03-24
date_checked: 2026-02-05
draft: false
last_edited: 2025-03-24
tags:
  - OMSCS
title: Week 9 - Inter-process communication
type: lecture
week: 9
---

[Inter-process communication (IPC)](../../notes/inter-process_communication_(ipc).md)

# Message based IPC

Message based [IPC](../../notes/inter-process_communication_(ipc).md) opens two ports (not necessarily in the networking sense) one in each process. Then the kernel is used to move the messages between the two ports. Examples of this are:
- Pipes: A stream of bytes between the process - no structured messages. This is used when connecting stdin to stdout of a process when you pipe them in a terminal.
- Message queues: A queue of structured messages that the processes can pop one at a time. In [linux](../../notes/linux.md) there are two APIs for this: SystemV and [POSIX](../../notes/portable_operating_system_interface_(posix).md).
- Network sockets: Uses the same interface as connecting to a network port. Normally the [operating system](../../notes/operating_system_(os).md) optimizes this process by skipping some overhead of the network protocols.
Message based [IPC](../../notes/inter-process_communication_(ipc).md) is simple to use as the kernel handles the [synchronization](../../notes/synchronization.md) but comes with overhead as the message has to be copied between processes and involves [context switches](../../notes/context_switch_(cpu).md) to communicate with the kernel.

# Shared Memory IPC

This form of [IPC](../../notes/inter-process_communication_(ipc).md) maps a bit of memory into both processes. After it is mapped in neither processes need to go through the kernel to communicate. However that means both processes need [synchronization](../../notes/synchronization.md) to ensure they don't over-write one another. They also need to establish a shared protocol on how to communicate.

The main APIs here are: SystemV and [POSIX](../../notes/portable_operating_system_interface_(posix).md).

## SystemV shared memory

- Uses "segments" of shared memory which are not necessarily contiguous physical memory.
- The memory is shared system wide. This means there are system wide limits on shared memory.
- The [operating system](../../notes/operating_system_(os).md) creates a shared memory segment and identifies it by a key.
- Processes need to map that [physical memory](../../notes/physical_memory.md) into their [virtual memory](../../notes/virtual_memory.md).
- This segment can be detached (so it no longer has a mapping in [virtual memory](../../notes/virtual_memory.md)).
- The segment can also be destroyed so it no longer has a system identifier.

In comparison to SysV [POSIX](../../notes/portable_operating_system_interface_(posix).md) uses a shared file descriptor to access the shared memory.

## Synchronization

As multiple processes can now access the same memory we need to be able to coordinate reads and writes.

Pthreads [mutexes](../../notes/mutex.md) and [conditional variables](../../notes/conditional_variables_(mutex).md) can be used for this but we will need to share their data structures in the shared memory to be accessed by both processes.

This can also be achieved via a message queue by sending read write messages.

Otherwise [semaphores](../../notes/semaphores.md) can be used for this which will be covered later.

# Command line utility with IPC

When using SysV you can use the following command line functions to manage IPC resources:
- ipcs: This is used to display information about the utilities. The -m flag displays information on shared memory only.
- ipcrm: This deletes IPC entities. You can specify an exact one using the -m flag with the shmid.

When using the [POSIX](../../notes/portable_operating_system_interface_(posix).md) API the IPC tools are saved as files and can be accessed via:
- /dev/shm: For shared memory and semaphores.
- /dev/mqueue: For shared queues.

# Design considerations

When using shared memory, you can choose between one large segment of shared memory for two processes or lots of smaller segment for each purpose.

