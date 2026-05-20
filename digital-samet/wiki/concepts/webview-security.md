# WebView Security

- **Source:** [[ka-web-mobile-security]]
- **Tags:** #mobile-security #web-security #webview #attacks

## Overview
WebViews are components that allow mobile applications to render and interact with web content (HTML/JS) directly within the native app interface. They are a primary mechanism for **Webification**.

## Shared Responsibility
WebViews bridge the gap between the native app process and the web environment, creating unique security challenges.

## Attack Vectors

### 1. App-to-Web Attacks
A malicious or compromised native app manipulates the hosted web content.
- **Mechanism:** Injecting JavaScript into the WebView.
- **Goal:** Stealing sensitive data from the web session (e.g., session cookies for a bank site rendered in a WebView).

### 2. Web-to-App Attacks
Untrusted web content exploits the bridge to gain access to the host app's resources.
- **Mechanism:** Exploiting **JavaScript Bridges** (interfaces that allow JS code to call native Java/Swift methods).
- **Goal:** Privilege escalation to the level of the host app, potentially accessing sensors (GPS, Camera) or the file system.

## Best Practices
- **Restrict JavaScript:** Disable JS in WebViews unless absolutely necessary.
- **Whitelist Origins:** Only allow the WebView to load content from trusted domains.
- **Secure Bridges:** Carefully validate all inputs passed from JS to native code.
- **Use Modern APIs:** Prefer `WKWebView` (iOS) or contemporary Android implementations that offer better isolation.

## Related Concepts
- [[appification-and-webification]]
- [[mobile-app-stores-security]]
- [[web-content-isolation-sop-csp]]
