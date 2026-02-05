---
aliases:
  - spurious wakeups
created: 2024-09-05
date_checked: 2026-02-05
draft: false
last_edited: 2026-02-05
tags:
  - OS
title: Spurious wakeups
type: definition
---
>[!note] Spurious wakeups
>When waking up [threads](thread.md) in a [mutex](mutex.md) block using signal/broadcast if you still hold the mutex then the threads will just be moved to waiting on the mutex as it is still held. This is a *spurious wakeup* as we pay the cost of [context switching](context_switch_(cpu).md) to the thread just to hand back control to the [CPU](central_processing_unit_(cpu).md).

