# -*- coding:utf-8 -*-
# /usr/bin/env python
# Author:   Chang
# Function: 求和为s的连续子序列 优化版本
# Version : 1.0
# Contact : 582246340@sjtu.edu.cn

# 初始化两个指针，初始值都为0，之后向右遍历，若两者和等于s，则两个指针都向右移动
# 如果子序列和大于s，则第一个指针向右移动一位；若子序列和小于s则第二个指针向右移动一位

def get_seq(nums, target):
    ans = []
    if sum(nums) < target:
        return ans
    i = 0
    j = 0
    while j < len(nums):
        if sum(nums[i:j + 1]) == target:
            ans.append(nums[i:j + 1])
            i += 1
            j += 1
        elif sum(nums[i:j + 1]) < target:
            j += 1
        else:
            if j > i:
                i += 1
            else:
                i += 1
                j += 1
    return ans


if __name__ == "__main__":
    nums = [4, 5, 4, 3, 5, 7, 7, 1, 2, 3, 2, 1, 2, 4, 5, 4, 3, 5, 7, 8, 4, 1, 4, 12]
    ans = get_seq(nums, 6)
    print(ans)
