---
concept: Usable Security
source: [[ka-human-factors]]
tags: [concept, human-factors, usability, cybok]
---

# Concept: Usable Security

## Definition
The ISO (9241-11:2018) defines usability as the "effectiveness, efficiency and satisfaction with which specified users achieve specified goals in particular environments."

## The Three Pillars of Usability
1. **Effectiveness**: Accuracy and completeness in achieving goals.
2. **Efficiency**: Resources expended (time, effort) relative to the goal achieved.
3. **Satisfaction**: Comfort and acceptability of the system to its users.

## Fitting the Task to the Human
Rather than blaming users for being the "weakest link," usable security seeks to design tasks that fit:
- **Human Capabilities & Limitations**: Respecting limits on attention and memory.
- **User Goals & Tasks**: Recognizing that security is often a secondary task to "production" goals.
- **Context of Use**: Physical and social environment.
- **Device Limitations**: Mobile vs. desktop interfaces.

## Cognitive Constraints
- **Attention**: Humans can only focus on one primary task at a time. Status messages on screen edges are often ignored.
- **Alarm Fatigue**: People stop paying attention to alarms classified as irrelevant or unreliable (e.g., high false-positive rates in SSL warnings).
- **Memory**: 
    - **Short Term (STM)**: Limited to ~6 characters for easy recall (e.g., OTPs).
    - **Long Term (LTM)**: Items retrieved frequently are better embedded; semantic memory fades faster than episodic (autobiographical) memory.

## Recommendations
- Use **Two-Factor Authentication (2FA)** and **Password Managers** to reduce memory load.
- Avoid expiring strong passwords unless compromised.
- Design warnings to be **NEAT**: Necessary, Explained, Actionable, and Tested.

## References
- [[ka-human-factors]]
- [[cia-triad]]
