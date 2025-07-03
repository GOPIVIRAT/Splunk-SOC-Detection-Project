# 🌐 Suspicious Network Connection (Sysmon)

# 🔍 Purpose:
This rule detects suspicious or abnormal external outbound connections from processes or locations that typically shouldn’t communicate with the internet.

# 💡 Why This Rule is Important:
Malware often tries to connect to Command & Control (C2) servers, exfiltrate data, or download more payloads.
This rule helps detect such behavior — especially when non-browser or unknown apps make outbound connections on high-risk ports.

# 🧪 Simulation Steps:

Simulated an outbound connection using a non-standard application (e.g. wpscloudsvr.exe)

Connection went to an external IP address using port 443

This activity triggered Windows Event ID 3 (Network Connection) via Sysmon

# ⚙️ Tuning the Rule to Reduce Noise (Very Important):

To reduce false positives from legitimate apps like browsers or collaboration tools (Zoom, Edge, Teams, etc.), I added filters:

Ignored processes like chrome, firefox, zoom, edge, etc.

Allowed IP ranges for internal/private networks (e.g. 192.168.0.0/16, 172.16.0.0/12)

Filtered known safe ports with unusual behavior from Temp folders or AppData

✅ This tuning ensures that the rule focuses on high-risk connections, reducing noise while maintaining visibility into suspicious behavior.


# 📌 MITRE Techniques Mapped:

T1071.001 – Application Layer Protocol: Web (HTTP/S)

T1046 – Network Service Scanning (if probing external services)

T1105 – Ingress Tool Transfer (if downloading payloads)




**Screenshot:**  

![Image](https://github.com/user-attachments/assets/8214aba5-8989-4635-92c8-36f226106084)  


# ✅ Conclusion:
This rule helps detect potentially malicious outbound connections from unusual file locations or processes. With added filtering and tuning, it reduces noise and focuses on truly suspicious behavior — helping analysts stay alert without alert fatigue. 
