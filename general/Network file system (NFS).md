---
aliases:
  - NFS
checked: false
created: 2025-04-13
last_edited: 2025-04-13
publish: true
tags:
  - OS
type: definition
---
>[!tldr] Network file system (NFS)
>This is a [[Distributed file system (DFS)|distributed file system]] developed by Sun. This uses [[Remote Procedure Calls (RPC)]] to communicate between servers and client. When the client opens a request to a file, it creates a virtual file descriptor which contains details about the server and file. This is used by the client to read/write to the server. If the server dies that descriptor returns an error so the client knows there was an issue with the request.
>![[nfs_arcitecture.png]]

