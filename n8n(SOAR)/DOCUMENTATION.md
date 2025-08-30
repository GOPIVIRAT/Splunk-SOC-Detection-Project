
**🚀 Automated Alerting Workflow (Suricata → Splunk → n8n → Alerting)**

To enhance incident response efficiency, I integrated Suricata IDS with Splunk for log analysis and then automated alert forwarding to n8n for real-time notifications.

**📌 Detection:** Suricata generated alerts for suspicious activities (e.g., SSH brute force attempts).

**📌 Correlation in Splunk:** I wrote custom SPL queries to track repeated login failures, aggregate events, and detect brute-force patterns.

**📌 Automation with n8n:** Using webhooks, I automated the process of pushing Splunk alerts into n8n workflows. This allowed real-time notifications and further automated actions (e.g., sending alerts, triggering response workflows).

**📌 Outcome:** Security events such as “Possible SSH Brute Force Attempt” were detected in Splunk and instantly forwarded to n8n, reducing response time and enabling proactive defense.

<img width="1303" height="379" alt="image" src="https://github.com/user-attachments/assets/9c510bcc-f753-4c17-8cb4-39458a52f4e2" />



<img width="1074" height="458" alt="image" src="https://github.com/user-attachments/assets/ef88f567-85c0-4604-bf7c-e1a2536129b2" />

**Phishing Analysis - URLScan.io and VirusTotal**


<img width="1068" height="405" alt="image" src="https://github.com/user-attachments/assets/15ed8c0e-647a-4db3-a35e-b8999b817db8" />

