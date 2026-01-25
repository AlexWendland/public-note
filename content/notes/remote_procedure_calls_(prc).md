---
aliases:
  - RPC
created: 2025-04-12
date_checked:
draft: false
last_edited: 2025-04-12
tags:
  - OS
title: Remote procedure calls (PRC)
type: definition
---
>[!tldr] Remote procedure calls (PRC)
>A Remote Procedure Call (RPC) is a protocol that allows a program to execute a procedure (function) on a different address space, typically on another computer over a network, as if it were a local function call. This offers
>
>- *Transparency*: The programmer calls a function like normal, but behind the scenes, that call is sent to another machine or process.
> - *Abstraction*: The network communication, serialization, and deserialization are abstracted away from the programmer.
> - *Bidirectional*: RPC can be synchronous (waiting for a response) or asynchronous (fire-and-forget).
>- *Client-server model*: The caller is the client, and the callee (who implements the procedure) is the server.

