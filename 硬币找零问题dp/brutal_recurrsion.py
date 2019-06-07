# -*- coding:utf-8 -*-
# /usr/bin/env python
# Author:   Chang
# Function: 找零钱问题
# Version : 1.0
# Contact : 582246340@sjtu.edu.cn

# 给你 k 种面值的硬币，面值分别为 c1, c2 ... ck，再给一个总金额 n，问你最少需要几枚硬币凑出这个金额，如果不可能凑出，则回答 -1 。
# 比如说，k = 3，面值分别为 1，2，5，总金额 n = 11，那么最少需要 3 枚硬币，即 11 = 5 + 5 + 1 。

# 关键在于状态转移方程
# f(n) = 0(当n为0时)   =1+min(f(n-ci)) (当n不为0时)

# 首先给出暴力递归解

def coinChange(values, total):
    """
    :param values: 代表k种面值的硬币 组成的的列表
    :param total: 持有的总金额数
    :return: 最少需要的硬币数目，若无法换零则返回-1
    """
    # k = len(values)
    if total == 0:
        return 0
    # 初始时设置硬币数目为极大值
    ans = 100
    for coin in values:
        if coin > total:
            continue
        tmp = coinChange(values, total - coin)
        if tmp == -1:
            continue
        ans = min(ans, tmp + 1)
    return ans if ans != 100 else -1


if __name__ == "__main__":
    values = [1, 2, 5]
    total = 11
    print(coinChange(values, total))
