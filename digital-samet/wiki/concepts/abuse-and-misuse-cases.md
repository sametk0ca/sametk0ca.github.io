# Abuse and Misuse Cases

- **Source:** [[ka-secure-software-lifecycle]]
- **Tags:** #sdlc #requirements #abuse-cases #misuse-cases

## Overview
While standard "Use Cases" describe intended behavior by benevolent actors, Abuse and Misuse Cases focus on undesirable actions to help "think like an attacker" during requirements and design.

## 1. Abuse Cases
Describe the behavior of a system when under attack by a **malicious actor**.
- **Focus:** Intentional harm.
- **Process:**
    1. Identify malicious actors and their motivations.
    2. Define the bad actor's goals (abuse cases).
    3. Analyze how abuse cases threaten legitimate use cases.
    4. Design fortifications to mitigate the threat.

## 2. Misuse Cases
Focus on actions by **benevolent users** that result in a security breach due to error or deception.
- **Focus:** Unintentional harm (human error).
- **Example:** A user falling for a phishing attack or accidentally sharing sensitive data.
- **Benefit:** Helps in designing better UI/UX and fail-safe defaults to protect users from themselves.

## 3. Application in SDLC
- **Requirements:** Input for specifying security controls.
- **Testing:** Foundation for risk-based security testing and penetration testing.
- **Design:** Informing architectural risk analysis.

## Related Concepts
- [[threat-modeling-stride]]
- [[os-security-principles]]
- [[soim-fundamental-concepts]]
