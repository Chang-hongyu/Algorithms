# -*- coding:utf-8 -*-
# /usr/bin/env python
# Author:   Chang
# Function: 硬币找零 带备忘录的递归算法
# Version : 1.0
# Contact : 582246340@sjtu.edu.cn

def coinChange(values, total):
    """
    带备忘录的递归算法
    :param values: k种不同面值的硬币列表
    :param total: 金额总额
    :return: 最少硬币个数，无法找零返回-1
    """
    # 备忘录初始化为-2
    memo = [-2 for _ in range(total + 1)]
    return helper(values, total, memo)


def helper(values, num, memo):
    """
    :param values: k种不同面值的硬币列表
    :param num: 需要查找的总额
    :param memo: 备忘录 初始化为-2
    :return: 总额num对应的最小找零数
    """
    if num == 0:
        return 0
    if memo[num] != -2:
        return memo[num]
    ans = 100
    for coin in values:
        if coin > num:
            continue
        tmp = helper(values, num - coin, memo)
        if tmp == -1:
            continue
        ans = min(ans, 1 + tmp)

    # 记录本轮答案
    memo[num] = ans if ans != 100 else -1
    return memo[num]


if __name__ == "__main__":
    values = [1, 2, 5]
    total = 12
    print(coinChange(values, total))
