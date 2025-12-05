---
aliases:
  - IPC
  - inter-process communication
checked: false
created: 2024-08-26
draft: false
last_edited: 2024-08-26
tags:
  - OS
title: Inter-process communication (IPC)
type: definition
---
>[!tldr] Inter-process communication (IPC)
>*Inter-process communication* is the method or API in which different [processes](process.md) can communicate with one another. There are four main methods to communicate messages between two [processes](process.md).
>1. **Message-passing IPC**: This is via the [OS](operating_system_(os).md) which offers an API to pass messages between [processes](process.md) the [OS](operating_system_(os).md) puts them on a message bus that is sent to the other [process](process.md). This has the advantage that it is managed by the [OS](operating_system_(os).md) and is safe - though it has the disadvantage of needing the [OS](operating_system_(os).md) which incurs a lot of overhead.
>2. **Shared memory IPC**: This lets two processes share some [physical memory](physical_memory.md) which is mapped into both their [virtual memory](virtual_memory.md) space. This means the [OS](operating_system_(os).md) is out of the way but the two processes must know how to use that shared memory with one another - sometimes having to re-implement code in the [OS](operating_system_(os).md).
>3. **Higher level semantics**: Such as shared files or [Remote Procedure Calls (RPC)](remote_procedure_calls_(rpc).md).
>4. **Synchronization**: Methods in which two processes can [synchronize](synchronization.md) so not to adversely effect one an others operation. Examples are [mutexes](mutex.md) or [semaphores](semaphores.md).
