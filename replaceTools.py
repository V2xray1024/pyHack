'''
Description: 命令格式如 python script.py old_str new_str filename
             对指定文件内容进行全局替换，并且替换完后打印替换了多少处内容
Author: yrwang
Date: 2021-09-01 18:03:12
LastEditTime: 2021-09-02 21:39:50
LastEditors: yrwang
'''

import sys

# print(sys.argv)
old_str = sys.argv[1]
new_str = sys.argv[2]
filename = sys.argv[3]

# 1 读取文件
f = open(filename, "r+")
data = f.read()
# 2 计算并替换
old_str_count = data.count(old_str)
new_data = data.replace(old_str, new_str)
# 3 清空
f.seek(0)
f.truncate()
# 4 保存新数据
f.write(new_data)

print(f"成功替换了{old_str}为{new_str},一共{old_str_count}处....")
