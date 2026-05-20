# Physics-Based Attack Detection

- **Source:** [[ka-cps-security]]
- **Tags:** #cps #detection #control-theory #physics

## Overview
Physics-based attack detection uses models of physical laws and the system's expected dynamics to identify anomalies in sensor data or control signals that "cyber-only" intrusion detection systems might miss.

## 1. Core Idea
Classical IDSs monitor network packets and OS logs. Physics-based IDSs monitor the *physical evolution* of the system. If a sensor reports a trajectory that is physically impossible or inconsistent with current control actions, an alert is raised.

## 2. Detection Classes

### Physical-Law Anomalies
Checks if sensor readings violate fundamental physical principles.
- **Example:** In a water tank, if the intake valve is closed, the water level cannot rise. If a sensor reports a rise, it is either faulty or under attack.
- **Advantage:** Low false alarm rate for "impossible" events.

### Historical Anomalies
Uses machine learning to identify data patterns never seen before.
- **Example:** A power grid configuration that has never occurred in 10 years of operation might indicate a coordinated attack.
- **Limitation:** May generate more false alarms due to legitimate but rare system states.

## 3. Passive vs. Active Detection

### Passive Monitoring
Continuously correlating sensor values against a mathematical model (e.g., using a Kalman Filter to predict the next state).

### Active Detection (Physical Attestation)
Intentionally injecting a small "probe" or "watermark" into the physical process and verifying that the sensors report the expected reaction.
- **Example:** Briefly changing a motor's speed and checking if the tachometer reflects the change. If the sensor reports a constant speed, the attacker is likely replaying old valid data.

## 4. Challenges
- **Model Inaccuracy:** Real-world systems are noisy and complex; models are always approximations.
- **Stealthy Attacks:** Attackers who know the model can inject false data that stays just within the margin of error (e.g., "bias injection" attacks) to slowly drive the system to a dangerous state.

## Related Concepts
- [[cps-fundamental-characteristics]]
- [[transduction-attacks-on-sensors]]
- [[industrial-control-systems-ics-security]]
