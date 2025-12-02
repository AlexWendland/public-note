---
aliases:
checked: false
course: 'CS7641 Machine Learning'
created: 2024-02-19
draft: false
last_edited: 2024-02-19
title: Week 6 - Bayesian learning
tags:
  - OMSCS
type: lecture
week: 6
---
# Week 6 - Bayesian learning

## Bayes rule

To start this lecture lets remind ourselves of the definition of [conditional probability](../../general/conditional_probability.md).

[Conditional probability](../../general/conditional_probability.md)

As a simple corollary we get [Bayes rule](../../general/bayes_rule.md).

[Bayes rule](../../general/bayes_rule.md)

>[!question]
>Suppose there is a illness effects $0.8\%$ of the population $\mathbb{P}[I] = 0.008$. We have a test that has a [true positive](../../general/result_types.md) chance of $98\%$ (i.e. $\mathbb{P}[+ve | I] = 0.98$) and a [true negative](../../general/result_types.md) result of $97\%$ (i.e. $\mathbb{P}[-ve \vert \lnot I] = 0.97$). Given you have a positive test result are you more likely to have the illness or not?

Here we apply [Bayes rule](../../general/bayes_rule.md).
$$\mathbb{P}[I \ \vert +ve] = \frac{\mathbb{P}[+ve \ \vert \ I] \cdot \mathbb{P}[I]}{\mathbb{P}[+ve]} = \frac{0.98 \cdot 0.008}{\mathbb{P}[+ve]} = \frac{0.00784}{\mathbb{P}[+ve]} $$
whereas
$$\mathbb{P}[\lnot I \ \vert +ve] = \frac{\mathbb{P}[+ve \ \vert \ \lnot I] \cdot \mathbb{P}[\lnot I]}{\mathbb{P}[+ve]} = \frac{(1 - \mathbb{P}[-ve \vert \lnot I]) \cdot (1 - \mathbb{P}[I])}{\mathbb{P}[+ve]} = \frac{0.02976}{\mathbb{P}[+ve]}$$
giving that we are more likely to not have the illness than have it with a positive result.

## Applying this to learning

Suppose $h \in H$ is a hypothesis belonging to our [hypothesis space](../../general/modelling_paradigm.md) and we have $D$ data. Then to see the probability our hypothesis is given the data $\mathbb{P}[h \vert D]$ we can use [Bayes rule](../../general/bayes_rule.md) to reduce it to things we can calculate
$$
\mathbb{P}[h \vert D] = \frac{\mathbb{P}[D \vert h]\mathbb{P}[h]}{\mathbb{P}[D]}.
$$
- Here $\mathbb{P}[D \vert h]$ is the accuracy of our prediction.
- Then $\mathbb{P}[h]$ is a reflection of prior knowledge about which hypothesis are likely or not.
- Lastly $\mathbb{P}[D]$ reflects our prior knowledge about the data we are sampling from.

When we are training our model on [training data](../../general/training_data.md) $T$, we are trying to find
$$
\mbox{arg}\max_{h \in H} \mathbb{P}[h \vert T].
$$
Though for each $h \in H$ we have the same $\mathbb{P}[D]$ as this does not depend on $h$. So we might as well remove this from our calculation - here we get the [maximum a posteriori probability](../../general/maximum_a_posteriori_probability_estimate_(map).md).

[Maximum a posteriori probability estimate (MAP)](../../general/maximum_a_posteriori_probability_estimate_(map).md)

Sometimes we will have no prior preference on the [hypothesis space](../../general/modelling_paradigm.md) in this case we might as well assume it is uniform and remove it from our calculations - here we get the [maximum likelihood estimation](../../general/maximum_likelihood_estimation_(mle).md).

[Maximum likelihood estimation](../../general/maximum_likelihood_estimation_(mle).md)

Though to actually calculate these would be very hard - as the [hypothesis space](../../general/modelling_paradigm.md) might be very large.

## Noise free data

Suppose:
- There is some target $c : A \rightarrow B$.
- We have some [irreducible error](../../general/irreducible_error.md) free (noise free) [training data](../../general/training_data.md) $T$, so for $(a,b) \in T$ we have $b = c(a)$.
- We have a finite [hypothesis space](../../general/modelling_paradigm.md) $H$ which contains the target $c \in H$.
- We have no prior preference on the [hypothesis space](../../general/modelling_paradigm.md) $H$.
- Each hypothesis is an [independent event](../../general/independent_events.md).

Now we are use [Bayes rule](../../general/bayes_rule.md) to calculate $\mathbb{P}(h \vert T)$ for each $h \in H$.
- As we have no prior preference on $H$ we have $\mathbb{P}[h] = \frac{1}{\vert H \vert}$.
- As we know the data is noise free we have
$$\mathbb{P}[T \vert h] = \begin{cases} 1 & \mbox{if } b = h(a) \mbox{ for all } (a,b) \in T\\ 0 & \mbox{otherwise} \end{cases}$$
however this describes the [version space](../../general/version_space.md) for $H$ with $T$, $VS_H(T)$, so
$$\mathbb{P}[T \vert h] = \mathbb{I}[h \in VS_H(T)].$$
- As each hypothesis is an [independent event](../../general/independent_events.md) we have
$$\mathbb{P}[T] = \sum_{h \in H} \mathbb{P}[T \vert h]\mathbb{P}[h] = \sum_{h \in VS_H(T)} \frac{1}{\vert H \vert} = \frac{\vert VS_H(T) \vert}{\vert H \vert}.$$
This gives
$$
\mathbb{P}(h \vert T) = \frac{\mathbb{P}[T \vert h] \mathbb{P}[h]}{\mathbb{P}[T]} = \frac{\mathbb{I}[h \in VS_H(T)]}{\vert VS_H(T) \vert}.
$$
## Gaussian noise

In the previous set up we assumed there was no noise, this time we will introduce some.

Suppose:
- There is some target $c : A \rightarrow \mathbb{R}$.
- We have some [i.i.d.](../../general/independent_identically_distributed_samples.md) [normally distributed](../../general/normal_distribution.md) noise values $\epsilon \sim N(0,\sigma^2)$ for each of our [training data](../../general/training_data.md) $t \in T$.
- The [training data](../../general/training_data.md) $T$ is such that $(a_i,b_i) \in T$ we have $b_i = c(a_i) + \epsilon_i$.

Now lets try to compute the [maximum likelihood estimation](../../general/maximum_likelihood_estimation_(mle).md) for our [hypothesis space](../../general/modelling_paradigm.md) $H$.
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
So this shows that [finding the maximum likelihood estimation for normally distributed noise is the same as minimising mean squared error](../../general/finding_the_maximum_likelihood_estimation_for_normally_distributed_noise_is_the_same_as_minimising_mean_squared_error.md).

>[!note]
>If we switch our assumption about how the noise is distributed, then we find a different loss function will be appropriate.

This shows that the loss function we use really relates to the noise we have in our observations.

## Probability length

[Length of a probability](../../general/length_of_a_probability.md)

Now assume we have a prior distribution on our [hypothesis space](../../general/modelling_paradigm.md) $H$ such that $\mathbb{P}[h]$ is higher when it is a simpler explanation. For some [training data](../../general/training_data.md) $T$ lets look at the [maximum a posteriori probability estimate](../../general/maximum_a_posteriori_probability_estimate_(map).md)
$$
\begin{align*}
h_{MAP} = & \mbox{arg}\max_{h \in H}  \ \mathbb{P}[T \vert h]\mathbb{P}[h]\\
= & \mbox{arg}\max_{h \in H} \left [ \ \log\left ( \mathbb{P}[T \vert h]\right ) + \log \left ( \mathbb{P}[h] \right ) \ \right ] & \mbox{by taking logs}\\
= & \mbox{arg}\min_{h \in H} \left [ \ -\log\left ( \mathbb{P}[T \vert h]\right ) - \log \left ( \mathbb{P}[h] \right ) \ \right ] & \mbox{negative max is min}\\
= & \mbox{arg}\min_{h \in H} \left [ \ \mbox{length}[T \vert h] + \mbox{length}[h] \ \right ] & \mbox{by the definition of length}\\
\end{align*}
$$
here we have a pay off. Longer length explanations in $\mbox{length}[h]$ may lead better explanations of $T$ by the hypothesis. Though this will have to be worth in increase in length of that hypothesis. This is [Occam's razor](../../general/occam's_razor.md) in an equation.

## Bayesian classification

[Bayeses optimal classifier](../../general/bayeses_optimal_classifier.md)

