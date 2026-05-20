# Physical Layer Key Establishment

- **Source:** [[ka-physical-layer-security]]
- **Tags:** #physical-layer #cryptography #keys #wireless

## Overview
Physical layer key establishment uses the unique, random, and correlated properties of a wireless communication channel to derive shared secret keys between two devices without relying on traditional public-key infrastructure.

## 1. Key Principle: Channel Reciprocity
If two devices (Alice and Bob) measure the channel response between them within a very short time interval, their measurements will be highly correlated.
- **Uniqueness:** According to wireless theory, an attacker located more than half a wavelength away from Alice or Bob will measure a significantly different (de-correlated) channel response.
- **Mechanism:** The random multi-path environment (reflections, scattering) acts as a source of shared entropy available only to the two legitimate parties.

## 2. The Process
1. **Channel Probing:** Alice and Bob exchange a series of non-secret probe packets and measure channel properties (e.g., RSSI - Signal Strength, or CIR - Channel Impulse Response).
2. **Quantization:** Each party independently converts their analog measurements into a sequence of bits (e.g., using a threshold).
3. **Information Reconciliation:** Because measurements are not perfectly identical due to noise, the parties use error-correcting codes to arrive at the same bit sequence.
4. **Privacy Amplification:** Using a hash function to transform the reconciled bits into a shorter, high-entropy cryptographic key, ensuring that any partial information leaked to an attacker is eliminated.

## 3. Advantages and Limitations
- **Pros:** Does not require a pre-shared secret or heavy public-key computations; suitable for mobile and ad-hoc networks.
- **Cons:** Vulnerable to sophisticated attackers with multiple antennas or those who can predict or influence the physical environment.

## Related Concepts
- [[key-lifecycle-management]]
- [[jamming-attacks-and-resilience]]
- [[radio-fingerprinting-device-identification]]
