---
aliases:
checked: false
course: "[[CS6210 Advanced Operating Systems]]"
created: 2025-10-01
last_edited: 2025-10-01
draft: true
tags:
  - OMSCS
type: lecture
week: 5
---
# Week 5 - Distributed Systems

The definition of what a distributed system is varies but in this course we use the following 3 properties:

1. Nodes on the network are connected via some LAN or WAN.
2. Nodes do not share memory.
3. The computational event time is significantly smaller than the communication time.

Definition 3 is used a fair bit and within this you can consider a cluster of machines even within the same rack in a data center - distributed computing.

> [!note] Parallel vs Distributed
> The concerns of parallel and distributed computing can overlap, however the main difference is that in parallel computing, the nodes share memory and are tightly coupled. In distributed computing, the nodes do not share memory and are loosely coupled.

## Happened before relation

In distributed systems, it is useful to work out what should happen when and which events could be interleaved in different orders.
To this extent we define a relationship on events in a system, namely a -> b means a 'happened before b'. This is defined by the following:

- Process: If a and b are on the same process and a comes before b, then a -> b.
- Message: If a is a send event and b is the corresponding receive event, then a -> b.
- Transitivity: If a -> b and b -> c, then a -> c.
- Concurrency: If neither a -> b or b -> c, than a and b are concurrent (a || b).

## Lamports clock

Suppose we have processes $P_i$ for $1 \leq i \leq n$ and each process has events $e^i_j$ for $j \in \mathbb{N}$, where $e^i_j -> e^i_{j+1}$.

We then define a clock, $c: {e^i_j}_{1 \leq i \leq n, j \in \mathbb{N}} \rightarrow \mathbb{N}$ such that $e^a_b -> e^x_y \Rightarrow c(e^a_b) < c(e^x_y)$.

> [!note] Concurrent events
> Whilst $e^a_b -> e^x_y \Rightarrow c(e^a_b) < c(e^x_y)$ the opposite implication is NOT true, two concurrent events could be ordered arbitrarily.

### Total order

We can derive a total order $\Rightarrow$ from a clock $c: {e^i_j}_{1 \leq i \leq n, j \in \mathbb{N}} \rightarrow \mathbb{N}$ by ordering the processes $P_i$ (lets assume we do this by saying $P_i < P_j \Rightleftarrow i < j$.
The we define $\Rightarrow$ by the following:
- If $c(e^a_b) < c(e^x_y)$ then $e^a_b \Rightarrow e^x_y$.
- If $c(e^a_b) = c(e^x_y)$ and $P_a < P_x$ then $e^a_b \Rightarrow e^x_y$.

### Distributed M.E. Lock

Suppose you have a set of processes $P_i$ that want to establish a distributed mutual exclusion lock.
We can use the total ordering before to do this, each process messages all other processes with the clock time of when they want the clock with the PID.
Upon receiving a message from another process, each process acks the message.
As each process builds a queue of requests for the lock with a time associated to it, it can work out if it can hold the lock. Which can happen in the following situation:

- It is at the top of the queue.
- Each other process has acked its message or sent a message of its own.

Once it knows it can hold the lock, it enters the critical section and when done sends each other process an unlock message.
This is correct with the following assumptions:

- Messages arrive in order.
- No message is lost.
- The Queue is totally ordered using the clock time with the PID.

As described this lock takes $3(n-1)$ messages to obtain the lock, however there are efficiencies that can be made to make this alot better.

### Real world time
