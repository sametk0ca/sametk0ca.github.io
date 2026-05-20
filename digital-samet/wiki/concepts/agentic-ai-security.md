# Agentic AI Security (2026)

- **Source:** [[ai-agent-security-2026]]
- **Tags:** #ai-security #agents #autonomous-systems #modern-security

## Overview
Autonomous AI agents that can independently execute actions (browsing, code execution, API calls) introduce a major security paradigm shift. Unlike standard LLMs, agents can be hijacked to perform malicious real-world actions.

## 2026 Vulnerabilities
- **Prompt Injection at Scale:** Malicious websites can hijack agents browsing their content (Indirect Injection) to perform actions like stealing session tokens or sending unauthorized emails.
- **WebSocket Exploits (ClawJacked):** A 2026 discovery where agents running locally are hijacked via malicious web content interacting with their management interfaces.
- **Shadow Agents:** Employees deploying unmanaged agents that handle sensitive corporate data without security review.

## Defensive Strategies
- **Sandboxed Execution:** Running agent actions in ephemeral, isolated environments.
- **Agentic SOC:** Using defensive agents to monitor, validate, and block malicious actions from other agents.
- **Human-in-the-Loop (HITL):** Mandatory approval for high-risk actions (file deletion, financial transfers).

## Related Concepts
- [[ai-llm-security]]
- [[prompt-injection]]
- [[excessive-agency]] (New concept pending)
