---
aliases:
  - thread
  - threads
created: 2024-08-26
date_checked:
draft: false
last_edited: 2024-08-26
tags:
  - OS
title: Thread
type: definition
---
>[!tldr] Thread
> A *thread* is the smallest unit of execution within a [process](process.md), representing a single sequence of instructions that the [CPU](central_processing_unit_(cpu).md) can execute. Each thread within a [process](process.md) shares the process's resources, such as memory and file handles, but operates with its own set of [CPU registers](cpu_register.md), [stack](stack_(os).md), and [program counter](program_counter_(pc).md). In the [Process control block (PCB)](process_control_block_(pcb).md), the state of each thread is tracked, including its individual register values, program counter, and thread-specific data, while sharing the broader process-level information like memory space and [I/O](input_output_(io).md) resources.

