---
aliases: 
checked: false
created: 2024-05-29
last_edited: 2024-05-29
draft: false
tags:
  - networks
type: definition
---
>[!tldr] TCP Reno
>This is the classical [[Congestion control in TCP]]. It starts the window size to be 1 packets big. It uses [[Additive increase Multiplicative Decrease (AIMD)|AIMD]] with two different signals.
>- If a message is waited on 3 times, it halves the congestion window in [[Additive increase Multiplicative Decrease (AIMD)|AIMD]].
>- If it reaches a timeout window (i.e. no message is received for a given length of time). It resets the congestion window back to 1.
>
>This however is quite slow to start. Therefore Reno implements "slow start" doubling up to some threshold. This means that while the congestion window is below the that threshold every [[Round trip time (RTT)|RTT]] it doubles the congestion window. Once it passes this threshold or it drops a packet it switchest back to [[Additive increase Multiplicative Decrease (AIMD)|AIMD]]
>The "slow start" also takes place if we have a timeout. In this case the threshold is set to be the congestion window before the timeout.  



