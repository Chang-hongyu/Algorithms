# -*- coding:utf-8 -*-
# /usr/bin/env python
# Author:   Chang
# Function: 加入一天冷却期的股票交易 可以完成多次交易  leetcode_309
# Version : 1.0
# Contact : 582246340@sjtu.edu.cn


# 卖出股票之后的第一天不能买入，必须隔一天才能下一次买进股票
# 法1：加入备忘机制的递归 第二题代码增加一些处理 时间复杂度O(n^2)

def stock1(prices):
    if len(prices) <= 1:
        return 0
    memo = [-1 for _ in range(len(prices))]

    def dp(start):
        if start >= len(prices):
            return 0
        if memo[start] != -1:
            return memo[start]
        ans = 0
        cur_min = prices[start]
        for sell in range(start + 1, len(prices)):
            # 保证本次操作无利润时可以不交易
            cur_min = min(cur_min, prices[sell])
            ans = max(ans, dp(sell + 2) + prices[sell] - cur_min)
        memo[start] = ans
        return ans

    return dp(0)


if __name__ == "__main__":
    prices = [1, 2, 3, 0, 2]
    print(stock1(prices))
