---
aliases:
checked: false
course: "[[CS6210 Advanced Operating Systems]]"
created: 2025-11-20
last_edited: 2025-11-20
draft: true
tags:
  - OMSCS
type: lecture
week: 8
---
# Week 8 - Internet Computing

Normally web based issues are called 'embarrassingly parallel'.

> [!definition] Embarrassingly parallel
> These problems can be broken down into easy to do parallel operations, such as accessing email, doing a web search, or downloading files.
> No two clients rely on each other so all computation can be broken down on the per user level.

## Issues in giant scale systems

The structure of giant scale internet services normally follows the below pattern:

- Clients on the outside of the network.

- You come through some IP network.

- There is some load manager moving load between different back end servers.

- Back end servers, often on the order of 100 to 1000 servers

![Giant Scale System Structure](../../images/giant_scale_systems_structure.png)

With running one of these services, you need to know how to handle server failures - as in this case it is when rather than if one happens.

### Sense of scale

As of 2000:

| Service               | Nodes   | Queries    | CPUs/Node |
| --------------------- | ------- | ---------- | --------- |
| AOL Web               | > 1,000 | 10B/day    | 4-CPU     |
| Inktomi search engine | > 1,000 | > 80M/day  | 2-CPU     |
| Geocities             | > 300   | 25M/day    | ???       |
| Anon Web-based email  | > 5,000 | 1B/day     | ???       |

There are distinct advantages of structuring a system like this:

- Horizontal scaling: adding more nodes to the system scales it up.
- Cost control: 

### Load manager

There are different strategies we can take for load balancing requests:

- Round robin: Each requests gets sent to a different server to be handled.
This is done at the server level which makes it very efficient.
However, we struggle with handling servers that are down.
This also assume all machines on the network are equal and for the same thing.

- Layer 4 switches (Transport layer): This can inspect who the packet is intended to be for and make decisions on where to send that packet based on that.
For example this allows us to act as a reverse proxy to send packets intended for one application to a specific subset of servers.
This can also hide down servers from the client using a Backplane with the servers it is serving.
This Backplane can also be used for higher level semantics such as sending requests with particular body to different instances - this allows for different nodes to only replicated limited data for their preferred queries.

### DQ Principle

This theory is about matching demand with supply and varying parameters around this.
We start with some definitions:

- Q_0: The total number of queries we need to server in this time step.

- Q_c: The number of queries we handled in this time step.

- Yield: Q = Q_c/ Q_0 \in [0,1] the proportion of the queries we handled in this time step.

- D_f: The full amount of data the system holds to handle this query.

- D_v: The amount of data we use to server requests in this time step.

- Harvest: D = D_v/ D_f \in [0,1] the proportion of the data we used to server requests in this time step.
This is a proxy for how 'well' we handled the request - did we use all possible websites to check against your query or just a limited set of them.

It is assumed for a given set up the product DQ is a constant.
This means that there is a payoff to have if the constant DQ is not 1.
We can either server a limited set of requests at the full quality or we can offer all the queries at a degraded quality.

When thinking about D, what it is in reality depends on how the system is limited.
For example you could be I/O bound, as you simply need to process a lot of data to handle a request.
However, in most giant scale services it is more likely that they are network bound.
This means it is hard to scale up the DQ constant at some points - as getting more network may be out of your control.

There are some metrics people talk about for huge data centers:

- I/O ops per second: How many I/O operations per second the system can handle.
- Mean time to repair: How long does it take for a server to recover after a failure.
- Mean time between failure: How long does it take for a server to go down.
- Uptime: This is defined by MTTR and MTBF as (MTBF - MTTR)/MTBF and expressed as number of 9's so 5 9's is 0.99999 as this ratio.

However, uptime has its limitations.
For example if a failure happens in down time - then no one really cares.
