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
G_t​ := \sum_{k=0}^{\infty} \gamma^kr_{t+k+1}​
$$
where $\gamma \in [0,1)$ is the [[Discounted rewards|discount factor]]. The true [[Value function (MDP)|value function]] $V^{\pi}(s)$ for a policy $\pi$ is the _expected_ return when starting in state $s$ and following policy $\pi$:
$$
V^{\pi}(s) = \mathbb{E}\left [ G_t ​\vert s_t​ = s \right ]
$$
Monte Carlo methods estimate $V^{\pi}(s)$ by averaging the _actual returns_ $G_t$​ observed from many episodes where state $s$ was visited. If we have $t$ previous estimates for the value of state $s$, say $V_1​(s),V_2​(s), \ldots ,V_{t−1}​(s)$, and we observe a new return $G_t​(s)$ for state $s$ in the current episode, a simple way to update our estimate $V_t​(s)$ is via an incremental average:
$$
\begin{align*}
V_t(s) & = \frac{(t-1) V_{t-1}(s) + G_t(s)}{t}\\
& = V_{t-1}(s) + \frac{1}{t} \left ( G_t(s) - V_{t-1}(s) \right )
\end{align*}
$$
Here, $V_{t−1}​(s)$ is our previous estimate for the value of state $s$, and $G_t(s)$ is the observed return from state $s$ in the $t$'th time it was visited. This update moves the estimate $V_t​(s)$ a fraction of the way towards the newly observed return $G_t​(s)$.

The weighting factor of $1/t$ was only an artifact of using equal weighting between each run, however we can update this to be more general.
$$
V_t(s) = V_{t-1} + \alpha_t (R_t(s) - V_{t-1}(s))
$$

![[Learning rate convergence]]

However, calculating the full return $G_t$​ requires waiting until the end of an episode, which can be slow or impractical in long-running or continuous tasks. Temporal Difference Learning methods overcome this by updating estimates _based on other estimates_. This technique is known as **bootstrapping**.

---

Instead of using the _actual future return_ $G_t$​, TD methods use an _estimated future return_. The simplest form, **TD(0)** (or one-step TD), uses the reward from the next time step plus the discounted value of the next state: rt+1​+γV(st+1​). This is the _target_ for our update. The difference between this target and our current estimate V(st​) is the **TD error**: $δt​=(rt+1​+γV(st+1​))−V(st​)$The TD(0) update rule for the value function V(st​) is then:V(st​)←V(st​)+α(rt+1​+γV(st+1​)−V(st​)) This means we are moving our estimate V(st​) a step closer to rt+1​+γV(st+1​). This fundamental idea allows learning to occur after each single step of interaction, making TD methods highly efficient. **Note:** Since updates occur after each step, TD methods inherently use an "every-visit" approach if a state appears multiple times within an episode.

It's important to recognize that this derivation focuses on the [[State-value function|state-value function]] V(s). For directly learning which actions to take (i.e., for control), we typically extend these ideas to [[Action-value function|action-value functions]] Q(s,a), which explicitly incorporate the chosen action. This leads to algorithms like [[SARSA]] and [[Q-learning]].


## K-step estimators


## Empirical evidence 