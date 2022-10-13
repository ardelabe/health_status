#!/usr/bin/env python3

'''Use convert("RGB") method for converting RGBA to RGB image.
Size: Change image resolution from 3000x2000 to 600x400 pixel
Format: Change image format from .TIFF to .JPEG'''

from PIL import Image
import os, sys

size = 600, 400
# /home/student-01-e934fb5c3c34/supplier-data/images
path_of_the_directory = '/home/ander/Dropbox/pdf_and_email_and_other/supplier-data/images'
for infile in os.listdir(path_of_the_directory):
    # print(infile[-5:])
    if infile[-5:] == '.tiff':
        try:
            with Image.open(path_of_the_directory + '/' + infile) as im:
                # print(im.mode)
                if not im.mode == 'RGB':
                    im = im.resize(size).convert('RGB')
                im.save(path_of_the_directory + '/' + infile[:-5] + '.jpeg')
        except OSError:
            print("cannot convert", infile)
