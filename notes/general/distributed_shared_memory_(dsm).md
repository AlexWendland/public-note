---
aliases:
checked: false
created: 2025-04-13
draft: false
last_edited: 2025-04-13
title: Distributed shared memory (DSM)
tags:
  - OS
type: definition
---
>[!tldr] Distributed shared memory (DSM)
>Distributed shared memory is a [Peer distributed application](peer_distributed_application.md) which enables machines to share their memory and have access to memory which does not exist on the machine locally. This extends the machines effective memory size. Though the payoff is some memory access will be slower.
>
>The network will try to intelligently replicate memory locations to reduce memory latency for the machine. However this will required consistency protocols to ensure any replicated state is consistent between machines.

