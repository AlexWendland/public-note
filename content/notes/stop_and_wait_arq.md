---
aliases:
created: 2024-05-27
date_checked:
draft: false
last_edited: 2024-05-27
tags:
  - networks
title: Stop and wait ARQ
type: definition
---
>[!tldr] Stop and wait ARQ
>This is an implementation of [ARQ](automatic_repeat_request_(arq).md) that sends some messages and wait for an acknowledgement before sending more. It uses a window size determined by the [Transmission control in TCP](transmission_control_in_tcp.md). It will only send the window size worth of unacknowledged message before stopping to wait for a new acknowledgement message or the timeout window to be exceeded.


