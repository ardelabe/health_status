#!/usr/bin/env python3


import csv
import os




# f = open(path + '/health_check.csv')
# csv_f = csv.reader(f)
# for row in csv_f:
#     print(row)
# f.close()

def csv_to_list():
    path = os.getcwd() + '/log' + '/health_check.csv'
    list_of_logs = []
    with open(path, newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            list_of_logs.append(row)
    return list_of_logs


def settings_to_list():
    path = os.getcwd() + '/settings.csv'
    list_of_settings = []
    with open(path, newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            list_of_settings.append(row)
    return list_of_settings


def check_last_log(list_of_logs):
    last_row = list_of_logs[len(list_of_logs) - 1]
    

if __name__ == "__main__":
    # print(csv_to_list())
    # check_last_log(csv_to_list())
    print(settings_to_list())