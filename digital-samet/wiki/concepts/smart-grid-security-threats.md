# Smart Grid Security Threats

- **Source:** [[ka-cps-security]]
- **Tags:** #cps #smart-grid #energy #attacks #privacy

## Overview
The modernization of the electrical power grid (Smart Grid) involves integrating renewable energy, smart meters, and bidirectional communication. While improving efficiency, it introduces new cyber and physical attack vectors.

## 1. False Data Injection (FDI) Attacks
The most studied threat in power systems.
- **Mechanism:** Attackers compromise a subset of sensors (RTUs or PMUs) and inject carefully crafted false readings.
- **Target:** **State Estimation** algorithms. By bypassing "bad data detection" (which assumes random faults), the attacker tricks the grid operator into seeing a different system state.
- **Impact:** Misguided control decisions, resulting in physical damage to transformers, line overflows, or localized blackouts.

## 2. Load-Altering Attacks (LAA)
Exploiting the growing number of high-wattage IoT devices (e.g., smart air conditioners, water heaters, EV chargers).
- **Mechanism:** Using an IoT botnet to simultaneously turn these devices on or off.
- **Impact:**
    - **Frequency Instability:** Rapid changes in demand can cause the grid frequency to drop or spike, triggering protective relay trips.
    - **Economic Manipulation:** Causing sudden spikes in demand to manipulate energy market prices.
    - **Cascading Failures:** Forcing the system to violate safety margins (N-1 criterion).

## 3. Privacy Threats
Smart meters collect energy usage data at high granularity (e.g., every 15 minutes).
- **Information Leakage:** Usage patterns can reveal if a user is home, what appliances they are using (Non-Intrusive Load Monitoring - NILM), and their daily routines.
- **Surveillance:** This data can be exploited by advertisers, insurers, or criminals (e.g., identifying when a house is empty for a burglary).

## 4. Protection Systems Under Attack
Attackers can target the configuration of protection equipment (e.g., under-frequency load shedding - UFLS).
- **Scenario:** If an attacker disables UFLS, a minor failure that the grid should normally survive can escalate into a national blackout.

## Related Concepts
- [[physics-based-attack-detection]]
- [[industrial-control-systems-ics-security]]
- [[cyber-physical-safety-and-integrity]]
