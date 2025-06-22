---
aliases:
  - EvoArch
  - Evolutionary Architecture model
checked: false
created: 2024-05-23
last_edited: 2024-05-23
draft: false
tags:
  - networks
type: definition
---
>[!tldr] Evolutionary Architecture model (EvoArch)
> This is a model built to explain the [[Internet protocol stack hourglass shape]]. It builds a [[Directed acyclic graph (DAG)|DAG]] in discrete time steps $G_i = (V_i,E_i)$ over time $i \in \mathbb{N}$ to model the [[Protocol (networks)|protocols]] in the [[Open Systems interconnection (OSI) model|OSI model]].
> - Define a set of layers $L$,
> - Each vertex $v \in V_i$ gets mapped to a layer $l(v) \in L$,
> - Each edge $(u,v) \in E_i$ has $l(v) = l(u) +1$ and describes the relationship protocol $v$ can use protocol $u$ as its lower level protocol.
> - We define the set of parents of a node $S_i(v) = \{u \in V_i \vert (u,v) \in E_i\}$ to be substrates.
> - The children of node $P_i(u) = \{v \in V_i \vert (u,v) \in E_i\}$ we define to be its Product.
> - Each layer $l \in L$ has a generality probability associated to it, $s(l) \in [0,1]$. This determine the probability a higher level protocol will depend on a new protocol in this layer in the future. For each $v \in V_i$ where $l(v) > 1$ for each $u \in V_i \backslash V_{i+1}$ where $l(u) = l(v) +1$ then $(u,v) \in E_i$ with probability $s(l)$.
> - Each node $v \in V$ has a value at time $i$, $v_i(v)$, this is defined by the product of that node i.e. $v_i(v) = f(P_i(v))$.
> - There is a competitor threshold $c \in [0,1]$ that defines to competitors for nodes 
> $$C_i(v) = \{u \in V_i \vert l(u) = l(v) \ \land \ \frac{\vert P(v) \cap P(u)\vert}{\vert P(u) \vert} > 1\}.$$
> - Nodes die if their competitors have too much value. This also kills upstream nodes if they only depended on that node for its layer. 
> - Nodes also get added randomly to the graph as a percentage of the total size of the current network. Though this can very depending on the implementation
> 
> To update this model we do the following steps.
> 1. Introduce new nodes to the model.
> 2. Going from top to bottom carry out the following for each layer
> 	1. Add new edges for new nodes.
> 	2. Calculate new values for the nodes.
> 	3. Examine nodes in decreasing value order and remove if needed.
> 3. Stop if we reach a predetermined number of nodes.
