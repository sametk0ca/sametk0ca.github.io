# CPS Fundamental Characteristics

- **Source:** [[ka-cps-security]]
- **Tags:** #cps #embedded #real-time #control-theory

## Overview
Cyber-Physical Systems (CPSs) are defined by the conjoining of the engineering traditions of the cyber world (computation, communication) and the physical world (sensing, actuation, dynamics).

## 1. Embedded Systems Nature
- **Resource Constraints:** Devices often have limited CPU power, RAM, and energy (especially battery-powered sensors).
- **Bare-metal / Firmware:** Many low-level controllers run without a general-purpose operating system to minimize overhead and attack surface.
- **Specific Functionality:** Unlike general PCs, CPS agents usually perform a very narrow set of predefined tasks.

## 2. Real-Time Requirements
- **Determinism:** In safety-critical systems, the *timing* of a computation is as important as its *correctness*.
- **RTOS:** Use of Real-Time Operating Systems to guarantee task completion within strict deadlines (e.g., deploying an airbag or adjusting a flight surface).

## 3. Networked Control
- **Protocol Evolution:** Migration from isolated serial links (Modbus, DNP3) to IP-compatible networks (Modbus/TCP, IEC 61850).
- **Low-power Wireless:** Adoption of standards like WirelessHART, ZigBee, and 6LoWPAN for large-scale sensor deployments.
- **Networked Feedback Loops:** The controller may be geographically distant from the sensors/actuators, relying on the network for the feedback signal.

## 4. Control Theory Integration
- **Feedback Loops:** Sensors observe physical variables, controllers compute a response, and actuators apply it to reach a desired state.
- **Hybrid Systems:** Modeling systems using both continuous-time dynamics (differential equations for physics) and discrete-time logic (finite-state machines for computation).

## Related Concepts
- [[industrial-control-systems-ics-security]]
- [[physics-based-attack-detection]]
- [[cyber-physical-safety-and-integrity]]
