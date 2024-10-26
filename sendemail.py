from postmark import PMMail
import os
from dotenv import find_dotenv, load_dotenv

dotenv_path = find_dotenv()
load_dotenv(dotenv_path)

POSTMARK_API = os.getenv("POSTMARK_API")

def send_email_postmark(sender_email, recipient_email, subject, body):
    try:
        # Create a new PMMail object
        email = PMMail(
            api_key=POSTMARK_API,  # Your Postmark API key
            sender=sender_email,  # Your verified sender email
            to=recipient_email,  # Recipient's email address
            subject=subject,  # Email subject
            text_body=body  # Email body
        )
        
        # Send the email
        email.send()
        print("Email sent successfully.")
    except Exception as e:
        print(f"Failed to send email: {e}")

# Example usage
sender_email = "szhou390@gatech.edu"  # Replace with your verified sender email
recipient_email = "szhou390@gatech.edu"  # Replace with recipient email
subject = "Test Email from Postmark"
body = "This is a test email sent using Postmark API."
send_email_postmark(sender_email, recipient_email, subject, body)
