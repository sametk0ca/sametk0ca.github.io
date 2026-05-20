# Forensic Conceptual Models

- **Source:** [[ka-forensics]]
- **Tags:** #forensics #models

## Overview
Forensic conceptual models provide frameworks for rebuilding the sequence of events from available digital data sources.

## Primary Approaches

### State-Centric Models
- **Description:** Starting point is a "snapshot" of the system's state at a single point in time.
- **Example:** Forensic imaging of a hard drive or storage medium.
- **Mechanism:** Knowledge of system/application operation is used to deduce a prior state (e.g., if file fragments are present but the file is not available through the OS, it was likely deleted).
- **Constraint:** Limited historical data points; difficult to deduce exact timing or a sequence of many past states.

### Log-Centric (History-Centric) Models
- **Description:** Relies on an explicit, timestamped history of events that document updates to the system's state over time.
- **Example:** Packet captures (pcap), operating system monitoring logs, application transaction logs.
- **Advantage:** Provides a more direct reconstruction of the sequence of events.

## Related Concepts
- [[digital-forensics-definitions]]
- [[forensic-traces]]
- [[soim-fundamental-concepts]]
