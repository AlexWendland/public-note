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

## Real world time

Given the function $c$ is called a clock - in the real world we use a clock.
We may assume clocks are all the same but in reality this is not commonly the case - two different machines may have different times.
To handle this we try to make assumptions about 'how' off these clocks are from the consensus.

Now instead of having a global clock $c$ we have a per-process clock $c_i: \mathbb{R} \rightarrow \mathbb{R}$ for each process $P_i$.

### Lamports Physical Clock

We say $e^i_x \mapsto e^j_y$ if $c_i(e^i_x) < c_j(e^j_y)$.
For the system of clocks to be 'good' we require the following conditions:

1. PC1: Bound on individual clock difference
$$
\left ( \frac{dc_i(t)}{dt} - 1 \right ) < \kappa, \forall i, (\kappa << 1).
$$

2. PC2: Bound on mutual drift
$$
c_i(t) - c_j(t) < \epsilon, \forall i,j.
$$

These rules in essence say that no clock is too far off real time and that no two clocks are that far away from eachother.
This means they are all fairly consistent.

Then for these process clock times to be useful we need to bound their drift in relation to interprocess communication time.
The faster you are communicating the more drift within your clocks matter.

Let $\mu$ be a lower bound on IPC.
Then suppose $P_i$ sends a message to $P_j$ at time $t$.
To avoid anomalies we would want that:

1. $c_i(t + \mu) - c_j(t) > 0$ (Clock time on P_i when the message has arrived is after the clock time on P_j when the message was sent.)

2. $c_i(t + \mu) - c_i(t) > \mu(1-\kappa)$ (this comes from PC1).

Combining these two we get:

$$
\mu \geq \frac{\epsilon}{1 - \kappa}
$$

## Distributed systems

Here it is important to differntiate between two terms:

- Latency: The time it takes for a message to get from one process to another.
- Throughput: The number of events per unit time (Bandwidth is a measure of throughput).
