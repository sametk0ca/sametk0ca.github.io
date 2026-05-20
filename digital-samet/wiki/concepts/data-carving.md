# Data Carving

- **Source:** [[ka-forensics]]
- **Tags:** #forensics #recovery #data-carving

## Overview
Data (structure) carving is the process of reconstructing logical objects (files, database records) from bulk data captures (disk/RAM images) without using metadata that describes their location.

## Key Process: File Content Carving
Reconstructing file content directly from block storage using format knowledge. It relies on two observations:
1. **Headers/Footers:** Many file formats have unique starting and ending tags (e.g., JPEG starts with `FF D8 FF` and ends with `FF D9`).
2. **Sequential Layout:** Filesystems favor sequential storage for throughput.

## Carving Algorithm (Basic)
1. **Scan** sequentially for a known header.
2. **Scan** sequentially for a corresponding footer.
3. **Copy** the data in between as a recovered artifact.

## Challenges: File Fragmentation
Carving is complicated when file content is not contiguous:
- **No Fragmentation:** Simple header-footer matching.
- **Nested Content:** A file (A) replaced deleted content around another (B). B is extracted first, making A contiguous.
- **Bi-fragmented Files:** Split into two contiguous pieces with other content in between.
- **Interleaved Content:** Multiple files mixed, often due to small gap filling.

## Significance
Carving is essential for recovering:
- **Deleted Files:** Reversing 'undelete' after filesystem metadata has been removed (e.g., by a "quick format").
- **Parts of Overwritten Files:** Reassembling remaining blocks of partially lost data.

## Related Concepts
- [[filesystem-forensics]]
- [[storage-abstraction-layers]]
- [[forensic-traces]]
