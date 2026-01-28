---
aliases:
created: 2024-02-19
date_checked: 2026-01-28
draft: false
last_edited: 2026-01-28
tags:
  - machine-learning
title: PAC learnable bound with VC-dimension
type: lemma
---
# Statement

> [!lemma] Lemma
> For a learner with a [hypothesis space](modelling_paradigm.md) $H$ with [VC dimension](vapnik-chervonenkis_dimension.md) $VC(H)$, if we draw
> $$m \geq \frac{1}{\epsilon} \left (8 \cdot VC(H) \cdot \log_2\left(\frac{13}{\epsilon}\right) + 4 \log_2\left(\frac{2}{\delta}\right) \right)$$
> [i.i.d.](independent_identically_distributed_samples.md) samples for [training data](training_data.md) $T$ and there exists a hypothesis [consistent](consistent_learner.md) with $T$, then this will be a [PAC learner](probably_approximately_correct_learnable_(pac).md) with $\leq \epsilon$ accuracy with probability $1-\delta$.

# Proof
