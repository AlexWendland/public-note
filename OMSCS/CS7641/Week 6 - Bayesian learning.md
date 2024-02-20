---
aliases: 
checked: false
course: "[[CS6200 Introduction to Graduate Algorithms]]"
created: 2024-02-19
last_edited: 2024-02-19
publish: true
tags:
  - OMSCS
type: lecture
week: 6
---
# Week 6 - Bayesian learning

## Bayes rule

To start this lecture lets remind ourselves of the definition of [[Conditional probability|conditional probability]].

![[Conditional probability]]

As a simple corollary we get [[Bayes rule]].

![[Bayes rule]]

>[!question]
>Suppose there is a illness effects $0.8\%$ of the population $\mathbb{P}[I] = 0.008$. We have a test that has a [[Result types|true positive]] chance of $98\%$ (i.e. $\mathbb{P}[+ve | I] = 0.98$) and a [[Result types|true negative]] result of $97\%$ (i.e. $\mathbb{P}[-ve \vert \lnot I] = 0.97$). Given you have a positive test result are you more likely to have the illness or not?

Here we apply [[Bayes rule]].
$$\mathbb{P}[I \ \vert +ve] = \frac{\mathbb{P}[+ve \ \vert \ I] \cdot \mathbb{P}[I]}{\mathbb{P}[+ve]} = \frac{0.98 \cdot 0.008}{\mathbb{P}[+ve]} = \frac{0.00784}{\mathbb{P}[+ve]} $$
whereas
$$\mathbb{P}[\lnot I \ \vert +ve] = \frac{\mathbb{P}[+ve \ \vert \ \lnot I] \cdot \mathbb{P}[\lnot I]}{\mathbb{P}[+ve]} = \frac{(1 - \mathbb{P}[-ve \vert \lnot I]) \cdot (1 - \mathbb{P}[I])}{\mathbb{P}[+ve]} = \frac{0.02976}{\mathbb{P}[+ve]}$$
giving that we are more likely to not have the illness than have it with a positive result. 

## Applying this to learning

Suppose $h \in H$ is a hypothesis belonging to our [[Modelling paradigm|hypothesis space]] and we have $D$ data. Then to see the probability our hypothesis is given the data $\mathbb{P}[h \vert D]$ we can use [[Bayes rule]] to reduce it to things we can calculate
$$
\mathbb{P}[h \vert D] = \frac{\mathbb{P}[D \vert h]\mathbb{P}[h]}{\mathbb{P}[D]}.
$$
- Here $\mathbb{P}[D \vert h]$ is the accuracy of our prediction. 
- Then $\mathbb{P}[h]$ is a reflection of prior knowledge about which hypothesis are likely or not. 
- Lastly $\mathbb{P}[D]$ reflects our prior knowledge about the data we are sampling from.

When we are training our model on [[Training data|training data]] $T$, we are trying to find
$$
\mbox{arg}\max_{h \in H} \mathbb{P}[h \vert T].
$$
Though for each $h \in H$ we have the same $\mathbb{P}[D]$ as this does not depend on $h$. So we might as well remove this from our calculation - here we get the [[Maximum a posteriori probability estimate (MAP)|maximum a posteriori probability]].

![[Maximum a posteriori probability estimate (MAP)]]

Sometimes we will have no prior preference on the [[Modelling paradigm|hypothesis space]] in this case we might as well assume it is uniform and remove it from our calculations - here we get the [[Maximum likelihood estimation (MLE)|maximum likelihood estimation]].

![[Maximum likelihood estimation (MLE)|Maximum likelihood estimation]]

Though to actually calculate these would be very hard - as the [[Modelling paradigm|hypothesis space]] might be very large.
