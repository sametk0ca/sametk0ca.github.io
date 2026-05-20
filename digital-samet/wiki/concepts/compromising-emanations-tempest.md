# Compromising Emanations (TEMPEST)

- **Source:** [[ka-physical-layer-security]]
- **Tags:** #physical-layer #tempest #side-channel #surveillance

## Overview
Compromising emanations are unintended signals (electromagnetic, acoustic, optical, or thermal) radiated by electronic devices that correlate with the confidential information being processed. The study and mitigation of these leaks is known as **TEMPEST**.

## 1. Categories of Emanations

### Electromagnetic (EM)
The most common type. Switching activities in CPUs, GPUs, and cables create radio frequency noise.
- **Van Eck Phreaking:** Reconstructing the image on a display by capturing and processing the EM radiation from the monitor or its cable (e.g., VGA or HDMI).
- **LED Leakage:** Using a high-speed photodiode to monitor the flickering of status LEDs (e.g., hard drive or network indicators) which can leak bits of data.

### Acoustic
Information leaking through sound or vibration.
- **Capacitor Squeal:** High-frequency sounds from voltage regulators on a motherboard can reveal information about the CPU load and, in some cases, cryptographic keys (e.g., prime factorization steps).
- **Keyboard Sound:** Inferring what a user is typing by analyzing the unique sound signature of each key press captured by a nearby microphone.

### Optical
Leaking information via light reflections.
- **Screen Reflections:** Reconstructing what is on a computer screen by analyzing reflections from household objects like spoons, bottles, or even the user's retina.

## 2. Exploitation Conditions
Historically, TEMPEST required expensive, specialized receivers. Today, the ubiquity of high-quality sensors in smartphones (cameras, microphones, accelerometers) makes these attacks much more accessible to low-budget adversaries.

## 3. Protective Measures
- **Shielding (Faraday Cages):** Enclosing sensitive equipment in grounded metal structures to block EM radiation.
- **Filtering:** Adding low-pass filters to power and communication lines to remove high-frequency noise.
- **Zoning (Distance):** Keeping sensitive equipment far away from walls or areas where an attacker could place a receiver.
- **Jamming (Noise Injection):** Intentionally generating random EM noise to drown out the compromising signals.
- **Redaction:** Using specialized fonts or display modes that minimize the EM signature of sensitive characters.

## Related Concepts
- [[side-channel-attacks-and-masking]]
- [[constant-time-cryptography]]
- [[hardware-isolation-technologies]]
