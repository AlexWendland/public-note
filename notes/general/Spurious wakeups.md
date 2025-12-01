---
aliases:
  - spurious wakeups
checked: false
created: 2024-09-05
draft: false
last_edited: 2024-09-05
tags:
  - OS
type: definition
---
>[!tldr] Spurious wakeups
>When waking up [[Thread|threads]] in a [[Mutex|mutex]] block using signal/broadcast lf you still hold the mutex then the threads will just be moved to waiting on the mutex as it is still held. This is a *spurious wakeup* as we pay the cost of  [[Context switch (CPU)|context switching]] to the thread just to hand back control to the [[Central processing unit (CPU)|CPU]].

