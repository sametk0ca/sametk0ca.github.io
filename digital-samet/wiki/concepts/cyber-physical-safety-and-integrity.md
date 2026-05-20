# Cyber-Physical Safety and Integrity

- **Source:** [[ka-cps-security]]
- **Tags:** #cps #safety #integrity #resilience

## Overview
In Cyber-Physical Systems (CPSs), the primary concern shift from information confidentiality to the **Safety** and **Integrity** of the physical process. A cyber-compromise can lead to catastrophic kinetic events (e.g., explosions, crashes).

## 1. Safety Systems vs. Cyber Security
- **Safety Instrumented Systems (SIS):** Dedicated hardware/software designed to bring a process to a safe state (e.g., Emergency Shutdown) if dangerous conditions are detected.
- **Independence:** SIS should ideally be physically and logically independent from the primary control system.
- **The Threat:** Modern malware (like **Triton**) specifically targets the SIS to disable safety protections, allowing a subsequent cyber-attack to cause physical damage.

## 2. Protections Against Natural Events (Fault Tolerance)
Traditional engineering has built-in protections against random failures (sensor noise, wear and tear):
- **N-1 Criterion:** The system can lose any single component and continue to operate correctly.
- **FDIR (Fault Detection, Isolation, and Reconfiguration):** Using redundancy to identify and bypass faulty components.
- **Robust Control:** Designing algorithms that remain stable despite uncertainty in environment or parameters.

## 3. Why Traditional Protections Fail Against Cyber-Attacks
Fault-tolerance mechanisms assume **independent, non-malicious failures**. 
- **Strategic Adversaries:** An attacker can induce *correlated* failures across multiple redundant components or feed "physically plausible" but incorrect data to the system to bypass anomaly detectors.

## 4. Resilience and Attack Mitigation
- **Resilient Estimation:** Algorithms that can correctly identify the system state even if some sensors are providing malicious data.
- **Virtual Sensors:** Using physical models to generate "expected" values when a real sensor is suspected of being compromised.
- **Safe Control Actions:** A "Reference Monitor" for physical commands that blocks any signal that would lead the system into an unsafe region of its state space.

## Related Concepts
- [[physics-based-attack-detection]]
- [[industrial-control-systems-ics-security]]
- [[transduction-attacks-on-sensors]]
