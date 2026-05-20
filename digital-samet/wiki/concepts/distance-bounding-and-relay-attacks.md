# Distance Bounding and Relay Attacks

- **Source:** [[ka-physical-layer-security]]
- **Tags:** #physical-layer #relay-attacks #distance-bounding #proximity

## Overview
Proximity is often used as a proxy for trust (e.g., being close to a car to unlock it). Relay attacks exploit this by making devices believe they are close to each other when they are not. **Distance Bounding** is the physical-layer defense against these attacks.

## 1. The Threat: Relay (Wormhole) Attacks
An attacker uses two surrogate devices to bridge the communication between two distant legitimate entities.
- **Example:** A Passive Keyless Entry (PKE) system. One attacker stands near the car, another near the owner's key inside a house. They relay the radio signal, and the car unlocks even though the owner is far away.
- **Logic:** Traditional cryptographic authentication cannot stop this, as the key is indeed providing valid responses; it's just doing so from the wrong location.

## 2. The Solution: Distance Bounding
Distance bounding protocols establish an upper bound on the physical distance between a **Verifier** and a **Prover** based on the round-trip time (RTT) of a signal.
- **Mechanism:** The Verifier sends a series of rapid single-bit challenges. The Prover must respond immediately (within nanoseconds).
- **Physics:** Since no signal can travel faster than the speed of light ($c \approx 30$ cm/ns), the RTT provides a fundamental physical limit on the distance ($d \le \frac{RTT \times c}{2}$).
- **Requirement:** The hardware must be capable of very low-latency processing (e.g., single-bit XOR) so that the computation time doesn't mask the travel time.

## 3. Vulnerabilities (Frauds)
- **Distance Fraud:** A lone malicious Prover tries to convince the Verifier they are closer than they really are.
- **Mafia Fraud (Standard Relay):** An external attacker relays the signal between an honest Verifier and an honest Prover.
- **Terrorist Fraud:** A malicious Prover colludes with an external attacker to fake their position without sharing their long-term secret keys.

## 4. Implementation Technologies
- **IR-UWB (Impulse-Radio Ultra Wideband):** The current best standard for secure ranging (cm-level precision). Its very short pulses (2-3 ns) make it difficult for attackers to manipulate the arrival time without being detected.
- **NFC:** Often lacks proper distance bounding, relying only on signal strength (RSSI), which is easily manipulated by an attacker using amplifiers.

## Related Concepts
- [[user-authentication-factors]] (Possession)
- [[physical-layer-key-establishment]]
- [[gnss-spoofing-and-takeover-attacks]]
