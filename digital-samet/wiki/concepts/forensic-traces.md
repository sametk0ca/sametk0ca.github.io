# Forensic Traces

- **Source:** [[ka-forensics]]
- **Tags:** #forensics #traces

## Overview
A digital (forensic) trace is an explicit or implicit record that testifies to the execution of specific computations, communications, or data storage events.

## Types of Traces

### Explicit Traces
- **Description:** Directly record the occurrence of events as part of normal system operation.
- **Examples:** System event logs (e.g., Windows Event Logs, syslog) and application logs.

### Implicit Traces
- **Description:** Allow the occurrence of events to be deduced from the observed state of the system, based on engineering knowledge.
- **Examples:** Deleted file fragments (deduced from disk state), metadata (file access times), or missing logs (indicating a cover-up).

## Engineering and Traces
- **Engineering Reality:** Traces are typically the result of conscious engineering decisions aimed at system functionality, not forensic utility.
- **Provenance and Authenticity:** Because digital information is easily modified, the provenance and authenticity of traces are critical challenges.
- **Locard's Exchange Principle:** While physical contact inevitably results in a trace, digital traces are neither inevitable nor a "natural" consequence of digital processing.

## Related Concepts
- [[digital-forensics-definitions]]
- [[forensic-conceptual-models]]
- [[soim-data-sources]]
