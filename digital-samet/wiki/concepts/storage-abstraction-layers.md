# Storage Abstraction Layers

- **Source:** [[ka-forensics]]
- **Tags:** #forensics #storage #architecture

## Overview
Forensic analysis of storage devices can be performed at several levels of abstraction. Each layer builds an increasingly abstract representation, starting from raw physical bits to user-facing application artifacts.

## The Four Main Layers

### 1. Physical Media
- **Description:** The lowest level where bits are encoded (HDDs, SSDs, Flash).
- **Forensic Approach:** Bit-by-bit extraction using custom mechanisms, chip-off (desoldering chips), or debugging interfaces (JTAG).
- **Challenge:** Expensive, time-consuming, and may require reverse engineering.

### 2. Block Device
- **Description:** Presents the medium as a sequence of fixed-size blocks (e.g., 512 or 4096 bytes).
- **Forensic Approach:** Imaging (bit-wise copying) via standard protocols like SATA, SCSI, or NVMe.
- **Terminology:** Sectors (magnetic disks), Logical Blocks (general term).

### 3. File System
- **Description:** Organizes block storage into files and directories with metadata (names, sizes, timestamps).
- **Forensic Approach:** Independent reconstruction of file-based storage out of constituent blocks using knowledge of filesystem structures (e.g., NTFS, Ext4).

### 4. Application Artifacts
- **Description:** High-level objects used by applications (documents, messages, images) or the OS (logs, registry, binaries).
- **Forensic Approach:** Yields most immediately relevant results regarding human actions and communications.

## Importance of Independent Reconstruction
Reconstructing artifacts from lower levels (instead of using the OS API) is critical for:
- Recovering data not available through the normal interface (deleted/hidden).
- Recovering partially overwritten data.
- Discovering malware that has subverted the OS.

## Related Concepts
- [[data-acquisition-methods]]
- [[filesystem-forensics]]
- [[data-carving]]
