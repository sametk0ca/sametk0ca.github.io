# Mobile Permission Models

- **Source:** [[ka-web-mobile-security]]
- **Tags:** #mobile-security #access-control #permissions

## Overview
Modern mobile operating systems use a permission-based access control system where users must explicitly grant an app the right to access sensitive data or sensors.

## 1. Privilege Levels

### Normal Permissions
- **Description:** Access to resources that pose minimal risk to privacy or system integrity (e.g., Internet access).
- **Enforcement:** Granted automatically by the system at install time without user intervention.

### Dangerous Permissions
- **Description:** Access to highly sensitive resources (e.g., GPS location, Camera, Microphone, Contacts).
- **Enforcement:** Requires the app to present a **Permission Dialog** to the user.

## 2. Timing of Consent

### Install-time Permissions (Legacy)
- **Mechanism:** The user is shown a list of all required permissions before installing the app.
- **Problem:** All-or-nothing choice; users often ignore the list to get the app.

### Runtime Permissions (Modern)
- **Mechanism:** The app requests a permission only when it is actually needed during execution.
- **Benefit:** Provides context for the request and allows users to deny specific rights while still using the app.

## 3. Human Factors and Limitations
- **Over-privilege:** Developers often request more permissions than necessary, violating the **Principle of Least Privilege**.
- **Comprehension:** Users frequently fail to understand the implications of a permission request.
- **Habituation:** Users tend to click "Allow" reflexively due to the frequency of prompts.

## Related Concepts
- [[aaa-fundamental-concepts]]
- [[os-design-paradigms]]
- [[mobile-app-stores-security]]
