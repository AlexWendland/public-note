---
aliases:
  - stack
  - stack overflow
checked: false
created: 2023-08-26
draft: false
last_edited: 2023-11-11
tags:
  - programming
  - computer-science
  - OS
title: Stack (OS)
type: definition
---
>[!tldr] Stack (OS)
> The *stack* of an application is a [FIFO](first_in_first_out_(fifo)_queue.md) queue of stack frames - these contains a functions parameters local variables and return address. These get added when a function is called and removed once a function completes. The stack acts as the control flow for a [process](process.md) determining where to return to once a function as completed. The stack has a fixed size when a process starts and if it goes beyond that size can cause a *stack overflow*.
