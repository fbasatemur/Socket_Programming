# -*- coding: utf-8 -*-
"""
Created on Tue Nov 10 13:30:36 2020

@author: fbasatemur
"""

import sys
import requests

def download(url, filename):
    recv = requests.get(url, stream=True)
    with open(filename, 'wb') as f:
        for chunk in recv.iter_content(chunk_size=1024): 
            if chunk: 
                f.write(chunk)


try:
    # TEST LINK => "https://ak.picdn.net/shutterstock/videos/1046054536/preview/stock-footage-close-up-of-woman-s-face-girl-opening-her-beautiful-blue-azzure-eyes-attractive-ginger-natural.mp4"
    url = sys.argv[1]
    filename = sys.argv[2]
    
    
    print ("DOWNLOADING... ")
    download(url, filename)
    print ("DOWNLOADED ")
    
except:
    print ("NOT DOWNLOADED !")
