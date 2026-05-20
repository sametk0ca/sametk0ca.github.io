# Model Checking Basics

- **Source:** [[ka-formal-methods]]
- **Tags:** #formal-methods #model-checking #verification

## Overview
Model checking is an automated technique for verifying that a finite-state model of a system satisfies a given property, typically specified in temporal logic.

## Key Components
1. **The Model:** A state-transition system (Kripke structure) representing all possible system behaviors.
2. **The Specification:** A logical formula, usually in **Linear Temporal Logic (LTL)** or **Computation Tree Logic (CTL)**.
3. **The Search:** The tool exhaustively explores the state space. If a violation is found, it provides a **Counter-example** (a trace showing how the error occurs).

## Common Temporal Operators
- **G (Globally):** The property must hold in every state of the trace.
- **F (Finally):** The property must hold at some point in the future.
- **X (Next):** The property must hold in the next state.

## Advanced Variants
- **Symbolic Model Checking:** Uses efficient data structures (like BDDs or SMT solvers) to handle large state spaces without explicit enumeration.
- **Probabilistic Model Checking:** Reasons about systems with stochastic behaviors (e.g., randomized protocols).
- **Hyperproperty Model Checking:** Specialized algorithms to check relations between traces (e.g., non-interference).

## Tools
- **SPIN:** General-purpose, uses Promela language.
- **NuSMV:** Symbolic model checker.
- **PRISM:** Probabilistic model checker.
- **FDR:** Refinement checker based on CSP process calculus.

## Related Concepts
- [[formal-methods-foundations]]
- [[hyperproperties-and-trace-properties]]
- [[symbolic-protocol-analysis]]
