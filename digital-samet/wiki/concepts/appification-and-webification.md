# Appification and Webification

- **Source:** [[ka-web-mobile-security]]
- **Tags:** #web-security #mobile-security #ecosystem

## Overview
Appification and Webification describe two complementary trends that have fundamentally changed how users interact with digital services and how those services are built.

## 1. Appification
The shift from using general-purpose web browsers to using specialized, single-purpose mobile applications (apps).
- **Core Mantra:** "There is an app for everything."
- **Impact:** Leads to a massive increase in the number of clients interacting with web services, often with highly diverse security implementations.
- **The Citizen Developer:** Appification lowers the entry barrier for software development, attracting non-professional developers who may lack security training, potentially leading to more vulnerable software.

## 2. Webification
The process of building these specialized apps using web technologies (JavaScript, HTML, CSS) instead of native compiled languages (Java, Kotlin, Swift).
- **Motivation:** Cross-platform compatibility and ease of development.
- **Security Consequence:** Web vulnerabilities (like XSS or injection) are now common in what appear to be native mobile applications.
- **Tech Stack:** Heavily reliant on **JavaScript**, **WebAssembly**, and **WebViews**.

## 3. Comparison of Ecosystems
- **Pre-Mobile:** Focus on server-side security (Perl, PHP) and static browser rendering.
- **Modern:** Rich client-side logic, heavy use of APIs, and centralized distribution via **Application Stores**.

## Related Concepts
- [[webview-security]]
- [[mobile-app-stores-security]]
- [[software-security-foundations]]
