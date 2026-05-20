# Radio Fingerprinting (Physical-Layer Identification)

- **Source:** [[ka-physical-layer-security]]
- **Tags:** #physical-layer #identification #fingerprinting #hardware-security

## Overview
Radio fingerprinting is the process of identifying a wireless device by extracting unique characteristics from its analog circuitry. These characteristics act as a "silicon fingerprint" that is hard to clone or modify.

## 1. The Physical Basis
Hardware imperfections introduced during the manufacturing process (variations in doping, wire width, component tolerances) result in unique, measurable artifacts in the transmitted radio signals. While these artifacts are often within official performance specifications, they are distinct for each device.

## 2. Features for Identification
- **Modulation Errors:** Deviations in the I/Q origin offset, frequency offset, or phase noise.
- **Turn-on Transients:** The short, unique signal pattern produced when a radio transmitter first switches from an idle to a transmitting state.
- **Clock Skew:** Small differences in the actual versus nominal clock frequency of the device's oscillator.

## 3. The Process
1. **Enrollment:** Capturing identification signals from known devices and storing their feature vectors (fingerprints) in a database.
2. **Identification (1:N):** Matching a new signal against the database to determine which specific device (or manufacturer class) it belongs to.
3. **Verification (1:1):** Confirming that a device is who it claims to be (e.g., checking if the radio fingerprint matches the claimed MAC address).

## 4. Key Properties
- **Universality:** Every device has some inherent physical characteristics.
- **Uniqueness:** Fingerprints should distinguish even between identical models from the same manufacturer.
- **Robustness:** Fingerprints must be stable over time and across different environmental conditions (temperature, voltage).

## 5. Attacks
- **Signal Replay:** An attacker records the analog signal of a target and replays it.
- **Feature Replay:** An attacker uses a high-end Signal Generator or Software Defined Radio (SDR) to synthesize a signal that specifically mimics the target's unique features.

## Related Concepts
- [[physically-unclonable-functions-puf]]
- [[physical-layer-key-establishment]]
- [[hardware-trojans-and-logic-locking]]
