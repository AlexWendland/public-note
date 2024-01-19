---
aliases:
  - perceptron rule
checked: false
created: 2024-01-18
last_edited: 2024-01-18
publish: true
tags:
  - programming
type: algorithm
---
# Perceptron rule

This is a way to train a [[Perceptron (neural network)|perceptron]] to classify [[Training data|training data]] $T$ where $A = \mathbb{R}^n$ and $B = \{0,1\}$ if the data is [[Linearly separable|linearly separable]]. We assume the [[Perceptron (neural network)|perceptron]] we are training is a function $p: \mathbb{R}^n \rightarrow \{0,1\}$ defined by weights $w_i, \theta \in \mathbb{R}$. For this we require a sufficiently small learning rate $\eta \in \mathbb{R}_{>0}$. The idea is to reply the data by nudging the weights ($\Delta w_i$) of the [[Perceptron (neural network)|perceptron]] slowly towards an even split.

To simplify the treatment of $\theta$ we just extend $A = \mathbb{R}^{n+1}$ where all of $T$ has a $-1$ (i.e. $x_{n+1} = -1$) in the additional position. Then we set $\theta =: w_{n+1}$ and compare to zero, i.e. instead of checking if
$$
\sum_{i=1}^n w_i x_i \geq \theta, \mbox{ we check } 0 \leq \sum_{i=1}^n w_ix_i + \theta \cdot -1 =: \sum_{i=1}^{n+1} w_i x_i.
$$
Then checking a random training example $(x,y) \in T$ with current weights $w_i$ we set $\hat{y} = \mathbb{I}(\sum_{i=1}^{n+1} w_i x_i \geq 0) \in \{0,1\}$ where $\mathbb{I}$ is the indicator function mapping true to $1$ and false to $0$. The we change the weights $\Delta w_i := \eta (y - \hat{y})x_i$ and then redefine $w_i \leftarrow w_i + \Delta w_i$. Note as $y, y_i \in \{0,1\}$ we have
$$
(y - \hat{y}) = \begin{cases} 0 & \mbox{if } y = \hat{y}\\ 1 & \mbox{if } y = 1 \mbox{ and } \hat{y} = 0\\ -1 & \mbox{if } y = 0 \mbox{ and } \hat{y} = 1.\end{cases}
$$
To make sure $\eta$ is low enough we might reduce it slowly over time (though we have to make sure the sequence of $\eta$ converge to zero whilst the sum of $\eta$ diverge to infinity) and then stop when $y = \hat{y}$ for all our training data. This will only stop if $T$ is [[Linearly separable|linearly separable]].

## Pseudocode

```pseudocode
perceptron_rule(T):
	Input: Training data T = {((x_1, x_2, ..., x_n, x_{n+1} = -1), y)}
	Output: perceptron weights w_1, w_2, ...., w_n, w_{n+1} = theta.
1. Set w_i = 1 for 1 = 1, 2, ..., n+1.
2. hat{y}_t = set_y_hat(T, w_i)
3. While there exists t in T such that hat{y}_t not = y_t, and let count be the number of intterations:
	3.1. Choose random t in T such that hat{y}_t not = y_t
	3.2. Set eta = 1/count
	3.3. for i = 1, ... , n+1
		3.3.1. Set delta w_i = eta (y - hat(y)_t) x_i
		3.3.2. Set w = w_i + delta w_i
	3.4. hat{y}_t = set_y_hat(T, w_i)
4. Return w_i

set_y_hat(T, w_i):
	Input: Training data T = {((x_1, x_2, ..., x_n, x_{n+1} = -1), y)} and
		perceptron weights w_1, w_2, ...., w_n, w_{n+1} = theta.
	Output: For each t in T new hat(y)_t
1. for t = ((x_1, ..., x_{n_1}), y) in T:
	1.1. Set hat{y}_t = bool(sum_{i=1}^{n+1} x_i >= 0)
2. return hat{y}_t
```

