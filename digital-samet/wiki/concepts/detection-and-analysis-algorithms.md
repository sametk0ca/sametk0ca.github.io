---
concept: Detection and Analysis Algorithms
source: [[ka-security-operations-and-incident-management]]
tags: [concept, soim, ids, anomaly-detection, misuse-detection, cybok]
---

# Concept: Detection and Analysis Algorithms

## 1. Misuse Detection (Signature-Based)
Identifies attacks by matching activity against a database of known malicious patterns (**signatures**).
- **Key Advantage**: High precision; results are easily interpreted and documented (e.g., linked to a CVE).
- **Key Challenge**: Requires constant updates; cannot detect unknown (**Zero-day**) attacks.
- **Examples**: Snort, Suricata, YARA rules.

## 2. Anomaly Detection
Identifies attacks by detecting deviations from a model of "normal" behavior.
- **Key Advantage**: Theoretically detects zero-day attacks.
- **Key Challenge**: Prone to false positives; anomalies are hard to interpret without deep domain knowledge.
- **Approaches**: 
    - **Statistical**: Using distributions and thresholds.
    - **Specification-Based**: Checking if activity violates system/protocol specifications (e.g., Bro/Zeek).
    - **Learning-Based**: Training models on historical data.

## 3. Evaluation Metrics
Detectors are binary classifiers evaluated using:
- **True Positives (TP)**: Correctly identified attacks.
- **False Positives (FP)**: Benign activity flagged as an attack (Type I error).
- **False Negatives (FN)**: Missed attacks (Type II error).
- **Precision**: $TP / (TP + FP)$ — How many alerts are real?
- **Recall**: $TP / (TP + FN)$ — How many of the total attacks were caught?
- **ROC Curves**: Visualizing the trade-off between FP and FN.

## 4. The Base-Rate Fallacy
In environments where attacks are rare relative to benign events, even a very low False Positive rate can result in a massive volume of false alerts, overwhelming human analysts.

## 5. Machine Learning (ML) in Detection
- **Supervised**: Labeled data (Normal vs. Attack) used to train classifiers (SVM, Decision Trees).
- **Unsupervised**: Finding outliers or clusters in unlabeled data.
- **Issues**: Feature engineering is knowledge-intensive; deep learning models often lack explainability.

## References
- [[ka-security-operations-and-incident-management]]
- [[soim-data-sources]]
- [[malware-analysis-methods]]
