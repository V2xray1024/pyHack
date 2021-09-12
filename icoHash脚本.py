'''
Description: 求网站ico文件hash的脚本
Author: yrwang
Date: 2021-09-12 10:13:40
LastEditTime: 2021-09-12 10:32:02
LastEditors: yrwang
'''
import requests
import mmh3

# requests请求ico文件地址
res = requests.get('https://www.chineseinla.com/favicon.ico')
# print(res)
favicon = res.content
hash = mmh3.hash(favicon)

print('http.favicon.hash:'+str(hash))
# 输出结果复制到shodan直接搜索即可~~
