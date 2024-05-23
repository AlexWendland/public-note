---
aliases: 
checked: false
created: 2024-05-23
last_edited: 2024-05-23
publish: true
tags:
  - networks
type: explainer
---
# Connection between [[Open Systems interconnection (OSI) model|OSI]] and [[Internet Protocol Stack (IPS) 5 layers|IPS]] models

The [[Open Systems interconnection (OSI) model|OSI model]] was originally invented when the main computers where main frames. Making [[Layer 5 Session|layer 5]] more important however in modern applications the roles and responsibilities of the last 3 layers in the [[Open Systems interconnection (OSI) model|OSI]] get very mixed and end up being combined into one in other. Some applications might not implement some of them.

For example [[Hyper Text Transfer Protocol (HTTP)|HTTP]] uses [[Cookies (web)|cookies]] for [[Layer 5 Session|layer 5]], extended [[American Standard Code for Information Interchange (ASCII)|ASCII]] for [[Layer 6 Presentation|layer 6]], and keywords for [[Layer 7 Application|layer 7]]. Whereas FTP doesn't have a way to implement [[Layer 5 Session|layer 5]], uses the same extended [[American Standard Code for Information Interchange (ASCII)|ASCII]] for [[Layer 6 Presentation|layer 6]] but different commands for [[Layer 7 Application|layer 7]].

This mix of these layers is normally dependent on the protocol - so normally rolled up into one thing.


![[model-comparison.png]]
