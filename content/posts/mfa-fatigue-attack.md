---
title: "MFA Fatigue"
date: 2026-03-31
draft: false
tags:
  - MFA
  - Social Engineering
  - Cybersecurity
  - Identity
categories:
  - Security Awareness
---

MFA Fatigue (also known as MFA Bombing or Push Spam) is a social engineering attack where an attacker who has already stolen a user's credentials repeatedly triggers multi-factor authentication requests. The goal is to overwhelm or "fatigue" the user until they finally click "Approve" just to stop the notifications.

### How it works:
1. Attacker steals the password (via phishing or breach).
2. Attacker logs in, triggering a Push notification.
3. Attacker repeats this dozens or hundreds of times, often at night.
4. User, annoyed or confused, eventually approves.

### Prevention:
- Use number matching (where the user must type a code shown on the screen).
- Educate users never to approve unexpected prompts.
- Implement adaptive authentication (blocking multiple failed attempts).
