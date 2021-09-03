'''
Description:python的zipfile模块 zipfile.ZipFile('filename')
Author: yrwang
Date: 2021-09-03 21:40:00
LastEditTime: 2021-09-03 21:52:33
LastEditors: yrwang
'''
# 导入模块，初始化
import zipfile
import sys


def zip_brute(zip_file, passwd_file):

    z = zipfile.ZipFile(zip_file)
    with open('passwd_file', 'r') as f:
        pass_list = f.readlines()
        for line in pass_list:
            try:
                # python3需要转成bytes格式
                z.extractall(pwd=bytes(line.strip(), encoding='utf-8'))
                print(f"brute successful!!! passwd is {line}")
                exit(0)
            except:
                pass
    print("your dic is too small,try an big dic!")


zip_brute(sys.argv[1], sys.argv[2])
