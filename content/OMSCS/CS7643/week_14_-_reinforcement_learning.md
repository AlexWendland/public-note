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
title: Week 14 - Reinforcement Learning
type: lecture
week: 14
---

The model for reinforcement learning is slightly different from that of supervised/unsupervised learning.
We have an agent who can take actions in an environment and at some time may receive a reward.

![reinforcement learning](../../../static/images/rl_setup.png)

To learn it doesn't have previous data - instead it normally interacts with the environment it needs to learn in.

Two dynamics that make RL difficult are:

- Sequential decisions: It needs to plan and execute actions over a sequence of states where the reward may be delayed.

- Evaluative feedback: It doesn't know which actions directly led to a positive or negative reward, just that it got it.

These difficulties are:

- Evaluative feedback: Need trial and error to find the right action.


- Delayed feedback: Actions may not lead to immediate reward.

- Non-stationary: Data distributions of visited states change when the policy changes.

- Fleeting nature: Actions you make once might not happen again or matter later on.

We will use the following notation:

At each time step $t$ the agent receives observation $o_t$ and creates action $a_t$.
The environment receives action $a_t$, then updates the observation to $o_{t+1}$ and emits a reward $r_{t+1}$.

# Markov Decision Process (MDP)

We can express RL problems in a MDP framework.
This includes:

- $S$: Set of all possible states.

- $A$: Set of possible actions.

- $R: S \times A \times S \rightarrow \mathbb{R}$: Reward function.

- $T: S \times A \times S \rightarrow \mathbb{R}$: Transition probability function (probability distribution across $(s,a,-)$.

- $\gamma \in [0,1]$: Discount factor.

Then any game is an *interaction trajectory*, which is a sequence of tuples $\{(r_t, s_t, a_t)\}_{t \in \mathbb{N}}$ where the agent gets reward $r_t$, then sees state $s_t$ and takes action $a_t$.
This is a Markov decision process as we assume the current state is all we need to make a decision.

## Policy

In most RL cases we assume that the reward and transition probabilities are not known. However, it can be informative to work out how to solve problems if you did know them.

We will work with *policies* — a probability distribution $\pi: S \times A \rightarrow [0,1]$ where $\pi(s,a)$ is the probability of taking action $a$ when in state $s$.
This can be deterministic where there is only one action you take with probability 1 for each state or stochastic where that is not the case.
To define a 'good policy' we need to decide if we want to maximise the next reward or future rewards.
To do this we use the discount factor $\gamma$ to exponentially weight future rewards.
This enables us to define the optimum policy:
$$
\pi^*(s) = \text{arg}\max_{\pi} \mathbb{E} \left [ \sum_{t \geq 0} \gamma^t r_t \vert \pi \right ]
$$
In other words pick the best policy to maximise the expected rewards where each future reward is discounted by $\gamma^t$ for time step $t$.
This means $\gamma$ encodes whether our agent prefers short term rewards over long term rewards.

## State value function

We define the state value function as the value of a state over the future rewards $V: S \rightarrow \mathbb{R}$.
This depends on a policy $\pi$ and can be defined as:
$$
V^{\pi}(s) = \mathbb{E}\left [ \sum_{t \geq 0} \gamma^t r_t \vert s_0 = s, \pi \right ]
$$
We have an optimal state value function defined as $V^* = V^{\pi^*}$.

## State-action value (Q-function)

We define the state-action value function as the value of a state-action pair $\langle s, a \rangle$ over the future rewards $Q: S \times A \rightarrow \mathbb{R}$.
This depends on a policy $\pi$ and can be defined as:
$$
Q^{\pi}(s,a) = \mathbb{E}\left [ \sum_{t \geq 0} \gamma^t r_t \vert s_0 = s, a_0 = a, \pi \right ]
$$
We have an optimal state action value function defined as $Q^* = Q^{\pi^*}$.

## Interactions

The optimal policy, value function and Q function can all be defined from one another.
$$
V^*(s) = \max_{a \in A} Q^*(s,a), \qquad \pi^*(s) = \text{arg}\max_{a \in A} Q^*(s,a).
$$
This enables us to recursively expand the $Q$ function.
$$
\begin{aligned}
Q^*(s,a) & = \mathbb{E}_{\substack{a_t \sim \pi^*(\cdot \vert s_t) \\ s_{t+1} \sim p(\cdot \vert s_t, a_t)}} \left [ \sum_{t \geq 0} \gamma^t r(s_t, a_t) \vert s_0 = s, a_0 = a \right ] \\
& = \gamma^0 r(s,a) + \mathbb{E}_{s' \sim p(\cdot \vert s,a)} \left [ \gamma \mathbb{E}_{\substack{a_t \sim \pi^*(\cdot \vert s_t) \\ s_{t+1} \sim p(\cdot \vert s_t, a_t)}} \left [ \sum_{t \geq 0} \gamma^t r(s_t, a_t) \vert s_1 = s' \right ] \right ] \\
& = \mathbb{E}_{s' \sim p(\cdot \vert s, a)} \left [ r(s,a) + \gamma V^*(s') \right ] \\
& = \sum_{s'} p(s' \vert s, a) \left [r(s,a) + \gamma V^*(s') \right ] \\
& = \sum_{s'} p(s' \vert s, a) \left [r(s,a) + \gamma \max_{a'} Q^*(s',a') \right ]
\end{aligned}
$$
You can do the same for $V^*(s)$ as well.
$$
V^*(s) = \max_{a \in A} \sum_{s' \in S} p(s' \vert s,a) \left [ r(s,a) + \gamma V^*(s') \right ]
$$
These are called the Bellman equations.

## Value iteration

Using the Bellman equations we can derive an algorithm for finding an optimal value function.

```pseudocode
1. Initialize V^*(s) = 0 for all states s.
2. While not converged:
2.1. For each state s:
  V^{i+1}(s) = max_a \sum_s' p(s' | s,a) [ r(s,a) + yV^{i}(s')]
3. Return $V^*(s)$
```

You can do the same for Q-function

```pseudocode
1. Initialize Q^*(s,a) = 0 for all states $s$.
2. While not converged:
2.1. For each state s and action a:
  Q^{i+1}(s,a) = \sum_s' p(s' | s,a) [ r(s,a) + y max_a' Q^{i}(s',a')]
3. Return $Q^*(s,a)$
```

## Policy iteration

We can use a similar idea to iterate on an optimal policy.

```pseudocode
1. Initialize pi^*(s) = a for a random action a.
2. While pi^* has not converged:
2.1. Evaluate V^pi iteratively (policy evaluation, not maximisation):
    V^{i+1}(s) = \sum_a pi(s,a) \sum_s' p(s' | s,a) [ r(s,a) + yV^{i}(s')]
2.2. Update pi to use new value function:
    pi^{i+1}(s) = argmax_a sum_s' p(s' | s,a) [r(s,a) + y V^{i}(s') ]
3. Return pi^*
```

Both value and policy iteration iterate over the whole state and action space. In many cases, this is not feasible.
They also require knowing the probability and reward functions.
Normally this is not possible, so we move on to algorithms that don't make these assumptions.

# Deep Q-learning

The idea behind deep Q-learning is to learn a parameterised Q-function from data $\{(s,a,s',r)_i\}_{i=1}^N$ that we will generate.
We want a Q-function that satisfies the Bellman equation.
$$
Q^*(s,a) = \mathbb{E}_{s' \sim p(\cdot \vert s,a)} \left [ r(s,a) + \gamma \max_{a'} Q^*(s',a') \right ]
$$
As we update the learned Q-function we will want to minimise the MSE Loss, e.g.
$$
MSE Loss := \left ( Q_{new}(s,a) - (r + \gamma \max_a Q_{old}(s',a)) \right )^2
$$
This means keeping a track of the old and new networks as we progress through training.
This gives us our training loop - however how do we collect this data?

The basics of how we collect the data is we have some policy to gather data.
We play a number of games to collect the data for our batch.
Then we update our optimum policy with this new data.
Then we use the optimum policy to somehow generate a new gather policy.
There are a couple of challenges here:

1. Exploration vs exploitation: If we follow the best policy all the time we will not learn about other actions we might not consider.

2. Non-iid, highly correlated data: If we just collect data using the same policy our data samples are not independent, instead it is highly correlated.

To get around the first challenge we use an $\epsilon$-greedy policy.
That is defined as follows:
$$
\pi_{\epsilon}(s) = \begin{cases}
\text{arg}\max_{a \in A} Q(s,a) & \text{with probability } 1 - \epsilon\\
\text{random action} & \text{with probability } \epsilon
\end{cases}
$$
We can then use $\epsilon$ to determine how much we explore vs exploit the environment.

To account for the second issue we can use a replay buffer.
This is a cache of transitions previously taken by the actor.
We continually update the buffer as more episodes are played, with older samples discarded.
We train the Q-network on random mini-batches of transitions from the replay memory, instead of consecutive samples.
The larger this buffer, the lower the correlation between samples.

Putting this all together we get the following algorithm:
```pseudocode
Deep Q-learning:
1. Initialize replay memory D to capacity N.
2. Initialise Q-function with random weights.
3. For episode in episodes:
3.1. Initialise sequence s_1 = {x_1} and preprocessed sequence phi_1 = phi(s_1)
3.2. For t = 1, T do
3.2.1. With probability \epsilon select random action a_t otherwise select a_t max_a Q(phi(s_t), a; theta)
3.2.2. Execute action a_t in emulator and observe reward r_t and image x_{t+1}.
3.2.3. Set s_{t+1} = s_t, a_t, x_{t+1} and preprocess phi_{t+1} = phi(s_{t+1})
3.2.4. Store transition (phi_t, a_t, r_t, phi_{t+1}) in D.
3.2.5. Sample random minibatch of transitions (phi_j, a_j, r_j, phi_{j+1}) from D.
3.2.6. Set y_j = r_j for terminal phi_{j+1} otherwise r_j + gamma max_a' Q({phi_{j+1}}, a'; theta)
3.2.7. Perform gradient descent step.
```

# Policy gradient

In deep Q-learning we learn a Q-function to derive a policy.
In policy gradient we learn a policy directly.
That is, we parameterise a policy function $\pi: S \times A \rightarrow [0,1]$ directly.
We then want to maximise:
$$
J(\pi) = \mathbb{E} \left [ \sum_{t \geq 0} r_t \vert s_0 = s, \pi \right ]
$$
(Here we assume $\gamma = 1$.)
This then transforms the optimum policy search to an optimum parameter search.

The issue with this approach is the delayed rewards.
In a classical supervised deep learning approach we would use a forward pass - compare that against the actual result and run back propagation through the network.
In RL we don't know the best action - so instead we can use the sign of the eventual reward to update the weights.

![policy gradient](../../../static/images/policy_gradients_loss.png)

To collect data we first run a collection of trajectories and find out the ultimate reward using our current $\pi_{\theta}$.
We then compute the policy gradients $\nabla_{\theta} J(\theta)$ and update the policy $\theta_{t+1} = \theta_t + \alpha \nabla_{\theta_t} J(\theta_t)$.
Below is how we derive $\nabla_{\theta} J(\theta)$ for the REINFORCE algorithm.
$$
\begin{aligned}
\nabla_{\theta} J(\theta) = & \nabla_{\theta} \mathbb{E}_{\tau \sim p_{\theta}(\tau)} [ R(\tau) ]\\
= & \nabla_{\theta} \int \pi_{\theta}(\tau) R(\tau) d\tau\\
= & \int \nabla_{\theta} \pi_{\theta}(\tau) R(\tau) d\tau\\
= & \int \nabla_{\theta} \pi_{\theta}(\tau) \frac{\pi_{\theta}(\tau)}{\pi_{\theta}(\tau)} R(\tau) d\tau\\
= & \int \pi_{\theta}(\tau) \nabla_{\theta} \log \pi_{\theta}(\tau) R(\tau) d\tau & \nabla_{\theta} \log \pi_{\theta}(\tau) = \frac{\nabla_{\theta} \pi(\tau)}{\pi(\tau)} \\
= & \mathbb{E}_{\tau \sim p_{\theta}(\tau)} [ \nabla_{\theta} \log \pi_{\theta}(\tau) R(\tau) ]
\end{aligned}
$$
Where this last equation can be approximated by collecting a finite number of samples.
This can be expanded further to clarify this.
$$
\begin{aligned}
\nabla_{\theta} J(\theta) = & \mathbb{E}_{\tau \sim p_{\theta}(\tau)} [ \nabla_{\theta} \log \pi_{\theta}(\tau) R(\tau) ]\\
= & \mathbb{E}_{\tau \sim p_{\theta}(\tau)} \left [ \nabla_{\theta} \left [ \log p(s_0) + \sum_{t=1}^T \log \pi_{\theta}(a_t \vert s_t) + \sum_{t=1}^T \log p(s_{t+1} \vert s_t, a_t) \right ] R(\tau) \right ]\\
= & \mathbb{E}_{\tau \sim p_{\theta}(\tau)} \left [ \nabla_{\theta} \left [ \sum_{t=1}^T \log \pi_{\theta}(a_t \vert s_t) \right ] \sum_{t=1}^T R(s_t, a_t) \right ]\\
\end{aligned}
$$
This does not know which particular action led to the reward, so instead we update all actions taken based on the reward at the end.
This can sometimes harm the algorithm too much, so variants were developed to mitigate this.
These variants subtract a state-based baseline from the reward.
The two most common ones are:

- Actor-critic which uses the Q-values learned from the data.

$$
\nabla_{\theta} J(\pi_\theta) = \mathbb{E}_{a \sim \pi_{\theta}} [ \nabla_{\theta} \log \pi_{\theta}(a \vert s) Q^{\pi_{\theta}}(s,a) ]
$$

- Advantage actor-critic, uses Q minus V values.
$$
\nabla_{\theta} J(\pi_\theta) = \mathbb{E}_{a \sim \pi_{\theta}} [ \nabla_{\theta} \log \pi_{\theta}(a \vert s) \left ( Q^{\pi_{\theta}}(s,a) - V^{\pi_{\theta}}(s)\right ) ]
$$

