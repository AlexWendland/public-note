---
aliases:
checked: false
course: "[[CS6210 Advanced Operating Systems]]"
created: 2025-10-23
last_edited: 2025-10-23
draft: true
tags:
  - OMSCS
type: lecture
week: 6
---

# Week 6 - Distributed objects and middle ware

## Spring OS

When innovating as a company in the OS space you have two options:

1. Build a new OS from scratch.

2. Build a better implementation of an existing OS.

This decision is normally constrained by your customer base.
In the company Sun Microsystem, they choose to keep the unix interface but try for better 'under the hood' implementations.
This is similar to CPU's which are said to be 'Intel inside' but have different implementations.
In this case it was 'Unix inside' but they changed the implementation.

### Procedural vs Object design

The distinction between procedural and object-oriented design is often oversimplified.

**Procedural Design (Traditional Unix):**
- You have **data structures** (file descriptors, process control blocks, etc.)
- You have **functions** that operate on those structures (open(), read(), write())
- The function doesn't "belong to" the data - you pass data to functions
- System calls are essentially: `function(handle, parameters) → result`

**Object-Oriented Design (Spring OS):**
- You have **objects** with their own identity and lifecycle
- Each object **owns its operations** - you don't pass it to functions, you invoke methods on it
- The object's implementation is hidden behind the interface
- Invocations look like: `object.method(parameters) → result`

### Why This Matters for Spring OS

The crucial difference emerges in **distributed systems**:

1. **Location Transparency**: In Spring's object model, an object can live anywhere (different process, different machine). When you call `object.method()`, the middleware handles whether that's local or remote. In procedural design, you're calling a function in your address space that operates on local data.

2. **Identity**: Objects have unique identities (object references). In procedural design, you just have handles/pointers to data structures that only make sense in your address space.

3. **Multiple Implementations**: An interface in Spring can have different implementations with the same calling pattern. In procedural Unix, you often need different function calls for different underlying implementations.

### Spring OS approach

Within Spring OS, they go for a Microkernel approach but the idea was to make a Networked OS.
Therefore they wanted a clear separation between the kernel and other services - as these services could be running on a different machine.

![[Spring OS.png]]

For this to work they needed to encapsulate state and have a strong interface between the services.
They reduce the size of the kernel to something they call the 'nucleus' and a vm manager.
This follows the ideas of Liedtke's microkernel where all that is offered by the kernel is threads, IPC and address spaces.
One thing to highlight though is the network proxy will become increasingly important as we wish to distribute services across a network.

### Nucleus (Microkernel)

This is the core part of the Spring OS - it offers two services, IPC and threads.
However, it does this in a very decoupled way.

![[Spring OS Nucleus.png]]

In Spring OS, there is a concept of a domain that acts as an address space.
Domains contact each other through the Nucleus using 'Doors' - these are a capability-based permission to access a part of the interface of another domain.
When trying to use the door they have to go via the nucleus as a protected procedure call and this runs a thread in the target domain's address space.
As a door is a capability, these can be shared between domains.
Similar to the lightweight RPC paper, Spring OS tries to make the use of these doors as fast as possible to keep the system performant.
Each domain holds a door table that contains the door handles it can use.

### Object invocation Across the network

To make cross network domain calls, Spring OS uses network proxies.
These are domains that sit on each machine and mirror the calls that can be made across the network.

![[spring_os_network.png]]

When a client on a different machine wants to make a call to a server elsewhere, it uses a door into its local Proxy.
This door then starts the proxy to forward the request to the target machine's proxy - which in turn uses a door on its local nucleus to access the requested service.
This happens transparently to the client that just makes a local door call.
