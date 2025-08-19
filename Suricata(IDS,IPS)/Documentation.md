***📂 Threat Detection using Suricata and Splunk***

**🔎 Project Overview**

In this project, I built a Network Intrusion Detection System (NIDS) using Suricata on Linux to capture malicious traffic and forward logs into Splunk for centralized monitoring and analysis.

I then simulated multiple real-world attacker techniques across different stages of the attack lifecycle, such as:

🔍 Reconnaissance – Nmap scanning to identify open ports and services

🔑 Brute Force Attacks – SSH and RDP brute force attempts using Hydra

📡 Exploitation – Attempted login success/failure tracking on SSH and RDP

🖥️ Lateral Movement – SMB/NetBIOS scans (ports 139, 445)

📥 Malware Delivery Simulation – downloading and executing suspicious files (benign test samples, not real malware)

🌐 Web Application Attacks – SQL injection and XSS test payloads against a test web server

🔒 Defense Evasion – detecting abnormal traffic patterns like ICMP tunneling or suspicious large DNS queries

To validate detection, I wrote custom Suricata rules for each scenario and visualized alerts in Splunk.

This project demonstrates the end-to-end SOC workflow:
➡️ Attack simulation → Detection → Alerting → Investigation → Proof.

🛠️ Step 1: Proof of Log Forwarding to Splunk

First, I configured Suricata to forward its logs (eve.json,fast.log) into Splunk.
This proves that Suricata can monitor traffic and send it to a SIEM for further detection and analysis.

📸 [Add Screenshot: Suricata logs visible in Splunk]

🛠️ Step 2: Port Scanning with Nmap

As an attacker, I used Nmap to scan my victim machine for open ports.
This simulates the reconnaissance phase of an attack.

Example command:

nmap -sS -p- <target-ip>


🛠️ Step 3: Writing Suricata Rules for Detection

Next, I wrote custom Suricata rules to detect scanning attempts on sensitive ports (22, 135, 139, 445, 3389, 5357).

Example rule:

alert tcp any any -> $HOME_NET 22 (msg:"SSH Port Scan Detected"; sid:100001; rev:1;)
alert tcp any any -> $HOME_NET 445 (msg:"SMB Port Scan Detected"; sid:100002; rev:1;)


📸 [Add Screenshot: Suricata rules created and loaded]

🛠️ Step 4: Detection of Port Scan in Splunk

After scanning, Suricata generated alerts for suspicious connections.
Splunk ingested the logs, showing evidence of a port scan attack.

📸 [Add Screenshot: Splunk alert showing port scan detection]

🛠️ Step 5: SSH Brute Force Attack Simulation

Next, I simulated a brute force attack using Hydra against SSH on the victim.

Example command:

hydra -l testuser -P passwords.txt ssh://<target-ip>


📸 [Add Screenshot: Hydra brute force attempts in terminal]

🛠️ Step 6: Writing Suricata Rule for SSH Brute Force

To detect brute force activity, I created a Suricata rule for repeated SSH login attempts.

Example rule:

alert tcp any any -> $HOME_NET 22 (msg:"SSH Brute Force Attempt"; flow:to_server,established; content:"SSH"; sid:100010; rev:1;)


📸 [Add Screenshot: Rule added for SSH brute force]

🛠️ Step 7: SSH Brute Force Detection in Splunk

Suricata generated alerts for brute force attempts, which were visible in Splunk.

📸 [Add Screenshot: Splunk alert for SSH brute force detection]

🛠️ Step 8: Proof of Login (Success or Failure)

If credentials were wrong → multiple failed login attempts seen in Splunk.

If credentials were correct → successful SSH login alert + system logs confirm access.

📸 [Add Screenshot: Failed login + successful login proof]

🔐 Skills Demonstrated

Configuring Suricata IDS

Log forwarding to Splunk

Writing custom IDS rules

Simulating attacks (Nmap, Hydra brute force)

Detecting and validating alerts in Splunk

End-to-end SOC workflow (attack → detection → investigation → proof)
