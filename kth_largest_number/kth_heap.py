# -*- coding:utf-8 -*-
# /usr/bin/env python
# Author:   Chang
# Function: 使用堆排序的思想求第k大的数
# Version : 1.0
# Contact : 582246340@sjtu.edu.cn

# 优点在于空间复杂度的降低到O(k)，时间复杂度近似nlg(k)

# 维护一个k大小的最小堆，对于数组中的每一个元素判断与堆顶的大小，若堆顶较大，则不管。

# 否则弹出堆顶，将当前值插入到堆中，继续调整最小堆。

import random


def Parent(i):
    return (i - 1) // 2


def Left(i):
    return 2 * i + 1


def Right(i):
    return 2 * i + 2


def minHeapify(A, i, size):
    # 以下三个量均表示索引
    lchild = Left(i)
    rchild = Right(i)
    smallest = i
    # 确保根节点有两个子节点
    if i < size // 2:
        if lchild < size and A[lchild] < A[smallest]:
            smallest = lchild
        if rchild < size and A[rchild] < A[smallest]:
            smallest = rchild
        if smallest != i:
            A[i], A[smallest] = A[smallest], A[i]
            # 注意此处smallest的位置并没有改变
            minHeapify(A, smallest, size)


def buildMinHeap(A, size):
    for i in range(size // 2)[::-1]:
        minHeapify(A, i, size)


def heapSort(A):
    size = len(A)
    buildMinHeap(A, size)
    for i in range(1, size)[::-1]:
        A[0], A[i] = A[i], A[0]
        minHeapify(A, 0, i)


def findKthLargest(A, k):
    if k > len(A):
        return False
    heap = A[:k]
    buildMinHeap(heap, k)
    for i in range(k, len(A)):
        if A[i] > heap[0]:
            heap[0] = A[i]
            minHeapify(heap, 0, k)
    return heap[0]


if __name__ == "__main__":
    # 创建数组A,元素不重复
    A = []
    random.seed(1234)
    while len(A) < 500:
        tmp = random.randint(1, 10000)
        if tmp not in A:
            A.append(tmp)
    print(A)

    k = 12
    ans = findKthLargest(A, k)

    heapSort(A)
    print(A)

    print(A[k - 1])
    print(ans)
