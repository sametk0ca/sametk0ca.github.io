# AI Adversarial Techniques (MITRE ATLAS)

- **Source:** [[mitre-attack-2026]], [[owasp-llm-top10-2024]]
- **Tags:** #ai-security #atlas #adversarial-ml #agentic-ai

## Overview
As AI systems transition from chatbots to **Autonomous Agents**, the attack surface has shifted toward manipulating the model's logic, memory, and tool-calling capabilities.

## 2026 Core Techniques
### 1. AI Agent Context Poisoning
Targeting the active context window. An attacker provides data (via a hijacked web page or email) that contains instructions intended to override the agent's system prompt while it is processing that data.

### 2. Persistent Memory Manipulation
Adversaries target the **Long-Term Memory** (often Vector Databases in RAG systems). By injecting malicious "facts" into the database, they can permanently alter the model's behavior for all future sessions.

### 3. Tool Credential Harvesting
Autonomous agents often have access to APIs and internal databases. Attackers use prompt injection to trick the agent into exfiltrating its own service tokens or credentials.

## Defense: The "Guardrail" Layer
Modern defense involves specialized AI-Firewalls that sit between the agent's reasoning engine and its tool-calling interface, performing real-time validation of all outbound actions.

## Related Concepts
- [[agentic-ai-security]]
- [[prompt-injection]]
- [[ai-llm-security]]
