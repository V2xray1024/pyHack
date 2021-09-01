'''
Description: 
Author: yrwang
Date: 2021-07-18 15:59:40
LastEditTime: 2021-08-30 21:42:47
LastEditors: yrwang
'''
import socket

c = socket.socket()

c.connect(('192.168.215.153', 2336))

while True:
    data = input('~:')
    if not data:
        break
    c.send(data)
    if not data:
        break
    print(data)
