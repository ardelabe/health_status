#!/usr/bin/env python3


import os, sys
from datetime import date
import reports


if __name__ == "__main__":
    path = os.getcwd() + '/supplier-data/descriptions/'
    filename = '/tmp/processed.pdf'
    today_date = date.today().strftime("%B %d, %Y")
    reports.generate_report(filename, 'Processed Update on {date}'.format(date=today_date), reports.process_text_data(path))