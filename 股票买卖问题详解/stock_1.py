# -*- coding:utf-8 -*-
# /usr/bin/env python
# Author:   Chang
# Function: 允许买买一次 求最大利润 leetcode_121
# Version : 1.0
# Contact : 582246340@sjtu.edu.cn

# 对于本题 有多种解法，每个题目最后一种解法是状态机解法
# 状态机解法是复杂度最低的，但是不好理解，我们有详细的推导

# 解法1 给定初始买入日，对后面所有售出日遍历，求解最大利润
def stock1(prices):
    """
    对应时间复杂度为O(n2)
    :param prices: 对应股票当日的售价
    :return: 最大利润值
    """
    if len(prices) <= 1:
        return 0
    ans = 0
    for buy in range(len(prices) - 1):
        for sell in range(buy + 1, len(prices)):
            ans = max(ans, prices[sell] - prices[buy])
    return ans


# 解法2 固定卖出时间，向前穷举寻找买入日，寻找prices[buy]最小的那天，可以简化运算
def stock2(prices):
    """
    本方法的时间复杂度为O(n)，因为简化了cur_min的计算
    :param prices: 价格列表
    :return: 最大利润
    """
    if len(prices) <= 1:
        return 0
    ans = 0
    # 记录售出日之前位置 最小的元素
    cur_min = prices[0]
    for sell in range(1, len(prices)):
        # 更新sell日期之前的价格的最小值，注意包含sell这一天和不包含这一天都可以
        cur_min = min(cur_min, prices[sell])
        ans = max(ans, prices[sell] - cur_min)
        # 也可以这样反过来写
        # ans = max(ans, prices[sell] - cur_min)
        # cur_min = min(cur_min, prices[sell])
    return ans


# 解法3 前后两日相减，形成长度为n-1的价格差列表，之后求最大连续子数组 时间复杂度也为O(n)
def stock3(prices):
    if len(prices) <= 1:
        return 0
    diff = []
    for i in range(1, len(prices)):
        diff.append(prices[i] - prices[i - 1])
    # 价格差列表的长度
    n = len(diff)
    ans = 0
    # 动态规划求最大连续子数组
    max_sum = diff[0]
    pre_sum = diff[0]
    for j in range(1, n):
        pre_sum = max(pre_sum + diff[j], diff[j])
        max_sum = max(max_sum, pre_sum)
    ans = max(0, max_sum)
    return ans


def stock4(prices):


if __name__ == "__main__":
    prices = [7, 1, 5, 3, 6, 4]
    print(stock1(prices))
    print(stock2(prices))
    print(stock3(prices))
