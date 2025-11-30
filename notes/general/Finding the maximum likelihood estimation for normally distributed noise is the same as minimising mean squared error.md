---
aliases: 
checked: false
created: 2024-02-21
last_edited: 2024-02-21
draft: false
tags:
  - maths
type: lemma
---
# Statement

> [!important] Lemma
> Suppose we have some target $c : A \rightarrow \mathbb{R}$ where the [[Training data|training data]] $T$ has [[Independent identically distributed samples|i.i.d.]] [[Normal distribution|normally distributed]] noise values $\epsilon \sim N(0,\sigma^2)$ such that $(a_i,b_i) \in T$ we have $b_i = c(a_i) + \epsilon_i$. Then finding the [[Maximum likelihood estimation (MLE)|maximum likelihood estimation]] is the same as minimising the [[Mean squared error (MSE)]], i.e.
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