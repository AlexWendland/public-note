---
aliases:
checked: false
course: CS7641 Machine Learning
created: 2024-01-17
draft: false
last_edited: 2024-01-17
tags:
  - OMSCS
title: Week 2 - Regression and classification
type: lecture
week: 2
---
 Regression history

[Regression problems](../../general/regression_problems.md)

The name comes from [regression to the mean](../../general/regression_to_the_mean.md), this was the technique they used to first talk about it - then the word regression for the technique stuck.

 Polynomial Regression

[Polynomial regression](../../general/polynomial_regression.md)

Once we have an [objective function](../../general/objective_function.md) we can use training data to fit the parameters $c_{p}$.

Note that [linear regression](../../general/linear_regression.md) is [polynomial regression](../../general/polynomial_regression.md) but where $k=1$.

[linear regression](../../general/linear_regression.md)

# Polynomial regression using [MSE](../../general/mean_squared_error_(mse).md)

[MSE](../../general/mean_squared_error_(mse).md)

[Calculate polynomial regression coefficients for MSE](../../general/calculate_polynomial_regression_coefficients_for_mse.md)

# Picking a degree

Below is an example of [polynomial regression](../../general/polynomial_regression.md) done on different degree polynomials.

![Polynomial Regression Example](../../../images/polynomial_regression_example.png)

As we increase the degree the fitting polynomial, the fit to the points we are training on gets better. However, at a point the utility of the curve outside of these points gets less.

This is easy to see by eye but how can we computationally infer this?

# Cross validation

[Cross validation](../../general/cross_validation.md)

![Cross Validation Example](../../../images/cross_validation_example.png)

When using cross validation to assess the accuracy of our fit in the example before, you can see it agrees with our intuition. Whilst the high order approximations are a closer fit for the [training data](../../general/training_data.md), they are a worse fit for the [test data](../../general/testing_data.md). Therefore we could use [cross validation](../../general/cross_validation.md) to pick the best polynomial without breaking the integrity of the [testing data](../../general/testing_data.md).

Generally you need to find the right sweet spot between [underfitting](../../general/underfitting.md) and [overfitting](../../general/overfitting.md) by varying the degree of the polynomial.

![Getting the right fit](../../../images/excalidraw/Getting_the_right_fit.excalidraw.svg)

[Transforming discrete input for regression](../../general/transforming_discrete_input_for_regression.md)
