# coding=utf-8
'''
Description:quick_sort
Author: yrwang
Date: 2021-07-30 14:17:27
LastEditTime: 2021-07-30 14:46:09
LastEditors: yrwang
'''


# 第一个元素的归位函数
def partition(nums, left, right):
    tmp = nums[left]
    while left < right:
        while nums[right] >= tmp and left < right:
            right -= 1
        nums[left] = nums[right]
        while nums[left] <= tmp and left < right:
            left += 1
        nums[right] = nums[left]
    nums[left] = tmp


# 快排左右两部分递归排序
def quick_sort(nums, left, right):
    if left < right:
        mid = partition(nums,left,right)
        quick_sort(nums, left, mid-1)
        quick_sort(nums, mid+1, right)


nums = [5, 7, 3, 2, 8, 9, 1, 4, 6]
# print(nums)
# partition(nums, 0, len(nums)-1)
# print(nums)
quick_sort(nums, 0, len(nums) - 1)
print(nums)
