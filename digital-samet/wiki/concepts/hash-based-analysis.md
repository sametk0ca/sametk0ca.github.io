# Hash-based Analysis

- **Source:** [[ka-forensics]]
- **Tags:** #forensics #hashing #integrity

## Overview
Hash-based analysis uses cryptographic hashing to identify known files, validate data integrity, and discover file fragments.

## Main Techniques

### 1. Whole-File Hashing
- **Integrity Validation:** Computing hashes for an entire forensic target (drive, partition) to demonstrate evidence integrity across the chain of custody.
- **File Identification:** Matching file hashes against known sets (e.g., NIST's NSRL) to:
    - **Filter Out:** Remove common OS and application files.
    - **Pinpoint:** Identify known malware or contraband.

### 2. Block-Level Hashing
- **Fragment Discovery:** Splitting files into fixed-size blocks (e.g., 4 KiB) to identify fragments of known files on a disk or RAM image.
- **High-Entropy Identification:** Identifying compressed or encrypted data which has high entropy.
- **Improving Carving:** Excluding known blocks before performing the carving process to reduce false positives.

## Core Properties
- **Collision Resistance:** It is computationally infeasible to find two different inputs with the same hash output (e.g., SHA-2, SHA-3).
- **Efficiency:** Hash-based filtering is fast and computationally affordable.

## Reference Databases
- **NSRL (National Software Reference Library):** Maintained by NIST, covers common software installations.

## Related Concepts
- [[approximate-matching]]
- [[data-carving]]
- [[forensic-investigative-process]]
