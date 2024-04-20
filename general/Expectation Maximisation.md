---
aliases: 
checked: false
created: 2024-03-09
last_edited: 2024-03-09
publish: true
tags:
  - programming
  - machine-learning
type: algorithm
---
# Expectation Maximisation

Expectation maximising is an algorithm which can be used on problems such as [[Clustering problem|clustering problem]]. It is used in situations where you assume your data follows some underlying distribution $\mathbb{D}$ which in this instance is given by parameters $\theta$. We assume $\theta \in H$ our [[Modelling paradigm|hypothesis space]]. 

Suppose we draw $m$ samples from $\mathbb{D}_{\theta}$ which has an observed component $X = \{x_1, \ldots, x_m\}$ and an unobserved component $Z = \{z_1, \ldots, z_m\}$. Therefore the samples of $\mathbb{D}_{\theta}$ are given by $Y = X \cup Z$. 

Once you are provided with $X$ you can treat the values of $Z$ as random variables - similar with $Y$. Both $Z$ and $Y$ depend on the unknow parameters $\theta$.  

During the EM algorithm we will update our current hypothesis $h \in H$ for the parameters $\theta$, to a new hypothesis $h' \in H$. We want to update $h \in H$ by trying to maximise 
$$Q(h' \vert h) = \mathbb{E}[ \ln( \ \mathbb{P}_{\mathbb{D}} \ [Y \ \vert \ h']) \ \vert \ X, h \ ]
$$
Lets unpack this - we use our current hypotheses $h$ to guess at the values of $Z$. This gives us $X$ and $Z$ therefore $Y$. Now we want to find the hypothesis $h'$ (or parameters for $\mathbb{D}$) that maximises the log probability that $Y$ would occur. This follows a nice natural two step process.
1. Given our current hypothesis $h$ calculate the values for $Z$ the unobserved parameters, this gives us the function $Q(h' \vert h): H \rightarrow \mathbb{R}$, and then
2. Using the values of $X$ and $Z$ for $Y$ - find a hypothesis
$$
h' = \mbox{arg}\max_{h' \in H} Q(h' \vert h) = \mbox{arg}\max_{h' \in H} \mathbb{E}[ \ln( \mathbb{P}_{\mathbb{D}} \ [Y \ \vert \ h']) \ \vert \ X, h \ ].
$$

If the function $Q(h' \vert h)$ is continuous for all $h', h \in H$ then we will converge to a local maximum however we don't know how long this will take us or if this local maximum is a global maximum.

## Correctness

- We are monotonically decreasing [[Maximum likelihood estimation (MLE)|Maximum likelihood]] error of the groupings.
- Though this is not guaranteed to converge.
- Though it will not diverge either! 
- It can get stuck in local optimums.
	- So it is best that we restart this algorithm and take the best outcome.