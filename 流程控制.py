'''
Description: python 流程控制练习
Author: yrwang
Date: 2021-08-30 18:25:59
LastEditTime: 2021-08-30 19:54:08
LastEditors: yrwang
'''
# 单分支/双分支
age = int(input("your age is:"))
if age < 25:
    print("you are a little boy!")
else:
    print("you are old boy!")

# 多分支
'''
if
elif
else
'''
girl_age = 30
count = 0 
while count<3:
    count += 1
    your_guess = int(input("输入你的猜测："))
    if your_guess > girl_age:
        print("老娘永远18岁！")
    elif your_guess < girl_age:
        print("小嘴真甜！")
    else:
        print("看人真准！")
        break
# 练习 打印成绩
while 1:
    grade = int(input("请输入成绩："))
    if 90 <= grade and grade <= 100:
        print("你的成绩等级为：A!")
    elif 80 <= grade and grade < 90:
        print("你的成绩等级为：B!")
    elif 80 <= grade and grade < 90:
        print("你的成绩等级为：B!")
    elif 60 <= grade and grade < 80:
        print("你的成绩等级为：C!")
    elif 40 <= grade and grade < 60:
        print("你的成绩等级为：D!")
    else:
        print("你的成绩等级为：E!")
