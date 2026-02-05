---
aliases:
  - Dynamic Adaptive Streaming over HTTP
  - DASH
created: 2024-07-27
date_checked: 2026-02-05
draft: false
last_edited: 2024-07-27
tags:
  - networks
title: Dynamic Adaptive Streaming over HTTP (DASH)
type: definition
---
> [!tldr] Dynamic Adaptive Streaming over HTTP (DASH)
> This is a technique to implement [bitrate adaption](bitrate_adaptation.md). This has multiple implementations such as [HTTP Live Streaming (HLS)](http_live_streaming_(hls).md) or [MPEG-DASH](mpeg-dash.md). These implementations differ in detail such as the encoding algorithms, segment sizes, DRM support, bitrate adaptation algorithms, etc.
>
> Here videos are cut into chunks and each chunk is encoded at different [bitrates](bitrate.md). Each time a video chunk is downloaded it calls the [bitrate adaption](bitrate_adaptation.md) function $f$ to determine the [bitrate](bitrate.md).
>
>![Dash Function](../../static/images/DASH_function.png)
>
>Where $\{R_1, R_2, \ldots, R_m\}$ is the set of [bitrates](bitrate.md).

