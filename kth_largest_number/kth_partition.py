# -*- coding:utf-8 -*-
# /usr/bin/env python
# Author:   Chang
# Function: 利用快速排序的思想来求第k大的数
# Version : 1.0
# Contact : 582246340@sjtu.edu.cn

# 快速排序每次把一个元素交换到正确的位置，同时可以左边都放上大的，右边都放上小的，排序之后，查看枢纽元位置q。

# 如果枢纽元位置等于k-1，说明找到这个元素；如果大于k-1，说明要求出前一个序列第k大的数。

# 如果枢纽元位置小于k-1，说明要求出后一个序列中第k-q大的元素，算法每次折半，时间复杂度为O(N)。

# 空间复杂度也为O(N)，对于很大的数据不太合适

import random


def quickSort(A, l, r):
    if l < r:
        p = partition(A, l, r)
        quickSort(A, l, p - 1)
        quickSort(A, p + 1, r)


def partition(A, l, r):
    x = A[r]
    i = l - 1
    for j in range(l, r):
        if A[j] >= x:
            i += 1
            A[i], A[j] = A[j], A[i]
    A[i + 1], A[r] = A[r], A[i + 1]
    return i + 1


def findKthLargest(A, l, r, k):
    pos = partition(A, l, r)
    if pos == l + k - 1:
        return A[pos]
    if pos > l + k - 1:
        return findKthLargest(A, l, pos - 1, k)
    else:
        return findKthLargest(A, pos + 1, r, k - (pos - l + 1))


if __name__ == "__main__":
    # 创建数组A,元素不重复
    A = []
    random.seed(1234)
    while len(A) < 5000:
        tmp = random.randint(1, 100000)
        if tmp not in A:
            A.append(tmp)

    k = 12
    ans = findKthLargest(A, 0, len(A) - 1, k)
    quickSort(A, 0, len(A) - 1)
    print(A)
    print(A[k - 1])
    print(ans)
