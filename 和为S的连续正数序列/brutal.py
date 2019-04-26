# -*- coding:utf-8 -*-
# /usr/bin/env python
# Author:   Chang
# Function: 在正数序列中求出和为s的连续子序列 暴力求解法
# Version : 1.0
# Contact : 582246340@sjtu.edu.cn

# 思路1：暴力求解法
def get_seq(nums, target):
    ans = []
    if sum(nums) < target:
        return ans
    for i in range(len(nums)):
        for j in range(i, len(nums)):
            if sum(nums[i:j]) == target:
                ans.append(nums[i:j])
    return ans


if __name__ == "__main__":
    nums = [4, 5, 4, 3, 5, 7, 7, 1, 2, 3, 2, 1, 2, 4, 5, 4, 3, 5, 7, 8, 4, 1, 4, 12]
    ans = get_seq(nums, 6)
    print(ans)
