# Filesystem Forensics

- **Source:** [[ka-forensics]]
- **Tags:** #forensics #filesystem #storage

## Overview
Filesystem forensics uses knowledge of data structures and algorithms to extract content independently of the OS and access artifacts the standard API does not provide.

## Core Concepts

### 1. Storage Organization
- **Blocks/Sectors:** Fixed-size units (historically 512 bytes, now 4096 bytes).
- **Clusters:** Contiguous sequences of blocks (smallest allocation unit).
- **Partitions:** Contiguous areas of raw drive for a designated use.
- **Volumes:** Logical abstractions of partitions (can span multiple devices).

### 2. Filesystem Definition
- **File:** A named (opaque) sequence of bytes stored persistently. Interpretation is outside OS purview (handled by applications).
- **Filesystem:** An OS subsystem responsible for persistent storage and organization of files on a partition/volume. Provides standard APIs (e.g., POSIX).

## Forensic Value
Filesystem forensics enables access to:
- **Deallocated Files:** Parts of deleted files not yet overwritten.
- **Hidden Data:** Purposefully placed data in areas outside normal file storage.
- **Implied History:** Reconstructing file creation/deletion from filesystem structural changes.

## Analysis Techniques
- **Metadata Analysis:** Examining file names, sizes, timestamps, and permissions.
- **Structural Analysis:** Understanding on-disk layout of directories and file tables (e.g., MFT in NTFS).
- **Integrity Checks:** Ensuring security compromises or anti-forensics (e.g., modified timestamps) do not skew the analysis.

## Related Concepts
- [[storage-abstraction-layers]]
- [[data-carving]]
- [[data-acquisition-methods]]
