---
aliases:
  - ACL
  - access control list
checked: false
created: 2024-07-21
draft: false
last_edited: 2024-07-21
tags:
  - networks
  - security
type: definition
---
>[!tldr] Access control list (ACL) filters
>Access Control List filters are deployed by [[Internet Service Provider (ISP)|ISPs]] or [[Internet Exchange Points (IXPs)|IXPs]] at their [[Autonomous system (AS)|AS]] border routers to filter out unwanted traffic. These filters, whose implementation depends on vendor-specific hardware, are effective when the hardware is homogeneous, and the deployment of the filters can be automated. The drawbacks of these filters include limited scalability, and since the filtering does not occur at the ingress points, it can exhaust the bandwidth to a neighbouring AS.

