---
aliases:
checked: false
course: CS7642 Reinforcement Learning
created: 2025-05-20
draft: false
last_edited: 2025-05-20
tags:
  - OMSCS
title: Week 2 - Temporal Difference learning
type: lecture
week: 2
---

Within [reinforcement learning](../../general/reinforcement_learning.md) there are broadly 3 types of algorithms:

1. **Model-based**: These algorithms first aim to understand the environment by building or learning an explicit model of it. This model describes how the environment behaves (e.g., transition probabilities and rewards).
	1. **Model Learning/Update**: Run through an example (an interaction with the environment) to collect data and update the parameters of a [MDP](../../general/markov_decision_process.md) model. This typically involves estimating state transition probabilities and reward functions.
	2. **Planning/Solving**: Use the learned [MDP](../../general/markov_decision_process.md) model (e.g., using algorithms like [Value iteration (MDP)](../../general/value_iteration_(mdp).md) or [Policy Iteration (MDP)](../../general/policy_iteration_(mdp).md)) to generate an optimal (or near-optimal) [value function](../../general/value_function_(rl).md).
	3. **Policy Derivation**: Use the calculated [value function](../../general/value_function_(rl).md) and the learned model to derive an optimal [policy](../../general/policy_(mdp).md). This policy dictates the best action to take in each state, often by choosing the action that maximizes the expected future reward (e.g., using argmax over the Q-values derived from the value function and model).
2. **Value-function based (model-free)**: These algorithms bypass the need to build an explicit model of the environment. Instead, they directly learn a [value function](../../general/value_function_(rl).md) (or action-value function) that estimates the goodness of states or state-action pairs.
	1. **Value Function Update**: Run through an example (an interaction with the environment) and use the observed outcomes (rewards and next states) to directly update the [value function](../../general/value_function_(rl).md). This might be a state-value function V(s) or, more commonly, an action-value function Q(s,a), which estimates the expected return of being in state s and taking action a.
	2. **Policy Extraction**: Implicitly or explicitly derive a [policy](../../general/policy_(mdp).md) for each state by evaluating the actions that lead to the highest estimated value. For Q-functions, this often means choosing the action a that maximizes Q(s,a) for a given state s.
3. **Policy Search (or Policy Optimization)**: This approach directly searches for an optimal [policy](../../general/policy_(mdp).md) without necessarily learning a value function or a model. The goal is to find a policy that directly maps states to actions and maximizes the cumulative reward.
	1. **Policy Evaluation and Update**: Run through an example using the current [policy](../../general/policy_(mdp).md). Based on the observed outcomes (rewards and trajectories), directly update the parameters of the policy to improve its performance. This often involves gradient-based methods where the policy parameters are adjusted in the direction that increases the expected return.

The different approaches have varying trade-offs. Generally, model-based approaches are often more computationally intensive for the planning step but can be more sample efficient (requiring fewer interactions with the environment) because they can "plan" internally without needing new real-world data for every decision. Conversely, model-free approaches (including value-function based and policy search) are typically less computationally intensive per update (as they don't involve a full planning step) but are often more sample intensive, requiring many interactions with the environment to learn effectively. Policy search methods, in particular, can be good for continuous action spaces and may sometimes converge faster than value-based methods in certain complex scenarios, but they can also be more prone to local optima.

# Temporal difference learning

The setup for *Temporal Difference Learning* involves a sequential interaction with an environment, typically broken down into distinct 'runs' or **episodes**. Each episode consists of a sequence of states, actions, and rewards. The overarching goal is to enable a learning agent to improve its actions in future episodes by refining its understanding of the value of different states.

For a single episode, say $E = (s_0, a_0, r_1, s_1, a_1, \ldots)$, we can define the **return** from a state $s_t$​ as the total [discounted reward](../../general/discounted_rewards.md) from that point on wards until the end of the episode (or indefinitely in a continuing task). This is often denoted as
$$
G(s_n) := \sum_{k=0}^{\infty} \gamma^kr_{n+k+1}​
$$
where $\gamma \in [0,1)$ is the [discount factor](../../general/discounted_rewards.md). The true [value function](../../general/value_function_(rl).md) $V^{\pi}(s)$ for a policy $\pi$ is the _expected_ return when starting in state $s$ and following policy $\pi$:
$$
V^{\pi}(s) = \mathbb{E}\left [ G(s_n) ​\vert s_n​ = s \right ]
$$
We estimate $V^{\pi}(s)$ by averaging the _actual returns_ $G_t(s)$​ observed from many episodes where state $s$ was visited.

>[!note] Notation
> We can define $G_t(s)$ in multiple ways:
> - **First visit**: Let $G_t(s) = G_t(s_n)$ where $s_n = s$ and that is the smallest such $n$ where this is true.
> - **Every visit**: Let $G_t(s) = \sum_{n \in \mathbb{N}, s_n = s} G_t(s_n)$  adding the values for each visit.

If we have $t-1$ previous estimates for the value of state $s$, say $V_1​(s),V_2​(s), \ldots ,V_{t−1}​(s)$, and we observe a new return $G_t​(s)$ for state $s$ in the current episode, a simple way to update our estimate $V_t​(s)$ is via an incremental average:
$$
\begin{align*}
V_t(s) & = \frac{(t-1) V_{t-1}(s) + G_t(s)}{t}\\
& = V_{t-1}(s) + \frac{1}{t} \left ( G_t(s) - V_{t-1}(s) \right )
\end{align*}
$$
This update moves the estimate $V_t​(s)$ a fraction of the way towards the newly observed return $G_t​(s)$ by the difference between them (thus the name!) multiplied by a factor of $1/t$. The weighting factor of $1/t$ was only an artifact of using equal weighting between each run, however we can update this to be more general.
$$
V_t(s) = V_{t-1} + \alpha_t (G_t(s) - V_{t-1}(s))
$$

[Learning rate convergence](../../general/learning_rate_convergence.md)

However, calculating the full return $G_t$​ requires waiting until the end of an episode, which can be slow or impractical in long-running or continuous tasks. Temporal Difference Learning methods overcome this by updating estimates _based on other estimates_. This technique is known as **bootstrapping**.

>[!caution] What happened to the action?
> It's important to recognize that this derivation focuses on the [value function](../../general/value_function_(rl).md) V(s). For directly learning which actions to take (i.e., for control), we typically extend these ideas to quality function $Q(s,a)$, which explicitly incorporate the chosen action. This leads to algorithms like [SARSA](sarsa.md) and [Q-learning](../../general/q-learning.md).

# TD(1)

In [temporal difference (TD)](temporal_difference_learning.md) methods, our aim is to update value function estimates incrementally as an episode unfolds, rather than waiting until the very end.

Previously we update a state's value estimate based on the full return $G_t$ observed after visiting that state. However, this requires waiting until the end of an episode, which can be inefficient or impossible in continuous tasks.

TD(1) offers an "online" way to achieve the same result as the full return method. It does this by distributing the credit for the eventual return back to all states visited earlier in the episode. It uses a mechanism called **eligibility traces** $e(s)$ within episodes, which essentially keep a decaying record of how recently and frequently a state has been visited within the current episode.

## Eligibility Trace Mechanism for TD(1)

Within each episode, we maintain an eligibility trace $e(s)$ for every state $s$, initialized to zero. When an agent transitions from state $s_t$​ to $s_{t+1​}$ and receives reward $r_{t+1​}$ at step t:

1. **Increment Current State's Trace:** $e(s_t) \leftarrow e(s_t) + 1$
2. **Decay All Traces:** For all states s, $e(s_t) \leftarrow \gamma e(s_t)$ (where $\gamma$ is the [discount factor](../../general/discounted_rewards.md))

This decay by $\gamma$ means that older visits to a state have their eligibility reduced, reflecting the diminishing importance of past events due to discounting.

## TD(1) Update Rule

When an episode begins we have the value function from the previous episode $V_{old}$ and our job is to create a new value function $V_{new}$. At each step $t$ within this episode, after the transition $(s_t, a_t, r_{t+1}, s_{t+1})$, we calculate a **TD error** for the current transition:
$$\delta_t = r_{t+1} + \gamma V_{old}(s_{t+1}) - V_{old}(s_t).$$This $\delta_t$​ is the fundamental prediction error: the difference between the current estimate $V_{new}(s_t​)$ and a one-step bootstrapped estimate of the true return.

Then, we update the value estimate for _every state s_ based on this $\delta_t$​ and its eligibility trace $e(s)$:
$$
V_{new}(s) \leftarrow V_{new}(s) + \alpha \ \delta_t \ e(s)
$$
where $\alpha$ is the learning rate for this episode.

Here's the pseudocode for TD(1) (with accumulating traces):

```pseudocode
Initialize V(s) arbitrarily for all s in S

For each episode:
	Set V_old = V
	// We will use V for V_new
	Set e(s) = 0 for all s in S (reset traces for new episode)
	Initialize starting state s_0

	For each step t from 0 until episode terminates (s_t -> a_t -> r_{t+1} -> s_{t+1}):
		// 1. Calculate TD Error for current step using V_old
		// Note: if s_{t+1} is terminal, V_old(s_{t+1}) is 0
		delta_t = r_{t+1} + gamma * V_old(s_{t+1}) - V_old(s_t)

		// 2. Update eligibility trace for current state
		e(s_t) = e(s_t) + 1

		// 3. Update all state values in V_new and decay all eligibility traces
		For each state s in S:
			V(s) = V(s) + alpha * delta_t * e(s)
			e(s) = gamma * e(s)

Output: V
```

The remarkable property of TD(1) is that, over the course of a single episode, the _total_ update made to the value of a state $V_{new}​(s_t​)$ (accumulating all the small updates it receives due to future $\delta_t$) is precisely equivalent to the update that a we got from total returns if a state was visited.
$$
V_{new}(s) = V_{new}(s) + \alpha (G_t(s) - V_{old}(s))
$$

To see why the update rule is equivalent, lets assume some state $s$ was the start of the episode and never visited again.
$$
\begin{align*}
V_{new}(s) & = V_{old}(s) + \sum_{n=0}^{\infty} \alpha_t (r_n + \gamma V_{old}(s_n) - V_{old}(s_{n-1})) e_n(s)\\
& = V_{old}(s) + \alpha_t \sum_{n=1}^{\infty} (r_n + \gamma V_{old}(s_n) - V_{old}(s_{n-1})) \gamma^{n-1}\\
& = V_{old}(s) + \alpha_t \sum_{n=1}^{\infty} (\gamma^{n-1}r_n + \gamma^n V_{old}(s_n) - \gamma^{n-1} V_{old}(s_{n-1}))\\
& = V_{old}(s) + \alpha_t \left ( \left (\sum_{n=1}^{\infty} \gamma^{n-1} r_n \right) + \left( \sum_{n=1}^{\infty} \gamma^n V_{old}(s_n) \right ) - \left (V_{old}(s_0) + \sum_{n=1}^{\infty} \gamma^n V_{old}(s_{n}) \right ) \right )\\
& = V_{old}(s) + \alpha_t (G_t(s) - V_{old}(s))\\
\end{align*}
$$

This generalizes to work for states that are revisited and matches the every visit definition of $G_t(s)$.

# Issues with TD(1)

While TD(1) offers the appeal of total returns but also suffers similar drawbacks:

1. **High Variance:** TD(1) relies on the full, actual (but noisy) return $G_t$​ as its effective target (over an episode). This "target" can vary significantly from one episode to another, leading to high variance in the value function estimates. This high variance can make learning slow and unstable, especially in environments with long episodes or high stochastic. The updates for $V_new$​ are influenced by potentially very distant future rewards, which can be unpredictable.
2. **Sensitivity to Long Episodes / Computational Cost:** Because it involves summing and propagating effects over entire episodes, TD(1) can be computationally more intensive per step for very long episodes. All eligibility traces for all states must be updated and decayed at each time step. Additionally, for extremely long episodes, the value of $\gamma^k$ for large $k$ can become infinitesimally small, making the traces effectively zero for distant past states, requiring significant computations for minimal impact.
3. **No Immediate Bootstrapping Advantage:** While the TD error $\gamma_t$​ itself involves bootstrapping (using $V_{old}​(s_{t+1​})$), the cumulative effect of TD(1) over an episode is a Monte Carlo-like update. This means it doesn't fully leverage the "bootstrapping" advantage of updating estimates based primarily on other _estimates_ from immediate successor states. This immediate bootstrapping property can be highly beneficial for faster learning and reducing variance in certain scenarios.

These issues motivate the need for methods that can leverage the benefits of bootstrapping more directly, leading us to consider other forms of temporal difference learning, such as TD(0).

# TD(0)

While TD(1) provides an elegant online method for computing total returns, it inherently suffers from practical issues, mainly high variance. The target for its effective update ($G_t$​) is a single, potentially very noisy, sample of the true expected return. This can lead to slow and unstable learning, especially in environments with long or stochastic episodes.

A different perspective for learning value functions is to aim for **Bellman consistency**. The true [value function](../../general/value_function_(rl).md) $V^{\pi}(s)$ is defined by the [Bellman equation](../../general/bellman_equation.md), which states that the value of a state must be consistent with the expected value of its immediate successor states:
$$V^{\pi}(s)=\mathbb{E}_{\pi}​[R_{t+1}​+\gamma V^{\pi}(S_{t+1}​)∣S_t​=s].$$From this viewpoint, we seek a value function $V$ that best "fits" the observed transitions according to this consistency principle.

**TD(0)** (or one-step TD) directly addresses this. Instead of waiting for the full episodic return, TD(0) uses a **bootstrapped target** based on the very next observed reward and the _estimated value of the very next state_. This target, $r_{t+1}​ + \gamma V_{old}​(s_{t+1}​)$, is a sample of the right-hand side of the Bellman equation.

The TD(0) update rule for a state $s_t$​ is:
$$
V_{new}​(s_t​) \leftarrow V_{new​}(s_t​)+ \alpha (r_{t+1​}+\gamma V_{old}​(s_{t+1}​)− V_{old}​(s_t​))
$$
where $V_{old}$​ is the value function from the beginning of the episode (or previous learning iteration), ensuring a stable target for the current episode's updates.

```
Initialize V(s) arbitrarily for all s in S

For each episode:
	Set V_old = V
	// We will use V for V_new

	For each step t from 0 until episode terminates (s_t -> a_t -> r_{t+1} -> s_{t+1}):
		// 1. Calculate TD Error for current step using V_old
		// Note: if s_{t+1} is terminal, V_old(s_{t+1}) is 0
		delta_t = r_{t+1} + gamma * V_old(s_{t+1}) - V_old(s_t)

		Set V(s_t) = V(s_t) + alpha delta_t

Output: V
```

## TD(0) and Maximum Likelihood Estimation

From a theoretical standpoint, TD(0) can be seen as an approach to find the value function that is a **maximum likelihood estimate (MLE)** for the parameters of the [Bellman equation](../../general/bellman_equation.md), given the observed single-step transitions. More precisely, it often corresponds to minimizing the sum of squared one-step TD errors over the dataset of transitions.

While TD(1) aims to average the _true total returns_ (making it an unbiased estimator but with high variance), TD(0) aims to achieve _local consistency_ with the [Bellman equations](../../general/bellman_equation.md) for each observed transition. This means that TD(0) is trying to make the value of $s_t$​ as consistent as possible with the observed $r_{t+1}​+\gamma V_{old}​(s_{t+1​})$. This bootstrapping approach, even if it introduces some bias (because $V_{old}​(s_{t+1​})$ is itself an estimate), significantly **reduces variance** compared to TD(1). This lower variance often leads to faster and more stable convergence in practice, making TD(0) a cornerstone of many reinforcement learning algorithms.

# K-step estimators


# Empirical evidence
