+++
title = "VirtualBox Yapılandırması ve Ağ Modları"
date = "2026-05-19"
draft = false
tags = ["Bilgi Bankası", "Virtualization"]
categories = ["Eğitim"]
type = "bilgi-bankasi"
+++

VirtualBox, açık kaynak kodlu ve ücretsiz bir sanallaştırma yazılımıdır. Siber güvenlik lab ortamı kurarken en önemli konu **Ağ Yapılandırmasıdır**.

### 1. Ağ Bağlantı Türleri (Kritik)
Sanal makinenin dış dünyayla nasıl iletişim kuracağını belirler:
- **NAT (Network Address Translation):** Sanal makine internete çıkabilir ama dışarıdan kimse ona erişemez. Varsayılan ayardır.
- **Bridged Adapter (Köprü Bağdaştırıcısı):** Sanal makine, fiziksel bilgisayarınızla aynı modeme bağlıymış gibi davranır. Kendi IP'sini modemden alır. Güvenlik riski taşır çünkü sanal makine evdeki diğer tüm cihazlarla doğrudan iletişim kurabilir.
- **Internal Network (Dahili Ağ):** Sadece sanal makineler kendi arasında konuşur. Ana bilgisayar (Host) bile bu ağı göremez. Malware analizi için en güvenli yoldur.
- **Host-Only Adapter:** Sanal makine sadece ana bilgisayarla konuşabilir. İnternet erişimi yoktur.

### 2. Guest Additions
VMware Tools'un VirtualBox karşılığıdır. 
- **Shared Clipboard (Paylaşılan Pano):** Eğer "Kopyala-Yapıştır" özelliği açıksa, sanal makinedeki bir zararlı, ana bilgisayarınızın panosuna (clipboard) veri yazabilir veya oradaki şifrelerinizi okuyabilir.

### 3. USB Passthrough
Ana bilgisayara takılan bir USB cihazını doğrudan sanal makineye atama özelliğidir.
- **Analiz:** Bir USB'yi analiz etmek istiyorsanız, onu ana bilgisayara hiç "değdirmeden" (mount etmeden) doğrudan sanal makineye atayarak ana bilgisayarınızı virüsten koruyabilirsiniz.