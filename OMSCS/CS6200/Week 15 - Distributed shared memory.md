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
week: 15
---
# Week 15 - Distributed shared memory

## Additional reading

- [Distributed Shared Memory: Concepts and Systems](https://s3.amazonaws.com/content.udacity-data.com/courses/ud923/references/ud923-protic-paper.pdf)

## Distributed shared memory

Distributed shared memory is similar to a [[Distributed file system (DFS)|distributed file system]] however all clients are also clients to others. They share the state mutually.

![[Peer distributed application]]

![[Distributed shared memory (DSM)]]

This technology is become more relevant in data centers since the development of [[Remote direct memory access (RDMA)]].

![[Remote direct memory access (RDMA)]]

## Hardware vs software support

The basic concept in distributed shared memory is when memory access is not local it goes via the network.

![[shared_memory.png]]

Whilst in data-centers they use hardware such as [[Remote direct memory access (RDMA)]] this is an expensive option. Other applications can achieve the same using software. 

