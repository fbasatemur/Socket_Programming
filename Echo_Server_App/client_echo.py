# -*- coding: utf-8 -*-
"""
Created on Thu Oct 22 21:18:28 2020

@author: fbasatemur
"""
 
import socket as s

localhost = "127.0.0.1"
port = 1246

msg = input("Message:")

sd = s.socket(s.AF_INET, s.SOCK_STREAM)
sd.connect((localhost, port))

data=""

if not msg:
    print("Message is empty")

else:
    sd.send(str(msg).encode('utf-8'))
    data = sd.recv(1024).decode('utf-8')

    print(data)

sd.close()
    