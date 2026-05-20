# Jamming Attacks and Resilience

- **Source:** [[ka-physical-layer-security]]
- **Tags:** #physical-layer #network-security #jamming #wireless

## Overview
Jamming is a physical layer denial-of-service attack where an adversary injects interference into a wireless channel to prevent intended receivers from successfully decoding legitimate messages.

## 1. Attack Types

### Constant Jamming
The jammer emits a continuous signal, regardless of whether a legitimate transmission is occurring. Easy to detect but highly effective.

### Reactive Jamming
The most sophisticated and power-efficient type. The jammer "listens" to the channel and only starts transmitting as soon as it detects a legitimate preamble or signal. Difficult to detect and can be surgical (e.g., targeting only control packets).

### Overshadowing
The attacker emits a signal that is orders of magnitude stronger than the legitimate signal at the receiver's antenna, forcing the receiver's hardware to "lock" onto the malicious signal.

### Signal Annihilation
A rare but theoretical attack where the adversary emits an identical signal but with **reversed polarity** to create destructive interference, effectively "canceling" the legitimate signal at the receiver.

## 2. Resilience Mechanisms (Anti-Jamming)
Countermeasures focus on introducing uncertainty about which frequency or time slot will be used, forcing the jammer to spread its power too thinly.

- **DSSS (Direct Sequence Spread Spectrum):** Multiplying the data signal with a high-rate spreading sequence.
- **FHSS (Frequency Hopping Spread Spectrum):** Rapidly switching the carrier frequency according to a pseudo-random sequence shared between the sender and receiver.
- **UFH (Uncoordinated Frequency Hopping):** A specialized technique for broadcast scenarios where no pre-shared secret exists. The sender and receiver hop independently, and the receiver uses a wideband radio to catch fragments of the message.

## 3. Key Metric: Jamming-to-Signal (J/S) Ratio
The effectiveness of jamming is measured by the J/S ratio at the receiver. If this ratio exceeds a certain threshold (specific to the hardware and modulation), the legitimate communication fails.

## Related Concepts
- [[network-attacker-models]] (DoS)
- [[physical-layer-key-establishment]]
- [[radio-fingerprinting-device-identification]]
