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

The setup for temporal difference learning is you get a continual input of new 'runs' of a particular environment. Each run is called a episode. The goal is then to use the inputs to update your learner so they can act better in the next episode.

For a single run $E = (s_{n}, a_{n}, r_{n})_{n \in \mathbb{N}}$ we can use [[Discounted rewards|discounted rewards]] to calculate the reward $R(s_k)$ of each state within that run by setting
$$
R(s_k) = \sum_{i=0}^{\infty} \gamma^i r_{k+1}
$$
However, when we have $t$ runs $E_k$ for $1 \leq k \leq t$ we would like to average out the value of any state. If we do what is above to generate $R_k(s)$ for $1 \leq k \leq t$  for each run. The for a state $s \in S$ where $s$ appears in runs $\mathcal{E}_s = \{k \vert  s = s_n \in E_k \}$ we can set a value function of a state after $t$ runs as
$$
V_t(s) = \frac{1}{\vert \mathcal{E}_s\vert} \sum_{k \in \mathcal{E}_s} V_k(s).
$$
Though instead of doing this when all runs are up, we can instead do this incrementally. For what appears below lets assume every state appears in every run.
$$
\begin{align*}
V_t(s) & = \left ( (t-1) V_{t-1}(s) + R_t(s) \right ) / t\\
& = V_{t-1}(s) + 1/t \left ( R_t(s) - V_{t-1}(s) \right )
\end{align*}
$$
Here we are updating the value function each time by the weighted difference between the actual discounted reward of the state for that run and the previous value of the state.

The weighting factor of $1/t$ was only an artifact of using equal weighting between each run, however we can update this to be more general.
$$
V_t(s) = V_{t-1} + \alpha_t (R_t(s) - V_{t-1}(s))
$$
![[Learning rate convergence]]




## K-step estimators


## Empirical evidence 