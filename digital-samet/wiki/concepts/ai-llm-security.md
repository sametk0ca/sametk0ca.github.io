# AI & LLM Security

- **Source:** [[owasp-llm-top10-2024]]
- **Tags:** #ai-security #llm #owasp #modern-security

## Overview
AI & Large Language Model (LLM) security extends traditional software security by addressing unique vulnerabilities in model training, inference, and integration.

## OWASP Top 10 for LLM Applications (2024)
1. **LLM01: Prompt Injection:** Manipulating model behavior via crafted inputs. See: [[yz-prompt-injection]].
2. **LLM02: Insecure Output Handling:** Failing to validate model output before passing it to downstream APIs (e.g., SSRF or XSS).
3. **LLM03: Training Data Poisoning:** Tampering with the data used to train or fine-tune models to introduce hidden backdoors.
4. **LLM06: Sensitive Information Disclosure:** Model inadvertently revealing private data (PII, secrets) in its training set.
5. **LLM08: Excessive Agency:** Giving models too much autonomy to perform actions (e.g., deleting files, sending emails) without human-in-the-loop validation.

## Defensive Strategies
- **Human-in-the-Loop:** Requiring manual approval for high-risk actions.
- **Output Sanitization:** Treating LLM output as untrusted user input.
- **RAG Security:** Protecting the vector database and retrieval chain.

## Related Concepts
- [[prompt-injection]]
- [[software-security-foundations]]
- [[injection-vulnerabilities]]
