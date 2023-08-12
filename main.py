import argparse
import os
import logging
import random
from services.quote_service import get_random_quote
from services.image_service import fetch_image
from scheduler.schedule import schedule_reminder
from dotenv import load_dotenv

load_dotenv()

logging.basicConfig(level=logging.INFO)


def parse_arguments():
    parser = argparse.ArgumentParser(description='Schedule study reminders.')
    parser.add_argument('--run-now', action='store_true',
                        help='Send the notification immediately.')
    return parser.parse_args()


def main():
    args = parse_arguments()
    run_now = args.run_now

    number = os.getenv("RECIPIENT_PHONE_NUMBER")
    email = os.getenv("EMAIL_USERNAME")
    password = os.getenv("EMAIL_PASSWORD")
    phone_provider = "T-Mobile"
    sender_credentials = (email, password)
    # Get a random subject from the list
    subjects = ["You can do it!", "You got this!",
                "Keep going!", "Don't give up!", "Go get 'em!", "Eye on the prize!", "Stay focused!", "Stay strong!", "Stay motivated!", "Stay positive!", "Stay hungry!", "Stay humble!", "Stay curious!", "Stay passionate!", "Stay committed!", "Stay consistent!", "Stay disciplined!", "Stay persistent!", "Stay patient!", "Stay healthy!", "Stay happy!", "Stay grateful!", "Stay inspired!", "Stay creative!", "Stay confident!", "Stay fearless!", "Stay honest!", "Stay humble!", "Stay kind!", "Stay motivated!", "Stay positive!", "Stay strong!"]
    subject = random.choice(subjects)
    if not all([number, email, password]):
        logging.error(
            "Required environment variables are missing. Please check the configuration.")
        return

    # get quote
    quote, author = get_random_quote()
    message = f"{quote} - {author}"

    # fetch image
    image_result = fetch_image()
    if not image_result['success']:
        logging.error(f"Failed to fetch image: {image_result.get('error')}")
        return

    file_path = os.path.join("images", "downloaded_image.jpg")

    schedule_reminder(number, message, phone_provider,
                      sender_credentials, subject, file_path, run_now)

    logging.info("Reminder scheduled successfully.")


if __name__ == "__main__":
    main()
