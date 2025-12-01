---
aliases:
checked: false
created: 2024-05-23
draft: false
last_edited: 2024-05-23
tags:
  - networks
type: definition
---
>[!tldr] End to end principle
> The end to end principle states that certain functions in a [[Network|network]], such as error correction or data integrity, are best implemented at the endpoints (source and destination) rather than in the intermediary nodes (like [[Router|routers]] and [[Switch|switches]]). This ensures more efficient and reliable communication by minimizing the complexity and potential points of failure within the network.
>
> For example [[Transmission Control Protocol (TCP)|TCP]] handles error checking, data re-transmission, and flow control but this is handled in the application layer rather than within the [[Switch|switches]] or [[Router|routers]].

