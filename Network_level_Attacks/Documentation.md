***📂 Threat Detection using Suricata and Splunk***

**🔎 Project Overview**

In this project, I built a Network Intrusion Detection System (NIDS) using Suricata on Linux to capture malicious traffic and forward logs into Splunk for centralized monitoring and analysis.

 Then i simulated multiple real-world attacker techniques across different stages of the attack lifecycle, such as:

🔍 Reconnaissance – Nmap scanning to identify open ports and services

🔑 Brute Force Attacks – SSH and RDP brute force attempts using Hydra

📡 Exploitation – Attempted login success/failure tracking on SSH and RDP

🖥️ Lateral Movement – SMB/NetBIOS scans (ports 139, 445)

📥 Malware Delivery Simulation – downloading and executing suspicious files (benign test samples, not real malware)

🌐 Web Application Attacks – SQL injection and XSS test payloads against a test web server

🔒 Defense Evasion – detecting abnormal traffic patterns like ICMP tunneling or suspicious large DNS queries

To validate detection, I wrote custom Suricata rules for each scenario and visualized alerts in Splunk.

This project demonstrates the end-to-end SOC workflow:

**➡️ Attack simulation → Detection → Alerting → Investigation → Proof.**

**🛠️ Step 1: Proof of Log Forwarding to Splunk**

First, I configured Suricata to forward its logs (eve.json,fast.log) into Splunk.
This proves that Suricata can monitor traffic and send it to a SIEM for further detection and analysis.

<img width="1282" height="490" alt="Image" src="https://github.com/user-attachments/assets/452939af-0555-4ec9-88c2-ef5725b4b6c1" /> 

**🛠️ Step 2: Port Scanning with Nmap**

As an attacker, I used Nmap to scan my victim machine for open ports.
This simulates the reconnaissance phase of an attack.

<img width="710" height="251" alt="Image" src="https://github.com/user-attachments/assets/13e42b55-a693-4a58-8c85-c2e80bedbc5d" />

**🛠️ Step 3: Writing Suricata Rules for Detection**

<img width="1293" height="449" alt="Image" src="https://github.com/user-attachments/assets/4f1500fa-4a1e-434d-9c9f-8e3228f0aa3f" />


**🛠️ Step 4: Detection of Port Scan in Splunk**

After scanning, Suricata generated alerts for suspicious connections.
Splunk ingested the logs, showing evidence of a port scan attack.

<img width="1283" height="618" alt="Image" src="https://github.com/user-attachments/assets/155c0f64-a2ad-4390-8b16-78f7bbce1745" /> 

<img width="854" height="534" alt="Image" src="https://github.com/user-attachments/assets/19ec1e72-74de-461c-a1e9-f03c8a825228" /> 


**🛠️ Step 5: SSH Brute Force Attack Simulation**

Next, I simulated a brute force attack using Hydra against SSH on the victim.

<img width="1336" height="606" alt="Image" src="https://github.com/user-attachments/assets/31cb23e9-149d-462b-9d2e-bbc3e9b36577" /> 


**🛠️ Step 6: SSH Brute Force Detection in Splunk**

Suricata generated alerts for brute force attempts, which were visible in Splunk.

<img width="1304" height="640" alt="Image" src="https://github.com/user-attachments/assets/11f8881c-deee-4199-adb7-1abbac8d1505" /> 

**🛠️ Step 7: Proof of Login (Success or Failure)**

If credentials were wrong → multiple failed login attempts.

<img width="1336" height="606" alt="Image" src="https://github.com/user-attachments/assets/31cb23e9-149d-462b-9d2e-bbc3e9b36577" /> 

**Detection:**

<img width="1299" height="426" alt="Image" src="https://github.com/user-attachments/assets/e8af6416-96bd-46e7-a685-e330f20007c2" /> 


If credentials were correct → successful SSH login confirm access linux.

<img width="1366" height="662" alt="Image" src="https://github.com/user-attachments/assets/d54611a6-981c-41ec-959a-67065e59d435" /> 

**🛠️ Step 8: Login detection in splunk**

<img width="1219" height="306" alt="Image" src="https://github.com/user-attachments/assets/03eb64c0-550c-4794-abf8-05f958152a0a" /> 


**🔐 Skills Demonstrated**

Configuring Suricata IDS

Log forwarding to Splunk

Writing custom IDS rules

Simulating attacks (Nmap, Hydra brute force)

Detecting and validating alerts in Splunk

End-to-end SOC workflow (attack → detection → investigation → proof)
