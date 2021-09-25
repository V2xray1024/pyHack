import socket

c = socket.socket()

c.connect(('192.168.215.153', 2336))

while True:
    data = input('~:')
    if not data:
        break
    c.send(data)
    print(str(c.recv(1024)))
    if not data:
        break
    print(data)
