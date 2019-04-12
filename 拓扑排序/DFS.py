# -*- coding:utf-8 -*-
# /usr/bin/env python
# Author:   Chang
# Function: 深度优先搜索 判断有向图中是否存在环
# Version : 1.0
# Contact : 582246340@sjtu.edu.cn

# 时间复杂度O(N),空间复杂度O(N)

# 我们每次找到一个节点，判断从这个节点出发是否有环

# 具体做法是使用一个visited数组，当visited[i]值为0，说明还没有判断这个点，visited[1]值为1说明当前的循环正在判断这个点

# 当visited[i]的值为2，说明已经判断过这个点，含义是从这个点往后的所有路径都没有环，认为这个点是安全的

# 我们对每个点出发都做这个判断，检查这个点出发的所有路径上是否有环，如果判断过程中找到当前的正在判断的路径，说明有环

# 若找到判断正常的点，说明往后都不可能存在环，认为当前的节点也是安全的

# 如果当前点是未知状态，那么先把当前点标记成为正在访问状态，然后找后续的节点，知道找到安全的节点为止。

# 如果最后到达了无路可走的状态，说明当前节点是安全的。


import collections


def canFinish(numCourses, prerequisites):
    graph = collections.defaultdict(list)
    for u, v in prerequisites:
        # graph[v]表示v的出节点列表
        graph[v].append(u)

    # 记录各个节点状态的数组
    visited = [0 for _ in range(numCourses)]
    for i in range(numCourses):
        if not dfs(graph, visited, i):
            return False
    return True

# 判断是否节点是否安全，即该节点出发的路径是否无环
def dfs(graph, visited, i):
    if visited[i] == 1:
        return False
    if visited[i] == 2:
        return True
    visited[i] = 1
    for j in graph[i]:
        if not dfs(graph, visited, j):
            return False
    visited[i] = 2
    return True
