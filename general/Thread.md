---
aliases:
  - thread
  - threads
checked: false
created: 2024-08-26
last_edited: 2024-08-26
draft: false
tags:
  - OS
type: definition
---
>[!tldr] Thread
> A *thread* is the smallest unit of execution within a [[Process|process]], representing a single sequence of instructions that the [[Central processing unit (CPU)|CPU]] can execute. Each thread within a [[Process|process]] shares the process's resources, such as memory and file handles, but operates with its own set of [[CPU register|CPU registers]], [[Stack (OS)|stack]], and [[Program counter (PC)|program counter]]. In the [[Process control block (PCB)]], the state of each thread is tracked, including its individual register values, program counter, and thread-specific data, while sharing the broader process-level information like memory space and [[Input output (IO)|I/O]] resources.

