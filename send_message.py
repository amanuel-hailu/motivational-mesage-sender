import smtplib
import ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders
from os.path import basename
from providers import PROVIDERS


def send_mms_via_email(numbers, message, file_path, mime_maintype, mime_subtype, provider, sender_credentials, subject="", smtp_server="smtp.gmail.com", smtp_port=465):
    sender_email, email_password = sender_credentials

    with smtplib.SMTP_SSL(smtp_server, smtp_port, context=ssl.create_default_context()) as email:
        email.login(sender_email, email_password)
        numbers = [
            "5713312357",
            "5713312054",
            "2406186282"
        ]
        for number in numbers:
            receiver_email = f'{number}@{PROVIDERS.get(provider).get("sms")}'

            email_message = MIMEMultipart()
            email_message["Subject"] = subject
            email_message["From"] = sender_email
            email_message["To"] = receiver_email

            email_message.attach(MIMEText(message, "plain"))

            with open(file_path, "rb") as attachment:
                part = MIMEBase(mime_maintype, mime_subtype)
                part.set_payload(attachment.read())

                encoders.encode_base64(part)
                part.add_header(
                    "Content-Disposition",
                    f"attachment; filename={basename(file_path)}",
                )

                email_message.attach(part)

            text = email_message.as_string()

            try:
                email.sendmail(sender_email, receiver_email, text)
                print(f"Message sent to {number}")
            except Exception as e:
                print(f"Failed to send message to {number}: {str(e)}")
