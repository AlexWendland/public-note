---
aliases:
checked: false
course: "[[CS6210 Advanced Operating Systems]]"
created: 2025-08-29
last_edited: 2025-08-29
draft: true
tags:
  - OMSCS
type: lecture
week:
---
# Week 2 - OS Structure Overview

The OS structure is the way OS is organised with respect to the applications it serves and the underlying hardware it manages.

Some desirable traits for this to have are:

- **Protection**: Defending the user from the OS's activities but also the OS from anything ran by the user. Similarly each user from one another.
- **Performance**: The time taken to run the services the OS offers.
- **Flexibility**: The ability to adapted the services the OS offers for different use cases.
- **Scalability**: The performance of the OS increases as the resources provided increases.
- **Agility**: adapting to changes in application needs or resource availability.
- **Responsiveness**: The ability to respond to events in a timely manner.

## Different OS Structures

- **Monolithic**: In a monolithic OS all the OS application run is a separate address space to user applications.
This means all access to the underlying hardware has to go through a context switch to be used by the OS.
- **DOS**: In the DOS (Disk operating system) all the OS applications are still together in one program however that programme shares the address space with theuser applications.
This means no context switching to use OS calls but less protection for user applications.
- **Microkernel**: In a Microkernel we have a minimilistic core operating system that offers services such as [[inter-process-communication-ipc]] and address space separation.
Other services such as file systems, memory management, and network managers all run as user level applications.

DOS was built for single user personal computers.
Therefore, the loss of security was considered acceptable - but makes it a bad choice for a general purpose OS.
Monolithic OS have the protection of a general purpose OS but require context switching for OS calls.
However, Monolithic OS gain performance by consolidating system calls so once you have switched to the OS it can do everything.

The downside to both the Monolithic and DOS is their flexibility.
As they do not let you switch out components one size has to fit all.
That means the OS has to handling responsive applications in the same way it handles CPU intensive applications.
This is where the Microkernel comes in, as the core services offered by the OS as user applications, it is possible for an application to choose which application it wants to provide a service it needs.
Though it pays for flexibility with performance due to each of the OS services running in a separate users space and relying on IPC offered by the Microkernel - this can cause many context switches to perform basic operations.
Context switches in this case may have a hidden second cost of copying data, and locality as we clear the [[translation-lookaside-buffer-tlb]]

