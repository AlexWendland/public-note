---
aliases:
checked: false
created: 2025-04-09
draft: false
last_edited: 2025-04-09
title: Pseudo devices
tags:
  - OS
type: definition
---
>[!tldr] Pseudo devices
>Pseudo devices are not back by real hardware however offer virtual interfaces to the [OS](operating_system_(os).md). They offer functionality that is useful for testing, debugging and interacting with the [OS](operating_system_(os).md). Examples of some devices in linux are:
>- `/dev/null`: All written data here is discarded.
>- `/dev/zero`: Provided an infinite stream of zero-values when read.
>- `/dev/random`: Generates a cryptographically secure random data.
>- `/dev/urandom`: Generates non-blocking random data.
>- `/dev/full`: Simulates a full disk generating an error when getting written to.

