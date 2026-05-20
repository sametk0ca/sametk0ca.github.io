---
concept: Developer-Centric Security
source: [[ka-human-factors]]
tags: [concept, human-factors, developers, cybok]
---

# Concept: Developer-Centric Security

## Overview
Usability challenges affect not only end-users but also highly technical users like software developers and system administrators. Errors at this level (e.g., Heartbleed) can have catastrophic systemic impacts.

## Challenges for Developers
- **Task Focus**: Like end-users, developers often view security as a secondary task relative to functional requirements.
- **API Complexity**: Many cryptographic libraries and security APIs are difficult to use correctly, leading to implementation errors.
- **Pressure**: Extreme pressure to complete applications quickly often leads to security being deprioritized.
- **Support Systems**: Developers often rely on forums like StackOverflow for support. While productive, the advice found there is not always secure.

## Principles for Usable Security APIs
Green and Smith (2016) proposed principles for making security libraries more usable for developers:
1. **Secure by Default**: The easiest way to use the API should be the most secure.
2. **Hard to Misuse**: Design the API so that common mistakes are difficult to make.
3. **Clear Documentation**: Official documentation should be as easy to use as community forums but provide more secure guidance.
4. **Actionable Feedback**: Tools (like static analysis) should provide clear, actionable feedback rather than just "usability smells."

## Recommendations
- **Experiential Learning**: Developers should directly experience the impact of their security choices (e.g., handling help desk calls or dealing with incident losses).
- **Strong Security Culture**: Foster an organizational mindset that prioritizes secure coding practices.
- **Tooling**: Improve the usability of static and dynamic analysis tools to help developers find and fix vulnerabilities early.

## References
- [[ka-human-factors]]
- [[usable-security]]
- [[positive-security]]
