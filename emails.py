'''
parameters to emails.generate_email():
    From: automation@example.com
    To: username@example.com
    Replace username with the username given in the Connection Details Panel on the right hand side.
    Subject line: Upload Completed - Online Fruit Store
    E-mail Body: All fruits are uploaded to our website successfully. A detailed list is attached to this email.
    Attachment: Attach the path to the file processed.pdf
'''



#!/usr/bin/env python3


import email.message
import mimetypes
import os.path
import smtplib


def generate_email(sender, recipient, subject, body, attachment_path=''):
    
    # Basic Email formatting
    message = email.message.EmailMessage()
    message["From"] = sender
    message["To"] = recipient
    message["Subject"] = subject
    message.set_content(body)

    # Process the attachment and add it to the email
    if os.path.exists(attachment_path):
        attachment_filename = os.path.basename(attachment_path)
        mime_type, _ = mimetypes.guess_type(attachment_path)
        mime_type, mime_subtype = mime_type.split('/', 1)
        with open(attachment_path, 'rb') as ap:
            message.add_attachment(ap.read(),
                maintype=mime_type,
                subtype=mime_subtype,
                filename=attachment_filename)

    return message


def send_email(message):
  """Sends the message to the configured SMTP server."""
  mail_server = smtplib.SMTP('localhost')
  mail_server.send_message(message)
  mail_server.quit()


if __name__ == "__main__":
    sender = 'automation@example.com'
    recipient = 'username@example.com'
    # Replace username with the username given in the Connection Details Panel on the right hand side.
    subject = 'Upload Completed - Online Fruit Store'
    body = 'All fruits are uploaded to our website successfully. A detailed list is attached to this email.'
    attachment_path = '/tmp/processed.pdf/'
    print(generate_email(sender, recipient, subject, body, attachment_path))
    