---
aliases:
checked: false
course: '[[CS7641 Machine Learning]]'
created: 2024-02-21
draft: false
last_edited: 2024-02-21
tags:
  - OMSCS
type: lecture
week: 6
---
# Week 6 - Bayesian Inference

## Joint distributions

We can use the definition of [[Conditional probability|conditional probability]] to help calculate joint probabilities.
$$\mathbb{P}]A \cap B] = \mathbb{P}[A, B] = \mathbb{P}[A \vert B] \mathbb{P}[B].$$
If probabilities are independent this simplifies to
$$\mathbb{P}[A, B] = \mathbb{P}[A] \ \mathbb{P}[B].$$
We say simplifies as to keep track of $\mathbb{P}[A, B]$ if $A$ has domain of size $n$ and $B$ of size $m$ we only need to keep track of $n + m - 2$ values whereas in the first case we need to keep track of $nm - 1$ values.

Therefore independence simplifies the amount of knowledge we need to store to compute the probability of a large state. Therefore is useful to generalise the definition of independence.

![[Conditional independence]]

>[!note] Why is it a generalisation?
>Note if $A$ and $B$ are [[Independent events|independent event]] then
>$$\mathbb{P}[A \vert B] = \frac{\mathbb{P}[A, B]}{\mathbb{P}[B]} = \mathbb{P}[A].$$
>We could say that $A$ is conditionally independent on $B$ given any event.

## Bayesian networks (belief networks)

For a set of [[Random variable|random variables]] $X_v$ for $v \in V$ we would like to [[Graph|graph]] these relationships using a directed graph. We want an edge $(u,v) \in E$ to signify that $X_u$ is dependent on $X_v$. Though there is a lot of choice in this as for any two dependent variables we could choose $(u,v) \in E$ or $(v,u) \in E$ - however we want to make a directional choice.

![[Bayesian network]]

$\mathbb{P}[X_1 = a_1, X_2 = a_2, .... X_n = a_n] = \prod_{i=1}^n \mathbb{P}[X_i = a_i \vert X_u = a_u \forall (u,v) \in E]$


>[!example] Independent variables
>Let $A$ and $B$ be [[Independent events|independent event]]. Then $G = (\{A, B\}, \emptyset )$ forms a [[Bayesian network]] as
>$$\mathbb{P}[A,B] = \mathbb{P}[A]\mathbb{P}[B].$$
>Note that it also forms a [[Bayesian network]] with $G = (\{A, B\}, \{(A,B)\} )$ or $G = (\{A, B\}, \{(B,A)\} )$ but it would not be minimal.

>[!example] Conditionally independent
>Suppose we have [[Random variable|random variables]] $A$, $B$, and $C$ where $C$ is [[Conditional independence|conditionally independent]] of $A$ given $B$. Then $G = (\{A, B, C\}, \{(A,B), (B,C)\})$ forms as [[Bayesian network]].

The property of being [[Conditional independence|conditionally independent]] is deducible from the [[Bayesian network]] $(G, X)$ by using the [[Chain rule (probability)|chain rule]].

![[Chain rule (probability)|chain rule]]

Lets [[Topological sorting (DAG)|topological order]] $V$ so $V = \{1, 2, \ldots, n\}$ where $(i,j) \in E$ we have $i < j$. Then apply the [[Chain rule (probability)|chain rule]] to
$$
\mathbb{P}[X_1, X_2, \ldots, X_n] = \prod_{k=1}^n \mathbb{P}[X_k \vert X_1, X_2, \ldots, X_{k-1}]
$$
and compare this to
$$\mathbb{P}[X] =\prod_{v \in V} \mathbb{P}[X_v \vert \bigcap_{(u,v) \in E} X_u].$$
So for any $X_i$ and $j < i$ such that $(j,i) \not \in E$ then $X_i$ is [[Conditional independence|conditionally independent]] of $X_j$ given $\bigcup_{(u,i) \in E} X_u$.

This is in fact a defining property of [[Bayesian network]].

![[Local Markov property]]

![[Bayesian network if and only if it satisfies the local Markov Property]]

## Inference rules

Once you have a [[Bayesian network]] you can use it to calculate all kinds of conditional probabilities. There are 3 main rules that help you do this.

![[Marginalisation (probability)]]

![[Chain rule (probability)|chain rule]]

![[Bayes rule#Statement]]

>[!example]
>Suppose we have two boxes, the first box has 3 green balls and 1 orange, the second has 3 blue and 2 green. Then we do the following, we pick a box with a half chance of picking either $P$, we draw and do not replace 1 ball from that box $D1$, lastly we draw another ball from the same box $D2$.
>This can be represented as a [[Bayesian network]] with the following graph $(\{P, D1, D2\}, \{(P, D1), (D1, D2), (P, D2)\})$. Note this means $D1$ depends on $P$ and $D2$ depends on $P$ and $D1$.
>What is $\mathbb{P}[D2 =$ blue $\vert D1 =$ green$]$?

We can write out the [[Conditional probability|conditional probability]] tables when they rely on all their dependents quite easily. First note $\mathbb{P}[P = 1] = \mathbb{P}[P = 2] = 0.5$. For the first joint distribution, we have what is below.

| $P$ | $\mathbb{P}[D1 = green \vert P]$ | $\mathbb{P}[D1 = orange\vert P]$ | $\mathbb{P}[D1= blue \vert P]$ |
| --- | -------------------------------- | -------------------------------- | ------------------------------ |
| 1   | 3/4                              | 1/4                              | 0                              |
| 2   | 2/5                              | 0                                | 3/5                            |

What follows is the second.

| P   | D1     | $\mathbb{P}[D2 = green \vert P, D1]$ | $\mathbb{P}[D2 = orange \vert P, D1]$ | $\mathbb{P}[D2 = blue \vert P, D1]$ |
| --- | ------ | ------------------------------------ | ------------------------------------- | ----------------------------------- |
| 1   | green  | 2/3                                  | 1/3                                   | 0                                   |
| 1   | orange | 1                                    | 0                                     | 0                                   |
| 2   | green  | 1/4                                  | 0                                     | 3/4                                 |
| 2   | blue   | 1/2                                  | 0                                     | 1/2                                 |

These tables perfectly set us up to calculate an exact state using the [[Chain rule (probability)|chain rule]]. So we are going to try and rewrite this probability in terms of exact states first. So lets use the definition of [[Conditional probability|conditional probability]]
$$\mathbb{P}[D2 = blue \vert D1 = green] = \frac{\mathbb{P}[D2 = blue, D1 = green]}{\mathbb{P}[D1 = green]}$$
Next lets use [[Marginalisation (probability)|marginalisation]] to add in the first variable.
$$\mathbb{P}[D2 = blue \vert D1 = green] = \frac{\mathbb{P}[D2 = blue, D1 = green, P=1] + \mathbb{P}[D2 = blue, D1 = green, P=2]}{\mathbb{P}[D1 = green, P = 1] + \mathbb{P}[D1 = green, P = 2]}$$

Lastly lets use the [[Chain rule (probability)|chain rule]] to turn them into the probabilities we have in the tables above. For example
$$\mathbb{P}[D2 = blue, D1 = green, P=1] = \mathbb{P}[P=1] * \mathbb{P}[D1 = green \vert P=1] * \mathbb{P}[D2 = blue \vert D1 = green, P=1]$$

doing this for each quantity we get

$$\mathbb{P}[D2 = blue \vert D1 = green] = \frac{1/2*3/4*0 + 1/2*2/5*3/4}{1/2*3/4 + 1/2*2/5} = \frac{3/10}{23/20} = \frac{6}{23}.$$

## Naive Bayes Classifier

Lets picture a [[Bayesian network]] with one root node and all other nodes as children of it. For this it is useful to think of an example.

>[!example] Spam mail
>We are given 3 words Viagra, Price and Udacity and depending on the existence of these words in an email we have to decide if it is spam or not. We can sample for already labelled data to understand the probabilities of these words appearing or not appearing.

First lets draw the Naive Bayes Classifier diagram.

![Naice Bayes](../../../images/excalidraw/Naice Bayes.excalidraw.svg)

This is a model for if the email is spam or not. Lets assume the probability of spam is $\mathbb{P}[Spam] = 0.4$. Then we have the [[Conditional probability|conditional probabilities]] below.

| $\mathbb{P}[V \vert S]$ | $V = Viagra$ | $V = Prince$ | $V = Udacity$ |
| ----------------------- | ------------ | ------------ | ------------- |
| $S = Spam$              | 0.3          | 0.2          | 0.0001        |
| $S = Not \ Spam$        | 0.001        | 0.1          | 0.1           |

To work these out we have only had to sample from our spam and non-spam mail how many times they contain the word $V$.

Now we would like to know
$$\mathbb{P}[Spam \vert Viagra, \lnot Prince, \lnot Udacity]$$
To turn this into something we can use from above we apply [[Bayes rule]] to this
$$\mathbb{P}[S \vert V, \lnot P, \lnot U] = \frac{\mathbb{P}[V, \lnot P, \lnot U \vert S] \mathbb{P}[S]}{\mathbb{P}[V, \lnot P, \lnot U]}.$$
(Shortening the words to their first letters.) Next we apply the [[Chain rule (probability)|chain rule]] but knowing that $V$ $P$ and $U$ are [[Conditional independence|conditionally independent]].
$$
\begin{align*}
\mathbb{P}[S \vert V, \lnot P, \lnot U] & = \frac{\mathbb{P}[V, \lnot P, \lnot U \vert S] \mathbb{P}[S]}{\mathbb{P}[V, \lnot P, \lnot U]}\\
& = \frac{\left ( \mathbb{P}[V \vert \lnot P, \lnot U, S] \mathbb{P}[\lnot P \vert \lnot U, S] \mathbb{P}[\lnot U \vert S] \right ) \mathbb{P}[S]}{\mathbb{P}[V, \lnot P, \lnot U]} & \mbox{chain rule}\\
& = \frac{\left ( \mathbb{P}[V \vert S] \mathbb{P}[\lnot P \vert S] \mathbb{P}[\lnot U \vert S] \right ) \mathbb{P}[S]}{\mathbb{P}[V, \lnot P, \lnot U]} & \mbox{conditional independence}\\
& = \frac{\left ( \mathbb{P}[V \vert S] \mathbb{P}[\lnot P \vert S] \mathbb{P}[\lnot U \vert S] \right ) \mathbb{P}[S]}{\sum_{X \in \{S, \lnot S\}}\mathbb{P}[V, \lnot P, \lnot U, X]} & \mbox{marginalisation}\\
& = \frac{\left ( \mathbb{P}[V \vert S] \mathbb{P}[\lnot P \vert S] \mathbb{P}[\lnot U \vert S] \right ) \mathbb{P}[S]}{\sum_{X \in \{S, \lnot S\}} \mathbb{P}[V \vert X] \mathbb{P}[\lnot P \vert X] \mathbb{P}[\lnot U \vert X] \mathbb{P}[X]} & \mbox{chain and c.i.}\\
& = \frac{0.3*0.8*0.9999*0.4}{0.3*0.8*0.9999*0.4 + 0.001*0.9*0.9*0.6} & \mbox{substution}\\
& \approx 0.9949
\end{align*}
$$

We want to do this but not have to crack out the pen and paper every time.

![[Naive Bayes classifier]]

This is cool as,
- Normally [[Inference]] is expensive to do, however in this case it makes it really cheap.
- The model has few parameters so has low [[Spacial complexity|spacial complexity]].
- If you have sufficient data you can make very good estimates on these probabilities.
- This connects [[Inference]] and [[Classification problems|classification problems]].
- Empirically widely successful.

Though the main consideration when using this is you will need to smooth the data to make sure we don't zero out options due to limitations of our data.

## Why sample

- To get indicative distributions of the date. Potentially this is costly and we can now use these probabilities to run simulations.
- To simulate a complex process by sampling smaller bits of it.
- Approximate inference, the process of looking at samples that only have a certain property to understand joint distributions.
	- Actual inference is hard!
- To "visualise" or get a feel for the data so we have intuition to reason about the state.
