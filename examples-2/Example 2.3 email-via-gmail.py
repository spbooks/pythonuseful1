#!/usr/bin/env python3

import smtplib
from email.mime.text import MIMEText

# Set your own Gmail details here.
# The username should be the part before @gmail.com.
GMAIL_USERNAME = "mygmailaccount12345"
# The password is the App Password you generated from https://myaccount.google.com/apppasswords
GMAIL_APP_PASSWORD = "yxyloqscucpxdsxq"

# The text of the message
email_text = f"""
Hi! This is the report from your script.

I have added 1 + 2 and I got the answer {1+2}.

Bye!
"""
# A list of recipients. This can be your own address.
# This should always be a list, even if there's only one entry.
recipients = ["sil@kryogenix.org"]

# Create the message from the message text
msg = MIMEText(email_text)
msg["Subject"] = "Email report: a simple sum"
msg["To"] = ", ".join(recipients)
# It's being sent from your Gmail account, so we know the From address.
msg["From"] = f"{GMAIL_USERNAME}@gmail.com"

# Now use smtplib to actually send the email
smtp_server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
# Log in using your specified username and password
smtp_server.login(GMAIL_USERNAME, GMAIL_APP_PASSWORD)
# And send the email
smtp_server.sendmail(msg["From"], recipients, msg.as_string())
smtp_server.quit()
