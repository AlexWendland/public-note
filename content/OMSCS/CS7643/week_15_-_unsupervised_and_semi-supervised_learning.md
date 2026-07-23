---
aliases:
course_code: CS7643
course_name: Deep Learning
created: '2026-07-22'
date_checked: '2026-07-22'
draft: false
last_edited: '2026-07-22'
tags:
  - OMSCS
title: Week 15 - Unsupervised and semi-supervised learning
type: lecture
week: 15
---

In this lecture we cover what we do when we have unlabelled examples.
There are different cases here:

- Self-supervised learning: We have a dataset of unlabelled examples and we want to find some structure in the data.

- Few-shot learning: We have 1-5 labeled examples per category with no unlabelled examples.

- Semi-supervised learning: We have a mix of labeled and unlabeled data and we want to establish a labeling over all the data.
Normally this would be with 10+ examples per category.

In most real-world applications you are likely in one of these settings as labeling data is financially and time-consuming.
Therefore getting good signal from a smaller amount of data is critical.

In supervised learning the setting was fairly easy - we run data through a forward pass and use a loss function to update weights via backpropagation.
However, with unlabeled data we don't have the target to run the loss against.
Therefore, we have a couple of considerations:

- Which loss function to use?

- How to optimise/train the model?

- Which architecture to use?

- Normally we want to do this for some transfer learning about a task we care about.

# Semi-supervised learning

In this case we will have a small amount of labelled data and a much larger amount of unlabelled data.

The first idea here is to use the labeled data to build a bad model, then use that bad model on the unlabelled examples to see if it is very confident on the labels of some of the unlabelled examples.
If it can predict the category to some high level confidence we then add that label as a pseudo-label.
Then we weakly augment the unlabelled data (rotations, translations, etc) and train against the augmented data with the pseudo-label.
We also strongly augment the data using RandAugment or another aggressive pixel-level transform and add it to the dataset with the pseudo-label.

![FixMatch](../../../static/images/fixmatch.png)

Whilst I have described a two stage process, it doesn't need to be!
We build a mini-batch of B labelled data (we can also weakly augment it) samples then also add in $\mu B$ unlabelled examples.
Then we train normally on the labelled examples but for the unlabelled examples we use the loss:
$$
\frac{1}{\mu B} \sum_{b=1}^{\mu B} \mathbb{I}(\max(q_b) \geq \tau ) H(\hat{q_b}, q_b)
$$
Where $\tau$ is the confidence threshold, $\hat{q_b}$ is the 1-hot embedding of the maximal class in $q_b$, and $H$ is the cross entropy loss.

> [!warning] Augmentation is required
> The reason this algorithm took quite a while to develop was doing it without augmentation didn't work well.

To give a sense of the numbers, in the original FixMatch (this algorithm) paper they used a batch size of 64 of labelled data, with $\mu = 7$, $\tau = 0.95$ and they used a cosine learning rate schedule.
The much larger batch sizes of unlabeled data is required for this to operate well - as well as the high confidence to not get noisy pseudo-labels.
Though these change based on the dataset - on ImageNet we needed a much larger batch size with a lower confidence threshold.

## Label propagation

We can use clustering algorithms to inform what labels may be - this is called label propagation and can provide a good alternative to pseudo-labels.

![Label propagation](../../../static/images/label_propagation.png)

# Few-shot learning

The general setting for few-shot learning is you have a large number of base classes with lots of data.
Then you have an additional $N$ classes for which you only have 1-5 examples - these are called the support set for these classes.
Then you have a number of 'query' sets which need to be placed in these $N$ classes.

## Transfer learning baseline

We have already talked about this kind of setting in our CNN section.
The algorithm we would do here is:

1. Train a feature extractor and classifier on the Base classes until we get a good performance.

2. Freeze the feature extractor weights and then train a new classifier on the support set for the new $N$ classes.

3. Finally, run the queries through feature extractor and new classifier to make the predictions.

This is a pretty strong baseline and actually out-performs a lot of sophisticated methods.

### Cosine similarity layer

Traditionally for the classification layer we would use a fully connected linear layer followed by softmax.
However, with so few examples we might not be able to train that accurately.
So instead we use cosine similarity.
That is for each new class we have a parameter $w_i \in \mathbb{R}^d$ where $d$ is the dimension of the feature space.
We look at the output vector from the feature extractor $f$ and calculate cosine similarity, e.g.
$$
\text{cosine similarity}(f, w_i) = \frac{f \cdot w_i}{\|f\| \|w_i\|}
$$
to each of these classes then take softmax to get the closest class.

![Cosine similarity layer](../../../static/images/cosine_similarity_layer.png)

This ends up working better than a linear layer in lots of cases.

### Cons of the baseline

The main downside to the baseline is that during the main learning stage on the base classes it does not know the existence of the real task and the $N$ classes that matter.

## Meta-training

To get around the issue with the baseline we can instead use the Base classes to help the feature extractor get good at the task it will ultimately be used for.
Here you hold out some of the base classes during training of the feature extractor and then use meta-train/test sets to improve the feature extractor on the exact task you are hoping it will do.

![Meta-training](../../../static/images/meta_training.png)

However, it has been shown the gradient descent doesn't work well when we have a small support set (i.e. 2) so instead we need to look at different ways to learn (e.g. meta-learning).
First way to do this is to take inspiration from known learning algorithms:

- kNN/kernel machine: Matching networks

- Gaussian classifier: Prototypical Networks

Otherwise we could look at how we learn - for example with gradient descent.

- Gradient descent: Meta-Learner LSTM, or

- Model-Agnostic Meta-learning MAML.

### Meta-learning: Gradient descent via LSTM

Consider the gradient descent update rule:
$$
\theta_t = \theta_{t - 1} - \alpha_t \nabla_{\theta_{t-1}} L_t
$$
This looks similar to the LSTM cell update rule:
$$
c_t = f_t \odot c_{t-1} + i_t \odot \tilde{c}_t
$$
Here we are considering $c_t$ to be the parameters $\theta_t$.
The first term $f_t$ determines how much of the previous state to forget.
The second term $i_t$ determines how much of the new state to learn $\tilde{c}_t$ (which can be compared with $-\nabla_{\theta_{t-1}} L_t$) just like $\alpha_t$.

This means we can use an LSTM model to replicate how we learn with gradient descent.
In the concept of meta-learning we can use the held out base classes to train the algorithm on how to learn the support classes and compare it to the query classes.

![Meta-learner: LSTM](../../../static/images/meta_learner_lstm.png)

### Meta-learning: Model-agnostic meta-learning

It is not clear if we need the whole of the LSTM model to make this effective.
There are other approaches that instead of learning how to learn for the one-shot exercise, just learn a good starting point for the classification network for the one-shot exercise.

![Model-agnostic meta-learning](../../../static/images/model_agnostic_meta_learning.png)

The idea here is to use the training tasks to update the initial weight for our classifier but not update the learning mechanism like we did in the LSTM case.

Due to MAML being normal gradient descent we know it will converge to a local minimum - so in practice it is much more common than the LSTM case.

# Unsupervised/self-supervised learning

In unsupervised learning there are multiple tasks we might want to perform:

- Clustering: Grouping similar data together.

- Dimension reduction: Reducing the dimensionality of the data.

- Density estimation: Estimating the density function of the data e.g. $\mathbb{P}(x)$.

The issue with unsupervised/self-supervised learning is we have no loss function to train a network with.

## Autoencoders

One of the simplest loss functions we can do is run data through a neural network to reconstruct the original data.
We can do this with an autoencoder network to learn lower dimensional embeddings of the input data.

![Unsupervised Autoencoder](../../../static/images/unsupervised_autoencoder.png)

Then we can use the low dimension embedding it creates on other tasks such as classification or clustering.

## Clustering assumption

When doing clustering we essentially make a big assumption.
High density regions form clusters whilst low density regions separate clusters which hold a coherent semantic meaning.

Therefore we can use algorithms like k-means to cluster our data.
We can then use this to generate pseudo-labels and use the pseudo-labels to train a classifier.
Then with this new classifier we can look at the lower dimensional embedding and run k-means again.
Iteratively hoping we build a good embedding of the data.

![Clustering assumption](../../../static/images/clustering_assumption.png)

This has certain fail states like assuming everything is in one cluster and not learning any representation - but there are ways to avoid this.

## Surrogate tasks

The idea here is to generate tasks we don't really care about but make a model solve.
In hopes that by doing that it learns a good embedding of the data into a space we can use for another task.
For example:

- Reconstruction: Just like the auto-encoder.

- Rotations: Train a model to predict how rotated an image is from its original form.

- Colourization: Train a neural network to add colour back to a grayscaled image.

- Relative image patch: Provide a model with two patches of an image and it needs to say how far apart and in what direction the patches are from each other.

- Instance discrimination: This uses a CNN model to encode the images - then we train a classifier that can take two such embeddings and say if they are augmented versions of the same image or different images.

- Video next frame prediction.

This method of training has shown better performance on secondary tasks such as object detection when compared to algorithms that were trained with full knowledge of the labels.
