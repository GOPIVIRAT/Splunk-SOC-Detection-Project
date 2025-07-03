# Remote Threat Detection Rule

# 🔍 Purpose:
This rule detects remote process injection attempts into sensitive or high-value system processes like lsass.exe, winlogon.exe, or explorer.exe, which attackers often target for credential theft, privilege escalation, or user session hijacking.

# 💡 Why This Rule is Important:
Remote or local code injection is a powerful technique used by advanced attackers and malware to hide malicious execution inside legitimate processes.
By monitoring key target processes, you can catch early signs of advanced persistence or credential dumping activity — especially important in post-exploitation stages.

# 🧪 Simulation Steps:

Simulated process injection using tools like Mimikatz, Cobalt Strike, or custom PowerShell payloads.

Targeted processes like:

lsass.exe (for credential dumping)

explorer.exe (for session hijacking)

winlogon.exe (for persistence)

Detected via Sysmon Event ID 8 (Process Access - memory injection)

# 🔧 Rule Tuning :

Focused only on high-value target processes (lsass.exe, explorer.exe, winlogon.exe) while ignoring common benign injections into processes like services.exe.

Normalized process names to lowercase using lower() to catch all variations.

Categorized the type of injection based on the target process (Credential Theft, User Hijacking, etc.).

Ignored frequent safe injections that could generate noise, such as those from svchost or services.exe.

This tuning helped reduce false positives while catching stealthy and high-impact attacks.


# 📌 MITRE Techniques Mapped:

T1055 – Process Injection

T1055.001 – Dynamic-link Library Injection

**Screenshot:**  
![Image](https://github.com/user-attachments/assets/1c2c760e-b4bf-4c81-833e-d76d9dbb7e19) 

# ✅ Conclusion:
This rule is designed to catch advanced attacker behavior, especially in post-compromise scenarios.
By monitoring process injections into sensitive targets and reducing noise from normal OS behavior, it gives SOC analysts a focused and high-fidelity alert that can stop credential theft or stealthy persistence early.

