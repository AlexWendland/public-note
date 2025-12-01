---
aliases:
checked: false
created: 2024-01-17
draft: false
last_edited: 2024-01-17
tags:
  - machine-learning
type: method
---
# Calculate polynomial regression coefficients for MSE

To demonstrate the calculation of the coefficients for [[Polynomial regression|polynomial regression]] with [[Mean squared error (MSE)|MSE]] suppose we have 1-dimensional input $A$ and [[Training data|training data]] $(x_i, y_i)$. For an order $k$ polynomial we are looking for coefficients $c_j$ for $0 \leq j \leq k$ that roughly do the following
$$
\left( \begin{array}
\ 1 & x_1 & x_1^2 & \ldots & x_1^k\\
1 & x_2 & x_2^2 & \ldots & x_2^k\\
\vdots & \vdots & \vdots & \ddots & \vdots\\
1 & x_n & x_n^2 & \ldots & x_n^k
\\\end{array} \right)
\left( \begin{array}
\ c_1\\
c_2\\
\vdots\\
c_k
\\\end{array} \right) \approx
\left( \begin{array}
\ y_1\\
y_2\\
\vdots\\
y_n
\\\end{array} \right), \ \ \ \ \mbox{we call this} \ \ \ \ X C \approx Y
$$
in a completely not mathematically sound way we can do the following rearrangement
$$
\begin{align*}
XC & \approx Y\\
X^TX C & \approx X^TY & \mbox{this makes } X^TX \mbox{ square}\\
(X^TX)^{-1}(X^TX) C & \approx (X^TX)^{-1} X^TY & \mbox{assuming } (X^TX)^{-1} \mbox{ is invertable}\\
C & \approx (X^TX)^{-1} X^TY
\end{align*}
$$
completing our fuzzy maths. We use this as our definition of $C$ and moreover this has some nice properties that actually minimises $C$ with respect to [[Mean squared error (MSE)|MSE]]. This can expand out to be multi-variate by increasing the size of $X$ and $C$ respectively.
