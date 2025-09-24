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

void lock(){
  while(test_and_set(locked) == LOCKED); // spin
}

void unlock(){
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

void lock(){
  while(test_and_set(locked) == LOCKED){
    while(locked == LOCKED); // spin
  }
}

void unlock(){
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

void lock_with_fixed_delay(){
  while(locked == LOCKED or test_and_set(locked) == LOCKED){
    while(locked == LOCKED); // spin
    wait(d[P_i]); // wait for an amount of time that depends on the processor id
  }
}

// This does not use the cache, so we do not require a cache coherent system.
void lock_with_exponential_delay(){
  int delay = INITIAL_DELAY;
  while(test_and_set(locked) == LOCKED){
    wait(delay);
    delay = min(MAX_DELAY, delay*EXP_CONST); // exponential backoff
  }
}

void unlock(){
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
};

void lock(lock L){
  int my_ticket = fetch_and_increment(L->next_ticket);
  while(my_ticket != L->now_serving);// spin
}

void unlock(lock L){
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
};

void lock(queue_lock L){
  int my_ticket = fetch_and_increment(L->next_ticket);
  while(L->flag[my_ticket % MAX_THREADS] == LOCKED); // spin
  L->flag[my_ticket % MAX_THREADS] = LOCKED; // reset for next use
}

void unlock(queue_lock L){
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
};

struct lock{
  queue_node * tail = NULL; // points to the last node in the queue
};

void lock(lock L, queue_node * my_node){
  queue_node *prev = fetch_and_store(L->tail, my_node); // atomically swap the tail with my_node
  if(prev == NULL){ // no one has the lock
    my_node->got_lock = 1; // set the flag
  } else {
    previous->next = my_node; // add myself to the end of the queue
    while(my_node->got_lock == 0); // spin
  }
}

void unlock(lock L, queue_node * my_node){
  bool someone_in_queue = compare_and_swap(L->tail, my_node, NULL); // If I am the tail node - swap it to null and return true, otherwise return false.
  if (someone_in_queue){
    while(my_node->next == NULL); // spin
    my_node->next->got_lock = 1; // signal the next node
  }
}
```

### Comparison

| Metric | Spin T&S | Spin on read | Spin w/ delay | Ticket | Array Q | List Q |
|--------|----------|--------------|---------------|--------|---------|--------|
|Latency | Low      | Low          | High          | Low    | Low     | Low    |
|Contention | High  | Medium       | Low           | Low    | Low     | Low    |
|Fairness | No      | No           | No            | Yes    | Yes     | Yes    |
|Spin on pvt variable | No | No    | No            | No     | Yes     | Yes    |
| RMW ops per lock | High | Medium | Low           | Low    | 1    | 1 (max 2) |
| Space  | Low      | Low          | Low           | Low    | High    | Medium |
| Signal one | No   | No           | No            | No     | Yes     | Yes    |
| Complex instructions | No | No   | No            | No     | Yes     | Yes    |



## Barrier implementations

With barrier implementations we are looking for:

- *Minimal contention*: We would like to reduce the amount of contention on the memory bus.
- *Latency*: We would like to minimise the amount of time the barrier mechanism takes.
... fill more in here.

### Centralised barrier

The simplest barrier implementation is to just count the threads in to the barrier and only release them when all threads have arrived.
One issue with this is when to release them, as some thread will need to reset the count.
This has to happen before threads are allowed to continue, otherwise they could finish the next section before the count is reset.

```c
struct barrier{
  int size = N;
  int count = N;
};

void bar(barrier B){
  decrement(B->count); // Atomic
  if(B->count == 0){
    B->count = B->size; // reset the count
  } else {
    while(B->count != B->size); // spin
  }
}
```

### Sense reversing barrier

The centralised barrier can only be used once, as each thread will need to notice that the count has been reset to the size.
Ideally, we would like to be able to reuse the barrier.
For this we can use a boolean flag to indicate if the barrier has been reset.
This means the barrier can be used in 'episodes'.

```c
struct barrier{
  int size = N;
  int count = N;
  bool sense = false;
};

void bar(barrier B){
  decrement(B->count); // Atomic
  if(B->count == 0){
    B->count = B->size; // reset the count
    B->sense = !B->sense; // flip the sense
  } else {
    bool my_sense = B->sense;
    while(B->sense == my_sense); // spin
  }
}
```

The issue with the centralised barriers are the contention on a single shared variables.
This means it has to be available to all threads and which is in a cache coherent system will generate lots of traffic.
Ideally, we would like to reduce contention by having multiple shared variables.

### Tree barrier

To reduce contention we will use a k-ary tree, and divide the threads up into groups of size less than or equal to some k.
These groups will be attached to a leaf node of a tree, and the last to arrive at each node will signal its parent node.
Once the root node has been released, this message will propagate down the tree to release all threads.

```c
struct barrier_node{
  int count = k; // number of children
  barrier_node * parent = NULL; // pointer to parent node
  bool sense = false; // sense for this node
};

// Some way to get the leaf node associated with the thread id.
barrier_node *get_leaf_node(int thread_id);

void bar_recursive(barrier_node * B){
  decrement(B->count); // Atomic
  if(B->count == 0){
    if(B->parent != NULL){
      B->sense = !B->sense; // flip the sense
    } else {
      bar_recursive(B->parent); // signal parent
    }
  } else {
    bool my_sense = B->sense;
    while(B->sense == my_sense); // spin
  }
}

void bar(int thread_id) {
  barrier_node *my_node = get_leaf_node(thread_id);
  bar_recursive(my_node);
}
```

The advantage of this approach is that contention is reduced as each node in the tree has its own count variable.
That means at most k threads will be trying to update it at once.
However, the node that signals the parent node is unknown at compile time.
This has the downside that the shared memory can not be optimised to be close to the CPU's that will need it.
So next we look at barriers where the memory locations are known at compile time.

### MCS Tree barrier

To pre-determine the memory locations each thread needs to access ahead of time, we build a 4-ary tree of the threads.
Then each thread knowns its parent thread before entering the barrier.
Then a parent thread has to wait for all its children to arrive before it can signal its parent.

For waking up, there is a separate binary tree to signal the children to wake up.
The root of the wakeup node and the barrier node are the same.

```c
struct barrier_node{
  bool has_children[4]; // Each location indicates if there is a child there
  bool child_not_read[4]; // The variable each child to flag that it has arrived
  bool *parent_not_ready = NULL; // pointer to parents child_not_read[child_index]
};

// The mapping from thread id to the node.
barrier_node *get_barrier_node(int thread_id);

struct wake_up_node{
  wake_up_node *left_child = NULL;
  wake_up_node *right_child = NULL;
  bool awake = false;
};

// The mapping from thread id to the wake up node.
wake_up_node *get_wake_up_node(int thread_id);

void bar(int thread_id) {
  barrier_node *my_barrier_node = get_barrier_node(thread_id);
  wake_up_node *my_wake_up_node = get_wake_up_node(thread_id);
  // Wait for all children to arrive
  for(int i = 0; i < 4; i++){
    if(my_barrier_node->has_children[i]){
      while(my_barrier_node->child_not_read[i] == false); // spin
      my_barrier_node->child_not_read[i] = false; // reset for next use
    }
  }

  // Signal parent and wait for wake up
  if(my_barrier_node->parent_not_ready != NULL){
    *(my_barrier_node->parent_not_ready) = true;
    while(my_wake_up_node->awake == false); // spin
  }

  // Wake up children
  if(my_wake_up_node->left_child != NULL){
    my_wake_up_node->left_child->awake = true;
  }
  if(my_wake_up_node->right_child != NULL){
    my_wake_up_node->right_child->awake = true;
  }
}
```

The numbers 4 and 2 were picked specifically as they have good theoretical properties.
The 4-ary trees mean that the flags for all threads can sit in one memory address.
The 2-ary tree means the signaling only takes $log_2(n)$ steps to wake up all threads.
Notice here that we do not need a complex atomic operation - just read and writes.

### Tournament barrier

The tournament barrier is similar to the MCS tree barrier, but instead of each thread having its own node, pairs of threads share a node.
Think of this node as a tournament which will have one 'winner' and 'loser' thread (which is pre-determined).
The winner thread will advance to the parent node and the loser thread will spin until the winner thread signals the tournament is over.

```c
struct tournament_node{
  bool loser_arrived = false; // flag for loser to indicate it has arrived
  bool tournament_over = false; // flag for winner to indicate it has arrived
  tournament_node * parent = NULL; // pointer to parent node
  bool is_winner; // indicates if this thread is the winner or loser
};

tournament_node *get_tournament_node(int thread_id);
bool is_winner(int thread_id);

void bar_recursive(tournament_node * B, bool is_winner){
  if (is_winner){
    while(B->loser_arrived == false); // spin
    if(B->parent != NULL){
      bar_recursive(B->parent, is_winner(B->parent_thread_id)); // signal parent
    }
    B->tournament_over = true; // signal tournament is over
  } else {
    B->loser_arrived = true; // signal arrival
    while(B->tournament_over == false); // spin
  }
}

void bar(int thread_id) {
  tournament_node *start_node = get_tournament_node(thread_id);
  bool is_winner = is_winner(thread_id);
  bar_recursive(start_node, is_winner);
}
```

A major advantage of the tournament barrier is there is no need for a atomic operation (other than read/write), as no two threads are ever writing to the same memory location.
Also notice that the memory needed for each thread is known before hand - so this can be placed close to the required CPU.
The only interactions between threads is sending a signal that either they have arrived or the tournament is over, we do not actually need shared memory to run this system.
This means it can be implemented on a cluster which only has message passing between nodes.
A downside for the tournament barrier against MCS is that only 2 nodes can share the same cache line - whereas MCS can have 4.

### Dissemination barrier

Within the tree based barriers there are normally  a single thread which is responsible for kicking off the rest of the processes to wake up.
This also means that the level of parallelism is limited by the height of the tree.
In the dissemination barrier, instead all processes 'gossip' amongst one another to signal they have arrived at the barrier.
This is done in a number of rounds where each thread $i$ messages node $i + 2^k$ saying it has arrived and waits for a message from node $i - 2^k$ on round $k$ (starting from $k=0$).
This has the nice effect that to progress past round $k$, atleast $2^{k+1}$ nodes must have made it to the barrier.
Therefore after round $ceil(log_2(n))$ all nodes must have arrived at the barrier - and we can safely proceed.

```c
int THREAD_COUNT;
int ROUNDS = ceil(log_2(THREAD_COUNT));

struct barrier{
  int position;
  bool flags[ROUNDS];
};

// Mapping from position to the barrier structure.
barrier *get_barrier(int position);

void bar(barrier B) {
  for(int k = 0; k < ROUNDS; k++){
    barrier *partner = get_barrier((B->position + 2^k) % THREAD_COUNT);
    B->flags[k] = true; // signal partner I have arrived
    while(B->flags[k] == false); // spin
  }
}
```

This barrier takes $O(n log(n))$ messages to complete, but each thread only needs $O(log(n))$ space.
As these are just messages the thread do not need to share memory - so this can be implemented on a cluster.
There is no hierarchy, so there is no single point of contention.

### Aside: Architectures for the system

When considering which barrier or lock to use, we need to consider the architecture we are running on.
The 4 main ones discussed here are:

- Cache coherent Shared Memory Processors (CC-SMP): These systems have hardware support for cache coherence.
  This means that if one CPU updates a memory location, all other CPUs will see the updated value.
  This is the most common architecture in modern systems.

- Cache coherent Non-Uniform Memory Access (CC-NUMA): These systems have hardware support for cache coherence, but memory access time is not uniform.
  This means that some memory locations are closer to some CPUs than others.

- Non-Cache coherent Non-Uniform Memory Access (NC-NUMA): These systems do not have hardware support for cache coherence, and memory access time is not uniform.
  This means that some memory locations are closer to some CPUs than others.

- Message Passing clusters: These systems do not have shared memory, and all communication is done via message passing.

### Performance comparison

TODO: Read the MCS paper and fill in this.

# Remote Procedure Calls (RPC)

Within processes that are running on the same machine, we still use the client-server model.
This enables safety as the processes can be running in separate protection domains (address spaces).
When programming the client-server model between machines we would use RPC - however could we use it within the same machine?
The main concern here is performance.

> [!note] Procedure call
> Within a process, a procedure call is a function call that is made within the same address space.
> Normally, the arguments are moved from the scope of the caller within the stack for a procedure call and vice versa for the return value.
> This all happens in compile time and is very fast.
> However, within RPC this will all happen at run time and will be slower.

## RPC performance concerns

The main issue with RPC between processes is the involvement of the kernel and the copying of data.
Lets break down the steps involved in an RPC call using message passing through the kernel:

1. The client traps to the kernel to call the RPC method.
The arguments get copied from the clients address space to the kernel's address space.
The kernel may need to check that the client is allowed to communicate with the server process.

2. The kernel switches to the server to execute the RPC method.
The arguments get copied from the kernel's address space to the server's address space.

3. The server then executes the RPC method with the arguments and calculates the return value.

4. The server traps to the kernel to return the value.
The return value gets copied from the server's address space to the kernel's address space.

5. The kernel switches to the client to return the value.
The return value gets copied from the kernel's address space to the client's address space.

This is 4 copies of data and 4 context switches for a single RPC call.
This is all happening at run time and is very slow.

This is in fact slightly worse for RPC calls when you consider the different components of the RPC stack.
For this we consider one direction client -> server.

1. The client prepares the arguments for the RPC call in the clients stack.

2. The client stub serialises the arguments into a message format.

3. The kernel copies the serialised message from the clients address space to the kernel's address space.

4. The kernel copies the serialised message from the kernel space to the server address space.

5. The server stub deserialises the message into the server's stack.

## Reducing RPC overhead (Bindings)

To make this faster, we will used shared memory and optimise for the common case - which should be calling the RPC method.
However, for this we make setting up the RPC connection more expensive (what we will call a binding).
We follow this process below:

1. The server registers its procedures with a 'name server'.

2. The client uses the name server to try and call the RPC method, this traps to the kernel.

3. The kernel checks with the server that the client is allowed to communicate with the server process.
If so, the server grants permission to the client.

4. The kernel then sets up a data structure called a Procedure Descriptor (PD) within the kernel.
The PD stores which entrypoint within the server to use for this RPC, the size of the argument stack (A-stack), and the number of simultaneous calls that can be made to the method.

5. The kernel also creates a shared memory region between the client and server (called the A-stack) for them to communicate without the intervention of the kernel.

6. The kernel returns a Binding Object (BO) to the client - within the kernel this is lined to the PD but for the client acts as permission to call the RPC method.

The for the client to call the method the following happens:

1. The client stubs copies the arguments from the client stack into the A-stack (which have to be passed by value - not reference).

2. The client then traps into the kernel presenting BO to call the method.

3. The kernel uses the BO to find the PD and then switches to the server process on exactly the entry point specified for this method.

4. The server stub then uses the A-stack to copy the arguments out into the server stack and can call the method.

5. Once the server is done calculating the return value, it copies the return value into the A-stack.

6. The server then traps back to the kernel to return control to the client.

7. Finally, the client stub can use the A-stack to copy the return value into the client stack.

This has the following advantages:

- There are half as many copies of data, as we no longer need to pass the information through the kernel.

- The stubs need to do less serialisation, as the message is doing less travelling so can stay in a format closer to how they would be represented in the stack of a process.

- Simplified permissions, by presenting the BO the kernel does not need to validate the client has access to the server.

However, we still suffer from the context switches to the kernel and the implicit costs of these switches from the loss of locality within the caches.

## RPC using SMP

For highly used RPC methods, in a shared memory processor we can avoid the loss of locality by pinning the server to a CPU.
This way we can keep the caches on that CPU warm with the server process.
The shared memory allows for the quick transfer between the client and server of the call arguments and returns.

## Summary

Using RPC within a machine is possible, but there are performance concerns.
However, this opens up better protection between processes and a cleaner programming model.
