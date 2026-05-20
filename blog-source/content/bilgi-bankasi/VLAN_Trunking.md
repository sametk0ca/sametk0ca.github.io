+++
title = "VLAN (Virtual LAN) ve Trunking"
date = "2026-05-19"
draft = false
categories = ["Networking"]
type = "bilgi-bankasi"
+++

VLAN, fiziksel bir ağı mantıksal olarak birden fazla sanal ağa bölme teknolojisidir. Bir Switch üzerindeki portları gruplayarak, birbirlerinden izole edilmiş ağlar oluşturmamızı sağlar.

### 1. Neden VLAN Kullanılır?
- **Güvenlik (İzolasyon):** Muhasebe departmanındaki bir bilgisayarın, yazılım ekibinin ağındaki sunuculara doğrudan erişmesini engeller.
- **Performans:** Broadcast trafiğini sınırlar (Broadcast Domain'i böler).
- **Esneklik:** Bir kullanıcı masasını değiştirse bile, port ayarı yapılarak aynı VLAN'da kalması sağlanabilir.

### 2. Trunking ve 802.1Q
Birden fazla VLAN trafiğinin tek bir fiziksel kablo (genellikle Switch'ler arası bağlantı) üzerinden taşınması işlemidir.
- **Tagging (Etiketleme):** Paketlerin hangi VLAN'a ait olduğunu belirtmek için paketin içine bir "etiket" (VLAN ID) eklenir. Bu standarda **IEEE 802.1Q** denir.

### 3. VLAN Güvenlik Riskleri
- **VLAN Hopping (VLAN Atlaması):** Bir saldırganın, bulunduğu VLAN'dan başka bir VLAN'ın trafiğine sızmasıdır.
    - **Switch Spoofing:** Saldırgan kendi cihazını bir Switch gibi göstererek "Trunk" bağlantısı kurmaya çalışır. **Önlem:** Kullanılmayan portlar kapatılmalı ve portlar "access" moduna sabitlenmelidir.
    - **Double Tagging:** Pakete iki adet etiket ekleyerek Switch'i yanıltma işlemidir. **Önlem:** "Native VLAN" ID'si varsayılandan (VLAN 1) farklı bir değere değiştirilmelidir.

### 4. Router-on-a-Stick
Farklı VLAN'ların birbirleriyle konuşabilmesi (Inter-VLAN Routing) için bir Router'a veya Layer 3 Switch'e ihtiyaç vardır. Router'ın tek bir portunun alt arayüzlere (sub-interfaces) bölünerek tüm VLAN'lara hizmet vermesine bu ad verilir.

### Gerçek Dünya Analojisi
VLAN, bir otel katındaki odalar gibidir. Odalar yan yanadır (Aynı fiziksel Switch) ama her odanın duvarları vardır ve kimse yan odayı göremez. Trunking ise otelin asansörü gibidir; her kattan insanı (VLAN trafiği) tek bir asansör boşluğundan taşır ama herkes kendi katında iner.