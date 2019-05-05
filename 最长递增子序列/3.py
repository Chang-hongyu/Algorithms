# -*- coding:utf-8 -*-
# /usr/bin/env python
# Author:   Chang
# Function: 最长递增子序列 优化方案
# Version : 1.0
# Contact : 582246340@sjtu.edu.cn

# 采用二分查找思想，优化最长递增子序列方案，时间复杂度NlogN

# 插入完毕的数组只是存储的对应长度LIS的最小末尾，有了这个末尾我们可以一个个插入数据


def binary_search(nums, target):
    left = 0
    right = len(nums) - 1
    while left <= right:
        mid = (left + right) // 2
        if nums[mid] == target:
            return mid
        elif nums[mid] > target:
            right = mid - 1
        else:
            left = mid + 1
    return left


def LIS(nums):
    if len(nums) == 1:
        return 1
    # 辅助一维数组，记录对应长度LIS的最小末尾
    tmp = [nums[0]]
    ans = 1
    for i in range(1, len(nums)):
        if nums[i] > tmp[-1]:
            tmp.append(nums[i])
            ans += 1
        # 否则，查找nums[i]应该插入的位置，将此位置的元素替换为nums[i]
        index = binary_search(tmp, nums[i])
        tmp[index] = nums[i]
    return ans


if __name__ == "__main__":
    nums = [2, 1, 5, 3, 6, 4, 8, 9, 7]
    ans = LIS(nums)
    print(ans)
