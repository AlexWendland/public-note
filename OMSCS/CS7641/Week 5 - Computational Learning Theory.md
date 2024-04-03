---
aliases: 
checked: false
course: "[[CS7641 Machine Learning]]"
created: 2024-02-13
last_edited: 2024-02-13
publish: true
tags:
  - OMSCS
type: lecture
week: 5
---
# Week 5 - Learning Theory

[[Computational learning theory]] is fundamentally about 3 things:
- defining learning problems,
- show algorithms work, and
- showing problems are easy or hard. 

When considering problems it is useful to think about:
1. The probability of successful training.
	1. The probability the process works $1 - \delta$ 
2. Number of examples you need to train on.
	1. The size of the training set $m$.
3. Complexity of the hypothesis class.
	1. How complex is the representation - [[Modelling paradigm|modelling paradigm]]
4. Accuracy to which the target concept is approximated. 
	1. Within some $\epsilon$.
5. Manner in which the examples are presented.
	1. Batch or online.
6. Manner in which the [[Training data|training data]] is collected.
	1. Learner requests examples.
	2. Teacher gives examples.
	3. Fix distribution.
	4. Examples are picked poorly.

## 20 Questions

20 Questions is a game where there is a set of possible answers $A$ and a correct answer $c \in A$. There is a player (questioner) who wants to find $c \in A$ and a questionee who knows $c \in A$. The player then asks questions [[Boolean variable|boolean]] questions to questionee who answers True or false about item $c \in A$. 

> [!Note] 20 Questions
> In the traditional version of the game you have until 20 questions to guess the answer, thus the name!

There are different set ups for this game - but the point is to demonstrate the power of how [[Training data]] is collected. 

For simplicity we will call the questionee the teacher and the questioner the learner. 

### Simple: Teacher provides questions

If the goal of the game is too arrive at the answer as quickly as possible but the teacher can provide the questions. This should be solvable in 1 question.

The teacher can provide the question
- "Is the answer $c \in A$?"

### Normal: Binary search

If the learner has to come up with the questions. The best strategy in terms of expectation is to ask questions that divide the remaining potential answers into two even sized chunks. That way no matter the answers you have halved the solution space. This takes $\log_2(\vert A \vert)$ time to find $c$.

This method assumes that any question is valid.

### Restricted questions for the teacher

Lets further formalise this problem. Suppose further you can only ask questions in set $X$ about the answers in $A$.

For an example let $X$ be $k$-bit literals that relate to [[Boolean variable|boolean]] assignments for $X_i$ with $1 \leq i \leq k$. Then assume $A$ are boolean functions on $k$ variables that can be expressed as a logical formula involving $X_i$ or their negations $\overline{X_i}$ joint with $\land$. Then the answer to question $x \in X$ is $c(x)$.

>[!example]
>Suppose $k = 5$ and let $c = \overline{X_2} \land X_4 \land \overline{X_5}$. Then we might have the following series of questions

| $X_1$ | $X_2$ | $X_3$ | $X_4$ | $X_5$ | $c$ |
| ----- | ----- | ----- | ----- | ----- | --- |
| 1     | 0     | 1     | 1     | 0     | 1   |
| 0     | 0     | 0     | 1     | 0     | 1   |
| 1     | 1     | 1     | 1     | 0     | 0   |
| 1     | 0     | 1     | 0     | 0     | 0   |
| 1     | 0     | 1     | 1     | 1     | 0    |

In this set up we require 2 questions to establish the variables that didn't matter by having a true case where they were either 0 or 1. Then the number of questions as there are variables in the formula to verify they are required. 

You can see this in the above example. The first two questions show that $X_1$ and $X_3$ are not included in the formula, the 3rd one shows that if $X_2$ is positive then it fails, 4th one shows if $X_4$ is negative it fails and the last one shows that if $X_5$ is positive it fails.

So if the teacher presents the questions here it only takes at most $k + 2$ questions to work out the answer.

### Restricted question for the learner

In the current set up, if the learner were to guess it would take them $2^k$ guesses. As the formula potentially uses all literal and there is only one correct answer.

## Learning with mistake bounds

Clearly the restricted questions for the learner is a hard problem. Though instead we can change the set up.

Suppose instead of the learner giving an example to the teacher to answer, instead the teacher is going to give the learner an example to predict. The teacher then verifies if they were correct or not. If the learner is wrong they get a -1 to their score.

Instead of then trying to get the formula in the least time possible, we are trying to get the largest score from the provided examples.



### Algorithm

We are going to slowly build a table that reflects our guess of the formula. For each variable $X_i$ we have 3 possible states, not included, negative, and positive. In the example above this table would look like:

| Variable | Positive | Negative |
| ---- | ---- | ---- |
| $X_1$ |  |  |
| $X_2$ |  | Y |
| $X_3$ |  |  |
| $X_4$ | Y |  |
| $X_5$ |  | Y |

Where something that is neither positive or negative is not included.

The algorithm starts as follows:
1. Initialise the table with all positive and negatives selected.
2. For each example $x \in X$
	1. Using the table make a guess of the answer
		1. If a variable is ticked positive, it needs to be positive.
		2. If a variable is ticked negative, it needs to be negative.
	2. If we are wrong:
		2. For each $X_i$
			1. If $X_i$ was 0, remove $X_i$'s positive tick if it exists.
			2. If $X_i$ was 1, remove $X_i$'s negative tick if it exists.

This algorithm will only ever make $k+1$ mistakes so we have a bound on the number of mistakes we can make.

## Definitions

In machine learning there are similar definitions to other algorithmic disciplines.

![[Run time complexity]]

However there are some domain specific definitions as well.

![[Sample complexity]]

Touching upon the example above.

![[Mistake bound]]

Lets fix terminology for the next section. Suppose we are in the [[Modelling framework|modelling framework]] with some training data $T$. 
- Given some [[Modelling paradigm|hypothesis space]] $H$ the "true hypothesis" is $c \in H$ (i.e. for all $(a,b) \in T$ $c(a) = b$). 
- The current candidate hypothesis will be $h \in H$.
- A [[Consistent learner|consistent learner]] $h$ is one where $h(a) = c(a)$ for all $(a,b) \in T$.
- The [[Version space|version space]] VS(T) = \{$h \ \vert$  $h$ is a consistent learner with respect to $T$\}.

## Pac learning

There are two concepts of error when evaluating a hypothesis.

![[Training error]]

![[True error]]

Using this we can define what we call "probably approximately correct" (PAC) learner.

![[Probably approximately correct learnable (PAC)|PAC learner]]

Though showing something is PAC-learner is hard.

>[!example] $k$-bit example
>Suppose our underlying set $X = \{0,1\}^k$ and $H = C = \{h_i : h_i(x) = x_i\}$. Is there an algorithm that is $\epsilon$, $\delta$ [[Probably approximately correct learnable (PAC)|PAC learner]]?

## $\epsilon$-exhausted version space

![[epsilon-exhausted version space]]

>[!example] Xor example
>Suppose $A = \{0,1\}^2$ and our real function is [[Exclusive or|xor]] $\oplus$ on two variables $x_1$ and $x_2$. Let $H = \{x_1, \overline{x_1}, x_2, \overline{x_2}, T, F, \land, \lor, \oplus, =\}$ and set probability distribution $\mathbb{D}(0,0) = 0.1$, $\mathbb{D}(0,1) = 0.5$, $\mathbb{D}(1,0) = 0.4$, and $\mathbb{D}(1,1) = 0$. 
>Then with $T = \{((0,0), 0), ((1,0), 1)\}$ we have our [[Version space|version space]] to be $VS_H(T) = \{x_1, \lor, \oplus\} \subset H$.
>This [[Version space|version space]] is $0.5$-exhausted as $x_1$ doesn't correctly map $(0,1)$ and $\lor$ doesn't correctly map $(1,1)$. However as $\mathbb{D}(0,1) = 0.5$ and $\mathbb{D}(1,1) = 0$ a hypothesis in the [[Version space|version space]] has error at worst $0.5$. 

This is useful concept for finding the number of samples we need to take to us to give us a [[Probably approximately correct learnable (PAC)|PAC learner]].

![[Haussler Theorem]]

Note in the definition of [[Probably approximately correct learnable (PAC)|PAC learner]] $\mathbb{P}[Error_{\mathbb{D}}(h) > \epsilon]$ is exactly the quantity we need to bound with $\delta$ (as we need the probability of finding a good learner to be $1 - \delta$). Therefore if we have the ability to draw [[Independent identically distributed samples|i.i.d.]] examples we need $m$ to obey
$$
\vert H \vert e^{-m\epsilon} \leq \delta.
$$
Which rearranging for $m$ gives us
$$
m \geq \frac{1}{\epsilon}\left ( \ln(\vert H \vert) + \ln\left(\frac{1}{\delta}\right) \right).
$$
(Note this is polynomial in $\frac{1}{\epsilon}$, $\vert H \vert$ and $\frac{1}{\delta}$ as required by a [[Probably approximately correct learnable (PAC)|PAC learner]].) So given that good learner does exist in our [[Modelling paradigm|hypothesis space]] we have use drawing [[Independent identically distributed samples|i.i.d.]] representatives to give us a [[Probably approximately correct learnable (PAC)|PAC learner]] by checking if the hypothesis are consistent with the observations.

>[!example] 10-bit example
>Suppose our underlying set $X = \{0,1\}^10$ and $H = C = \{h_i : h_i(x) = x_i\}$. How many [[Independent identically distributed samples|i.i.d.]] samples do we need to draw to find a $\epsilon = 0.1$, $\delta = 0.2$ with $\mathbb{D}$ being uniform [[Probably approximately correct learnable (PAC)|PAC learner]]?
>Using the above formula we need
>$$m \geq 40 > 10 \cdot ( 2.3 + 1.6 ).$$

Note here that we didn't use what $\mathbb{D}$ was in this computation. 

A weakness of [[Haussler Theorem]] is that it doesn't handle infinite dimensional hypothesis spaces. 