# User Authentication Factors

- **Source:** [[ka-aaa]]
- **Tags:** #aaa #authentication #passwords #mfa

## Overview
User authentication is the process of providing assurance that a user identity linked to a subject (process) belongs to the person who triggered its creation.

## The Three Traditional Factors

### 1. Something You Know (Knowledge)
- **Examples:** Passwords, PINs, security questions.
- **NIST Modern Guidance (SP 800-63):**
    - Favors length over complexity.
    - Discourages periodic forced password changes without cause.
    - Discourages "hints" or knowledge-based questions (easily findable on social media).
    - Recommends "show password while typing" to reduce entry errors.

### 2. Something You Have (Possession)
- **Examples:** Security tokens (YubiKey), smartphone apps (authenticator apps), smartcards.
- **Mechanism:** One-Time Passwords (OTP) or challenge-response cryptographic protocols.

### 3. Something You Are (Inherence)
- **Examples:** Fingerprints, face, iris patterns.
- **Key challenge:** Unlike passwords, biometric features are not secrets (they are left everywhere).

## Modern Extensions

### Something You Do (Behavioral)
- **Examples:** Keystroke dynamics, voice patterns, touch screen gestures.
- **Benefit:** Enables **Continuous Authentication**—checking if the user is still the same person throughout the session without friction.

## Multi-Factor Authentication (MFA/2FA)
Combining at least two different factors to increase security. 
- **Requirement:** Factors must be independent. (Note: Using a password and a TAN app on the *same* smartphone reduces independence).
- **Regulation:** Directives like **PSD2** in the EU mandate SCA (Strong Customer Authentication) for online payments.

## Related Concepts
- [[biometric-authentication-mechanisms]]
- [[federated-identity-protocols]]
- [[aaa-fundamental-concepts]]
