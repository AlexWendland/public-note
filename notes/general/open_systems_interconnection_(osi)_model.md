---
aliases:
  - OSI
  - OSI model
checked: false
created: 2024-05-21
draft: false
last_edited: 2024-05-21
title: Open Systems interconnection (OSI) model
tags:
  - networks
type: definition
---
>[!tldr] Open Systems interconnection (OSI) model
>The OSI model was presented by the [International Organisation for Standardisation (ISO)](international_organisation_for_standardisation_(iso).md) for how networks should be structured. Its ultimate goal is to gaurentee safe communication between two hosts that may or may not be on the same [network](network.md). It has 7 layers each with a different responsibility.
>1. [Physical layer](layer_1_physical.md),
>2. [Data Link layer](layer_2_data_link.md),
>3. [Network layer](layer_3_network.md),
>4. [Transport layer](layer_4_transport.md),
>5. [Session layer](layer_5_session.md),
>6. [Presentation layer](layer_6_presentation.md), and
>7. [Application layer](layer_7_application.md)
>
>This separation allows for scalability, molecularity and flexibility to add or remove components. Though comes with some down sides such as
>- Some layers' functionality depends on the information from other layers, which can violate the goal of layer separation.
>- One layer may duplicate lower-layer functionalities. For example, the functionality of error recovery can occur in lower layers but also in upper layers as well.
>- Some additional overhead that is caused by the abstraction between layers.

