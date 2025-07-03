# 🔁 Persistence via Startup Folder

# 🔍 Purpose:
This rule detects when a file is dropped or placed into the Windows Startup folder. This technique is commonly used by attackers to run malware automatically when the user logs in.

# 💡 Why This Rule is Important:
The Windows Startup folder allows programs to launch automatically on system boot or user login.
If an attacker can drop a malicious script or executable here, it runs silently every time the system starts — a classic persistence trick. This rule helps catch that early.

# 🧪 Simulation Steps:

Dropped a malicious .exe or .bat file into the following location:

C:\Users\<username>\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup
Used a script or simple copy command like:

copy evil.exe "C:\Users\DELL\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup\evil1.bat"
This activity triggered Sysmon Event ID 11 (FileCreate)

Detected and alerted via Splunk rule.

# 🔍 Splunk Rule Triggered:

[T1547] Startup Folder File Drop – Persistence


**Screenshot:**  
![Image](https://github.com/user-attachments/assets/53d1a624-e53d-43a8-97ab-02832f1ee4a5)



# ✅ Conclusion:
This rule helps detect when a malicious file is placed in the Startup folder, a well-known persistence tactic. It’s a simple but powerful way to catch early-stage attacks.

