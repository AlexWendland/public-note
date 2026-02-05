---
aliases:
  - concurrency
  - concurrently
created: 2024-09-04
date_checked: 2026-02-05
draft: false
last_edited: 2024-09-04
tags:
  - OS
  - computer-science
title: Concurrency
type: definition
---
>[!note] Concurrency
> This is a technique to handle large tasks that require waiting on different resources outside the control of the executor. This means starting lots of different tasks and switching to a different task whenever you are blocked from progressing on your current task. A common technique here is [asynchronous programming](asynchronous_programming.md) or [multi-threading](multi-threading.md) using a single kernel [thread](thread.md).

