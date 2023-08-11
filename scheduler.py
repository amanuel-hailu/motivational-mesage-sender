from send_message import send_mms_via_email
from datetime import datetime
from time import sleep
import random


def schedule_reminder(number, message, phone_provider, sender_credentials, subject, file_path="", run_now=False):
    if run_now:
        send_mms_via_email(
            number, message, file_path, "image", "jpeg", phone_provider, sender_credentials, subject)
        print("Run now!")
        return

    while True:
        current_time = datetime.now().time()
        if current_time.hour == 13:  # Check if it's 1 pm
            # Random minute between 1 pm and 2 pm
            random_minutes = random.randint(0, 59)
            sleep(random_minutes * 60)  # Wait for the random minute
            # Based on send_type, send the message

            send_mms_via_email(
                number, message, file_path, "image", "jpeg", phone_provider, sender_credentials, subject)
            print("MMS Reminder sent!")

            sleep((59 - random_minutes) * 60 + 3600)  # Wait until next 1 pm
        sleep(60)  # Check every minute
