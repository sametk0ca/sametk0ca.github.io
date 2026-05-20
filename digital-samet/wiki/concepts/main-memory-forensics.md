# Main Memory Forensics

- **Source:** [[ka-forensics]]
- **Tags:** #forensics #ram #volatile-memory

## Overview
Main memory forensics involves extracting and analyzing the run-time state of a system from volatile memory (RAM). Data in RAM is increasingly critical for recovering encryption keys and open network connections.

## Key Information Extracted
- **Process Information:** Enumerating running processes, threads, loaded modules, stack, heap, and code segments.
- **File Information:** Identifying open files, shared memory, and anonymously mapped memory (shows user intent).
- **Network Connections:** Open/recently closed connections, protocol info, and data queues.
- **Artifacts and Fragments:** Traces of disk and network data cached in memory for long periods.

## Acquisition and Analysis
- **Live Forensics:** Using a trusted pre-installed agent for real-time remote snapshots.
- **Snapshot Analysis:** Analyzing a raw memory dump (snapshot). More difficult due to the "semantic gap".
- **The Semantic Gap:** The problem of extracting meaningful OS-level information (processes, files) from a raw sequence of bits in a memory dump.

## Alternative Sources
Memory content can also be found in:
- System hibernation files.
- Page/swap files.
- Crash dumps.

## Related Concepts
- [[storage-abstraction-layers]]
- [[soim-data-sources]]
- [[malware-analysis-methods]]
