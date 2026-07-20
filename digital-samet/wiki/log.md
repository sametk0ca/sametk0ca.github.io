# Wiki Log

## [2026-07-20] publish | Neuromorphic BCI, eBPF Agentic AI & Post-Quantum TLS (bci-neuromorphic-security.md, ebpf-agentic-ai-security.md, post-quantum-kyber-tls-overhead.md)
- Synthesized and published 3 bilingual blog posts:
  1. **Neuromorphic & BCI Security**: Analyzed brain-computer interface threat vectors, P300 brain eavesdropping side-channels, neural signal injection, and differential privacy / hardware enclave mitigations. Included Xiaohei hand-drawn illustration.
  2. **eBPF for Agentic AI Security**: Explored kernel-level sandboxing, dynamic system call filtering (`openat`, `execve`), and network egress control for autonomous LLM agents. Included Xiaohei hand-drawn illustration.
  3. **Post-Quantum Handshake Overhead**: Detailed real-world TLS 1.3 packet fragmentation, MTU boundaries, middlebox drops, and TTFB latency overhead when deploying Kyber768 hybrid key exchanges. Included Xiaohei hand-drawn illustration.

## [2026-07-13] publish | Bypassing Path Traversal Filters (To-Do/drafts/path-traversal-filter-bypass.md)
- Synthesized and published a bilingual blog post explaining Directory Traversal and Filter Bypass vulnerabilities.
- **Path Traversal & Filter Bypass**: Explored how simple string replacement (`replace("../", "")`) fails to protect web applications. Explained the mechanics of nested string bypasses (`....//`) and secure coding remedies using canonical path resolution (`os.path.abspath`) and whitelisting.
- Included a custom "Xiaohei" (小黑) hand-drawn illustration depicting the filter bypass mechanism.

## [2026-07-10] publish | Zero-Knowledge Proofs (wiki/concepts/zero-knowledge-proofs.md)
- Synthesized and published a bilingual blog post explaining Zero-Knowledge Proofs (ZKP).
- **Zero-Knowledge Proofs**: Intuitive explanation using the Ali Baba Cave metaphor. Detailed the three core cryptographic properties: Completeness, Soundness, and Zero-Knowledge. Covered Sigma protocols, ZK-SNARKs, and the Fiat-Shamir Transform.
- Included a custom "Xiaohei" (小黑) hand-drawn illustration depicting the Ali Baba Cave concept metaphor.

## [2026-07-06] publish | Game Cheats & Anti-Cheats (wiki/concepts/game-security-and-cheats.md)
- Synthesized and published a bilingual blog post on game cheating mechanisms and anti-cheat defenses.
- **Game Cheats & Anti-Cheats**: Detailed how memory reading/writing, World-to-Screen projection (ESP), and ViewAngle manipulation (Aimbot) operate. Explained DLL injection, function hooking, and defensive layers including Ring 0 kernel-level drivers, behavioral heuristics, and server-side validation.
- Included an architecture flow diagram in Mermaid showing the relation between the Client Game Process, Cheat Process/Driver, Anti-Cheat Driver, and the Game Server.

## [2026-07-02] publish | BGP Security & Software Supply Chain Security (wiki/concepts/bgp-security-and-prefix-hijacking.md, wiki/concepts/software-supply-chain-security.md)
- Synthesized and published two separate bilingual blog posts covering routing security and package management safety.
- **BGP Security & Prefix Hijacking**: Explained Border Gateway Protocol structural trust issues, Prefix Hijacking, Route Leaks, and mitigations like RPKI (ROA/ROV), BGPsec, and ASPA. Included routing flow diagrams in Mermaid.
- **Software Supply Chain Security**: Described modern supply chain attacks (dependency confusion, typosquatting), the SLSA framework (provenance and levels 1-3), and SBOM benefits. Included build pipeline flowcharts in Mermaid.

## [2026-06-23] publish | WhatsApp & Instagram Security (wiki/concepts/authentication-identity-protocols.md, wiki/concepts/phishing-and-clickjacking-details.md)
- Synthesized and published two separate bilingual blog posts answering everyday security questions.
- **WhatsApp Security**: Discussed the Signal Protocol, Double Ratchet mechanism, cloud backup risks, and endpoint compromises. Included E2EE workflow diagrams in Mermaid.
- **Instagram Hacking**: Contrasted server-side security (Argon2/bcrypt, rate limits) with client-side/human errors (phishing, credential stuffing, stealer malware). Included attacker vector comparison flowcharts in Mermaid.

## [2026-06-23] publish | Constant-Time Cryptography (wiki/concepts/constant-time-cryptography.md)
- Synthesized and published bilingual blog post on Constant-Time Cryptography, explaining how execution timing variations can leak keys.
- Included a sequence flow diagram in Mermaid to illustrate standard vs. constant-time comparisons.

## [2026-06-21] publish | Race Condition (wiki/concepts/race-condition-vulnerability.md)
- Synthesized and published bilingual blog post on Race Condition vulnerabilities, explaining the TOCTOU (Time of Check to Time of Use) window.
- Included explanations for financial logic flaws, privilege escalation, and symlink attacks.
- Added a sequence flow diagram in Mermaid to illustrate simultaneous balance deduction exploits.
- Provided mitigation strategies such as database locking (SELECT FOR UPDATE), mutex locks, atomic operations, and rate limiting.

## [2026-06-20] publish | IP Camera Vulnerabilities (wiki/concepts/ip-camera-vulnerabilities.md)
- Synthesized and published bilingual blog post on IP camera and CCTV vulnerabilities, highlighting weak credentials, unencrypted RTSP/HTTP streams, firmware RCE, UPnP port exposure, and optical/physical tampering.
- Added architectural attack vector diagrams in Mermaid for Turkish and English sections.

## [2026-06-20] publish | Kill Switch (wiki/concepts/killswitch.md)
- Synthesized and published bilingual blog post explaining the kill switch concept across different layers (VPN, WannaCry malware, hardware, cloud/software engineering).
- Added VPN kill switch and WannaCry check-flow diagrams in Mermaid.

## [2026-06-14] publish | Synthetic Identity & Deepfakes (wiki/concepts/synthetic-identity-deepfakes.md)
- Synthesized and published bilingual blog post on deepfake-as-a-service, voice cloning scams, and defenses.
- Added voice-cloning phishing flowchart in Mermaid.

## [2026-06-14] publish | Biometric Authentication Mechanisms (wiki/concepts/biometric-authentication-mechanisms.md)
- Synthesized and published bilingual blog post on fingerprint/face scanners, Type I/II errors, and liveness detection.
- Added enrollment and verification pipeline diagram in Mermaid.

## [2026-06-14] publish | Human Error in Security (wiki/concepts/human-error.md)
- Synthesized and published bilingual blog post on Swiss Cheese model, System 1 & 2 thinking, and human-centric security.
- Added Swiss Cheese model visualization in Mermaid.

## [2026-06-14] publish | Distance Bounding and Relay Attacks (wiki/concepts/distance-bounding-and-relay-attacks.md)
- Synthesized and published bilingual blog post on relay attacks and physical-layer distance bounding.
- Added sequence diagram in Mermaid.

## [2026-06-14] publish | Hardware Root of Trust (wiki/concepts/hardware-root-of-trust.md)
- Synthesized and published bilingual blog post on TPM, HSM, and Chain of Trust hierarchy.
- Added architectural diagram in Mermaid.

## [2026-06-14] publish | Byzantine Fault Tolerance (wiki/concepts/byzantine-fault-tolerance.md)
- Synthesized and published bilingual blog post on the Byzantine Generals Problem and BFT consensus requirements.
- Added node consensus diagram in Mermaid.

## [2026-06-14] publish | TEMPEST: Understanding Compromising Emanations (wiki/concepts/compromising-emanations-tempest.md)
- Synthesized and published bilingual blog post on TEMPEST and compromising physical signals.
- Added system architecture diagram in Mermaid.

## [2026-06-14] publish | GNSS Spoofing and Takeover Attacks (wiki/concepts/gnss-spoofing-and-takeover-attacks.md)
- Synthesized and published bilingual blog post on civilian GPS physical layer vulnerabilities.
- Added coherent vs non-coherent spoofing diagram in Mermaid.

## [2026-05-19] ingest | DevSecOps Roadmap Expansion (48 Topics)
- Analyzed `raw/devsecops.txt` and restructured `wiki/roadmap/devsecops.md` with 48 detailed sub-topics.
- Created 48 new detailed topic files in Turkish across various categories:
    - **DevSecOps:** Foundations, ACLs, Segmentation, SQLi/XSS Prevention, STRIDE, PASTA, Supply Chain, SBOM, Pipeline Hardening, etc.
    - **Programming:** Ruby, Rust, Go, JavaScript/Node.js, Bash, PowerShell.
    - **Cloud:** CSPM, Cloud IAM, KMS.
    - **Compliance & Frameworks:** SOC2, ISO 27001, NIST CSF.
    - **Defense & IR:** SOAR, Alert Types, Containment, RCA.
- Updated `wiki/index.md` with a new "DevSecOps & Software Security" section for improved discoverability.
- Integrated all topics from the source roadmap into the wiki structure with detailed technical overviews and best practices.

## [2026-05-18] ingest | Comprehensive Cybersecurity Roadmap Expansion (301 Topics)
- Analyzed `raw/cyber-security.txt` and expanded the roadmap to include all 301 topics.
- Created logical groupings for related topics to maintain wiki quality and manageability.
- Added 9 new comprehensive category files in Turkish:
    - `wiki/topics/CTFs/CTF_Platformlari.md` (HTB, THM, VulnHub, etc.)
    - `wiki/topics/Certifications/Sertifikalar.md` (A+, Security+, OSCP, CISSP, etc.)
    - `wiki/topics/Cloud/Bulut_Guvenligi.md` (AWS, Azure, SaaS/PaaS/IaaS, etc.)
    - `wiki/topics/Programming/Programlama_Dilleri.md` (Python, Bash, Go, C++, etc.)
    - `wiki/topics/Frameworks/Guvenlik_Frameworkleri.md` (MITRE ATT&CK, NIST, ISO 27001, etc.)
    - `wiki/topics/IncidentResponse/Olay_Mudahale.md` (IR Phases, Threat Hunting, OSINT, etc.)
    - `wiki/topics/Tools/Siber_Guvenlik_Araclari.md` (Kali, Metasploit, Nmap, Wireshark, etc.)
    - `wiki/topics/Legal_Compliance/Uyumluluk_ve_Hukuk.md` (GDPR/KVKK, HR, Auditing, etc.)
- Restructured `wiki/roadmap/cybersecurity.md` to integrate all new topics and category links.
- Ensured all 301 topics from the source text are accounted for and explained in Turkish.

## [2026-05-12] publish | DNS Leaks (wiki/concepts/dns-leak.md)
... (rest of the file)
