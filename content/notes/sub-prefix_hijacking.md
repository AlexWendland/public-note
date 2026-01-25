---
aliases:
created: 2024-07-21
date_checked:
draft: false
last_edited: 2024-07-21
tags:
  - networks
  - security
title: Sub-prefix hijacking
type: definition
---
>[!tldr] Sub-prefix hijacking
>This is a form of [BGP Hijacking](bgp_hijacking.md) where the attacking [AS](autonomous_system_(as).md) announces a sub-path for a prefix a genuine [AS](autonomous_system_(as).md) announced. This will be preferentially used as it is a more precise prefix. This disrupts the flow of traffic to the intended [AS](autonomous_system_(as).md).

