---
aliases:
course_code: CS7643
course_name: Deep Learning
created: '2026-06-30'
date_checked:
draft: true
last_edited: '2026-06-30'
tags:
  - OMSCS
title: Week 9 - Language models
type: lecture
week: 9
---

The general problem of language models is to predict the probability of a sentence of words.
For example:

$$
\mathbb{P}(\text{The dog barked at the cat})
$$

We do this generally by breaking the sentence down into words and using conditional probability:

$$
\mathbb{P}(w_1 w_2 \ldots w_n) = \prod_{i=1}^{n} \mathbb{P}(w_i \vert w_{i-1}, w_{i-2}, \ldots w_1 )
$$

This has lots of applications, such as:

1. Text completion: Given the current sentence what is the next most likely word.

2. Audio transcription: If a word is missing in a sequence what is the most likely word to fill it.

We can in fact extend this model to take in other context $c$.

# Recurrent neural networks

Recurrent neural networks enable our models to handle sequences as inputs.
In our examples these might be sequences of words, or letters but there are applications outside of natural language processing.

The issues with handling sequences of inputs is we need a model that can handle variable length input.
To do this we change the design of our model so that it takes as input a state $h_{t-1}$ and the new word $x_t$ then outputs a new state $h_t$.

![Recurrent neural network](../../../static/images/rnns.png)

This is expressed as $f_{\theta}$ where $h_t = f_{\theta}(h_{t-1}, x_t)$.

> [!note] Recurrent neural networks
> When people talk about RNN's they normally mean this model.
> However, some people in the literature mean any network that is not a DAG when it comes to inputs/outputs.

These networks provide a problem when running back propagation - as now the training data is sequences of words but the network takes this state variable.
However, to carry out backpropogation we just 'unroll' the network.
E.g.
$$
f_{\theta}(x_1 x_2 \ldots x_n) = f_{\theta}(x_n, f_{\theta}(x_{n-1}, f_{\theta}(x_{n-2}, \ldots f_{\theta}(x_1, 0))))
$$
For very long inputs this can make the back-propagation really long also - so sometimes we use 'truncated back propagation through time' where we instead only back propogate for a fixed number of time steps and cut it short at that point.

RNN's are 'two headed' they have a forward mode which is only about updating the hidden state $h_t$, but they also can be used to output $y_t$.
The output $y_t$ depends on the hidden state $h_t$ and can be calculated at all steps or only a given one.
It is usual that we run the model in 'forward mode' through the whole input and only call the output at the end.

> [!example] "Vanilla" (Elman) RNN
> This is the simplest RNN model, where we use an affine combination of the input vectors with a bais term with an activation function to generate another state.
> $$ h_t = f_{\theta}(h_{t-1}, x_t) = \sigma_{\theta}(U_{\theta} x_t + V_{\theta} h_{t-1} + a_{\theta}) $$
> To get the output of the network we apply another transformation.
> $$ y_t = \sigma_{\text{out}}(W_{\text{out}} h_t + \beta_{\text{out}}) $$
> Where the activation functions are typical logistic functions, or tanh.

The gradient presents an issue due to the vanishing/exploding gradient problem.
That is as the series size gets longer the gradient goes to zero in infinity!
For example consider a simple update function
$$f_{\theta}(x_t, h_{t-1}) = W_{\theta}(x_t + h_{t-1})$$
When considering the derivative
$$\frac{\partial h_t}{\partial x_0} = W_{\theta}^t$$
Now if $\vert W_{\theta} \vert > 1$ we have this gradient diverge whereas if $\vert W_{\theta} \vert < 1$ it converges to zero.

# Long short-term memory

A model was proposed to get around the issue of the vanishing/exploding gradient problem.
This was called the long short-term memory model - which can train itself to forget information in the past.
Here we introduce 5 new terms:

- Forget gate $f_t$: This is a gate that decides what to forget.

- Input gate $i_t$: This is a gate that decides what to input.

- Candidate update $u_t$: This is the update that is used to update the state.

- Output gate $o_t$: This is a gate that decides what to output.

- Cell state $c_t$: This is the state of the cell.

These gates are all calculated using:

$$
\begin{bmatrix} f_t \\ i_t \\ u_t \\ o_t \end{bmatrix} = \begin{bmatrix} \sigma \\ \sigma \\ \tanh \\ \sigma \end{bmatrix}(\begin{bmatrix} W_{f} \\ W_{i} \\ W_{u} \\ W_{o} \end{bmatrix} \left ( W_{theta} \begin{bmatrix} x_t \\ h_{t-1} \\ \end{bmatrix} + b_{\theta} \right )
$$

(Note here that $\sigma$ is the sigmoid function.)
These are then used to update the cell state $c_t$ and hidden state $h_t$ as follows:

$$
\begin{align}
c_t &= f_t c_{t-1} + i_t u_t \\
h_t &= o_t \tanh(c_t)
\end{align}
$$

# RNNs as language models

First to go from words to something a model will understand we take a 1-hot embedding of our words.
This means we pick an underlying vocabulary of words $W$ and then embed a particular word a unit vector with a single non-zero entry.

Now we have a sequence of words can be a sequence of vectors.
We can use these as inputs to our RNN.
Note that we can know use the model in forward mode along our sequence before we get it to output the prediction of the next word in a sequence.

## Evaluation

It is common in machine learning to use cross-entropy for our loss function.
Suppose we have two probability distributions $p, p^{\ast}$ over state $\mathcal{X}$ then this is defined as:

$$
H(p^{\ast}, p) = -\sum_{x \in \mathcal{X}} p^{\ast}(x) \log p(x)
$$

In the NLP setting we can extend this to the 'per-word cross-entropy':

$$
H(s) = - \frac{1}{N} \sum_{i=1}^N \log p(w_i \vert w_{i-1}, \ldots )
$$

This is commonly used as a loss function for language models.
Another quantity that could be used for this is the perplexity:

$$
\begin{align}
\text{Perplexity}(s) &= \prod_{i=1}^N \root{N}{\frac{1}{\mathbb{P}(w_i \vert w_{i-1}, \ldots)}}\\
&= b^{- \frac{1}{N} \sum_{i=1}^N \log_b \mathbb{P}(w_i \vert w_{i-1}, \ldots)}
&= b^{H(s)}
$$

This is tied to per-word cross-entropy as laid out above.
The lower the perplexity the better.

## Training

To train a RNN language model, we use the input data but run it both in forward and output mode.
Then we can compare the output of each step to the next word to get the loss (after applying softmax).
Then the loss of the whole model is simply the average loss across the whole text.

# Transformer encoder

A transformer encoder is an alternative to the RNN for producing contextualised representations of a sequence.
Rather than processing tokens one at a time and compressing history into a hidden state, it processes all tokens simultaneously using self-attention — i.e., the non-local layer idea from week 8 applied to the full sequence.

For an input sequence of $n$ token embeddings $X \in \mathbb{R}^{n \times d}$, each layer computes:

$$
\text{Attention}(Q, K, V) = \text{softmax}\!\left(\frac{QK^T}{\sqrt{d_k}}\right)V, \quad Q = XW_Q,\ K = XW_K,\ V = XW_V
$$

Each token attends directly to every other token, so there is no sequential bottleneck and no vanishing gradient over long distances.
This also means the computation is fully parallelisable across the sequence — a major practical advantage over RNNs.

Since attention is order-agnostic, **positional encodings** are added to the token embeddings to inject sequence order.
These can be fixed (sinusoidal) or learned, and they are what determines the model's **context window**: the maximum $n$ the model was trained with.
Extending beyond this degrades performance because the model has never seen those positions.

> [!note] Comparison with RNNs
> | | RNN | Transformer encoder |
> |---|---|---|
> | Neighborhood | Previous hidden state only | All tokens (via attention) |
> | Long-range dependencies | Hard (vanishing gradient) | Direct — O(1) path between any two tokens |
> | Parallelism | Sequential | Fully parallel |
> | State | Fixed-size hidden vector | Full sequence of vectors |

# Masked language models

We can use a transformer to learn 'ideas' about the language.
One technique here is masked language modeling where we hide certain words and get it to output predictions of what each mask is.
For it to be able to do this, we add to the input symbols the 'position' of that symbol within the word.
Whilst this task in itself is not useful we can still use the learning this model has done for other tasks using transfer learning.

![Masked language model](../../../static/images/masked_language_models.png)

There are a couple interesting tasks we can transfer this model onto doing:

- Token-level tasks: Predicting what each token is, for example if it is a date, location or a persons name.

- Cross-lingual tasks: Translating between languages.

- Natural language inference: Given a sentence and a question, predict the answer to the question.

These models tend to be massive in size.
This means they can be very expensive to train and run - however we can 'pass their knowledge on' to smaller models using a teacher-student.
Here we use the predictions of the teacher to act as the loss function for the student.
This technique is called 'knowledge distillation' and works very well - but it is still an open research question as to why.

![Knowledge distillation](../../../static/images/knowledge_distillation.png)

One of the explanations on why this is so powerful is because not only can the teacher say the correct answer they can also pass on their probabilities of other words that might be similar.
