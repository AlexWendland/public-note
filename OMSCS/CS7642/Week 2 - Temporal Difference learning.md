---
aliases: 
checked: false
course: "[[CS7642 Reinforcement Learning]]"
created: 2025-05-20
last_edited: 2025-05-20
publish: true
tags:
  - OMSCS
type: lecture
week: 2
---
# Week 2 - Temporal Difference learning

Within [[Reinforcement learning|reinforcement learning]] there are broadly 3 types of algorithms:

1. **Model-based**: These algorithms first aim to understand the environment by building or learning an explicit model of it. This model describes how the environment behaves (e.g., transition probabilities and rewards).
	1. **Model Learning/Update**: Run through an example (an interaction with the environment) to collect data and update the parameters of a [[Markov decision process|MDP]] model. This typically involves estimating state transition probabilities and reward functions.
	2. **Planning/Solving**: Use the learned [[Markov decision process|MDP]] model (e.g., using algorithms like [[Value iteration (MDP)]] or [[Policy Iteration (MDP)]]) to generate an optimal (or near-optimal) [[Value function (MDP)|value function]].
	3. **Policy Derivation**: Use the calculated [[Value function (MDP)|value function]] and the learned model to derive an optimal [[Policy (MDP)|policy]]. This policy dictates the best action to take in each state, often by choosing the action that maximizes the expected future reward (e.g., using argmax over the Q-values derived from the value function and model).
2. **Value-function based (model-free)**: These algorithms bypass the need to build an explicit model of the environment. Instead, they directly learn a [[Value function (MDP)|value function]] (or action-value function) that estimates the goodness of states or state-action pairs.
	1. **Value Function Update**: Run through an example (an interaction with the environment) and use the observed outcomes (rewards and next states) to directly update the [[Value function (MDP)|value function]]. This might be a state-value function V(s) or, more commonly, an action-value function Q(s,a), which estimates the expected return of being in state s and taking action a.
	2. **Policy Extraction**: Implicitly or explicitly derive a [[Policy (MDP)|policy]] for each state by evaluating the actions that lead to the highest estimated value. For Q-functions, this often means choosing the action a that maximizes Q(s,a) for a given state s.
3. **Policy Search (or Policy Optimization)**: This approach directly searches for an optimal [[Policy (MDP)|policy]] without necessarily learning a value function or a model. The goal is to find a policy that directly maps states to actions and maximizes the cumulative reward.
	1. **Policy Evaluation and Update**: Run through an example using the current [[Policy (MDP)|policy]]. Based on the observed outcomes (rewards and trajectories), directly update the parameters of the policy to improve its performance. This often involves gradient-based methods where the policy parameters are adjusted in the direction that increases the expected return.

The different approaches have varying trade-offs. Generally, model-based approaches are often more computationally intensive for the planning step but can be more sample efficient (requiring fewer interactions with the environment) because they can "plan" internally without needing new real-world data for every decision. Conversely, model-free approaches (including value-function based and policy search) are typically less computationally intensive per update (as they don't involve a full planning step) but are often more sample intensive, requiring many interactions with the environment to learn effectively. Policy search methods, in particular, can be good for continuous action spaces and may sometimes converge faster than value-based methods in certain complex scenarios, but they can also be more prone to local optima.

## Temporal difference learning

The setup for *Temporal Difference Learning* involves a sequential interaction with an environment, typically broken down into distinct 'runs' or **episodes**. Each episode consists of a sequence of states, actions, and rewards. The overarching goal is to enable a learning agent to improve its actions in future episodes by refining its understanding of the value of different states.

For a single episode, say $E = (s_0, a_0, r_1, s_1, a_1, \ldots)$, we can define the **return** from a state $s_t$​ as the total [[Discounted rewards|discounted reward]] from that point on wards until the end of the episode (or indefinitely in a continuing task). This is often denoted as
$$
G(s_n) := \sum_{k=0}^{\infty} \gamma^kr_{n+k+1}​
$$
where $\gamma \in [0,1)$ is the [[Discounted rewards|discount factor]]. The true [[Value function (MDP)|value function]] $V^{\pi}(s)$ for a policy $\pi$ is the _expected_ return when starting in state $s$ and following policy $\pi$:
$$
V^{\pi}(s) = \mathbb{E}\left [ G(s_n) ​\vert s_n​ = s \right ]
$$
We estimate $V^{\pi}(s)$ by averaging the _actual returns_ $G_t(s)$​ observed from many episodes where state $s$ was visited.

>[!note] Notation
> We can define $G_t(s)$ in multiple ways:
> - **First visit**: Let $G_t(s) = G_t(s_n)$ where $s_n = s$ and that is the smallest such $n$ where this is true. Here $t$ counts the number of episodes $s$ has appeared in.
> - **Every visit**: Let $G_t(s) = G_t(s_n)$ where $s_n = s$, and we run what is below every time we visit $s$. Here $t$ counts the number of times $s$ has appeared in previous episodes. 

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

![[Learning rate convergence]]

However, calculating the full return $G_t$​ requires waiting until the end of an episode, which can be slow or impractical in long-running or continuous tasks. Temporal Difference Learning methods overcome this by updating estimates _based on other estimates_. This technique is known as **bootstrapping**.

## TD(1)

In [[Temporal Difference Learning|temporal difference (TD)]] methods, our aim is to update value function estimates incrementally as an episode unfolds, rather than waiting until the very end.

Previously we update a state's value estimate based on the full return $G_t$ observed after visiting that state. However, this requires waiting until the end of an episode, which can be inefficient or impossible in continuous tasks.

TD(1) offers an "online" way to achieve the same result as the full return method. It does this by distributing the credit for the eventual return back to all states visited earlier in the episode. It uses a mechanism called **eligibility traces** $e(s)$ within episodes, which essentially keep a decaying record of how recently and frequently a state has been visited within the current episode.

### Eligibility Trace Mechanism for TD(1)

Within each episode, we maintain an eligibility trace $e(s)$ for every state $s$, initialized to zero. When an agent transitions from state $s_t$​ to $s_{t+1​}$ and receives reward $r_{t+1​}$ at step t:

1. **Increment Current State's Trace:** $e(s_t) \leftarrow e(s_t) + 1$
2. **Decay All Traces:** For all states s, $e(s_t) \leftarrow \gamma e(s_t)$ (where $\gamma$ is the [[Discounted rewards|discount factor]])

This decay by $\gamma$ means that older visits to a state have their eligibility reduced, reflecting the diminishing importance of past events due to discounting.

### TD(1) Update Rule



At each step $t$ within an episode, after the transition $(s_t, a_t, r_{t+1}, s_{t+1})$, we calculate a **TD error** for the current transition: $\delta_t = r_{t+1} + \gamma V(s_{t+1}) - V(s_t)$. This $\delta_t$​ is the fundamental prediction error: the difference between the current estimate $V(s_t​)$ and a one-step bootstrapped estimate of the true return.

Then, we update the value estimate for _every state s_ based on this $\delta_t$​ and its eligibility trace $e(s)$:
$$
V(s) \leftarrow V(s) + \alpha \ \delta_t \ e(s)
$$
where $\alpha$ is the learning rate for this episode.

Here's the pseudocode for TD(1) (with accumulating traces):

```pseudocode
For each episode t
	For all s, set e(s) = 0 and V_t(s) = V_{t-1}(s).
	 	For each step s_{n-1} -> s_{n} where reward r_t was gained
	 		Set e(s_{n-1}) := e(s_{n-1}) + 1
			For all state s,
				V_t(s) := V_t(s) + \alpha_t (r_n + \gamma V_{t-1}(s_n) - V_{t-1}(s_{n-1})e(s)
	 			e(s) := \gamma e(s)
```

For each episode we are incrementally learning $V_{t}$ each step of the episode. The value $e(s)$ tracks how many times this episode we have visited $s$ weighted by how long ago it was. This is achieved by setting $e(s_{n-1}) = e(s_{n-1}) + 1$, as we were previously there, and $e(s) = \gamma e(s)$ at the end of the step decaying previous visits by $\gamma$.

To see why the update rule is equivalent, lets assume some state $s$ was the start of the episode and never visited again.
$$
\begin{align*}
V_t(s) & = V_{t-1}(s) + \sum_{n=0}^{\infty} \alpha_t (r_n + \gamma V_{t-1}(s_n) - V_{t-1}(s_{n-1})) e_n(s)\\
& = V_{t-1}(s) + \alpha_t \sum_{n=1}^{\infty} (r_n + \gamma V_{t-1}(s_n) - V_{t-1}(s_{n-1})) \gamma^{n-1}\\
& = V_{t-1}(s) + \alpha_t \sum_{n=1}^{\infty} (\gamma^{n-1}r_n + \gamma^n V_{t-1}(s_n) - \gamma^{n-1} V_{t-1}(s_{n-1}))\\
& = V_{t-1}(s) + \alpha_t \left ( \left (\sum_{n=1}^{\infty} \gamma^{n-1} r_n \right) + \left( \sum_{n=1}^{\infty} \gamma^n V_{t-1}(s_n) \right ) - \left (V_{t-1}(s_0) + \sum_{n=1}^{\infty} \gamma^n V_{t-1}(s_{n}) \right ) \right )\\
& = V_{t-1}(s) + \alpha_t (G_t(s) - V_{t-1}(s))\\
\end{align*}
$$

This method has a major drawback though, we only use

- The values from the episodes the state was in, and 
- The states previous value function.

This means we don't use the value function of different states to update one another. Like we do in the [[Bellman equation]], where the value of the state is based on the value of the surrounding states.

## TD(0) rule



It's important to recognize that this derivation focuses on the [[Value function (MDP)|value function]] V(s). For directly learning which actions to take (i.e., for control), we typically extend these ideas to quality function $Q(s,a)$, which explicitly incorporate the chosen action. This leads to algorithms like [[SARSA]] and [[Q-learning]].


## K-step estimators


## Empirical evidence 