---
title: "CyberWiki"
date: 2026-05-19
draft: false
description: "Technical reference and knowledge base."
---

<style>
  .wiki-grid {
    display: grid;
    grid-template-columns: repeat(auto-fill, minmax(260px, 1fr));
    gap: 1.25rem;
    margin: 2rem 0;
  }
  .wiki-card {
    display: flex;
    flex-direction: column;
    background: var(--entry);
    border: 1px solid var(--border);
    border-radius: 16px;
    padding: 1.5rem;
    text-decoration: none;
    color: var(--primary) !important;
    transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);
    box-shadow: 0 4px 10px rgba(0, 0, 0, 0.1);
    position: relative;
    overflow: hidden;
  }
  .wiki-card::after {
    content: '';
    position: absolute;
    bottom: 0;
    left: 0;
    width: 100%;
    height: 4px;
    background: var(--card-accent, var(--primary));
    opacity: 0.8;
  }
  .wiki-card:hover {
    transform: translateY(-5px);
    border-color: var(--card-accent, var(--primary));
    box-shadow: 0 12px 25px rgba(0, 0, 0, 0.15);
  }
  .wiki-card-icon {
    font-size: 2rem;
    margin-bottom: 0.75rem;
  }
  .wiki-card-title {
    font-size: 1.15rem;
    font-weight: 700;
    margin-bottom: 0.25rem;
  }
  .wiki-card-desc {
    font-size: 0.85rem;
    color: var(--secondary);
    font-weight: 500;
  }
</style>

## Türkçe (TR)

Bu sayfa, teknik güvenlik konularını ve siber savunma metodolojilerini içeren kapsamlı bir bilgi tabanıdır.

### Kategoriler

<div class="wiki-grid">
  <a href="/categories/attacks/" class="wiki-card" style="--card-accent: #ef4444;">
    <div class="wiki-card-icon">⚔️</div>
    <div class="wiki-card-title">Saldırı Teknikleri</div>
    <div class="wiki-card-desc">Attacks</div>
  </a>
  <a href="/categories/networking/" class="wiki-card" style="--card-accent: #3b82f6;">
    <div class="wiki-card-icon">🌐</div>
    <div class="wiki-card-title">Ağ Güvenliği</div>
    <div class="wiki-card-desc">Networking</div>
  </a>
  <a href="/categories/os/" class="wiki-card" style="--card-accent: #10b981;">
    <div class="wiki-card-icon">🖥️</div>
    <div class="wiki-card-title">İşletim Sistemleri</div>
    <div class="wiki-card-desc">OS</div>
  </a>
  <a href="/categories/devsecops/" class="wiki-card" style="--card-accent: #8b5cf6;">
    <div class="wiki-card-icon">🏗️</div>
    <div class="wiki-card-title">DevSecOps</div>
    <div class="wiki-card-desc">Software & Cloud Security</div>
  </a>
  <a href="/categories/defense/" class="wiki-card" style="--card-accent: #06b6d4;">
    <div class="wiki-card-icon">🛡️</div>
    <div class="wiki-card-title">Savunma ve İzleme</div>
    <div class="wiki-card-desc">Defense</div>
  </a>
  <a href="/categories/cryptography/" class="wiki-card" style="--card-accent: #eab308;">
    <div class="wiki-card-icon">🔐</div>
    <div class="wiki-card-title">Kriptografi</div>
    <div class="wiki-card-desc">Cryptography</div>
  </a>
  <a href="/categories/hardware/" class="wiki-card" style="--card-accent: #f97316;">
    <div class="wiki-card-icon">🔌</div>
    <div class="wiki-card-title">Donanım</div>
    <div class="wiki-card-desc">Hardware</div>
  </a>
  <a href="/categories/programming/" class="wiki-card" style="--card-accent: #ec4899;">
    <div class="wiki-card-icon">💻</div>
    <div class="wiki-card-title">Programlama</div>
    <div class="wiki-card-desc">Programming</div>
  </a>
  <a href="/categories/principles/" class="wiki-card" style="--card-accent: #6366f1;">
    <div class="wiki-card-icon">📜</div>
    <div class="wiki-card-title">Güvenlik İlkeleri</div>
    <div class="wiki-card-desc">Principles</div>
  </a>
  <a href="/categories/virtualization/" class="wiki-card" style="--card-accent: #0ea5e9;">
    <div class="wiki-card-icon">☁️</div>
    <div class="wiki-card-title">Sanallaştırma</div>
    <div class="wiki-card-desc">Virtualization</div>
  </a>
  <a href="/categories/tools/" class="wiki-card" style="--card-accent: #a855f7;">
    <div class="wiki-card-icon">🛠️</div>
    <div class="wiki-card-title">Güvenlik Araçları</div>
    <div class="wiki-card-desc">Tools</div>
  </a>
  <a href="/categories/incidentresponse/" class="wiki-card" style="--card-accent: #dc2626;">
    <div class="wiki-card-icon">🚨</div>
    <div class="wiki-card-title">Olay Müdahale</div>
    <div class="wiki-card-desc">Incident Response</div>
  </a>
  <a href="/categories/legal_compliance/" class="wiki-card" style="--card-accent: #64748b;">
    <div class="wiki-card-icon">⚖️</div>
    <div class="wiki-card-title">Hukuk ve Uyum</div>
    <div class="wiki-card-desc">Legal & Compliance</div>
  </a>
  <a href="/categories/certifications/" class="wiki-card" style="--card-accent: #10b981;">
    <div class="wiki-card-icon">🎓</div>
    <div class="wiki-card-title">Sertifikalar</div>
    <div class="wiki-card-desc">Certifications</div>
  </a>
  <a href="/categories/cloud/" class="wiki-card" style="--card-accent: #0284c7;">
    <div class="wiki-card-icon">☁️</div>
    <div class="wiki-card-title">Bulut Güvenliği</div>
    <div class="wiki-card-desc">Cloud</div>
  </a>
  <a href="/categories/frameworks/" class="wiki-card" style="--card-accent: #14b8a6;">
    <div class="wiki-card-icon">📋</div>
    <div class="wiki-card-title">Frameworkler</div>
    <div class="wiki-card-desc">Frameworks</div>
  </a>
  <a href="/categories/ctfs/" class="wiki-card" style="--card-accent: #f43f5e;">
    <div class="wiki-card-icon">🏁</div>
    <div class="wiki-card-title">CTF Yarışmaları</div>
    <div class="wiki-card-desc">CTFs</div>
  </a>
</div>

---

*Not: Tüm içerikler teorik ve pratik bilgi amaçlıdır. Etik sınırlar dışındaki kullanımlar sorumluluğumuzda değildir.*

---

## English (EN)

This page is a comprehensive knowledge base of technical security topics.

### Categories

<div class="wiki-grid">
  <a href="/categories/attacks/" class="wiki-card" style="--card-accent: #ef4444;">
    <div class="wiki-card-icon">⚔️</div>
    <div class="wiki-card-title">Attack Techniques</div>
    <div class="wiki-card-desc">Attacks</div>
  </a>
  <a href="/categories/networking/" class="wiki-card" style="--card-accent: #3b82f6;">
    <div class="wiki-card-icon">🌐</div>
    <div class="wiki-card-title">Network Security</div>
    <div class="wiki-card-desc">Networking</div>
  </a>
  <a href="/categories/os/" class="wiki-card" style="--card-accent: #10b981;">
    <div class="wiki-card-icon">🖥️</div>
    <div class="wiki-card-title">Operating Systems</div>
    <div class="wiki-card-desc">OS</div>
  </a>
  <a href="/categories/devsecops/" class="wiki-card" style="--card-accent: #8b5cf6;">
    <div class="wiki-card-icon">🏗️</div>
    <div class="wiki-card-title">DevSecOps</div>
    <div class="wiki-card-desc">Software & Cloud Security</div>
  </a>
  <a href="/categories/defense/" class="wiki-card" style="--card-accent: #06b6d4;">
    <div class="wiki-card-icon">🛡️</div>
    <div class="wiki-card-title">Defense & Monitoring</div>
    <div class="wiki-card-desc">Defense</div>
  </a>
  <a href="/categories/cryptography/" class="wiki-card" style="--card-accent: #eab308;">
    <div class="wiki-card-icon">🔐</div>
    <div class="wiki-card-title">Cryptography</div>
    <div class="wiki-card-desc">Cryptography</div>
  </a>
  <a href="/categories/hardware/" class="wiki-card" style="--card-accent: #f97316;">
    <div class="wiki-card-icon">🔌</div>
    <div class="wiki-card-title">Hardware Security</div>
    <div class="wiki-card-desc">Hardware</div>
  </a>
  <a href="/categories/programming/" class="wiki-card" style="--card-accent: #ec4899;">
    <div class="wiki-card-icon">💻</div>
    <div class="wiki-card-title">Programming</div>
    <div class="wiki-card-desc">Programming</div>
  </a>
  <a href="/categories/principles/" class="wiki-card" style="--card-accent: #6366f1;">
    <div class="wiki-card-icon">📜</div>
    <div class="wiki-card-title">Security Principles</div>
    <div class="wiki-card-desc">Principles</div>
  </a>
  <a href="/categories/virtualization/" class="wiki-card" style="--card-accent: #0ea5e9;">
    <div class="wiki-card-icon">☁️</div>
    <div class="wiki-card-title">Virtualization</div>
    <div class="wiki-card-desc">Virtualization</div>
  </a>
  <a href="/categories/tools/" class="wiki-card" style="--card-accent: #a855f7;">
    <div class="wiki-card-icon">🛠️</div>
    <div class="wiki-card-title">Security Tools</div>
    <div class="wiki-card-desc">Tools</div>
  </a>
  <a href="/categories/incidentresponse/" class="wiki-card" style="--card-accent: #dc2626;">
    <div class="wiki-card-icon">🚨</div>
    <div class="wiki-card-title">Incident Response</div>
    <div class="wiki-card-desc">Incident Response</div>
  </a>
  <a href="/categories/legal_compliance/" class="wiki-card" style="--card-accent: #64748b;">
    <div class="wiki-card-icon">⚖️</div>
    <div class="wiki-card-title">Legal & Compliance</div>
    <div class="wiki-card-desc">Legal & Compliance</div>
  </a>
  <a href="/categories/certifications/" class="wiki-card" style="--card-accent: #10b981;">
    <div class="wiki-card-icon">🎓</div>
    <div class="wiki-card-title">Certifications</div>
    <div class="wiki-card-desc">Certifications</div>
  </a>
  <a href="/categories/cloud/" class="wiki-card" style="--card-accent: #0284c7;">
    <div class="wiki-card-icon">☁️</div>
    <div class="wiki-card-title">Cloud Security</div>
    <div class="wiki-card-desc">Cloud</div>
  </a>
  <a href="/categories/frameworks/" class="wiki-card" style="--card-accent: #14b8a6;">
    <div class="wiki-card-icon">📋</div>
    <div class="wiki-card-title">Security Frameworks</div>
    <div class="wiki-card-desc">Frameworks</div>
  </a>
  <a href="/categories/ctfs/" class="wiki-card" style="--card-accent: #f43f5e;">
    <div class="wiki-card-icon">🏁</div>
    <div class="wiki-card-title">CTF Competitions</div>
    <div class="wiki-card-desc">CTFs</div>
  </a>
</div>

---

*Note: All content is for theoretical and practical information purposes. We are not responsible for uses outside ethical limits.*
