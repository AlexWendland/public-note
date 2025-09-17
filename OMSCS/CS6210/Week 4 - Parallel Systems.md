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

## Shared Memory architectures

Here we detail 3 different approaches to shared memory architectures:

### 1. Dance Hall Architecture

In this architecture, CPU's and distributed memory sit on either side of an interconnection network.
All memory is accessible to all CPU's.

![[dance_hall.png]]

### 2. Symetric Multiprocessor (SMP)

In this architecture, CPU's share a common bus to access a single memory.
Access time from each CPU to the memory is the same.
This is the most common architecture in modern systems.

![[smp.png]]

### 3. Distributed Shared Memory (DSM)

In this architecture each CPU has its own local memory, but can also access memory on other CPU's.
These access are done via a interconnection network and take longer that accessing local memory.

![[dsm.png]]

### Caches

Within all the designs above, each CPU has its own cache.
This is important as (for example) in SMP cache access takes around 2 cycles - whereas memory access is around 100 cycles.
