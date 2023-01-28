import imghdr
import os
import smtplib
from email.message import EmailMessage

EMAIL_PASSWORD = os.getenv("GMAIL_APP_PASSWORD")
SENDER = "gammasynchrony2@gmail.com"
RECEIVER = "gammasynchrony2@gmail.com"

email_message = EmailMessage()
email_message['Subject'] = "Cat Provisions Update"
email_message.set_content("Update: See Attached")

def send_email(image_path):
    with open(image_path, "rb") as file:
        content = file.read()

    email_message.add_attachment(content,
                                 maintype="image",
                                 subtype=imghdr.what(None, content))

    gmail = smtplib.SMTP("smtp.gmail.com", 587)
    gmail.ehlo()
    gmail.starttls()
    gmail.login(SENDER, EMAIL_PASSWORD)
    gmail.sendmail(SENDER, RECEIVER, email_message.as_string())
    gmail.quit()

if __name__ == "__main__":
    send_email("../test_image.png")