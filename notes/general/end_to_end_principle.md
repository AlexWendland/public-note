---
aliases:
checked: false
created: 2024-05-23
draft: false
last_edited: 2024-05-23
name: End to end principle
tags:
  - networks
type: definition
---
>[!tldr] End to end principle
> The end to end principle states that certain functions in a [network](network.md), such as error correction or data integrity, are best implemented at the endpoints (source and destination) rather than in the intermediary nodes (like [routers](router.md) and [switches](switch.md)). This ensures more efficient and reliable communication by minimizing the complexity and potential points of failure within the network.
>
> For example [TCP](transmission_control_protocol_(tcp).md) handles error checking, data re-transmission, and flow control but this is handled in the application layer rather than within the [switches](switch.md) or [routers](router.md).

