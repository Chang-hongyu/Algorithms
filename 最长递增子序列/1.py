# -*- coding:utf-8 -*-
# /usr/bin/env python
# Author:   Chang
# Function: 最长递增子序列
# Version : 1.0
# Contact : 582246340@sjtu.edu.cn

# 先将数组排序，之后求原始数组和排序后数组的最长公共子序列
# N^2时间空间复杂度，原址排序
def quickSort(nums, start, end):
    if start < end:
        mid = partition(nums, start, end)
        quickSort(nums, start, mid - 1)
        quickSort(nums, mid + 1, end)


def partition(nums, start, end):
    pivot = nums[end]
    i = start - 1
    for j in range(start, end):
        if nums[j] <= pivot:
            i += 1
            nums[i], nums[j] = nums[j], nums[i]
    nums[i + 1], nums[end] = nums[end], nums[i + 1]
    return i + 1


def LCS(nums1, nums2):
    m = len(nums1)
    n = len(nums2)
    # 记录最长公共子序列长度的矩阵
    dp = [[0 for j in range(n + 1)] for i in range(m + 1)]
    for i in range(m):
        for j in range(n):
            if nums1[i] == nums2[j]:
                dp[i + 1][j + 1] = dp[i][j] + 1
            else:
                dp[i + 1][j + 1] = max(dp[i + 1][j], dp[i][j + 1])
    return dp[-1][-1]


if __name__ == "__main__":
    nums = [2, 1, 5, 3, 6, 4, 8, 9, 7]
    nums1 = [2, 1, 5, 3, 6, 4, 8, 9, 7]
    quickSort(nums, 0, len(nums) - 1)
    lis = LCS(nums, nums1)
    print(lis)
