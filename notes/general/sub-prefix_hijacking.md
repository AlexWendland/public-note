---
aliases:
checked: false
created: 2024-07-21
draft: false
last_edited: 2024-07-21
name: Sub-prefix hijacking
tags:
  - networks
  - security
type: definition
---
>[!tldr] Sub-prefix hijacking
>This is a form of [BGP Hijacking](bgp_hijacking.md) where the attacking [AS](autonomous_system_(as).md) announces a sub-path for a prefix a genuine [AS](autonomous_system_(as).md) announced. This will be preferentially used as it is a more precise prefix. This disrupts the flow of traffic to the intended [AS](autonomous_system_(as).md).

