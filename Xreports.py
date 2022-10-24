#!/usr/bin/env python3

''' 
this code should: 
1.1. read health_check.csv and save a .txt with the necessary info to create a report
1.2. read health_check.csv and save a pdf report
2. read .txt and create a report
'''
from reportlab.platypus import SimpleDocTemplate
from reportlab.platypus import Paragraph, Spacer, Table, Image
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib import colors
import os, sys
from datetime import date

def process_text_data(path_to_file):
    processed_info = ''
    for infile in os.listdir(path_to_file):
        # print(infile)
        with open(path_to_file + infile) as file:
            temp_list = file.readlines()
            processed_info += 'name: ' + temp_list[0] + '<br/>' + 'weight: ' + temp_list[1] + 2 * '<br/>'
    print(processed_info)
    return processed_info

def generate_report(filename, title, additional_info):
    styles = getSampleStyleSheet()
    report = SimpleDocTemplate(filename)
    report_title = Paragraph(title, styles["h1"])
    report_info = Paragraph(additional_info, styles["BodyText"])
    empty_line = Spacer(1,20)
    report.build([report_title, empty_line, report_info, empty_line])


if __name__ == "__main__":
    # path = os.getcwd() + '/log/'
    # filename = '/tmp/processed.pdf'
    # today_date = date.today().strftime("%B %d, %Y")
    # generate_report(filename, 'Processed Update on {date}'.format(date=today_date), process_text_data(path))
    
