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

## Synchronization Primitives

This was covered in CS6200 also:

[[week-10-synchronization-constructs]]

### Exclusive Locks

These are locks where at most one thread can have it at a time.

### Shared Locks

These are locks which have more complicated semantics of access, for example readers-writer locks.

### Barriers

This is a synchronization primitive where threads wait until all threads have reached the barrier before proceeding.

## Lock implementations

> [!reminder] Atomic Operations
> These are operations which are guaranteed to not be interrupted when running on the CPU.

When we want to implement a exclusive lock, read and write atomic operations are not enough and we need a RMW (read modify write) atomic operation.
Below are some of the usual suspects:

- Test-and-set: This operation gets the current value of a memory location and sets it to 1.
- Fetch-and-increment: This operation gets the current value of a memory location and increments it.
- Fetch-and-phi: This is a generic version of fetch-and-increment where phi is any function.

When we are assessing different lock implementations, we care about:

- Latency: If the lock is not currently used, how long does it take to acquire it.
- Waiting time: If the lock is currently used, how long does it take to acquire it.
- Contention: If the lock is currently used but then released, how long does it take to acquire it.
- Fairness: Do threads get the lock in the order they requested it.

Whilst waiting time is application specific, the other two can be used to compare different lock implementations.

### Spin lock (test-and-set)

This is the simplest lock implementation.
Here you have a shared memory address that represents if the lock is busy or not - lets call `locked`.

```c
LOCKED = 1;
UNLOCKED = 0;

lock(){
  while(test_and_set(locked) == LOCKED); // spin
}

unlock(){
  locked = UNLOCKED;
}
```

This is a pretty bad lock for 3 reasons:
- Blocks useful work from being done whilst spinning.
- Massive contention as multiple threads carry out test-and-set on the same memory location.
- Does not utilise caching in anyway.

### Cached spin lock

If we can assume the caches are kept cache consistent through the hardware, we can use these values to save us needing to perform the costly atomic operation.
This is similar to uncached version where we have a `locked` variable.

```c
LOCKED = 1;
UNLOCKED = 0;

lock(){
  while(test_and_set(locked) == LOCKED){
    while(locked == LOCKED); // spin
  }
}

unlock(){
  locked = UNLOCKED;
}
```

Whilst this dramatically reduces the number of test_and_set operations, if the hardware uses write-invalidate this is on the order of O(n^2) memory accesses as for each test_and_set every processor needs to get the new value of locked from memory.

### Spin locks with delay

To reduce the contention on the memory bus, we can add a delay between each test_and_set operation.

```c
LOCKED = 1;
UNLOCKED = 0;

EXP_CONST = 2;
INITIAL_DELAY = 1;
MAX_DELAY = ??;

lock_with_fixed_delay(){
  while(locked == LOCKED or test_and_set(locked) == LOCKED){
    while(locked == LOCKED); // spin
    wait(d[P_i]); // wait for an amount of time that depends on the processor id
  }
}

// This does not use the cache, so we do not require a cache coherent system.
lock_with_exponential_delay(){
  int delay = INITIAL_DELAY;
  while(test_and_set(locked) == LOCKED){
    wait(delay);
    delay = min(MAX_DELAY, delay*EXP_CONST); // exponential backoff
  }
}

unlock(){
  locked = UNLOCKED;
}
```

This dramatically reduces contention on the memory bus, but increases latency of acquiring the lock.

### Ticket lock

This mimics getting a ticket in a shop to be served next.
You get a ticket number when you enter and you wait until your number comes up.

```c
struct lock{
  int next_ticket = 0; // The next ticket to be given out
  int now_serving = 0; // The ticket number currently being served
}

lock(lock L){
  int my_ticket = fetch_and_increment(L->next_ticket);
  while(my_ticket != L->now_serving);// spin
}

unlock(lock L){
  L->now_serving = L->now_serving + 1;
}
```

This lock is now fair but there is quite a bit of contention when the now_serving variable is updated as all threads will be trying to read it.
The issue here is that all threads are spinning on the same memory location - if we can instead only signal the next thread we can greatly reduce contention.

### Array-based queueing lock

To do this, we can create an array which acts a circular queue.

```c
MAX_THREADS = ??; // maximum number of threads that can use the lock
HAS_LOCK = 1;
LOCKED = 0;

struct queue_lock{
  int[MAX_THREADS] flag; // array of flags, initialise with flag[0] = HAS_LOCK and all others LOCKED
  int next_ticket = 0; // The next ticket to be given out
  int current_ticket = 0; // The ticket number currently being served
}

lock(queue_lock L){
  int my_ticket = fetch_and_increment(L->next_ticket);
  while(L->flag[my_ticket % MAX_THREADS] == LOCKED); // spin
  L->flag[my_ticket % MAX_THREADS] = LOCKED; // reset for next use
}

unlock(queue_lock L){
  L->current_ticket = L->current_ticket + 1;
  L->flag[L->current_ticket % MAX_THREADS] = HAS_LOCK; // set flag
}
```

This dramatically reduces contention as each thread is spinning on a different memory location.
However, this lock requires a large amount of memory - O(n) for the number of threads, which could be very large.

### Link list lock

For array-based queueing locks it used a lot of space even if only 2 threads are going to use it.
So instead it would be good to use a linked list to dynamically allocate memory.

```c
struct queue_node{
  int got_lock = 0;
  queue_node * next = NULL;
}

struct lock{
  queue_node * tail = NULL; // points to the last node in the queue
}

lock(lock L, queue_node * my_node){
  queue_node * previous = fetch_and_store(L->tail, my_node); // atomically swap the tail with my_node
  if(prev == NULL){ // no one has the lock
    my_node->got_lock = 1; // set the flag
  } else {
    previous->next = my_node; // add myself to the end of the queue
    while(my_node->got_lock == 0); // spin
  }
}
