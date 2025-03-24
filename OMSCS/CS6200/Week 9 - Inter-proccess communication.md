---
aliases: 
checked: false
course: "[[CS6200 Graduate introduction to Operating Systems]]"
created: 2025-03-24
last_edited: 2025-03-24
publish: true
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