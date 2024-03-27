"""
To send email we first need email address.
and make sure to that google account has "Less secure app access" turned on
we can find this option under "Security" section
and Just try it on.
"""

import smtplib
from email.message import EmailMessage


# first we need to write, which email is sending and which email is going to receive it.
sender = "test@gmail.com"
receiver = "test76@gmail.com"



msg = EmailMessage()
msg['Subject'] = 'Hello from Python'
msg['From'] = sender
msg['To'] = receiver
msg.set_content('Test email sent from a Python script.')

# use SMTP to send the email
with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
    smtp.login(sender, 'test-pass')
    smtp.send_message(msg)
