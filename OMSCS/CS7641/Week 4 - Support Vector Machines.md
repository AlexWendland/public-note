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

![[Dot product]]

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

## Margin

Suppose we have a linear separator defined by $w$ and $b$. Once again set $X_1 = \{x^t \vert y^t = 1\}$ and $X_2 = \{x^t \vert y^t = -1\}$ for our training data $T$. It is useful to have a concept for the minimum distance from a point in $X_1 \cup X_2$ to the hyperplane $H = (w, b)$.

![[Margin for a linear separator]]


## Calculating the best $w$ and $b$

Let $x_1 \in X_1$ and $x_2 \in X_2$ be the points such that
$$
x_1 \cdot w + b = \min_{x \in X_1} x \cdot w + b, \mbox{ and } \ x_2 \cdot w + b = \max_{x \in X_2} x \cdot w + b
$$
i.e. these are the positive and negative points that are closest to the line. If we have chosen $b$ optimally we would have that
$$
x_1 \cdot w + b = - \left ( x_2 \cdot w + b \right).
$$
The distance between the [[Hyperplane|hyperplanes]] defined by $H_1 = (x_1, w)$ and $H_2 = (x_2, w)$ is given by
$$
x_1 \cdot \frac{w}{\vert \vert w \vert \vert} - x_2 \cdot \frac{w}{\vert \vert w \vert \vert} = \frac{(x_1 - x_2) \cdot w}{\vert \vert w \vert \vert}.
$$
This gives the margin to be
$$\rho = \frac{(x_1 - x_2) \cdot w}{2 \vert \vert w \vert \vert}.$$
So to pick the best $w$ and $b$ we will need to maximise $\rho$. However notice we can always scale $w$ so that
$$
x_1 \cdot w + b = - \left ( x_2 \cdot w + b \right) = 1.
$$
Therefore if we make the [[Linearly separable|linearly separable]] constraint that
$$
y^t \left ( \sum_{i=1}^n x^t_i w_i + b \right ) \geq 1
$$
to maximise $\rho$ is the same as
$$
\max \frac{(x_1 - x_2) \cdot w}{2 \vert \vert w \vert \vert} = \max \frac{(x_1 \cdot w + b) - (x_2 \cdot w + b))}{2 \vert \vert w \vert \vert} = \max \frac{1}{\vert \vert w \vert \vert}.
$$
Therefore we now have an optimisation problem.

For [[Linearly separable|linearly separable]] $(x^t, y^t) \in \mathbb{R}^n \times \{-1,1\}$ find $w \in \mathbb{R}^n$ and $b \in \mathbb{R}$ where $\max_{w, b} \frac{1}{\vert \vert w \vert \vert}$ such that
$$
y^t \left ( \sum_{i=1}^n x^t_i w_i + b \right ) \geq 1, \mbox{ for all } t \in T.
$$
>[!note] Support vectors
>Training points $x^t$ where
>$$\vert w \cdot x^t \vert = 1$$
>are called support vectors. As they constrain the [[Hyperplane|hyperplane]] $(w, b)$.
## Back to reality

Our training data is nearly never [[Linearly separable|linearly separable]] so how can we adapt what we have to handle this?

Instead of enforcing 
$$
y^t \left ( \sum_{i=1}^n x^t_i w_i + b \right ) \geq 1, \mbox{ for all } t \in T.
$$
we allow some error $\zeta_t$ and we want to minimise it.

For training data $(x^t, y^t) \in \mathbb{R}^n \times \{-1,1\}$ find $w \in \mathbb{R}^n$ and $b \in \mathbb{R}$ where 
$$\min_{w, b, \zeta} \frac{1}{2}\vert \vert w \vert \vert^2 + C \sum_{t \in T} \zeta_t$$
such that
$$
y^t \left ( \sum_{i=1}^n x^t_i w_i + b \right ) \geq 1 - \zeta_t \ \mbox{ and } \zeta_t \geq 0, \mbox{ for all } t \in T.
$$

>[!Note] Switched max for min
>We transformed the maximisation problem of $\frac{1}{\vert \vert W \vert \vert}$ to a minimisation of $\frac{1}{2} \vert \vert w \vert \vert^2$. I don't really know why they add the half, I think they square it to get rid of the square root in the modulus. 

We have added a trade off parameter $C \in \mathbb{R}$ do we care more about a tight fit or a lower error term. 

## Here comes the magic

This is apparently a [[Quadratic programming problem|quadratic programming problem]] and can be transformed to the  "Dual Optimization Problem" which is as follows
$$ \max_{\alpha} \sum_{t \in T} \alpha_t - \frac{1}{2} \sum_{t,s \in T} \alpha_t \alpha_s y^t y^s (x^t \cdot x^s)$$ such that
$$ \alpha_t \geq 0 \mbox{ for all } t \in T, \mbox{ and } \sum_{t \in T} \alpha_ty^t = 0.$$
Which we turn this into a classifier by setting:
$$
\hat{f}(x) = \mbox{sgn}\left ( \sum_{t \in T} \alpha_t y^t (x^t \cdot x) + b \right )$$
where 
$$
b = y^s - \sum_{t \in T} \alpha_t y^t (x^t \cdot x^s), \mbox{ for any } s \in T \mbox{ such that } \alpha^s \not = 0.
$$
The form should remind you of [[Boosting]] where we take an average of lots of different views on the data. However in reality lots of these $\alpha_t = 0$ if they are not the support vectors closest to the line. So it might be more correct to think of this as close to [[k-nearest neighbour|KNN]].

## Kernel methods

In reality data could be far from linearly separable. 


