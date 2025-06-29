# 🌐 Suspicious Network Connection (Sysmon)

**Purpose:**  
Detects abnormal outbound connections made by non-browser processes.

**Simulation Steps:**  
- Use tools like PowerShell or cmd to reach out to external IPs
- Monitor with Sysmon Event ID 3
- Alert on unusual parent processes (e.g., Excel reaching out)

**Screenshot:**  

![Image](https://github.com/user-attachments/assets/8214aba5-8989-4635-92c8-36f226106084)   
