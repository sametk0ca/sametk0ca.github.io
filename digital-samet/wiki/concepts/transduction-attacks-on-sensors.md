# Transduction Attacks on Sensors (Analog Attacks)

- **Source:** [[ka-cps-security]]
- **Tags:** #cps #attacks #sensors #analog #transduction

## Overview
A transduction attack targets the *physical interface* of a sensor (the transducer) rather than its software. It manipulates the physical environment to inject false signals into the digital system without needing a computer exploit.

## 1. Mechanism
Sensors translate a physical property (e.g., sound, light, temperature) into an electrical signal. Many sensors have unintentional "couplings" with other physical phenomena.
- **Example:** An accelerometer (designed to measure movement) might unintentionally vibrate in response to high-frequency sound waves (resonance).

## 2. Attack Examples
- **Acoustic Injection:** Using ultrasonic or audible speakers to interfere with gyroscopes in drones, causing them to crash or behave erratically.
- **Electromagnetic Interference (EMI):** Using intentional EM waves to trick sensors (e.g., medical devices or industrial temperature sensors) into reporting false values.
- **Optical Injection:** Using lasers or bright lights to blind or spoof LiDAR/Cameras in autonomous vehicles.
- **Signal Clipping:** Overpowering a sensor's input so that it saturates, hiding real signals or creating "ghost" readings.

## 3. Key Differentiator
In a traditional cyber-attack, the attacker modifies the *digital value* in the controller's memory. In a transduction attack, the attacker makes the sensor *truthfully report* a false physical reality. This bypasses cryptographic authentication because the malicious signal is generated at the source.

## 4. Countermeasures
- **Physical Shielding:** Encasing sensors in materials that block unintentional signals (EM shields, acoustic foam).
- **Redundancy & Sensor Fusion:** Correlating data from multiple, different types of sensors (e.g., verifying a LiDAR distance with a Radar reading).
- **Filtering:** Using low-pass or band-pass filters to remove signals outside the expected operating frequency.
- **Anomaly Detection:** Monitoring the physics of the system to identify "impossible" sensor behavior.

## Related Concepts
- [[physics-based-attack-detection]]
- [[hardware-security-vulnerabilities]]
- [[cps-fundamental-characteristics]]
