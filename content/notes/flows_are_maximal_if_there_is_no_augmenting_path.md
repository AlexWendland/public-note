---
aliases:
created: 2023-10-03
date_checked:
draft: false
last_edited: 2023-11-11
tags:
  - maths
title: Flows are maximal if there is no augmenting path
type: lemma
---
# Statement

>[!important] Lemma
>Given a [flow network](flow_network.md) $(G, c, s, t)$ a [flow](flow.md) $f$ is maximal if there is no [path](path_(graph).md) from $s$ to $t$ in the [residual network](residual_network_(flow).md) $(G^f, c^f, s, t)$.
>

# Proof

This follows from the proof of the [Max-flow min-cut Theorem](max-flow_min-cut_theorem.md).

In particularly [Claim 2](max-flow_min-cut_theorem.md#claim-2) in the proof of the main result gives us that value of $f$ is the capacity of some [st-cut](st-cut.md). With the corollary of [Claim 1](max-flow_min-cut_theorem.md#claim-1) being that for these to be equal they must be maximal/minimal in their own respects.
