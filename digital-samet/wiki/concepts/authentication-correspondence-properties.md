# Authentication Correspondence Properties

- **Source:** [[ka-aaa]]
- **Tags:** #aaa #authentication #formal-methods #verification

## Overview
Correspondence properties are formal requirements used to analyze the correctness of authentication protocols. They specify how the views of the **Prover (Responder)** and the **Verifier (Initiator)** must align at the end of a protocol run.

## Key Properties (Gavin Lowe Hierarchy)

### 1. Aliveness
Whenever the Verifier concludes a protocol run, the Prover must have been active (engaged in a run) at some point.
- **Minimal Requirement:** Proves the peer is "alive" but doesn't guarantee who they think they are talking to.

### 2. Weak Agreement
Whenever the Verifier concludes a protocol run apparently with a specific Prover, that Prover must have been engaged in a run apparently with that specific Verifier.
- **Focus:** Identity matching.

### 3. Non-Injective Agreement
Similar to weak agreement, but responder and receiver must also agree on a specific set of **Data Items** (e.g., nonces, session keys).
- **Focus:** Data consistency.

### 4. Agreement (Full Agreement)
The strongest property. It adds **Injectivity** to non-injective agreement: every run of the Verifier corresponds to a unique and distinct run of the Prover.
- **Focus:** Prevents replay attacks where one prover run is reused for multiple verifier sessions.

## Tooling
These properties are typically verified using symbolic analysis tools like **TAMARIN** or **ProVerif**. A violation of a property indicates a logic flaw in the protocol (e.g., the Public-Key Needham-Schroeder attack).

## Related Concepts
- [[symbolic-protocol-analysis]]
- [[federated-identity-protocols]]
- [[aaa-fundamental-concepts]]
