
import imaplib
import email
from email.header import decode_header
import time
import re
import requests
from bs4 import BeautifulSoup

# ---------------------- CONFIG ----------------------
IMAP_SERVER = "imap.gmail.com"
EMAIL_ACCOUNT = "gopisiddamsetty@gmail.com"  # ← Replace with your Gmail address
EMAIL_PASSWORD = "wdpa laqy rpyf uavw"    # ← Replace with your Gmail App Password
VIRUSTOTAL_API_KEY = "49de7eeaa064446a3a9bc36ea84eaf874be1b6154ec69a98c5ec5ddac9a944a2"  # ← Replace with your VT API Key (optional)
NUM_EMAILS_TO_CHECK = 20
# ----------------------------------------------------

def clean(text):
    return "".join(c if c.isalnum() else "_" for c in text)

def connect_to_email():
    mail = imaplib.IMAP4_SSL(IMAP_SERVER)
    mail.login(EMAIL_ACCOUNT, EMAIL_PASSWORD)
    return mail

def extract_links_from_html(html_content):
    soup = BeautifulSoup(html_content, "html.parser")
    return list(set([a['href'] for a in soup.find_all('a', href=True)]))

def decode_mime_words(s):
    if not s:
        return ""
    decoded = decode_header(s)
    return ''.join([t[0].decode(t[1]) if isinstance(t[0], bytes) else str(t[0]) for t in decoded])

def scan_virustotal(url):
    if not VIRUSTOTAL_API_KEY:
        return "VirusTotal: Skipped (No API Key)"
    headers = {"x-apikey": VIRUSTOTAL_API_KEY}
    try:
        response = requests.post(
            "https://www.virustotal.com/api/v3/urls",
            headers=headers,
            data={"url": url},
            timeout=5
        )
        if response.status_code != 200:
            return "VirusTotal: Submission Failed"

        analysis_id = response.json()['data']['id']
        analysis_url = f"https://www.virustotal.com/api/v3/analyses/{analysis_id}"

        time.sleep(5)
        result = requests.get(analysis_url, headers=headers, timeout=5)
        if result.status_code != 200:
            return "VirusTotal: Scan Failed"

        stats = result.json()['data']['attributes']['stats']
        score = stats.get('malicious', 0)
        return f"VirusTotal: {score}/90 flagged" if score else "VirusTotal: 0/90 flagged"

    except requests.exceptions.Timeout:
        return "VirusTotal: Timeout"
    except Exception:
        return "VirusTotal: Scan Failed"

def get_email_auth_headers(msg):
    auth_results = msg.get("Authentication-Results", "")
    spf = "PASS" if "spf=pass" in auth_results.lower() else "FAIL"
    dkim = "PASS" if "dkim=pass" in auth_results.lower() else "FAIL"
    dmarc = "PASS" if "dmarc=pass" in auth_results.lower() else "FAIL"
    return spf, dkim, dmarc

def process_emails():
    mail = connect_to_email()
    mail.select("inbox")
    _, message_numbers = mail.search(None, "ALL")
    messages = message_numbers[0].split()[-NUM_EMAILS_TO_CHECK:]

    for num in reversed(messages):
        _, msg_data = mail.fetch(num, "(RFC822)")
        for response_part in msg_data:
            if isinstance(response_part, tuple):
                msg = email.message_from_bytes(response_part[1])

                subject = decode_mime_words(msg["subject"])
                from_ = decode_mime_words(msg.get("From"))
                spf, dkim, dmarc = get_email_auth_headers(msg)

                print("=" * 60)
                print(f"📧 From     : {from_}")
                print(f"📝 Subject  : {subject}")
                print(f"🛡️  SPF: {spf} | DKIM: {dkim} | DMARC: {dmarc}")

                links_found = []

                if msg.is_multipart():
                    for part in msg.walk():
                        content_type = part.get_content_type()
                        if content_type == "text/html":
                            html = part.get_payload(decode=True).decode(errors="ignore")
                            links_found += extract_links_from_html(html)
                else:
                    if msg.get_content_type() == "text/html":
                        html = msg.get_payload(decode=True).decode(errors="ignore")
                        links_found += extract_links_from_html(html)

                links_found = list(set(links_found))
                if links_found:
                    print("🔗 Clean Links Found:")
                    for i, link in enumerate(links_found, start=1):
                        vt_result = scan_virustotal(link)
                        print(f"   {i}. {link}\n      🧪 {vt_result}")
                else:
                    print("🔗 No links found.")

    mail.logout()

# ---------------------- MAIN -------------------------
if __name__ == "__main__":
    try:
        process_emails()
    except KeyboardInterrupt:
        print("\n[!] Script stopped by user.")
    except imaplib.IMAP4.error as e:
        print(f"[!] Login failed: {e}")
    except Exception as e:
        print(f"[!] Error: {e}")

thsi script helps to identify the email good or bad



