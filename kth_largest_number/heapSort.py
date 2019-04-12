# -*- coding:utf-8 -*-
# /usr/bin/env python
# Author:   Chang
# Function: 
# Version : 1.0
# Contact : 582246340@sjtu.edu.cn

# 保持堆的性质，是对最大堆进行操作的重要子程序。输入一个数组A和一个下标i，以及放在堆中元素个数

# 当maxHeapify被调用时，假定left[i]和right[i]为根的两棵二叉树都是最大堆，A[i]在最大堆中下降以维持最大堆。

# 从元素A[i],A[left],A[right]中找出最大的，并将其下标存在largest中，如果A[i]是最大的，那么已经是最大堆，结束。

# 否则i的某个子节点中有最大元素，则交换A[i]和A[largest]，从而使i及其子女满足堆性质。对孩子树递归调用maxHeapify。

# 之后是建立最大堆，对于i<size//2，进行最大堆性质的维护，因为大于等于size//2的节点都是子节点，不用维护最大堆性质

# 最后进行堆排序，将A[0]和A[size-1]交换，并且维持最大堆性质。可以在原址进行堆排序


def Left(i):
    return 2 * i + 1


def Right(i):
    return 2 * i + 2


def maxHeapify(A, i, size):
    # 以下三个量均表示索引
    lchild = Left(i)
    rchild = Right(i)
    largest = i
    # 确保根节点有两个子节点
    if i < size // 2:
        if lchild < size and A[lchild] > A[largest]:
            largest = lchild
        if rchild < size and A[rchild] > A[largest]:
            largest = rchild
        if largest != i:
            A[i], A[largest] = A[largest], A[i]
            maxHeapify(A, largest, size)


def buildMaxHeap(A, size):
    for i in range(size // 2)[::-1]:
        maxHeapify(A, i, size)


def heapSort(A):
    size = len(A)
    buildMaxHeap(A, size)
    for i in range(1, size)[::-1]:
        A[0], A[i] = A[i], A[0]
        maxHeapify(A, 0, i)


if __name__ == "__main__":
    A = [12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
    heapSort(A)
    print(A)
