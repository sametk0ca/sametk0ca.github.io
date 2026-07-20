---
title: "Zero-Knowledge Proofs | Sıfır Bilgi Kanıtları"
date: 2026-07-10
description: "An intuitive explanation of Zero-Knowledge Proofs using the Ali Baba Cave metaphor. / Ali Baba Mağarası benzetmesiyle Sıfır Bilgi Kanıtlarının sezgisel açıklaması."
tags: ["Cryptography", "ZKP", "Security"]
categories: ["Blog"]
ShowToc: true
math: true
mermaid: false
cover:
    image: "/img/xiaohei-zero-knowledge-proofs-1.jpg"
    alt: "Zero-Knowledge Proofs Illustration"
    relative: false
---

# Sıfır Bilgi Kanıtları (ZKP): Sırrı Açıklamadan Bilgiyi Kanıtlamak

Kriptografinin en büyüleyici konseptlerinden biri, bir sırrı açıklamadan o sırra sahip olduğunuzu bir başkasına kanıtlayabilmenizdir. Geleneksel sistemlerde, bir sisteme giriş yapmak için parolanızı (yani sırrınızı) karşı tarafa göndermeniz gerekir. Karşı taraf parolanızı doğrular ama bu süreçte sırrınızı da öğrenmiş olur. Sıfır Bilgi Kanıtları (Zero-Knowledge Proofs - ZKP), bu paradigmayı tamamen değiştirerek gizliliği en üst seviyeye taşır.

## Ali Baba Mağarası Metaforu

ZKP konseptini anlamanın en klasik yolu **Ali Baba Mağarası** benzetmesidir. Ortasında gizli bir kapı olan dairesel (veya Y şeklinde) bir tünel düşünün. Bu kapı sadece gizli bir kelime veya anahtarla açılabilmektedir.

Aşağıdaki illüstrasyonda görebileceğiniz gibi, kanıt sunmak isteyen **Kanıtlayıcı** (Prover - tüneldeki 小黑) kapının anahtarına sahip olduğunu, dışarıda bekleyen **Doğrulayıcı**ya (Verifier - megafonlu 小黑) kanıtlamak istemektedir. Ancak anahtarın kendisini veya gizli kelimeyi doğrulamak amacıyla karşı tarafa vermek istemez.

![İllüstrasyon / Illustration](/img/xiaohei-zero-knowledge-proofs-1.jpg)

Süreç şu şekilde işler:
1. Kanıtlayıcı tünele girer ve kapıya kadar ilerler. Doğrulayıcı onun hangi yoldan gittiğini görmez.
2. Doğrulayıcı mağaranın girişine gelir ve rastgele bir yol seçerek seslenir: *"Sol yoldan çık!"* veya *"Sağ yoldan çık!"* (Rastgele Meydan Okuma).
3. Eğer Kanıtlayıcı gerçekten anahtara sahipse, kapıyı açıp istenen taraftan çıkabilir. Eğer anahtarı yoksa, sadece şans eseri (%50 ihtimalle) doğru tarafta bekliyor olabilir.
4. Bu test defalarca tekrarlanır. 20 kez tekrarlanan bir testte Kanıtlayıcının anahtara sahip olmadan her seferinde doğru taraftan çıkabilme ihtimali $1/2^{20}$ (milyonda bir) civarındadır.

Sonuç olarak Doğrulayıcı, anahtarı hiç görmeden ve gizli kelimeyi hiç duymadan Kanıtlayıcının anahtara sahip olduğuna ikna olur.

## ZKP'nin Üç Temel Özelliği

Bir protokolün sıfır bilgi kanıtı sayılabilmesi için matematiksel olarak üç özelliği karşılaması gerekir:

1. **Eksiksiz Bilgi (Completeness):** Eğer iddia doğruysa ve Kanıtlayıcı dürüstse, dürüst bir Doğrulayıcı her zaman ikna olacaktır.
2. **Güvenilirlik (Soundness):** Eğer iddia yanlışsa, hilekar bir Kanıtlayıcı, dürüst bir Doğrulayıcıyı (çok düşük bir şans olasılığı hariç) asla ikna edemez.
3. **Sıfır Bilgi (Zero-Knowledge):** Eğer iddia doğruysa, Doğrulayıcı iddianın doğruluğu dışında hiçbir ek bilgi (sırrın kendisi) öğrenemez.

## Protokol Yapıları ve Gerçek Hayat Kullanımları

### 1. Sigma ($\Sigma$) Protokolleri
Genellikle üç adımlı etkileşimli bir yapıya sahiptir: **Taahhüt** (Commitment), **Meydan Okuma** (Challenge) ve **Yanıt** (Response). Bu yapı klasik etkileşimli ZKP akışını oluşturur.

### 2. ZK-SNARKs (Succinct Non-Interactive Arguments of Knowledge)
Modern uygulamalarda etkileşimli süreçler verimsizdir. ZK-SNARKs, kanıtların tek bir adımda gönderilmesini ve çok hızlı doğrulanmasını sağlayan etkileşimsiz yapılardır. Özellikle Zcash gibi gizlilik odaklı blockchain projelerinde ve katman-2 ölçekleme çözümlerinde yaygın olarak kullanılır.

### 3. Fiat-Shamir Dönüşümü
Etkileşimli bir Sigma protokolünü, rastgele meydan okumayı bir hash fonksiyonuyla değiştirerek etkileşimsiz dijital imzalara dönüştürme yöntemidir.

Sıfır bilgi kanıtları; şifre paylaşmadan kimlik doğrulama, hassas finansal verileri açıklamadan kredi skoru kanıtlama ve merkeziyetsiz oylama sistemleri gibi gizlilik gerektiren geleceğin teknolojilerinde temel taşı olmaya devam etmektedir.

---

# Zero-Knowledge Proofs (ZKP): Proving Knowledge Without Revealing the Secret

One of the most fascinating concepts in modern cryptography is the ability to prove that you possess a secret without revealing the secret itself. In traditional digital systems, logging in requires sending your password (the secret) to the server. The server verifies it but learns the secret in the process. Zero-Knowledge Proofs (ZKP) completely shift this paradigm, enabling ultimate privacy.

## The Ali Baba Cave Metaphor

The classic way to intuitively grasp ZKP is through the **Ali Baba Cave** metaphor. Imagine a circular or Y-shaped cave with a locked door blocking the middle path. This door can only be unlocked with a secret key or passphrase.

As shown in our hand-drawn illustration below, the **Prover** (the 小黑 inside the tunnel) wants to prove to the **Verifier** (the 小黑 outside with the megaphone) that they know the secret key. However, they refuse to expose the key itself.

![İllüstrasyon / Illustration](/img/xiaohei-zero-knowledge-proofs-1.jpg)

The protocol proceeds as follows:
1. The Prover enters the cave and walks to the door. The Verifier cannot see which path the Prover took.
2. The Verifier approaches the entrance and shouts a random challenge: *"Exit from the Left path!"* or *"Exit from the Right path!"*
3. If the Prover truly possesses the key, they can open the door and exit from the requested side. If they don't, they only have a 50% chance of being on the correct side by luck.
4. By repeating this process multiple times, the probability of cheating decreases exponentially. After 20 rounds, the chance of guessing correctly every time is less than $1/2^{20}$ (about one in a million).

Thus, the Verifier becomes convinced that the Prover knows the secret key, without ever seeing the key or hearing the secret passphrase.

## Three Core Cryptographic Properties

To be mathematically classified as a Zero-Knowledge Proof, a protocol must satisfy three fundamental properties:

1. **Completeness:** If the statement is true and both parties follow the protocol, the honest Verifier will be convinced by the honest Prover.
2. **Soundness:** If the statement is false, a cheating Prover cannot convince the honest Verifier except with an negligibly small probability.
3. **Zero-Knowledge:** If the statement is true, the Verifier learns nothing other than the fact that the statement is true.

## Protocol Architectures and Applications

### 1. Sigma ($\Sigma$) Protocols
These are basic three-flow interactive proofs consisting of a **Commitment** from the prover, a **Challenge** from the verifier, and a **Response** from the prover.

### 2. ZK-SNARKs (Succinct Non-Interactive Arguments of Knowledge)
Interactive proofs are slow and inefficient for distributed systems. ZK-SNARKs enable non-interactive proofs that are very short (succinct) and can be verified in milliseconds, making them perfect for privacy-focused blockchains like Zcash and Ethereum Layer-2 scaling solutions.

### 3. Fiat-Shamir Transform
A technique used to convert interactive Sigma protocols into non-interactive signatures by replacing the Verifier's random challenge with a cryptographic hash of the commitment.

Zero-Knowledge Proofs serve as the foundation for the future of digital identity, secure authentication without password databases, private transactions, and secure decentralized voting.

*This post is linked to the Knowledge Base: [[zero-knowledge-proofs]]*
