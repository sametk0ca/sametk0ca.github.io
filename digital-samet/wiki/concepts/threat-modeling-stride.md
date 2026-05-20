# Threat Modeling and STRIDE

- **Source:** [[ka-secure-software-lifecycle]]
- **Tags:** #sdlc #threat-modeling #stride #design

## Overview
Threat modeling is a structured process to identify, document, and discuss security implications of a system's design. It helps teams anticipate adversary motivations and system weaknesses.

## 1. The STRIDE Model
Developed by Microsoft, STRIDE is a mnemonic used to categorize threats by the security property they violate:

| Threat | Security Property | Description |
| :--- | :--- | :--- |
| **S**poofing | Authenticity | Pretending to be someone or something else. |
| **T**ampering | Integrity | Maliciously modifying data or code. |
| **R**epudiation | Non-repudiation | Denying an action performed (lack of evidence). |
| **I**nformation Disclosure | Confidentiality | Exposing data to unauthorized parties. |
| **D**enial of Service | Availability | Making the system unusable for legitimate users. |
| **E**levation of Privilege | Authorisation | Gaining unauthorized access levels. |

## 2. The Process
1. **Model the System:** Create data-flow diagrams (DFDs) identifying processes, data stores, and trust boundaries.
2. **Apply STRIDE:** Analyze each DFD component against the STRIDE categories.
3. **Address Threats:** For each identified threat, decide whether to:
    - **Mitigate:** Add a security control (e.g., encryption, logging).
    - **Accept:** Consciously take the risk.
    - **Transfer:** Delegate risk to another party (e.g., insurance, cloud provider).
    - **Avoid:** Change the design to eliminate the threat.

## 3. Other Methods
- **Attack Trees:** Hierarchical diagrams of how an attacker reaches a goal.
- **PASTA:** Process for Attack Simulation and Threat Analysis.
- **LINDDUN:** Specifically for privacy-related threats.

## Related Concepts
- [[sdl-and-devsecops]]
- [[abuse-and-misuse-cases]]
- [[os-security-principles]]
