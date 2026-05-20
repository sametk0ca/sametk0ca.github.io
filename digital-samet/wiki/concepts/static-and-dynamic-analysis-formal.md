# Static and Dynamic Analysis (Formal Perspectives)

- **Source:** [[ka-formal-methods]]
- **Tags:** #formal-methods #static-analysis #dynamic-analysis #taint-analysis

## Overview
Program analysis tools range from fully automated, scalable static analyzers to real-time execution monitors.

## 1. Static Analysis
Analyzes program source or object code without execution.
- **Approach:** Uses **Abstract Interpretation** to approximate all possible executions.
- **Taint Analysis:** Tracks the flow of data from untrusted sources (inputs) to sensitive sinks (e.g., system calls, SQL queries).
- **Soundness vs. Precision:**
    - **Sound Tools:** Guarantee no false negatives (if they say it's clean, it really is) but may have false positives.
    - **Heuristic Tools:** Find bugs efficiently but may miss subtle vulnerabilities.
- **Examples:** CodeSonar, Coverity, Fortify.

## 2. Dynamic Analysis (Runtime Verification)
Checks properties while the system is running.
- **Mechanism:** A **Monitor** program observes an evolving execution trace and checks it against a formal specification (e.g., past-time temporal logic).
- **Benefit:** No false positives for safety properties; works on the real system in its actual environment.
- **Limitation:** Can only detect violations in the *observed* executions (weak guarantees compared to verification).
- **Examples:** MonPoly (monitoring security policies).

## Industrial Adoption
Large organizations like **Google** and **Amazon** integrate these tools into their CI/CD pipelines.
- **Google:** Focuses on pattern-matching and lightweight abstract interpretation to suggest fixes during code review.
- **Amazon:** Uses formal tools like **TLA+** for critical components (hypervisors, crypto libraries) alongside broad static analysis.

## Related Concepts
- [[model-checking-basics]]
- [[os-hardening-techniques]]
- [[adversary-modeling-in-formal-methods]]
