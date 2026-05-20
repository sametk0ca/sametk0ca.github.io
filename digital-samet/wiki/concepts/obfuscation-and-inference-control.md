---
concept: Obfuscation and Inference Control
source: [[ka-privacy-and-online-rights]]
tags: [concept, privacy, anonymization, differential-privacy, cybok]
---

# Concept: Obfuscation and Inference Control

## Overview
Obfuscation techniques (Soft Privacy) relax the strict confidentiality of cryptography to limit the extent to which an adversary can make inferences from a dataset. These are often used for statistical analysis and data publishing.

## 1. Anonymization
- **Definition**: Removing direct identifiers (names, IDs) to decouple identity from information.
- **Challenge**: Data patterns themselves can be unique (**quasi-identifiers**). Re-identification attacks often succeed by cross-referencing with other datasets (e.g., Netflix prize dataset or AOL search logs).

## 2. k-anonymity
- **Goal**: Ensure each individual is indistinguishable from at least $k-1$ others.
- **Methods**:
    - **Generalization**: Reducing precision (e.g., ZIP code 21345 becomes 21***).
    - **Suppression**: Deleting specific data points or entire records.
- **Limitations**:
    - **l-diversity**: Needed if all $k$ individuals have the same sensitive attribute (e.g., same medical diagnosis).
    - **t-closeness**: Ensures the distribution of sensitive attributes in a group is close to the overall population.

## 3. Dummy Addition
- **Definition**: Adding fake data points (**dummies**) to hide real samples.
- **Challenge**: Dummies must be indistinguishable from real points to be effective. Adversaries can often filter them out using statistical analysis.

## 4. Differential Privacy
- **Definition**: Currently the "gold standard." It is a property of a mechanism, not a dataset.
- **Core Principle**: An algorithm is differentially private if its output doesn't change significantly whether any single individual's data is included or not.
- **Formal Definition ($\epsilon$-differential privacy)**: Bounds the maximum change in output probability when one record is added or removed.
- **Advantages**: Provides a formal framework to reason about leakage regardless of adversary prior knowledge.
- **Caveats**:
    - $\epsilon$ value selection is critical; high $\epsilon$ (e.g., >1) provides less protection.
    - **Sensitivity**: The more an individual's data affects the output, the more noise is required.

## References
- [[ka-privacy-and-online-rights]]
- [[privacy-as-confidentiality]]
