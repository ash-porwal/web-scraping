"""
To send email we first need email address.
and make sure to that google account has "Less secure app access" turned on
we can find this option under "Security" section
and Just try it on.
"""
import smtplib, ssl
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email import encoders

# first we need to write, which email is sending and which email is going to receive it.
sender = "viratg76@gmail.com"
receiver = "viratg76@gmail.com"

# now we need to write message which we want to send
msg = MIMEMultipart() # this starts creationg of the message
msg["Subject"] = "Testing automation mail"
msg["FROM"] = sender
msg["To"] = ','.join(receiver) # , just in case if we provided multiple receiver

part = MIMEBase("application", "octet-stream")
part.set_payload("testing automation from Python")
# part.set_payload(open("path/to/file", "rb").read()) # in case you want to open a file
encoders.encode_base64(part)
part.add_header("Content-Disposition", "attachment; filename='test.csv'")
msg.attach(part)