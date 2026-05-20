---
concept: Privacy as Informational Control
source: [[ka-privacy-and-online-rights]]
tags: [concept, privacy, control, settings, cybok]
---

# Concept: Privacy as Informational Control

## Overview
This paradigm moves from the pure concealment of information to the ability of users to control how their shared information is used and processed. It is often linked to the right to "informational self-determination."

## 1. Privacy Settings
Controls provided by web services to express user preferences.
- **Complexity Issue**: Many settings are too complex for average users, leading to misconfiguration and unintended disclosure.
- **Support Techniques**:
    - **Expert-defined policies**: High protection but can be restrictive.
    - **Machine Learning recommendations**: Suggesting settings based on user groups or social graphs (though the graph itself is sensitive).
    - **Crowdsourcing**: Finding the "optimum" settings based on community input.

## 2. Policy Negotiation & Communication
Automating the exchange of privacy preferences between users and services.
- **P3P (Platform for Privacy Preferences)**: A W3C standard for websites to encode policies in a machine-readable format. (Note: P3P lacks enforcement mechanisms).
- **Sticky Policies**: Data is "stuck" to a policy that travels with it, defining its allowed uses.
- **Purpose-Based Access Control**: Ensuring data access is only granted if the purpose matches the user's policy.

## 3. Interpretability
Helping users understand long, legalistic privacy policies.
- **Polisis**: An AI-based tool that translates natural language privacy policies into visual, easy-to-understand summaries.

## Caveats
- **Trust Requirement**: Users must trust the service provider to actually follow the stated policies.
- **Reduced Risk Perception**: Giving users more control can lead them to share more data than they otherwise would (the "Control Paradox").

## References
- [[ka-privacy-and-online-rights]]
- [[privacy-paradigms]]
