**🛡️ Security Operations Project: Detecting Web Attacks with Splunk**
**1. Project Overview**

This project demonstrates how different types of web application attacks can be simulated on DVWA (Damn Vulnerable Web Application) and then detected in Splunk through log analysis.

**The documentation covers:**

Attack execution (with screenshots).

Captured logs in Splunk.

Detection queries and dashboards.

Future extension with real-world datasets.

**Lab Setup:**

DVWA running on Apache (local VM).

Splunk Enterprise with Universal Forwarder for log ingestion.

Wireshark for traffic observation.

**2. Attack Scenarios**
**2.1 Brute Force Attack**

Attack Performed: Multiple login attempts with different credentials.

Screenshot 1: DVWA brute force login page with repeated attempts.

Screenshot 2: Splunk search showing multiple login attempts from the same IP.

Splunk Detection Query:

index=dvwa sourcetype=access_combined "vulnerabilities/brute"
| stats count by clientip, uri_path 
| where count > 5


Detection Logic: Flags brute force attempts when >5 login tries are made by the same IP.

**2.2 SQL Injection (SQLi)**

Attack Performed: Injected payloads such as ' OR '1'='1 into login fields.

Screenshot 1: DVWA login field with SQLi payload.

Screenshot 2: Splunk query highlighting suspicious parameters in logs.

**Splunk Detection Query:**

index=dvwa sourcetype=access_combined 
(uri_query="*' OR*" OR uri_query="*1=1*") 
| stats count by clientip, uri_query


Detection Logic: Detects requests containing SQL injection keywords.

**2.3 Cross-Site Scripting (XSS)**

Attack Performed: Injected <script>alert('xss')</script> into input fields.

Screenshot 1: DVWA input box with XSS payload.

Screenshot 2: Splunk logs showing <script> injection attempts.

**Splunk Detection Query:**

index=dvwa sourcetype=access_combined 
(uri_query="*<script>*" OR uri_query="*alert(*") 
| stats count by clientip, uri_query


Detection Logic: Flags attempts to inject malicious JavaScript.

**2.4 Command Injection**

Attack Performed: Payloads like ; ls -la or && cat /etc/passwd were used.

Screenshot 1: DVWA command execution page with payload.

Screenshot 2: Splunk logs highlighting suspicious shell characters.

**Splunk Detection Query:**

index=dvwa sourcetype=access_combined 
(uri_query="*;*" OR uri_query="*&&*") 
| stats count by clientip, uri_query


Detection Logic: Identifies attempts to inject system commands.


6. Conclusion

This project demonstrates a full SOC analyst workflow:

Simulated attacks (Brute Force, SQL Injection, XSS, Command Injection).

Collected and analyzed logs in Splunk.

Built custom SPL queries and dashboards for detection.

Planned extension into real-world data for greater realism.

Next Step (Phase 2): Incorporate industry-recognized attack datasets to build a more advanced SOC detection portfolio.
