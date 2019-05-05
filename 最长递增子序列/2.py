# -*- coding:utf-8 -*-
# /usr/bin/env python
# Author:   Chang
# Function: 最长递增子序列长度
# Version : 1.0
# Contact : 582246340@sjtu.edu.cn

# 动态规划，暴力求解法，时间复杂度为N^2
# 假设以nums[j]结尾的数组序列的最大递增子序列长度为L[j]，

def LIS(nums):
    if len(nums) == 1:
        return 1
    dp = [1 for _ in range(len(nums))]
    ans = 1
    for j in range(2, len(nums)):
        for i in range(j):
            if nums[i] < nums[j]:
                dp[j] = max(dp[j], dp[i] + 1)
        ans = max(ans, dp[j])
    return ans


if __name__ == "__main__":
    nums = [2, 1, 5, 3, 6, 4, 8, 9, 7]
    ans = LIS(nums)
    print(ans)
