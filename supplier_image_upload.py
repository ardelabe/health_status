'''use the Python requests module to send the file contents 
to the [linux-instance-IP-Address]/upload URL.
takes the jpeg images from the supplier-data/images'''


#!/usr/bin/env python3
import requests
import os


path_of_the_directory= '/home/student-01-e934fb5c3c34/supplier-data/images'
for filename in os.listdir(path_of_the_directory):
    f = os.path.join(path_of_the_directory,filename)
    if os.path.isfile(f) and f[-5:] == '.jpeg':
        print(f)
        url = "http://localhost/upload/"
        with open(f, 'rb') as opened:
            r = requests.post(url, files={'file': opened})




	
