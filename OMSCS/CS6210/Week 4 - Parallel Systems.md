---
aliases:
checked: false
course: "[[CS6210 Advanced Operating Systems]]"
created: 2025-09-17
last_edited: 2025-09-17
draft: true
tags:
  - OMSCS
type: lecture
week: 4
---
# Week 4 - Parallel Systems

In modern computing, nearly all processors are multi-core.
This presents an interesting problem - how to share memory between them?

## Shared Memory Architectures

Here we detail 3 different approaches to shared memory architectures:

### 1. Dance Hall Architecture

In this architecture, CPUs and distributed memory sit on either side of an interconnection network.
All memory is accessible to all CPUs.

![[dance_hall.png]]

### 2. Symmetric Multiprocessor (SMP)

In this architecture, CPUs share a common bus to access a single memory.
Access time from each CPU to the memory is the same.
This is the most common architecture in modern systems.

![[smp.png]]

### 3. Distributed Shared Memory (DSM)

In this architecture each CPU has its own local memory, but can also access memory on other CPUs.
These accesses are done via an interconnection network and take longer than accessing local memory.

![[dsm.png]]

## Caches

Within all the designs above, each CPU has its own cache.
This is important as (for example) in SMP cache access takes around 2 cycles - whereas memory access is around 100 cycles.
However, the existence of a cache creates a problem - what if two CPUs have a copy of the same memory location in their cache, and one CPU updates it?

### Memory Consistency Models

In my previous lectures we covered memory consistency models in detail.

[[week-15-distributed-shared-memory]]

This course mainly focuses on sequential consistency.

![[sequential-consistency]]

### Cache Coherence

The memory model is the software engineers view of memory.
It mandates what you can expect when programming on multi-threaded systems.
The other side of this is cache coherence - the hardware engineers view of memory.
This is how the hardware ensures the memory model is upheld.

>[!note] Cache coherent processors
> One solution to this problem is for the hardware to make no promises of consistency.
> This, would be a cache incoherent processor - it is up to the software to implement consistency.
> However, below we detail methods for processors to be cache coherent.

Here are a couple methods to guarantee cache coherence:

- *Write-invalidate*: When a CPU writes to a memory location, it invalidates all other cached copies of that memory location.
- *Write-update*: When a CPU writes to a memory location, it updates all other cached copies of that memory location.

>[!warning] What happens for multiple writes?
> This will cause a race condition between writes.
> Not discussed in the lectures.

The downside to these approaches is they affect the 'scalability' of the systems.
With a good architecture, we would expect performance to scale linearly with the number of CPUs.
However, if messages need to be passed between CPUs for cache coherence (either invalidations or updates), this creates O(n²) communication overhead for n CPUs - not providing us with scalability.

#### Alternative Approach: Avoiding Shared Memory

Given the scalability challenges of cache coherence protocols, one radical solution emerges: simply avoid sharing memory between threads altogether. This approach eliminates the need for complex coherence protocols and their associated overhead.

>[!quote] Shared memory machines scale well when they don't share memory.
> This paradoxical statement highlights that the hardware capability for shared memory doesn't mean software must use it extensively.
