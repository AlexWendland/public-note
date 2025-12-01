---
aliases:
  - count to infinity problem
  - poison reverse
checked: false
created: 2024-06-04
draft: false
last_edited: 2024-06-04
name: Count to infinity problem
tags:
  - networks
type: explainer
---
# Count to infinity problem

This is a problem within the [Distance vector routing algorithms](distance_vector_routing_algorithms.md) caused by a change in the underlying graph or its distances. This causes very slow convergence to the correct intradomain distances as nodes all believe sending messages to one another using the old distances is the shortest path.

## Example

Suppose we have an [AS](autonomous_system_(as).md) with 3 routers $\{x,y,z\}$ which are all connected to one another with initial distances $d(z,x) = d(x,y) = 1$ and $d(y,z) = 10$ then we have the following shortest path tables.

| D(r,c) | x   | y   | z   |
| ------ | --- | --- | --- |
| x      | 0   | 1   | 1   |
| y      | 1   | 0   | 2   |
| z      | 1   | 2   | 0   |

The suppose the edge $(x,z)$ breaks. If the [Distance vector routing algorithms](distance_vector_routing_algorithms.md) don't take this problem into account then we get a slow escalation of distance.

Router $x$ requests its neighbour $y$ distances it updates $D(x,z) = 1 + 2 =3$ and broadcasts this. Then $y$ updates its distances $D(y,z) = 3 + 1 = 4$ and broadcasts this. Then the problem goes on.

## Avoidance

To get around this we track who we are planning on sending the update two to achieve the current minimum distance. If that is the same as the person we broadcast to then we set that distance to infinity. This method is called Poison reverse.

Whilst this solves the simple cases like above - it is easy to imagine chains for [routers](router.md) having this exact problem without being able to realise it.
