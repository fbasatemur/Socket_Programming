import socket as s

localhost = "127.0.0.1"
port = 1246
sd = s.socket(s.AF_INET, s.SOCK_STREAM)
sd.connect((localhost, port))
while True:
    data = sd.recv(1024).decode('utf-8')
    if not data:
        break
    print(data)
sd.close()