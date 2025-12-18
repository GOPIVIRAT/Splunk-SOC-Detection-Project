# End-to-End SOC Detection & Monitoring using Splunk and Suricata

In this project, I performed the role of a SOC Analyst, simulating real-world attacks, detecting them using Splunk, Suricata, and Sysmon, and building automated response workflows.
The project covers host-level attacks, network-level intrusions, phishing analysis, and custom Splunk detection rules, along with playbooks for automated response.


<img width="1536" height="672" alt="splunk final project image overview" src="https://github.com/user-attachments/assets/25ab68ce-1063-4a3f-a3fc-dba58da92f65" />


📂 Repository Structure

**📘Attack_Simulations_Docs/** → Performed host-level attacks (failed logins, brute force, privilege escalation, persistence, etc.) and documented their detection with screenshots and detailed proof-of-concepts.

**📘Network_level_Attacks/** → Using Suricata, Wireshark, and Kali Linux (DVWA web app), I executed and detected network-level attacks in Splunk with proper POC screenshots and documentation.

**📘Phishing_Analysis/** → Conducted phishing investigations (header, body, links, attachments) and wrote a few automation scripts to speed up phishing analysis tasks.

**📘Splunk_Rules/** → Developed custom SPL rules and correlation searches to reduce investigation time, mapped them to the MITRE ATT&CK framework for better threat coverage.

**📘Study_material/** → Notes, references, and research material I used throughout the project — helpful for SOC analyst learning and continuous improvement.

**📘n8n(SOAR)/**-->Designed automated incident response workflows in n8n, starting with SSH-based actions  triggered directly from Splunk alerts. This proves end-to-end SOAR automation, and in the future, the same framework can be extended to include advanced playbooks like (e.g., disabling users, blocking IPs)firewall rule updates, ticketing system integration, showcasing strong knowledge of real-world SOAR operations.

**📘Active_Directory/** → Basic understanding and setup notes for Windows AD; no project yet, but kept for future extension if time permits.
