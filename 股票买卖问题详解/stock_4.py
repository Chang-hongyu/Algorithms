# -*- coding:utf-8 -*-
# /usr/bin/env python
# Author:   Chang
# Function: 限定交易次数最大为k 求最大利润  leetcode_188
# Version : 1.0
# Contact : 582246340@sjtu.edu.cn


# 法1 加入备忘机制的递归算法 有些测试样例会超时
def stock1(prices, k):
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


if __name__ == "__main__":
    prices = [3, 2, 6, 5, 0, 3]
    print(stock1(prices, 2))
