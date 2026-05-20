# Secure Development Lifecycle (SDL) and DevSecOps

- **Source:** [[ka-secure-software-lifecycle]]
- **Tags:** #sdlc #devsecops #agile #process

## Overview
A Secure Development Lifecycle (SDL) is a proactive approach to building security into software from the earliest planning stages to decommissioning. **DevSecOps** is the modern evolution where security is integrated into rapid, automated delivery pipelines (CI/CD).

## 1. Traditional SDL (e.g., Microsoft SDL)
Focuses on discrete security activities at each phase of the waterfall or spiral model:
- **Training:** Building security awareness for all roles.
- **Requirements:** Defining security and privacy standards.
- **Design:** Using threat modeling and secure design principles.
- **Implementation:** Secure coding standards and tool-based review.
- **Verification:** SAST, DAST, and manual penetration testing.
- **Release:** Incident response planning and final security review.

## 2. DevSecOps (Secure DevOps)
In highly iterative environments, security must be automated to avoid slowing down delivery.
- **Continuous Integration (CI):** Automated security gates (SAST, SCA) run on every code commit.
- **Continuous Delivery (CD):** Automated configuration scanning and DAST run in staging environments.
- **Continuous Monitoring:** Instrumentation to detect "abnormal" behavior in production (supporting Mean Time to Contain - MTTC).
- **Compliance as Code:** Automating audits and policy checks within the pipeline.

## 3. Key Principles
- **Shift Left:** Moving security activities earlier in the lifecycle (where fixing bugs is cheaper).
- **Automation:** Reducing human error and ensuring consistent checks.
- **Feedback Loops:** Ensuring developers get security findings immediately within their IDE or PR process.

## Related Concepts
- [[threat-modeling-stride]]
- [[fuzz-testing-techniques]]
- [[software-security-foundations]]
