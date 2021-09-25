'''
Description: 
Author: yrwang
Date: 2021-07-18 18:01:51
LastEditTime: 2021-09-02 21:39:01
LastEditors: yrwang
'''
# 端口扫描工具
import socket
import sys

# 待扫描端口号 //自行配置常用端口
port = [21, 22, 23, 35, 80, 149, 445, 1433, 1521, 3306, 3389]


# 探测端口是否开放
def open(ip, port):
    s = socket.socket()
    try:
        s.connect((ip, port))
        return True
    except:
        return False


# 扫描结果
def scan_port(ip):
    for x in port:
        if open(ip, x):
            print('%s host %s open' % (ip, x))
        else:
            print('%s host %s close' % (ip, x))


def scan_port_range(ip):
    for x in range(s, e):
        if open(ip, x):
            print('%s host %s open' % (ip, x))
        # else:
        #     print('%s host %s close' % (ip, x))


try:
    # 使用sys库的argv函数做使用帮助
    if len(sys.argv) < 2:
        print('''
        This Program prints files to standard output.
        Any number of files can be specified.
        Options include:
            python portScan.py host ports
            python portScan.py 127.0.0.1 80,1433,3306,3389
            python portScan.py 127.0.0.1 80-90
            python portScan.py 127.0.0.1 all
        ''')
    # 加ip参数扫描
    if len(sys.argv) == 2:
        scan_port(sys.argv[1])
    # 加ip端口扫描
    elif len(sys.argv) == 3:
        # 端口参数为','分割
        if ',' in sys.argv[2]:
            p = sys.argv[2]
            p = p.split(',')
            for x in p:
                a = []
                a.append(int(x))
                port = a
                scan_port(sys.argv[1])
        # 端口为区间80-90
        elif '-' in sys.argv[2]:
            q = sys.argv[2]
            q = q.split('-')
            s = int(q[0])
            e = int(q[1])
            scan_port_range(sys.argv[1])
        # 端口参数为' all '
        elif 'all' == sys.argv[2]:
            s = 1
            e = 65535
            scan_port_range(sys.argv[1])
except KeyboardInterrupt:
    print("=" * 50)
    print("=" * 18 + "program end" + "=" * 18)
    print("=" * 50)

# 使用端口扫描工具
# scan_port('127.0.0.1')
