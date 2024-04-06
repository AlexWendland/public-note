---
aliases: 
checked: false
created: 2024-04-06
last_edited: 2024-04-06
publish: true
tags:
  - machine-learning
type: definition
---
>[!tldr] Incremental learning 
>Suppose we have a sequence of learning rates $\alpha: \mathbb{N} \rightarrow \mathbb{R}$. Then a value $V$ *incrementally learns* some random variable $X$ if for $t \in \mathbb{N}$ with samples $x_t$ from $X$ we set 
>$$V_t = V_{t-1}(1 - \alpha_t) + \alpha x_t$$ 
>then let $V = \lim_{t \rightarrow \infty} V_t$. This is denoted $V \leftarrow^{\alpha} X$.

