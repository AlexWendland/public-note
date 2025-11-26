---
aliases: 
checked: false
created: 2024-07-23
last_edited: 2024-07-23
draft: false
tags:
  - networks
  - security
type: definition
---
>[!tldr] Iris
>This is a system that detects [[DNS censorship]]. It does this by comparing the responses of open [[Domain Name System (DNS)|DNS]] resolvers on the internet. This is done in a multi-step process as shown below.
>![Iris Methodology](../images/iris_methodology.png)
>This first looks for open [[Domain Name System (DNS)|DNS]] resolvers that are part of the internet infrastructure (i.e. not home routers that are sometimes open due to misconfiguration).
>1. Scan [[Internet Protocol (IPv4)|IPv4]] space for open resolvers.
>2. Identify infrastructure [[Domain Name System (DNS)|DNS]] resolvers.
>
>Then we query them all for the same set of domains and compare the responses.
>
>3. Perform global [[Domain Name System (DNS)|DNS]] queries - establish a based line using 3 of them within the control of the Iris team.
>4. Annotate [[Domain Name System (DNS)|DNS]] responses with auxiliary information to assist classification.
>5. Additional [[DNS records|PTR]] and [[Transport Layer Security (TLS)|TLS]] scanning - this is to allow inconsistencies due to virtual hosting to be resolved. 
>
> After the dataset is gathered we then calculate two types of metrics:
> - **Consistency metrics**: Checking if the same look up in different locations provides different responses for [[Internet Protocol (IP)|IP address]], [[Autonomous system (AS)|AS]], [[Hyper Text Transfer Protocol (HTTP)|HTTP]] content, ect.
> - **Independent verifiable metrics**: These are metrics that use other datasets to verify they are correct such as [[Hypertext Transfer Protocol Secure (HTTPS)|HTTPS]] certificates. 
> 
> If both of these metrics are satisfied then the response is considered correct otherwise it is labelled as incorrect.