---
aliases: 
checked: false
course: "[[CS6200 Graduate introduction to Operating Systems]]"
created: 2025-04-12
last_edited: 2025-04-12
publish: true
tags:
  - OMSCS
type: lecture
week: 13
---
# Week 13 - Remote Procedure Calls

## Additional reading

- [Implementing Remote Procedure Calls](https://s3.amazonaws.com/content.udacity-data.com/courses/ud923/references/ud923-birrell-nelson-paper.pdf)

## Remote procedure calls (RPC)

![[Remote procedure calls (PRC)]]

To achieve this [[Remote procedure calls (PRC)|RPC]] has some requirements:
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

