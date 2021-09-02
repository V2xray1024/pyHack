'''
Description: 
Author: yrwang
Date: 2021-08-04 15:29:23
LastEditTime: 2021-09-02 21:39:27
LastEditors: yrwang
'''

import requests
from requests import status_codes


def getHtml(url, headers):
    res = requests.get(url, headers=headers)
    res.encoding = res.status_code
    return res.text, res.status_code


url = 'http://111.200.241.244:61531/'
headers = {
    'X-Forwarded-For': '123.123.123.123',
    'referer': 'https://www.google.com'
}
print(getHtml(url, headers).encode('utf-8'))
