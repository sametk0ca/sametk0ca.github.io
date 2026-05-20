As with any other department, the efficiency of the SOC team can be measured using different indicators and metrics. This room explores the most common evaluation approaches like ==MTTD== (Mean Time To Detect)and ==MTTR== (Mean Time To Response) and describes both methods to improve the metrics and potential consequences of ignoring them.
## Alerts Count

Imagine starting your shift and seeing 80 unresolved alerts in the queue. That's definitely overwhelming and prone to missing real threats hiding behind the noise spam. On the other hand, consider a whole week without any alerts. Sounds better at first glance, but also concerning since a too low count of alerts may indicate an issue in the SIEM or lack of visibility, leading to undetected breaches. The ideal metric value depends on company size but in general, **5 to 30 alerts per day per L1 analyst is a good metric**.

## False Positive Rate

If 75 out of 80 alerts (94%) were confirmed to be False Positives like system noise or typical IT activity - that's a bad signal for your team. With more noise, analysts tend to become less vigilant and more likely to miss the threat and treat all alerts just like "yet another spam". A False Positive rate of **0% is an unachievable ideal, but 80% or higher is a serious problem**, usually fixed by a tool and detection rules tuning, often called "False Positive Remediation".

## Alert Escalation Rate


L2 analysts rely on L1 to filter out the noise and escalate only the actionable, threatening alerts. At the same time, as L1, you don't want to be overconfident and triage alerts you do not fully understand without a senior support. The alert escalation rate comes in handy to evaluate how experienced and independent the L1 analysts are and how often they decide to escalate the alert. It is usually **aimed to be below 50%, or even better below 20%**.

## Threat Detection Rate

Imagine that out of six attacks for 2025, your SOC team detected and prevented four attacks, missed the fifth because of the broken detection rule, and the sixth because one of the L1 analysts misclassified the breach as False Positive. The resulting metric is TDR = 4 / 6 = 67%, and this is a very bad result. The threat detection rate **should always be at 100%** since every missed threat can have devastating consequences, such as ransomware infection and data exfiltration.

Next, remember that an alert by itself will not stop the breach, and it is important to timely receive the alert, triage it, and respond to the attack before the attackers achieve their goals. The requirements to ensure a quick detection and remediation of the threat are commonly grouped into a **Service Level Agreement (SLA)** - a document signed between the internal SOC team and its company management, or by the managed SOC provider (MSSP) and its customers. The agreement usually requires quick threat detection (measured by **MTTD**), timely alert acknowledgement by L1 analysts (measured by **MTTA**), and finally, prompt response to the threat, like isolating the device or securing the breached account (measured by **MTTR**):

![[678ecc92c80aa206339f0f23-1746642255233.svg]]

---
## 🔗 Bağlantılar
- [[TryHackMe SOC Path SAL/index|🛡️ TryHackMe: SOC Analyst Learning Path]]
- [[index|🏠 Ana İndeks]]
