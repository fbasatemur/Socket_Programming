import socket as s

visit=0
localhost="127.0.0.1"
port =1246
sd = s.socket(s.AF_INET, s.SOCK_STREAM)
sd.bind((localhost, port))
sd.listen(5)

while True:
    conn, adr = sd.accept()
    visit = visit + 1
    print(visit)
    conn.send(str(visit).encode('utf-8'))
    conn.close()
