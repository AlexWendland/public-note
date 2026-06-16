---
aliases:
course_code: CS7643
course_name: Deep Learning
created: '2026-06-06'
date_checked: '2026-06-08'
draft: false
last_edited: '2026-06-06'
tags:
  - OMSCS
title: Week 3 - Optimization of Deep Neural Networks
type: lecture
week: 3
---

Through backpropagation we get a learning method that is generalisable to a lot of structures.
However, picking the best structure requires a lot of knowledge and intuition.
For example:

- Sometimes adding an additional layer can dramatically reduce the size of earlier layers.

- There are structures like CNNs which model real processing of photos.

- Theoretical experiments show that 'gentle' dimension reduction can lead to better performance.

The decisions we need to make are:

- Architecture of the network: How many layers, what sizes should these layers have, and which activation functions.

- Data considerations: Should we normalise the data, can we augment the current data for more samples.

- Training and optimisations: What should the start values of our parameters be, how can we stop the model getting stuck.

- Machine learning considerations: Overfitting, etc.

The decisions also depend on each other.

# Architecture considerations

There are good starting points for designing your architecture:

1. Be guided by the type of data you are using, understanding its structure can help you decide what architecture to use.

2. The literature may have good ideas about what is important about the data type you are working with, such as CNNs for pictures or transformers for sequential data.

3. Understanding the flow of gradients through different modules.

Your architecture will be a mix of linear and non-linear layers.
The linear layers have a trivial gradient - however the choice of non-linear layers can be very important.
So you should consider the following for non-linear layers:

- The min/max of the output.

- How it behaves on inputs and what you would like the output to look like.

- Gradients:

  - What is its gradient behaviour at initialisation.

  - What is the gradient at the extreme values.

- How computationally complex is it?

> [!example] Sigmoid function
> The sigmoid function is given by:
> $$
> \sigma(x) = \frac{1}{1 + e^{-x}}
> $$
> This gives us:
>
> - Min/max: 0 and 1.
> - Output is always positive.
> - It saturates at the end—that is, really large values all map to nearly the same output and really negative values also map to nearly the same output.
> - Gradients:
>   - Vanishes at the extremes, meaning those values will be slow to change.
>   - Gradient is always positive (between 0 and 0.25).
> - Computationally 'large' with the exponential value.
>
> These gradient features actually cause a lot of problems.
> The small gradient at the extremes means that it will reduce the learning in not only this layer but also all preceding layers.
> Secondly, being always positive forces the same sign on the weight updates as if we have a $h_i = W a_{i-1}$ then:
> $$
> \frac{\partial h_i}{\partial W} = a_{i-1}
> $$
> Where $a_{i-1}$ entries are always positive.
> This means when we calculate:
> $$
> \frac{\partial L}{\partial W} = a_{i-1} \frac{\partial L}{\partial h_i}
> $$
> each output neuron's incoming weights will all carry the sign of $\frac{\partial L}{\partial h_i}$, meaning all inputs to that neuron must increase or decrease together.
> This means if the optimal update requires increasing one weight and decreasing another, it cannot be done in a single gradient step and requires zig-zagging over multiple steps.

> [!example] Tanh
> The hyperbolic tangent function tanh is given by:
> $$
> \tanh(x) = \frac{e^x - e^{-x}}{e^x + e^{-x}}
> $$
> This gives us:
>
> - Min/max: -1 and 1.
> - The function is centred around 0, meaning it can flip the sign of the inputs based on this.
> - It 'saturates' at the extremes.
> - Gradients:
>   - Vanishes at both extremes.
>   - Always positive between 0 and 1.
> - Computationally expensive.
>
> This still has some of the downsides of the sigmoid function but the negative values allows for the forward pass weights to change in opposite directions.

> [!example] ReLU
> The ReLU function is given by:
> $$
> \text{ReLU}(x) = \max(0, x)
> $$
> This gives us:
>
> - Min/max: 0 and infinity.
> - The function is always positive.
> - Gradients:
>   - 0 if $x \leq 0$ (dead ReLU).
>   - 1 otherwise.
> - Computationally cheap to compute.
>
> This still has the downside of always being positive but the gradient behaviour is much nicer, allowing learning when the input values are positive.

> [!example] Leaky ReLU
> The Leaky ReLU function is given by:
> $$
> \text{Leaky ReLU}(x) = \max(\alpha x, x), \text{ where } 0 < \alpha \ll 1
> $$
>
> - Min/max: -infinity and infinity.
> - $\alpha$ is a fixed hyperparameter (the learnable version is PReLU).
> - No saturation.
> - Gradients:
>   - $\alpha$ if $x \leq 0$.
>   - 1 otherwise.
> - Computationally cheap to compute.
>
> This has the benefit of always allowing the gradient to pass through.

There is no single best activation function but some rules of thumb are:

- Start with ReLU, it has generally good performance across all problem types.

- Try to avoid sigmoid as it slows learning too much unless you need to clamp the values for some reason.

- Sometimes leaky ReLU can make a big difference at scraping a bit more accuracy on an already good model.

# Initialisation

The initial values of the weights for training influence the speed of convergence.
On the trivial side, if you start close to a good local minimum then convergence is very fast.
However, less trivially, if you start with very large parameters the activation function will be saturated at these values and learning will be slow.
In comparison, starting with small values means we utilise the maximum of the activation function's gradient.
Another non-trivial example is if the weights are all the same or carry the same sign; it is hard for it to break out of moving in lock step.

A good starting point is to initialise weights following a normal distribution $N(\mu, \sigma)$.
If we keep $\mu = 0$ and $\sigma = 0.01$ then our weights are small and uncorrelated, avoiding all the problems given in the previous paragraph.

In deeper networks this might not be sufficient.
As activation function derivatives are normally very small and these compound, the gradients get even smaller.
This leads to very small updates each step.
However, larger initialisation risks saturation so we need to balance these two factors.

Ideally we would like to keep the variance of the activations the same throughout the layers.
There is a theoretically optimal way to do this for tanh - for a layer with $n_j$ input values and $n_{j+1}$ output values we should initialise weights using:

$$
\text{Uniform}\left ( - \frac{\sqrt{6}}{\sqrt{n_j + n_{j+1}}}, \frac{\sqrt{6}}{\sqrt{n_j + n_{j+1}}} \right )
$$

Practically however, empirical data showed that:

$$
N\!\left(0,\, \frac{1}{n_j}\right)
$$

works just as well.

For different activation functions you need different analysis.
For example with ReLU we can use:

$$
N\!\left(0,\, \frac{2}{n_j}\right)
$$

In summary, initialisation matters and is influenced by the activation functions we are using.
Too small a gradient will lead to slow learning and convergence.

# Data processing

From traditional machine learning, normalisation of the data is a common practice.
For deep learning this can be done as well - here we can subtract the mean and divide by the standard deviation.
We can do this in an unconditional way.
You can also do principal component analysis (PCA) but it is uncommon to do so.

## Batch normalisation

In deep learning we can make this normalisation a layer in our network, for a mini-batch of data $\mathcal{B} = B \times D$ where $B$ is the batch size.
We can compute the mean and variance of each dimension.
Then add the following layer:

- Calculate the mean $\mu_{\mathcal{B}} = \frac{1}{B} \sum_{i=1}^B x_i$.

- Calculate the variance $\sigma_{\mathcal{B}}^2 = \frac{1}{B} \sum_{i=1}^B (x_i - \mu_{\mathcal{B}})^2$.

- Normalise the data $\hat{x_i} = \frac{x_i - \mu_{\mathcal{B}}}{\sqrt{\sigma_{\mathcal{B}}^2 + \epsilon}}$.
(Include a small $\epsilon$ to avoid divide by zero).

- Add a learnable scale and shift to the data $o_i = \gamma \hat{x_i} + \beta$.
(Where $\gamma$ and $\beta$ are learnable parameters).

This allows the network to decide how much of the scale/shift it wants to use for each dimension.
This is called batch normalisation (BN) layer.

Note that we do this per-batch this adds some complications:

- During deployment we should use the mean/variance across the whole training data.

- Batch sizes should be sufficiently large as to not make the values of $\mu$ and $\sigma$ jump around too much.

Normalisation is particularly important before non-linear layers as we would like to avoid saturation.

# Optimisation

When we are optimising we are trying to reduce the loss with respect to the parameters of our model.
This generates us a 'loss surface' where the domain is the parameter space and the target is the loss.

Traditionally it was assumed that bad local minima were the main cause for sub-optimal training performance.
However, this was found not to be the case.
With the larger issues being:

- Noisy gradient estimates: Here we are using batches of the data which might not be a fair representation of the loss surface.

- Saddle points: Points where the gradient is zero but there are directions you can move to decrease the loss still.

- Ill-conditioned loss surfaces: These are just loss surfaces that are badly behaved.

## Momentum

The issue of getting stuck in saddle points is due to us following the steepest gradient descent update method.
This means when we get stuck in a saddle point it's hard to escape.
So instead of just moving in the direction of the steepest descent we use momentum, or we keep the velocity of us moving in the last direction to try to 'ride over' saddle points.
This is implemented by adding a new velocity term:

$$
v_i = \beta v_{i-1} - \frac{\partial L}{\partial w_{i-1}}, \quad w_i = w_{i-1} + \alpha v_i
$$

Where $\beta$ is a momentum term and $\alpha$ is the learning rate.
(Velocity can sometimes absorb the learning rate $v_i = \beta v_{i-1} - \alpha \frac{\partial L}{\partial w_{i-1}}$ where $w_i = w_{i-1} + v_i$ which is an equivalent derivation.)

## Nesterov Momentum

This is a slightly different approach where we move in the direction of the velocity first and then sample the gradient.
Then we actually move in the weight space in the gradient's direction:

$$
\begin{aligned}
\hat{w}_{i-1} & = w_{i-1} + \beta v_{i-1}\\
v_i & = \beta v_{i-1} - \frac{\partial L}{\partial \hat{w}_{i-1}}\\
w_i & = w_{i-1} + \alpha v_i
\end{aligned}
$$

> [!note] Only one update to the weights
> Notice here that we throw away the weight update $\hat{w}$ and only apply the updated velocity to the real weights.

This method allows us to correct overshooting minima before we do it—if we detect that we are going to overshoot in the other direction we slow down before hitting the bottom.

## Second Order Derivatives

If we really wanted to avoid saddle points - we could try to classify minima using a second order derivative.
This is called the Hessian matrix.
However, this is computationally very expensive, so practically deep learning doesn't normally apply this.

Functionally momentum methods give us some of the advantages of knowing the Hessian without the computational complexity.

The Hessian has other theoretical properties such as telling us how bad the loss surface is.
This can be done by looking at the condition number—which is the ratio between the largest and smallest eigenvalue.
This tells us the difference between the direction that drags us the most versus the direction that drags us the least.
This is important because if we have a large gradient in one direction we are likely to 'wobble' around, changing in that direction more than the gentler direction.
This can impact training performance.

## Per-parameter learning rates

To account for different size gradients in different directions we can have a learning rate for each parameter.
This normalises the learning rate across parameters.
There are multiple algorithms that implement this:

- Adagrad,

- RMSProp, and

- Adam.

These algorithms have actually been shown to be less effective than SGD with momentum but they require a lot less tuning to get right.

### RMSProp

This is an accumulation-based method where we track an exponential moving average of squared gradients and dial down the learning rate proportional to that.

$$
\begin{aligned}
G_i & = \beta G_{i-1} + (1- \beta) \left ( \frac{\partial L}{\partial w_{i-1}} \right )^2\\
w_i &= w_{i-1} - \frac{\alpha}{\sqrt{G_i + \epsilon}} \frac{\partial L}{\partial w_{i-1}}
\end{aligned}
$$

Where $\alpha$ is the learning rate, $\beta$ is the decay factor and $\epsilon$ is a small constant.

> [!note] Adagrad
> The precursor to RMSProp, Adagrad, is the same but without the decay: $G_i = G_{i-1} + \left(\frac{\partial L}{\partial w_{i-1}}\right)^2$.
> Because $G_i$ grows forever, the learning rate shrinks to near zero over long training — RMSProp's decay fixes this.

### Adam

We can combine RMSProp with momentum to get a fairly popular update method.

$$
\begin{aligned}
v_i & = \beta_1 v_{i-1} - (1 - \beta_1) \frac{\partial L}{\partial w_{i-1}}\\
\hat{v}_i & = \frac{v_i}{1 - \beta_1^t}\\
G_i & = \beta_2 G_{i-1} + (1- \beta_2) \left ( \frac{\partial L}{\partial w_{i-1}} \right )^2\\
\hat{G}_i & = \frac{G_i}{1 - \beta_2^t}\\
w_i &= w_{i-1} + \frac{\alpha \hat{v}_i}{\sqrt{\hat{G}_i + \epsilon}}
\end{aligned}
$$

Where here $t$ is the iteration number.
We define the hatted versions of $v$ and $G$ to account for the small start up values of these terms.
As $t$ increases this becomes less important but starting off it gives these terms a little boost.

## Learning rate tuning

Whilst we have these fancy methods to evolve the learning rate, a lot of the time we use more basic methods.

- Use a graduate student!

- Step scheduler: Decide a step size and decrease it on that schedule.

- Exponential scheduler: Exponentially decrease the learning rate, starting off with very small decay.

- Cosine scheduler: Recently, cyclic schedulers have gotten attention as a good way to avoid bad local minima.

# Regularisation

Regularisation is a way to prevent overfitting.
We increase the loss function based on the size of the parameters of our model.

> [!definition] L1 Regularisation
> Assuming we have some standard loss function $L$ then we add L1 regularisation using:
> $$
> L_{L1}(W) = L(x, y, W) + \lambda \vert W \vert
> $$

> [!definition] L2 Regularisation
> Assuming we have some standard loss function $L$ then we add L2 regularisation using:
> $$
> L_{L2}(W) = L(x, y, W) + \lambda \vert W \vert^2
> $$

> [!definition] Elastic Net Regularisation
> Assuming we have some standard loss function $L$ then we add elastic net regularisation using:
> $$
> L_{EN}(W) = L(x, y, W) + \alpha \vert W \vert + \beta \vert W \vert^2
> $$

L1 regularisation in particular tends to induce sparsity — forcing most weights to zero and concentrating signal in a small number of high-impact weights.
L2 regularisation instead penalises large weights evenly, keeping them small but not sparse.
Both are particularly important in deep learning where we have lots of parameters.

## Dropout regularisation

Weight-based regularisations don't stop the model relying heavily on one feature to determine the outcome.
This is not explicitly stopped by requiring lower weight values.
Therefore, we instead can use a technique called dropout.

The basic idea is we will block certain neurons on each layer whilst we train over one batch.
This means these will get zero value and not carry the gradient back.
We change the set that get blocked each training batch.
This ensures we can't rely too heavily on any part of the network for our discrimination—ensuring an evenly utilised network.

This does come with a slight downside though—when we test we use all neurons so the total activation at each output is increased.
To accommodate this we can either scale down the weights at test time or during the training we can do it.
Functionally this is done by keeping the ratio of neurons dropped out fixed.

# Data augmentation

Deep learning requires a lot of data - which sometimes is hard to obtain.
However, we can fully utilise our data by augmenting it to make more.

In the example of images we could:

- Rotate the image,

- Reflect the image,

- Flip the image,

- Crop the image,

- Add noise to the image,

- Crop small parts of the image out, or

- You could even mix two images together and provide the proportion as the target vector.

This forces our models to be robust and avoid over fitting on the data.

# Process of training

Training a network is hard and requires constant monitoring.
Therefore it is useful to print out a lot of data to check what is happening as it trains.

- Loss and accuracy curves.

- Gradient statistics/characteristics.

- Other aspects of the computational graph.

## Loss

When observing the loss curves you can make two fairly concrete observations:

- If it is decreasing too slowly, your learning rate is likely too low.

- If the loss goes back up—then your learning rate is too large.

You should also always plot both the training and validation losses to check for overfitting of the model.
Though this can also check for underfitting, where they stay very close together; in this case your model might not be expressive enough.

Normally the loss function is not really what you care about—it will be instead some other metric.
Sometimes the relationship between the loss and the metric you really care about can be complicated and may require you to reevaluate the loss function.

## Hyperparameter tuning

You should always tune your hyper-parameters and should not expect your first run to be very good.
However, certain hyper-parameters are more important than others.
Key parameters are learning rate and weight decay whereas momentum is more stable and we can just use a good default.

The best way to approach this is to do a coarse search of the space—then zero in on a 'fruitful' selection of parameters.
There are automated methods to tune hyperparameters, but normally these are not as efficient as just thinking about it yourself.

> [!warning] Hyperparameters are not independent
> Hyperparameters are not independent, therefore you can't tune a single one and then move on to the next.
> You need to tune all of them together.

