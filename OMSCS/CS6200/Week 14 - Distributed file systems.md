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

There are different models for a [[Distributed file system (DFS)]] in the client server model.

### Download model

In this model the client downloads the whole file from the server, applies any edits locally and re-uploads the file to the remote server.

![[download_model.png]]

This means:
- edits to the file are done locally and are fast,
- the client has to download the entire file and upload it even if they only need to edit a small part, and
- the server loses all control of the file whilst the client is using it which limits sharing.

### Fully remote model

In this model all commands the client wishes to do to the file are sent to the server who applies them on the server directly.

![[fully_remote_model.png]]

This means:
- file accesses are centralized,
- Consistency is easy to reason about, but
- every file operation pays the network cost.

### Remote access with caching

In this model we allow clients to locally store parts of files. However the clients will notify the server of their interactions with the file - such as if they edit it or delete it. Equally the server is responsible for updating their cache if other clients change the file.

This means:
- Low latency operations on cached files,
- Server load is reduced in comparison to the fully remote model,
- Server is aware of what clients are doing,
- Server has control into whihc accesses can be permitted, however
- The server is a lot more complex to handle all these consistency mechanisms. 

## State management

The server can either be stateful or stateless this has implications on the design of the server.

### Stateless

This works in both extreme models but does not work with caching. This means:

- Cannot support caching or more complex consistency management.
- Every request will need to contain the full context, meaning larger message sizes.
- No resources on the server are used to maintain the state.
- On failure you can just restart the application.

### Stateful

Needed for the caching model. The server tracks the state of the different clients.

- Can support locking, caching, and incremental operations.
- On failure we will need checkpointing or a recovery mechanism.
- Overheads on the server to maintain the state and consistency between the clients.

## Caching

This means that clients store a portion of the file system locally to do operations. When we do this we need to introduce coherence mechanisms.

For example, if two clients have the file F cached locally. When one of them updates the file how does the second client find out about it. From processor memory we had two options for this:

- Write-update: Update the cache of the second client.
- Write-invalidate: Alert the client to delete their cache.

However with [[Depth-first search (DFS)|DFS]] we have much larger network latency than in [[Central processing unit (CPU)|CPU]] so the question about when this happens is important:

- Does the client notify the server when changes happen, or
- Does the server poll for changes in the local cache.

## File sharing semantics

When two processes access a file on one machine changes become instantly available. (This is called UNIX semantics.)

![[single_machine_semantics.png]]

However on two machines this might not be the case and edits can happen on 'stale' data if the consistency model is not strong enough.

![[second_machine_semantics.png]]

*Session semantics*: This refers to syncs on open and close operations of a file. With the time between the open and close being a session. In this case the client checks on open they have the latest file and saves back to the server on close.

Sessions can be long if the client is editing a file for a long time - therefore it can be useful to introduce *periodic updates*. This could involve:

- The client writes-back periodically.
- The server invalidates the caches periodically which introduces a bound on inconsistency. 
- To support the above [[Distributed file system (DFS)]] can introduce flush/sync operations.

The server can implement *immutable files* which never get modified only have new files created.

The server can implement *transactions* so that all edits to a file are atomic and based on a particular version.

## Access patterns

When choosing a type of semantics it is important to understand the file access patterns:
- How often are files shared,
- How often are files written too,
- Importance of consistent view, or
- Does the access pattern change based on the type of file? Does it change for directories?

