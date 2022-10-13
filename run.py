'''
Python script that will automatically POST the fruit images and their respective description in JSON format.
process the text files (001.txt, 003.txt ...) from the supplier-data/descriptions directory. The script 
should turn the data into a JSON dictionary by adding all the required fields, including the image associated with the fruit (image_name), and uploading it to http://[linux-instance-external-IP]/fruits using the Python requests library.
'''


#! /usr/bin/env python3


import os
import requests


# TODO process files into JSON
# {"name": "Test Fruit", "weight": 100, "description": "This is the description of my test fruit", "image_name": "icon.sheet.png"}
# weight field is defined as an integer field.
list_of_dicts = []
path = os.getcwd() + '/supplier-data/descriptions/'
# print(path)
for infile in os.listdir(path):
    print(infile)
    with open(path + infile) as file:
        temp_list = file.readlines()
        temp_dict = {
            'name': temp_list[0].strip(), 
            'weight': int(temp_list[1].strip().split()[0]), 
            'description': temp_list[2].strip(), 
            'image_name': infile[:3] + '.jpeg'
        } 
        list_of_dicts.append(temp_dict)
# for dict in list_of_dicts:
#     print(dict)


# TODO Iterate over all the fruits and POST 
url = "http://35.232.157.111/fruits/"
for dict in list_of_dicts:
    response = requests.post(url, json=dict)
