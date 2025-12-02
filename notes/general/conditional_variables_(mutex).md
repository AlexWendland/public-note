---
aliases:
  - conditional variables
  - Conditional variables
checked: false
created: 2024-09-04
draft: false
last_edited: 2024-09-04
title: Conditional variables (Mutex)
tags:
  - OS
type: definition
---
>[!tldr] Conditional variables (Mutex)
> A [mutex](mutex.md) may need special operations applied upon some condition being met. (For example processing a list when it is full.) To implement this we use [data structure](data_structure.md) called conditional variable that holds at least:
> - A reference to the [mutex](mutex.md) it is related to, and
> - A list of waiting [threads](thread.md).
>
> Then an [OS](operating_system_(os).md) will offer 3 calls on the [API](application_programming_interface_(api).md):
> - wait(*mutex*, *condition*): [mutex](mutex.md) is released and reacquired when the condition is met (i.e. they are notified about the condition).
> - signal(*condition*): notify a single [thread](thread.md) waiting on the condition it has been met.
> - broadcast(*condition*): notify all [threads](thread.md) waiting on the condition. (Though as they are all waiting on the [mutex](mutex.md) they only activate one at a time.)
