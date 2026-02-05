---
aliases:
  - ACL
  - access control list
created: 2024-07-21
date_checked:
draft: false
last_edited: 2026-02-05
tags:
  - networks
  - security
title: Access control list (ACL) filters
type: definition
---
>[!definition] Access control list (ACL) filters
>Access Control List filters are deployed by [ISPs](internet_service_provider_(isp).md) or [IXPs](internet_exchange_points_(ixps).md) at their [AS](autonomous_system_(as).md) border routers to filter out unwanted traffic. These filters, whose implementation depends on vendor-specific hardware, are effective when the hardware is homogeneous, and the deployment of the filters can be automated. The drawbacks of these filters include limited scalability, and since the filtering does not occur at the ingress points, it can exhaust the bandwidth to a neighbouring AS.

