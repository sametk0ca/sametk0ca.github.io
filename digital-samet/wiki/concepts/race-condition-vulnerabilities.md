# Race Condition Vulnerabilities

- **Source:** [[ka-software-security]]
- **Tags:** #software-security #concurrency #race-conditions #toctou

## Overview
A race condition occurs when the behavior of a program depends on the relative timing or interleaving of concurrent actors (threads or processes) accessing a shared resource.

## Key Types

### 1. TOCTOU (Time Of Check Time Of Use)
The program checks a condition (e.g., file permissions) and then uses the resource based on that check. An attacker can intervene between the check and the use to invalidate the condition.
- **Scenario:** A privileged service checks if `/tmp/file` is a regular file owned by the user, then opens it. An attacker replaces it with a symbolic link to `/etc/shadow` between the check and the open.

### 2. Session Race Conditions
Occur in web applications where multiple concurrent requests for the same session access the session state simultaneously.
- **Impact:** Corruption of user data, unauthorized privilege escalation, or double-spending in financial applications.

## Prevention and Mitigation

### 1. Atomicity
Ensuring that the check and the use are performed as a single, uninterruptible operation.
- **System Calls:** Using atomic file system flags (e.g., `O_EXCL`, `O_NOFOLLOW`).
- **Locks:** Using mutexes or semaphores to provide exclusive access to shared memory.

### 2. Ownership Types
Language-level support (like in Rust) that ensures only one actor has "ownership" (and thus write access) to a resource at any given time, preventing data races by design.

### 3. Locking Discipline
Consistently following a strictly defined order for acquiring and releasing locks.

## Related Concepts
- [[os-design-paradigms]]
- [[software-security-foundations]]
- [[distributed-consensus-and-paxos]]
