#!/usr/bin/env python3


import psutil
import os
from log_generator import generate_log, generate_csv


def check_status():
    cpu_usage_percent = psutil.cpu_percent(4)
    root_disk_usage_percent = psutil.disk_usage('/').percent
    memory_usage_percent = psutil.virtual_memory().percent
    is_up = psutil.net_if_stats()['lo'].isup

    return cpu_usage_percent, root_disk_usage_percent, memory_usage_percent, is_up

if __name__ == "__main__":
    cpu_usage_percent, root_disk_usage_percent, memory_usage_percent, is_up = check_status()
    generate_log('health_check', os.getpid(), 'CPU usage: {percent}%'.format(percent=cpu_usage_percent), 'health_check.log')
    generate_log('health_check', os.getpid(), 'Disk usage by root partition: {percent}%'.format(percent=root_disk_usage_percent), 'health_check.log')
    generate_log('health_check', os.getpid(), 'Memory usage {percent}%'.format(percent=memory_usage_percent), 'health_check.log')
    generate_log('health_check', os.getpid(), 'Network status is up: {boolean_value}%'.format(boolean_value=is_up), 'health_check.log')
    generate_csv(cpu_usage_percent, root_disk_usage_percent, memory_usage_percent, is_up)