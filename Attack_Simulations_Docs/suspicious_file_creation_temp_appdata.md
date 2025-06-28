# 🧪 Suspicious File Creation in Temp/AppData

**Purpose:**  
Detects malware or droppers writing files to Temp or AppData.

**Simulation Steps:**  
- Simulate dropper writing a `.exe` or `.dll` to `%TEMP%` or `%APPDATA%`
- Monitor file creation via Sysmon Event ID 11
- Trigger alert on suspicious file names or locations

**Screenshot:**  

