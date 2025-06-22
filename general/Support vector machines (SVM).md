---
aliases:
  - SVM
  - support vector machines
  - SVMs
checked: false
created: 2024-02-02
last_edited: 2024-02-02
draft: false
tags:
  - programming
type: algorithm
---
# Support Vector Machines (SVM)

Support Vector Machines operate using the [[Modelling framework|modelling framework]] to try to [[Linearly separable|linearly separate]] data points. Suppose we have some [[Training data|training data]] $T \subset A \times B$. This utilises the [[Kernel trick|kernel trick]] to change the topology of the feature space of our data whilst still keeping the computation relatively simple. Let $K: A \times A \rightarrow \mathbb{R}$ represent such a kernel. Then we solve the following optimisation problem
$$ \max_{\alpha} \sum_{t \in T} \alpha_t - \frac{1}{2} \sum_{t,s \in T} \alpha_t \alpha_s y^t y^s K(x^t, x^s)$$ such that
$$ \alpha_t \geq 0 \mbox{ for all } t \in T, \mbox{ and } \sum_{t \in T} \alpha_ty^t = 0.$$
Which we turn this into a classifier by setting:
$$
\hat{f}(x) = \mbox{sgn}\left ( \sum_{t \in T} \alpha_t y^t K(x^t \cdot x) + b^t \right )$$
where 
$$
b^s = y^s - \sum_{t \in T} \alpha_t y^t K(x^t, x^s), \mbox{ for any } s \in T \mbox{ such that } \alpha^s \not = 0.
$$
Note that $K$ needs to obey [[Mercer’s condition]] for the underlying mapping of the feature space to exist.

## Run time

The complexity of the kernel function can add large overhead to the run time for training this model.

## Correctness

The accuracy of this model highly depends on the choice of the kernel function. This definition of similarity between two vectors. 