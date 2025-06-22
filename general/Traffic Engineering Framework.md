---
aliases: 
checked: false
created: 2024-06-08
last_edited: 2024-06-08
draft: false
tags:
  - networks
type: definition
---
>[!tldr] Traffic Engineering Framework
> This framework can help network operators decide distances between [[Router|routers]] within an [[Autonomous system (AS)|autonomous system]] for [[Intradomain routing|intradomain routing]]. This uses the following steps
> 1. **Measure**: Observe how the network flow is happening at the moment. This involves looking at the current set of shortest paths and the capacity of each of the links. 
> 2. **Model**: Predict how a change in weights would effect the these paths and capacities on the wires.
> 3. **Control**: Update the weights of the routers and go back to the first step to check your model was correct.