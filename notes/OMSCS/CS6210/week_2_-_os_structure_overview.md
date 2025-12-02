---
aliases:
checked: false
course: 'CS6210 Advanced Operating Systems'
created: 2025-08-29
draft: false
last_edited: 2025-08-29
title: Week 2 - OS Structure Overview
tags:
  - OMSCS
type: lecture
week: 2
---
# Week 2 - OS Structure Overview

The OS structure is the way OS is organised with respect to the applications it serves and the underlying hardware it manages.

Some desirable traits for this to have are:

- **Protection**: Defending the user from the OS's activities but also the OS from anything ran by the user. Similarly each user from one another.
- **Performance**: The time taken to run the services the OS offers.
- **Flexibility**: The ability to adapt the services the OS offers for different use cases.
- **Scalability**: The performance of the OS increases as the resources provided increases.
- **Agility**: adapting to changes in application needs or resource availability.
- **Responsiveness**: The ability to respond to events in a timely manner.

## Different OS Structures

### Monolithic OS
In a monolithic OS, all OS services run in a separate address space from user applications.
This means all access to the underlying hardware requires a context switch to kernel space.

**Protection**: Excellent - strong isolation between user and kernel space provides robust security.
**Performance**: Mixed - context switching overhead for each system call, but efficient for complex operations requiring multiple services since everything runs in kernel space.
**Flexibility**: Limited - all services are compiled into a single kernel, making it difficult to customize or replace individual components.

### DOS (Disk Operating System)
In DOS, OS services share the same address space as user applications, eliminating the need for context switching.

**Protection**: Poor - no isolation between user applications and OS services, making the system vulnerable to crashes and malicious code.
**Performance**: Excellent - no context switching overhead means very fast system calls.
**Flexibility**: Limited - like monolithic systems, components cannot be easily swapped or customized.

DOS was designed for single-user personal computers where the security trade-off was acceptable, but this makes it unsuitable for general-purpose or multi-user systems.

### Microkernel
A microkernel provides only core services like [inter-process-communication-ipc](inter-process-communication-ipc.md) and address space management. Other services (file systems, memory management, network drivers) run as user-level applications.

**Protection**: Moderate - while the minimal kernel reduces the trusted computing base, the distributed architecture creates a larger attack surface and complex inter-service communication that can introduce vulnerabilities.
**Performance**: Poor - frequent context switches and IPC between services create significant overhead. Each basic operation may require multiple context switches and data copying.
**Flexibility**: Excellent - services can be independently developed, replaced, or customized for specific applications.

The performance cost comes not just from context switches but also from data copying between services and cache/TLB invalidation when switching between different user-space services.

### Summary of Trade-offs

| Architecture | Protection | Performance | Flexibility |
|-------------|------------|-------------|-------------|
| **Monolithic** | ✅ High | 🔶 Mixed | ❌ Low |
| **DOS** | ❌ Low | ✅ High | ❌ Low |
| **Microkernel** | 🔶 Moderate | ❌ Low | ✅ High |

**Key insight**: Each architecture makes different trade-offs. Monolithic systems prioritize security and are reasonable for performance.
DOS prioritizes performance at the cost of security.
Microkernels prioritize flexibility but suffer performance penalties and have complex security considerations.

## Another way

There are two other structures that attempt to get the best of all worlds:

- A thin OS (like a Micro-Kernel), which implements mechanisms not policies.
- Access to resources without context switching like DOS.
- Flexibility for resource management (like a Micro-Kernel) without sacrificing protection (like DOS) or performance (like a Monolith).

We look at three different approaches to this

- The SPIN approach,
- The Exokernel approach, and
- The L3 Microkernel approach.

They all try to do the above but in different ways.

## Capabilities

Capabilities are unforgeable tokens that combine both identity and permission into one object.
Unlike traditional access control where the system checks "Who are you and what are you allowed to do?", capability-based systems ask "Do you have the right token?"

For example, in a c program once you have opened a file descriptor with certain privileges.
Having this file descriptor in your file descriptor table is sufficient to say you have access to that file - you do not need to check permissions again.

# SPIN approach

These notes are based on the paper: Extensibility, Safety and Performance in the SPIN Operating System

SPIN has two types of code:
1. **User applications** - run in user space and still require context switches for system calls (like traditional systems).
2. **Kernel extensions** - performance-critical code that runs within the kernel's address space. This accesses other OS resources as procedure calls.

> [!note] Procedure vs system call
> A procedure call is a function call within the same address space, whereas a system call involves switching from user space to kernel space.
> This means procedure calls are much faster than system calls.

This allows selective optimization: the bulk of an application remains in user space, but performance-critical parts can be written as kernel extensions that avoid border crossing overhead when accessing kernel services.

To get around the security concerns of running user code in kernel space, SPIN uses a highly typed programming language (Modula-3) to write the extension code.
This way the compiler enforces separation between extensions and other kernel code.

> [!note] Separation of kernel and extension code
> This was implemented similar to having header files within C.
> Extension code was in separate modules and could only access kernel services through interfaces defined in the module headers.

The typing within Modula-3 means that you can't re-type object pointers.
This enables logical protected domains enforced by the compiler and does not rely on hardware address spaces.

This enables flexibility by offering different interfaces for the same services.
Then users can choose whichever implementation suits their needs whilst not adding bloat to the program as they access the same underlying data.

Like monolithic systems, kernel extensions benefit from procedure call access to other kernel services. Unlike monolithic systems, only performance-critical code needs to run in kernel space - the rest of the application can remain safely in user space.

## Modula-3

Modula-3 is a strongly typed programming language with built in safety and encapsulation mechanisms.
It is memory-safe with automatic garbage collection, preventing manual memory management errors.
Its main abstraction is an object which has external entry points defined, and outside callers can not see its implementation.
These objects provide encapsulation due to outside callers only being able to access them via the external entry points.
The language supports threads and exception handling.

The use of generic interfaces provides flexibility and fine-grained protection via capabilities, for example with memory:

- At the hardware level resource, you can control a page frame.
- At the level of an interface there is the page allocation module.
- Collections of interfaces can be accessed via an entire VM.

These capabilities are supported as language pointers.

## Protection domains

Extensions exist within logical protection domains, which are kernel namespaces that contain code and exported interfaces.
Interfaces, which are language-level units, represent views on system resources that are protected by the operating system.
An in-kernel dynamic linker resolves code in separate logical protection domains at runtime, enabling cross-domain communication to occur with only the overhead of a procedure call.
These domains support the following mechanisms:

- **Create**: Initialise the object file content and export the names that are entry points to this domain.

- **Resolve**: This acts as a linker between two protection domains.
Then the source protection domain can use names (entry points) from the target protection domain as procedure calls.

- **Combine**: After resolving two domains to be in the same domain, you can use combine to offer these as one domain for another extension.
This is to combat the proliferation of many small domains and make the extensions easier to handle.

The domains allow SPIN to be extended in a custom way.
This makes the OS flexible to user preferences whilst also using Modula-3's strong typing to stay secure.

## Examples

Due to the flexibility of SPIN you can turn a lot of OS heavy operations into extensions of the OS to benefit similarly to the Monolith's consolidation.

- **Unix server**: You can extend SPIN to the full capabilities of any other OS, such as Linux, BSD, or even Windows.

- **Client-server**: When designing client-server applications, you can implement the server/client as an extension to SPIN.
This will dramatically speed up network operations as you can avoid context switching with system calls.

## Events

Extensions execute in response to system events.
An event can describe any potential action in the system, such as a virtual memory page fault, the scheduling of a thread, or an IP packet has arrived.
Events are declared within interfaces, and can be dispatched with the overhead of a procedure call.
Events contain metadata allowing them to be filtered and dispatched to the appropriate handlers.

Extensions in SPIN are defined in terms of events and handlers.
An event is a message that announces a change in the state of the system or a request for service.
An event handler is a procedure that receives the message.
An extension installs a handler on an event by explicitly registering the handler with the event through a central dispatcher that routes events to handlers.

### Two Levels of Event Protection

**Import-level protection**: Controls which domains can define handlers on events within a domain.
To handle any event, you must first be able to import the interface that defines it.
The domain defining the event can restrict access at import time.

**Guard-level protection**: After importing an interface, handlers can define guards to filter which specific message instances they want to handle.
Guards are defined by the handler (not the event definer) and act as boolean filters.

For example, with IP packet processing:
- **Import-level**: Your extension must be authorized to import the IP module to handle any `IP.PacketArrived` events
- **Guard-level**: Your TCP handler defines a guard that returns `TRUE` only for TCP packets, filtering out UDP packets

This two-level system means domains can have fewer, more generic events (like one `PacketArrived` event) while still providing fine-grained access control.
Extensions get precise filtering without requiring separate event types for every possible message variant.

### Handler ordering

When multiple handlers are registered for the same event, the default behavior is sequential execution:

> [!quote] Extensibility, Safety and Performance in the SPIN Operating System
> "By default, the dispatcher mimics procedure call semantics, and executes handlers synchronously, to completion, in undefined order, and returns the result of the final handler executed."

The execution order is undefined, meaning you cannot rely on handlers running in any specific sequence. However, this behavior is configurable - the event owner (the module that defines the event) can customize how handlers execute, including setting them to run asynchronously, with time bounds, or in specific orders.

## Core services of SPIN

SPIN provides the core services of a traditional OS, for example memory or CPU management.
However, SPIN allows you to extend these implementations to follow whichever policy you would like.

### Memory management

- Physical address: you can allocate, deallocate, and reclaim.
- Virtual memory: you can allocate and deallocate.
- Translation: you can create/destroy address spaces, and add/remove address mappings.
- Event handlers: page fault, access faults, and bad addresses.

### CPU management

For CPU management, SPIN introduces a new abstraction called strand which each group of extensions run on.
These are all ran on time-slices which it can do anything with but the global scheduler controls who is in control between the strands.

- SPIN abstraction: Strand, with the semantics defined by the extension.
- Event handlers: Block, unblock, checkpoint, resume.
- SPIN global scheduler: Interacts with application thread packages.

# Exokernel approach

These notes are based on: Exokernel: An Operating System Architecture for Application-Level Resource Management On Micro-Kernel Construction.

An Exokernel is a minimal kernel that only protects access to hardware resources, handles traps, and shares resources between applications.
The Exokernel has its own address space which has higher level access to hardware but hosts 'Library OS's that are in separate address spaces which can communicate with the exokernel.
A Library OS then can interact with the exokernel in a couple of ways:

- **Hardware mechanisms**: It can request access to a hardware resource, if allowed it gets back a token for use.
Then it can use access tokens to make hardware calls.
- **Downloading code**: It can download code into the exokernel to be run on different events such as traps.
- **Software Caching**: It can use a software cache supported by the Exokernel

## Hardware resource access

To reduce the number of context switches the Exokernel exposes resources directly.
To this extent it only protects certain operations, such as write - therefore allowing the Library OS to read without needing a context switch.

> [!example] TLB entries
> Assume we are on a guest OS that has the correct access to write to the TLB.
> - Virtual to physical mapping is calculated by the Library OS.
> - Binding is presented to the Exokernel with permissions.
> - Exokernel validates permissions and puts it in the TLB.
> - The Library OS can access the TLB multiple times for that mapping without switching to the Exokernel.

Therefore the two, 'heavy' Exokernel operations are getting permissions and using the write permissions.
Whereas the read (the more common operation) can be carried out multiple times with no Exokernel switch.

### Revoking resources

If the Exokernel needs to take resources away from the Library OS, it passes a 'revoke vector' back to the Library OS.
The Exokernel then allows the Library OS to take whichever corrective action it needs to to clean up the resources within its own address space.

To make this less cumbersome, the Exokernel offers options on resources such as 'autosave' when it obtains the resources.
For example, with a page of RAM memory this would enable the Exokernel to save down what is in RAM to disk before clearing it out.
This will save the amount of work the Library OS has to do when memory is revoked.

## Downloading code (secure binding)

Similarly to SPIN, you can download code into the Exokernel to run on events such as IP packet arrival.
This can filter an only call the Library OS if it is of the correct type.
However, this is not in a strongly typed language so this code can be more destructive to the OS than in the SPIN example.

> [!example] Page fault
> Assume our Library OS has already downloaded code to handle page faults.
> When applications are running on the Library OS and a page fault occurs.
>
> - We trap to the Exokernel causing a context switch.
>
> - The Exokernel runs the downloaded code to handle the page fault.
> (Note, without this code - the Exokernel would not know how to communicate with the Library OS as it does not know anything about how the process is structured.)
>
> - Control is returned to the Library OS in the way it has defined within the downloaded code.
>
> - The Library OS uses hardware resources to access the required page.
>
> - The application continues as normal.

Due to the security considerations of running code within the Kernel, not all applications can do this.
This capability is restricted to a set of trusted applications.

## Software caching

Due to the switching overhead of the Exokernel (bouncing between Library OS's) it enables processes to cache their TLB entries (S-TLB) and memory addresses by default.
This reduces the amount of cleanup the Library OS's need to implement manually and instead can rely on the Exokernel to do it.
This also provides a level of guarantee on what will be in the TLB - which can be a serious problem from efficiency with designs close to that of a Micro-kernel.

## CPU scheduling

To schedule different Library OS's the Exokernel uses a simple round-robin scheduler.
Each Library OS gets a time quantum to run in, and it is informed about when this is going to end so it can prepare for the context switch.
If a Library OS overruns its time quantum it will have its overrun deducted from the next time quantum when it runs.

Outside of time switches, the Exokernel is only invoked when directly called or if a trap occurs.
This technique should minimise the number of context switches.

## Exokernel data structures

The main data structures within an Exokernel we have already covered are:

- The Scheduler: This is a linear time vector tracking which Library OS is scheduled and for how long.

- Software TLB: This is a cache of TLB entries that the Exokernel maintains for each Library OS.

The other main data structure is the PE table,
which is a table of handler entry points within the library OS to run on different events.
Such traps would be exceptions, external interrupts, system calls and addressing context.

# L3 Microkernel approach

Within the SPIN and Exokernel papers they compared their approaches to the Mach Microkernel.
However, the Mach Microkernel was built for portability between many architectures rather than performance.
Within the L3 Microkernel we will see how when optimising for a particular processor we can get fast performance.

Typically, a Microkernel would run a small kernel in a privileged mode that covers the basics a kernel needs to offer: IPC, address spaces, threads, and UID (Unique Identifiers).
Then all other services run as user level processes such as CPU scheduling, file system, and memory manager.
This means there is a lot of switching between different address spaces, as well as IPC to share data between the processes.

## Why Microkernels are slow

There are multiple reasons why the typical model of a Microkernel is slow:

- Border crossings:
  - Explicit cost: this comes from the context switches themselves.
  - Implicit cost: this comes from the implications of context switches, such as TLB being cleared or the cache being cold.
- Protected procedure calls:
  - These are required for communication between OS services.
  - These procedure calls are 100× slower than normal procedure calls.

Concretely we will need to look at 4 costs.

- Kernel-user switches: This is the cost of physically switching from kernel to user mode or vice versa.

- Address space switches: This is the cost of switching between different address spaces from the TLB flush.

- Thread switches with IPC: When switching between two OS services operating in the user space, we require the kernel to mediate the change in control which adds another context switch to this operation.
This involves saving down all the state of the process.

- Memory effects: When we perform a context switch we will lose our current cache, meaning that we have to read from memory much more often, causing sluggish behaviour.

The L3 Microkernel aims to reduce all these costs by systematically building a Microkernel which avoids or reduces the costs.

## Kernel-user switches

The Mach Microkernel takes 900 cycles to switch from the user to kernel space.
This was due to Mach being optimised to work on any underlying architecture, meaning there is code bloat within these switches.
However, the L3 Microkernel was designed to take only 123 cycles.
This was built on top of the Pentium processor (so for a specific processor).
Within the paper they prove that the minimal number of cycles it could take is 107.

With this in hand, it discounts some of the results of the SPIN and Exokernel papers as they compared themselves against the Mach Microkernel.

## Address space switches

Here we concern ourself with TLB flushes.
Traditionally, the TLB is broken into two parts:

- **User space**: For the current running process.
- **Kernel space**: For the kernel, this is an optimisation so the kernel is always hot in the TLB as it is switched to so much.

This means in a MicroKernel where we switch between many user level applications (OS services) regularly we will flush the TLB often - meaning TLB misses requiring memory access.
Instead of splitting it like above we could instead split it via PID of the process.
That way when doing the TLB lookup we use the tag from the VPN and the PID to do the lookup.
There are two different implementations of this, either the hardware can support it with a AS-tagged (Address space tagged) TLB or we can support it using software tricks such as using a segmented registers.

The next question is how to partition the TLB into different processes to avoid regular TLB lookups.
First, the L3 paper separates processes into two categories:

- Large applications: These are likely to use up the whole user part of the TLB.

- Small applications: These are likely to have only a couple of frames for their working set.

When context switching between two large applications, the cost of the flush is a lot less (864 cycles in the pentium processor) than the loss of locality (cold caches).
In this case we can just fully flush the TLB as that is not the largest contributing factor.

However, when switching to or from small applications the TLB flush is the dominating cost.
Therefore if we can preserve the small application's TLB entries we can save a lot of time.

So the paper suggests partitioning the TLB into 3 sections.

- Large user application: This takes up the majority of the TLB.

- Small user applications: This takes up a small section of the TLB, and can store many small applications' TLBs.

- Kernel: This takes up a small section of the TLB, and is always hot.

When switching between two small applications we can preserve the TLB entries for both applications and the kernel.
This means the frequent border crossings from a large application to the kernel and smaller OS services can be done without the cost of flushing the TLB.

## Thread switches and IPC

When we switch threads we need to save down the state of the registers into that process PCB (Process Control Block).
In the L3 paper it shows this can be competitive in comparison to SPIN or the Exokernel.

(No details provided on how.)

## Memory effects

Alongside the TLB, we have the CPU cache which is arranged in a hierarchical manner as below:

- CPU registers: What is directly on the CPU,
- L1 cache: Smallest and fastest cache,
- L2 cache: Second fastest cache,
- L3 cache: Largest and slowest cache,
- Main memory: Slowest access.
- Disk: Can be used when the virtual memory is larger than the physical memory to save pages.

Quite often the Ln caches are typically physically tagged.
This means they group memory as they are arranged within the physical memory.

The suggestion within the L3 paper is to have your protection domains to be small and all within the same hardware address space.
This ensures that when switching between different user level applications we make sure the cache is still somewhat warm when moving from process to process.
This means the memory effects of context switches can be mitigated by carefully managing the protection domains within the hardware address space.

> [!note] Small protection domains
> This, similar to the TLB address space switching, only works for small protection domains.
> If we context switch between large protection domains that are likely to use all the memory then we can't pack it together in one hardware address space.

## Summary

The L3 Microkernel states that the kernel itself only need to offer 4 services:

- IPC: This is the most important service as it allows the kernel to mediate between different user level applications.

- Address spaces: This allows the kernel to create and destroy address spaces for user level applications.

- Threads: This allows the kernel to create and destroy threads for user level applications.

- UID: This allows the kernel to create and destroy unique identifiers for resources.

To make these services performant you need to specialise the Microkernel to the particular processor/kernel it is operating on.
That is to say, for an efficient Microkernel it cannot be portable like the Mach Microkernel.
