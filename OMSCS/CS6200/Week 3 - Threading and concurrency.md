---
aliases: 
checked: false
course: "[[CS6200 Graduate introduction to Operating Systems]]"
created: 2024-08-26
last_edited: 2024-08-26
publish: true
tags:
  - OMSCS
type: lecture
week: 3
---
# Week 3 - Threading and concurrency

["An Introduction to Programming with Threads"](https://s3.amazonaws.com/content.udacity-data.com/courses/ud923/references/ud923-birrell-paper.pdf) by Birrell

![[Thread]]

## Visual metaphor

Threads are like workers in a toy shop:
- is an active entity
	- Executing unit of toy order
- Works simultaneously with others
	- many workers completing toy orders
- requires coordination
	- sharing tools, parts, workstations

In comparison to a thread:
- is an active entity
	- executing unit of a [[Process|process]]
- works simultaneously with others
	- many threads executing
- requires coordination
	- sharing of [[Input output (IO)|IO]] devices, [[Central processing unit (CPU)|CPU]], and [[Virtual memory|virtual memory]].

## Difference between a process and a thread

Each [[Process|process]] has its own [[Address space (OS)|address space]] and [[Process control block (PCB)|PCB]] whereas each [[Thread|thread]] in a [[Process|process]] shares the same [[Address space (OS)|address space]], code and data but has its own [[CPU register|CPU registers]], [[Program counter (PC)|program counter]], and [[Stack (OS)|stack]]. A [[Thread|thread]] does not have its own [[Process control block (PCB)|PCB]] but its state is tracked in the [[Process|process]] [[Process control block (PCB)|PCB]].

![[process_vs_thread.png]]

## Benefits of multithreading

Threads allow us to parallelise a process over multiple cores without incurring the code complexity of [[Inter-process communication (IPC)]] or the overhead of multiple [[Process control block (PCB)|PCB]] instances. You can specialise threads for a particular task that needs the same items from the [[Cache|cache]] this allows you to run the task off a hot cache all the time.

Multi-threading on a single core also can be efficient. As one of the largest costs in [[Context switch (CPU)|context switching]] is to remap the [[Address space (OS)|address space]] the time it takes to [[Context switch (CPU)|context switch]] between [[Thread|threads]] is lower than that for [[Process|processes]]. Therefore if you have [[Input output (IO)|I/O]] bound tasks using multi-threading can improve performance.

## Downsides of mulitithreading

Now threads have access to the same [[Virtual memory|virtual memory]] they can perform operations on the same bit of memory which can lead to unintended outcomes. For example two threads incrementing a number leading to the number only being incremented by one.

## Concurrency control mechanisms

### Mutual exclusion

You can limit certain actions to only be carried out by one thread at a time. This is called mutex.

### Threads waiting

Similar to [[Process|processes]] threads can enter a wait state for [[Input output (IO)|I/O]] operations or other conditions. This is controlled by condition variables.

### Threads getting woken up

Threads can also wake each other up.

## Thread creation

Threads interfaces are different between providers. In this course we follow on specific implementation.

Threads have a data-structure that tracks their current state. Containing data like:
- Tread ID,
- Process it belongs to,
- [[CPU register]],
- [[Stack (OS)|stack]],
- attributes.

A [[Thread|thread]] can start another [[Thread|thread]] using the Fork command (not the same as UNIX fork). This takes a program to run and the arguments and starts a new thread.

A [[Thread|thread]] can be terminated using the `join` command which makes the thread calling it wait till the joined thread finishes and then gets any returned value.

>[!note] Different threads execute operations in a non-deterministic manner
> If two threads are safely writing to a list the order of those writes are non-deterministic as it is up to the kernel to schedule them.

## Mutex

![[Mutex]]

![[Conditional mutex]]

### Example: Reader/writer Problem

Suppose we want to read and write to some resource. We are fine with multiple [[Thread|threads]] reading the resource but we only want one writer ever writing to it and we do not want anyone reading from it at that time.

We could put a [[Mutex|mutex]] on the resource operations though that would only let one reader access it at one time. Instead we make a proxy variable and put a [[Mutex|mutex]] to access that. Lets consider the different states:
- No writer or reader accessing it (counter == 0),
- Any number of readers accessing it (counter > 0), or
- A single writer accessing it (counter == -1).

``` psuedocode
Mutex: counter_mutex
Condition: write_phase
Condition: read_phase
int: resource_counter

// Reader code
...
lock(mutex){
	while (resource_counter == -1):
		wait(mutex, read_phase)
	resource_counter++
}
// READ RESOURCE
lock(mutex){
	resource_counter--
	if(resource_counter == 0):
		signal(write_phase)
}
...
// Writer code
...
lock(mutex){
	while (resource_counter != 0):
		wait(mutex, write_phase)
	resource_conter = -1
}
// WRITE RESOURCE
lock(mutex){
	resource_counter = 0
	broadcast(read_phase)
	signal(write_phase)
}
...
```

>[!note] Use while on the condition in the critical section instead of if
> There are multiple reasons this is best practice:
> - This allows for multiple threads waiting on the same condition,
> - Anyone thread might not be the first thread to access it after it has been released,
> - The condition might have changed since it has been woken up.

The critical sections follow a similar structure. 

```pseudocode
lock(mutex){
	while !predicate_for_ok_state:
		wait(mutex, conditional_variable)
	update state => update predicate
	signal/broadcast conditional variables
}
```

In this example the real critical code is not protected by a [[Mutex|mutex]] which is the reading and writing of the resource. This proxy variable pattern is common and follows a general stricture.

### Proxy variable pattern

When controlling an operation using a proxy variable it uses the following pattern:

```pseudocode
// ENTER BLOCK
Controlled operation
// EXIT BLOCK

// ENTER BLOCK
lock(mutex){
	while(!predicate_for_access):
		wait(mutex, conditional_variable)
	update predicate for access
}

//EXIT BLOCK
lock(mutex){
	update predicate for stopping access
	signal/broadcast depending on predicate
}
```

### Common bugs with [[Mutex|mutexs]] and how to avoid them

- Use clear names for mutexs and conditional variables so you know what they refer too.
- Check you are locking and unlocking when accessing the resource.
- Check you have matched lock and unlock blocks when using the proxy pattern.
- Remember to use a single mutex for a single resource.
- Check the conditions for signalling and broadcasting. 
- Check you are not using signal when you need to use broadcast.
	- The other-way around is not an issue for correctness just efficiency as it will wake up the thread and should still execute correctly.
	- If you use signal the other threads may never wake up.
- Do you need execution order guarantees? 
	- Waking up threads does not guarantee this. 
- Spurious wakeups
- Deadlocks

### Spurious wakeups

When waking up threads in a mutex block using signal/broadcast lf you still hold the mutex then the threads will just be moved to waiting on the mutex as it is still held. This is a *spurious wakeup* as we pay the cost of  [[Context switch (CPU)|context switching]] to the thread just to hand back control to the [[Central processing unit (CPU)|CPU]].

This can sometimes be mitigated by moving the signal/broadcast out of the [[Mutex|mutex]] block.

```psuedocode
// WRITE RESOURCE WITH SPURIOUS WAKEUP
lock(mutex){
	resource_counter = 0
	broadcast(read_phase)
	signal(write_phase)
}
// WRITE RSOURCE WITHOUT SPURIOUS WAKEUP
lock(mutex){
	resource_counter = 0
}
broadcast(read_phase)
signal(write_phase)
```

Though this can only be done if the signal/broadcast does not rely on a controlled resource like the resource counter in the above example.

### Deadlocks

![[Deadlock]]

There are a couple techniques for solving or preventing deadlocks:
- Fine-grain locking: Forcing threads to only hold one [[Mutex|mutex]] at a time
	- This is very limiting to what locks can be used for.
- Composite [[Mutex|mutex]] that combine access to multiple [[Mutex|mutex]]. 
	- This can be hard to implement and enforce across a wide code base.
- [[Mutex]] ordering: You have to obtain [[Mutex|mutex]] in a given order.
	- This is the most common solution.
	- You have to enforce this order which can be complicated in a large code base.
- Rollback: Detect when deadlocks occur and rollback one of the threads to before the deadlock.
	- This is very expensive to implement and involves writing code that can be rolled back.
	- You can not use external code that can not be rolled back.
- Ostrich technique: Hope it does not happen and if it does restart the system.
	- Terrible to do but very easy to implement.

## Thread level

The concept of the [[Thread|thread]] exists at the kernel level and at the process level that can have its own thread scheduler. Then it is up to the process how it wants to map the threads within the process to threads on the kernel. Threads on the kernel are allocated to the [[Central processing unit (CPU)|CPU]] so to get use [[Parallelisation|parallelism]] whereas multiple [[Process|process]] [[Thread|threads]] on the same kernel [[Thread|thread]] run [[Concurrency|concurrently]] but not in [[Parallelisation|parallel]].



