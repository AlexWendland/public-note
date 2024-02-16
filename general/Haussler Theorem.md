---
aliases: 
checked: false
created: 2024-02-16
last_edited: 2024-02-16
publish: true
tags:
  - machine-learning
type: lemma
---
# Statement

> [!important] Haussler Theorem
> Suppose we are in the [[Modelling framework|modelling framework]] with finite [[Modelling paradigm|hypothesis space]] $H$ and [[Probability distribution|probability distribution]] $\mathbb{D}$ on $A$. Set $0 \leq \epsilon \leq 1$. Let our [[Training data|training data]] $T$ be $m$ [[Independent identically distributed samples|i.i.d.]] samples from $\mathbb{D}$ with associated correct answers. For any hypothesis $h \in H$ which is [[Consistent learner|consistent]] with $T$ we have a bound on the [[True error|true error]]
> $$\mathbb{P}[Error_{\mathbb{D}}(h) > \epsilon] \leq \vert H \vert e^{-m\epsilon}.$$

# Proof

Let $f$ be the target function.

Let $h \in H$ such that $\mathbb{P}_{\mathbb{D}}(h(a) = f(a)) \leq 1 - \epsilon$ (i.e. we have [[True error|true error]] $Error_{\mathbb{D}}(h) > \epsilon$). 

Then let $T$ be $m$ [[Independent identically distributed samples|i.i.d.]] samples from $A$ using $\mathbb{D}$. The probability $h$ is [[Consistent learner|consistent]] on $T$ is
$$\mathbb{P}_{\mathbb{D}}[h \mbox{ is consistent on } T] \leq (1 - \epsilon)^m$$
As the samples are [[Independent identically distributed samples|i.i.d.]]. Moreover as $\ln(1-\epsilon) \leq - \epsilon$ for $0 \leq \epsilon < 1$ this gives us
$$\mathbb{P}_{\mathbb{D}}[h \mbox{ is consistent on } T] \leq (1 - \epsilon)^m \leq e^{-m \epsilon}$$
If all $h \in H$ had $Error_{\mathbb{D}}(h) > \epsilon$ then we have
$$
\mathbb{P}[\mbox{Any } h \in H \mbox{ consistent with }T] \leq \vert H \vert e^{-m\epsilon} 
$$
the required result.

