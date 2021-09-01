'''
Description: 车牌摇号练习
Author: yrwang
Date: 2021-08-30 20:11:42
LastEditTime: 2021-08-30 21:21:00
LastEditors: yrwang
'''
import random
import string

count = 0
while count < 3:  # 摇号次数限制为 3次
    car_numbers = []
    for i in range(20):
        n1 = random.choice(string.ascii_uppercase)  # 车牌号第一个字母
        n2 = "".join(random.sample(string.ascii_uppercase + string.digits, 5))
        car_nums = f"京{n1}-{n2}"
        car_numbers.append(car_nums)  # 把生成的车牌号添加到列表
        print(i+1, car_nums)
    choice = input("请选择你喜欢的车牌号码：").strip()
    if choice in car_numbers:
        print(f"恭喜您选择了新车牌号：{choice}")
        exit("祝您生活愉快！")
    else:
        print("请选择存在的车牌号码！！！")
    count += 1
