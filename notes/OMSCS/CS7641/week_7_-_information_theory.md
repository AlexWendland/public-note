---
aliases:
checked: false
course_code: CS7641
course_name: Machine Learning
created: 2024-02-24
draft: false
last_edited: 2024-02-24
tags:
  - OMSCS
title: Week 7 - Information Theory
type: lecture
week: 7
---
# Information

We want to measure the amount of information we need to transmit to send a message. However, the underlying facts about the message we will receive effect the length of that message.

For example, if we have a fair coin and I need to tell you about 10 flips of this coin - I will need to transmit a message of 10 [bits](../../general/bit.md). There are $2^{10}$ potential outcomes which are evenly weighted so we can do no better than a message of size 10.

In comparison, if the coin we are flipping is unfair with the probability of heads being 1. Then there is only 1 potential outcome. Therefore I don't need to transmit any information to you for you to know the outcome of me flipping it 10 times - you already know.

Suppose now we are relaying messages about words using 4 letters. If each letter has equal probability of appearing in a word then to communicate a word of length 4 we need 8 [bits](../../general/bit.md). Where we use 2 [bits](../../general/bit.md) to indicate each letter.

Instead lets suppose the first letter has probability $0.5$ of being in each place, the second letter has probability $0.25$ and the last 2 letters have probability $0.125$. For a word of length 3 can we on expectation do better than 8 bits?

| Letter          | A   | B    | C     | D     |
| --------------- | --- | ---- | ----- | ----- |
| Probability     | 0.5 | 0.25 | 0.125 | 0.125 |
| Representation  | 0   | 10   | 110   | 111   |
| Expected length | 0.5 | 0.5  | 0.375 | 0.375 |

Using the underlying probability distribution we can design representations of these letters to reduce the expected length of a single letter to 1.75 therefore making the 4 letter word we can use only 7 bits on expectation.

This has the interesting side effect of the further away from being uniformly random the background distribution is the less information it takes to transmit a message about it will be.

Mathematically we use [Information entropy](../../general/information_entropy.md) to inform us about how close a [random variable](../../general/random_variable.md) is to being uniform. With higher value indicating it is closer to [uniformly random](../../general/uniform_distribution.md).

[Information entropy](../../general/information_entropy.md)

# Information between two variables

First lets remind ourselves of

[Joint distribution](../../general/joint_distribution.md)

We can use this to define what the [Joint Entropy](../../general/joint_entropy.md) between two variables is.

[Joint Entropy](../../general/joint_entropy.md)

We want a measure of how much one variables tells us about another. I.e. $\mathbb{P}[Y \vert X]$ is considerably larger than $\mathbb{P}[Y]$. This means that $Y$ is in some way consumed by $X$. First lets look at the [Information entropy](../../general/information_entropy.md) of the [conditional probability](../../general/conditional_probability.md).

[Conditional entropy](../../general/conditional_entropy.md)

Notice how independence plays out here.

[If two variables are independent joint entropy is additive](../../general/if_two_variables_are_independent_joint_entropy_is_additive.md)

[If two variables are independent conditional entropy excludes the dependent](../../general/if_two_variables_are_independent_conditional_entropy_excludes_the_dependent.md)

In the first case by looking at their joint distributions we still need the same amount of information as if we considered them individually. Secondly by telling you about $X$ it doesn't take any less information to tell you about $Y$.

[Conditional entropy](../../general/conditional_entropy.md) could be small in two cases - either $X$ tells us a lot about $Y$ (i.e. $\mathbb{P}[Y\vert X] = 1$) or that $H(Y)$ was very small to begin with. So we need a better idea to tell us how related $X$ and $Y$ are.

[Mutual information](../../general/mutual_information.md)

Let $X$ and $Y$ represent two [i.i.d.](../../general/independent_identically_distributed_samples.md) fair coin tosses then we have $I(X,Y) = 0$ i.e. these events tell us nothing about one another. Whereas $I(X,X) = 1$ $X$ completely tells us about $X$.

[Mutual information is symmetric](../../general/mutual_information_is_symmetric.md)

# KL-divergence

We would like to be able to tell when two distributions are similar. For this we use the following definition. Notice if $P = Q$ then $D_KL(P \vert \vert Q) = 0$.

[KL-divergence](../../general/kullback–leibler_divergence.md)
