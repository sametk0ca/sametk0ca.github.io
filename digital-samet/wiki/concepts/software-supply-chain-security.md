# Software Supply Chain Security & SLSA

- **Source:** [[slsa-supply-chain-2024]]
- **Tags:** #supply-chain #slsa #sbom #devsecops #modern-security

## Overview
Modern software is rarely built from scratch; it relies on complex supply chains of libraries, build tools, and CI/CD pipelines. Attackers (e.g., SolarWinds, XZ Utils) exploit these dependencies to inject malicious code into trusted software.

## SLSA Framework (2024)
**SLSA (Supply Chain Levels for Software Artifacts)** provides a standard for ensuring the integrity of software artifacts.
- **Core Concept:** Verifiable **Provenance** (metadata describing how, when, and where a piece of software was built).

### SLSA Levels (Build Track)
- **Level 1:** Documented build process with basic provenance.
- **Level 2:** Provenance is cryptographically signed by the build service.
- **Level 3:** Build environment is hardened and isolated from other builds to prevent cross-contamination.

## SBOM (Software Bill of Materials)
A formal list of all components, versions, and dependencies in a software package. Enables organizations to quickly identify if they are vulnerable to a newly discovered CVE (e.g., Log4Shell).

## Related Concepts
- [[sdl-and-devsecops]]
- [[software-security-foundations]]
- [[malware-evasion-techniques]]
