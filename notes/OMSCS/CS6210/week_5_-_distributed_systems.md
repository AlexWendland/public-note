---
aliases:
checked: false
course_code: CS6210
course_name: Advanced Operating Systems
created: 2025-10-01
draft: false
last_edited: 2025-10-01
tags:
  - OMSCS
title: Week 5 - Distributed Systems
type: lecture
week: 5
---

The definition of what a distributed system is varies but in this course we use the following 3 properties:

1. Nodes on the network are connected via some LAN or WAN.
2. Nodes do not share memory.
3. The computational event time is significantly smaller than the communication time.

Definition 3 is used a fair bit and within this you can consider a cluster of machines even within the same rack in a data center - distributed computing.

> [!note] Parallel vs Distributed
> The concerns of parallel and distributed computing can overlap, however the main difference is that in parallel computing, the nodes share memory and are tightly coupled. In distributed computing, the nodes do not share memory and are loosely coupled.

# Happened before relation

In distributed systems, it is useful to work out what should happen when and which events could be interleaved in different orders.
To this extent we define a relationship on events in a system, namely a -> b means a 'happened before b'. This is defined by the following:

- Process: If a and b are on the same process and a comes before b, then a -> b.
- Message: If a is a send event and b is the corresponding receive event, then a -> b.
- Transitivity: If a -> b and b -> c, then a -> c.
- Concurrency: If neither a -> b or b -> c, than a and b are concurrent (a || b).

# Lamports clock

Suppose we have processes $P_i$ for $1 \leq i \leq n$ and each process has events $e^i_j$ for $j \in \mathbb{N}$, where $e^i_j -> e^i_{j+1}$.

We then define a clock, $c: {e^i_j}_{1 \leq i \leq n, j \in \mathbb{N}} \rightarrow \mathbb{N}$ such that $e^a_b -> e^x_y \Rightarrow c(e^a_b) < c(e^x_y)$.

> [!note] Concurrent events
> Whilst $e^a_b -> e^x_y \Rightarrow c(e^a_b) < c(e^x_y)$ the opposite implication is NOT true, two concurrent events could be ordered arbitrarily.

## Total order

We can derive a total order $\Rightarrow$ from a clock $c: {e^i_j}_{1 \leq i \leq n, j \in \mathbb{N}} \rightarrow \mathbb{N}$ by ordering the processes $P_i$ (lets assume we do this by saying $P_i < P_j \Rightleftarrow i < j$.
The we define $\Rightarrow$ by the following:
- If $c(e^a_b) < c(e^x_y)$ then $e^a_b \Rightarrow e^x_y$.
- If $c(e^a_b) = c(e^x_y)$ and $P_a < P_x$ then $e^a_b \Rightarrow e^x_y$.

## Distributed M.E. Lock

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

# Real world time

Given the function $c$ is called a clock - in the real world we use a clock.
We may assume clocks are all the same but in reality this is not commonly the case - two different machines may have different times.
To handle this we try to make assumptions about 'how' off these clocks are from the consensus.

Now instead of having a global clock $c$ we have a per-process clock $c_i: \mathbb{R} \rightarrow \mathbb{R}$ for each process $P_i$.

## Lamports Physical Clock

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

# Distributed systems

Here it is important to differentiate between two terms:

- Latency: The time it takes for a message to get from one process to another.
- Throughput: The number of events per unit time (Bandwidth is a measure of throughput).

## RPC latency

RCP has many repeated steps that cause latency such as:

- Copying data

- Control transfer

- Protocol processing

We look at ways to reduce these.

### Data copying

There are normally 3 copies:

- Client stubs copy arguments into a message.

- Kernel copies message into kernel memory.

- Server copies message from the kernel.

The last one has to happen as the message needs to be passed to the server however we could skip the first one.
There are two ways this could happen:

1. The client stubs are loaded into the kernel and it marshals directly into the kernel memory.

2. The client stubs stay in the user space but copy into a shared descriptor between the user and kernel space.

The first option is unsafe for the operating system - however the second offers a real option to cut down on the amount of data copying.

### Control transfer

There are four control transfers:

- Client wait: This passes control from the client thread to another thread on the client to do work whilst we wait for the RPC process.

- Server switch: This switches to the server thread to handle the RPC call.

- Server wait: This passes control from the RPC server thread back to another server process.

- Client switch: This switches back to the client thread to handle the response.

In reality, only the switch waits are on the critical path.
With the wait switches being able to be delayed until the network transfer is complete.
However, in super critical RPC calls we can reduce this to one control transfer by spinning on the client thread meaning we do not need the client switch back at the end.
Though this does waste CPU cycles on the client machine.

### Protocol processing

When choosing the protocol to use RPC over - normally you have a reliability vs performance payoff.
However, if you are only using reliable LAN networks - you don't need to prioritise reliability as much.
Therefore you can drop a lot of reliability measures that cause delays such as:

- No low level acks: We expect all packages to get through reducing the number of messages sent.

- Remove hardware checksums: We assume no corruption on the LAN.

- No client side buffering: Instead of buffering we can get the client to resend.

- Overlap server side buffering with result transmission: Whilst running the whole RPC call again might be costly we can first send the message before buffering it for re-transmission.
This removes buffering from the critical path.

# Active networks

We talk about active networks in the context of the internet.
We can say that traditional internet routing is passive, it looks at the message identifies the destination and routes it accordingly.
In comparison, an active network is one where the routers can be programmed or configured to route traffic based on the needs of the application.

As a motivating example, think of needing to send a message to n individuals on the other side of the internet.
In passive networks you need to send n message - each addressed to the different users.
In an active network you could send one message to a node close to the recipients then branch the message off - reducing the network overhead.

Due to the nature of the internet we can not guarantee that all nodes in our network are active.
Therefore normally we use passive nodes to route our messages.
However, we can seek to use active nodes on the edge of the network as we are using it.

## Active Node Transfer System (ANTS)

The ANTS tool kit is an application level process for building smarter routing.
This comes with a small well defined API of what routers can do.
The along with your IP-header and payload there is an additional ANTS header.

```
ANTS Packet

           <--- ANTS Header --->
+---------+-------+----+----+---+-------+
|IP-header|Version|Type|Prev|hdr|Payload|
+---------+-------+----+----+---+-------+
           <------ ANTS Capsual ------->
```

This allows for normal routing of the packet using the IP-header.
However, the ANTS header allows for more functionality, which there are two key fields:

- Type: This is the hash of the code to be ran on the active node.

- Prev: This is the previous node that ran this code.

Instead of the packet containing the code, ANTS packets rely on the routers speaking to other nodes in the network to download the code.
It will reach out to the node defined in the Prev (previous) field who ran the code last.
Then it will download the code from them, and check it is valid using the type field.
This requires more network activity per packet - however we really would only use this for 'network flows' i.e. lots of packets all following the same path.
Then once the router has the code for the first packet it can simply run the same code for all subsequent packets.

> [!note] What if Prev doesn't have the code?
> In this case we just drop the packet - this happens on the internet a lot already.
> Therefore, the sender needs to take precautions on this happening - similar to TCP.

ANTS defines a basic API to use on each router:

- getAddress, getChannel, time: Get information about the router.

- routeForNode, deliverToApp: Send a capsual somewhere else.

- put, get, remove: Manage local storage on the router.

Most importantly, ANTS programmes can manipulate data on what is called the 'soft store' - data the router allows the packet to use.
This is where the code for the application is stored itself.

The important thing for all these applications is that they are lightweight and quick to execute.
The minimal API supports that whilst still allowing for useful applications to be built.

## Applications

Below is a list of applications for ANTS:

- Protocol independent multi-cast: As described before, we can use active nodes to branch messages to multiple recipients.

- Reliable multi-cast: We can build reliability into the multi-cast application by having nodes ack messages and re-send lost messages.

- Congestion notifications: We can have nodes monitor congestion and send messages back to the sender to slow down sending rates.

- Private IP (PIP): We can have nodes encrypt data on the fly to allow for private communication over public networks.

- Anycast routing: We can have nodes route messages to the 'best' node in a set of nodes - for example the least loaded web server.

Though these are all network applications, which is why ANTS brought about in the 1990's didn't take off - as it didn't have a real problem to solve.
However, in modern computing with data centers and cloud computing - active networks could have a real use case.
This has evolved into the idea of programmable networks and software defined networking (SDN).

## Payoffs

Pro:

- flexibility from App perspective

Cons:

- Protection threat: You are running anyones code on your router - this is a big security risk!
You also need to ensure isolation for different network flows.

  - ANTS runtime safety (this uses Java sandboxing to isolate code)

  - Code spoofing (uses the type to ensure no tampering)

  - Soft state integrity (very limited API means soft state can't be too complex)

- Resource management threats: You need to ensure that no one application can hog all the resources on the router.

  - At each node (restricted API ensures no complex resource usage)

  - Flooding the network (the internet is already susceptible to this)

## Feasibility

There are some major blockers to making ANTS and active networks more generally feasible.

1. Router makers loath to opening up the network.

  a. The internet is ruled by mass adoption, so router makers don't want to rock the boat and lose market share.

  b. Only feasible on the edge, not core routers.

2. Software routing cannot match hardware routing speeds.

  a. Hardware is VERY fast anything that needs to use software is going to run slower.

  b. Only feasible on the edges, the core needs to be fast to manage with the vast amounts of data.

3. Social + Psychological reasons.

  a. People don't like the idea of letting anyone run code on their router - it is a big risk.

# Component based OS services

In this subsection we explore the approach to build OS services as described in:

Building reliable, high-performance communication systems from components

The core idea is to take the approach of Micro-kernels and apply it to building your OS services as well.
This is define small building blocks and compose these to make our services.
However, as with micro-kernels component driven software may have overheads, such as copying memory, conforming to interfaces, and loss of locality.
This paper explores this and methods to get around it.

## Development process

In the paper they suggestion a 3 phase process to developing these components and services:

1. Specification: Define the requirements of the service.

  a. This is done using IOA (Input/Output Automata) which using c-like syntax and composition operators.

2. Code: Turn the requirements and specification into code that a computer can run.

  a. This is done in OCAML - a functional programming language.
It is object oriented but still as efficient as C.
It also has good integration with the IOA specifications.

3. Optimization: To remove the inefficiency layering our stack into different components has - we try to remove as much unneeded overhead as possible.

  a. This is done using a tool suit called Nuprl - which optimizes OCAML code using formal methods which are proven to be correct.
This guarantees the input and output code are equivalent.

## Getting an implementation

The first two steps can be iteratively built up over time.
You first start by writing a Abstract Behavioral Specification (ABS) - which is a high level specification of the service.
This will be written in IOA which you can use to prove properties about this service.

Then you can refine the ABS into a more Concrete Behavioural specification (CBS) - which is closer to the code you will write.
From this you can then convert the CBS into a implementation written in OCAML.
This issue with the implementation is it can be derived from the ABS but you can not prove it is equivalent.
Therefore, you don't know for sure it does have the properties you desire.

When building this implementation we want to focus on build an ensemble of components that can be composed together to make our service.
These components should have a well defined interface above and below so they fit together nicely.

## Optimization

The choice of using the layering ensemble method above can lead to inefficiencies mentioned above.
However, this allows for more flexibility whilst developing the application.
Though as a OS designer we need the system to be performant as it will be some of the most run code on a machine.

There are several sources of inefficiency here:

- Ocaml has implicit garbage collection, however this is costly and explicit garbage collection is much faster.

- As we move between interfaces we will marshal/unmarshal arguments to move between interfaces.

- When doing optimisations we want to focus on the common case and this can be 'fast tracked' at the expense of the other paths through the system.

Nuprl is a tool box which takes in unoptimized code and returned optimized code which is provably equivalent to the input.
There are tools which allow the conversion between Ocaml and the Nuprl coding language.
The optimization is part automated and part manual.
This is a 2 step process:

1. Static Optimization.

  a. This is where a Ocaml and Nuprl expert look at the code together and agree manual optimisations that can be done together.
This is done layer by layer and requires checking that these optimizations are correct and useful for the code.
For example, inlining functions in functional languages can make sizable performance improvements but need to be agreed that it is useful.

  b. These optimizations are normally done within each component - not between the components.

2. Dynamic Optimization.

  a. This is driven by the Nuprl framework.
This optimizes between layers, that collapses layers.
This is driven by Common Case Predicates (CCP).
This are checks that can be done against the input which if pass define the common case and can bypass layers to speed up their handling.

