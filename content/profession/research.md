---
title: Research
template: profession/research.html
description: Papers and software by Francesco Montagna on causal discovery and causal representation learning.
groups:
  - id: selected
    title: Selected works
    items:
      - title: Causal Learning with the Invariance Principle
        venue: arXiv 2026
        tldr: |
          Inferring causality usually needs a treatment and a control group: two populations whose differences come only from an intervention. What if the shifts happen *naturally* across observational datasets? Phrasing natural experiments in the language of structural causal models, we show that **three observational datasets with invariant causal mechanisms** are enough to uniquely infer the causal structure and to identify counterfactuals in acyclic models.
        links:
          - { label: arXiv, url: "https://arxiv.org/html/2605.13589v1" }
          - { label: alphaXiv overview, url: "https://www.alphaxiv.org/overview/2605.13589" }
      - title: On the Identifiability of Causal Graphs with the Invariance Principle
        venue: ICLR
        tldr: |
          We cast causal discovery as a simplified version of ICA. For a structural causal model with arbitrary bijective mechanisms and Gaussian noise, **three environments with invariant mechanisms** suffice to identify graphs of any size.
        links:
          - { label: OpenReview, url: "https://openreview.net/forum?id=ta8BKRa1bl" }
          - { label: alphaXiv overview, url: "https://www.alphaxiv.org/overview/2510.13583" }
      - title: The Rate–Distortion–Polysemanticity Tradeoff in Sparse Autoencoders
        venue: arXiv 2026
        tldr: |
          Sparse autoencoders face a three-way tradeoff: they can be accurate, sparse, or monosemantic, but generally not all three at once. Polysemantic features are often an efficient response to concepts that co-occur in the data — which makes feature hedging and splitting predictable consequences of the data-generating process.
        links:
          - { label: arXiv, url: "https://arxiv.org/abs/2605.14694" }
          - { label: alphaXiv overview, url: "https://www.alphaxiv.org/overview/2605.14694" }

  - id: other
    title: Other works
    items:
      - title: Causal discovery with score matching
        tldr: A line of work connecting causal graph inference with score-matching estimation.
        papers:
          - title: A very fast and efficient algorithm
            venue: CLeaR 2023
            links:
              - { label: paper, url: "https://proceedings.mlr.press/v213/montagna23b/montagna23b.pdf" }
              - { label: overview, url: "https://www.alphaxiv.org/overview/2304.03382" }
          - title: Score matching with no latent confounders
            venue: CLeaR 2023
            links:
              - { label: paper, url: "https://proceedings.mlr.press/v213/montagna23a/montagna23a.pdf" }
              - { label: overview, url: "https://www.alphaxiv.org/overview/2304.03265" }
          - title: Score matching with (potentially) latent confounders
            venue: CLeaR 2025
            links:
              - { label: paper, url: "https://proceedings.mlr.press/v275/montagna25a.html" }
              - { label: overview, url: "https://www.alphaxiv.org/overview/2407.18755" }
      - title: Benchmarking causal discovery methods
        venue: NeurIPS 2023
        tldr: We stress-test classical and state-of-the-art causal discovery methods under challenging conditions — non-i.i.d. data, latent confounders, faithfulness violations, misspecified parametric assumptions, and more.
        links:
          - { label: NeurIPS, url: "https://proceedings.neurips.cc/paper_files/paper/2023/hash/93ed74938a54a73b5e4c52bbaf42ca8e-Abstract-Conference.html" }
          - { label: alphaXiv overview, url: "https://www.alphaxiv.org/overview/2310.13387" }
      - title: Demystifying Amortized Causal Discovery with Transformers
        venue: TMLR
        tldr: Identifiability theory shows the limits of supervised-learning approaches to causal discovery.
        links:
          - { label: TMLR, url: "https://openreview.net/pdf?id=9Lgy7IGSfp" }
          - { label: alphaXiv overview, url: "https://www.alphaxiv.org/overview/2405.16924" }

  - id: software
    title: Software
    items:
      - title: causally
        tldr: Python library for sampling data from structural causal models under realistic assumptions.
        links:
          - { label: docs, url: "https://causally.readthedocs.io/en/latest/" }
      - title: dodiscover (PyWhy)
        tldr: I implemented several causal discovery algorithms for the [PyWhy](https://www.pywhy.org/) project.
        links:
          - { label: docs, url: "https://www.pywhy.org/dodiscover/dev/installation.html" }
---

My work asks **when and how cause–effect relationships can be learned from data**, and builds algorithms that do it. For the complete list of papers, see [Google Scholar](https://scholar.google.com/citations?user=StwghVgAAAAJ&hl=en).
