**DVWA Attack Simulation & Detection Using Splunk and Wireshark**
**1. Project Overview**

In this project, I set up Damn Vulnerable Web Application (DVWA) on a Kali Linux environment to simulate common web application attacks.
**The goal was:**

To perform real-world style attacks.

To capture logs and network traffic for detection.

To analyze attacks using Splunk and Wireshark.

To recommend defensive measures against each attack.

This project demonstrates both the attacker’s perspective and the defender’s perspective, making it highly relevant for a SOC Analyst role.

**2. Lab Setup**

Attacker Machine: Kali Linux

Target Application: DVWA (Damn Vulnerable Web Application)

**Monitoring Tools:**

Splunk → For log collection & analysis

Wireshark → For packet capture & traffic analysis

All attack attempts were logged and analyzed to validate detections.

**3. Attacks Performed & Analysis**
**3.1 Brute Force Attack**

**Description:**
Attempted repeated login attempts on DVWA using weak/default credentials.

**Detection in Splunk:**

Multiple failed login attempts within a short time.

HTTP status codes like 401 (Unauthorized) followed by a 200 (Successful login).

Source IP repeatedly targeting the login endpoint (/dvwa/login.php).
<img width="1366" height="662" alt="Image" src="https://github.com/user-attachments/assets/e0a53286-f0d9-4960-8811-b27edd959174" /> 
<img width="1327" height="279" alt="Image" src="https://github.com/user-attachments/assets/5b76d306-07c8-4d2a-a016-6f61d1baad80" /> 
<img width="1041" height="555" alt="Image" src="https://github.com/user-attachments/assets/c8f90480-91ed-4b46-9761-3df2c36e8f9a" />  
<img width="1302" height="362" alt="Image" src="https://github.com/user-attachments/assets/60f3bb74-709e-49c5-bece-b20353f71f70" />   

**Detection in Wireshark:**

Observed repeated HTTP POST requests with different username/password combinations.
<img width="1366" height="662" alt="Image" src="https://github.com/user-attachments/assets/aa8a5e78-7514-4312-84c0-6192f2339df8" />

**Mitigation Recommendations:**

Implement account lockout after multiple failed attempts.

Enforce strong password policies.

Enable multi-factor authentication (MFA).

Use WAF rules to detect abnormal login attempts.

**3.2 Command Injection**

**Description:**
Injected OS commands into DVWA’s vulnerable form (e.g., ; ls, ; ping -c 4 127.0.0.1).
<img width="1366" height="662" alt="Image" src="https://github.com/user-attachments/assets/831a9fd1-88ab-41c0-b40e-d69b2eab9093" /> 

**Detection in Splunk:**

Suspicious GET/POST requests with shell commands embedded.

HTTP response 200 OK but abnormal request URIs or parameters.
<img width="1304" height="327" alt="Image" src="https://github.com/user-attachments/assets/5c2934ef-e2b6-43b5-9c0a-a9c270300825" />

**Detection in Wireshark:**

Outbound ICMP packets triggered by injected ping command.

Traffic anomaly that would not normally occur during web browsing.
<img width="1366" height="662" alt="Image" src="https://github.com/user-attachments/assets/18305f26-2ff6-4d2b-b817-fc1f0f8cbc0d" />
<img width="1366" height="662" alt="Image" src="https://github.com/user-attachments/assets/6fbed74c-009c-49da-8710-53027511537d" />
<img width="1366" height="662" alt="Image" src="https://github.com/user-attachments/assets/113ffe59-ddd0-47d0-b3b6-ab9ea408bbde" />
**Mitigation Recommendations:**

Validate and sanitize all user inputs.

Restrict system calls in web applications.

Deploy Web Application Firewall (WAF) rules for command injection.

**3.3 SQL Injection**

**Description:**
Attempted to bypass login and extract data using payloads like ' OR '1'='1.
<img width="1366" height="662" alt="Image" src="https://github.com/user-attachments/assets/5d731bf3-542a-45c5-b419-8f452f5662a2" /> 

**Detection in Splunk:**

SQL-related error messages in responses.

Repeated access to parameters like id=1 OR 1=1.

Sudden increase in database query execution logs.
<img width="1307" height="386" alt="Image" src="https://github.com/user-attachments/assets/0fa82193-c2c3-4557-8491-279e2b098428" />

**Detection in Wireshark:**

Repeated crafted requests with SQL keywords (UNION, SELECT, OR).

<img width="1366" height="662" alt="Image" src="https://github.com/user-attachments/assets/953fafa2-e22f-4d0c-b243-e031b05150fc" />
<img width="1085" height="405" alt="Image" src="https://github.com/user-attachments/assets/39ea61e6-2dda-4454-a7be-265fa9382979" /> 

**Mitigation Recommendations:**

Use parameterized queries (prepared statements).

Sanitize and validate all inputs.

Monitor for abnormal database query patterns.

**3.4 Cross-Site Scripting (XSS)**

**Description:**
Injected malicious JavaScript into form fields (e.g., <script>alert("XSS")</script>).
<img width="1366" height="662" alt="Image" src="https://github.com/user-attachments/assets/18fa0e4f-f52e-4a36-8b3a-bbc0e712f822" /> 
<img width="1366" height="662" alt="Image" src="https://github.com/user-attachments/assets/5cf938ea-ccb6-4c0b-827c-94f45a3d4d49" />

**Detection in Splunk:**

Logs showing script tags <script> in request parameters.

Unusual encoding/decoding patterns.
<img width="1321" height="258" alt="Image" src="https://github.com/user-attachments/assets/798d9189-dfcb-4a39-8705-d3a5760ec33a" />


**Detection in Wireshark:**

HTTP responses containing injected JavaScript payloads.
<img width="1344" height="366" alt="Image" src="https://github.com/user-attachments/assets/59bd98e0-d23e-45e4-a40d-e2a64b8dbf9f" />

**Mitigation Recommendations:**

Apply input sanitization and output encoding.

Implement Content Security Policy (CSP).

Use frameworks with built-in XSS protection.

**4. Defender’s Perspective**

After analyzing all attacks, I documented the attack patterns, detection methods, and defensive recommendations.
This provides a roadmap for improving the organization’s web application security posture.

**5. Key Outcomes**

Successfully simulated Brute Force, Command Injection, SQL Injection, and XSS attacks.

Validated attack evidence using Splunk & Wireshark.

Recommended actionable defense strategies for each attack.


