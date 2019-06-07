# -*- coding:utf-8 -*-
# /usr/bin/env python
# Author:   Chang
# Function: 0-1背包问题
# Version : 1.0
# Contact : 582246340@sjtu.edu.cn

# 给定一组n个物品，每种物品都有自己的重量wi和价值vi，在限定的总重量C内，选择其中若干个
# 也即每种物品可以选0个或1个，设计选择方案使得物品的总价值最高。

# 典型的动态规划题目
# 定义dp(i,W)为前i件商品，总重量不超过W，时对应的最大价值。则对应的第i件商品，可选择或者不选择
# 有dp(i,W) = max(dp(i-1,W), dp(i-1,W-wi)+vi)
# 括号中第一项对应不选择第i件商品，第二项对应选择第i件商品，对应价值加vi

def package(n, weights, values, C):
    dp = [[0 for p in range(C + 1)] for q in range(n + 1)]
    for i in range(1, n + 1):
        for j in range(1, C + 1):

            dp[i][j] = dp[i - 1][j]
            # 上述递归式可以调用的前提是W>wi
            if j - weights[i - 1] > 0:
                dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - weights[i - 1]] + values[i - 1])
    return dp[n][C]


if __name__ == "__main__":
    n = 5
    c = 10
    w = [2, 2, 6, 5, 4]
    v = [6, 3, 5, 4, 6]
    print(package(n, w, v, c))
