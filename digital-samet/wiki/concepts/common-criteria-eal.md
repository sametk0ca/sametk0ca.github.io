# Common Criteria and EAL Levels

- **Source:** [[ka-secure-software-lifecycle]]
- **Tags:** #certification #assurance #eal #common-criteria

## Overview
The Common Criteria (ISO/IEC 15408) is an international standard for computer security certification. It provides a shared framework for evaluating IT products to ensure they meet claimed security requirements.

## 1. Core Definitions
- **Target of Evaluation (TOE):** The product or system being evaluated.
- **Protection Profile (PP):** A template of security requirements for a specific class of products (e.g., Firewalls, Smart Cards).
- **Security Target (ST):** The specific set of security requirements a TOE claims to meet.

## 2. Evaluation Assurance Levels (EAL)
EAL levels indicate the depth and rigor of the evaluation process. They do NOT measure the strength of security itself, but rather the *confidence* that the security features work as intended.

- **EAL 1:** Functionally tested.
- **EAL 2:** Structurally tested.
- **EAL 3:** Methodically tested and checked.
- **EAL 4:** Methodically designed, tested, and reviewed (high assurance for commercial products).
- **EAL 5:** Semi-formally designed and tested.
- **EAL 6:** Semi-formally verified design and tested (high-risk assets).
- **EAL 7:** Formally verified design and tested (highest assurance).

## 3. Significance
EAL certification is often a legal or regulatory requirement for government, defense, and critical infrastructure vendors. It allows for mutual recognition of product security across participating countries.

## Related Concepts
- [[software-maturity-models-samm-bsimm]]
- [[hardware-formal-verification]] (EAL 7)
- [[kernel-and-software-verification-case-studies]]
