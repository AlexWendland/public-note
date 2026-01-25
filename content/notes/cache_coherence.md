---
aliases:
  - cache coherent
  - cache coherence
created: 2025-04-08
date_checked:
draft: false
last_edited: 2025-04-08
tags:
  - OS
title: Cache coherence
type: definition
---
>[!tldr] Cache coherence
>*Cache coherence* refers to the process of keeping multiple cached copies of the same memory location consistent across different caches. This is especially important in multi-core processors, where each CPU core may have its own cache.
>
>There are two primary strategies for maintaining coherence:
>
>- **Write-invalidate**: When a core writes to a cached value, it **invalidates** that value in all other caches. Other cores must fetch the updated value from memory (or the writing core) on their next access. _This is a lazy strategy — it saves bandwidth but may cause a delay on future reads._
>- **Write-update**: When a core writes to a cached value, it **broadcasts** the update to all other caches so they can update their copies immediately. _This is an eager strategy — it keeps all caches ready, but increases communication cost._

