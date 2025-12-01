---
aliases:
checked: false
created: 2025-04-13
draft: false
last_edited: 2025-04-13
name: Sequential consistency
tags:
  - OS
type: definition
---
>[!tldr] Sequential consistency
>This is a [consistency model](consistency_model.md) that has the following rules:
>- Memory updates from different processors may be arbitrarily interleaved.
>- All processes will see the same interleaving.
>- Operations from the same process always appear in the order they were executed.

