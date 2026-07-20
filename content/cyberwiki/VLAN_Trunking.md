+++
title = "VLAN (Virtual LAN) ve Trunking | VLAN (Virtual LAN) and Trunking"
date = "2026-05-19"
draft = false
categories = ["Networking"]
type = "cyberwiki"
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

---

## English Version

VLAN is a technology of logically dividing a physical network into multiple virtual networks. By grouping ports on a Switch, it allows us to create networks isolated from each other.

### 1. Why Use VLAN?
- **Security (Isolation):** Prevents a computer in the accounting department from directly accessing servers on the software team's network.
- **Performance:** Limits Broadcast traffic (splits Broadcast Domain).
- **Flexibility:** Even if a user changes his desk, he can be kept in the same VLAN by adjusting the port.

### 2. Trunking and 802.1Q
It is the process of carrying multiple VLAN traffic over a single physical cable (usually the connection between Switches).
- **Tagging:** A "tag" (VLAN ID) is added to the packet to indicate which VLAN the packets belong to. This standard is called **IEEE 802.1Q**.

### 3. VLAN Security Risks
- **VLAN Hopping:** It is when an attacker infiltrates the traffic of another VLAN than the VLAN he is in.
    - **Switch Spoofing:** The attacker tries to establish a "Trunk" connection by disguising his own device as a Switch. **Precaution:** Unused ports should be closed and the ports should be fixed to "access" mode.
    - **Double Tagging:** It is the process of misleading the Switch by adding two tags to the package. **Precaution:** The "Native VLAN" ID must be changed to a value other than the default (VLAN 1).

### 4. Router-on-a-Stick
A Router or Layer 3 Switch is needed for different VLANs to talk to each other (Inter-VLAN Routing). This is the name given to the fact that a single port of the router is divided into sub-interfaces and serves all VLANs.

### Real World Analogy
VLAN is like rooms on a hotel floor. The rooms are next to each other (Same physical Switch) but each room has walls and no one can see the next room. Trunking is like a hotel elevator; It carries people from each floor (VLAN traffic) through a single elevator shaft, but everyone gets off on their own floor.
