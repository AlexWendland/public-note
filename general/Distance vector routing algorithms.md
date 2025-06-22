---
aliases:
  - DV
checked: false
created: 2024-06-02
last_edited: 2024-06-02
draft: false
tags:
  - networks
type: definition
---
>[!tldr] Distance vector routing algorithms
>Distance vector routing is a distributed [[Routing|routing]] algorithm. It uses the [[Bellman-Ford algorithm]] but in a distributed manner. 
>
>For this was assume all [[Router|routers]] know the routers they are directly connected to - within a [[Network|network]] they have an interface to. They also know the network cost of communicating with their neighbours. 
>
>Each [[Router|router]] maintains a table with all routers within their [[Autonomous system (AS)|AS]] to each they associate, that routers best guess at the distance to the router, and which neighbour router they need to send any [[Packets|packets]] to to achieve that best guess.
>
>Then all the routers broadcast this information to its neighbours and use their neighbours broadcasts to update their own tables. They update their tables using the [[Bellman-Ford algorithm|Bellman-Ford equation]]. 
>
>This has a [[Count to infinity problem]] where if the distance of a connection is increased dramatically or it is removed then two neighbours might keep thinking the fastest rout is via one another as there distances and dependent on that edge not being changed. This causes a very slow convergence to the real path. We can improve the algorithm to account for this however this algorithm will still be vulnerable to this with large graphs.
> 
>This has the pseudocode as below.

## Pseudocode

Let us have an [[Autonomous system (AS)|AS]] which is represented by an [[Graph|undirected graph]] $(V, E)$ where each of $v \in V$ are routers and an edge indicates they have a common network that belongs to their interfaces. Suppose this has a distance metric associated to it $d: E \rightarrow \mathbb{R}_{\geq 0}$. Then we describe an algorithm for a particular vertex $x \in V$ who has neighbours $N_{x}$. This will build two maps - $D: V \rightarrow \mathbb{R} \cup \{\inf\}$ current best guess of the shortest distance and $S: V \rightarrow N_x \cup \{-\}$  

```pseudocode

-- Initalisation
Set map D(v) = inf, S(y) = - for all v in V.
Set D(x) = 0
Set D(n) = d(x,n), S(n) = n for n in N_x
Send D to all members of N_x.

-- Recieve a message
Suppose we get D' from y in N_x
For every v in V where S(v) = y:
	# Can not use min here incase the distance has increased due 
	# to network changes
	Set D(v) = d(x,y) + D'(v)
For every v in V where S(v) /= y:
	Set D(v) = min(D(v), d(x,y) + D'(v))
	Update S(v) = y if D(v) decreased

If any value of D changes:
	# Handle to count to infinity problem
	For each n in N_x:
		Let D' be a copy of D
		For each v in V where S(v) = n:
			Set D'(v) = inf
		Send D' to n
```

