---
aliases:
course_code: CS7643
course_name: Deep Learning
created: '2026-06-08'
date_checked:
draft: false
last_edited: 2026-06-16
tags:
  - OMSCS
title: Week 4 - Convolution and Pooling Layers
type: lecture
week: 4
---

Convolution and pooling layers make up Convolutional Neural Networks (CNNs).
These have been shown to have significant improvements for tasks such as image recognition but also wider use outside of it.

# Convolution layers

One of the main drivers for not using fully connected layers in image processing is the size of that input.
They usually consist of 3 channels; red, green, and blue.
With each of these layers being height x width large - which can get very large: $3 \cdot H \cdot W$.
Therefore, we want to perform dimension reduction on it but preserving 'features' of the image.

We consider $K_1 \times K_2$ window (image patch/receptive field) of the image and look for a feature.
This uses $3 \cdot K_1 \cdot K_2 + 1$ (+1 for the bias) variables (what we will call the kernel) but we can use this same set of variables for many windows into the image.
This is because a feature such as an edge or a beak has the same chance of appearing in the top left as in the middle of an image.
So there is no need to train different variables for each receptive field we consider.
Note that this only takes $3 \cdot K_1 \cdot K_2 + 1$ variables instead of $3 \cdot H \cdot W$.
(Below we will just pretend there is only a single channel - but in reality we just expand the kernel up to encompass all 3 channels).
In fact, we can do this for multiple different types of features where we have different parameters.

> [!note] Convolution of functions
> For two functions $f(x)$ and $g(x)$ - their convolution is:
> $$(f \ast g)(x) = \int_{t \in D} f(t) g(x-t) dt$$
> This is a way to multiply two functions across their joint domain.

The way convolution relates to our setting is then $g(x)$ is our image and $f(x)$ is our kernel.
By multiplying the kernel by the receptive field and summing up - we are doing the discrete analogy of an integral.
More concretely if we let the image be $g(x,y)$ and the kernel be $k(x,y)$ - then our output layer is given by:

$$
o(x,y) = \sum_{a = 0}^{K_1 - 1} \sum_{b=0}^{K_2 - 1} k(a,b) g(x - a, y - b)
$$

However, you will notice in the convolution we use $g(x-t)$ which acts as a kind of 'flip'.
Whilst this is included in the convolution with the kernel, since the kernel weights are learned, the flip makes no practical difference — the model can just as easily learn the flipped kernel. If we remove it we get what is called cross-correlation.

$$
o(x,y) = \sum_{a = 0}^{K_1 - 1} \sum_{b=0}^{K_2 - 1} k(a,b) g(x + a, y + b)
$$

> [!note] Cross-correlation
> There is a notion similar to convolution called cross-correlation.
> The duality of it and convolution applies to our setting as well.
> The cross-correlation of two functions $f(x)$ and $g(x)$ is:
> $$(f \star g)(x) = \int_{t \in D} f(t) g(x+t) dt$$
> The graphical analogy is the same as convolution but without one flip.

However, when we perform back propagation the gradient w.r.t. the input involves convolving the upstream gradient with the flipped kernel — recovering the true convolution operation.

There are some differences in the deep learning setting - we normally have multiple channels.
In our case we call the output function the 'feature map'.
We also will add a bias term to the kernel.

As we are multiplying a $K_1 \times K_2$ grid along a $H \times W$ grid we get $(H - K_1 + 1) \times (W - K_2 + 1)$ output.
This is assuming we use a 'stride' of 1 - i.e. we move one in either direction.
We can increase the size of this stride to get a smaller output.
We can also 'pad' the image around the outside to get readings on the edges - this padding method could use zeros or contain some kind of image copy or reflection.
Both these changes will change the size of the output - the padding increasing it and the stride decreasing it.

Normally we will not just use a single feature but instead use multiple features.
In PyTorch this is expressed as the number of 'output channels'.
In this we use different initial values and biases for each feature and they do not share the same values.
This usually means they converge onto different features.

Computationally, to perform this we actually choose to vectorise the operation (known as im2col).
By that we mean turn the image patches into rows in a matrix.
Similarly, we turn the kernels into columns of the weight matrix.

# Pooling layers

We said at the start of this lecture the issue with using fully-connected layers on images is the size of the image.
Whilst the convolution layers extract features - they are not best placed to reduce the dimension of the image.
So instead we use pooling layers to reduce the size.

In short, a pooling layer takes an aggregation operation like max, mean, median, etc. and applies it in a similar way to convolution.
Here we can use stride length and padding once again.
In comparison to convolution layers - this uses no parameters as the aggregation functions are not parameterised.

The most common pooling operation is max pooling.
Sometimes these layers are actually gotten rid of and dimension reduction is done by the convolution layers.

Convolution layers give us **translation equivariance** — if a feature moves in the input, it moves correspondingly in the output (we are preserving the position of features).
Max pooling then gives us **approximate translation invariance** — a feature like an edge or a beak can shift a little within the image, but if that shift falls within the pooling window the max value is unchanged and the output looks identical.
Together these properties mean the network is sensitive to *what* features are present but robust to small changes in *where* they appear.

