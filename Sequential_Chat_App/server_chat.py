# -*- coding: utf-8 -*-
"""
Created on Thu Oct 22 23:56:48 2020

@author: fbasatemur
"""

import socket as s


localhost="127.0.0.1"
port =1246

sd = s.socket(s.AF_INET, s.SOCK_STREAM)
sd.bind((localhost, port))
sd.listen(5)

conn, adr = sd.accept()
while True:    
    data=""
    msg=""

    while data == "":
        data = conn.recv(1024).decode('utf-8')
    
    print("+: " + data)    
    msg = input("-: ")
    
    if msg in [".", ""]:
        conn.close()
        sd.close()
        print("Connection closed")
        break
    
    conn.send(str(msg).encode('utf-8'))
    
