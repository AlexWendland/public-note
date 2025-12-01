---
aliases:
checked: false
created: 2023-10-03
draft: false
last_edited: 2023-11-11
tags:
  - maths
type: lemma
---
# Statement

>[!important] Lemma
>Given a [[Flow network|flow network]] $(G, c, s, t)$ a [[Flow|flow]] $f$ is maximal if there is no [[Path (graph)|path]] from $s$ to $t$ in the [[Residual Network (flow)|residual network]] $(G^f, c^f, s, t)$.
>

# Proof

This follows from the proof of the [[Max-flow min-cut Theorem]].

In particularly [[Max-flow min-cut Theorem#Claim 2|Claim 2]] in the proof of the main result gives us that value of $f$ is the capacity of some [[st-cut]]. With the corollary of [[Max-flow min-cut Theorem#Claim 1|Claim 1]] being that for these to be equal they must be maximal/minimal in their own respects.
