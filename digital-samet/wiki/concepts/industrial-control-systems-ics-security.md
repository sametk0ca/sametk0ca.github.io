# Industrial Control Systems (ICS) Security

- **Source:** [[ka-cps-security]]
- **Tags:** #cps #ics #scada #plc #ot

## Overview
Industrial Control Systems (ICS) manage physical processes in critical infrastructure (water, oil, gas, chemical plants). Unlike standard IT, the priority in ICS is **Availability** and **Safety**.

## 1. Architecture: The Purdue Model
The standard model for segmenting ICS networks into layers:
- **Level 4/5 (Enterprise):** Business logistics and corporate IT.
- **Level 3 (Supervisory):** SCADA systems, HMI (Human Machine Interface), and data historians.
- **Level 2 (Control):** PLCs (Programmable Logic Controllers) and RTUs (Remote Terminal Units) executing control logic.
- **Level 0/1 (Process/Field):** Physical sensors and actuators (pumps, valves, motors).

## 2. Key Components
- **SCADA (Supervisory Control and Data Acquisition):** High-level monitoring and control over large geographic areas.
- **PLC:** Robust industrial computers that perform real-time regulatory control.
- **HMI:** Graphical interface for human operators to interact with the process.

## 3. Notable ICS Malware
Sofiticated, often state-sponsored tools designed for sabotage:
- **Stuxnet (2010):** Targeted Siemens PLCs in an Iranian nuclear facility. It manipulated motor speeds to destroy centrifuges while replaying normal sensor data to the HMI.
- **Industroyer (2016):** Automated attack on the Ukrainian power grid. Included modules for industrial protocols (IEC 104, DNP3).
- **Triton/Trisis (2017):** Specifically targeted Safety Instrumented Systems (SIS) from Schneider Electric. Designed to disable safety protections, potentially leading to life-threatening accidents.

## 4. Security Strategies
- **Network Segmentation:** Using firewalls and data diodes to isolate the Control Network from the Enterprise Network.
- **Protocol Security:** Upgrading legacy unauthenticated protocols to secure versions (e.g., IEC 62351).
- **Intrusion Detection:** Using NIDS optimized for OT protocols and **Physics-Based Detection** to identify anomalies in process variables.

## Related Concepts
- [[cps-fundamental-characteristics]]
- [[physics-based-attack-detection]]
- [[smart-grid-security-threats]]
