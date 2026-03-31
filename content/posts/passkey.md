---
showToc: true
title: "Passkey: Parolaların Sonu mu Geldi? | Is This the End of Passwords?"
date: 2026-03-31
draft: false
tags: ["Passkey", "Authentication", "Security", "Phishing"]
categories: ["Blog"]
cover:
    image: "https://images.unsplash.com/photo-1633265485768-3066373f1721?q=80&w=2070&auto=format&fit=crop"
    alt: "Passkeys"
    relative: false
---


# Parolaların Sonu mu Geldi? 

Son zamanlarda internette gezinirken bir siteye giriş yapmaya çalıştığınızda, "Bu site için bir Passkey oluşturmak ister misiniz?" gibi bir mesajın giderek daha sık karşınıza çıktığını fark ettiniz mi? Eğer bu durum kafanızı karıştırdıysa, yalnız değilsiniz. Çoğu kullanıcı bu yeni teknolojinin tam olarak ne olduğunu ve neden önemli olduğunu bilmiyor. 

**1. Bu Bir Parola Değil, Dijital Bir İmza**

Passkey'ler hakkında anlaşılması gereken en temel şey, bildiğiniz bir sırra (parola) değil, kriptografik bir ilkeye dayanmalarıdır: açık anahtar kriptografisi.

Bu konsepti basitçe şöyle özetleyebiliriz: Cihazınızda gizli tutulan bir **özel anahtar** ve giriş yapmak istediğiniz web sitesiyle paylaşılan bir **açık anahtar** olmak üzere iki anahtarınız vardır. Bu sistemin amacı verileri şifrelemek değil, dijital bir imza kullanarak kimliğinizi tartışmasız bir şekilde kanıtlamaktır. Süreç genel hatlarıyla şöyle işler: Web sitesi size benzersiz bir "challenge" (token) gönderir, cihazınızdaki "doğrulayıcı" bu token'ı özel anahtarınızla imzalar. Web sitesi daha sonra bu imzayı sizin açık anahtarınızı kullanarak doğrular ve giriş yapmanıza izin verir. Bu yöntem, internet üzerinden asla bir sır göndermeden sizin siz olduğunuzu kanıtlar.

"bir web sitesine parolanızı yazmak yerine, size bir token gönderirler, siz onu özel anahtarınızla imzalarsınız, onlar da bunu açık anahtarınızla doğrulayarak içeri girmenize izin verirler"

![](/Pasted%20image%2020260107172727.png)

**2. Neredeyse Tamamen Oltalama (Phishing) Saldırılarına Karşı Korumalıdır**

Bu, Passkey'lerin parolalara kıyasla en büyük avantajlarından biridir. Peki bu nasıl mümkün oluyor? Bir Passkey oluşturulduğunda, doğası gereği web sitesinin belirli alan adına (örneğin, `amazon.co.uk`) bağlanır.

Bir oltalama saldırısı senaryosunu düşünelim: Kullanıcı, sahte bir web sitesine (`mike-special-amazon.co.uk` gibi) yönlendiren bir oltalama bağlantısına tıklar. Tarayıcı, bu URL'in Passkey ile birlikte saklanan alan adı kimliğiyle eşleşmediğini görür. Sonuç olarak, sistem giriş için Passkey'i sunmayı reddeder ve saldırıyı tamamen etkisiz hale getirir.

"eğer bana bir e-posta gönderip 'bu web sitesine gir ve oturum aç' derseniz, web sitesinin URL'si bu gerçek URL olmayacak, hiçbiri eşleşmeyecek ve bu sistem sizin için etkinleşmeyecektir"

**3. Dizüstü Bilgisayarınızdaki Passkey, Telefonunuzda Çalışmaz (Genellikle)**

Kullanıcıların aklına gelen yaygın sorulardan biri şudur: "Dizüstü bilgisayarımda bir Passkey ayarlarsam, bunu telefonumda nasıl kullanırım?"

Cevap, tasarım gereği genellikle kullanamayacağınızdır. Standart bir Passkey'in özel anahtarı, belirli bir "doğrulayıcıda" (dizüstü bilgisayardaki Windows Hello veya telefondaki güvenli donanım gibi) saklanır ve o cihaza bağlıdır. Bu durum "bağlam bağlama" (context binding) olarak bilinir. Bu "bağlam bağlama" özelliği, dizüstü bilgisayarınızda oluşturulan anahtarın, o cihaza ve o tarayıcıya "kilitli" olduğu anlamına gelir. Telefonunuz tamamen farklı bir "bağlam" olduğu için o kilidi açamaz.

Ancak bu kuralın bir istisnası vardır: Eğer doğrulayıcı, cihazlar arasında senkronize olan bir parola yöneticisi gibi "taşınabilir" bir yapıdaysa, bu sınırlama ortadan kalkabilir.

**4. Telefonunuzu Kaybetmek, Passkey'inizi Sonsuza Dek Kaybetmek Anlamına Gelebilir**

Passkey'lerin günümüzdeki en büyük pratik sorunu kurtarma işlemidir. Eğer doğrulayıcınız (örneğin telefonunuz) kaybolur, çalınır veya bozulursa, üzerinde saklanan özel anahtar juga sonsuza dek kaybolur. Artık o Passkey'i kullanarak giriş yapamazsınız. Peki bu, telefonunuzu çalan birinin tüm hesaplarınıza erişebileceği anlamına mı gelir? Genellikle hayır. Çoğu Passkey sistemi, imzalama isteğini onaylamadan önce PIN, parmak izi veya yüz tanıma gibi bir "kullanıcı doğrulaması" talep eder. Bu, cihazınız ele geçirilse bile ek bir güvenlik katmanı sağlar.

Yine de, anahtarı kaybettiğinizde hesaba erişiminizi nasıl geri alırsınız? Mevcut ve ironik çözüm, hesaba yeniden erişim sağlamak için eski parolanızı kullanmaya geri dönmektir. Parola nihai yedekleme mekanizması olarak kaldığı sürece, parolaların temel sorunu olan oltalama saldırıları tam olarak çözülmüş sayılmaz.

"eğer cep telefonumda bir doğrulayıcı ve istemci olarak da tarayıcımı kullanıyorsam ve sonra telefonum parçalanırsa ya da çalınırsa ve yeni bir telefon alırsam, şimdi buraya, web sitesine nasıl giriş yapacağım? O Passkey ile değil, onu söyleyebilirim, çünkü onu asla geri alamayacağım. Cevap: bir parolayla."

**5. En Büyük Engel Teknoloji Değil, Biziz**

Teknik detaylardan ziyade insan faktörüne odaklandığımızda, Passkey'lerin yaygınlaşmasının önündeki en büyük engelin teknoloji değil, kullanıcıların konuyu anlaması ve eğitilmesi olduğunu görüyoruz.

Kullanıcı deneyimi oldukça kafa karıştırıcı olabiliyor. Bir web sitesi "Passkey ekle" diye soruyor, kullanıcı "evet"e tıklıyor ve ardından birden fazla seçenek (parola yöneticisi, Windows Hello vb.) beliriyor. Kullanıcı, bir Passkey'in ne olduğunu bile bilmediği için süreci yarıda bırakabiliyor. Durumu daha da karmaşıklaştıran şey ise, bir kullanıcının aynı web sitesi için birden fazla Passkey'e sahip olabilmesidir; örneğin biri dizüstü bilgisayarındaki Windows Hello'dan, diğeri telefonundan ve bir başkası parola yöneticisinden gelebilir. Genellikle tek bir parolaya alışkın olan kullanıcılar için bu durum oldukça kafa karıştırıcıdır.

Passkey'lerin parolaların yerini gerçekten alabilmesi için, halka ne olduklarını ve neden faydalı olduklarını anlatmak üzere büyük bir çaba gösterilmesi gerekiyor.

**Sonuç**

Passkey'ler, oltalama gibi uzun süredir devam eden birçok sorunu çözen, parolalara göre daha güçlü, daha güvenli ve daha kullanışlı bir alternatiftir. Teknolojik olarak üstün olsalar da, yaygınlaşmaları hem kurtarma sorunlarının çözülmesine hem de kullanıcıların bu yeni sisteme adapte olmasına bağlıdır. Bu yeni teknoloji, güvenliğe dair en büyük sorunlarımızdan bazılarını çözerken, aynı zamanda sorumluluğu da doğrudan bizim ve cihazlarımızın üzerine yüklüyor.

Peki, tüm dijital kimliğimizi tek bir cihazı kaybetmenin bizi dışarıda bırakabileceği bir sisteme emanet etmeye hazır mıyız, yoksa eski ve kusurlu parolalarımız daha uzun yıllar boyunca güvenlik ağımız olmaya devam mı edecek?

---
showToc: true

# Is This the End of Passwords?

Lately, have you noticed a message like "Would you like to create a Passkey for this site?" appearing more and more frequently when you try to log in to a website? If this situation has confused you, you are not alone. Most users do not know exactly what this new technology is or why it is important.

### 1. It Is Not a Password, It’s a Digital Signature

The most fundamental thing to understand about Passkeys is that they are not based on a secret you know (a password), but on a cryptographic principle: **public key cryptography**.

We can simplify this concept as follows: You have two keys—a **private key** kept secret on your device and a **public key** shared with the website you want to log in to. The purpose of this system is not to encrypt data, but to prove your identity beyond dispute using a digital signature. The process generally works like this: The website sends you a unique "challenge" (token); the "authenticator" on your device signs this token with your private key. The website then verifies this signature using your public key and grants you access. This method proves you are who you say you are without ever sending a "secret" over the internet.

> "Instead of typing your password into a website, they send you a token, you sign it with your private key, and they allow you in by verifying it with your public key."


![](/Pasted%20image%2020260107172727.png)

### 2. Almost Entirely Immune to Phishing Attacks

This is one of the greatest advantages of Passkeys compared to passwords. But how is this possible? When a Passkey is created, it is inherently tied to a specific domain name of the website (e.g., `amazon.co.uk`).

Consider a phishing scenario: A user clicks on a phishing link that directs them to a fake website (like `mike-special-amazon.co.uk`). The browser sees that this URL does not match the domain identity stored with the Passkey. As a result, the system refuses to present the Passkey for login, rendering the attack completely ineffective.

> "If you send me an email saying 'go to this website and log in,' the URL of the website will not be the real URL; none of them will match, and this system will not activate for you."

### 3. A Passkey on Your Laptop Won’t Work on Your Phone (Usually)

A common question users have is: "If I set up a Passkey on my laptop, how do I use it on my phone?"

The answer is that, by design, you generally cannot. The private key of a standard Passkey is stored in a specific "authenticator" (such as Windows Hello on a laptop or secure hardware on a phone) and is tied to that device. This is known as **"context binding."** This "context binding" feature means that the key created on your laptop is "locked" to that device and that browser. Since your phone is a completely different "context," it cannot open that lock.

However, there is an exception to this rule: If the authenticator is a "portable" structure, such as a password manager that synchronizes across devices, this limitation may be removed.

### 4. Losing Your Phone Might Mean Losing Your Passkey Forever

The biggest practical issue with Passkeys today is the recovery process. If your authenticator (e.g., your phone) is lost, stolen, or broken, the private key stored on it is also lost forever. You can no longer log in using that Passkey. Does this mean someone who steals your phone can access all your accounts? Generally, no. Most Passkey systems require "user verification," such as a PIN, fingerprint, or facial recognition, before approving a signing request. This provides an extra layer of security even if your device is compromised.

Still, how do you regain access to the account when you lose the key? The current and ironic solution is to revert to using your old password to regain access. As long as the password remains the ultimate backup mechanism, the fundamental problem of passwords—phishing attacks—is not fully solved.

> "If I am using an authenticator on my mobile phone and my browser as a client, and then my phone is smashed or stolen and I get a new phone, how do I log in to the website now? I can tell you it won't be with that Passkey, because I will never get it back. The answer: with a password."

### 5. The Biggest Hurdle Isn't Technology, It’s Us

When we focus on the human factor rather than technical details, we see that the biggest obstacle to the widespread adoption of Passkeys is not the technology, but the users' understanding and education on the subject.

The user experience can be quite confusing. A website asks to "Add a Passkey," the user clicks "yes," and then multiple options (password manager, Windows Hello, etc.) suddenly appear. Because the user doesn't even know what a Passkey is, they might abandon the process halfway through. Making matters more complex is that a user can have multiple Passkeys for the same website; for example, one from Windows Hello on their laptop, another from their phone, and another from a password manager. For users who are generally accustomed to a single password, this situation is quite perplexing.

For Passkeys to truly replace passwords, a major effort is needed to explain to the public what they are and why they are beneficial.

### Conclusion

Passkeys are a stronger, more secure, and more convenient alternative to passwords, solving many long-standing issues like phishing. While they are technologically superior, their widespread adoption depends on both solving recovery issues and users adapting to this new system. While this new technology solves some of our biggest security problems, it also places the responsibility directly on us and our devices.

So, are we ready to entrust our entire digital identity to a system where losing a single device could lock us out, or will our old and flawed passwords remain our safety net for many more years to come?
