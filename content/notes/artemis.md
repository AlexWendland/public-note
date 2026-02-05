---
aliases:
created: 2024-07-21
date_checked:
draft: false
last_edited: 2026-02-05
tags:
  - networks
  - security
title: ARTEMIS
type: definition
---
>[!definition] ARTEMIS
>ARTEMIS is a system designed to detect and mitigate [BGP Hijacking](bgp_hijacking.md), operated locally by network operators to protect their own prefixes. The system is based on several key ideas and [can be found in this paper](https://www.inspire.edu.gr/wp-content/pdfs/artemis_TON2018.pdf).
>
>This works in the following way.
>1. **Write a configuration File**: Lists all prefixes owned by the network, created by the network operator.
>2. **BGP Updates Mechanism**: Receives updates from local routers and monitoring services.
>3. **Anomaly Detection**: Compares received [BGP](border_gateway_protocol_(bgp).md) updates against the configuration file to detect anomalies in prefixes and AS-PATH fields.
>
>ARTEMIS can detect different types of BGP prefix hijacking attacks by monitoring for unusual patterns in BGP announcements.
>
>![Artemis Table](../../static/images/ARTEMIS_table.png)
>
>The system aims to minimise [false positives](result_types.md) and [false negatives](result_types.md). Operators can prioritise between accuracy and speed or opt for fewer inconsequential FNs at the cost of higher FPs.
>
>This is achieved by
>1. **Prefix Deaggregation**: The affected network announces more specific prefixes to counteract hijacked prefixes. For example, if a prefix 208.65.153.0/24 is hijacked, the network could announce 208.65.153.128/25 and 208.65.153.0/25.
>2. **Multiple Origin AS (MOAS)**: Third-party organisations announce the hijacked prefixes from their locations. This attracts global traffic to the third party, which scrubs it and tunnels it back to the legitimate AS.


