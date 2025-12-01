---
aliases:
checked: false
created: 2023-10-03
draft: false
last_edited: 2023-11-11
tags:
  - programming
type: lemma
---
# Statement

>[!important] Theorem
>For a [[Flow network|flow network]] $(G, c, s, t)$ the size of the [[Max flow problem|max flow]] is the same as the [[Min st-cut problem|min st-cut]].

# Proof

First we show [[Max flow problem|max flow]] $\leq$ [[Min st-cut problem|min st-cut]].

In fact we will show something even stronger. For any [[Flow|flow]] $f$ and [[st-cut]] $(L, R)$ we have
$$size(f) \leq capacity(L,R).$$
This follows from [[Max-flow min-cut Theorem#Claim 1|Claim 1]] as we have
$$size(f) = f^{out}(L) - f^{in}(L) \leq f^{out}(L) = capacity(L,R).$$
Next we want to show [[Max flow problem|max flow]] $\geq$ [[Min st-cut problem|min st-cut]].

From [[Max-flow min-cut Theorem#Claim 2|Claim 2]] let $f^{\ast}$ be a flow given by the [[Ford-Fulkerson Algorithm]]. Then we have a [[st-cut]] $(L^{\ast},R^{\ast})$ such that
$$size(f^{\ast}) = capacity(L^{\ast},R^{\ast}).$$
However, from the definition of min and max we have
$$\max_f size(f) \geq size(f^{\ast}) = capacity(L^{\ast},R^{\ast}) \geq \max_{(L,R)} capacity(L,R).$$
Therefore these two inequalities provide the required result.

# Claim 1

>[!important] Claim 1
>Let $f$ be a [[Flow|flow]] and $(L,R)$ an [[st-cut]]. Then define
>$$f^{out}(X) := \sum_{\substack{(x,y) \in E\\ x \in X, y \in \overline{X}}} f(x,y), \mbox{ and } f^{in}(X) := \sum_{\substack{(y,x) \in E\\ x \in X, y \in \overline{X}}} f(y,x).$$
>Therefore we have
>$$size(f) = f^{out}(L) - f^{in}(L).$$

# Proof of Claim 1

This follows from playing around with formulas
$$\begin{align*}
f^{out}(L) - f^{in}(L) = & \sum_{\substack{(l,r) \in E\\ l \in L, r \in R}} f(l,r) - \sum_{\substack{(r,l) \in E\\ l \in L, r \in R}} f(r,l)\\
= & \left ( \sum_{\substack{(l,r) \in E\\ l \in L, r \in R}} f(l,r) + \sum_{\substack{(l,l^{\ast}) \in E\\ l, l^{\ast} \in L}} f(l,l^{\ast}) \right ) - \left ( \sum_{\substack{(r,l) \in E\\ l \in L, r \in R}} f(r,l) + \sum_{\substack{(l^{\ast},l) \in E\\ l, l^{\ast} \in L}} f(l^{\ast},l)\right )\\
= & \sum_{l \in L} f^{out}(l) + \sum_{l \in L} f^{in}(l)\\
= & f^{out}(s) + \sum_{l \in L \backslash \{s\}} \left(f^{out}(l) - f^{in}(v)\right)\\
= & f^{out}(s)\\
= & size(f)
\end{align*}$$
With the 4th line following from the fact that we can assume $s$ has no in flow. The 5th line follows from the preservation of flow.

# Claim 2

>[!important] Claim 2
>Let $f^{\ast}$ be a [[Flow|flow]] from the [[Ford-Fulkerson Algorithm]] then there exists a [[st-cut]] $(L^{\ast},R^{\ast})$ such that
>$$size(f^{\ast}) = capacity(L^{\ast},R^{\ast}).$$

## Proof of Claim 2

As $f^{\ast}$ is given by the [[Ford-Fulkerson Algorithm]] there is no [[Path (graph)|path]] from $s$ to $t$ in the [[Residual Network (flow)|residual network]] $G^{f^{\ast}}$.

Let
$$L^{\ast} = \{v \in V \vert s-v \mbox{ are path connected in } G^{f^{\ast}}\} \mbox{ and } R^{\ast} = V \backslash L^{\ast}.$$
We know $t \not \in L^{\ast}$ as there is no [[Path (graph)|path]] from $s$ to $t$. So this is an [[st-cut]].

Now consider edge $(l,r) \in E$ with $l \in L^{\ast}$ and $r \in R^{\ast}$ as there is no edge $(l,r) \in E^{f^{\ast}}$ we have $f^{\ast}(l,r) = c(l,r)$.

Similarly for edges $(r,l) \in E$ with $l \in L^{\ast}$ and $r \in R^{\ast}$ as there is no edge $(l,r) \in E^{f^{\ast}}$ we have $f^{\ast}(r,l) = 0$.

From [[Max-flow min-cut Theorem#Claim 1|Claim 1]] we have
$$\begin{align*}size(f^{\ast}) & = (f^{\ast})^{out}(L) + (f^{\ast})^{in}(L)\\
& =  \sum_{\substack{(l,r) \in E\\ l \in L, r \in R}} f^{\ast}(l,r) + \sum_{\substack{(r,l) \in E\\ l \in L, r \in R}} f^{\ast}(r,l)\\
& = \sum_{\substack{(l,r) \in E\\ l \in L, r \in R}} c(l,r)\\
& = capacity(L^{\ast}, R^{\ast}).\end{align*}$$


