'''
Description: 循环练习
Author: yrwang
Date: 2021-08-30 19:19:41
LastEditTime: 2021-08-30 20:10:50
LastEditors: yrwang
'''
# 1 打印1-100的奇偶数
for i in range(100):
    if i % 2 == 0:
        print(f"{i} 是偶数")
# 2 循环打印楼层 循环嵌套
for i in range(1, 6):
    print(f"----------第{i}层----------")
    for j in range(10):
        print(f"L{i}-{i}0{j}")
# 3 break&continue
for i in range(1, 6):
    if i == 3:
        continue
    print(f"----------第{i}层----------")
    for j in range(10):
        if i == 4 and j == 4:
            print("遇到鬼了！game over!")
            break
        print(f"L{i}-{i}0{j}")
# 4 打印三角形练习
for i in range(10):
    if i <= 5:
        print("*"*i)
    else:
        print((10-i) * "*")
# 5 while循环 9x9乘法表
for i in range(1, 10):
    for j in range(1, i+1):
        print(f"{i}x{j}={i*j}", end=' ',)
    print()
