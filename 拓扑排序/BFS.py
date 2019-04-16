# -*- coding:utf-8 -*-
# /usr/bin/env python
# Author:   Chang
# Function: 利用宽度优先搜索，判断有向图中是否存在环
# Version : 1.0
# Contact : 582246340@sjtu.edu.cn

# LeetCode 207

# 时间复杂度O(N^2)，空间复杂度O(N)

# 每次选择入度为0的节点，作为序列的下一个节点，然后移除该节点和 从节点出发的所有的边

import collections


def canFinish(numCourses, prerequisites):
    graph = collections.defaultdict(list)
    indegrees = collections.defaultdict(int)

    for u, v in prerequisites:
        # graph[v]记录v的出点
        graph[v].append(u)
        # indegrees[u]记录u的入度
        indegrees[u] += 1

    for i in range(numCourses):
        zeroDegree = False
        for j in range(numCourses):
            # 找到入度为0的点，跳出，进行后续处理
            if indegrees[j] == 0:
                zeroDegree = True
                break
        # 若找不到入度为0的点，说明为有向无环图
        if not zeroDegree:
            return False
        # 将入度为0的节点入度设置为-1，并且将其指向的节点入度减1
        indegrees[j] = -1
        for node in graph[j]:
            indegrees[node] -= 1
    # n次循环结束，都有找到入度为0的节点，说明没有环
    return True
