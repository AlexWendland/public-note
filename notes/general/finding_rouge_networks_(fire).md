---
aliases:
checked: false
created: 2024-07-21
draft: false
last_edited: 2024-07-21
name: Finding rouge networks (FIRE)
tags:
  - networks
type: definition
---
>[!tldr] Finding rouge networks (FIRE)
>The FIRE (FInding Rogue nEtworks) system is designed to monitor the Internet for rogue networks—networks primarily used for malicious activities such as phishing, hosting spam pages, and distributing pirated software. It utilises three main data sources to identify potential rogue networks:
>
>1. **Botnet Command and Control Providers**:
 >   - Monitors networks hosting command and control (C&C) servers for botnets, focusing on [IRC](internet_relay_chat_protocol_(irc).md)-based and [HTTP](hyper_text_transfer_protocol_(http).md)-based botnets.
>    - These networks are chosen by bot-masters to avoid take-down.
>2. **Drive-by-Download Hosting Providers**:
>   - Detects networks hosting web pages that exploit browser vulnerabilities to install malware without user interaction.
>3. **Phish Housing Providers**:
 >   - Tracks URLs of servers hosting phishing pages that mimic legitimate sites to steal sensitive information. These pages are usually short-lived and hosted on compromised servers.
>
>The key difference between rogue and legitimate networks is the duration of malicious activity. Legitimate networks typically remove harmful content quickly, while rogue networks may host malicious content for extended periods. By ignoring IP addresses active for only a short time, the system filters out temporary abuses on legitimate networks.
>
>FIRE aggregates daily lists of malicious IP addresses from these data sources and analyzes them to identify rogue [Autonomous system (AS)](autonomous_system_(as).md). It does this by comparing the ratio of malicious IP addresses to the total number of IP addresses owned by each AS, highlighting the most malicious networks.

