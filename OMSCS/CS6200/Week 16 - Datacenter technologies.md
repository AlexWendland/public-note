---
aliases: 
checked: false
course: "[[CS6200 Graduate introduction to Operating Systems]]"
created: 2025-04-13
last_edited: 2025-04-13
publish: true
tags:
  - OMSCS
type: lecture
week: 16
---
# Week 16 - Data-center technologies

## Internet services

A internet service is simply one offered over a web interface. These normally consist of 3 layers:

- Presentation: Static content.
- Business logic: Dynamic content.
- Database tier: Data storage.

Whilst these layers are separated here they may be implemented on the same machine. Middleware can be offered to integrate the different layers together.

These different layers contact one another using [[Inter-process communication (IPC)|IPC]] methods such as [[Remote procedure calls (PRC)|RPC]] or shared memory (if they are located on the same machine).

To handle scale internet services are normally distributed across multi-process or multi-node "scale-out" architecture. This normally consists of a load-balancer that distributes load within the cluster. This follows the Boss-worker pattern where the workers could be:

- *Functionally homogeneous*: All workers are equal and the load-balancer round robins between them.
- *Functionally heterogeneous*: Nodes execute different tasks required for the internet service.

## Homogeneous architecture

These are ones where the workers are all equal. This enables a very simple load-balancer that does not need to keep much state about the different workers. It is very simple to scale up as you just add more of the same workers. However, this suffers from the workers not being able to utilize caching and if you need to process large amounts of data for each request - this can become slow.

![[homogeneous_architectures.png]]

## Heterogeneous architecture

These are ones where the workers are specialized to some kind of logic. This means each worker can optimism its cache or use devices that are specialized for that task. 

However, this adds considerable complexity to the front-end. As workers now are different the load balancer needs to keep track of which workers can do what. When increased demand comes to the system scaling up is not as simple as adding more workers you need to work out what workers are needed.

![[hetrogeneous_architectures.png]]

