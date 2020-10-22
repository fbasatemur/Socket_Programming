# -*- coding: utf-8 -*-
"""
Created on Thu Oct 22 21:25:15 2020

@author: fbasatemur
"""

import socket as s


localhost="127.0.0.1"
port =1246
sd = s.socket(s.AF_INET, s.SOCK_STREAM)
sd.bind((localhost, port))
sd.listen(5)

data=""
while True:
    conn, adr = sd.accept()
    data = conn.recv(1024).decode('utf-8')
    conn.send(str(data).encode('utf-8'))
    print("incoming message forwarded")
    
print("Connection closed")
conn.close()