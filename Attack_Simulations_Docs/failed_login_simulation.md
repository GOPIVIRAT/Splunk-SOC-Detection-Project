# 🔐 Failed Login Attempt

**Purpose:**  
Detects repeated failed login attempts (Event ID 4625) indicating possible brute force.

**Simulation Steps:**  
- Attempt login with wrong password 5+ times using the same account (`DELL`)
- Monitor Windows Security logs for Event ID 4625
- Validate trigger on Splunk

**Screenshot:**  

![Image](https://github.com/user-attachments/assets/eba15de0-384a-4f3b-9047-5ba9ec3e32cc)
