---
aliases:
checked: false
course_code: CS6200
course_name: Graduate introduction to Operating Systems
created: 2025-04-12
draft: false
last_edited: 2025-04-12
tags:
  - OMSCS
title: Week 13 - Remote Procedure Calls
type: lecture
week: 13
---
# Additional reading

- [Implementing Remote Procedure Calls](https://s3.amazonaws.com/content.udacity-data.com/courses/ud923/references/ud923-birrell-nelson-paper.pdf)

# Remote procedure calls (RPC)

[Remote procedure calls (PRC)](../../general/remote_procedure_calls_(prc).md)

To achieve this [RPC](../../general/remote_procedure_calls_(prc).md) has some requirements:
- Offers a client and server interface.
- Implements a procedure call Interface.
	- When RPC was invented procedural languages where big, this is synchronous and when it is called remote procedure call.
- Type checking.
	- This offers error handling, and
	- packet bytes interpretation.
- Cross-machine conversations.
- Higher-level protocol.
	- Access control, fault tolerance, and
	- Can support different transport protocols.

Below is an example flow of an [RPC](../../general/remote_procedure_calls_(prc).md) call:

![Rpc Example](../../../static/images/rpc_example.png)

# Steps to carry out an RPC operation

1. *Register*: (Optional) The server registers what procedures it offers, the argument types and location.
2. *Bind*: Client binds to the connecting server (this bind can get reused for multiple connections).
3. *Call*: Client makes RPC call and control passes to the client stub.
4. *Marshal*: The client stub serialises all the arguments into a message.
5. *Send*: The client stub sends the message to the server.
6. *Receive*: Server receives the message, passes the message into the server stub.
7. *Unmarshal*: Server stub deserialises the message.
8. *Actual call*: The server stub hands the parameters to the local implementation to carry out the implementation.
9. *Result*: The local implementation hands the result back to the server stub.
10. Similar operations to 4-7 happen to send the result back to the client.

# Interface definition language

The goal of [RPC](../../general/remote_procedure_calls_(prc).md) is that the server and client do not need to be programmed together or even written in the same language. To achieve this we need some language agnostic way to define the methods that can be called and the messages that are needed by them. This is where an [Interface definition language (IDL)](../../general/interface_definition_language_(idl).md) comes in.

[Interface definition language (IDL)](../../general/interface_definition_language_(idl).md)

An important aspect to any [IDL](../../general/interface_definition_language_(idl).md) is it includes a version number. This allows for easy upgrades to any interface you have defined.

# Marshalling

Marshalling is the process of taking input parameters that could be anywhere within a processes address space and putting them into a message to be sent to the other party. This will include some standards on how to serialize different types such as arrays and integers.

Unmarshalling is the opposite procedure when the other party receives the message.

Both these will not need to be written by the developer - instead they will be built into how the [RPC](../../general/remote_procedure_calls_(prc).md) framework is built.

## What about pointers?

RPC frameworks have two choices when a pointer is passed in:
- Don't support it and throw an error, or
- Serialize the object the pointer is pointing at.

# Binding and Registry

For the server and client to connect the client needs to know the servers address and port that it is operating on. Also the client should know what functions the server offer and the expected inputs/outputs of these functions. After this is known the client can 'bind' to the server to make the calls.

Knowing where the server is and what functions it offers can either be done explicitly in a hard coded fashion or there can be a registry that lets potential clients know what machines and functions are out there.

The registry can either be hosted centrally or placed on each machine. This will offer a central way to get the servers that support some function name and a version of the protocol.

# Handling failure

[RPC](../../general/remote_procedure_calls_(prc).md) frameworks implement error handling however, due to the framework operating over a network it sometimes can not know the cause of the issue. Therefore it offers a best guess at issues within this framework.

# SunRPC

This is an [RPC](../../general/remote_procedure_calls_(prc).md) framework developed by Sun in the 80s (bought by Oracle) for unix. They made the following design choices:

- Hosts a registry on each machine,
- It uses the XDR [IDL](../../general/interface_definition_language_(idl).md).
	- This uses a rpcgen compiler to convert .x (XDR) files into language specific implementations.
- Pointers are allowed and serialized.
- It makes a best effort attempt to catch information about failures and has built in retries.

# Java RMI

This is an [RPC](../../general/remote_procedure_calls_(prc).md) framework also developed by Sun but specifically for the Java language.

![Java Rmi](../../../static/images/java_rmi.png)

As this is specific to Java, it uses that for its [IDL](../../general/interface_definition_language_(idl).md) the framework matches Java's [OOP](../../general/object_oriented_programming_(oop).md) semantics. The implementation is split into two layers:

- Remote reference layer: How it communicates unicast, broadcast, return-first, response, return-if-all-match logic.
- Transport layer: Whether it uses [TCP](../../general/transmission_control_protocol_(tcp).md) [UDP](../../general/user_datagram_protocol_(udp).md) or [IPC](../../general/inter-process_communication_(ipc).md).
