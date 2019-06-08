# -*- coding:utf-8 -*-
# /usr/bin/env python
# Author:   Chang
# Function: 限定最大交易次数为2次，leetcode_123
# Version : 1.0
# Contact : 582246340@sjtu.edu.cn


# 法1 二维数组动态规划
def stock1(prices):
    # loc[i][j]代表第i天卖出，且经历j次交易的最大利润
    # glo[i][j]代表前i天，经历j次交易的最大利润
    if len(prices) <= 1:
        return 0
    loc = [[0, 0, 0] for _ in range(len(prices))]
    glo = [[0, 0, 0] for _ in range(len(prices))]
    for i in range(len(prices) - 1):
        # diff表示后一天和前一天价格的差值
        diff = prices[i + 1] - prices[i]
        for j in range(2):
            # loc[i+1][j+1]对应前i天j次交易的最大值，加上这一天价格差和0的最大值 或者
            # 第i天卖出经历j+1次交易的最大利润，加上这两天之间的价格差
            loc[i + 1][j + 1] = max(glo[i][j] + max(0, diff), loc[i][j + 1] + diff)
            # 前i天经历j次交易的最大利润，对应第i+1天卖出 和前i天交易j+1次的最大利润之间的最大值
            glo[i + 1][j + 1] = max(loc[i + 1][j + 1], glo[i][j + 1])
    return glo[-1][-1]


# 法2 参考第二题中加入备忘机制的递归算法
def stock2(prices, k):
    # 限制两次交易，将k设置为2即可 时间复杂度为O(k*n^2)
    # 不知道备忘录有多大，故直接使用字典，必要时向字典中添加元素
    memo = dict()

    def dp(start, k):
        if start >= len(prices):
            return 0
        if k == 0:
            return 0
        # 若存在于字典中，直接使用避免重复计算
        if (start, k) in memo:
            return memo[(start, k)]

        ans = 0
        cur_min = prices[start]
        for sell in range(start + 1, len(prices)):
            cur_min = min(cur_min, prices[sell])
            # 在递归调用中，将交易次数减少1
            ans = max(ans, dp(sell + 1, k - 1) + prices[sell] - cur_min)
        # 将相应的答案储存到字典中
        memo[(start, k)] = ans
        return ans

    return dp(0, k)


# 法3 通用方法 状态机
def stock3(prices):
    n = len(prices)
    dp_i10 = 0
    dp_i11 = float('-inf')
    dp_i20 = 0
    dp_i21 = float('-inf')
    for i in range(n):
        dp_i20 = max(dp_i20, dp_i21 + prices[i])
        dp_i21 = max(dp_i21, dp_i10 - prices[i])
        dp_i10 = max(dp_i10, dp_i11 + prices[i])
        dp_i11 = max(dp_i11, -prices[i])
    return dp_i20


if __name__ == "__main__":
    prices = [3, 3, 5, 0, 0, 3, 1, 4]
    print(stock1(prices))
    print(stock2(prices, 2))
    print(stock3(prices))
