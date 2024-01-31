---
aliases: 
checked: false
course: "[[CS6200 Introduction to Graduate Algorithms]]"
created: 2024-01-29
last_edited: 2024-01-29
publish: true
tags:
  - OMSCS
type: lecture
week: 4
---
# Week 4 - Support Vector Machines

## Linearly separable 

We are going to revisit the idea of [[Linearly separable|linearly separable]] points in the plane.

![[Linearly separable]]

Suppose we have [[Training data|training data]] $(x^t, y^t) \in \mathbb{R}^n \times \{1,-1\}$ for $t \in T$ such that $X_1 = \{x^t \vert y^t = 1\}$ and $X_2 = \{x^t \vert y^t = -1\}$ are linearly separable. This means that there exists some $w \in \mathbb{R}^n$ and $b \in \mathbb{R}$ such that
$$
y_t ( x^t \cdot w + b ) = y_t \left ( \sum_{i=1}^n x^t_i w_i + b \right ) \geq 0
$$
for every $t \in T$. 

Geometrically $w$ and $b$ represent a [[Hyperplane|hyperplane]] defined by $w$ being the [[Tangent vector|tangent vector]] and $bw$ being a point on the [[Hyperplane|hyperplane]]. 

![[SVM example]]

>[!Note] Direction of $w$
>When defining a [[Hyperplane|hyperplane]] you always have a choice of [[Tangent vector|tangent vector]] both in scaler (we will come back to that later) and direction. The direction of $w$ dictates which side of the [[Hyperplane|hyperplane]] is "positive", 
>- if $w = (1,0)$ with $b=0$ then the point $(2,3)$ lies on the "positive" side as $1 \cdot 2 + 0 \cdot 3 + 0 = 2$, whereas
>- if $w = (-1,0)$ with $b=0$ then the point $(2,3)$ lies on the "negative" side as $-1 \cdot 2 + 0 \cdot 3 + 0 = -2$.

## Best separator

When you have some points that are [[Linearly separable|linearly separable]] there might be many choices of $w$ and $b$. Though which one is the best? And what does the best mean?

Ideally we would want to choose a line that:
- [[Linearly separable|Linearly separates]] the points, whilst
- maximising the minimum distance between the points and the line.

The intuition as to why we would want this is by making our separating line the furthest away from the points it can be whilst still separating them means we are trying to avoid [[Overfitting|overfitting]] the best we can. The line is as far away from our training data as it possibly can be. 

