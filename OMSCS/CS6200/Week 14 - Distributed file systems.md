---
aliases: 
checked: false
course: "[[CS6200 Graduate introduction to Operating Systems]]"
created: 2024-12-31
last_edited: 2024-12-31
publish: true
tags:
  - OMSCS
type: lecture
week: 14
---
# Week 14 - Distributed file systems

## Additional reading

["Caching in the Sprite Network File System"](https://s3.amazonaws.com/content.udacity-data.com/courses/ud923/references/ud923-nelson-paper.pdf)

## Distributed file system

![[Distributed file system (DFS)]]

There are different models for distributing files:
- Client/server model: A client with the file system talks to a single server who has all the files.
- Client/server-cluster: A client contacts a cluster of servers who all have files the client can get files from. This can take different forms
	- *Replicated*: Each server has all the files.
	- *Partitioned*: each server serves part of the file system.
	- *Both*: Files are replicated and partitioned between machines (this is functionally how most large providers operate).
- *Peer-to-peer*: A cluster of computers act as peer backups for one another. (This will be covered in more detail next lecture.)

## Implementation

We talk about 2 extremes of how to implement a [[Distributed file system (DFS)]] in the client server model.

### Download model

In this mode