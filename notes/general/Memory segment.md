---
aliases:
  - segment
  - memory segments
checked: false
created: 2025-03-22
draft: false
last_edited: 2025-03-22
tags:
  - OS
type: definition
---
>[!tldr] Memory segment
>A _memory segment_ is a variable-sized block of memory used in [[Memory segmentation|segmentation]], an alternative to [[Paging system|paging]] for memory management. Instead of dividing memory into fixed-size [[Memory page|pages]], segmentation divides memory into logically distinct sections, such as code, data, and stack segments. Each [[Memory segment|segment]] has a base address and a limit, defining its size and boundaries. The [[Operating system (OS)|operating system]] and the [[Memory Management Unit (MMU)]] manage segment access using a [[Descriptor table|segment table]], which maps segment numbers to [[Physical memory|physical memory]]. Unlike [[Paging system|paging]], segmentation allows programs to organize memory based on logical structures rather than fixed-size blocks.
