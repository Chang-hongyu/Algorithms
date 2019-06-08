# -*- coding:utf-8 -*-
# /usr/bin/env python
# Author:   Chang
# Function: 允许买卖无数次 求最大利润  leetcode_122
# Version : 1.0
# Contact : 582246340@sjtu.edu.cn


# 法1：最简单的思路 贪心算法 只要后面比前面价格大，就将价格差加上
def stock1(prices):
    """
    核心思想是：既然可以预知未来，那么能赚一点就赚一点
    :param prices: 价格列表
    :return: 不限买卖次数 最大利润值
    """
    if len(prices) <= 1:
        return 0
    ans = 0
    for i in range(1, len(prices)):
        ans += max(0, prices[i] - prices[i - 1])
    return ans


# 法2 注意递归思想 stock2(prices)对应prices列表的情况下，不限买卖次数时的最大利润，要充分利用这一点
def stock2(prices):
    if len(prices) <= 1:
        return 0
    ans = 0
    # 对于选定的buy和sell，最大利润时将这次买卖最大利润和剩余最大利润加起来
    # 注意对于遍历到的buy和sell，也可以选择不买卖，但是这样的情况在后面双重循环中会查找到，所以不做处理
    for buy in range(len(prices)):
        for sell in range(buy + 1, len(prices)):
            ans = max(ans, stock2(prices[sell + 1:]) + prices[sell] - prices[buy])
    return ans


# 法3：根据解法2的递归，此递归有重叠子问题，我们加入备忘机制，消除一个循环来减小时间复杂度
# 所有的题目都可以修改此框架而得，但是可能无法通过所有测试样例
def stock3(prices):
    if len(prices) <= 1:
        return 0
    memo = [-1 for _ in range(len(prices))]

    # dp[start]表示的是本问题针对prices[start:]的解
    def dp(start):
        if start >= len(prices):
            return 0
        # 若备忘录中有本次计算的结果，则直接返回，不再重复计算
        if memo[start] != -1:
            return memo[start]
        ans = 0
        cur_min = prices[start]
        for sell in range(start + 1, len(prices)):
            # 理解：若cur_min等于prices[sell]，说明之前的都大于等于prices[sell]，那么售出不会有额外利润
            # 此处和解法2中不同，注意本题没有对所有buy日进行遍历，所以要选择当前卖或者不卖
            # 所以加入了cur_min来对当前的选择进行了处理，prices[sell]-cur_min==0时相当于不进行此次买卖
            cur_min = min(cur_min, prices[sell])
            # 额外利润体现在下一行中
            ans = max(ans, dp(sell + 1) + prices[sell] - cur_min)
        # 在备忘录中记录这一结果
        memo[start] = ans
        return ans

    return dp(0)


if __name__ == "__main__":
    prices = [7, 1, 5, 3, 6, 4]
    print(stock1(prices))
    print(stock2(prices))
    print(stock3(prices))
