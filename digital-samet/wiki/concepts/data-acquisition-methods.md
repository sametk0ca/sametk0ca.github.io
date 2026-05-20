# Data Acquisition Methods

- **Source:** [[ka-forensics]]
- **Tags:** #forensics #acquisition

## Overview
Data acquisition is the process of obtaining a working copy of a forensic target for analysis. Best practices involve analyzing data at rest on an exact bit-wise copy.

## Main Acquisition Types

### Physical Acquisition
- **Description:** Obtaining data directly from the hardware media without untrusted software mediation.
- **Methods:**
    - **Chip-off:** Physically removing and reading memory chips (destructive).
    - **JTAG:** Using standard testing/debugging hardware interfaces.
    - **Imaging (Pseudo-physical):** Using HBA protocols (SATA/SCSI/NVMe) to get block-level copies.
- **Benefit:** Access to over-provisioned "shadow storage" and area outside filesystem limits.

### Logical Acquisition
- **Description:** Relying on software layers (APIs, protocols) to acquire data.
- **Benefit:** Closer to user actions and application structures.
- **Risk:** Depends on the integrity and correctness of the API implementation.

## Integrity Measures
- **Write Blocking:** Hardware write blockers prevent accidental modification of target media.
- **Cryptographic Hashing:** Computed for the whole image and (ideally) for every block to demonstrate integrity.
- **Validation:** Independent testing (e.g., NIST's CFTT project) to verify tool reliability.

## Challenges

### 1. Data Consistency (Data Smearing)
- Occurs when imaging a live system. Not an issue in virtualized environments with snapshot mechanisms.

### 2. Encryption
- Pervasive by default. Frustrates analysis.
- **Technical Subversion:** Finding bugs, implementation errors, or administrative flaws.
- **Legal Compulsion:** Compelling key disclosure (e.g., RIPA 2000 in UK).

## Related Concepts
- [[forensic-investigative-process]]
- [[storage-abstraction-layers]]
- [[filesystem-forensics]]
