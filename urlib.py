'''
Description: 
Author: yrwang
Date: 2021-09-01 22:17:24
LastEditTime: 2021-09-02 21:40:07
LastEditors: yrwang
'''
import urllib.request
import urllib3.request

u = urllib.request.urlopen('http://baidu.com')

print(u.read().decode('utf-8'))
