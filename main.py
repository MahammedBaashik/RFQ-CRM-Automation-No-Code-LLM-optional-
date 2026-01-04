from email_parser import load_email
from extractor import extract_fields
from sheets_writer import write_to_sheet
from crm_mock import create_opportunity
from notifier import send_internal_alert
from auto_reply import generate_reply

email = load_email("data/incoming_email.txt")
data = extract_fields(email)

write_to_sheet(data)
opportunity = create_opportunity(data)

reply_en = generate_reply(data, "en")
reply_ar = generate_reply(data, "ar")

open("outputs/auto_reply_en.txt", "w").write(reply_en)
open("outputs/auto_reply_ar.txt", "w").write(reply_ar)

send_internal_alert(data)

print("✅ RFQ processed successfully")
