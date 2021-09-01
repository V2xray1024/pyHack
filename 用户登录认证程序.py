
'''
Description: 要求用户输入账号密码进行登录、用户账号信息保存在文件内、用户密码输错三次后锁定用户，下次再登录，检测到是这个已经被锁定的用户，则不允许登录，提示被锁
Author: yrwang
Date: 2021-09-01 21:09:38
LastEditTime: 2021-09-01 21:43:08
LastEditors: yrwang
'''
'''
1.确定在文件里(account.db)用户账号密码存放的结构
2.把账户数据读到内存
account = {
  "wyr":["wyr","123456","1"]
  ...
  ...
}
3.循环，要求用户输入账号密码，加判断
'''
accounts = {}
f = open("account.db", "r")
for line in f:
    line = line.strip().split(",")
    accounts[line[0]] = line
print(accounts)


while 1:
    username = input("Username:").strip()
    if username not in accounts:
        print("用户未注册.....")
        continue
    elif accounts[username][2] == "1":
        print("{username}被锁定，请联系管理员")
        continue
    count = 0
    while count < 3:
        passwd = input("Password:").strip()
        if passwd == accounts[username][1]:
            print(f"用户{username}登录成功！！！")
            exit("bye.....")
        else:
            print("错误的用户名或密码！！！")
        count += 1
    if count == 3:
        print(f"{username}输错3次密码，已被锁定！")
        accounts[username][2] = "1"
        f2 = open("account.db", "w")
        for username, value in accounts.items():
            line = ",".join(value) + "\n"
            f.write(line)
        f2.close()
        exit("bye........")
