---
aliases: 
checked: false
created: 2025-04-13
last_edited: 2025-04-13
draft: false
tags:
  - OS
type: definition
---
>[!tldr] Weak consistency
>Weak consistency is a [[Consistency model|consistency model]] that introduces a new operation - synchronize. The model only guarantees that all operations before all synchronization  points will be visible in the order of the synchronization points when any process calls synchronize. There are variations of this:
>- Single sync (like above).
>- Separate sync per subset of state (e.g. page)
>- Separate entry/acquire vs exit/release operations.

