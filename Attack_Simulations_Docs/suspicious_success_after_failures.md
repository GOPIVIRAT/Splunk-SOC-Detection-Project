# 🚨 Suspicious Success After Multiple Failures

# 🔍 Purpose:
This rule detects login attempts where a user fails multiple times and then successfully logs in, which can indicate a potential brute-force attack or credential guessing.

# 💡 Why This Rule is Important:
Attackers often try multiple incorrect passwords before they get it right.
If an account has many failed attempts and then suddenly logs in successfully, it's a red flag — especially if this activity happens in a short time span.

# 🧪 Simulation Steps:

Performed repeated failed logins (Event ID 4625) using brute force tools or manual attempts.

Eventually logged in successfully (Event ID 4624).

Triggered alert based on high failure count followed by success for the same user.

# 🔧 Rule Tuning :

Set threshold to 5 or more failed attempts before success to avoid false positives from users mistyping passwords.

Used mvfind(StatusList, "Success") to ensure the pattern includes both failures and success in the same window.

Filtered on Account_Name to correlate login events accurately.

This tuning helped focus only on suspicious login patterns and reduced alerts from normal user mistakes.

# 📌 MITRE Technique Mapped:

T1110 – Brute Force


**Screenshot:**  
![Image](https://github.com/user-attachments/assets/0b52a88e-1fa1-4a78-8ee9-2f596ac1e8ef) 


# ✅ Conclusion:
This rule helps detect a classic brute-force pattern — multiple failed login attempts followed by a successful one.

