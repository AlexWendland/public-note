---
aliases: 
checked: false
course: "[[CS6250 Computer Networks]]"
created: 2024-07-21
last_edited: 2024-07-21
publish: true
tags:
  - OMSCS
type: lecture
week: 8
---
# Week 8 - Security

The Internet was not designed or built with security in mind. Security came as an afterthought after adversaries started misusing or abusing Internet services, resources and infrastructure.

An attack on a system aims to compromise properties of a secure communication.

## Additional reading

### Important Readings

Measuring and Detecting Fast-Flux Service Networks  
[https://www.sec.tu-bs.de/pubs/2008-ndss.pdfLinks to an external site.](https://www.sec.tu-bs.de/pubs/2008-ndss.pdf)

FIRE: FInding Rogue nEtworks  
[https://sites.cs.ucsb.edu/~chris/research/doc/acsac09_fire.pdfLinks to an external site.](https://sites.cs.ucsb.edu/~chris/research/doc/acsac09_fire.pdf)

ASwatch: An AS Reputation System to Expose Bulletproof Hosting ASes  
_[Links to an external site.](https://conferences.sigcomm.org/sigcomm/2015/pdf/papers/p625.pdf)_[https://conferences.sigcomm.org/sigcomm/2015/pdf/papers/p625.pdfLinks to an external site.](https://conferences.sigcomm.org/sigcomm/2015/pdf/papers/p625.pdf)

Cloudy with a Chance of Breach: Forecasting Cyber Security Incident  
[https://www.usenix.org/system/files/conference/usenixsecurity15/sec15-paper-liu.pdfLinks to an external site.](https://www.usenix.org/system/files/conference/usenixsecurity15/sec15-paper-liu.pdf)

ARTEMIS: Neutralizing BGP Hijacking Within a Minute  
[https://www.inspire.edu.gr/wp-content/pdfs/artemis_TON2018.pdfLinks to an external site.](https://www.inspire.edu.gr/wp-content/pdfs/artemis_TON2018.pdf)

BGP Anomaly Detection Techniques: A Survey  
[https://www.researchgate.net/profile/Bahaa_Musawi/publication/309519246_BGP_Anomaly_Detection_Techniques_A_Survey/links/5a63db73aca272a1581bf3ea/BGP-Anomaly-Detection-Techniques-A-Survey.pdfLinks to an external site.](https://www.researchgate.net/profile/Bahaa_Musawi/publication/309519246_BGP_Anomaly_Detection_Techniques_A_Survey/links/5a63db73aca272a1581bf3ea/BGP-Anomaly-Detection-Techniques-A-Survey.pdf)

A Forensic Case Study on AS Hijacking: The Attacker’s Perspective  
[http://www.sigcomm.org/sites/default/files/ccr/papers/2013/April/2479957-2479959.pdfLinks to an external site.](http://www.sigcomm.org/sites/default/files/ccr/papers/2013/April/2479957-2479959.pdf)

An Analysis of Using Reflectors for Distributed Denial-of-Service Attacks  
[https://www.engineering.iastate.edu/~daniels/cpre592TD/readings/Anonymity_and_Concealment/paxson01analysis.pdfLinks to an external site.](https://www.engineering.iastate.edu/~daniels/cpre592TD/readings/Anonymity_and_Concealment/paxson01analysis.pdf)

Stellar: Network Attack Mitigation using Advanced Blackholing  
[https://dl.acm.org/doi/10.1145/3281411.3281413Links to an external site.](https://dl.acm.org/doi/10.1145/3281411.3281413)

Inferring BGP Blackholing Activity in the Internet  
[https://dl.acm.org/doi/10.1145/3131365.3131379Links to an external site.](https://dl.acm.org/doi/10.1145/3131365.3131379)

Next Gen Blackholing to Counter DDoS  
[https://ripe78.ripe.net/presentations/9-RIPE_Presentation_MW.pdfLinks to an external site.](https://ripe78.ripe.net/presentations/9-RIPE_Presentation_MW.pdf "Link")

### Book References

Kurose-Ross Edition 6th, Section 8.1

## Secure communications

There a 4 properties of secure communication:
- **Confidentiality**: The message can only be read by the person who was the intended recipient of the message.
- **Integrity**: The message was received as intended and has not been manipulated. 
- **Authentication**: The person who you are talking to is who you think they are.
- **Availability**: You can communicate when you need to through this channel.

## DNS abuse

Attackers have developed techniques abusing the DNS protocol to extend the uptime of domains that are used for malicious purposes (e.g., Command and Control hosting infrastructure, phishing, spamming domains, hosting illegal businesses, and illegal content). The ultimate goal of this abuse is to remain undetectable for longer.

These techniques have their roots in legitimate DNS-based techniques that legitimate businesses and administrators use.

![[Round robin DNS (RRDNS)]]

![[DSN-based content delivery]]

![[Fast-Flux Service Networks (FFSN)]]

## Rouge network detection

There are different approaches to detecting rouge networks. The most intuitive method is to see if they are hosting bad actors.

![[Finding rouge networks (FIRE)]]

The approach has a couple downsides:
- It is infeasible to monitor all networks all the time.
- It takes a long time for malicious IPs to get on the back list.
- This struggles to distinguish between bad networks and networks that are curntly being misused but are not themselves bad (such as a service that hosts websites for other people).

We could instead look at the network topology of the system to see if it is behaving like a bad actor.

![[ASwatch]]

Lastly we can instead of looking at if a network is behaving badly work out if the network is likely to be breached or to have been breached. This allows us to know if we can trust that network even if it is operated with good intentions.

This system predicts the likelihood of a security breach within an organisation using externally observable features. It uses these features to train a [[Random forest]] model, making it callable to all organizations. The features fall into three main categories:

1. **Mismanagement Symptoms**:
    - **Open Recursive Resolvers**: Misconfigured [[Domain Name System (DNS)|DNS]] resolvers that can be exploited.
    - **DNS Source Port Randomization**: Servers lacking this feature are more vulnerable.
    - **BGP Misconfiguration**: Short-lived routes indicating routing issues.
    - **Untrusted HTTPS Certificates**: Detection of invalid certificates via TLS handshake.
    - **Open SMTP Mail Relays**: Servers improperly configured to filter mail, increasing risk.
2. **Malicious Activities**:
    - **Spam Activity**: IP addresses involved in spam, identified by services like CBL and SpamCop.
    - **Phishing and Malware**: Detection of phishing and malware sources via platforms like PhishTank.
    - **Scanning Activity**: IP addresses involved in scanning detected by monitors like Dshield.
3. **Security Incident Reports**:
    - **VERIS Community Database**: A collection of over 5000 cybersecurity incidents.
    - **Hackmageddon**: Aggregates monthly security incidents.
    - **Web Hacking Incidents Database**: Repository of cyber security incidents.

### Model and Evaluation:

- **Random Forest Classifier**: Trained using 258 features, including the ones described above, along with statistical secondary features and organization size.
- **Baseline Comparison**: Compared against a [[Support vector machines (SVM)]].
- **Output**: The model provides a risk probability which, when thresholded, gives a binary class label indicating breach likelihood.
- **Data Handling**: Training-testing splits are time-based to ensure sequential data integrity.
- **Accuracy**: The model achieves an accuracy of 90% with the optimal parameters.

This system effectively uses external indicators of mismanagement, malicious activity, and past incidents to predict the probability of future breaches in an organization's network.

