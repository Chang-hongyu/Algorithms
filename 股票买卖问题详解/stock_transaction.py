# -*- coding:utf-8 -*-
# /usr/bin/env python
# Author:   Chang
# Function: 每次交易手续费为fee，可以进行尽可能多的交易，求最大利润  leetcode_714
# Version : 1.0
# Contact : 582246340@sjtu.edu.cn


# 法1 加备忘机制的递归方案修改 时间复杂度为O(n^2)
def stock1(prices, fee):
    """
    :param prices: 价格列表 可以进行尽可能多的交易
    :param fee: 每次交易的手续费
    :return: 最大利润
    """
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
            cur_min = min(cur_min, prices[sell])
            ans = max(ans, dp(sell + 1) + prices[sell] - cur_min - fee)
        memo[start] = ans
        return ans

    return dp(0)


# 法2：通用方法 状态机
def stock2(prices, fee):
    n = len(prices)
    dp_i_0 = 0
    dp_i_1 = float('-inf')
    for i in range(n):
        tmp = dp_i_0
        dp_i_0 = max(dp_i_0, dp_i_1 + prices[i] - fee)
        dp_i_1 = max(dp_i_1, tmp - prices[i])
    return dp_i_0


# 法3：同上，对手续费的处理放在买入时
def stock3(prices, fee):
    n = len(prices)
    dp_i_0 = 0
    dp_i_1 = float('-inf')
    for i in range(n):
        tmp = dp_i_0
        dp_i_0 = max(dp_i_0, dp_i_1 + prices[i])
        dp_i_1 = max(dp_i_1, tmp - prices[i] - fee)
    return dp_i_0


if __name__ == "__main__":
    prices = [1, 3, 2, 8, 4, 9]
    print(stock1(prices, 2))
    print(stock2(prices, 2))
    print(stock3(prices, 2))
