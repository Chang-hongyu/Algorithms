# -*- coding:utf-8 -*-
# Author:   Chang
# Function: 求出最长公共子序列，并且打印出路径
# Version : 1.0
# Contact : 582246340@sjtu.edu.cn

# 序列X共有m个元素，序列Y共有n个元素
# 若X[m-1]==Y[n-1] 那么X[:m]和Y[:n]的最长公共子序列就是X[:m-1]和Y[n-1]的最长公共子序列的长度加1
# 若X[m-1]!=Y[n-1] 那么X[:m]和Y[:n]的最长公共子序列长度就是X[:m-1]和Y[:n]的最长公共子序列的长度、
# 与X[:m]和Y[:n-1]的最长公共子序列 之间的最大值


def LCS_len(X, Y):
    m = len(X)
    n = len(Y)
    # 记录最长公共子序列长度的矩阵
    dp = [[0 for j in range(n + 1)] for i in range(m + 1)]
    # 记录方向的矩阵
    flag = [[0 for j in range(n + 1)] for i in range(m + 1)]

    for i in range(m):
        for j in range(n):
            if X[i] == Y[j]:
                dp[i + 1][j + 1] = dp[i][j] + 1
                flag[i + 1][j + 1] = 'OK'
            # 对应j变化，i不变化
            elif dp[i + 1][j] > dp[i][j + 1]:
                dp[i + 1][j + 1] = dp[i + 1][j]
                flag[i + 1][j + 1] = 'LE'
            else:
                dp[i + 1][j + 1] = dp[i][j + 1]
                flag[i + 1][j + 1] = 'UP'
    return dp, flag


def printLCS(flag, X, i, j):
    if i == 0 or j == 0:
        return
    if flag[i][j] == 'OK':
        printLCS(flag, X, i - 1, j - 1)
        print(X[i - 1], end="")
    elif flag[i][j] == 'LE':
        printLCS(flag, X, i, j - 1)
    else:
        printLCS(flag, X, i - 1, j)


if __name__ == "__main__":
    X = "ABCBDAB"
    Y = "BDCABA"
    dp, flag = LCS_len(X, Y)

    print("记录最大长度输出:")
    for i in dp:
        print(i)
    print("")

    print("位置变换记录输出:")
    for j in flag:
        print(j)
    print("")

    printLCS(flag, X, len(X), len(Y))
    print("")
    print("最长公共子序列的长度为:", dp[-1][-1])
