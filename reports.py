# generate a PDF file to send to the supplier, indicating that the data was correctly processed.
# format:
'''
Processed Update on <Today's date>

[blank line]

name: Apple

weight: 500 lbs

[blank line]
'''
# report named processed.pdf
# reportlab Python library, define the method generate_report to build the PDF reports

#!/usr/bin/env python3


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
            processed_info += temp_list[0] + '<br/>' + temp_list[1] + 2 * '<br/>'
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
    path = os.getcwd() + '/supplier-data/descriptions/'
    filename = '/tmp/processed.pdf'
    today_date = date.today().strftime("%B %d, %Y")
    generate_report(filename, 'Processed Update on {date}'.format(date=today_date), process_text_data(path))
    
