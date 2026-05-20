# Side-Channel Attacks and Masking

- **Source:** [[ka-hardware-security]]
- **Tags:** #hardware-security #side-channel #attacks #countermeasures #masking

## Overview
Side-channel attacks exploit physical information leaked by a hardware device during computation (e.g., power consumption, timing, EM radiation) to recover secret keys.

## 1. Attack Types

### Simple Power Analysis (SPA)
Directly observing power traces to identify key-dependent branches (e.g., the "if" branch in RSA taking more time than the "else").

### Differential Power Analysis (DPA)
Collecting thousands or millions of power traces and using statistical correlation to reveal sub-keys based on data-dependent power variations.

### Electromagnetic (EM) Analysis
Measuring localized EM radiation from the chip surface. Provides more granular information than global power consumption.

### Transient Execution Attacks
Exploiting micro-architectural side-effects (e.g., cache hits/misses) of instructions that were executed speculatively but eventually discarded (e.g., **Spectre**, **Meltdown**).

## 2. Countermeasures

### Constant-Time Execution
Ensuring the algorithm takes the same number of cycles/instructions regardless of the data or key bits. This eliminates timing side-channels.

### Masking
The most prominent countermeasure at the logic level.
- **Mechanism:** Secrets are split into multiple random shares (e.g., $Secret = x \oplus y$). The hardware performs calculations on these shares independently.
- **Goal:** The power consumption of any single share is statistically independent of the secret.
- **Cost:** Significant increase in area, randomness requirement, and power.

### Hiding
Reducing the signal-to-noise ratio.
- **Methods:** Adding noise, using jittery clocks, or using specialized dual-rail logic styles that consume constant power regardless of data transitions.

### Blinding
Applying random values to inputs (scalar/message blinding) at the algorithm level to prevent SPA/DPA on public-key operations.

## Related Concepts
- [[constant-time-cryptography]]
- [[side-channel-formal-analysis]]
- [[hardware-security-vulnerabilities]]
