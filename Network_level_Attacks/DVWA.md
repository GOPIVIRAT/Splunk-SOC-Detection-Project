DVWA Attack Simulation & Detection Using Splunk and Wireshark
1. Project Overview

In this project, I set up Damn Vulnerable Web Application (DVWA) on a Kali Linux environment to simulate common web application attacks.
The goal was:

To perform real-world style attacks.

To capture logs and network traffic for detection.

To analyze attacks using Splunk and Wireshark.

To recommend defensive measures against each attack.

This project demonstrates both the attacker’s perspective and the defender’s perspective, making it highly relevant for a SOC Analyst role.

2. Lab Setup

Attacker Machine: Kali Linux

Target Application: DVWA (Damn Vulnerable Web Application)

Monitoring Tools:

Splunk → For log collection & analysis

Wireshark → For packet capture & traffic analysis

All attack attempts were logged and analyzed to validate detections.

3. Attacks Performed & Analysis
3.1 Brute Force Attack

Description:
Attempted repeated login attempts on DVWA using weak/default credentials.

Detection in Splunk:

Multiple failed login attempts within a short time.

HTTP status codes like 401 (Unauthorized) followed by a 200 (Successful login).

Source IP repeatedly targeting the login endpoint (/dvwa/login.php).

Detection in Wireshark:

Observed repeated HTTP POST requests with different username/password combinations.

Mitigation Recommendations:

Implement account lockout after multiple failed attempts.

Enforce strong password policies.

Enable multi-factor authentication (MFA).

Use WAF rules to detect abnormal login attempts.

3.2 Command Injection

Description:
Injected OS commands into DVWA’s vulnerable form (e.g., ; ls, ; ping -c 4 127.0.0.1).

Detection in Splunk:

Suspicious GET/POST requests with shell commands embedded.

HTTP response 200 OK but abnormal request URIs or parameters.

Detection in Wireshark:

Outbound ICMP packets triggered by injected ping command.

Traffic anomaly that would not normally occur during web browsing.

Mitigation Recommendations:

Validate and sanitize all user inputs.

Restrict system calls in web applications.

Deploy Web Application Firewall (WAF) rules for command injection.

3.3 SQL Injection

Description:
Attempted to bypass login and extract data using payloads like ' OR '1'='1.

Detection in Splunk:

SQL-related error messages in responses.

Repeated access to parameters like id=1 OR 1=1.

Sudden increase in database query execution logs.

Detection in Wireshark:

Repeated crafted requests with SQL keywords (UNION, SELECT, OR).

Mitigation Recommendations:

Use parameterized queries (prepared statements).

Sanitize and validate all inputs.

Monitor for abnormal database query patterns.

3.4 Cross-Site Scripting (XSS)

Description:
Injected malicious JavaScript into form fields (e.g., <script>alert("XSS")</script>).

Detection in Splunk:

Logs showing script tags <script> in request parameters.

Unusual encoding/decoding patterns.

Detection in Wireshark:

HTTP responses containing injected JavaScript payloads.

Mitigation Recommendations:

Apply input sanitization and output encoding.

Implement Content Security Policy (CSP).

Use frameworks with built-in XSS protection.

4. Defender’s Perspective

After analyzing all attacks, I documented the attack patterns, detection methods, and defensive recommendations.
This provides a roadmap for improving the organization’s web application security posture.

5. Key Outcomes

Successfully simulated Brute Force, Command Injection, SQL Injection, and XSS attacks.

Validated attack evidence using Splunk & Wireshark.

Recommended actionable defense strategies for each attack.

6. Future Scope

Expand detections by integrating Suricata IDS into Splunk.

Automate detection with SOAR (Security Orchestration, Automation, and Response).

Include alerting and dashboarding for faster incident response.

7. Screenshots

(Insert screenshots of attack execution, Splunk logs, and Wireshark captures here)
