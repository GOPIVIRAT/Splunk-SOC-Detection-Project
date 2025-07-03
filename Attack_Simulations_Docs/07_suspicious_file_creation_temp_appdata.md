# 🧪 Suspicious File Creation in Temp/AppData

# 🔍 Purpose:
This rule detects when suspicious files are created inside temporary directories like C:\Temp, %TEMP%, or %AppData%\Local\Temp. These locations are often abused by malware during execution or staging.

# 💡 Why This Rule is Important:
Attackers and malware commonly use Temp folders to drop payloads before execution, because these directories often have write permissions and are less monitored.
This rule helps identify suspicious activity by watching for new file creation in these high-risk paths.

# 🧪 Simulation Steps:

Created a fake malware file in the Temp folder:

echo "powershell malware simulation" > C:\Users\DELL\AppData\Local\Temp\_PSScriptPolicyTest_4sdj5fcx.25g.ps1

This triggered Sysmon Event ID 11 (FileCreate)

The rule was designed to detect file creation in paths containing:

\Temp\

\AppData\Local\Temp\

\Windows\Temp\

# 🔍 Splunk Rule Triggered:

[T1059,T1204] Suspicious File Creation – Temp Directory


**Screenshot:**  
![Image](https://github.com/user-attachments/assets/f8c012fb-ecee-4cf6-9d9f-e8e68fa2c28c) 

# ✅ Conclusion:
This rule helps detect when malware or scripts try to create files in temporary locations, which is often a step in malware unpacking or execution. Catching it early can stop payload execution.
