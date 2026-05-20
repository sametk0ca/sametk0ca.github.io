# GNSS Spoofing and Takeover Attacks

- **Source:** [[ka-physical-layer-security]]
- **Tags:** #physical-layer #gps #gnss #spoofing #attacks

## Overview
Global Navigation Satellite Systems (GNSS), such as GPS and Galileo, are critical for positioning and timing. However, civilian signals are unencrypted and unauthenticated, making them vulnerable to physical layer spoofing.

## 1. Attack Objective
- **Incorrect Position:** Tricking a receiver (e.g., a ship or drone) into believing it is at a different location.
- **Incorrect Time:** Manipulating the precise atomic clock time provided by satellites, which is vital for telecommunications and financial markets.
- **Disruption:** Causing the receiver to lose its lock and stop functioning.

## 2. Spoofing Classifications

### Non-Coherent Spoofing
The attacker uses a signal generator to transmit authentic-looking GPS signals that are not synchronized with the real signals.
- **Detection:** Relatively easy, as the receiver will see a sudden jump in signal power or a loss of lock before re-acquiring the fake signal.

### Coherent Spoofing (Seamless Takeover)
The strongest form of attack. The attacker's signal is perfectly synchronized with the legitimate satellite signal currently being received.
- **Process:**
    1. Attacker transmits synchronized signals at a lower power than the real ones.
    2. Attacker gradually increases power until the receiver's tracking loops "lock" onto the malicious signal.
    3. Once the takeover is complete, the attacker slowly introduces a temporal or data shift to lead the receiver to a false position.
- **Detection:** Extremely difficult because the transition is invisible to standard receivers.

## 3. Vulnerability of Civilian GPS
Civilian GPS uses publicly known spreading codes (C/A code) and data structures. This allows any attacker with a Software Defined Radio (SDR) to synthesize fake signals. Military GPS uses encrypted codes (P(Y) code) to prevent this, but it doesn't scale for general use.

## 4. Detection and Mitigation
- **Anomaly Detection:** Monitoring signal-to-noise ratio, number of visible satellites, and carrier phase consistency.
- **Multiple Antennas:** Checking if the signal arrival angle matches the expected satellite positions.
- **Signal Authentication:** Implementing cryptographic signatures in the navigation message (e.g., Galileo OS-NMA).
- **Inertial Fusion:** Cross-checking GNSS data with internal sensors (accelerometers, gyroscopes).

## Related Concepts
- [[transduction-attacks-on-sensors]]
- [[distance-bounding-and-relay-attacks]]
- [[network-attacker-models]]
