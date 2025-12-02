---
aliases:
checked: false
created: 2024-02-21
draft: false
last_edited: 2024-02-21
title: Finding the maximum likelihood estimation for normally distributed noise is
  the same as minimising mean squared error
tags:
  - maths
type: lemma
---
# Statement

> [!important] Lemma
> Suppose we have some target $c : A \rightarrow \mathbb{R}$ where the [training data](training_data.md) $T$ has [i.i.d.](independent_identically_distributed_samples.md) [normally distributed](normal_distribution.md) noise values $\epsilon \sim N(0,\sigma^2)$ such that $(a_i,b_i) \in T$ we have $b_i = c(a_i) + \epsilon_i$. Then finding the [maximum likelihood estimation](maximum_likelihood_estimation_(mle).md) is the same as minimising the [Mean squared error (MSE)](mean_squared_error_(mse).md), i.e.
> $$h_{MLE} = \mbox{arg}\min_{h \in H} mse(h, T).$$

# Proof

This comes from direct calculation.

$$
\begin{align*}
h_{MLE} & = \mbox{arg}\max_{h \in H} \mathbb{P}[T \vert h]\\
& = \mbox{arg}\max_{h \in H} \prod_{t \in T} \mathbb{P}[t \vert h] & \mbox{as each } \epsilon \mbox{ is i.i.id}\\
& = \mbox{arg}\max_{h \in H} \prod_{t \in T} \frac{1}{\sigma \sqrt{2\pi}} \exp \left [ - \frac{1}{2} \left ( \frac{b_i - h(a_i)}{\sigma} \right )^2 \right ] & \mbox{normal distribution}\\
& = \mbox{arg}\max_{h \in H} \prod_{t \in T} \exp \left [ - \frac{1}{2} \left ( \frac{b_i - h(a_i)}{\sigma} \right )^2 \right ] & \mbox{no change in argmax}\\
& = \mbox{arg}\max_{h \in H} \sum_{t \in T} - \frac{1}{2} \left ( \frac{b_i - h(a_i)}{\sigma} \right )^2 & \mbox{log is concave}\\
& = \mbox{arg}\max_{h \in H} \sum_{t \in T} - \left (b_i - h(a_i) \right )^2 & \mbox{no change in argmax}\\
& = \mbox{arg}\min_{h \in H} \sum_{t \in T} \left (b_i - h(a_i) \right )^2 & \mbox{negative max is min}\\
& = \mbox{arg}\min_{h \in H} mse(h,T) & \mbox{definition of MSE.}
\end{align*}
$$
