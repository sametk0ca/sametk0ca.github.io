# Fault Injection and Redundancy

- **Source:** [[ka-hardware-security]]
- **Tags:** #hardware-security #fault-attacks #active-attacks #countermeasures

## Overview
Fault injection attacks involve actively manipulating a system's environment to induce errors in its execution, which can then be exploited to bypass security checks or reveal secrets.

## 1. Attack Vectors
- **Voltage Glitching:** Momentarily dropping the power supply voltage to cause the CPU to skip an instruction (e.g., bypassing an `if (password_correct)` check).
- **Clock Glitching:** Manipulating the clock signal to cause a "double-edge" or shortened cycle, leading to incorrect calculations.
- **Electromagnetic (EM) Pulses:** Inducing electrical currents in the chip's internal wiring to flip bits.
- **Laser Attacks:** Using a high-precision laser to target specific transistors or memory cells.
- **Rowhammer:** Purely software-induced bit flipping in DRAM.

## 2. Exploitation Examples
- **RSA-CRT Attack:** Inducing a single fault during an RSA signature calculation using the Chinese Remainder Theorem (CRT) allows an attacker to mathematically derive the secret signing key.
- **Status Register Flipping:** Forcing a boolean return value from `false` to `true`.

## 3. Countermeasures

### Redundancy
- **Spatial Redundancy:** Performing the same calculation on two or more independent hardware modules and comparing the results.
- **Temporal Redundancy:** Performing the calculation twice on the same hardware at different times.
- **Limitation:** Redundancy increases the attack surface for side-channel analysis, as it provides more traces for the attacker to observe.

### Error Correcting Codes (ECC)
Using mathematical codes (e.g., Parity, Hamming codes) to detect and correct bit-flips in memory or on communication buses.

### Sensors
Adding physical monitors to the hardware:
- **Voltage/Clock Monitors:** Triggering a system reset if the power or clock signal deviates from normal bounds.
- **Mesh Layers:** Active metal layers on top of the chip that detect physical probing or drilling.
- **Light/Temperature Sensors:** Detecting when the chip package has been opened or subjected to extreme conditions.

## Related Concepts
- [[hardware-security-vulnerabilities]] (Rowhammer)
- [[software-security-mitigation-techniques]]
- [[digital-signatures-applied]] (RSA-CRT)
