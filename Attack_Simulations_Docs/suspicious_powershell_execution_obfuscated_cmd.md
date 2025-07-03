# 🧩 Suspicious Obfuscated PowerShell Execution

# 🔍 Purpose:
This rule detects suspicious PowerShell command-line activities such as encoded payloads, use of Invoke-Expression (IEX), policy bypass flags, and downloading scripts from the internet using Net.WebClient.

# 💡 Why This Rule is Important:
PowerShell is frequently used by attackers due to its versatility and trust by the system.
Malicious actors use obfuscation, in-memory execution, and network-based payload delivery through PowerShell — making it a high-value telemetry source for SOC teams.

# 🧪 Simulation Steps:

Base64 encoded PowerShell payload using -EncodedCommand

Remote script execution using IEX and Net.WebClient

Executed all commands from a terminal or script to simulate attacker behavior.

These actions generated Sysmon Event ID 1 (Process Creation)

# 🔧 Rule Tuning to Reduce Noise:

To reduce false positives and improve accuracy:

Focused only on risky PowerShell keywords like -EncodedCommand, IEX, bypass, and webclient.

Ignored normal admin or system scripts that commonly use PowerShell for safe automation.

Used lower() to make keyword matching case-insensitive.

Grouped detections by type (Base64, Invoke-Expression, etc.) to help triage faster.

# Screenshot: 

![Image](https://github.com/user-attachments/assets/3f595a7c-a676-4b50-8a6f-4e9a271b2453)  

