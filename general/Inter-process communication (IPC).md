---
aliases:
  - IPC
  - inter-process communication
checked: false
created: 2024-08-26
last_edited: 2024-08-26
publish: true
tags:
  - OS
type: definition
---
>[!tldr] Inter-process communication (IPC)
>*Inter-process communication* is the method or API in which different [[Process|processes]] can communicate with one another. There are two main methods to communicate messages between two [[Process|processes]].
>1. **Message-passing IPC**: This is via the [[Operating system (OS)|OS]] which offers an API to pass messages between [[Process|processes]] the [[Operating system (OS)|OS]] puts them on a message bus that is sent to the other [[Process|process]]. This has the advantage that it is managed by the [[Operating system (OS)|OS]] and is safe - though it has the disadvantage of needing the [[Operating system (OS)|OS]] which incurs a lot of overhead. 
>2. **Shared memory IPC**: This lets two processes share some [[Physical memory|physical memory]] which is mapped into both their [[Virtual memory|virtual memory]] space. This means the [[Operating system (OS)|OS]] is out of the way but the two processes must know how to use that shared memory with one another - sometimes having to re-implement code in the [[Operating system (OS)|OS]].
>3. **Higher level semantics**: Such as shared files or [[Remote Procedure Calls (RPC)]].
>4. **Synchronization**: Methods in which two processes can [[Synchronization|synchronize]] so not to adversely effect one an others operation. Examples are [[Mutex|mutexes]] or [[Semaphores|semaphores]].