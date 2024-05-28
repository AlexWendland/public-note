---
aliases: 
checked: false
created: 2024-05-28
last_edited: 2024-05-28
publish: true
tags:
  - networks
type: explainer
---
# Congestion control in [[Transmission Control Protocol (TCP)|TCP]]

Congestion control is use to utilise the network with the following goals in mind:
- Efficiency: We should try to have high utilisation of the network at all times.
- Fairness: Each user should have a fair share of the network.
- Low delay: We should not overwhelm the switches and routers buffers causing a large delay within the network.
- Fast convergence: We want to get to a stable point that achieves all the above quickly.

