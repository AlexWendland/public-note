---
aliases:
created: 2025-04-09
date_checked: 2026-01-29
draft: false
last_edited: 2025-04-09
tags:
  - OS
title: Pseudo devices
type: definition
---
>[!tldr] Pseudo devices
>Pseudo devices are not backed by real hardware but offer virtual interfaces to the [OS](operating_system_(os).md). They provide functionality that is useful for testing, debugging and interacting with the [OS](operating_system_(os).md). Examples of some devices in Linux are:
>- `/dev/null`: All written data here is discarded.
>- `/dev/zero`: Provides an infinite stream of zero-values when read.
>- `/dev/random`: Generates cryptographically secure random data.
>- `/dev/urandom`: Generates non-blocking random data.
>- `/dev/full`: Simulates a full disk and generates an error when written to.
