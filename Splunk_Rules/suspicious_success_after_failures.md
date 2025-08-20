# 📌 Title: Suspicious Login – Success After Multiple Failures
# 📝 Description: Detects successful login (EventCode 4624) following 5 or more failed attempts (EventCode 4625) for the same account. This may indicate successful brute-force or password-guessing.
# 🧠 MITRE ATT&CK Technique: T1110 – Brute Force
# 🏷️ Tags: authentication, failed_logins, brute_force, EventCode_4625, EventCode_4624, windows_security
# 👨‍💻 Author: Siddamsetty Gopi

index=* host="DESKTOP-UKJ4CF3" source="WinEventLog:Security" (EventCode=4625 OR EventCode=4624)
| eval LoginStatus=if(EventCode==4625, "Failed", "Success")
| stats count(eval(LoginStatus="Failed")) as FailedCount,
        values(LoginStatus) as StatusList,
        latest(_time) as LastEventTime
        by Account_Name
| where FailedCount >= 5 AND mvfind(StatusList, "Success") >= 0
| eval LastLoginTime = strftime(LastEventTime, "%Y-%m-%d %H:%M:%S")
| table Account_Name, FailedCount, StatusList, LastLoginTime
| sort -LastLoginTime

# 🧾 Explanation:

#### 🛠️ How it Works:
- Looks for both **failed (4625)** and **successful (4624)** login attempts.
- Tracks failed attempts per account (`FailedCount`).
- Flags if:
  - A success login happens **after 5+ failures**.
- Converts time to readable format.

#### ✅ Why It’s Useful:
- Helps detect **brute-force attacks that succeeded**.
- Common pattern: attacker tries multiple passwords until one works.
- Adds visibility into **successful compromise** — not just attempts.

#### 👨‍💻 Analyst Tip:
Correlate this alert with:
- **Source IP or hostname**  
- **Login time (e.g., unusual hours)**  
- **New geographic locations**

Escalate quickly if the login came from an **unknown or external IP** or if followed by suspicious actions like privilege escalation.
