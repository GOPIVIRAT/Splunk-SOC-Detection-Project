import imaplib
import email
import requests
import re
import html
from email import policy
from email.header import decode_header
from email.parser import BytesParser

# === Configuration ===
IMAP_SERVER = "imap.gmail.com"
EMAIL_ACCOUNT = "gopisiddamsetty@gmail.com"
EMAIL_PASSWORD = "wdpa laqy rpyf uavw"
VIRUSTOTAL_API_KEY = "49de7eeaa064446a3a9bc36ea84eaf874be1b6154ec69a98c5ec5ddac9a944a2"

def connect_to_email():
    mail = imaplib.IMAP4_SSL(IMAP_SERVER)
    mail.login(EMAIL_ACCOUNT ,EMAIL_PASSWORD)
    mail.select("inbox")
    return mail



def decode_subject(subject_raw):
    decoded = decode_header(subject_raw)
    subject = ""
    for part, enc in decoded:
        if isinstance(part, bytes):
            try:
                subject += part.decode(enc or 'utf-8', errors='ignore')
            except:
                subject += part.decode(errors='ignore')
        else:
            subject += part
    return subject.strip()

def clean_urls(text):
    text = html.unescape(text)  # Remove HTML entities like &#39;
    return re.findall(r'https?://[^\s\'"<>]+', text)

def scan_attachment(file_data, filename):
    url = "https://www.virustotal.com/api/v3/files"
    headers = {"x-apikey": VIRUSTOTAL_API_KEY}
    files = {"file": (filename, file_data)}
    response = requests.post(url, headers=headers, files=files)
    if response.status_code == 200:
        return response.json()
    return {"error": "Failed to scan"}

def check_email_security(headers):
    auth_results = headers.get("Authentication-Results", "")
    spf_pass = "spf=pass" in auth_results.lower()
    dkim_pass = "dkim=pass" in auth_results.lower()
    dmarc_pass = "dmarc=pass" in auth_results.lower()
    return spf_pass, dkim_pass, dmarc_pass

def process_emails():
    mail = connect_to_email()
    result, data = mail.search(None, "UNSEEN")
    email_ids = data[0].split()

    for eid in email_ids:
        result, msg_data = mail.fetch(eid, "(RFC822)")
        raw_email = msg_data[0][1]
        msg = BytesParser(policy=policy.default).parsebytes(raw_email)

        from_addr = msg["From"]
        subject = decode_subject(msg["Subject"] or "(No Subject)")
        spf, dkim, dmarc = check_email_security(msg)

        print("=" * 70)
        print(f"📧 From     : {from_addr}")
        print(f"📝 Subject  : {subject}")
        print(f"🛡️  SPF: {'PASS' if spf else 'FAIL'} | DKIM: {'PASS' if dkim else 'FAIL'} | DMARC: {'PASS' if dmarc else 'FAIL'}")

        # === Extract Links
        urls_found = []
        for part in msg.walk():
            if part.get_content_type() in ["text/plain", "text/html"]:
                try:
                    payload = part.get_payload(decode=True).decode(errors="ignore")
                    urls_found += clean_urls(payload)
                except:
                    continue

        if urls_found:
            print("🔗 Links:")
            for i, url in enumerate(urls_found[:5], 1):  # Show max 5 links
                print(f"   {i}. {url[:100]}{'...' if len(url) > 100 else ''}")
        else:
            print("🔗 Links: None Found")

        # === Scan Attachments
        for part in msg.walk():
            if part.get_content_disposition() == "attachment":
                filename = part.get_filename()
                file_data = part.get_payload(decode=True)
                print(f"📎 Attachment: {filename} (scanning...)")
                scan_result = scan_attachment(file_data, filename)
                if "data" in scan_result:
                    vt_id = scan_result['data'].get('id', 'N/A')
                    print(f"   🔍 VT Scan ID: {vt_id}")
                else:
                    print("   ❌ Failed to scan attachment.")

    mail.logout()

# === Run
if __name__ == "__main__":
    process_emails()
