'''
Report an error if CPU usage is over 80%
Report an error if available disk space is lower than 20%
Report an error if available memory is less than 500MB
Report an error if the hostname "localhost" cannot be resolved to "127.0.0.1"
'''

#!/usr/bin/env python3


import shutil
import psutil
import emails


def check_status():
    cpu_usage_percent = psutil.cpu_percent(4)
    root_available_space_percent = psutil.disk_usage('/').percent
    available_memory_bytes = psutil.virtual_memory().available
    net_info = psutil.net_io_counters()
    localhost_resolves = net_info.bytes_sent > 0 and net_info.bytes_recv > 0

    return cpu_usage_percent, root_available_space_percent, available_memory_bytes, localhost_resolves

def check_health(cpu_usage_percent, root_available_space_percent, available_memory_bytes, localhost_resolves):
    # cpu_usage_percent, root_available_space_percent, available_memory_bytes, localhost_resolves = check_health()
    send_mail = False
    cpu_limit = 80.0
    disk_limit = 80.0
    ram_limit = 524288000 
    if cpu_usage_percent > cpu_limit or root_available_space_percent < disk_limit or available_memory_bytes < ram_limit or localhost_resolves:
        send_mail = True
    if send_mail == True:
        table = '<table><tr><th>Case</th><th>Subject Line</th></tr><tr><td>CPU usage is over 80%</td><td>Error - CPU usage is over 80%</td></tr><tr><td>Available disk space is lower than 20%</td><td>Error - Available disk space is less than 20%</td></tr><tr><td>available memory is less than 500MB</td><td>Error - Available memory is less than 500MB</td></tr><tr><td>hostname "localhost" cannot be resolved to "127.0.0.1"</td><td>Error - localhost cannot be resolved to 127.0.0.1</td></tr></table>'
        sender = 'automation@example.com'
        recipient = 'username@example.com'
        # Replace username with the username given in the Connection Details Panel on the right hand side.
        subject = table
        body = 'Please check your system and resolve the issue as soon as possible.'
        attachment_path = '/tmp/processed.pdf/'
        return emails.generate_email(sender, recipient, subject, body, attachment_path)
    else:
        return 'Healthcheck ok - nothing to worry'


if __name__ == "__main__":
    a, b, c, d = check_status()
    print(check_health(a, b, c, d))