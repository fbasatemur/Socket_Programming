# -*- coding: utf-8 -*-
"""
Created on Thu Oct 22 23:55:59 2020

@author: fbasatemur
"""

import socket as s

localhost = "127.0.0.1"
port = 1246

sd = s.socket(s.AF_INET, s.SOCK_STREAM)
sd.connect((localhost, port))

while True:
    data=""
    msg=""
    
    msg = input("-: ")
    if msg in [".", ""]:
        sd.close()
        print("Connection closed")
        break
    
    else:
        sd.send(str(msg).encode('utf-8'))
        while data == "":    
            data = sd.recv(1024).decode('utf-8')
            
        print("+: " + data)
    
