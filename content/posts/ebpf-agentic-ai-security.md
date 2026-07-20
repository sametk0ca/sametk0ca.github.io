---
title: "eBPF for Agentic AI Security | eBPF ile Otonom AI Ajan Güvenliği"
date: 2026-07-20
description: "Monitoring and sandboxing autonomous AI agents at the Linux kernel layer using eBPF. / Linux çekirdek katmanında eBPF kullanarak otonom yapay zeka ajanlarını izleme ve dizginleme."
tags: ["eBPF", "Agentic AI", "Linux Kernel", "LLM Security", "Sandboxing"]
categories: ["Blog"]
ShowToc: true
math: false
mermaid: false
cover:
    image: "/img/xiaohei-ebpf-agentic-ai-security-1.jpg"
    alt: "eBPF Agentic AI Security Illustration"
    relative: false
---

## 🇹🇷 Türkçe (TR)

### Giriş: Otonom AI Ajanlarının Çekirdek Seviyesinde Dizginlenmesi

Otonom yapay zeka ajanları (Agentic AI), sistemlerimizde terminal komutları çalıştıran, kod derleyen, API çağrıları yapan ve dosya sistemini manipüle eden bağımsız aktörler haline gelmiştir. Antigravity, Claude Code ve AutoGPT gibi otonom araçlar geliştirme süreçlerini hızlandırırken, bu ajanların kontrol dışı eylemleri (hallucination) veya Prompt Injection saldırıları sonucu yetkisiz komutlar çalıştırması ciddi güvenlik riskleri yaratmaktadır.

Geleneksel kullanıcı alanı (user-space) güvenlik duvarları ve uygulama kısıtlamaları, dinamik olarak kod üreten AI ajanlarını engellemekte yetersiz kalmaktadır. Bu noktada modern Linux çekirdeğinin en güçlü teknolojilerinden biri olan **eBPF (Extended Berkeley Packet Filter)** devreye girmektedir. eBPF, çekirdek kodunu yeniden derlemeden Linux çekirdeği (kernel) seviyesinde yüksek performanslı, güvenli ve gerçek zamanlı izleme ile dizginleme imkanı sunar.

![İllüstrasyon / Illustration](/img/xiaohei-ebpf-agentic-ai-security-1.jpg)

---

### AI Ajan Tehdit Modeli ve eBPF Mimarisi

Otonom bir AI ajanı sisteme eriştiğinde aşağıdaki potansiyel zararlı eylemleri gerçekleştirebilir:

1. **İzinsiz Dosya Erişimi & Exfiltration:** Hassas yapılandırma dosyalarını (`.env`, `id_rsa`, AWS tokenları) okuyup dış API sunucularına aktarmak.
2. **Kötü Niyetli Proses Başlatma:** Sistemde yetkisiz ters kabuk (Reverse Shell) veya arka plan süreçleri çalıştırmak.
3. **Ağ Soket Manipülasyonu:** Beklenmeyen IP adreslerine veya portlara çıkış trafiği başlatmak.

eBPF mimarisi, Linux çekirdeğindeki sistem çağrılarını (`sys_enter_execve`, `sys_enter_connect`, `sys_enter_openat`) kancalayarak (hook) AI ajanının başlattığı her süreci sıfır gecikme (zero-overhead) ile denetler.

---

### eBPF ile Gerçek Zamanlı Ajan Dizginleme Mekanizması

#### 1. Dynamic System Call Filtering (Dinamik Sistem Çağrısı Filtreleme)
eBPF bytecode programları, AI ajan sürecinin cgroup veya PID bilgilerini takip ederek ajanın sadece izin verilen dizinlerde (`/tmp/scratch`, `workspace/`) dosya yazmasına izin verir. `/etc/passwd` veya `~/.ssh/` dizinlerine erişim denemeleri çekirdek seviyesinde `EPERM` (Operation Not Permitted) hatası ile anında engellenir.

#### 2. Network Egress Enforcement (Ağ Çıkış Kısıtlaması)
AI ajanlarının araç kullanırken (tool calling) yapacağı HTTP/DNS istekleri eBPF `tc` (Traffic Control) ve socket filter programları ile denetlenir. Ajan sadece beyaz listede (allowlist) yer alan API endpoint'leri ile haberleşebilir.

#### 3. Real-Time Telemetry & Behavioral Audit (Gerçek Zamanlı Telemetri)
eBPF ring buffer yapısı sayesinde, AI ajanının gerçekleştirdiği tüm `execve` komut zinciri ve süreç ağacı (process tree) sıfır performans kaybıyla SIEM ve güvenlik panellerine aktarılır.

---
---

## 🇬🇧 English (EN)

### Introduction: Sandboxing Autonomous AI Agents at the Kernel Layer

Autonomous AI agents (Agentic AI) have evolved from passive conversational models into active system operators capable of executing shell commands, compiling code, invoking web APIs, and modifying local filesystems. While autonomous coding assistants (such as Antigravity, Claude Code, and AutoGPT) drastically boost developer productivity, they also introduce critical security concerns. Hallucinations, untrusted prompt injections, or compromised tool-use workflows can lead to unauthorized system commands and data exfiltration.

Traditional user-space security controls and static permission prompts fail to adapt to the non-deterministic, dynamically generated execution paths of LLM agents. To address this gap, modern security engineering turns to **eBPF (Extended Berkeley Packet Filter)**—a revolutionary Linux kernel technology that enables sandboxing, real-time observability, and fine-grained access control directly within the kernel without altering kernel source code.

---

### Threat Model of Agentic Execution & eBPF Security Architecture

When an autonomous AI agent is granted local terminal execution privileges, it introduces several distinct threat vectors:

1. **Unauthorized Sensitive File Access:** Unintentional reading and exfiltration of environment files (`.env`), private keys (`id_rsa`), or credential stores.
2. **Malicious Process Spawning:** Execution of unauthorized binaries, background daemons, or reverse shell sockets triggered by indirect prompt injection.
3. **Unsanctified Network Egress:** Initiating socket connections to unapproved remote command-and-control (C2) or third-party endpoints.

eBPF programs attach directly to kernel tracepoints and kprobes (e.g., `sys_enter_execve`, `sys_enter_openat`, `sys_enter_connect`). By intercepting events at the kernel boundary, eBPF evaluates execution context with near-zero runtime latency.

---

### Technical Implementation of eBPF Agent Governance

#### 1. Dynamic Kernel-Level Process Isolation
By attaching eBPF programs to process cgroups or tracking specific agent PID trees, security engineers can enforce strict path-scoping rules. Attempts by the AI agent to open or modify protected system paths (such as `/etc/shadow`, `~/.aws/credentials`) are blocked instantly at the VFS layer by returning an `EPERM` error code.

#### 2. Programmable Network Egress Control
eBPF socket filters and Traffic Control (TC) hooks inspect all outbound TCP/UDP traffic originated by agent processes. Outbound connections are matched against an in-memory eBPF map of approved API domains, instantly dropping unauthorized egress packets.

#### 3. High-Throughput Audit Telemetry
Leveraging eBPF ring buffers, every system call, process tree fork, and file modification initiated by the AI agent is streamed continuously to security observability tools, providing complete forensic transparency over autonomous agent behaviors.

---

*This post is linked to the Knowledge Base: [[Knowledge Base / eBPF Agentic AI Security]]*
