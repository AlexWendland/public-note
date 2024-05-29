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

There are two approaches when it comes to congestion control. 
- Network assisted: You rely on the network to provide some signal about how congested it is. This could be done via:
	- ICMP source quench.
- End-to-end congestion control: Hosts need to infer congestion from the traffic they receive. This can use different signal such as:
	- Packet delay based on acknowledgement times.
	- Packet loss using some level of timeout when waiting for acknowledgements 

[[Transmission Control Protocol (TCP)|TCP]] uses the end-to-end approach. It mainly uses packet loss to detect congestion as packet delay can have quite a bit of noise in the system.

[[Transmission Control Protocol (TCP)|TCP]] uses ACK messages as a probes and adopts a probe-and-adapt approach to adjusting the window size (number of unacknowledged packets) for congestion control. 

