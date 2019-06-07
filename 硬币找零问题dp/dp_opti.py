# -*- coding:utf-8 -*-
# /usr/bin/env python
# Author:   Chang
# Function: 找零钱问题优化过之后的动态规划解法
# Version : 1.0
# Contact : 582246340@sjtu.edu.cn

def coinChange(values, total):
    # 构造dp table
    dp = [100 for i in range(total + 1)]
    dp[0] = 0
    for i in range(1, total + 1):
        for coin in values:
            # 当前面值比当前要求的总金额还大
            if coin > i:
                continue
            dp[i] = min(dp[i], 1 + dp[i - coin])
    return dp[total] if dp[total] < 100 else -1


if __name__ == "__main__":
    values = [1, 2, 5]
    total = 12
    print(coinChange(values, total))
