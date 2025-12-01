---
aliases:
  - concurrency
  - concurrently
checked: false
created: 2024-09-04
draft: false
last_edited: 2024-09-04
tags:
  - OS
  - computer-science
type: definition
---
>[!tldr] Concurrency
> This is a technique to handle large tasks that require waiting on different resources outside the control of the executor. This means starting lots of different tasks and switching to a different task whenever you are blocked from progressing on your current task. A common technique here is [[Asynchronous programming|asynchronous programming]] or [[Multi-threading|multi-threading]] using a single kernel [[Thread|thread]].

