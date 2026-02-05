---
aliases:
created: 2024-06-08
date_checked: 2026-02-05
draft: false
last_edited: 2026-02-05
tags:
  - networks
title: Traffic Engineering Framework
type: definition
---
>[!definition] Traffic Engineering Framework
> This framework can help network operators decide distances between [routers](router.md) within an [autonomous system](autonomous_system_(as).md) for [intradomain routing](intradomain_routing.md). This uses the following steps:
> 1. **Measure**: Observe how the network flow is happening at the moment. This involves looking at the current set of shortest paths and the capacity of each of the links.
> 2. **Model**: Predict how a change in weights would affect these paths and capacities on the links.
> 3. **Control**: Update the link weights and go back to the first step to check your model was correct.
