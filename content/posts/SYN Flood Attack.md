---
title: "SYN Flood"
date: 2026-01-04
draft: false
tags: ["DDoS", "Network Security", "Red Team"]
categories: ["Writeups"]
---



## (TR) Türkçe Versiyon

Siber güvenlik dünyasında saldırı yöntemleri, isimleri karmaşık olsa da genellikle günlük hayattaki davranışların dijital yansımalarıdır. Bugün, bir sunucuyu devre dışı bırakmanın en klasik yollarından biri olan **SYN Flood** saldırısını inceleyeceğiz.

Günümüz ilişkilerinde sıkça duyduğumuz bir kavram var: **“Ghosting”**. Yani birisiyle güzel güzel konuşurken aniden ortadan kaybolmak. İşte SYN Flood, tam olarak bir hackerın hedef sunucuya “ghosting” uygulamasından ibarettir.

Gelin bu sürecin teknik detaylarına ve sunucunun neden bu duruma yenik düştüğüne bakalım.

### Normal Süreç: 3-Zamanlı El Sıkışma (3-Way Handshake)

İnternetteki güvenilir veri iletimi (TCP), iki tarafın birbirini teyit etmesiyle başlar. İstemci (kullanıcı) ve Sunucu arasında gerçekleşen bu görüşme üç aşamadan oluşur:

1. **SYN (Sen):** “Selam sunucu, bağlantı kurmak istiyorum.”
2. **SYN-ACK (Sunucu):** “Selam, isteğini aldım ve onaylıyorum. Hazır mısın?”
3. **ACK (Sen):** “Evet hazırım, veri alışverişine başlayalım.”

Bu son aşamadan sonra bağlantı kurulur ve web sayfası yüklenmeye başlar.

### Saldırı Anı: Cevapsız Bekleyiş

SYN Flood saldırısında hacker, bu nezaket kuralını kötüye kullanır. İletişimi başlatır ama asla tamamlamaz.

Senaryo şöyle gelişir:

1. Saldırgan sunucuya **SYN** paketini gönderir (Bağlantı isteği).
2. Sunucu bu isteği alır, hafızasında (RAM) bu bağlantı için bir yer ayırır ve **SYN-ACK** cevabını gönderir.
3. **Ve sessizlik…** Saldırgan, son onay mesajı olan **ACK** paketini asla göndermez.

Sunucu, karşı taraftan cevap gelmeyince “Belki bağlantısı yavaştır” diye düşünerek beklemeye devam eder. Bu duruma **Half-Open (Yarı Açık) Bağlantı** denir.





### Sunucu Neden Çöküyor?

Her sunucunun aynı anda bekletebileceği bağlantı istekleri için bir kapasitesi vardır. Buna **Backlog Queue (Bekleme Kuyruğu)** denir.

Hacker, saniyede binlerce sahte IP adresi üzerinden “Selam” deyip ortadan kaybolduğunda, sunucunun bekleme kuyruğu “cevap gelmesini bekleyen” yarım kalmış bağlantılarla dolar.

Kuyruk tamamen dolduğunda, sunucu artık **gerçek kullanıcılardan** gelen istekleri kabul edemez hale gelir. Siz web sitesine girmeye çalıştığınızda, sunucu size cevap veremez çünkü tüm kaynaklarını, onu “ghostlayan” sahte isteklere cevap beklemek için harcıyordur.

Sonuç: Hizmet Kesintisi (DoS).

### Nasıl Korunulur?

Bu durumdan korunmanın en yaygın yollarından biri **SYN Cookies** yöntemidir. Sunucu, gelen ilk isteğe hemen kaynak ayırmak yerine, cevabın içine şifreli bir imza (cookie) gizler. Ancak karşı taraf son onayı (ACK) gönderdiğinde bu imzayı kontrol eder ve kaynağı o zaman ayırır. Böylece sunucu, boş yere bekletilmekten kurtulur.

Buna ek olarak sunucu cevaplar için **timeout** da ayarlayabilir. Karşı taraftan bir süre cevap gelmezse onun için ayırdığı kaynağı serbest bırakır (ne kadar tanıdık değil mi?).

**Özetle:** SYN Flood, sunucuyu binlerce sonuçsuz diyalog içinde boğmaktır. Modern güvenlik duvarları ve doğru konfigürasyonlarla bu hayaletlerden korunmak mümkündür.

## (EN) English Version

In the world of cybersecurity, many attack vectors act like digital reflections of real-world behaviors. Today, we will look at one of the most classic ways to overwhelm a server: the **SYN Flood** attack.

We are all familiar with the modern dating concept of **“Ghosting”** — initiating contact with someone, getting a reply, and then suddenly vanishing without a trace. Technically speaking, a SYN Flood is essentially a hacker “ghosting” a server on a massive scale.

Let’s break down the mechanics of this attack and why servers fall for it.

### The Normal Process: The 3-Way Handshake

Reliable data transmission on the internet (TCP) starts with a mutual agreement between the client and the server. This is known as the **3-Way Handshake**:

1. **SYN (You):** “Hello server, I’d like to connect.”
2. **SYN-ACK (Server):** “Hi! Request acknowledged. Are you ready?”
3. **ACK (You):** “Yes, I am. Let’s start exchanging data.”

Once this third step is complete, the connection is established, and the website loads.

### The Attack: Left on “Read”

In a SYN Flood attack, the hacker exploits this protocol. They initiate the conversation but deliberately refuse to finish it.

Here is the scenario:

1. The attacker sends a **SYN** packet (Connection request).
2. The server receives it, allocates memory resources for this new connection, and replies with a **SYN-ACK**.
3. **Then, silence…** The attacker never sends the final **ACK** confirmation.

The server, assuming the user might just have a slow connection, keeps the port open and waits. This state is called a **Half-Open connection**.




### Why Does the Server Crash?

Every server has a limit on how many pending connections it can handle at once. This is called the **Backlog Queue**.

When a hacker sends thousands of “Hello” requests per second from spoofed IP addresses and then vanishes, the server’s backlog queue fills up with these half-open connections.

Once the queue is full, the server cannot accept any requests from **legitimate users**. When a real person tries to visit the website, the server is too busy waiting for the “ghosts” to reply. The result is a Denial of Service (DoS).

### How to mitigate it?

One of the most effective defenses is using **SYN Cookies**. Instead of allocating memory immediately upon receiving a request, the server encodes the connection details into the sequence number (a cookie) of its reply. The server only allocates resources _after_ the final ACK is received and the cookie is verified. This prevents the memory from being exhausted by fake requests.

In addition, the server can set a timeout for replies. If the other party doesn’t respond for a while, it releases the resource it reserved for the other party (how familiar, right?).

**In short:** A SYN Flood is about drowning the server in thousands of unfinished conversations. With modern firewalls and proper configuration, it is possible to protect your infrastructure from these digital ghosts.