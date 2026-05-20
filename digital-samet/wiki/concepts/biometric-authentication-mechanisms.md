# Biometric Authentication Mechanisms

- **Source:** [[ka-aaa]]
- **Tags:** #aaa #authentication #biometrics #liveness

## Overview
Biometric authentication (or verification) builds on "who you are" by capturing unique biological features of a person.

## The Process
1. **Enrollment:** User registers a reference feature vector (template).
2. **Capture:** A device captures a new template during authentication.
3. **Extraction:** Features (e.g., minutiae in fingerprints) are extracted from the template.
4. **Comparison:** Extracted features are matched against the reference. Access is granted if the match exceeds a **Threshold**.

## Error Types
- **False Rejection (Type I Error):** A genuine user is rejected.
- **False Acceptance (Type II Error):** An impostor is incorrectly accepted.
- **Failure to Capture:** Inability to extract enough features from a user during enrollment or capture.

## Security Challenges

### 1. Spoofing
Adversaries presenting fake objects (e.g., photos, silicone fingers) to deceive the sensor.

### 2. Liveness Detection
Critical defense against spoofing. Techniques to ensure the sample is from a living person (e.g., checking for pulse, pupil dilation, or heat).

### 3. Stability
Features can change over time due to aging, injury, or environment (e.g., wet hands affecting fingerprint sensors).

## Prominent Technologies
- **Fingerprint:** Based on ridge patterns.
- **Face Recognition:** Mapping facial geometry.
- **Iris Recognition:** Analyzing the complex patterns of the iris.
- **FIDO UAF:** Biometrics can be used locally on a device to unlock a cryptographic key, which then performs the actual authentication to the server.

## Related Concepts
- [[user-authentication-factors]]
- [[aaa-fundamental-concepts]]
