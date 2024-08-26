---
aliases:
  - stack
  - stack overflow
checked: false
created: 2023-08-26
last_edited: 2023-11-11
publish: true
tags:
  - programming
  - computer-science
  - OS
type: definition
---
>[!tldr] Stack (OS)
> The *stack* of an application is a [[First in first out (FIFO) queue|FIFO]] queue of stack frames - these contains a functions parameters local variables and return address. These get added when a function is called and removed once a function completes. The stack acts as the control flow for a [[Process|process]] determining where to return to once a function as completed. The stack has a fixed size when a process starts and if it goes beyond that size can cause a *stack overflow*.
