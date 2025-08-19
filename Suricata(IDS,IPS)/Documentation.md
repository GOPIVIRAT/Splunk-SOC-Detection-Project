**📂 Project: Network Threat Detection using Suricata and Splunk**
**🔎 Project Overview**

In this project, I built a Network Intrusion Detection System (NIDS) using Suricata to capture and analyze malicious traffic, and integrated the logs into Splunk for monitoring and threat hunting.
The goal was to simulate real-world attacker behavior (port scanning, brute force attacks, unauthorized access) and then create detection rules to alert on these activities.

This project demonstrates how network-based security monitoring complements host-based security to give a full SOC visibility.

**⚙️ Lab Setup**

Attacker Machine: Kali Linux (used for nmap, hydra, etc.)

Victim Machine: Ubuntu / Windows (running SSH & RDP services)

NIDS: Suricata (deployed on monitoring interface)

SIEM: Splunk (receiving Suricata’s eve.json,fast.log logs)


**🛠️ Attack Simulations & Detections**
1. Port Scanning with Nmap

**Attack:**
Used nmap to discover open ports on the victim machine.
**Example:**

nmap -sS -p- <target-ip>


**Detection:**
Suricata rules detected suspicious connection attempts to multiple ports.
Alerts were forwarded to Splunk and visualized as "Port Scan Detected".

Screenshots: all port scan find, scanning nmap, suricata rules.

**2. SSH Brute Force Attack**

**Attack:**
Used Hydra to brute force SSH login with a custom wordlist.
**Example:**

hydra -l user -P passwords.txt ssh://<target-ip>


**Detection:**
Suricata custom rule was written to trigger on multiple SSH attempts.
Logs in Splunk showed brute force alerts.

Screenshots: bruteforce ssh, ssh failed, ssh login detection.

**3. Successful SSH Access**

**Attack:**
After brute force, correct credentials were used to log in.

**Detection:**

Suricata flagged SSH session initiation.

Windows Event Logs (ID 4624) confirmed successful login.

Splunk correlation showed proof of compromise.

Screenshots: login proof, password found ssh login, ssh accesss.

**4. RDP Port Scan**

**Attack:**
Scanned for exposed RDP ports (3389).

**Detection:**
Suricata raised alerts for connections to sensitive service ports.

Screenshots: port scan rdp.

**📊 Detection Engineering**

I wrote custom Suricata rules for detecting:

Port scans on sensitive ports (22, 135, 139, 445, 3389, 5357).

SSH brute force attempts.

Unauthorized SSH access.

All alerts were forwarded to Splunk where I built dashboards and searches for attack detection, correlation, and investigation.

**🔐 Key Skills Demonstrated**

Network Intrusion Detection (Suricata)

Log Forwarding & Parsing (eve.json,fast.log → Splunk)

Threat Hunting in Splunk

Writing IDS Rules (Suricata signatures)

Attack Simulation (Nmap, Hydra, SSH/RDP exploitation)

SOC Workflow (Detection → Investigation → Validation)

**🚀 Next Steps**

Simulate web attacks (SQL Injection, XSS on DVWA).

Simulate malware infection using EICAR or Atomic Red Team.

Build correlation rules in Splunk (link host + network logs).
