import argparse
import os
from scheduler import schedule_reminder
from dotenv import load_dotenv

load_dotenv()

# Example command: python main.py --send-type sms


def main():
    parser = argparse.ArgumentParser(description='Schedule study reminders.')
    # parser.add_argument('--run-now', action='store_true',
    #                     help='Send the notification immediately.')
    # parse argument for send_type and --run-now
    parser.add_argument('--run-now', action='store_true',
                        help='Send the notification immediately.')

    # parse the arguments
    args = parser.parse_args()
    run_now = args.run_now

    number = os.getenv("RECIPIENT_PHONE_NUMBER")
    phone_provider = "T-Mobile"
    email = os.getenv("EMAIL_USERNAME")
    password = os.getenv("EMAIL_PASSWORD")
    sender_credentials = (email, password)
    subject = "PLkjkEAST!"
    message = "Hey, it's time to study! Don't forget to focus on your goals."
    file_path = "pic.jpg"

    schedule_reminder(number, message, phone_provider,
                      sender_credentials, subject, file_path, run_now)


if __name__ == "__main__":
    main()
