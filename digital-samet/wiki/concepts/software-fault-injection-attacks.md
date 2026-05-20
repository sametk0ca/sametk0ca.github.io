# Software-Based Fault Injection (Rowhammer)

- **Source:** [[ka-software-security]]
- **Tags:** #software-security #hardware #vulnerabilities #rowhammer

## Overview
Fault injection attacks aim to modify the execution state of a system to induce errors that can be exploited. While traditionally physical, some attacks can be performed purely through software.

## Rowhammer Attack
The most prominent software-based fault injection attack exploiting hardware implementation details.
- **Physical Cause:** High-density DRAM cells are placed close together. Rapidly accessing (hammering) one row of memory cells causes electrical interference (crosstalk).
- **Effect:** The electrical charge in adjacent rows can leak, causing bits to flip (0 to 1 or vice versa) even if those rows were never accessed by the software.
- **Security Impact:** If an attacker can flip a bit in a security-critical location (e.g., a page table entry, a cryptographic key, or a boolean flag like `is_root`), they can bypass all software-level isolation.

## Other Hardware-Software Interface Threats
- **Side-Channels:** Spectre and Meltdown exploit speculative execution to leak data across security domains.
- **Voltage/Clock Glitching:** (Usually physical) Inducing errors by momentarily dropping the CPU voltage or manipulating the clock signal.

## Mitigations
- **Target Row Refresh (TRR):** Hardware-level mitigation in newer DRAM to refresh adjacent rows more frequently.
- **Disabling Optimizations:** Turning off features like memory deduplication which can assist in Rowhammer exploitation.
- **Error Correcting Code (ECC) Memory:** Can detect and sometimes correct single-bit flips, making Rowhammer much harder.

## Related Concepts
- [[hardware-security-vulnerabilities]]
- [[side-channel-formal-analysis]]
- [[memory-protection-mechanisms]]
