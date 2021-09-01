import urllib.request
import urllib3.request

u = urllib.request.urlopen('http://baidu.com')

print(u.read().decode('utf-8'))
