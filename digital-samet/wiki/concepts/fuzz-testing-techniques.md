# Fuzz Testing Techniques (Fuzzing)

- **Source:** [[ka-software-security]]
- **Tags:** #software-security #detection #testing #fuzzing

## Overview
Fuzzing is an automated dynamic analysis technique that involves providing a large volume of random, semi-random, or malformed inputs to a program to trigger crashes or unexpected behavior (witnessing vulnerabilities).

## Core Taxonomies

### 1. Black-box Fuzzing
The fuzzer has no knowledge of the program's internal structure.
- **Random Fuzzing:** Purely random bits as input.
- **Model-based (Grammar) Fuzzing:** Follows a predefined specification of the input format (e.g., PDF or network protocol) to bypass early parsing checks.
- **Mutation-based Fuzzing:** Takes existing valid inputs and performs small changes (flips, swaps) to them.

### 2. White-box Fuzzing
The fuzzer analyzes the program's structure to guide input generation.
- **Dynamic Symbolic Execution (DSE):** Executes the program with concrete values while maintaining "symbolic" constraints for branches. It uses an SMT solver to find new inputs that flip branch decisions, maximizing code coverage.

### 3. Grey-box Fuzzing
Uses lightweight feedback (e.g., edge coverage) from the program during execution to evolve the input pool.
- **Example:** AFL (American Fuzzy Lop) uses instrumentation to detect which inputs exercise new parts of the code.

## Fuzzing Process
1. **Target Identification:** Choosing the software component to test.
2. **Input Generation:** Creating the fuzzing data.
3. **Execution:** Running the target with the data.
4. **Monitoring:** Detecting crashes, hangs, or memory errors (e.g., via AddressSanitizer).
5. **Triage:** Analyzing crashes to determine if they are security-critical vulnerabilities.

## Related Concepts
- [[static-and-dynamic-analysis-formal]]
- [[software-security-foundations]]
- [[memory-management-vulnerabilities]]
