# Injection Vulnerabilities (Structured Output Generation)

- **Source:** [[ka-software-security]]
- **Tags:** #software-security #injection #sqli #xss

## Overview
Injection vulnerabilities occur when a program constructs structured output (code or data for another component) by improperly concatenating strings derived from untrusted input.

## Key Types

### 1. SQL Injection (SQLi)
Injecting malicious SQL commands into a query.
- **Cause:** `query = "SELECT * FROM users WHERE name='" + input_name + "'"`.
- **Impact:** Data exfiltration, bypassing authentication, or database corruption.

### 2. Cross-Site Scripting (XSS)
Injecting malicious JavaScript into HTML pages viewed by other users.
- **Stored XSS:** Malicious script is saved on the server (e.g., in a comment).
- **Reflected XSS:** Malicious script is part of a URL and reflected back by the server.

### 3. Command Injection
Injecting shell commands into system calls.
- **Impact:** Full system compromise under the privileges of the application.

## Prevention Strategies

### 1. Separation of Code and Data
- **Prepared Statements / Parameterized Queries:** The query structure is predefined, and user input is treated strictly as data.
- **LINQ (Language Integrated Query):** Using language features instead of raw strings to build queries.

### 2. Output Encoding and Sanitization
- **Context-aware Encoding:** Converting dangerous characters (e.g., `<` to `&lt;`) based on where the data is placed (HTML, JS, CSS).
- **Sanitization:** Removing or neutralizing dangerous parts of the input.

### 3. Strong Typing
Using regular expression types or specialized data structures to represent structured data (like XML or JSON) instead of plain strings.

## Related Concepts
- [[web-origin-security-policies]] (CSP)
- [[static-and-dynamic-analysis-formal]] (Taint analysis)
- [[software-security-foundations]]
