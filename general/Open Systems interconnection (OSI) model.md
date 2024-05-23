---
aliases:
  - OSI
  - OSI model
checked: false
created: 2024-05-21
last_edited: 2024-05-21
publish: true
tags:
  - networks
type: definition
---
>[!tldr] Open Systems interconnection (OSI) model
>The OSI model was presented by the [[International Organisation for Standardisation (ISO)]] for how networks should be structured. Its ultimate goal is to gaurentee safe communication between two hosts that may or may not be on the same [[Network|network]]. It has 7 layers each with a different responsibility.
>1. [[Layer 1 Physical|Physical layer]],
>2. [[Layer 2 Data Link|Data Link layer]],
>3. [[Layer 3 Network|Network layer]],
>4. [[Layer 4 Transport|Transport layer]],
>5. [[Layer 5 Session|Session layer]],
>6. [[Layer 6 Presentation|Presentation layer]], and
>7. [[Layer 7 Application|Application layer]]
>
>This separation allows for scalability, molecularity and flexibility to add or remove components. Though comes with some down sides such as
>- Some layers' functionality depends on the information from other layers, which can violate the goal of layer separation.
>- One layer may duplicate lower-layer functionalities. For example, the functionality of error recovery can occur in lower layers but also in upper layers as well. 
>- Some additional overhead that is caused by the abstraction between layers.

