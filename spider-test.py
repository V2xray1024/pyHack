import re
import requests

url = 'https://bbs.ichunqiu.com/portal.php'
# print r.status_code
# print r.content
# headers == bypass
headers = {
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.77 Safari/537.36'
}
r = requests.get(url=url,headers=headers)

names = re.findall('style="color: #555555;">(.*?)</a>',r.content)

for n in names:
    print(n)
