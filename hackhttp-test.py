import hackhttp


url = 'https://www.cnvd.org.cn/'

ht = hackhttp.hackhttp()
headers = {
    'Accept': 'text/html, */*; q=0.01',
    'Accept-Encoding': 'gzip, deflate, br',
    'Accept-Language': 'zh-CN,zh;q=0.9',
    'Connection': 'keep-alive',
    'Host': 'www.cnvd.org.cn',
    'Origin': 'https://www.cnvd.org.cn',
    'Referer': 'https://www.cnvd.org.cn/',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.77 Safari/537.36',
    'X-Requested-With': 'XMLHttpRequest',
    'Cookie': '__jsluid_s=fae2f1b464dd5adeec96e18b6d7ceabf; JSESSIONID=9C6BCE1E1F41C878EBB6C71D08E132D8; __jsl_clearance_s=1627541369.638|0|vreaWqLxWNgzNz5l72lGYy47pms%3D'
}
code,head,html,redirect_url,log= ht.http(url=url,headers=headers)

print(code)
# print html
print(log)