---
aliases:
  - segmentation
checked: false
created: 2025-03-22
last_edited: 2025-03-22
publish: true
tags:
  - OS
type: definition
---
>[!tldr] Memory segmentation
>_Segmentation_ is a memory management technique that divides memory into logically distinct [[Memory segment|memory segments]], such as code, data, and stack segments, each with a variable size. Instead of using fixed-size blocks like [[Paging system|paging]], segmentation allows programs to allocate memory dynamically based on their needs. The [[Operating system (OS)|operating system]] manages memory through a [[Descriptor table|descriptor table]], which stores the base address and limit of each segment. Segmentation can reduce [[Internal fragmentation|internal fragmentation]] but may lead to [[External fragmentation|external fragmentation]] without additional management techniques.