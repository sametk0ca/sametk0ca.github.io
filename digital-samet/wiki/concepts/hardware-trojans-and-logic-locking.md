# Hardware Trojans and Logic Locking

- **Source:** [[ka-hardware-security]]
- **Tags:** #hardware-security #supply-chain #trojans #ip-protection

## Overview
The globalization of the semiconductor supply chain (design in US, foundry in Asia, assembly elsewhere) introduces risks of malicious manipulation and theft of intellectual property.

## 1. Hardware Trojans
A Hardware Trojan is a malicious addition or modification to an integrated circuit (IC) by an untrusted party in the supply chain.
- **Goal:** Leak sensitive data (keys), disable functionality (kill-switch), or degrade performance.
- **Classification:**
    - **Physical:** Size, location, and distribution of the Trojan logic.
    - **Activation:** Triggered by internal events (counters, specific data patterns) or external signals (antenna, physical sensors).
    - **Action:** Information leakage, functional change, or denial of service.
- **Detection:** Extremely difficult because Trojans are tiny compared to the billions of transistors in a modern SoC. Techniques include side-channel analysis and visual inspection via Scanning Electron Microscope (SEM).

## 2. Logic Locking
A design-for-trust technique to protect an IC from reverse engineering and unauthorized manufacturing.
- **Mechanism:** The designer adds extra "locking gates" to the circuit. The correct functionality is only enabled when a secret key is applied to these gates.
- **Benefits:**
    - **Overbuilding Prevention:** A foundry cannot produce extra functional chips to sell on the gray market without the key.
    - **Reverse Engineering Protection:** Even if the physical layout is copied, the circuit logic remains non-functional without the key.
- **Attack:** Adversaries use **SAT Solvers** to try and find the secret key by analyzing the locked netlist and comparing it with an authorized, functioning chip.

## 3. Camouflaging
A circuit-level technique to thwart visual reverse engineering.
- **Method:** Designing standard cells that look identical under a microscope but perform different logic functions (e.g., an AND gate that looks like an OR gate).

## Related Concepts
- [[hardware-root-of-trust]]
- [[software-security-foundations]]
- [[side-channel-attacks-and-masking]]
