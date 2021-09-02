'''
Description: 张三公司有300名员工，开年会抽奖，奖项如下：一等奖3名(泰国5日游)、二等奖6名(手机一部)、三等奖30名(大保健一套)。规则如下：1、共抽三次，第一次抽3等奖，第二次抽2等奖，第三次抽1等奖；2、每个员工只能中将一次
Author: yrwang
Date: 2021-08-30 21:24:21
LastEditTime: 2021-09-02 21:39:19
LastEditors: yrwang
'''

import random
# 打印员工列表
employees = []
for i in range(300):
    employees.append(f"员工{i}")

#
grade_levels = [30, 6, 3]
count = 0
while count < 3:
    choice = input(f"开始抽奖{3-count}等奖！！！！！")
    choiced_employee = random.sample(employees, grade_levels[count])
    print(choiced_employee)
    for j in choiced_employee:
        employees.remove(j)  # 删除已经中奖的员工
    count += 1
