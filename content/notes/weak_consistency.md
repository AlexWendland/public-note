---
aliases:
created: 2025-04-13
date_checked: 2026-01-29
draft: false
last_edited: 2025-04-13
tags:
  - OS
title: Weak consistency
type: definition
---
>[!definition] Weak consistency
>Weak consistency is a [consistency model](consistency_model.md) that introduces a new operation: synchronise. The model only guarantees that all operations performed before a synchronisation point will be visible to processes that call synchronise afterwards. There are variations of this:
>- Single sync (like above).
>- Separate sync per subset of state (e.g. page)
>- Separate entry/acquire vs exit/release operations.

