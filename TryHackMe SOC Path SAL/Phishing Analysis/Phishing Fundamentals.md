
Let's look at the following email address, billy@johndoe.com.

1. The **user mailbox** is billy
2. **@** (thanks Ray)
3. The **domain** is johndoe.com

To simplify this even further, think about the street on which you live on.

- You can think of your street as the **domain**. 
- The recipient's first/last name, along with the house number in this scenario, represents the **user mailbox**. 

With this information, the postal worker delivering the mail knows into which mailbox to put the letter(s). 

Next, let's look at the network protocols used to send an email from the sender to the recipient.

A handful of protocols are involved with the "magic" that takes place when you hit SEND in an email client. 

By now, you should already know that certain protocols were created to handle specific network-related tasks, such as email. 

There are 3 specific protocols involved to facilitate the outgoing and incoming email messages, and they are briefly listed below.

- **SMTP** (**Simple Mail Transfer Protocol)** - It is utilized to handle the sending of emails. 

- **POP3 (Post Office Protocol)** - Is responsible transferring email between a client and a mail server. 

- **IMAP (Internet Message Access Protocol)** - Is responsible transferring email between a client and a mail server. 

You should have noticed that both **POP3** and **IMAP** have the same definition. But there are differences between the two.

The difference between the two is listed below: (credit [AOL](https://help.aol.com/articles/what-is-the-difference-between-pop3-and-imap) -- _[You got mail!](https://www.youtube.com/watch?v=gFBLiHpkcOk)_)

**POP3**

- Emails are downloaded and stored on a single device.
- Sent messages are stored on the single device from which the email was sent.
- Emails can only be accessed from the single device the emails were downloaded to.
- If you want to keep messages on the server, make sure the setting "Keep email on server" is enabled, or all messages are deleted from the server once downloaded to the single device's app or software.

**IMAP**

- Emails are stored on the server and can be downloaded to multiple devices.
- Sent messages are stored on the server.
- Messages can be synced and accessed across multiple devices.

Now let's talk about how email travels from the sender to the recipient.


![[email-network-flow-4.png]]

1. Alexa composes an email to Billy (`billy@johndoe.com`) in her favorite email client. After she's done, she hits the send button.
2. The **SMTP** server needs to determine where to send Alexa's email. It queries **DNS** for information associated with `johndoe.com`. 
3. The **DNS** server obtains the information `johndoe.com` and sends that information to the **SMTP** server. 
4. The **SMTP** server sends Alexa's email across the Internet to Billy's mailbox at `johndoe.com`.
5. In this stage, Alexa's email passes through various **SMTP** servers and is finally relayed to the destination **SMTP** server. 
6. Alexa's email finally reached the destination **SMTP** server.
7. Alexa's email is forwarded and is now sitting in the local **POP3/IMAP** server waiting for Billy. 
8. Billy logs into his email client, which queries the local **POP3/IMAP** server for new emails in his mailbox.
9. Alexa's email is copied (**IMAP**) or downloaded (**POP3**) to Billy's email client.


Another method to obtain the same email header information, and more, is by viewing the '**raw**' email details.
![[email-raw-headers-2b.png]]


Different types of malicious emails can be classified as one of the following:

- **[Spam](https://www.proofpoint.com/us/threat-reference/spam)** - unsolicited junk emails sent out in bulk to a large number of recipients. The more malicious variant of Spam is known as **MalSpam**.
- **[Phishing](https://www.proofpoint.com/us/threat-reference/phishing)** -  emails sent to a target(s) purporting to be from a trusted entity to lure individuals into providing sensitive information. 
- **[Spear phishing](https://www.proofpoint.com/us/threat-reference/spear-phishing) -** takes phishing a step further by targeting a specific individual(s) or organization seeking sensitive information.  
- **[Whaling](https://www.rapid7.com/fundamentals/whaling-phishing-attacks/)** - is similar to spear phishing, but it's targeted specifically to C-Level high-position individuals (CEO, CFO, etc.), and the objective is the same. 
- [**Smishing**](https://www.proofpoint.com/us/threat-reference/smishing) - takes phishing to mobile devices by targeting mobile users with specially crafted text messages. 
- [**Vishing**](https://www.proofpoint.com/us/threat-reference/vishing) - is similar to smishing, but instead of using text messages for the social engineering attack, the attacks are based on voice calls.

Below are typical characteristics phishing emails have in common:

- The **sender email name/address** will masquerade as a trusted entity (**[email spoofing](https://www.proofpoint.com/us/threat-reference/email-spoofing)**)
- The email subject line and/or body (text) is written with a **sense of urgency** or uses certain keywords such as **Invoice**, **Suspended**, etc. 
- The email body (HTML) is designed to match a trusting entity (such as Amazon)
- The email body (HTML) is poorly formatted or written (contrary from the previous point)
- The email body uses generic content, such as Dear Sir/Madam. 
- **Hyperlinks** (oftentimes uses URL shortening services to hide its true origin)
- A [malicious attachment](https://www.proofpoint.com/us/threat-reference/malicious-email-attachments) posing as a legitimate document

A BEC (==Business Email Compromise==) is when an adversary gains control of an internal employee's account and then uses the compromised email account to convince other internal employees to perform unauthorized or fraudulent actions.

---
## 🔗 Bağlantılar
- [[TryHackMe SOC Path SAL/index|🛡️ TryHackMe: SOC Analyst Learning Path]]
- [[index|🏠 Ana İndeks]]
