#!/usr/bin/env python3


import os, sys
from datetime import date
import reports, emails


if __name__ == "__main__":
    path = os.getcwd() + '/supplier-data/descriptions/'
    filename = '/tmp/processed.pdf'
    today_date = date.today().strftime("%B %d, %Y")
    reports.generate_report(filename, 'Processed Update on {date}'.format(date=today_date), reports.process_text_data(path))
    sender = 'automation@example.com'
    recipient = 'username@example.com'
    # Replace username with the username given in the Connection Details Panel on the right hand side.
    subject = 'Upload Completed - Online Fruit Store'
    body = 'All fruits are uploaded to our website successfully. A detailed list is attached to this email.'
    attachment_path = '/tmp/processed.pdf/'
    # message = emails.generate_email(sender, recipient, subject, body, attachment_path)
    # emails.send_email(message)
    message = emails.generate_email(sender, recipient, subject, body, '/tmp/processed.pdf')
    print(message)
    emails.send_email(message)